import Foundation

public struct LessonSession: Equatable, Sendable {
    public let subject: Subject
    public private(set) var stepIndex: Int
    public private(set) var showingFinished: Bool

    public init(subject: Subject) {
        self.subject = subject
        self.stepIndex = 0
        self.showingFinished = false
    }

    public var stepCount: Int { subject.steps.count }

    public var currentStep: DrawStep? {
        guard stepsAreInRange else { return nil }
        return subject.steps[stepIndex]
    }

    public mutating func goForward() {
        if showingFinished { return }
        if stepIndex + 1 < subject.steps.count {
            stepIndex += 1
        } else {
            showingFinished = true
        }
    }

    public mutating func goBack() {
        if showingFinished {
            showingFinished = false
            return
        }
        if stepIndex > 0 {
            stepIndex -= 1
        }
    }

    public mutating func showFinished() {
        showingFinished = true
    }

    public mutating func showSteps() {
        showingFinished = false
    }

    private var stepsAreInRange: Bool {
        stepIndex >= 0 && stepIndex < subject.steps.count
    }
}
