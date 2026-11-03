import Foundation

public struct PathParseError: Error, Equatable, CustomStringConvertible {
    public let message: String

    public init(message: String) {
        self.message = message
    }

    public var description: String { message }
}

/// Turns an SVG path string into move, line, cubic, and close commands.
/// Arcs and quadratic curves are converted to cubics. Y grows downward.
public func parseSVGPath(_ d: String) throws -> [PathCommand] {
    var scanner = PathScanner(characters: Array(d))
    return try scanner.parse()
}

private struct PathScanner {
    let characters: [Character]
    var index = 0
    var current = Point(x: 0, y: 0)
    var subpathStart = Point(x: 0, y: 0)
    var lastCubicControl: Point?
    var lastQuadControl: Point?
    var previous: Previous = .other
    var commands: [PathCommand] = []

    enum Previous {
        case cubic
        case quad
        case other
    }

    mutating func parse() throws -> [PathCommand] {
        skipSeparators()
        guard index < characters.count else {
            throw PathParseError(message: "Path is empty")
        }
        guard let first = characters[safe: index], isCommand(first) else {
            throw PathParseError(message: "Path must start with a command")
        }
        var command = first
        index += 1
        var implicit = false
        while true {
            if !implicit {
                // command already consumed
            }
            try readCommand(command)
            skipSeparators()
            if index >= characters.count { break }
            let next = characters[index]
            if isCommand(next) {
                command = next
                index += 1
                implicit = false
            } else {
                if command == "M" { command = "L" }
                if command == "m" { command = "l" }
                if command == "Z" || command == "z" {
                    throw PathParseError(message: "Close path cannot be repeated with numbers")
                }
                implicit = true
            }
        }
        return commands
    }

    mutating func readCommand(_ command: Character) throws {
        switch command {
        case "M", "m":
            let point = try readPoint(relative: command == "m")
            move(to: point)
        case "L", "l":
            let point = try readPoint(relative: command == "l")
            line(to: point)
        case "H", "h":
            let x = try readNumber()
            let absolute = command == "h" ? current.x + x : x
            line(to: Point(x: absolute, y: current.y))
        case "V", "v":
            let y = try readNumber()
            let absolute = command == "v" ? current.y + y : y
            line(to: Point(x: current.x, y: absolute))
        case "C", "c":
            let relative = command == "c"
            let c1 = try readPoint(relative: relative)
            let c2 = try readPoint(relative: relative)
            let end = try readPoint(relative: relative)
            cubic(c1: c1, c2: c2, end: end)
        case "S", "s":
            let relative = command == "s"
            let c2 = try readPoint(relative: relative)
            let end = try readPoint(relative: relative)
            let c1 = reflectedCubicControl()
            cubic(c1: c1, c2: c2, end: end)
        case "Q", "q":
            let relative = command == "q"
            let control = try readPoint(relative: relative)
            let end = try readPoint(relative: relative)
            quadratic(control: control, end: end)
        case "T", "t":
            let end = try readPoint(relative: command == "t")
            let control = reflectedQuadControl()
            quadratic(control: control, end: end)
        case "A", "a":
            try arc(relative: command == "a")
        case "Z", "z":
            commands.append(.close)
            current = subpathStart
            previous = .other
            lastCubicControl = nil
            lastQuadControl = nil
        default:
            throw PathParseError(message: "Unknown command \(command)")
        }
    }

    mutating func move(to point: Point) {
        current = point
        subpathStart = point
        commands.append(.move(x: point.x, y: point.y))
        previous = .other
        lastCubicControl = nil
        lastQuadControl = nil
    }

    mutating func line(to point: Point) {
        current = point
        commands.append(.line(x: point.x, y: point.y))
        previous = .other
        lastCubicControl = nil
        lastQuadControl = nil
    }

    mutating func cubic(c1: Point, c2: Point, end: Point) {
        commands.append(.cubic(x1: c1.x, y1: c1.y, x2: c2.x, y2: c2.y, x: end.x, y: end.y))
        current = end
        lastCubicControl = c2
        lastQuadControl = nil
        previous = .cubic
    }

