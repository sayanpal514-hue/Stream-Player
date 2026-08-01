# Advanced Stream Player v2.0

> **EDUCATIONAL PURPOSE ONLY**
> This project is made purely for educational and learning purposes. It demonstrates how media streaming protocols, cookies, and DRM systems work at a conceptual level. The author does not endorse or encourage any unauthorized access to paid or protected content.

---

## Made By

**Sayan Pal**

---

## Overview

**Advanced Stream Player** is a Python-based command-line application that allows you to play online video streams using [MPV](https://mpv.io/) — one of the most powerful open-source media players available. It provides a clean, menu-driven terminal UI to play streams, pass authentication cookies, and explore DRM-protected content handling.

This project was built to understand how:
- Online video streaming protocols (HLS, DASH) work
- Browser cookies are used for authenticated playback
- DRM (Digital Rights Management) systems protect content
- Python can be used to wrap and control external media players

---

## Project Structure

```
Stream Player/
|
|-- main.py            # Entry point -- starts the app, checks MPV availability
|-- ui.py              # Terminal UI -- menus, user interaction, flow control
|-- player.py          # StreamPlayer class -- wraps MPV via subprocess
|-- cookie_handler.py  # CookieHandler class -- loads cookies from JSON files
|-- drm_handler.py     # DRMHandler class -- placeholder for DRM decryption logic
|-- config.json        # Local configuration file (can be empty initially)
`-- README.md          # This file
```

---

## How It Works

### 1. main.py -- The Entry Point
When you run `python main.py`, it:
1. Automatically adds the sibling `mpv/` folder to the system PATH (so MPV can be found even without a global install)
2. Checks if `mpv.exe` is available on the system
3. Creates the config directory `~/.streamplayer/` if it doesn't exist
4. Calls the `main()` function from `ui.py` to launch the interactive menu

---

### 2. ui.py -- The Terminal UI
The heart of the application. It presents a menu-driven interface:

```
+------------------------------------------+
|              MAIN MENU                   |
+------------------------------------------+
|  1.  Play Stream URL                     |
|  2.  Load Cookies & Play                 |
|  3.  Decrypt DRM & Play                  |
|  4.  Settings                            |
|  5.  Exit                                |
+------------------------------------------+
```

**Option 1 -- Play Stream URL:**
- You enter a direct video stream URL (e.g. an .m3u8 HLS link or .mpd DASH manifest)
- MPV is launched via player.py to play the stream
- No authentication is used

**Option 2 -- Load Cookies & Play:**
- You enter a stream URL and a path to a cookie file (JSON format)
- The cookie file path is passed to MPV via --cookies-file
- Useful for streams that require authentication (e.g. logged-in sessions)
- Cookies can be exported from your browser using extensions like EditThisCookie

**Option 3 -- Decrypt DRM & Play:**
- You enter a stream URL
- The DRMHandler attempts to decrypt it (currently a placeholder)
- In a real implementation, this is where Widevine/PlayReady key extraction would occur
- This feature is intentionally left unimplemented for educational reasons

**Option 4 -- Settings:**
- Set default MPV options (e.g. --volume=80 --fullscreen)
- Set a download path for future use
- Settings are saved to ~/.streamplayer/config.json

**Option 5 -- Exit:**
- Cleanly exits the application

---

### 3. player.py -- The Stream Player

Uses Python's subprocess module to launch mpv.exe with the provided stream URL.
Optionally passes --cookies-file if a cookie file is provided.
MPV handles all the heavy lifting: buffering, decoding, and rendering.

---

### 4. cookie_handler.py -- Cookie Loader

Reads a JSON cookie file from disk and returns the data as a Python dictionary.
Used to understand how browser sessions can be reused in scripts.

---

### 5. drm_handler.py -- DRM Handler (Placeholder)

Currently returns None with an informational message.
Represents the concept of DRM decryption (e.g. Widevine L3).
Intentionally not implemented -- DRM circumvention is illegal and unethical.

---

## Getting Started

### Prerequisites

| Requirement | Details                                    |
|-------------|--------------------------------------------|
| Python 3.9+ | https://www.python.org/downloads/          |
| MPV v0.41.0 | Portable -- included in ../mpv/ folder     |

### Running the App

```powershell
cd "D:\fancode scrapper\Stream Player"
python main.py
```

No pip install needed -- only Python standard library is used.

---

## What is HLS / DASH?

| Protocol | Full Name                               | Extension | Used By              |
|----------|-----------------------------------------|-----------|----------------------|
| HLS      | HTTP Live Streaming                     | .m3u8     | Apple, most CDNs     |
| DASH     | Dynamic Adaptive Streaming over HTTP    | .mpd      | YouTube, Netflix     |

Both protocols split video into small chunks served over plain HTTP. MPV plays both natively.

---

## What Are Stream Cookies?

When you log into a streaming website, your browser stores a session cookie -- a token that proves you are authenticated. Some streams require this token with each request.

This app lets you supply a cookie file so MPV can authenticate itself, just like your browser would.

NOTE: Using cookies from an account you do not own is unauthorized access and is illegal.

---

## What is DRM?

Digital Rights Management (DRM) is a technology used by platforms like Netflix, Disney+, and Amazon Prime to encrypt video streams so only licensed players can decrypt and play them.

Common DRM systems:
- Widevine (Google) -- used by Chrome, Android
- PlayReady (Microsoft) -- used by Edge, Windows
- FairPlay (Apple) -- used by Safari, iOS

This project's drm_handler.py is a stub that acknowledges DRM exists but does NOT implement decryption, as doing so without authorization violates laws like the DMCA.

---

## What You Can Learn From This Project

- How Python's subprocess module can wrap external CLI tools
- How streaming protocols (HLS/DASH) work conceptually
- How browser cookies are structured and used in HTTP requests
- How to build a clean terminal UI without any frameworks
- How DRM systems protect content at a high level
- Good Python project structure: separation of concerns across modules

---

## Legal & Ethical Disclaimer

This project is created strictly for educational purposes to understand how video streaming technology works.

- Do NOT use this tool to access content you are not authorized to view
- Do NOT use this tool to bypass DRM on commercial content
- Do NOT use this tool to scrape or redistribute copyrighted streams
- DO use this to learn about streaming protocols and Python programming
- DO test with your own self-hosted streams or publicly available test streams

The author bears no responsibility for any misuse of this software.

---

## Built With

- Python 3 -- Core logic and UI
- MPV -- Media playback engine (https://mpv.io)
- subprocess -- Python standard library for process management
- json -- Python standard library for config and cookie parsing

---

## License

This project is released for educational use only. No license is granted for commercial or unauthorized use.

---

Made with love by Sayan Pal for learning purposes.
