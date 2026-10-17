# 🚀 Automated Release, Distribution & Auto-Update Guide

This guide documents the automated build, release, packaging, and in-app auto-update pipeline for **Obsidian Vocab Mobile Edition** (`com.vocabapp.obsidianstudio`).

---

## 📋 Architectural Overview

The repository utilizes a decoupled three-tier architecture:

```text
                  I MODIFY CODE OR DATA
                            │
                            ▼
              npm run version:bump 1.1.0
                            │
                            ▼
                     git push --tags
                            │
                            ▼
                      GitHub Actions
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
    release-mobile.yml              ios-distribution.yml
   (Android APK & AAB)             (TestFlight / App Store)
            │                               │
            ▼                               ▼
    GitHub Release v1.1.0            App Store Connect
   (ObsidianVocab-v1.1.0.apk)
            │
            ▼
    INSTALLED MOBILE DEVICES
  (In-App GitHub Releases Check)
            │
            ▼
    One-Tap APK Download & In-Place Update
```

---

## 🛠️ 1. Local Development

### Prerequisites
* **Node.js**: v18 or v20+
* **JDK**: OpenJDK 17 (Eclipse Temurin recommended)
* **Android SDK**: API 34+ with Command-line tools

### Running the App Locally
```bash
# Navigate to the application layer
cd "main app"

# 1. Install dependencies
npm install

# 2. Run Database verification
npm run verify-db

# 3. Start local development server & Live Watcher (localhost:3080)
npm run dev

# 4. Sync web assets into native Android container
npm run cap:sync

# 5. Build fresh Android debug APK locally
npm run cap:build
```

---

## 🏷️ 2. Version Management (Single Source of Truth)

