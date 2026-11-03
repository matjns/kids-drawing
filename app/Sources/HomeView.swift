import DrawingCore
import SwiftUI

struct HomeView: View {
    @EnvironmentObject private var model: AppModel

    private let columns = [GridItem(.adaptive(minimum: 160, maximum: 220), spacing: 16)]

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                categoryRow
                if model.visibleSubjects.isEmpty {
                    Text("Nothing in this category yet.")
                        .font(.system(size: 20, weight: .medium, design: .rounded))
                        .foregroundStyle(.secondary)
                        .frame(maxWidth: .infinity, alignment: .center)
                        .padding(.top, 40)
                } else {
                    LazyVGrid(columns: columns, spacing: 16) {
                        ForEach(model.visibleSubjects) { subject in
                            subjectCard(subject)
                        }
                    }
                }
                Text("Works offline. Nothing here uses the internet.")
                    .font(.system(size: 13, design: .rounded))
                    .foregroundStyle(.secondary)
                    .padding(.top, 4)
            }
            .padding(24)
        }
    }

    private var categoryRow: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 8) {
                categoryChip(title: "All", category: nil, tint: Theme.ink)
                ForEach(Category.allCases) { category in
                    categoryChip(title: category.title, category: category, tint: Theme.chip(category))
                }
            }
        }
    }

    private func categoryChip(title: String, category: Category?, tint: Color) -> some View {
        let selected = model.selectedCategory == category
        return Button(title) { model.selectCategory(category) }
            .buttonStyle(
                KidButtonStyle(
                    fill: selected ? tint : Theme.card,
                    foreground: selected ? .white : Theme.ink,
                    border: selected ? .clear : Theme.line
                )
            )
    }

    private func subjectCard(_ subject: Subject) -> some View {
        Button { model.open(subject) } label: {
            VStack(spacing: 8) {
                DrawingCanvas(
                    subject: subject,
                    revealedThrough: nil,
                    highlightNew: false,
                    animate: false,
                    replayToken: 0
                )
                .frame(height: 130)
                .padding(6)
                .background(RoundedRectangle(cornerRadius: 12, style: .continuous).fill(Theme.paper))
                HStack(spacing: 6) {
                    Text(subject.title)
                        .font(.system(size: 16, weight: .semibold, design: .rounded))
                        .foregroundStyle(Theme.ink)
                    if model.progress.hasFinished(subject.id) {
                        Image(systemName: "checkmark.circle.fill")
                            .foregroundStyle(Theme.good)
                    }
                }
            }
            .padding(10)
            .frame(maxWidth: .infinity)
            .background(RoundedRectangle(cornerRadius: 18, style: .continuous).fill(Theme.card))
            .overlay(
                RoundedRectangle(cornerRadius: 18, style: .continuous)
                    .stroke(Theme.line, lineWidth: 1)
            )
        }
        .buttonStyle(.plain)
        .accessibilityLabel(subject.title)
    }
}
