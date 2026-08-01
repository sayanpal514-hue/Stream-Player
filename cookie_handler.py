#!/usr/bin/env python3
"""
Cookie Handler Module
"""

import json


class CookieHandler:
    def load(self, path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception:
            return {}
