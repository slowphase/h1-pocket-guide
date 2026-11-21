# h1 pocket guide: design notes and source discrepancies

**This edition (v1.1.0)** is built from the h1 guide at jakehandy.com/h1 for h1 v0.3.0 (4cff936, 20 November 2026). The source of truth for wording was a Firefox "Print to PDF" export of that page (21 November 2026), checked against the live page's text, including the FAQ answers the PDF export collapsed.

The first edition (v1.0.0, h1 v0.2.1, 5b697e5, 18 November 2026) was built from a Safari export. Its notes are kept below where they still apply.

## Design choices

**Page format.** 432 × 658 pt (6 × 9.14 in), the same 1 : 1.523 ratio as the iPad mini's 1488 × 2266 display, so each page fills the screen in portrait with no letterboxing. It's screen-first and not intended for A4 printing.

**Colour.** Background #17191E (charcoal, not black). Body text is a warm off-white (#EDE9E0, about 14:1 contrast). Secondary text is #B4B2AA (about 8:1) and labels are #8A8C92 (about 5:1). Panels and dividers are only a few steps lighter than the background. There's no transparency anywhere in the file, so it looks the same in every PDF viewer.

**Instrument accents.** The v0.2.1 printed guide showed each accent at about 67% brightness (COZY was #ab765c). Scaling back by 255/171 gives each instrument's artwork colour exactly (COZY #ffb089 matches the cat, TIDE #80d4ff the moon, PIP #c8ff4b the sprite). Those full-strength colours are used for the name, category, knob names, the line on each knob card and the artwork outline. BONK is the one exception: it would become pure white, the same as the body text, so it stays a light grey (#c9c9c9) like its artwork.

The v0.3.0 site now sets each accent at full strength in its CSS. TILT (#ff9630) and PLUNK (#96deff) are taken from there directly. The fourteen existing accents were left as they were; they match the site's values to within one or two steps, except BARD (site #f0c674, this edition #e9c070) and KOI (site #68ee96, this edition #64e691), which are a shade lighter on the site. That's a visible but small difference, and it's left alone so the existing pages don't change.

**Type.** These are the guide's own typefaces, embedded: Space Grotesk for reading text and headings, JetBrains Mono for labels, values, knob and algorithm names, and keycaps. Body text is 13.5 to 14.5 px on a 576 px-wide page (about 8 pt physical on an iPad mini). Text was never shrunk to make a page fit. Only spacing was adjusted.

PLUNK's intro ends with an emoji (😎). So that the build doesn't depend on whatever emoji font a machine has, that one glyph is subset from Noto Color Emoji (SIL OFL 1.1) into `fonts/noto-color-emoji-1f60e.woff2`. It's the only character drawn from a third font.

**Reusable components.**
- *Labelled rows* (reference, holds and combos, metronome, recording steps, and now USB audio and MIDI): the button, combination or topic is in a left column, and the explanation is on the right.
- *Knob rows* (all settings pages): a KNOB 1 to 4 badge, the setting name, its values on the right and the full description.
- *Instrument page*: artwork (184 pt) beside the name, category and intro, then the four knobs as a 2×2 grid of cards, then the algorithms in two numbered columns. An odd last algorithm (LAVA's ninth, HOOVER) spans both columns.
- *Keycaps*: FM-1 button names inside running text, exactly where the website shows them as keys.

**Navigation.**
- The cover thumbnails link to each instrument, and the cover's "How it works" goes to USB audio and MIDI.
- The contents page links all nine sections and all 16 instruments.
- Every footer has "← contents", a section label that jumps to the start of its section, and a page number that also goes to contents. The contents page's own footer goes back to the cover.
- In-text cross-references that the website links ("see layers", "see USB host", "See USB audio and MIDI", "See loop settings and step settings") are links here too.
- 41 nested bookmarks cover the sections, the 16 instruments, and the sub-sections of intro, reference, global settings and recording.
- Internal links are written as plain page jumps (not named destinations), so they work in Books, Preview, GoodNotes and Acrobat.
- All text is selectable and searchable, and all fonts are embedded and subset.

**Artwork.** The guide's own 480 × 480 PNGs, lossless and unchanged. The site's pictures are animated, so a PDF export captures whichever frame is showing. The v0.3.0 export caught different frames of the same fourteen pictures (no knob-label overlays, and a blank frame for KNOT), so the v1.0.0 captures, with their overlays such as "WOW" and "SPIN", were kept. TILT and PLUNK are new captures from the v0.3.0 export. The four screenshots (step pattern, notches, ARP page, EDIT strip) are pixel-identical in both exports.

**Layout changes in v1.1.0.** Only spacing and page breaks moved. The cover grid is eight across instead of seven, with the source's USB line under the tagline. The contents rows are 1 px tighter so a row of sixteen instruments fits. LAVA's page uses slightly smaller gaps (`.inst.dense`). Where sections split is set by `SPLIT_*` constants at the top of `build.py`.

## Edition stamp

Jake's own line, "Guide matches h1's current build, v0.3.0 (4cff936), 20 November 2026", is kept word for word. In a downloaded PDF the word "current" will eventually go out of date, so this edition adds a separate stamp on the cover and the final page: the pocket guide's own version, the h1 firmware build it documents, and a pointer to jakehandy.com/h1 for newer builds. The PDF filename and metadata carry the same two version numbers. Set them with `EDITION`, `FIRMWARE`, `FIRMWARE_HASH` and `FIRMWARE_DATE` at the top of `content.py`.

## Final page structure (37 pages)

| Pages | Content |
|---|---|
| 1 | Cover |
| 2 | Contents |
| 3 | 01 intro, USB audio and MIDI (USB audio, MIDI in) |
| 4 | USB audio and MIDI continued (MIDI out, USB host), 02 reference starts |
| 5 | reference, on the FM-1 continued, MASTER note |
| 6 | holds and combos |
| 7 | holds and combos continued, 03 switching between loop and step |
| 8 | 04 loop settings |
| 9 | 05 step settings |
| 10–25 | 06 the sixteen instruments, exactly one page each |
| 26–30 | 07 global settings (GLO, metronome, KEYS, FX, ENV, LFO, ARP, SEQ) |
| 31–33 | 08 recording (recording a loop; keyboard map and writing steps; writing steps continued and layers) |
| 34–37 | 09 FAQs (all fourteen), with credits and links on the last page |

## Source discrepancies and content not preserved

1. **FAQs.** The site has 14 questions. The PDF export captured them collapsed, without answers, so every answer was copied from the live page on 21 November 2026. All fourteen are included, in the site's order (v1.0.0 had only four, because the site couldn't be reached then). Their links (The Firmware Hub, GitHub, the simulator, fm1-browser-simulator, docs/SAMPLES.md, and "USB audio and MIDI") work as on the site. The install steps keep the site's line breaks.
2. **Apostrophes.** The source uses straight apostrophes throughout, now including the FAQ answers (v1.0.0 took its FAQ answers from a screenshot that showed curly ones). This edition follows the source.
3. **Accent colours.** As described above.
4. **Artwork versions.** As described above. The h1 GitHub repo (docs/img) has slightly different stills, without the knob-label overlays. The guide's own images were used.
5. **"handy-1" on the cover.** The live page's text includes "handy-1" beside the h1 wordmark, but it isn't visible in the PDF export, so the cover is unchanged. The intro's "h1 (or handy-1)" is included.
6. **Typo kept as written.** COZY's TOY algorithm reads "Bright, out of tune, short" with no full stop, exactly as in the source.
7. **"above".** The recording section says "see the GLOBAL page above", which refers to the website's layout. In this edition the global settings come before recording, so it still reads correctly, but the wording is unchanged either way.
8. **Cover buttons.** "Get it on The Firmware Hub", "Install on GitHub" and "open the simulator" were removed from the cover by the editor's choice. The three links are kept as plain text links in the credits on the final page, so no external link from the source is lost. The source's new cover line about USB audio and MIDI is included.
9. **Interactive web content.** The site's animated, knob-reactive visuals can only appear as stills.
10. **Bold and keys.** Emphasis and keycaps follow the source exactly. New in v0.3.0: the on-screen messages REC: NEW LAYER, LAYER 2, LAYER 3 and LOOP FULL are bold, as on the site; in the first layers paragraph only the first REC is a key, as on the site.
11. **Release link.** The build line links v0.3.0 (4cff936) to github.com/jakehandy/h1/releases/tag/v0.3.0, as the site does.

## Checks performed on the final PDF

- Every page rendered and inspected visually.
- Automated overflow check of every page (Playwright + Chrome). The tightest page has 14 px of clear space above the footer (LAVA).
- Word-level comparison of the v0.3.0 source PDF against the new PDF. Nothing is missing apart from the source's "+" expand icons. Everything extra is navigation, page numbers, the edition stamp and the FAQ answers.
- Each instrument appears on exactly one page with its intro, four knobs and all algorithms on that page.
- 193 links in total, all resolving: 174 internal page jumps and 19 external (10 distinct URLs).
- Fonts: Space Grotesk and JetBrains Mono, plus the one-glyph Noto Color Emoji subset. All embedded, no system fallback fonts.
- Rebuilding the unmodified v1.0.0 source reproduced the published v1.0.0 PDF's text exactly before any changes were made.
