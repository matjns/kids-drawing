import AppKit
import SwiftUI

@MainActor
final class AppDelegate: NSObject, NSApplicationDelegate {
    func applicationDidFinishLaunching(_ notification: Notification) {
        NSWindow.allowsAutomaticWindowTabbing = false
    }

    func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool {
        true
    }

    func applicationSupportsSecureRestorableState(_ app: NSApplication) -> Bool {
        true
    }
}

@main
struct DrawWithMeApp: App {
    @NSApplicationDelegateAdaptor(AppDelegate.self) private var appDelegate
    @StateObject private var model = AppModel()

    var body: some Scene {
        WindowGroup("Draw With Me") {
            ContentView()
                .environmentObject(model)
                .frame(minWidth: 880, minHeight: 640)
        }
        .defaultSize(width: 1120, height: 780)
        .commands {
            CommandGroup(replacing: .newItem) {}
            CommandMenu("Draw") {
                Button("Next Step") { model.forward() }
                    .keyboardShortcut(.rightArrow, modifiers: [.command])
                    .disabled(model.lesson == nil || model.screen != .studio)
                Button("Previous Step") { model.back() }
                    .keyboardShortcut(.leftArrow, modifiers: [.command])
                    .disabled(model.lesson == nil || model.screen != .studio)
                Button("Show Finished Drawing") { model.showFinished() }
                    .keyboardShortcut(.return, modifiers: [.command])
                    .disabled(model.lesson == nil || model.screen != .studio)
                Button("Surprise Me") { model.surprise() }
                    .keyboardShortcut("r", modifiers: [.command])
                Button("All Drawings") { model.goHome() }
                    .keyboardShortcut("1", modifiers: [.command])
                Button("Find a Drawing") { model.focusSearch = true }
                    .keyboardShortcut("f", modifiers: [.command])
            }
        }
    }
}
