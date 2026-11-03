import DrawingCore
import SwiftUI

enum Theme {
    static let paper = Color(red: 0.984, green: 0.965, blue: 0.925)
    static let ink = Color(red: 0.165, green: 0.165, blue: 0.200)
    static let oldLine = Color(red: 0.73, green: 0.70, blue: 0.66)
    static let newLine = Color(red: 0.118, green: 0.306, blue: 0.537)
    static let coral = Color(red: 0.878, green: 0.420, blue: 0.275)
    static let card = Color.white
    static let line = Color(red: 0.86, green: 0.83, blue: 0.78)
    static let good = Color(red: 0.176, green: 0.510, blue: 0.357)
    static let hint = Color(red: 0.992, green: 0.925, blue: 0.835)
    static let hintInk = Color(red: 0.42, green: 0.27, blue: 0.16)

    static func chip(_ category: Category) -> Color {
        switch category {
        case .animals: return Color(red: 0.486, green: 0.604, blue: 0.447)
        case .fantasy: return Color(red: 0.557, green: 0.486, blue: 0.765)
        case .vehicles: return Color(red: 0.298, green: 0.486, blue: 0.608)
        case .food: return Color(red: 0.878, green: 0.604, blue: 0.353)
        case .nature: return Color(red: 0.369, green: 0.604, blue: 0.420)
        case .space: return Color(red: 0.243, green: 0.298, blue: 0.541)
        case .buildings: return Color(red: 0.769, green: 0.471, blue: 0.416)
        case .everyday: return Color(red: 0.431, green: 0.498, blue: 0.569)
        }
    }
}

struct KidButtonStyle: ButtonStyle {
    var fill: Color
    var foreground: Color
    var border: Color? = nil

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.system(size: 18, weight: .semibold, design: .rounded))
            .padding(.horizontal, 18)
            .padding(.vertical, 12)
            .frame(minHeight: 48)
            .background(
                RoundedRectangle(cornerRadius: 14, style: .continuous)
                    .fill(fill.opacity(configuration.isPressed ? 0.84 : 1))
            )
            .overlay(
                RoundedRectangle(cornerRadius: 14, style: .continuous)
                    .stroke(border ?? Color.clear, lineWidth: border == nil ? 0 : 2)
            )
            .foregroundStyle(foreground)
    }
}
