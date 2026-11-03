// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "DrawingCore",
    platforms: [
        .macOS(.v14)
    ],
    products: [
        .library(name: "DrawingCore", targets: ["DrawingCore"])
    ],
    targets: [
        .target(
            name: "DrawingCore",
            path: "Sources/DrawingCore",
            resources: [
                .process("Resources")
            ]
        ),
        .testTarget(
            name: "DrawingCoreTests",
            dependencies: ["DrawingCore"],
            path: "Tests/DrawingCoreTests"
        )
    ]
)
