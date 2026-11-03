import Foundation

public struct Library: Sendable {
    public let subjects: [Subject]
    public let formatVersion: Int

    private let aliasIndex: [String: String]
    private let aliases: [(String, String)]

    public init(subjects: [Subject], formatVersion: Int = 1) throws {
        var seenIDs = Set<String>()
        var index: [String: String] = [:]
        var pairs: [(String, String)] = []
        for subject in subjects {
            if subject.id.isEmpty {
                throw LibraryError.invalid("A drawing is missing an id.")
            }
            if !seenIDs.insert(subject.id).inserted {
                throw LibraryError.invalid("Two drawings share the id \(subject.id).")
            }
            if subject.steps.count < 3 {
                throw LibraryError.invalid("\(subject.title) needs at least 3 steps.")
            }
            let names = [subject.id, subject.title] + subject.words
            var local = Set<String>()
            for name in names {
                let key = normalizeQuery(name)
                guard !key.isEmpty else { continue }
                if !local.insert(key).inserted { continue }
                if let other = index[key], other != subject.id {
                    throw LibraryError.invalid("The word \"\(key)\" is used by both \(other) and \(subject.id).")
                }
                index[key] = subject.id
                pairs.append((key, subject.id))
            }
        }
        self.subjects = subjects
        self.formatVersion = formatVersion
        self.aliasIndex = index
        self.aliases = pairs
    }

    public static func load(from data: Data) throws -> Library {
        let decoder = JSONDecoder()
        let file: BookFile
        do {
            file = try decoder.decode(BookFile.self, from: data)
        } catch {
            throw LibraryError.invalid("The drawing file is not valid JSON.")
        }
        if file.formatVersion != 1 {
            throw LibraryError.invalid("This app reads drawing format 1.")
        }
        var subjects: [Subject] = []
        subjects.reserveCapacity(file.subjects.count)
        for entry in file.subjects {
            subjects.append(try entry.makeSubject())
        }
        return try Library(subjects: subjects, formatVersion: file.formatVersion)
    }

    public func subject(id: String) -> Subject? {
        subjects.first { $0.id == id }
    }

    public func subjects(in category: Category) -> [Subject] {
        subjects.filter { $0.category == category }
    }

    public func match(_ raw: String) -> QueryOutcome {
        let normalized = normalizeQuery(raw)
        if normalized.isEmpty {
            return .choices(
                message: "Type a word first, or tap Surprise me.",
                subjects: suggestions(seed: "empty")
            )
        }
        if let greeting = greetingMessage(for: normalized) {
            return .choices(message: greeting, subjects: suggestions(seed: normalized))
        }
        if let outcome = resolve(normalized) {
            return outcome
        }
        let stripped = stripStopwords(normalized)
        if stripped != normalized, let outcome = resolve(stripped) {
            return outcome
        }
        let squashed = stripped.replacingOccurrences(of: " ", with: "")
        if squashed != stripped, let id = aliasIndex[squashed], let subject = subject(id: id) {
            return .subject(subject)
        }
        return tryAnother(seed: normalized)
    }

    public func browseMatches(prefix raw: String, limit: Int = 6) -> [Subject] {
        let query = normalizeQuery(raw)
        guard query.count >= 1, !isBlockedWord(query) else { return [] }
        var found: [Subject] = []
        var seen = Set<String>()
        let ranked = aliases.sorted { lhs, rhs in
            if lhs.0.count != rhs.0.count { return lhs.0.count < rhs.0.count }
            return lhs.0 < rhs.0
        }
        for (alias, id) in ranked {
            guard alias == query || (query.count >= 2 && alias.hasPrefix(query)) else { continue }
            guard seen.insert(id).inserted, let subject = subject(id: id) else { continue }
            found.append(subject)
            if found.count == limit { break }
        }
        return found
    }

