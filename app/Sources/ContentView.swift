import DrawingCore
import SwiftUI

struct ContentView: View {
    @EnvironmentObject private var model: AppModel
    @FocusState private var searchFocused: Bool

    var body: some View {
        Group {
            if model.library == nil && model.loadError == nil {
                loadingView
            } else if model.library == nil {
                errorView
            } else {
                readyView
            }
        }
        .background(Theme.paper)
        .preferredColorScheme(.light)
        .onChange(of: model.focusSearch) { _, shouldFocus in
            if shouldFocus {
                searchFocused = true
                model.focusSearch = false
            }
        }
    }

    private var loadingView: some View {
        VStack(spacing: 16) {
            ProgressView()
                .controlSize(.large)
            Text("Opening the drawing book…")
                .font(.system(size: 22, weight: .semibold, design: .rounded))
                .foregroundStyle(Theme.ink)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }

    private var errorView: some View {
        VStack(spacing: 12) {
            Image(systemName: "book.closed")
                .font(.system(size: 42))
                .foregroundStyle(Theme.coral)
            Text("The drawing book couldn't be opened.")
                .font(.system(size: 26, weight: .bold, design: .rounded))
                .foregroundStyle(Theme.ink)
            if let loadError = model.loadError {
                Text(loadError)
                    .font(.system(size: 15, design: .rounded))
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                    .frame(maxWidth: 420)
            }
        }
        .padding(32)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }

    private var readyView: some View {
        VStack(alignment: .leading, spacing: 0) {
            header
                .padding(.horizontal, 24)
                .padding(.top, 18)
                .padding(.bottom, 12)
            if let notice = model.notice {
                noticeBanner(notice)
                    .padding(.horizontal, 24)
                    .padding(.bottom, 12)
            } else if !model.liveMatches.isEmpty {
                liveMatches
                    .padding(.horizontal, 24)
                    .padding(.bottom, 12)
            }
            Divider().overlay(Theme.line)
            if model.screen == .studio, model.lesson != nil {
                StudioView()
            } else {
                HomeView()
            }
        }
        .onChange(of: model.query) { _, _ in
            model.clearNotice()
        }
        .onAppear { searchFocused = true }
    }

    private var header: some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack(alignment: .firstTextBaseline) {
                Image(systemName: "pencil.and.outline")
                    .font(.system(size: 28, weight: .semibold))
                    .foregroundStyle(Theme.coral)
                VStack(alignment: .leading, spacing: 2) {
                    Text("Draw With Me")
                        .font(.system(size: 34, weight: .bold, design: .rounded))
                        .foregroundStyle(Theme.ink)
                    Text("Pick a word. Copy the lines on your paper.")
                        .font(.system(size: 16, weight: .medium, design: .rounded))
                        .foregroundStyle(.secondary)
                }
                Spacer()
                if !model.progress.finishedIDs.isEmpty {
                    Text("\(model.progress.finishedIDs.count) drawn")
                        .font(.system(size: 16, weight: .semibold, design: .rounded))
                        .padding(.horizontal, 14)
                        .padding(.vertical, 8)
                        .background(Capsule().fill(Theme.card))
                        .overlay(Capsule().stroke(Theme.line, lineWidth: 1))
                }
            }
            HStack(spacing: 10) {
                HStack(spacing: 8) {
                    Image(systemName: "magnifyingglass")
                        .foregroundStyle(.secondary)
                    TextField("Try cat, rocket, pizza…", text: $model.query)
                        .textFieldStyle(.plain)
                        .font(.system(size: 22, weight: .medium, design: .rounded))
                        .focused($searchFocused)
                        .onSubmit { model.submit() }
                }
                .padding(.horizontal, 16)
                .frame(minHeight: 52)
                .background(RoundedRectangle(cornerRadius: 16, style: .continuous).fill(Theme.card))
                .overlay(RoundedRectangle(cornerRadius: 16, style: .continuous).stroke(Theme.line, lineWidth: 1))

                Button("Draw") { model.submit() }
                    .buttonStyle(KidButtonStyle(fill: Theme.coral, foreground: .white))
                Button { model.surprise() } label: {
                    Label("Surprise me", systemImage: "sparkles")
                }
                .buttonStyle(KidButtonStyle(fill: Theme.card, foreground: Theme.ink, border: Theme.line))
            }
            if let saveWarning = model.saveWarning {
                Text(saveWarning)
                    .font(.system(size: 14, design: .rounded))
                    .foregroundStyle(Theme.hintInk)
            }
        }
    }

    private var liveMatches: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 8) {
                ForEach(model.liveMatches) { subject in
                    Button(subject.title) { model.open(subject) }
                        .buttonStyle(KidButtonStyle(fill: Theme.card, foreground: Theme.ink, border: Theme.line))
                }
            }
        }
    }

    private func noticeBanner(_ notice: Notice) -> some View {
        VStack(alignment: .leading, spacing: 10) {
            Text(notice.message)
                .font(.system(size: 22, weight: .bold, design: .rounded))
                .foregroundStyle(notice.isGentleRedirect ? Theme.hintInk : Theme.ink)
            if !notice.suggestions.isEmpty {
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack(spacing: 8) {
                        ForEach(notice.suggestions) { subject in
                            Button(subject.title) { model.open(subject) }
                                .buttonStyle(KidButtonStyle(fill: Theme.coral, foreground: .white))
                        }
                    }
                }
            }
        }
        .padding(16)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(
            RoundedRectangle(cornerRadius: 16, style: .continuous)
                .fill(notice.isGentleRedirect ? Theme.hint : Theme.card)
        )
    }
}
