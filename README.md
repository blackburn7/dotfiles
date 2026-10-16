# dotfiles

My application configs and personal UI tweaks. Each app gets its own folder
with setup instructions.

| Folder | Contents |
| --- | --- |
| [browser/amp-ui](browser/amp-ui/) | Chrome extension for Amp typography and layout |
| [iterm2](iterm2/) | Active iTerm2 profile and global preferences |

## Set up a new machine

```sh
git clone https://github.com/blackburn7/dotfiles.git ~/dotfiles
```

Follow the README in each app's folder. The Amp extension is loaded directly
from `browser/amp-ui`; it needs no build step. iTerm2 settings are stored as a
readable XML plist.

## Save changes

Edit the Amp extension directly in `browser/amp-ui`. After changing iTerm2
settings, focus the session whose profile you want to save, then run:

```sh
python3 iterm2/export.py
git diff
git add browser/amp-ui iterm2
git commit -m "Update app configs"
git push
```

The iTerm2 exporter captures the saved profile used by the current session and
the global preferences. It exports exactly one profile each time. The repo is
a snapshot; nothing commits or pushes changes automatically.

On the original Mac, `~/amp-ui` links to `~/dotfiles/browser/amp-ui`, so Chrome's
existing unpacked-extension path continues to work.

## Add more configs

Create a folder named for the app, add its config files and restore instructions,
then add it to the table above. Keep machine-specific overrides in `local-only/`.

The Amp extension is based on [tjbai's Amp tweaks](https://github.com/tjbai/dotfiles/tree/main/firefox/amp-tweaks).
Its bundled Inter fonts include their license in `browser/amp-ui/fonts/OFL.txt`.
