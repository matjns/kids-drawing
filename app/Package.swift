// swift-tools-version:5.9
import Foundation
import PackageDescription

// SwiftPM names a local package after its folder, so the parent package's
// identity is whatever the checkout folder is called (for example
// "kids-drawing" on CI). Work it out here so the build does not depend on it.
let corePackage = URL(fileURLWithPath: Context.packageDirectory)
    .deletingLastPathComponent()
    .lastPathComponent
    .lowercased()

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
                .product(name: "DrawingCore", package: corePackage)
            ],
            path: "Sources"
        )
    ]
)
