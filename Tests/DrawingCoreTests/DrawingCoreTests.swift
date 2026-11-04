import XCTest
@testable import DrawingCore

final class PathParserTests: XCTestCase {
    func testLineAndClose() throws {
        let commands = try parseSVGPath("M10 10 L20 20 Z")
        XCTAssertEqual(commands.count, 3)
        XCTAssertEqual(commands[0], .move(x: 10, y: 10))
        XCTAssertEqual(commands[1], .line(x: 20, y: 20))
        XCTAssertEqual(commands[2], .close)
    }

    func testRelativeLineReturnsToStartAfterClose() throws {
        let commands = try parseSVGPath("M10 10 L20 20 Z l 5 5")
        XCTAssertEqual(commands.last, .line(x: 15, y: 15))
    }

    func testImplicitLineAfterMove() throws {
        let commands = try parseSVGPath("M10 10 30 40")
        XCTAssertEqual(commands[1], .line(x: 30, y: 40))
    }

    func testHorizontalAndVertical() throws {
        let commands = try parseSVGPath("M0 0 H10 V20 h5 v-5")
        XCTAssertEqual(commands[1], .line(x: 10, y: 0))
        XCTAssertEqual(commands[2], .line(x: 10, y: 20))
        XCTAssertEqual(commands[3], .line(x: 15, y: 20))
        XCTAssertEqual(commands[4], .line(x: 15, y: 15))
    }

    func testJammedSignsAndDecimals() throws {
        let signed = try parseSVGPath("M10-20")
        XCTAssertEqual(signed[0], .move(x: 10, y: -20))
        let decimals = try parseSVGPath("M10.5.25")
        XCTAssertEqual(decimals[0], .move(x: 10.5, y: 0.25))
    }

    func testSmoothCubic() throws {
        let commands = try parseSVGPath("M0 0 C10 0 10 10 0 10 S-10 20 0 20")
        guard case .cubic(_, _, _, _, let x, let y) = commands.last else {
            return XCTFail("expected a cubic")
        }
        XCTAssertEqual(x, 0, accuracy: 0.001)
        XCTAssertEqual(y, 20, accuracy: 0.001)
    }

    func testQuadraticEndPoint() throws {
        let commands = try parseSVGPath("M0 0 Q10 20 20 0")
        guard case .cubic(_, _, _, _, let x, let y) = commands.last else {
            return XCTFail("expected a cubic")
        }
        XCTAssertEqual(x, 20, accuracy: 0.001)
        XCTAssertEqual(y, 0, accuracy: 0.001)
    }

    func testArcQuarterCircleBulgesDown() throws {
        let commands = try parseSVGPath("M100 0 A100 100 0 0 1 0 100")
        let points = commands.flattened(tolerance: 0.4)
        let mid = points[points.count / 2]
        XCTAssertEqual(mid.x, 70.7, accuracy: 3)
        XCTAssertEqual(mid.y, 70.7, accuracy: 3)
    }

    func testEmptyPathThrows() {
        XCTAssertThrowsError(try parseSVGPath("   "))
    }

    func testCircleBounds() throws {
        let commands = try parseSVGPath(
            "M 100 70 C 116.57 70 130 83.43 130 100 C 130 116.57 116.57 130 100 130 C 83.43 130 70 116.57 70 100 C 70 83.43 83.43 70 100 70 Z"
        )
        let box = try XCTUnwrap(commands.bounds())
        XCTAssertEqual(box.minX, 70, accuracy: 1)
        XCTAssertEqual(box.maxX, 130, accuracy: 1)
        XCTAssertEqual(box.minY, 70, accuracy: 1)
        XCTAssertEqual(box.maxY, 130, accuracy: 1)
    }
}

final class NormalizeTests: XCTestCase {
    func testPunctuationAndCase() {
        XCTAssertEqual(normalizeQuery("  Ice-Cream! "), "ice cream")
        XCTAssertEqual(normalizeQuery("cow's"), "cows")
        XCTAssertEqual(normalizeQuery("T-Rex"), "t rex")
    }
}

final class LibraryTests: XCTestCase {
    private var library: Library!