The single source of truth for the entire application is:
[`main app/public/version.json`](file:///c:/Users/user/Desktop/Vocab%20app/main%20app/public/version.json)

```json
{
  "version": "1.0.0",
  "versionCode": 1,
  "name": "Obsidian Vocab",
  "releaseDate": "2026-10-02",
  "minAndroidSdk": 24,
  "targetAndroidSdk": 34,
  "githubRepo": "yorren005/vocab-app"
}
```

### Automated Version Synchronization
Do NOT manually edit multiple files. Use the automated bumper:

```bash
cd "main app"

# Patch release (e.g., 1.0.0 -> 1.0.1)
npm run version:bump patch

# Minor release (e.g., 1.0.0 -> 1.1.0)
npm run version:bump minor

# Major release (e.g., 1.0.0 -> 2.0.0)
npm run version:bump major

# Or specify exact version:
npm run version:bump 1.2.0
```

The script automatically:
1. Validates SemVer formatting.
2. Increments `versionCode`.
3. Synchronizes `main app/public/version.json`.
4. Synchronizes `main app/package.json`.
5. Syncs assets into `android/app/src/main/assets/public/` via `npx cap sync android`.
6. Dynamically feeds `android/app/build.gradle` so Gradle builds inherit the exact version and code automatically.

---

## 🤖 3. GitHub Actions CI/CD Pipeline

Three specialized workflows are located in [`.github/workflows/`](file:///c:/Users/user/Desktop/Vocab%20app/.github/workflows):

### 1. `build-and-test.yml` (Continuous Integration)
* **Trigger:** Every `git push` to `main` (excluding tags) and on `pull_request`.
* **Runner:** `ubuntu-latest`.
* **Actions:**
  - Validates markdown database structure and integrity (`npm run verify-db`).
  - Compiles in-memory vault index (`npm run index`).
  - Syncs assets to Capacitor Android (`npx cap sync android`).
  - Assembles Android Debug APK (`./gradlew assembleDebug`).
  - Uploads debug APK as a workflow artifact for rapid device testing.

### 2. `release-mobile.yml` (Production Mobile Releases)
* **Trigger:** Pushing a version tag (e.g. `git push origin v1.1.0`) or manual trigger via `workflow_dispatch`.
* **Runner:** `ubuntu-latest`.
* **Actions:**
  - Performs full pre-release validation (`verify-db` + `index`).
  - Synchronizes Capacitor assets.
  - Assembles production APK (`ObsidianVocab-vX.Y.Z.apk`).
  - Signs APK with production keystore if GitHub Secrets are configured (otherwise packages debug/ready APK).
  - Computes cryptographic SHA-256 checksums (`checksums.txt`).
  - Automatically generates release notes from git commit log.
  - Publishes official **GitHub Release** attaching both the `.apk` and `checksums.txt`.

### 3. `ios-distribution.yml` (Apple TestFlight & App Store)
* **Trigger:** Manual trigger via `workflow_dispatch`.
* **Runner:** `macos-latest`.
* **Status:** Ready for when the iOS platform target is added (`npm i @capacitor/ios && npx cap add ios`). Checks platform readiness and guides packaging via Xcode and App Store Connect API keys.

---

## 📲 4. In-App Mobile Auto-Update System

The mobile application embeds [`mobile-updater.js`](file:///c:/Users/user/Desktop/Vocab%20app/main%20app/public/js/mobile-updater.js) to provide a seamless update lifecycle:

```text
Application Launches (or user taps "Check for Updates" in Settings)
                           │
                           ▼
  Queries https://api.github.com/repos/yorren005/vocab-app/releases/latest
                           │
                           ▼
    Compares SemVer: Installed v1.0.0 vs Latest Release v1.1.0
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
   No Update Available            Update Available
    (Shows "Up to date")                  │
                                          ▼
                               Prompts with Update Banner & Modal
                               (Displays Release Notes & APK Size)
                                          │
                                          ▼
                               User Taps "Download & Install"
                                          │
                                          ▼
                        Android Download Manager downloads APK
                                          │
                                          ▼
                          Android Package Installer opens
                      "Do you want to update this app?
                       Your existing data will not be lost."
                                          │
                                          ▼
                             App Updated In-Place!
```

### Safety & Data Integrity Guarantees
* **Zero Data Loss:** Updating the APK preserves all `localStorage` state (study marks: 🟢 Learned, 🟡 Studying, 🔴 Unread), user themes, and typography preferences.
* **Offline Resilience:** If device is offline or GitHub API is throttled, the updater silently skips background checks and never interrupts user study.
* **No Embedded Secrets:** Uses GitHub's public read-only Releases REST API.

---

## 🔑 5. GitHub Actions Secrets Configuration

To configure production release signing, navigate to **GitHub Repository Settings ➔ Secrets and variables ➔ Actions** and add:

| Secret Name | Description | Required? |
| :--- | :--- | :--- |
| `ANDROID_KEYSTORE_BASE64` | Base64-encoded release `.keystore` / `.jks` file | Optional (fallback to ready APK) |
| `ANDROID_KEYSTORE_PASSWORD` | Password for the release keystore | Optional |
| `ANDROID_KEY_ALIAS` | Key alias in the release keystore | Optional |
| `ANDROID_KEY_PASSWORD` | Password for the specific key alias | Optional |
| `APP_STORE_CONNECT_KEY_ID` | App Store Connect API Key ID (for iOS) | Optional (for iOS TestFlight) |
| `APP_STORE_CONNECT_ISSUER_ID` | App Store Connect Issuer ID (for iOS) | Optional (for iOS TestFlight) |
| `APP_STORE_CONNECT_KEY_BASE64`| Base64-encoded `.p8` API key (for iOS) | Optional (for iOS TestFlight) |

> [!TIP]
> **How to create a release keystore for Android:**
> ```bash
> keytool -genkey -v -keystore release.keystore -alias vocabapp -keyalg RSA -keysize 2048 -validity 10000
> # Convert to base64 for GitHub Secrets:
> [Convert]::ToBase64String([IO.File]::ReadAllBytes("release.keystore")) | Set-Clipboard
> ```

---

## 🚀 6. Step-by-Step Production Release Procedure

When you are ready to ship an update:

```bash
# Step 1: Make your changes and test locally
npm run release:check

# Step 2: Bump the version (this automatically syncs all files and Android assets)
npm run version:bump 1.1.0

# Step 3: Commit the changes
git add -A
git commit -m "chore(release): v1.1.0"

# Step 4: Create and push the Git tag
git tag v1.1.0
git push origin main --tags
```

**That's it!** GitHub Actions will automatically take over, compile the native Android APK, create the GitHub Release, and your installed mobile users will detect and download the update.

---

## ❓ 7. Troubleshooting

| Issue | Cause | Resolution |
| :--- | :--- | :--- |
| **Build fails on `verify-db`** | Missing frontmatter, unclosed quotes, or broken hierarchy | Run `npm run verify-db` locally to inspect the exact failing note path. |
| **`gradlew` permission denied on GitHub Actions** | Missing execute bit in git index | Run `git update-index --chmod=+x android/gradlew` locally and push. |
| **Update check shows rate limit error** | Exceeded unauthenticated 60 requests/hr GitHub IP limit | The app throttles checks automatically every 12h. Wait a few minutes or download APK directly from GitHub Releases page. |
| **Android APK install error: "App not installed"** | Key mismatch (e.g. updating a debug-signed app with a release-signed app) | For in-place upgrades, the signing certificate must match. Ensure testing uses the same signing configuration. |
