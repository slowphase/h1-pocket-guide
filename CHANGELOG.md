# Changelog

Each entry gives the guide version and the h1 firmware build its text describes.

## v1.1.0, November 2026 · documents h1 v0.3.0 (4cff936)

Text updated to Jake Handy's guide for h1 v0.3.0 (jakehandy.com/h1, as of 21 November 2026). Same design, now 37 pages.

**New in the source, now in this edition**

- Two new instruments, each on its own page: **TILT** (electronic drum kits) and **PLUNK** (recorded drum kits). Sixteen instruments in all. The cover grid is now eight across, and the contents page lists all sixteen.
- **LAVA** has a ninth algorithm, **HOOVER**. It spans both columns on the LAVA page.
- A new **USB audio and MIDI** section in the intro (USB audio, MIDI in, MIDI out, USB host), and the source's matching line on the cover with a "How it works" link to it.
- New hold: **OCT − and OCT + for a second** turns the USB port into a host for a USB-MIDI keyboard.

**Changed in the source**

- Recorded loops are now **saved**: as soon as a take closes, and they survive a power-off. Updated in the reference (REC / PLAY), switching between loop and step, recording a loop (steps 3 and PLAY), writing steps, and the FAQ "Is my loop saved when I power off?" (the answer changed from No to Yes).
- **LAYERS** is on by default. The layers section is rewritten: each layer keeps its own instrument, algorithm, knobs, ENV and LFO; the screen shows REC: NEW LAYER and LAYER 2, 3…; up to sixteen layers; LOOP FULL at 1,024 notes. The SEQ + REC row and the recording note changed to match.
- **BARS** now goes to 128 (1 · 2 · 4 · 8 · 16 · 32 · 64 · 128) in both loop and step settings, and loop settings adds the 1,024-note limit.
- MIDI velocity: notes from a MIDI keyboard are recorded and played back with their velocity, and steps keep it too. MIDI CC 20–23 are also sent back out over USB.
- Smaller wording changes: "h1 (or handy-1)", "(LAVA has nine)" in the intro and reference, "Dots under the name show which one you are on", "Tap both together" for the middle octave.

**Unchanged** (checked line by line): the other fourteen instruments' descriptions, knobs and algorithms; all global settings pages; the metronome; the keyboard map; the screenshots.

**Layout**

- Sections 01–05 now take seven pages instead of five, so every page still keeps clear space above the footer. LAVA uses slightly tighter spacing (same type sizes) to fit its ninth algorithm.
- "(see layers)", "(see USB host)" and "See USB audio and MIDI" are now tappable, as they are on the website.
- **All fourteen FAQs** are now included, in the site's order, with answers copied from the live page (v1.0.0 had four). They take four pages, with the credits on the last.
- 41 bookmarks (USB audio and MIDI, TILT and PLUNK added).

## v1.0.0, November 2026 · documents h1 v0.2.1 (5b697e5)

First release.

- Jake Handy's h1 guide (jakehandy.com/h1, as of 18 November 2026) laid out as a 30-page dark PDF for the iPad mini in portrait (432 × 658 pt, the iPad mini's screen ratio).
- One page per instrument (all fourteen), plus intro, reference, sequencer, global settings, recording and FAQs.
- Tappable contents page, 38 bookmarks, and working links in every footer.
- Original wording and artwork unchanged. Four of the site's FAQs are included. The source differences are listed in [source/NOTES.md](source/NOTES.md).
- An edition stamp on the cover and final page gives the guide version and firmware build, so an old copy can't pass for current documentation.
