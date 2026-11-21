# h1 pocket guide: editable source

Everything needed to rebuild the PDF, for example when Jake's guide is updated for a newer h1. You don't need any of this to read the guide: the finished PDF is in [`downloads/`](../downloads/).

## What's where

| Path | What it is |
| --- | --- |
| `content.py` | All the guide's text, transcribed verbatim, plus the instrument colours. **Edit the words here.** Set `EDITION`, `FIRMWARE`, `FIRMWARE_HASH` and `FIRMWARE_DATE` at the top. |
| `style.css` | The design system: page size, colours, type and components. |
| `build.py` | Assembles the pages, prints them with headless Chrome, then adds bookmarks, page links and metadata. The `SPLIT_*` constants near the top set where long sections break across pages. |
| `img/` | The guide's original artwork and screenshots (Jake Handy). |
| `fonts/` | Space Grotesk and JetBrains Mono, plus a one-glyph subset of Noto Color Emoji for PLUNK's 😎 (all SIL OFL 1.1). |
| `NOTES.md` | Design choices, page structure, source differences and the checks run on the PDF. |

Markup in `content.py`: `[[SEQ]]` makes a keycap, `**text**` makes emphasis, and `{{text|anchor}}` makes an internal link (for example `{{layers|layers}}`).

## Building

Needs Python 3 and Google Chrome.

```
cd source
pip install -r requirements.txt
python3 build.py           # writes h1-pocket-guide-v<EDITION>-h1-<FIRMWARE>.pdf
python3 build.py --check   # also reports clear space above the footer on every page
```

`--check` uses Playwright with your installed Chrome. A negative number means a page overflows.

Page numbers, the contents page, footers and bookmarks are all worked out from the page order in `assemble()`, so moving where a section splits keeps everything in step.

## Updating for a newer h1

1. Update the wording in `content.py` from [jakehandy.com/h1](https://jakehandy.com/h1), keeping Jake's text exactly as he wrote it.
2. Set `FIRMWARE`, `FIRMWARE_HASH` and `FIRMWARE_DATE` to the new h1 build, and bump `EDITION`. Watch for FAQ answers: browser PDF exports collapse them, so copy them from the live page.
3. Rebuild with `--check`, look at every page, and make sure each instrument still fits on one page. If a page overflows, move a `SPLIT_*` boundary in `build.py` before touching spacing.
4. Add an entry to `CHANGELOG.md`, and add the new PDF and source zip to `downloads/` (keep the older ones).
5. Write the GitHub release notes in `release-notes/` (one file per guide version): what changed in h1 between the two documented builds, cross-checked against Jake's own h1 release notes, plus anything that couldn't be verified. Paste that file into the GitHub Release for the new guide version.

Check the result with `pdffonts` too. Only Space Grotesk, JetBrains Mono and the NotoColorEmoji subset should be listed.
