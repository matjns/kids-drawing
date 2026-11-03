import DrawingCore
import Foundation

enum SupportDirectory {
    static func drawWithMe() -> URL {
        let fileManager = FileManager.default
        let base = fileManager.urls(for: .applicationSupportDirectory, in: .userDomainMask).first
            ?? fileManager.homeDirectoryForCurrentUser
                .appendingPathComponent("Library/Application Support", isDirectory: true)
        return base.appendingPathComponent("Draw With Me", isDirectory: true)
    }
}

enum BundledBook {
    static func load() -> Result<Library, Error> {
        do {
            guard let data = try locateData() else {
                return .failure(LibraryError.missingBook)
            }
            return .success(try Library.load(from: data))
        } catch {
            return .failure(error)
        }
    }

    private static func locateData() throws -> Data? {
        let fileManager = FileManager.default
        var urls: [URL] = []
        if let bundled = Bundle.main.url(forResource: "drawings", withExtension: "json") {
            urls.append(bundled)
        }
        let roots = [
            Bundle.main.resourceURL,
            Bundle.main.bundleURL,
            Bundle.main.executableURL?.deletingLastPathComponent(),
        ]
        for root in roots.compactMap({ $0 }) {
            urls.append(root.appendingPathComponent("drawings.json"))
            urls.append(root.appendingPathComponent("DrawingCore_DrawingCore.bundle/drawings.json"))
            urls.append(root.appendingPathComponent("DrawingCore_DrawingCore.bundle/Contents/Resources/drawings.json"))
            if let items = try? fileManager.contentsOfDirectory(at: root, includingPropertiesForKeys: nil) {
                for item in items where item.pathExtension == "bundle" {
                    urls.append(item.appendingPathComponent("drawings.json"))
                    urls.append(item.appendingPathComponent("Contents/Resources/drawings.json"))
                    if let nested = Bundle(url: item)?.url(forResource: "drawings", withExtension: "json") {
                        urls.append(nested)
                    }
                }
            }
        }
        if let executable = Bundle.main.executableURL,
           let walked = walk(from: executable.deletingLastPathComponent()) {
            urls.append(walked)
        }
        if let walked = walk(from: URL(fileURLWithPath: fileManager.currentDirectoryPath)) {
            urls.append(walked)
        }
        for url in urls where fileManager.fileExists(atPath: url.path) {
            return try Data(contentsOf: url)
        }
        return nil
    }

    private static func walk(from start: URL) -> URL? {
        var directory = start
        let fileManager = FileManager.default
        for _ in 0..<8 {
            let candidate = directory.appendingPathComponent("Sources/DrawingCore/Resources/drawings.json")
            if fileManager.fileExists(atPath: candidate.path) {
                return candidate
            }
            let parent = directory.deletingLastPathComponent()
            if parent.path == directory.path { break }
            directory = parent
        }
        return nil
    }
}
