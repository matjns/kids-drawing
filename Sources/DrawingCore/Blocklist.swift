import Foundation

/// Words we will not match to a drawing. Unknown words already get a gentle
/// redirect; this list stops rude or unsafe words from landing on a nearby subject
/// (for example a one-letter typo of a real drawing).
func isBlockedWord(_ normalized: String) -> Bool {
    if normalized.isEmpty { return false }
    if blockedWords.contains(normalized) { return true }
    let tokens = normalized.split(separator: " ").map(String.init)
    for token in tokens {
        if blockedWords.contains(token) { return true }
        for variant in pluralVariants(token) where blockedWords.contains(variant) {
            return true
        }
    }
    for variant in pluralVariants(normalized) where blockedWords.contains(variant) {
        return true
    }
    return false
}

func pluralVariants(_ word: String) -> [String] {
    var variants: [String] = []
    if word.hasSuffix("ies"), word.count > 4 {
        variants.append(String(word.dropLast(3)) + "y")
    }
    if word.hasSuffix("es"), word.count > 3 {
        variants.append(String(word.dropLast(2)))
    }
    if word.hasSuffix("s"), !word.hasSuffix("ss"), word.count > 2 {
        variants.append(String(word.dropLast()))
    }
    return variants
}

private let blockedWords: Set<String> = [
    "ass", "asses", "asshole",
    "bastard",
    "bitch",
    "boob", "boobs",
    "butt",
    "cock",
    "crap",
    "damn",
    "dick",
    "fuck", "fuk", "fck",
    "gun", "guns",
    "hate",
    "hell",
    "kill",
    "nazi",
    "nude",
    "penis",
    "porn",
    "pussy",
    "sex", "sexy",
    "shit",
    "slut",
    "war",
]
