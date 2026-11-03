import DrawingCore
import SwiftUI

struct StudioView: View {
    @EnvironmentObject private var model: AppModel

    var body: some View {
        if let lesson = model.lesson {
            ScrollView {
                ViewThatFits(in: .horizontal) {
                    HStack(alignment: .top, spacing: 28) {
                        paper(lesson)
                        controls(lesson)
                            .frame(width: 340)
                    }
                    VStack(alignment: .leading, spacing: 20) {
                        paper(lesson)
                        controls(lesson)
                    }
                }
                .padding(24)
            }
        }
    }

    private func paper(_ lesson: LessonSession) -> some View {
        VStack(spacing: 0) {
            ZStack(alignment: .top) {
                RoundedRectangle(cornerRadius: 8, style: .continuous)
                    .fill(Color(red: 0.96, green: 0.86, blue: 0.55))
                    .frame(width: 92, height: 22)
                    .offset(y: -8)
                DrawingCanvas(
                    subject: lesson.subject,
                    revealedThrough: lesson.showingFinished ? nil : lesson.stepIndex,
                    highlightNew: !lesson.showingFinished,
                    animate: model.progress.animateSteps && !lesson.showingFinished,
                    replayToken: model.replayToken
                )
                .padding(18)
                .background(
                    RoundedRectangle(cornerRadius: 22, style: .continuous)
                        .fill(Theme.card)
                        .shadow(color: .black.opacity(0.06), radius: 16, y: 8)
                )
            }
            .frame(maxWidth: 560)
            .aspectRatio(1, contentMode: .fit)
            .focusable()
            .onKeyPress(.leftArrow) {
                model.back()
                return .handled
            }
            .onKeyPress(.rightArrow) {
                model.forward()
                return .handled
            }
        }
        .frame(maxWidth: .infinity)
    }

    @ViewBuilder
    private func controls(_ lesson: LessonSession) -> some View {
        if lesson.showingFinished {
            finishedControls(lesson)
        } else {
            stepControls(lesson)
        }
    }

    private func stepControls(_ lesson: LessonSession) -> some View {
        let step = lesson.subject.steps[lesson.stepIndex]
        return VStack(alignment: .leading, spacing: 16) {
            Text("Step \(lesson.stepIndex + 1) of \(lesson.stepCount)")
                .font(.system(size: 16, weight: .semibold, design: .rounded))
                .foregroundStyle(Theme.newLine)
            Text(step.instruction)
                .font(.system(size: 28, weight: .bold, design: .rounded))
                .foregroundStyle(Theme.ink)
                .fixedSize(horizontal: false, vertical: true)
            if lesson.stepIndex == 0 {
                Text("Look at the blue lines, draw them, then press Next.")
                    .font(.system(size: 16, design: .rounded))
                    .foregroundStyle(.secondary)
            }
            legend
            HStack(spacing: 10) {
                Button("Back") { model.back() }
                    .buttonStyle(KidButtonStyle(fill: Theme.card, foreground: Theme.ink, border: Theme.line))
                    .disabled(!model.canGoBack)
                    .opacity(model.canGoBack ? 1 : 0.45)
                Button(lesson.stepIndex + 1 >= lesson.stepCount ? "See it finished" : "Next") {
                    model.forward()
                }
                .buttonStyle(KidButtonStyle(fill: Theme.coral, foreground: .white))
            }
            Toggle(
                "Animate the new lines",
                isOn: Binding(
                    get: { model.progress.animateSteps },
                    set: { model.setAnimate($0) }
                )
            )
            .font(.system(size: 17, weight: .medium, design: .rounded))
            .toggleStyle(.switch)
            if model.progress.animateSteps {
                Button("Watch again") { model.replay() }
                    .buttonStyle(KidButtonStyle(fill: Theme.card, foreground: Theme.ink, border: Theme.line))
            }
            Button("Show the finished drawing") { model.showFinished() }
                .buttonStyle(KidButtonStyle(fill: Theme.ink, foreground: .white))
            Button("All drawings") { model.goHome() }
                .buttonStyle(KidButtonStyle(fill: Theme.card, foreground: Theme.ink, border: Theme.line))
            Text("⌘← and ⌘→ move between steps.")
                .font(.system(size: 13, design: .rounded))
                .foregroundStyle(.secondary)
        }
    }

    private func finishedControls(_ lesson: LessonSession) -> some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("Finished \(lesson.subject.title.lowercased())")
                .font(.system(size: 16, weight: .semibold, design: .rounded))
                .foregroundStyle(Theme.good)
            Text("This is the whole picture. Copy the dark lines on your paper.")
                .font(.system(size: 26, weight: .bold, design: .rounded))
                .foregroundStyle(Theme.ink)
                .fixedSize(horizontal: false, vertical: true)
            if let cheer = model.cheer {
                Text(cheer)
                    .font(.system(size: 18, weight: .medium, design: .rounded))
                    .foregroundStyle(Theme.good)
            }
            Button("I drew it!") { model.markDrawn() }
            .buttonStyle(KidButtonStyle(fill: Theme.good, foreground: .white))
            Button("Back to the steps") { model.showSteps() }
                .buttonStyle(KidButtonStyle(fill: Theme.card, foreground: Theme.ink, border: Theme.line))
            Button { model.surprise() } label: {
                Label("Surprise me", systemImage: "sparkles")
            }
            .buttonStyle(KidButtonStyle(fill: Theme.coral, foreground: .white))
            Button("All drawings") { model.goHome() }
                .buttonStyle(KidButtonStyle(fill: Theme.card, foreground: Theme.ink, border: Theme.line))
        }
    }

    private var legend: some View {
        HStack(spacing: 16) {
            HStack(spacing: 6) {
                Capsule().fill(Theme.newLine).frame(width: 28, height: 6)
                Text("Draw this now")
            }
            HStack(spacing: 6) {
                Capsule().fill(Theme.oldLine).frame(width: 28, height: 6)
                Text("Already drawn")
            }
        }
        .font(.system(size: 15, weight: .medium, design: .rounded))
        .foregroundStyle(Theme.ink)
    }
}
