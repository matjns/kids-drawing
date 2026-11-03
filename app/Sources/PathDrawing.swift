import DrawingCore
import SwiftUI

struct StrokeShape: Shape {
    var commands: [PathCommand]
    var viewBox: ViewBox

    func path(in rect: CGRect) -> Path {
        var inkPath = Path()
        let scale = Swift.min(rect.width / viewBox.width, rect.height / viewBox.height)
        let extraX = (rect.width - viewBox.width * scale) / 2
        let extraY = (rect.height - viewBox.height * scale) / 2
        func point(_ x: Double, _ y: Double) -> CGPoint {
            CGPoint(
                x: extraX + (x - viewBox.minX) * scale,
                y: extraY + (y - viewBox.minY) * scale
            )
        }
        for command in commands {
            switch command {
            case .move(let x, let y):
                inkPath.move(to: point(x, y))
            case .line(let x, let y):
                inkPath.addLine(to: point(x, y))
            case .cubic(let x1, let y1, let x2, let y2, let x, let y):
                inkPath.addCurve(
                    to: point(x, y),
                    control1: point(x1, y1),
                    control2: point(x2, y2)
                )
            case .close:
                inkPath.closeSubpath()
            }
        }
        return inkPath
    }
}

func scaledStrokeWidth(_ width: Double, in size: CGSize, viewBox: ViewBox) -> CGFloat {
    let scale = Swift.min(size.width / viewBox.width, size.height / viewBox.height)
    return CGFloat(width * scale)
}
