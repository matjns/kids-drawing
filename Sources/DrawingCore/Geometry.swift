import Foundation

extension Array where Element == PathCommand {
    public func flattened(tolerance: Double = 0.8) -> [Point] {
        var points: [Point] = []
        var current: Point?
        var start: Point?
        for command in self {
            switch command {
            case .move(let x, let y):
                let point = Point(x: x, y: y)
                current = point
                start = point
                points.append(point)
            case .line(let x, let y):
                let point = Point(x: x, y: y)
                current = point
                points.append(point)
            case .cubic(let x1, let y1, let x2, let y2, let x, let y):
                let origin = current ?? Point(x: 0, y: 0)
                let cubic = flattenCubic(
                    p0: origin,
                    p1: Point(x: x1, y: y1),
                    p2: Point(x: x2, y: y2),
                    p3: Point(x: x, y: y),
                    tolerance: tolerance
                )
                if points.isEmpty {
                    points.append(contentsOf: cubic)
                } else {
                    points.append(contentsOf: cubic.dropFirst())
                }
                current = Point(x: x, y: y)
            case .close:
                if let start, current != start {
                    points.append(start)
                }
                current = start
            }
        }
        return points
    }

    public func bounds(tolerance: Double = 0.8) -> Bounds? {
        let points = flattened(tolerance: tolerance)
        guard let first = points.first else { return nil }
        var box = Bounds(minX: first.x, minY: first.y, maxX: first.x, maxY: first.y)
        for point in points.dropFirst() {
            box.minX = Swift.min(box.minX, point.x)
            box.minY = Swift.min(box.minY, point.y)
            box.maxX = Swift.max(box.maxX, point.x)
            box.maxY = Swift.max(box.maxY, point.y)
        }
        return box
    }
}

private func flattenCubic(p0: Point, p1: Point, p2: Point, p3: Point, tolerance: Double) -> [Point] {
    var output = [p0]
    func recurse(_ a: Point, _ b: Point, _ c: Point, _ d: Point, _ depth: Int) {
        if depth > 14 || (distance(b, from: a, to: d) <= tolerance && distance(c, from: a, to: d) <= tolerance) {
            output.append(d)
            return
        }
        let ab = midpoint(a, b)
        let bc = midpoint(b, c)
        let cd = midpoint(c, d)
        let abbc = midpoint(ab, bc)
        let bccd = midpoint(bc, cd)
        let middle = midpoint(abbc, bccd)
        recurse(a, ab, abbc, middle, depth + 1)
        recurse(middle, bccd, cd, d, depth + 1)
    }
    recurse(p0, p1, p2, p3, 0)
    return output
}

private func midpoint(_ a: Point, _ b: Point) -> Point {
    Point(x: (a.x + b.x) / 2, y: (a.y + b.y) / 2)
}

private func distance(_ point: Point, from a: Point, to b: Point) -> Double {
    let vx = b.x - a.x
    let vy = b.y - a.y
    let lengthSquared = vx * vx + vy * vy
    if lengthSquared < 1e-8 {
        return hypot(point.x - a.x, point.y - a.y)
    }
    let t = max(0, min(1, ((point.x - a.x) * vx + (point.y - a.y) * vy) / lengthSquared))
    let qx = a.x + t * vx
    let qy = a.y + t * vy
    return hypot(point.x - qx, point.y - qy)
}

public func normalizeQuery(_ raw: String) -> String {
    var output = ""
    var pendingSpace = false
    for character in raw.lowercased() {
        if character.isLetter || character.isNumber {
            output.append(character)
            pendingSpace = false
        } else if character == "'" || character == "’" {
            continue
        } else if !output.isEmpty && !pendingSpace {
            output.append(" ")
            pendingSpace = true
        }
    }
    return output.trimmingCharacters(in: .whitespaces)
}