    public func suggestions(seed: String, count: Int = 3, excluding: Set<String> = []) -> [Subject] {
        var generator = SplitMix64(seed: stableHash(seed))
        var pool = subjects.filter { !excluding.contains($0.id) }
        if pool.isEmpty { pool = subjects }
        pool.shuffle(using: &generator)
        var picked: [Subject] = []
        var used = Set<Category>()
        for subject in pool where !used.contains(subject.category) {
            picked.append(subject)
            used.insert(subject.category)
            if picked.count == count { return picked }
        }
        for subject in pool where !picked.contains(where: { $0.id == subject.id }) {
            picked.append(subject)
            if picked.count == count { break }
        }
        return picked
    }

    public func surprise(excluding id: String? = nil, rng: inout some RandomNumberGenerator) -> Subject {
        let pool = subjects.filter { $0.id != id }
        let choices = pool.isEmpty ? subjects : pool
        let index = Int.random(in: 0..<choices.count, using: &rng)
        return choices[index]
    }

    private func resolve(_ query: String) -> QueryOutcome? {
        if query.isEmpty { return nil }
        if let id = aliasIndex[query], let subject = subject(id: id) {
            return .subject(subject)
        }
        for variant in pluralVariants(query) {
            if let id = aliasIndex[variant], let subject = subject(id: id) {
                return .subject(subject)
            }
        }
        if isBlockedWord(query) {
            return tryAnother(seed: query)
        }
        if let category = category(for: query) {
            return .browse(category)
        }
        if let prefixed = prefixMatch(query) {
            return prefixed
        }
        if let fuzzy = fuzzyMatch(query) {
            return fuzzy
        }
        return nil
    }

    private func prefixMatch(_ query: String) -> QueryOutcome? {
        guard query.count >= 2 else { return nil }
        var hits: [Subject] = []
        var seen = Set<String>()
        for (alias, id) in aliases where alias.count > query.count && alias.hasPrefix(query) {
            guard seen.insert(id).inserted, let subject = subject(id: id) else { continue }
            hits.append(subject)
        }
        return uniqueOrChoices(hits)
    }

    private func fuzzyMatch(_ query: String) -> QueryOutcome? {
        guard query.count >= 4, let first = query.first else { return nil }
        let limit = query.count >= 9 ? 2 : 1
        var bestDistance = limit + 1
        var hits: [Subject] = []
        var seen = Set<String>()
        for (alias, id) in aliases {
            guard alias.first == first else { continue }
            if abs(alias.count - query.count) > limit { continue }
            let distance = damerau(query, alias, limit: limit)
            if distance > limit || distance > bestDistance { continue }
            guard let subject = subject(id: id) else { continue }
            if distance < bestDistance {
                bestDistance = distance
                hits = [subject]
                seen = [id]
            } else if distance == bestDistance, seen.insert(id).inserted {
                hits.append(subject)
            }
        }
        return uniqueOrChoices(hits)
    }

    private func uniqueOrChoices(_ hits: [Subject]) -> QueryOutcome? {
        if hits.isEmpty { return nil }
        if hits.count == 1 { return .subject(hits[0]) }
        return .choices(message: "Which one should we draw?", subjects: Array(hits.prefix(6)))
    }

    private func tryAnother(seed: String) -> QueryOutcome {
        .tryAnother(message: QueryOutcome.tryAnotherMessage, suggestions: suggestions(seed: seed))
    }

    private func category(for query: String) -> Category? {
        categoryWords[query]
    }
}

private let stopwords: Set<String> = [
    "a", "an", "the", "please", "draw", "me", "of", "my", "some", "want",
    "to", "i", "like", "can", "you", "lets", "with", "for",
]

private let greetings: [String: String] = [
    "hi": "Hi! Type a word to draw, like cat or rocket.",
    "hello": "Hi! Type a word to draw, like cat or rocket.",
    "hey": "Hi! Type a word to draw, like cat or rocket.",
    "help": "Type a word you want to draw, or tap Surprise me.",
]

