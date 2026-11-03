#!/usr/bin/env bash
# Build Draw With Me on a Mac, or run the logic tests anywhere Swift is installed.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

MODE="${1:-build}"

if [[ "$MODE" == "test" ]]; then
  swift test
  exit 0
fi

if [[ "$MODE" != "build" ]]; then
  echo "Usage: ./build.sh [build|test]" >&2
  exit 2
fi

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "Building the Mac app needs macOS. On this machine, run: ./build.sh test" >&2
  exit 1
fi

export MACOSX_DEPLOYMENT_TARGET=14.0

build_one() {
  local triple="$1"
  local bin_dir
  bin_dir="$(cd "$ROOT/app" && swift build -c release --triple "$triple" --product DrawWithMe --show-bin-path | tail -n 1)"
  if [[ ! -x "$bin_dir/DrawWithMe" ]]; then
    echo "Could not find DrawWithMe in $bin_dir" >&2
    exit 1
  fi
  echo "$bin_dir/DrawWithMe"
}

echo "Building arm64…"
ARM="$(build_one arm64-apple-macosx14.0)"
echo "Building x86_64…"
INTEL="$(build_one x86_64-apple-macosx14.0)"

DIST="$ROOT/dist"
APP="$DIST/Draw With Me.app"
rm -rf "$APP"
mkdir -p "$APP/Contents/MacOS" "$APP/Contents/Resources"

lipo -create "$ARM" "$INTEL" -output "$APP/Contents/MacOS/DrawWithMe"
chmod +x "$APP/Contents/MacOS/DrawWithMe"
cp "$ROOT/Config/Info.plist" "$APP/Contents/Info.plist"
cp "$ROOT/Config/PrivacyInfo.xcprivacy" "$APP/Contents/Resources/PrivacyInfo.xcprivacy"
cp "$ROOT/Sources/DrawingCore/Resources/drawings.json" "$APP/Contents/Resources/drawings.json"
cp "$ROOT/Config/AppIcon.icns" "$APP/Contents/Resources/AppIcon.icns"
printf 'APPL????' > "$APP/Contents/PkgInfo"

# Also drop the Swift package resource bundle next to the executable and in Resources.
# Bundle.module looks in both places. The loose drawings.json above is what the app loads first.
for bin in "$ARM" "$INTEL"; do
  bundle_dir="$(dirname "$bin")"
  if [[ -d "$bundle_dir/DrawingCore_DrawingCore.bundle" ]]; then
    cp -R "$bundle_dir/DrawingCore_DrawingCore.bundle" "$APP/Contents/Resources/"
    cp -R "$bundle_dir/DrawingCore_DrawingCore.bundle" "$APP/Contents/MacOS/"
    break
  fi
done

ZIP="$DIST/Draw With Me-mac-universal.zip"
rm -f "$ZIP"
STAGE="$(mktemp -d)"
cp -R "$APP" "$STAGE/"
cp "$ROOT/README-mac.txt" "$STAGE/"
(
  cd "$STAGE"
  zip -r -y -X "$ZIP" "Draw With Me.app" "README-mac.txt"
)
rm -rf "$STAGE"

echo "Built $APP"
echo "Zip   $ZIP"
