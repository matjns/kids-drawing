import Foundation

public enum Category: String, Codable, CaseIterable, Sendable, Identifiable {
    case animals
    case fantasy
    case vehicles
    case food
    case nature
    case space
    case buildings
    case everyday

    public var id: String { rawValue }

    public var title: String {
        switch self {
        case .animals: return "Animals"
        case .fantasy: return "Fantasy"
        case .vehicles: return "Vehicles"
        case .food: return "Food"
        case .nature: return "Nature"
        case .space: return "Space"
        case .buildings: return "Buildings"
        case .everyday: return "Everyday Things"
        }
    }
}

public struct ViewBox: Equatable, Sendable {
    public var minX: Double
    public var minY: Double
    public var width: Double
    public var height: Double

    public init(minX: Double, minY: Double, width: Double, height: Double) {
        self.minX = minX
        self.minY = minY
        self.width = width
        self.height = height
    }

    public static let page = ViewBox(minX: 0, minY: 0, width: 200, height: 200)
}

public enum PathCommand: Equatable, Sendable {
    case move(x: Double, y: Double)
    case line(x: Double, y: Double)
    case cubic(x1: Double, y1: Double, x2: Double, y2: Double, x: Double, y: Double)
    case close
}

public struct Stroke: Equatable, Sendable {
    public var d: String
    public var width: Double
    public var fill: Bool
    public var commands: [PathCommand]

    public init(d: String, width: Double = 4.6, fill: Bool = false, commands: [PathCommand]) {
        self.d = d
        self.width = width
        self.fill = fill
        self.commands = commands
    }
}

public struct DrawStep: Equatable, Sendable {
    public var instruction: String
    public var strokes: [Stroke]

    public init(instruction: String, strokes: [Stroke]) {
        self.instruction = instruction
        self.strokes = strokes
    }
}

public struct Subject: Equatable, Sendable, Identifiable {
    public var id: String
    public var title: String
    public var category: Category
    public var words: [String]
    public var viewBox: ViewBox
    public var steps: [DrawStep]

    public init(
        id: String,
        title: String,
        category: Category,
        words: [String],
        viewBox: ViewBox,
        steps: [DrawStep]
    ) {
        self.id = id
        self.title = title
        self.category = category
        self.words = words
        self.viewBox = viewBox
        self.steps = steps
    }
}

public struct Point: Equatable, Sendable {
    public var x: Double
    public var y: Double

    public init(x: Double, y: Double) {
        self.x = x
        self.y = y
    }
}

public struct Bounds: Equatable, Sendable {
    public var minX: Double
    public var minY: Double
    public var maxX: Double
    public var maxY: Double

    public init(minX: Double, minY: Double, maxX: Double, maxY: Double) {
        self.minX = minX
        self.minY = minY
        self.maxX = maxX
        self.maxY = maxY
    }
}

public enum LibraryError: Error, Equatable, LocalizedError {
    case unreadable
    case missingBook
    case invalid(String)

    public var errorDescription: String? {
        switch self {
        case .unreadable:
            return "The drawing file could not be read."
        case .missingBook:
            return "The drawing file is missing from the app."
        case .invalid(let reason):
            return reason
        }
    }
}

public enum QueryOutcome: Equatable, Sendable {
    case subject(Subject)
    case browse(Category)
    case choices(message: String, subjects: [Subject])
    case tryAnother(message: String, suggestions: [Subject])

    public static let tryAnotherMessage = "Let's try another one!"

    public var matchedSubject: Subject? {
        if case .subject(let subject) = self { return subject }
        return nil
    }
}
