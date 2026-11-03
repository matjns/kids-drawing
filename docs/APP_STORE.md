# Putting Draw With Me on the Mac App Store

The project is already set up for a normal Mac App Store app. These are the steps that still need an Apple Developer account and a Mac.

## Already done

- Bundle id `com.kidscomputer.drawing`
- Display name **Draw With Me**
- Version 1.0.0 (build 1)
- macOS 14 or newer, Apple silicon and Intel
- App icon (`Config/AppIcon.icns`)
- Sandbox entitlements with no network and no special files (`Config/DrawWithMe.entitlements`)
- Privacy manifest that says we collect nothing (`Config/PrivacyInfo.xcprivacy`)
- No accounts, ads, analytics, or web links
- Progress stays in Application Support on this Mac. The unsigned zip uses `~/Library/Application Support/Draw With Me/`. After App Store signing, macOS puts that folder inside the app's sandbox container. Same file, just a different parent folder.

The copy from `./build.sh` is unsigned, so the sandbox is not turned on yet. Signing with the entitlements file turns it on. The app still has no network code either way.

## 1. Apple setup

1. Enroll in the Apple Developer Program.
2. In Certificates, Identifiers & Profiles, register the App ID `com.kidscomputer.drawing` with the App Sandbox capability.
3. Create a Mac App Store provisioning profile for that App ID.
4. Create an App Store Connect record for Draw With Me, macOS, bundle id `com.kidscomputer.drawing`.

## 2. Build

On a Mac, from this folder:

```bash
./build.sh
```

That writes `dist/Draw With Me.app` and `dist/Draw With Me-mac-universal.zip`.

You can also open `app/Package.swift` in Xcode, pick the DrawWithMe scheme, and run it while you are changing the screens. The drawing book is loaded from the project folder when you run it that way.

## 3. Sign

Replace the certificate name with yours. The profile file comes from the developer site.

```bash
cp /path/to/Draw_With_Me.provisionprofile "dist/Draw With Me.app/Contents/embedded.provisionprofile"
codesign --force --deep --sign "Apple Distribution: Your Name (TEAMID)" \
  --entitlements Config/DrawWithMe.entitlements \
  --options runtime \
  "dist/Draw With Me.app"
```

## 4. Make the installer package and upload

```bash
productbuild --component "dist/Draw With Me.app" /Applications \
  --sign "3rd Party Mac Developer Installer: Your Name (TEAMID)" \
  "dist/DrawWithMe.pkg"
```

Open Transporter, sign in, and deliver `DrawWithMe.pkg`.

## 5. App Store Connect questions

- **Privacy nutrition label:** Data Not Collected. The app does not collect data.
- **Age rating:** 4+. There is no unrestricted web, no user-made public content, and no violence.
- **Export compliance:** The app does not use encryption. It does not connect to the network.
- **Category:** Education.
- **Screenshots:** Take them on a Mac after the app is running. A useful set is the drawing grid, a step with the new lines in blue, and the finished picture. The files in `docs/screenshots/` show the line art itself; they are not App Store screenshots of the window.
- **Review notes:** Offline drawing helper for children. No account. No network. Type a word such as cat, or tap Surprise me. Steps can be moved with the buttons or with Command-Left and Command-Right.

## Direct download instead of the store

The GitHub release zip is the unsigned app, same idea as Race Time. Parents open it with the steps in `README-mac.txt`. That build is not the App Store build. Do not turn on the launcher-style "quit other apps" behavior here; this app is meant to stay sandbox-friendly.
