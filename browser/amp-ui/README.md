# Amp UI

A personal Chrome/Chromium extension for styling ampcode.com. It injects CSS
at page startup, with bundled Inter Variable fonts. There is no build step,
JavaScript content script, background process, or remote font request.

Inspired by [tjbai's Amp tweaks](https://github.com/tjbai/dotfiles/tree/main/firefox/amp-tweaks).
The starter uses its compact typography, 54rem transcript, flat user messages,
blue unread threads, and hidden selection toolbar/group status dots. Amp's
existing color theme stays active. Font assets come from that reference;
Inter is by Rasmus Andersson and is distributed under the SIL Open Font License
in `fonts/OFL.txt`.

## Install in Chrome

1. Open `chrome://extensions`.
2. Enable **Developer mode** in the top-right corner.
3. Click **Load unpacked** and select this folder, usually `~/dotfiles/browser/amp-ui`.
4. Refresh your Amp tab.

Leave this folder in place: Chrome loads the extension from it. An unpacked
extension remains installed across browser restarts. To undo the styling,
disable/remove **Amp UI** in the extensions page and refresh Amp.

On the original Mac, `~/amp-ui` links to this folder so the existing Chrome
installation path continues to work.

## Customize

Edit `custom.css`, then click the reload icon on **Amp UI** in
`chrome://extensions` and refresh your Amp tab. It loads after `amp.css`.

| Setting | Default | Example adjustment |
| --- | --- | --- |
| `--amp-ui-text-scale` | `0.92` | `1.1` for larger text |
| `--amp-ui-column-width` | `54rem` | `62rem` for more width |
| `--amp-ui-text-weight` | `450` | `400` for lighter text |
| `--amp-ui-paragraph-gap` | `0.9em` | `1.1em` for more space |
| `--amp-ui-selection-toolbar` | `none` | `flex` to restore |
| `--amp-ui-group-status` | `none` | `inline-flex` to restore |
| `--amp-ui-unread-color` | Amp's bright blue | Any CSS color |

To restore the user-message glow, remove the labeled block in `amp.css`.
The font scale and width variable override Amp's appearance settings while the
extension is active, including in full-width mode. Comment grids still use Amp's
full-width and expanded-comment layouts, matching TJ's reference.

## Preview

Open `preview.html` in a browser. It uses sample content and the same CSS to
compare the starter styling, light/dark themes, and narrow layouts. This is a
local preview, not a capture of your authenticated Amp session. The extension
does not inject any of the preview's JavaScript into Amp.

## Scope and maintenance

The manifest matches only `https://ampcode.com/*`, including the public site.
It has no additional API permissions. Bundled fonts are exposed only to that
origin. Chrome still describes site access when installing content styles.

Selectors are based on the reference extension's Amp DOM hooks. They avoid
generated Svelte class names, but Amp can still change those hooks. If a tweak
stops working, inspect the affected element and update its selector. The
comment layout additionally relies on Amp's inline `18rem` expanded gutter.

References: [Chrome content scripts](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts),
[loading an unpacked extension](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world#load-unpacked).
