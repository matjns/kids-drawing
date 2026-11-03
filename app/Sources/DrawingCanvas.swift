import DrawingCore
import SwiftUI

struct InkMark: Identifiable {
    let id: Int
    let stepIndex: Int
    let orderInStep: Int
    let stroke: Stroke
}

struct DrawingCanvas: View {
    let subject: Subject
    var revealedThrough: Int?
    var highlightNew: Bool
    var animate: Bool
    var replayToken: Int

    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @State private var drawnNew = 0
    @State private var trim: CGFloat = 1

    private var marks: [InkMark] {
        var items: [InkMark] = []
        var running = 0
        for (stepIndex, step) in subject.steps.enumerated() {
            if let revealedThrough, stepIndex > revealedThrough { break }
            for (order, stroke) in step.strokes.enumerated() {
                items.append(InkMark(id: running, stepIndex: stepIndex, orderInStep: order, stroke: stroke))
                running += 1
            }
        }
        return items
    }

    private var newMarks: [InkMark] {
        guard let revealedThrough else { return [] }
        return marks.filter { $0.stepIndex == revealedThrough }
    }

    private var shouldAnimate: Bool {
        highlightNew && animate && !reduceMotion && revealedThrough != nil && !newMarks.isEmpty
    }

    var body: some View {
        GeometryReader { proxy in
            let size = proxy.size
            ZStack {
                ForEach(marks) { mark in
                    markView(mark, size: size)
                }
            }
            .frame(width: size.width, height: size.height)
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(accessibilityText)
        .task(id: replayToken) {
            await play()
        }
        .onAppear {
            if !shouldAnimate {
                drawnNew = newMarks.count
                trim = 1
            }
        }
    }

    @ViewBuilder
    private func markView(_ mark: InkMark, size: CGSize) -> some View {
        let shape = StrokeShape(commands: mark.stroke.commands, viewBox: subject.viewBox)
        let lineWidth = scaledStrokeWidth(mark.stroke.width, in: size, viewBox: subject.viewBox)
        let tint = color(for: mark)
        if shouldDraw(mark) {
            if mark.stroke.fill {
                shape.fill(tint)
            } else if isTrimming(mark) {
                shape
                    .trim(from: 0, to: trim)
                    .stroke(tint, style: StrokeStyle(lineWidth: lineWidth, lineCap: .round, lineJoin: .round))
            } else {
                shape.stroke(tint, style: StrokeStyle(lineWidth: lineWidth, lineCap: .round, lineJoin: .round))
            }
        }
    }

    private func shouldDraw(_ mark: InkMark) -> Bool {
        guard highlightNew, revealedThrough != nil else { return true }
        guard mark.stepIndex == revealedThrough else { return true }
        if !shouldAnimate { return true }
        return mark.orderInStep <= drawnNew
    }

    private func isTrimming(_ mark: InkMark) -> Bool {
        guard shouldAnimate, mark.stepIndex == revealedThrough else { return false }
        return mark.orderInStep == drawnNew && !mark.stroke.fill
    }

    private func color(for mark: InkMark) -> Color {
        guard highlightNew, let revealedThrough else { return Theme.ink }
        return mark.stepIndex == revealedThrough ? Theme.newLine : Theme.oldLine
    }

    private var accessibilityText: String {
        if let revealedThrough {
            let step = subject.steps[revealedThrough]
            return "Step \(revealedThrough + 1) of \(subject.steps.count). \(step.instruction) New lines are blue. Earlier lines are grey."
        }
        return "Finished drawing of a \(subject.title.lowercased())."
    }

    private func play() async {
        guard shouldAnimate else {
            drawnNew = newMarks.count
            trim = 1
            return
        }
        let total = newMarks.count
        for index in 0..<total {
            if Task.isCancelled { return }
            var paused = Transaction()
            paused.disablesAnimations = true
            withTransaction(paused) {
                drawnNew = index
                trim = 0
            }
            await Task.yield()
            withAnimation(.easeInOut(duration: 0.45)) {
                trim = 1
            }
            try? await Task.sleep(nanoseconds: 480_000_000)
        }
        drawnNew = total
        trim = 1
    }
}
