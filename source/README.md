# h1 pocket guide: editable source

Everything needed to rebuild the PDF, for example when Jake's guide is updated for a newer h1. You don't need any of this to read the guide: the finished PDF is on the [Releases page](https://github.com/slowphase/h1-pocket-guide/releases).

## What's where

| Path | What it is |
| --- | --- |
| `content.py` | All the guide's text, transcribed verbatim, plus the instrument colours. **Edit the words here.** Set `EDITION` and `FIRMWARE` at the top. |
| `style.css` | The design system: page size, colours, type and components. |
| `build.py` | Assembles the pages, prints them with headless Chrome, then adds bookmarks, page links and metadata. |
| `img/` | The guide's original artwork and screenshots (Jake Handy). |
| `fonts/` | Space Grotesk and JetBrains Mono (SIL OFL 1.1). |
| `NOTES.md` | Design choices, page structure, source differences and the checks run on the PDF. |

Markup in `content.py`: `[[SEQ]]` makes a keycap and `**text**` makes emphasis.

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
2. Set `FIRMWARE` and `FIRMWARE_BUILD` to the new h1 build, and bump `EDITION`.
3. Rebuild with `--check`, look at every page, and make sure each instrument still fits on one page.
4. Add an entry to `CHANGELOG.md` and publish a new release with the PDF and source zip.

Check the result with `pdffonts` too. Only Space Grotesk and JetBrains Mono should be listed.
