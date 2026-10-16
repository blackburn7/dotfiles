# iTerm2

`com.googlecode.iterm2.plist` contains the saved **Default** profile used by the
active session at the initial export, plus global settings such as keyboard
shortcuts, tab/window appearance, and the custom color preset. The profile uses
Monaco at size 12. Other saved profiles are omitted.

The exporter removes window-position caches, recent-file locations, installation
metadata, and iTerm's `NoSync` runtime keys. It does not export terminal output,
shell history, Keychain entries, or session-only profile overrides.

## Restore

1. Open iTerm2 **Settings → General → Settings**.
2. Enable **Load settings from a custom folder or URL**.
3. Select this repo's `iterm2` directory, usually `~/dotfiles/iterm2`.
4. If asked which settings to use, choose the saved settings from the folder.
5. Restart iTerm2 to load them.

This loads the exported global settings and the single saved profile. Back up
any existing settings you want to retain before restoring on another machine.

See [iTerm2's settings documentation](https://iterm2.com/documentation-preferences-general.html#settings).

## Update the snapshot

Select the iTerm2 session whose saved profile you want to export, then run from
the repo root:

```sh
python3 iterm2/export.py
```

To export a specific saved profile without using the current session:

```sh
python3 iterm2/export.py --profile Default
```

Profile names must be unique. Each export replaces the snapshot with exactly
one profile, sets that profile as the exported default, and retains the global
settings. Your live iTerm2 preferences are not changed. Review and commit the
resulting diff to save it in GitHub.
