[![Crowdin](https://d322cqt584bo4o.cloudfront.net/corsixth-for-android/localized.png)](https://crowdin.com/project/corsixth-for-android) [![Snapshot](https://github.com/alanwoolley/CorsixTH-Android/actions/workflows/build_and_sign.yml/badge.svg)](https://github.com/alanwoolley/CorsixTH-Android/actions/workflows/build_and_sign.yml)

# Theme Hospital — Thor Edition

An unofficial adaptation of **Theme Hospital for the AYN Thor**, built on CorsixTH and CorsixTH-Android.

Keep your hospital on the top screen while managing rooms, furniture, staff and hospital information on the bottom. Thor Edition adds touch gestures, controller support, expanded decoration tools and a redesigned interface for dual-screen play.

**You must supply your own original Theme Hospital game data. No original game data is included or downloaded by this project.**

## Features

### Dual-screen interface

- Hospital gameplay on the top screen, with management controls on the bottom.
- Swipe between management pages, including **Build, Furnish and Edit Rooms**.
- Continuous page cycling: swipe past either end to return to the opposite end.
- Enlarged dialogues, clearer text and improved use of the bottom screen.
- Larger, darker main-menu text and readability improvements for settings, tips and staff information.
- Refined hospital overview showing finances, reputation, patients, staff and treatment progress.
- Enlarged animated adviser and a more prominent hospital-opening clock.
- Optional trackpad controls on a dedicated Controls page.
- Video cutscenes routed to the top screen.

### Touch and controller controls

- Tap directly on the hospital view to select.
- Pinch to zoom.
- Use two fingers to pan.
- Long-press objects to access editing.
- Use a longer press on supported objects or walls to open decoration controls.
- While placing an object, hold with one finger and swipe or circle with another to rotate it.
- Controller support for navigation, selection, placement and camera control.

### Decorating your hospital

- Recolour supported furniture and wall surfaces.
- Secondary and tertiary colour options where supported by the asset.
- Floor and wall texture choices.
- Retain wall stripes where present.
- Paint individual sections, a whole wall run or a whole room.
- Optional vending-machine appearance packs, selectable through the furnishing interface.

Decoration support depends on the object and its animation layers; not every visible pixel is independently recolourable.

### Audio and optional enhancements

- Separate music and sound-effects volume controls.
- Reduced default music volume.
- Classic/remastered soundtrack selection when a compatible music pack is installed.
- Support for additional ambient receptionist announcements.
- Support for optional startup artwork and vending-machine skins.

**Enhancement support is included; the privately supplied music, voice recordings, title artwork and branded vending skins are not included in the public release.**

## Requirements

- AYN Thor is the primary target device.
- ARM64 Android device running **Android 8.1 or later**.
- Your own installed **full PC version of Theme Hospital**.
- English game-language data for the current importer.
- Enough free storage for the game files and a temporary import copy.

Other Android devices and display arrangements are not the primary testing target.

## Installation

1. Download the APK from this repository’s **Releases** section.
2. Install it on your Thor. Android may ask you to allow installation from your browser or file manager.
3. Start the app.
4. Follow the game-data import instructions.
5. After a successful import, select **Play Theme Hospital**.

### What game data should I provide?

On your computer, locate the installed game folder containing:

| Folder | Purpose |
|---|---|
| `DATA` | Core game graphics, animations and language data |
| `QDATA` | Additional game graphics and interface resources |
| `LEVELS` | Original level data |
| `SOUND` | Original music, sound effects and speech |
| `ANIMS` | Video files; include this for video playback |

The installation folder is often called **HOSP**. English language data includes `DATA/LANG-0.DAT`.

Copy that folder to your Thor, or compress it into a normal ZIP and transfer the ZIP. The importer accepts a ZIP with an enclosing installation folder and handles upper- or lowercase filenames.

Choose either:

- **Choose installed game folder**
- **Choose game-data ZIP**

**An installer EXE, disc image, save file or demo alone is not sufficient.** Install the full game on your computer first, then supply its installed data.

Imports are checked before replacing existing game data. Missing essential files produce an explanation so you can correct the selection.

After a successful import, the selected source folder or ZIP can be removed: the app keeps its own copy.

## Updating

**Install updates over the existing app. Do not uninstall first.**

Official updates using the same package ID and signing certificate retain:

- Imported game data.
- Saved hospitals.
- Settings.
- Previously installed optional enhancement assets.

You should not need to repeat the import after a normal update.

Uninstalling the app or clearing its Android storage removes its private data. Keep backups of important saves, especially when changing devices.

## Optional enhancement packs

Close the game, then long-press its launcher icon and select **Game data & packs**. Choose **Import optional enhancement pack (.zip)**.

This shortcut requires a launcher that supports Android app shortcuts. The pack-import option is also available after the initial game-data import.

Compatible packs can provide:

- Remastered music.
- Additional receptionist announcements.
- Startup artwork.
- Alternative vending-machine appearances.

Only supported asset files are imported. Packs cannot replace game scripts, native libraries, settings or saves.

Without a pack, the game uses its standard presentation and original soundtrack. Missing remastered tracks fall back to their classic versions.

See [the technical README](thor/README.md) for supported filenames and pack formats.

Only use or distribute enhancement assets for which you have the necessary permission. Owning Theme Hospital does not automatically grant redistribution rights for modified artwork, remastered music or third-party branding.

## Current release: 0.22

This release introduces public distribution with user-supplied game data:

- Clear first-start installation instructions.
- Folder and ZIP imports.
- Validation before replacing existing data.
- Recovery from an interrupted game-data installation.
- Separate engine updates and persistent game-data storage.
- Optional enhancement-pack importing.
- Public packages without original game data or private enhancement assets.
- Source distribution without signing credentials.

The build, importer logic and offscreen level/save-load checks have passed. Physical-device testing of the new Android file-picker and update flow remains important.

## Reporting problems

Please include:

- App version.
- Device model and Android version.
- Whether this was a fresh installation or an update.
- Steps to reproduce the problem.
- A screenshot or exact error message where possible.
- Whether optional enhancement packs are installed.

Please do not upload original game data, commercial installers or signing keys to issues or pull requests.

## Building from source

Build instructions are in [thor/README.md](thor/README.md).

The project uses Java, Python, the Android SDK and the Android NDK. Build scripts package a restricted public asset set and exclude original game data and private enhancement assets.

Release signing credentials are not distributed. A build signed with your own key cannot directly update an installed release signed with a different certificate.

## Licensing

This repository contains components under several licences. It should not be described as entirely MIT-licensed.

| Component | Licence |
|---|---|
| CorsixTH engine | MIT |
| CorsixTH-Android port | GPL-3.0-or-later |
| New Thor adaptation code covered by `THOR_LICENSE.txt` | MIT |
| FFmpeg configuration supplied with this release | LGPL-3.0-or-later |
| FreePats MIDI instrument samples | GPL-2.0-or-later, with a composition exception |
| DejaVu Sans font | Bitstream Vera/DejaVu terms |
| Other libraries | Their respective included licences |

The MIT licence for the Thor additions does not replace the licences or obligations of upstream components. Distribution of the combined Android port must comply with the applicable GPL and other dependency requirements.

Retain copyright and licence notices and make the corresponding source available when distributing the APK. Consult the actual licence files for their full terms.

Relevant files:

- [CorsixTH-Android licence](corsixth-android/LICENSE.txt)
- [CorsixTH licence](corsixth-android/jni/CorsixTH/LICENSE.txt)
- [Thor adaptation licence](thor/THOR_LICENSE.txt)
- [Third-party notices](thor/notices/)

### Original game assets and trademarks

Original Theme Hospital graphics, music, speech, videos and other game data are **not covered by this project’s open-source licences** and are not included in the public distribution.

Theme Hospital and third-party names, logos and trademarks remain the property of their respective owners.

This is an unofficial fan project. It is not affiliated with, endorsed by or supported by Electronic Arts, Bullfrog or AYN.

The software is provided without warranty, subject to the terms of its component licences.

## Credits

Built on the work of:

- [CorsixTH](https://github.com/CorsixTH/CorsixTH) and its contributors.
- [CorsixTH-Android](https://github.com/alanwoolley/CorsixTH-Android) and its contributors.
- The developers of SDL, SDL_mixer, FFmpeg, Lua, FreeType and the other included libraries.
- The FreePats and DejaVu projects.

Original Theme Hospital by Bullfrog Productions.

