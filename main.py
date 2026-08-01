#!/usr/bin/env python3
"""
Advanced Stream Player - Main Entry Point
"""

import sys
import os
import shutil

# Ensure the bundled/local MPV is discoverable even if PATH hasn't been refreshed
_MPV_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mpv")
_MPV_DIR = os.path.normpath(_MPV_DIR)
if os.path.isdir(_MPV_DIR) and _MPV_DIR not in os.environ.get("PATH", ""):
    os.environ["PATH"] = _MPV_DIR + os.pathsep + os.environ.get("PATH", "")

if __name__ == "__main__":
    # Create config directory if it doesn't exist
    config_dir = os.path.expanduser("~/.streamplayer")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    # Check for mpv CLI availability
    if not shutil.which("mpv"):
        print("[!] Warning: 'mpv' executable not found in PATH.")
        print("    Playback will not work until MPV is installed.")
        print("    Download MPV from: https://mpv.io/installation/")
        print("    The application will still launch so you can explore the UI.")
        print("")

    from ui import main
    main()