private let categoryWords: [String: Category] = [
    "animal": .animals,
    "animals": .animals,
    "pet": .animals,
    "pets": .animals,
    "fantasy": .fantasy,
    "magic": .fantasy,
    "vehicle": .vehicles,
    "vehicles": .vehicles,
    "food": .food,
    "foods": .food,
    "snack": .food,
    "snacks": .food,
    "nature": .nature,
    "space": .space,
    "building": .buildings,
    "buildings": .buildings,
    "everyday": .everyday,
    "things": .everyday,
]

private func greetingMessage(for query: String) -> String? {
    greetings[query]
}

private func stripStopwords(_ query: String) -> String {
    let kept = query.split(separator: " ").map(String.init).filter { !stopwords.contains($0) }
    return kept.joined(separator: " ")
}

private func damerau(_ a: String, _ b: String, limit: Int) -> Int {
    let left = Array(a)
    let right = Array(b)
    let n = left.count
    let m = right.count
    if abs(n - m) > limit { return limit + 1 }
    if n == 0 { return m }
    if m == 0 { return n }
    var previous = Array(0...m)
    var beforePrevious = Array(repeating: 0, count: m + 1)
    for i in 1...n {
        var current = Array(repeating: 0, count: m + 1)
        current[0] = i
        var rowBest = current[0]
        for j in 1...m {
            let cost = left[i - 1] == right[j - 1] ? 0 : 1
            var value = min(previous[j] + 1, current[j - 1] + 1, previous[j - 1] + cost)
            if i > 1, j > 1, left[i - 1] == right[j - 2], left[i - 2] == right[j - 1] {
                value = min(value, beforePrevious[j - 2] + 1)
            }
            current[j] = value
            rowBest = min(rowBest, value)
        }
        if rowBest > limit { return limit + 1 }
        beforePrevious = previous
        previous = current
    }
    return previous[m]
}

private struct BookFile: Decodable {
    var formatVersion: Int
    var subjects: [SubjectFile]
}

private struct SubjectFile: Decodable {
    var id: String
    var title: String
    var category: String
    var words: [String]
    var viewBox: [Double]?
    var steps: [StepFile]

    func makeSubject() throws -> Subject {
        guard let category = Category(rawValue: category) else {
            throw LibraryError.invalid("\(id) has an unknown category.")
        }
        let box = try decodeBox(viewBox, id: id)
        if steps.isEmpty {
            throw LibraryError.invalid("\(title) has no steps.")
        }
        var drawSteps: [DrawStep] = []
        for (offset, step) in steps.enumerated() {
            let instruction = step.instruction.trimmingCharacters(in: .whitespacesAndNewlines)
            if instruction.isEmpty {
                throw LibraryError.invalid("\(title) step \(offset + 1) is missing its words.")
            }
            if step.strokes.isEmpty {
                throw LibraryError.invalid("\(title) step \(offset + 1) has no lines.")
            }
            var strokes: [Stroke] = []
            for stroke in step.strokes {
                let commands: [PathCommand]
                do {
                    commands = try parseSVGPath(stroke.d)
                } catch {
                    throw LibraryError.invalid("\(title) has a line that could not be read.")
                }
                strokes.append(
                    Stroke(
                        d: stroke.d,
                        width: stroke.width ?? 4.6,
                        fill: stroke.fill ?? false,
                        commands: commands
                    )
                )
            }
            drawSteps.append(DrawStep(instruction: instruction, strokes: strokes))
        }
        return Subject(
            id: id,
            title: title,
            category: category,
            words: words,
            viewBox: box,
            steps: drawSteps
        )
    }
}

private struct StepFile: Decodable {
    var instruction: String
    var strokes: [StrokeFile]
}

private struct StrokeFile: Decodable {
    var d: String
    var width: Double?
    var fill: Bool?
}

private func decodeBox(_ values: [Double]?, id: String) throws -> ViewBox {
    guard let values, !values.isEmpty else { return .page }
    guard values.count == 4, values[2] > 0, values[3] > 0 else {
        throw LibraryError.invalid("\(id) has a bad viewBox.")
    }
    return ViewBox(minX: values[0], minY: values[1], width: values[2], height: values[3])
}
