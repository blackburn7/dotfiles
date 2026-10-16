#!/usr/bin/env python3
"""Export the saved profile used by iTerm2's current session, plus global settings."""

import argparse
from pathlib import Path
import plistlib
import subprocess
import sys


TRANSIENT_PREFIXES = (
    "NoSync",
    "NSWindow Frame ",
    "NSNav",
    "NSSplitView Subview Frames ",
    "NSToolbar Configuration ",
)
TRANSIENT_KEYS = {
    "PrefsCustomFolder",
    "LoadPrefsFromCustomFolder",
    "SULastCheckTime",
    "SUUpdateGroupIdentifier",
    "SUUpdateRelaunchingMarker",
    "WindowNumber",
    "iTerm Version",
}


def active_profile_name():
    script = '''
if application id "com.googlecode.iterm2" is running then
    tell application id "com.googlecode.iterm2"
        tell current session of current window
            return profile name
        end tell
    end tell
else
    error "Open iTerm2 and select a session first, or pass --profile NAME."
end if
'''
    return subprocess.run(
        ["osascript", "-e", script], check=True, capture_output=True, text=True
    ).stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", help="Use a saved profile by name instead of the current session")
    args = parser.parse_args()
    profile_name = args.profile if args.profile is not None else active_profile_name()
    raw = subprocess.run(
        ["defaults", "export", "com.googlecode.iterm2", "-"],
        check=True, capture_output=True,
    ).stdout
    preferences = plistlib.loads(raw)
    matches = [p for p in preferences.get("New Bookmarks", []) if p.get("Name") == profile_name]
    if len(matches) != 1:
        raise ValueError(
            f"Expected one saved profile named {profile_name!r}, found {len(matches)}. "
            "Give the profile a unique name in iTerm2 before exporting."
        )
    profile = matches[0]
    exported = {
        key: value for key, value in preferences.items()
        if not key.startswith(TRANSIENT_PREFIXES) and key not in TRANSIENT_KEYS
    }
    exported["New Bookmarks"] = [profile]
    exported["Default Bookmark Guid"] = profile["Guid"]
    if exported.get("Default Browser Profile Guid") != profile["Guid"]:
        exported.pop("Default Browser Profile Guid", None)
    destination = Path(__file__).resolve().with_name("com.googlecode.iterm2.plist")
    contents = plistlib.dumps(exported, fmt=plistlib.FMT_XML, sort_keys=True)
    destination.write_bytes(contents)
    print(f"Saved {profile_name!r} (1 profile) and global preferences to {destination}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        detail = error.stderr
        if isinstance(detail, bytes):
            detail = detail.decode(errors="replace")
        sys.exit(detail.strip() if detail else str(error))
    except ValueError as error:
        sys.exit(str(error))