    mutating func quadratic(control: Point, end: Point) {
        let c1 = Point(
            x: current.x + 2.0 / 3.0 * (control.x - current.x),
            y: current.y + 2.0 / 3.0 * (control.y - current.y)
        )
        let c2 = Point(
            x: end.x + 2.0 / 3.0 * (control.x - end.x),
            y: end.y + 2.0 / 3.0 * (control.y - end.y)
        )
        commands.append(.cubic(x1: c1.x, y1: c1.y, x2: c2.x, y2: c2.y, x: end.x, y: end.y))
        current = end
        lastQuadControl = control
        lastCubicControl = nil
        previous = .quad
    }

    func reflectedCubicControl() -> Point {
        guard previous == .cubic, let control = lastCubicControl else { return current }
        return Point(x: 2 * current.x - control.x, y: 2 * current.y - control.y)
    }

    func reflectedQuadControl() -> Point {
        guard previous == .quad, let control = lastQuadControl else { return current }
        return Point(x: 2 * current.x - control.x, y: 2 * current.y - control.y)
    }

    mutating func arc(relative: Bool) throws {
        let rx = abs(try readNumber())
        let ry = abs(try readNumber())
        let rotation = try readNumber()
        let large = try readFlag()
        let sweep = try readFlag()
        let end = try readPoint(relative: relative)
        if rx < 1e-8 || ry < 1e-8 || (end.x == current.x && end.y == current.y) {
            line(to: end)
            return
        }
        let pieces = arcToCubics(
            from: current,
            to: end,
            rx: rx,
            ry: ry,
            rotationDegrees: rotation,
            large: large,
            sweep: sweep
        )
        if pieces.isEmpty {
            line(to: end)
            return
        }
        for piece in pieces {
            commands.append(piece)
        }
        current = end
        previous = .other
        lastCubicControl = nil
        lastQuadControl = nil
    }

    mutating func readPoint(relative: Bool) throws -> Point {
        let x = try readNumber()
        let y = try readNumber()
        if relative {
            return Point(x: current.x + x, y: current.y + y)
        }
        return Point(x: x, y: y)
    }

    mutating func readFlag() throws -> Bool {
        let value = try readNumber()
        if value == 0 { return false }
        if value == 1 { return true }
        throw PathParseError(message: "Arc flag must be 0 or 1")
    }

    mutating func readNumber() throws -> Double {
        skipSeparators()
        guard index < characters.count else {
            throw PathParseError(message: "Expected a number")
        }
        let start = index
        let first = characters[index]
        if first == "+" || first == "-" {
            index += 1
        }
        var sawDigit = false
        while index < characters.count, characters[index].isNumber {
            sawDigit = true
            index += 1
        }
        if index < characters.count, characters[index] == "." {
            index += 1
            while index < characters.count, characters[index].isNumber {
                sawDigit = true
                index += 1
            }
        }
        if index < characters.count, characters[index] == "e" || characters[index] == "E" {
            var look = index + 1
            if look < characters.count, characters[look] == "+" || characters[look] == "-" {
                look += 1
            }
            let exponentStart = look
            while look < characters.count, characters[look].isNumber {
                look += 1
            }
            if look > exponentStart {
                index = look
            }
        }
        if !sawDigit {
            throw PathParseError(message: "Expected a number")
        }
        let text = String(characters[start..<index])
        guard let value = Double(text) else {
            throw PathParseError(message: "Bad number \(text)")
        }
        return value
    }

    mutating func skipSeparators() {
        while index < characters.count {
            switch characters[index] {
            case " ", "\n", "\r", "\t", ",":
                index += 1
            default:
                return
            }
        }
    }

    func isCommand(_ character: Character) -> Bool {
        switch character {
        case "M", "m", "L", "l", "H", "h", "V", "v", "C", "c", "S", "s", "Q", "q", "T", "t", "A", "a", "Z", "z":
            return true
        default:
            return false
        }
    }
}

