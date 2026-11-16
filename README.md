# Theme Hospital Thor 0.22 — user-supplied game data

Unofficial Android / AYN Thor adaptation of CorsixTH. This public APK contains
no original Theme Hospital game-data archive. It retains the dual-screen UI,
touch gestures, controller mapping, decorating system, soundtrack selection,
volume controls, cutscene routing and optional enhancement-pack support.

## First start

1. Install your own full PC copy of Theme Hospital on a computer.
2. Locate the installation folder containing `DATA`, `QDATA`, `LEVELS` and
   `SOUND` (often called `HOSP`). This release expects English language data
   (`DATA/LANG-0.DAT`). Include `ANIMS` to enable the original videos.
3. Copy that folder to Android, or compress the folder into a normal ZIP and
   copy the ZIP. It is fine for the ZIP to contain a wrapper folder.
4. Start Thor and choose **Choose installed game folder** or **Choose game-data
   ZIP**. Use Android's file picker to select it. After validation, tap **Play
   Theme Hospital**.

An EXE, GOG/EA installer, ISO/disc image, save file or demo alone is not accepted.
Install/extract the full game first. This app does not download game data or
check purchase receipts. You remain responsible for permission to use the data.
Allow space for the imported data and a temporary import copy. Imports are
limited to 1.5 GB / 40,000 entries to reject accidentally selected large folders.
The importer reports missing essential files, rejects unsafe paths and duplicate
filenames, and normalises imported filenames. No all-files permission is needed.
Once import succeeds, the original selected folder/ZIP can be removed.

## Updating an existing installation

Install the new APK **over the existing app**. Keep the same application ID and
signing certificate. The supplied 0.22 APK uses the existing Thor certificate:
SHA-256 `85bfd2677d8190c24f4cc93e4c16e3568d3da81a85ed54690fa94fb62d09442e`.
(The authoritative fingerprint is also recorded in TEST_RESULTS_0.22.txt.)

Game data lives in private `files/hospital`, saves in `files/saves`, settings in
`files/config.txt`. These do not depend on the engine version marker. Engine
updates refresh `files/engine` and leave imported data, saves and optional assets
intact. Existing 0.21 private installations are recognised automatically. The
importer stages and validates replacements before committing them, with recovery
if the process stops during the directory switch. Failed validation does not
replace existing data. Updating never asks for a valid existing import again.

**Uninstalling or clearing app storage removes the private data.** Updating is
not uninstall/reinstall. Back up important saves before changing devices.

## Optional enhancement packs

The public APK and source exclude the privately supplied remastered tracks,
additional receptionist recordings, branded vending skins and title artwork.
Previously installed assets remain usable. Without packs, the original game
soundtrack is used and CorsixTH's standard menu artwork is shown. Selecting
Remastered without a music pack explains how to import one, rather than silently
pretending remastered music is playing.

Close the game, then long-press its launcher icon and select **Game data & packs**.
Choose **Import optional enhancement pack (.zip)**. The shortcut depends on
launcher support. On a fresh install this control is also shown after game-data
import. For development or launchers without shortcuts, the same screen can be
opened with `adb shell am start -n org.corsixth.thor/.SetupActivity --ez manage true`.
The importer refuses to modify files while the game activity is running.

Pack ZIP layout (one or more supported files, no scripts):

- `Music/ATLANTIS.mp3`, `CANDY.mp3`, `DOCTOR.mp3`, `FORTUNE.mp3`, `MEND.mp3`,
  `NIGHTSH.mp3`, `SIXSEVEN.mp3`, `STEADY.mp3` under that same Music folder.
- `Bitmap/receptionist.dat` and optionally `Bitmap/receptionist.json`.
- `Bitmap/thor_title.cthg`.
- `Bitmap/thor_vending.dat`.

These graphics/voice files must be in Thor's existing compiled asset format;
plain PNG or WAV files are not substitutes. Generic conversion scripts are in
`artwork`; their private input files are not supplied. The ZIP importer permits
only the named asset files, never Lua scripts, native libraries, saves or settings.
A partial music pack falls back to classic tracks where remasters are missing.
Import only assets you have permission to use and redistribute packs only with
appropriate permission. Importing a game copy does not license unrelated packs.

## Building

Required: Python 3, Java JDK (21 used here), Android SDK platform 35 and build-tools
35.0.0; Android NDK 26.3.11579264 for native rebuilds. Targets ARM64, Android 8.1+.
The source includes the existing native libraries and their source. Set
`THOR_USE_PREBUILT=1` only when using these unchanged libraries for Java/Lua work.
For native changes omit that setting to invoke ndk-build.

Set `ANDROID_HOME`, `ANDROID_NDK_HOME`, `JAVA_HOME`, and add Java's bin to PATH.
Supply an external key through `THOR_SIGNING_KEY`; supply passwords through
`THOR_STORE_PASSWORD` and `THOR_KEY_PASSWORD`. Run `python thor/build.py` from the
source archive root. Signing credentials are never generated or distributed.
Use your own key for your fork. It cannot update Tom's signed release; use a
separate app ID or explicitly migrate/back up data before replacing the app.

`build.py` stages an explicit public asset set. Even if local `assets/hospital.zip`
or optional private assets are present, they are not packaged. `prepare_assets.py`
only validates redistributable runtime resources; it cannot bundle game data.

`assets/music.zip` contains FreePats instrument samples and licences, not game
music. `assets/font.ttf` is DejaVu Sans. FFmpeg 5.1.3 source is included in
`third_party_sources`; its original Android build script is under
`corsixth-android/jni/ffmpeg`. Extract the tarball, run that script from the FFmpeg
source after setting its NDK path, and copy the resulting per-ABI include/lib
folders into the corresponding jni/ffmpeg ABI directory before ndk-build.

See `notices` and the upstream component licences. The Android port has GPL
requirements as well as CorsixTH's MIT licence: publish this source alongside the
APK and preserve those notices. This packaging is not a legal clearance of all
branding or possible distribution channels.

## Validation

See TEST_RESULTS_0.22.txt. Pure Java importer tests can run without Android:

    javac -d /tmp/thor-test thor/src/org/corsixth/thor/GameData.java thor/src/org/corsixth/thor/EnhancementPack.java thor/tests/GameDataTest.java
    java -cp /tmp/thor-test GameDataTest

Native offscreen tests exercise the clean public asset set, level loading and
save/reload with a locally supplied original installation. No original game
files or saves are included in test fixtures.
