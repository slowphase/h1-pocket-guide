# h1 pocket guide: design notes and source discrepancies

Built from the h1 guide at jakehandy.com/h1 (v0.2.1, 5b697e5, 18 November 2026), using a Safari "Print to PDF" export of that page as the source of truth for wording.

## Design choices

**Page format.** 432 × 658 pt (6 × 9.14 in), the same 1 : 1.523 ratio as the iPad mini's 1488 × 2266 display, so each page fills the screen in portrait with no letterboxing. It's screen-first and not intended for A4 printing.

**Colour.** Background #17191E (charcoal, not black). Body text is a warm off-white (#EDE9E0, about 14:1 contrast). Secondary text is #B4B2AA (about 8:1) and labels are #8A8C92 (about 5:1). Panels and dividers are only a few steps lighter than the background. There's no transparency anywhere in the file, so it looks the same in every PDF viewer.

**Instrument accents.** The printed guide shows each accent at about 67% brightness (COZY is #ab765c). Scaling back by 255/171 gives each instrument's artwork colour exactly (COZY #ffb089 matches the cat, TIDE #80d4ff the moon, PIP #c8ff4b the sprite). Those full-strength colours are used for the name, category, knob names, the line on each knob card and the artwork outline. BONK is the one exception: it would become pure white, the same as the body text, so it stays a light grey (#c9c9c9) like its artwork.

**Type.** These are the guide's own typefaces, embedded: Space Grotesk for reading text and headings, JetBrains Mono for labels, values, knob and algorithm names, and keycaps. Body text is 13.5 to 14.5 px on a 576 px-wide page (about 8 pt physical on an iPad mini). Text was never shrunk to make a page fit. Only spacing was adjusted.

**Reusable components.**
- *Labelled rows* (reference, holds and combos, metronome, recording steps): the button or combination is in a left column as keycaps, and the explanation is on the right.
- *Knob rows* (all settings pages): a KNOB 1 to 4 badge, the setting name, its values on the right and the full description. This keeps each setting tied to its physical knob without four cramped columns.
- *Instrument page*: artwork (184 pt) beside the name, category and intro, then the four knobs as a 2×2 grid of cards, then the eight algorithms in two numbered columns.
- *Keycaps*: FM-1 button names inside running text, as on the website.

**Navigation.**
- The cover thumbnails link to each instrument.
- The contents page links all nine sections and all 14 instruments.
- Every footer has "← contents", a section label that jumps to the start of its section, and a page number that also goes to contents. The contents page's own footer goes back to the cover.
- 38 nested bookmarks cover the sections, the 14 instruments, and the sub-sections of reference, global settings and recording.
- Internal links are written as plain page jumps (not named destinations), so they work in Books, Preview, GoodNotes and Acrobat.
- All text is selectable and searchable, and all fonts are embedded and subset.

**Artwork.** The guide's own 480 × 480 PNGs, lossless and reproduced unchanged. They're the guide's versions, including the knob-label overlays such as "WOW" and "SPIN". Each image is stored once and reused (cover, contents, instrument page). 480 px is the highest resolution available from the source, which is about 250 ppi at its size on the instrument pages.

## Edition stamp

Jake's own line, "Guide matches h1's current build, v0.2.1 (5b697e5), 18 November 2026", is kept word for word. In a downloaded PDF the word "current" will eventually go out of date, so this edition adds a separate stamp on the cover and the final page: the pocket guide's own version, the h1 firmware build it documents, and a pointer to jakehandy.com/h1 for newer builds. The PDF filename and metadata carry the same two version numbers. Set them with `EDITION` and `FIRMWARE` at the top of `content.py`.

## Final page structure (30 pages)

| Pages | Content |
|---|---|
| 1 | Cover |
| 2 | Contents |
| 3–5 | 01 intro, 02 reference (on the FM-1, holds and combos) |
| 6 | 03 switching between loop and step, 04 loop settings |
| 7 | 05 step settings |
| 8–21 | 06 the fourteen instruments, exactly one page each |
| 22–26 | 07 global settings (GLO, metronome, KEYS, FX, ENV, LFO, ARP, SEQ) |
| 27–29 | 08 recording (recording a loop, keyboard map, writing steps, layers) |
| 30 | 09 FAQs, credits and links |

## Source discrepancies and content not preserved

1. **FAQs.** The printed PDF captured all 13 FAQ questions collapsed, with no answers, and the live site couldn't be reached from the build environment. By the editor's choice, only these four are included, with answers transcribed from a screenshot of the site: "Why does nothing happen when I turn a knob on a settings page and then go home?", "A note is stuck. How do I stop it?", "Is my loop saved when I power off?" and "Why does the ALGORITHM knob change the picture so much?". The other nine questions are left out:
   - Can I put it on my FM-1 yet?
   - How will I install it?
   - How do I leave h1 again?
   - What if an install goes wrong?
   - Does it work on every FM-1?
   - Can I play it from a MIDI keyboard?
   - Does it work with a screen reader?
   - Does the simulator sound like the device?
   - Is it open source?
2. **Apostrophes.** The printed PDF uses straight apostrophes, and the FAQ screenshot shows curly ones. Each is kept as its source shows it.
3. **Accent colours.** As described above, the PDF's accent colours are about 67% of the artwork colours. The full-strength colours were used, as an editorial decision.
4. **Artwork versions.** The h1 GitHub repo (docs/img) has slightly different stills, without the knob-label overlays. The guide's own images were used.
5. **Damaged characters in the source PDF.** Safari's export broke some ligatures in the PDF's text layer (for example "se!ings", "o"", "di"erent", "cuto#"). These were transcribed as the words they display ("settings", "off", "different", "cutoff"), which is what the page shows visually.
6. **Typo kept as written.** COZY's TOY algorithm reads "Bright, out of tune, short" with no full stop, exactly as in the source.
7. **"above".** The recording section says "see the GLOBAL page above", which refers to the website's layout. In this edition the global settings come before recording, so it still reads correctly, but the wording is unchanged either way.
8. **Cover buttons.** "Get it on The Firmware Hub", "Install on GitHub" and "open the simulator" were removed from the cover by the editor's choice. The three links are kept as plain text links in the credits on the final page, so no external link from the source is lost.
9. **Interactive web content.** The site's animated, knob-reactive visuals can only appear as the stills the source PDF captured.
10. **Bold.** Emphasis follows the source exactly (for example "Home:", "On a page:", "Writing steps:", "The quick way.", "Reading the notches.", "The metronome."). Words the source sets in regular weight were left regular.

## Checks performed on the final PDF

- Every page rendered and inspected visually.
- Automated overflow check of every page (Playwright + Chrome). The tightest page has 21 px of clear space above the footer.
- Word-level comparison of the source PDF against the new PDF. The only differences are the nine omitted FAQ questions, navigation text, the added FAQ answers, and glitches in the source's text layer.
- Each instrument appears on exactly one page with all 27 to 28 of its text elements on that page.
- 148 links in total, all resolving: 143 internal page jumps and 5 distinct external URLs. Every footer word is a working link.
- Fonts: Space Grotesk and JetBrains Mono only, all embedded, with no system fallback fonts.
