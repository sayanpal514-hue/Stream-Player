#!/usr/bin/env python3
"""
Stream Player Module
"""

import subprocess
import shutil


class StreamPlayer:
    def __init__(self):
        self.mpv_path = shutil.which("mpv")

    def play(self, url, cookies=None):
        if not self.mpv_path:
            print("  Error: mpv not found on system.")
            return

        cmd = [self.mpv_path]
        if cookies:
            cmd += ["--cookies-file", cookies]
        cmd.append(url)

        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError:
            print("  Error: playback failed.")
        except KeyboardInterrupt:
            print("\n  Playback stopped.")
