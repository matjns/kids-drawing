import Foundation

public struct Progress: Codable, Equatable, Sendable {
    public var finishedIDs: [String]
    public var animateSteps: Bool

    public init(finishedIDs: [String] = [], animateSteps: Bool = true) {
        self.finishedIDs = finishedIDs
        self.animateSteps = animateSteps
    }

    public mutating func markFinished(_ id: String) {
        guard !finishedIDs.contains(id) else { return }
        finishedIDs.append(id)
        finishedIDs.sort()
    }

    public func hasFinished(_ id: String) -> Bool {
        finishedIDs.contains(id)
    }
}

public struct FileProgressStore: Sendable {
    public var fileURL: URL

    public init(directory: URL) {
        self.fileURL = directory.appendingPathComponent("progress.json")
    }

    public func load() -> Progress {
        guard let data = try? Data(contentsOf: fileURL) else { return Progress() }
        guard let progress = try? JSONDecoder().decode(Progress.self, from: data) else { return Progress() }
        return progress
    }

    public func save(_ progress: Progress) throws {
        let directory = fileURL.deletingLastPathComponent()
        try FileManager.default.createDirectory(at: directory, withIntermediateDirectories: true)
        let data = try JSONEncoder().encode(progress)
        try data.write(to: fileURL, options: [.atomic])
    }
}