    override func setUpWithError() throws {
        let url = URL(fileURLWithPath: #file)
            .deletingLastPathComponent()
            .deletingLastPathComponent()
            .deletingLastPathComponent()
            .appendingPathComponent("Sources/DrawingCore/Resources/drawings.json")
        let data = try Data(contentsOf: url)
        library = try Library.load(from: data)
    }

    func testBookIsLargeEnough() {
        XCTAssertGreaterThanOrEqual(library.subjects.count, 60)
        XCTAssertEqual(library.formatVersion, 1)
        for category in Category.allCases {
            XCTAssertFalse(library.subjects(in: category).isEmpty, category.rawValue)
        }
    }

    func testEveryAliasMatchesItsSubject() {
        for subject in library.subjects {
            XCTAssertEqual(library.match(subject.id).matchedSubject?.id, subject.id)
            XCTAssertEqual(library.match(subject.title).matchedSubject?.id, subject.id)
            for word in subject.words {
                XCTAssertEqual(
                    library.match(word).matchedSubject?.id,
                    subject.id,
                    "\(word) should open \(subject.id)"
                )
            }
        }
    }

    func testSynonymsPluralsAndTypos() {
        XCTAssertEqual(library.match("kitty").matchedSubject?.id, "cat")
        XCTAssertEqual(library.match("kittens").matchedSubject?.id, "cat")
        XCTAssertEqual(library.match("cats").matchedSubject?.id, "cat")
        XCTAssertEqual(library.match("kat").matchedSubject?.id, "cat")
        XCTAssertEqual(library.match("puppy").matchedSubject?.id, "dog")
        XCTAssertEqual(library.match("mice").matchedSubject?.id, "mouse")
        XCTAssertEqual(library.match("leaves").matchedSubject?.id, "leaf")
        XCTAssertEqual(library.match("butterflies").matchedSubject?.id, "butterfly")
        XCTAssertEqual(library.match("ice-cream").matchedSubject?.id, "ice-cream")
        XCTAssertEqual(library.match("icecream").matchedSubject?.id, "ice-cream")
        XCTAssertEqual(library.match("aeroplane").matchedSubject?.id, "airplane")
        XCTAssertEqual(library.match("lorry").matchedSubject?.id, "truck")
        XCTAssertEqual(library.match("draw me a puppy").matchedSubject?.id, "dog")
        XCTAssertEqual(library.match("unicron").matchedSubject?.id, "unicorn")
        XCTAssertEqual(library.match("dragan").matchedSubject?.id, "dragon")
        XCTAssertEqual(library.match("horse").matchedSubject?.id, "horse")
        XCTAssertEqual(library.match("house").matchedSubject?.id, "house")
    }

    func testAmbiguousPrefixOffersChoices() {
        guard case .choices(_, let subjects) = library.match("plan") else {
            return XCTFail("plan should offer choices")
        }
        let ids = Set(subjects.map(\.id))
        XCTAssertTrue(ids.contains("airplane"))
        XCTAssertTrue(ids.contains("planet"))
    }

    func testCategoryWordBrowses() {
        XCTAssertEqual(library.match("animals"), .browse(.animals))
        XCTAssertEqual(library.match("space"), .browse(.space))
        XCTAssertEqual(library.match("car").matchedSubject?.id, "car")
    }

    func testUnknownAndBlockedAreGentle() {
        assertGentle(library.match("xyzzy"))
        assertGentle(library.match("gun"))
        assertGentle(library.match("boob"))
        assertGentle(library.match("crap"))
        assertGentle(library.match("butt"))
        assertGentle(library.match("ass"))
        assertGentle(library.match("shit"))
        assertGentle(library.match("cock"))
        XCTAssertNotEqual(library.match("gun").matchedSubject?.id, "sun")
        XCTAssertNotEqual(library.match("boob").matchedSubject?.id, "book")
        XCTAssertNotEqual(library.match("crap").matchedSubject?.id, "crab")
        XCTAssertNotEqual(library.match("butt").matchedSubject?.id, "butterfly")
        XCTAssertNotEqual(library.match("ass").matchedSubject?.id, "astronaut")
    }

    func testGreetingIsNotAScolding() {
        guard case .choices(let message, let subjects) = library.match("hello") else {
            return XCTFail("hello should offer ideas")
        }
        XCTAssertFalse(message == QueryOutcome.tryAnotherMessage)
        XCTAssertEqual(subjects.count, 3)
    }

    func testDrawingsStayOnThePage() {
        for subject in library.subjects {
            for step in subject.steps {
                XCTAssertGreaterThanOrEqual(step.instruction.count, 12, subject.id)
                for stroke in step.strokes {
                    let box = stroke.commands.bounds()
                    XCTAssertNotNil(box, subject.id)
                    if let box {
                        XCTAssertGreaterThanOrEqual(box.minX, -10, subject.id)
                        XCTAssertGreaterThanOrEqual(box.minY, -10, subject.id)
                        XCTAssertLessThanOrEqual(box.maxX, 210, subject.id)
                        XCTAssertLessThanOrEqual(box.maxY, 210, subject.id)
                    }
                }
            }
        }
    }

    func testSuggestionsUseDifferentCategories() {
        let picks = library.suggestions(seed: "xyzzy", count: 3)
        XCTAssertEqual(picks.count, 3)
        XCTAssertEqual(Set(picks.map(\.category)).count, 3)
    }

    func testSurpriseSkipsTheCurrentDrawing() {
        var generator = SplitMix64(seed: 99)
        let first = library.surprise(rng: &generator)
        var again = SplitMix64(seed: 7)
        let next = library.surprise(excluding: first.id, rng: &again)
        XCTAssertNotEqual(next.id, first.id)
    }

    func testMissingWidthDefaults() throws {
        let json = """
        {"formatVersion":1,"subjects":[{
          "id":"dot","title":"Dot","category":"everyday","words":["dot"],
          "steps":[
            {"instruction":"Draw a tiny dot on the page.","strokes":[{"d":"M10 10 L20 10"}]},
            {"instruction":"Draw another short line under it.","strokes":[{"d":"M10 20 L20 20"}]},
            {"instruction":"Close them with a last short line.","strokes":[{"d":"M15 10 L15 20"}]}
          ]
        }]}
        """.data(using: .utf8)!
        let book = try Library.load(from: json)
        XCTAssertEqual(book.subjects[0].steps[0].strokes[0].width, 4.6)
        XCTAssertFalse(book.subjects[0].steps[0].strokes[0].fill)
    }

    private func assertGentle(_ outcome: QueryOutcome, file: StaticString = #file, line: UInt = #line) {
        guard case .tryAnother(let message, let suggestions) = outcome else {
            return XCTFail("expected a gentle redirect", file: file, line: line)
        }
        XCTAssertEqual(message, "Let's try another one!", file: file, line: line)
        XCTAssertEqual(suggestions.count, 3, file: file, line: line)
    }
}

final class LessonTests: XCTestCase {
    func testForwardAndBack() throws {
        let subject = try sampleSubject()
        var lesson = LessonSession(subject: subject)
        XCTAssertEqual(lesson.stepIndex, 0)
        lesson.goForward()
        XCTAssertEqual(lesson.stepIndex, 1)
        lesson.goBack()
        XCTAssertEqual(lesson.stepIndex, 0)
        lesson.goBack()
        XCTAssertEqual(lesson.stepIndex, 0)
        lesson.goForward()
        lesson.goForward()
        XCTAssertEqual(lesson.stepIndex, subject.steps.count - 1)
        XCTAssertFalse(lesson.showingFinished)
        lesson.goForward()
        XCTAssertTrue(lesson.showingFinished)
        lesson.goForward()
        XCTAssertTrue(lesson.showingFinished)
        lesson.goBack()
        XCTAssertFalse(lesson.showingFinished)
        XCTAssertEqual(lesson.stepIndex, subject.steps.count - 1)
    }