private extension Array {
    subscript(safe index: Int) -> Element? {
        guard index >= 0, index < count else { return nil }
        return self[index]
    }
}

private func arcToCubics(
    from start: Point,
    to end: Point,
    rx rxIn: Double,
    ry ryIn: Double,
    rotationDegrees: Double,
    large: Bool,
    sweep: Bool
) -> [PathCommand] {
    let phi = rotationDegrees * .pi / 180
    let cosPhi = cos(phi)
    let sinPhi = sin(phi)
    let dx = (start.x - end.x) / 2
    let dy = (start.y - end.y) / 2
    let x1p = cosPhi * dx + sinPhi * dy
    let y1p = -sinPhi * dx + cosPhi * dy

    var rx = abs(rxIn)
    var ry = abs(ryIn)
    let lambda = (x1p * x1p) / (rx * rx) + (y1p * y1p) / (ry * ry)
    if lambda > 1 {
        let scale = sqrt(lambda)
        rx *= scale
        ry *= scale
    }

    let rx2 = rx * rx
    let ry2 = ry * ry
    let x1p2 = x1p * x1p
    let y1p2 = y1p * y1p
    var numerator = rx2 * ry2 - rx2 * y1p2 - ry2 * x1p2
    let denominator = rx2 * y1p2 + ry2 * x1p2
    if numerator < 0 { numerator = 0 }
    let sign: Double = (large == sweep) ? -1 : 1
    let coef = sign * sqrt(numerator / max(denominator, 1e-12))
    let cxp = coef * (rx * y1p) / ry
    let cyp = coef * -(ry * x1p) / rx
    let centerX = cosPhi * cxp - sinPhi * cyp + (start.x + end.x) / 2
    let centerY = sinPhi * cxp + cosPhi * cyp + (start.y + end.y) / 2

    func vectorAngle(ux: Double, uy: Double, vx: Double, vy: Double) -> Double {
        let dot = ux * vx + uy * vy
        let length = sqrt(ux * ux + uy * uy) * sqrt(vx * vx + vy * vy)
        var angle = acos(max(-1, min(1, dot / max(length, 1e-12))))
        if ux * vy - uy * vx < 0 { angle = -angle }
        return angle
    }

    let theta1 = vectorAngle(
        ux: 1, uy: 0,
        vx: (x1p - cxp) / rx,
        vy: (y1p - cyp) / ry
    )
    var delta = vectorAngle(
        ux: (x1p - cxp) / rx,
        uy: (y1p - cyp) / ry,
        vx: (-x1p - cxp) / rx,
        vy: (-y1p - cyp) / ry
    )
    if !sweep && delta > 0 { delta -= 2 * .pi }
    if sweep && delta < 0 { delta += 2 * .pi }

    let segments = max(1, Int(ceil(abs(delta) / (.pi / 2))))
    let stepAngle = delta / Double(segments)
    var output: [PathCommand] = []

    func map(_ theta: Double) -> Point {
        let x = rx * cos(theta)
        let y = ry * sin(theta)
        return Point(
            x: centerX + x * cosPhi - y * sinPhi,
            y: centerY + x * sinPhi + y * cosPhi
        )
    }

    func derivative(_ theta: Double) -> Point {
        let dx = -rx * sin(theta)
        let dy = ry * cos(theta)
        return Point(
            x: dx * cosPhi - dy * sinPhi,
            y: dx * sinPhi + dy * cosPhi
        )
    }

    for segment in 0..<segments {
        let startAngle = theta1 + stepAngle * Double(segment)
        let endAngle = startAngle + stepAngle
        let alpha = (4.0 / 3.0) * tan(stepAngle / 4.0)
        let p0 = map(startAngle)
        let p3 = map(endAngle)
        let d0 = derivative(startAngle)
        let d3 = derivative(endAngle)
        output.append(
            .cubic(
                x1: p0.x + alpha * d0.x,
                y1: p0.y + alpha * d0.y,
                x2: p3.x - alpha * d3.x,
                y2: p3.y - alpha * d3.y,
                x: p3.x,
                y: p3.y
            )
        )
    }
    return output
}
