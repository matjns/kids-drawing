import Combine
import DrawingCore
import SwiftUI

enum Screen: Equatable {
    case home
    case studio
}

struct Notice: Equatable {
    var message: String
    var suggestions: [Subject]

    var isGentleRedirect: Bool { message == QueryOutcome.tryAnotherMessage }
}

@MainActor
final class AppModel: ObservableObject {
    @Published private(set) var library: Library?
    @Published private(set) var loadError: String?
    @Published var query = ""
    @Published var selectedCategory: Category?
    @Published var screen: Screen = .home
    @Published var lesson: LessonSession?
    @Published var notice: Notice?
    @Published var cheer: String?
    @Published private(set) var progress: DrawingProgress
    @Published var replayToken = 0
    @Published var focusSearch = false
    @Published var saveWarning: String?

    private let store: FileProgressStore

    init() {
        let resolvedStore = FileProgressStore(directory: SupportDirectory.drawWithMe())
        store = resolvedStore
        progress = resolvedStore.load()
        switch BundledBook.load() {
        case .success(let loaded):
            library = loaded
        case .failure(let error):
            loadError = error.localizedDescription
        }
    }

    var visibleSubjects: [Subject] {
        guard let library else { return [] }
        if let selectedCategory {
            return library.subjects(in: selectedCategory)
        }
        return library.subjects
    }

    var liveMatches: [Subject] {
        guard notice == nil, let library else { return [] }
        return library.browseMatches(prefix: query)
    }

    var canGoBack: Bool {
        guard let lesson else { return false }
        return lesson.showingFinished || lesson.stepIndex > 0
    }

    func submit() {
        guard let library else { return }
        cheer = nil
        switch library.match(query) {
        case .subject(let subject):
            open(subject)
        case .browse(let category):
            selectedCategory = category
            screen = .home
            lesson = nil
            notice = nil
        case .choices(let message, let subjects):
            notice = Notice(message: message, suggestions: subjects)
            screen = .home
        case .tryAnother(let message, let suggestions):
            notice = Notice(message: message, suggestions: suggestions)
            screen = .home
        }
    }

    func open(_ subject: Subject) {
        lesson = LessonSession(subject: subject)
        screen = .studio
        notice = nil
        cheer = nil
        query = subject.title
        replayToken += 1
    }

    func surprise() {
        guard let library else { return }
        var generator = SystemRandomNumberGenerator()
        let subject = library.surprise(excluding: lesson?.subject.id, rng: &generator)
        open(subject)
    }

    func goHome() {
        screen = .home
        cheer = nil
    }

    func selectCategory(_ category: Category?) {
        selectedCategory = category
        screen = .home
    }

    func forward() {
        guard var current = lesson else { return }
        current.goForward()
        lesson = current
        cheer = nil
        replayToken += 1
    }

    func back() {
        guard var current = lesson, canGoBack else { return }
        current.goBack()
        lesson = current
        cheer = nil
        replayToken += 1
    }

    func showFinished() {
        guard var current = lesson else { return }
        current.showFinished()
        lesson = current
        cheer = nil
        replayToken += 1
    }

    func showSteps() {
        guard var current = lesson else { return }
        current.showSteps()
        lesson = current
        cheer = nil
        replayToken += 1
    }

    func replay() {
        replayToken += 1
    }

    func setAnimate(_ value: Bool) {
        progress.animateSteps = value
        persist()
        replayToken += 1
    }

    func markDrawn() {
        guard let subject = lesson?.subject else { return }
        progress.markFinished(subject.id)
        cheer = cheerText(subject: subject, count: progress.finishedIDs.count)
        persist()
    }

    func clearNotice() {
        guard notice != nil else { return }
        notice = nil
    }

    private func persist() {
        do {
            try store.save(progress)
            saveWarning = nil
        } catch {
            saveWarning = "Couldn't save progress on this Mac."
        }
    }

    private func cheerText(subject: Subject, count: Int) -> String {
        switch count {
        case 1:
            return "That's your first finished drawing. Try another when you want."
        case 5:
            return "Five drawings finished. Your lines are getting steadier."
        case 10, 20, 30, 40, 50:
            return "You've finished \(count) drawings. That's a lot of practice."
        default:
            return "Nice work. The \(subject.title.lowercased()) is ready to copy on paper."
        }
    }
}
