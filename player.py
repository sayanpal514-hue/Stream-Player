#!/usr/bin/env python3
"""
Stream Player Module
"""

import subprocess
import shutil


class StreamPlayer:
    def __init__(self, config=None):
        self.mpv_path = shutil.which("mpv")
        self.config = config or {}

    def play(self, url, cookies=None):
        if not self.mpv_path:
            print("  Error: mpv not found on system.")
            return

        cmd = [self.mpv_path]

        actual_url = url
        custom_headers = []
        if self.config.get("headers"):
            for k, v in self.config["headers"].items():
                custom_headers.append(f"{k}: {v}")

        user_agent = self.config.get("user_agent")

        if "|" in url:
            parts = url.split("|", 1)
            actual_url = parts[0]
            header_str = parts[1]
            for kv in header_str.split("&"):
                if "=" in kv:
                    k, v = kv.split("=", 1)
                    if k.lower() == "user-agent":
                        user_agent = v
                    else:
                        custom_headers.append(f"{k}: {v}")

        if user_agent:
            cmd.append(f"--user-agent={user_agent}")
            
        if custom_headers:
            headers_str = ",".join(custom_headers)
            cmd.append(f"--http-header-fields={headers_str}")
                
        if self.config.get("buffer_size"):
            cmd.append(f"--demuxer-max-bytes={self.config['buffer_size']}")

        if self.config.get("mpv_options"):
            cmd.extend(self.config["mpv_options"])

        if cookies:
            cmd += ["--cookies-file", cookies]
        cmd.append(actual_url)

        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError:
            print("  Error: playback failed.")
        except KeyboardInterrupt:
            print("\n  Playback stopped.")
