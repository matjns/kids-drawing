// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "DrawWithMe",
    platforms: [
        .macOS(.v14)
    ],
    products: [
        .executable(name: "DrawWithMe", targets: ["DrawWithMe"])
    ],
    dependencies: [
        .package(path: "..")
    ],
    targets: [
        .executableTarget(
            name: "DrawWithMe",
            dependencies: [
                .product(name: "DrawingCore", package: "DrawingCore")
            ],
            path: "Sources"
        )
    ]
)
