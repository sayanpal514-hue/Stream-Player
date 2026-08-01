#!/usr/bin/env python3
"""
Advanced Stream Player - UI Module
"""

import sys
import os
from player import StreamPlayer
from drm_handler import DRMHandler
from cookie_handler import CookieHandler
import json


def load_config():
    """Load config from local project directory first, then user home."""
    # Try local config.json first
    local_config = os.path.join(os.path.dirname(__file__), "config.json")
    if os.path.exists(local_config):
        try:
            with open(local_config, "r") as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
        except Exception:
            pass

    # Fall back to user home config
    config_path = os.path.expanduser("~/.streamplayer/config.json")
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_config(config):
    config_dir = os.path.expanduser("~/.streamplayer")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    config_path = os.path.join(config_dir, "config.json")
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    clear_screen()
    print("")
    print("  +==========================================+")
    print("  |       Advanced Stream Player  v2.0       |")
    print("  +==========================================+")
    print("")


def print_menu():
    print("  +------------------------------------------+")
    print("  |              MAIN MENU                   |")
    print("  +------------------------------------------+")
    print("  |  1.  Play Stream URL                     |")
    print("  |  2.  Load Cookies & Play                 |")
    print("  |  3.  Decrypt DRM & Play                  |")
    print("  |  4.  Settings                            |")
    print("  |  5.  Exit                                |")
    print("  +------------------------------------------+")
    print("")


def prompt(label):
    """Helper to get user input with consistent styling."""
    return input("  {} > ".format(label)).strip()


def pause():
    """Wait for the user to press Enter."""
    input("\n  Press Enter to continue...")


def settings_menu(config):
    while True:
        print_banner()
        print("  +------------------------------------------+")
        print("  |               SETTINGS                   |")
        print("  +------------------------------------------+")
        print("  |  1.  Set Default MPV Options             |")
        print("  |  2.  Set Download Path                   |")
        print("  |  3.  Back to Main Menu                   |")
        print("  +------------------------------------------+")
        print("")

        choice = prompt("Choice")

        if choice == "1":
            print("")
            print("  Enter default MPV options (space separated):")
            print("  Example: --volume=80 --fullscreen")
            options = prompt("MPV Options")
            if options:
                config["mpv_options"] = options.split()
                save_config(config)
                print("\n  [OK] MPV options saved.")
            else:
                print("\n  [!] No options entered, nothing saved.")
            pause()

        elif choice == "2":
            print("")
            print("  Enter download path:")
            path = prompt("Path")
            if path:
                if os.path.isdir(path):
                    config["download_path"] = path
                    save_config(config)
                    print("\n  [OK] Download path set to: {}".format(path))
                else:
                    print("\n  [!] Path does not exist or is not a directory.")
            else:
                print("\n  [!] No path entered, nothing saved.")
            pause()

        elif choice == "3":
            break

        else:
            print("\n  [!] Invalid choice. Please enter 1, 2, or 3.")
            pause()


def play_with_url(player, url):
    """Play a URL without cookies."""
    if not url:
        print("\n  [!] No URL provided.")
        pause()
        return
    print("\n  [>>] Loading stream...")
    player.play(url)
    pause()


def play_with_cookies(player, cookie_handler, url):
    """Play a URL using a cookie file."""
    if not url:
        print("\n  [!] No URL provided.")
        pause()
        return

    print("")
    print("  Enter cookie file path:")
    cookie_path = prompt("Cookie file")

    if not cookie_path:
        print("\n  [!] No cookie file specified.")
        pause()
        return

    if not os.path.exists(cookie_path):
        print("\n  [!] Cookie file not found: {}".format(cookie_path))
        pause()
        return

    print("\n  [>>] Loading stream with cookies...")
    # Pass the file path directly to mpv's --cookies-file
    player.play(url, cookies=cookie_path)
    pause()


def play_with_drm(player, drm_handler, url):
    """Attempt DRM decryption then play."""
    if not url:
        print("\n  [!] No URL provided.")
        pause()
        return

    print("\n  [*] Attempting DRM decryption...")
    decrypted = drm_handler.decrypt(url)
    if decrypted:
        print("\n  [>>] Playing decrypted stream...")
        player.play(decrypted)
        pause()
    else:
        print("\n  [!] DRM decryption failed or is not supported.")
        pause()


def main():
    print_banner()
    print("  Initializing components...")

    config = load_config()
    player = StreamPlayer()
    cookie_handler = CookieHandler()
    drm_handler = DRMHandler()

    print("  [OK] Stream Player ready.")
    pause()

    while True:
        print_banner()
        print_menu()

        choice = prompt("Choice")

        if choice == "1":
            print_banner()
            print("  -- Play Stream URL --")
            print("")
            url = prompt("Stream URL")
            play_with_url(player, url)

        elif choice == "2":
            print_banner()
            print("  -- Load Cookies & Play --")
            print("")
            url = prompt("Stream URL")
            play_with_cookies(player, cookie_handler, url)

        elif choice == "3":
            print_banner()
            print("  -- Decrypt DRM & Play --")
            print("")
            url = prompt("Stream URL")
            play_with_drm(player, drm_handler, url)

        elif choice == "4":
            settings_menu(config)

        elif choice == "5":
            print_banner()
            print("  Goodbye!")
            print("")
            sys.exit(0)

        else:
            print("\n  [!] Invalid choice. Please enter 1-5.")
            pause()