    private func sampleSubject() throws -> Subject {
        let json = """
        {"formatVersion":1,"subjects":[{
          "id":"box","title":"Box","category":"everyday","words":["box"],
          "steps":[
            {"instruction":"Draw the first side of the box.","strokes":[{"d":"M10 10 L40 10"}]},
            {"instruction":"Draw the second side of the box.","strokes":[{"d":"M40 10 L40 40"}]},
            {"instruction":"Draw the rest of the box.","strokes":[{"d":"M40 40 L10 40 L10 10"}]}
          ]
        }]}
        """.data(using: .utf8)!
        return try Library.load(from: json).subjects[0]
    }
}

final class ProgressStoreTests: XCTestCase {
    func testRoundTripAndCorruptFile() throws {
        let directory = FileManager.default.temporaryDirectory
            .appendingPathComponent("draw-with-me-tests-\(UUID().uuidString)", isDirectory: true)
        let store = FileProgressStore(directory: directory)
        XCTAssertEqual(store.load(), DrawingProgress())
        var progress = DrawingProgress()
        progress.markFinished("cat")
        progress.markFinished("cat")
        progress.markFinished("rocket")
        progress.animateSteps = false
        try store.save(progress)
        let loaded = store.load()
        XCTAssertEqual(loaded.finishedIDs, ["cat", "rocket"])
        XCTAssertFalse(loaded.animateSteps)
        try Data("nope".utf8).write(to: store.fileURL)
        XCTAssertEqual(store.load(), DrawingProgress())
        try? FileManager.default.removeItem(at: directory)
    }
}
