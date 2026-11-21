# -*- coding: utf-8 -*-
"""All guide text, transcribed verbatim from the h1 guide (jakehandy.com/h1, v0.3.0).
Markup used inside strings:  [[SEQ]] -> keycap,  **x** -> emphasis.
Only wording from the source goes in here."""

# Edition stamp: this layout's own version, and the firmware build the text describes.
EDITION = "1.1.0"
EDITION_DATE = "November 2026"
FIRMWARE = "v0.3.0"
FIRMWARE_HASH = "4cff936"
FIRMWARE_DATE = "20 November 2026"
FIRMWARE_BUILD = f"{FIRMWARE} ({FIRMWARE_HASH})"
REPO = "https://github.com/slowphase/h1-pocket-guide"
GUIDE_URL = "https://jakehandy.com/h1"

SITE = "https://jakehandy.com/"
LINK_HUB = "https://thefirmwarehub.com/firmware/h1/"
LINK_GITHUB = "https://github.com/jakehandy/h1/releases/latest"
LINK_SIM = "https://jakehandy.com/public/h1/simulator.html"
LINK_RELEASE = f"https://github.com/jakehandy/h1/releases/tag/{FIRMWARE}"

COVER = {
    "brand": "jakehandy.com / h1",
    "title": "h1",
    "tagline_b": "Custom firmware for the M-VAVE FM-1.",
    "tagline": "Sixteen instruments with themed dynamic visuals.",
    # the source's cover line; "How it works" links to the USB section
    "usb_b": "USB audio and MIDI.",
    "usb": "Record it straight into a computer or phone over one USB cable. MIDI in over USB and TRS, with velocity. MIDI out over USB.",
    "usb_link": "How it works",
    "links": [("Get it on The Firmware Hub", LINK_HUB), ("Install on GitHub", LINK_GITHUB), ("open the simulator", LINK_SIM)],
    "build": f"Guide matches h1's current build, {FIRMWARE_BUILD}, {FIRMWARE_DATE}. This page will change as h1 does.",
    "credit": "Not affiliated with M-VAVE. FM-1 is their product. · jakehandy.com",
}
COUNT_WORD = "Sixteen"          # used only in the cover tagline (source wording)
COUNT_LABEL = "sixteen"         # contents heading, "the sixteen instruments"

# accent colours exactly as used in the source guide
INSTRUMENTS = [
    {"id": "cozy", "name": "COZY", "cat": "lo-fi keys",
     "intro": "An electric piano with tines, one with reeds, a felted upright, a tape flute and vibes, all played back off a record that's been loved a bit too much.",
     "knobs": [("DUST", "Crackle and hiss."), ("WOW", "The record is warped."), ("MUFFLE", "A blanket over the speaker."), ("SWAY", "Tremolo, side to side.")],
     "algos": [("TINE", "A soft bar with a short bell on top."), ("REED", "Barks when you dig in."), ("FELT", "Detuned partials and a hammer thump."), ("TAPE", "An airy flute."),
               ("VIBES", "A bar with its fourth harmonic and a turning fan."), ("DUSK", "Two soft triangles. Fog."), ("TOY", "Bright, out of tune, short"), ("RADIO", "A small speaker with hum.")]},
    {"id": "orbit", "name": "ORBIT", "cat": "space",
     "intro": "Synths from a long way out: slow strings, a pulsar's ticking filter, tuned dust, radio from a dead probe, an endless riser, a hole.",
     "knobs": [("SWEEP", "The filter."), ("SPIN", "How fast everything that turns, turns."), ("SHIMMER", "Octaves glittering on top."), ("GRAVITY", "Notes sag and fall away when you let go.")],
     "algos": [("NEBULA", "Pitched noise."), ("DRIFT", "Slow strings."), ("PULSAR", "A filter that ticks and jumps."), ("COMET", "Always falling."),
               ("QUASAR", "A disc falling in."), ("RADIO", "Keyed like a number station."), ("WARP", "Three saws an octave apart, always climbing."), ("HOLE", "Nothing, with a bright edge.")]},
    {"id": "koi", "name": "KOI", "cat": "struck metal and wood",
     "intro": "Struck metal and wood over still water. Oh, and some koi.",
     "knobs": [("MALLET", "Soft felt to hard wood."), ("RIPPLE", "Two bars a hair apart."), ("LINGER", "How long it rings."), ("SINK", "Bends and dulls. Sinking.")],
     "algos": [("PAN", "A handpan."), ("TONGUE", "A tongue drum."), ("KALIMBA", "A kalimba."), ("MARIMBA", "A marimba."),
               ("DROPS", "Each note comes up to its pitch from below."), ("GAMELAN", "A gamelan bar."), ("BOWL", "A singing bowl, long."), ("RAIN", "Keeps landing while you hold it, octaves up, and harder the more you play.")]},
    {"id": "haunt", "name": "HAUNT", "cat": "spooky ambient",
     "intro": "Slow, cold, mostly air: a few sines drifting against each other, a wind that whistles at the note's pitch, and a lot of room. Also ghosts.",
     "knobs": [("FOG", "The wind."), ("DREAD", "Voices pull out of tune; a shadow a semitone above."), ("SHIVER", "A tremble in level and pitch."), ("DEPTH", "An octave below, and darker.")],
     "algos": [("SEANCE", "Plain and spooky."), ("CRYPT", "An octave down, detuned, hollow."), ("WRAITH", "Notes sag and waver."), ("STATIC", "A radio between stations."),
               ("CHOIR", "Voices sliding from OO to AH."), ("BELLS", "Struck, and they toll again (when they like)."), ("DEEP", "Two octaves down."), ("VOID", "Every swell runs backwards. Reality is drawn towards the infinite.")]},
    {"id": "tide", "name": "TIDE", "cat": "analog pad",
     "intro": "Detuned saws through a slow filter.",
     "knobs": [("GLOW", "Filter cutoff."), ("HALO", "Resonance."), ("DRIFT", "Detune and wander."), ("SURGE", "Slow swells of filter and level.")],
     "algos": [("MOON", "Warm saws with a sub."), ("SUN", "Brighter, an octave up."), ("ECLIPSE", "Pulses through a band-pass."), ("AURORA", "A shimmer that grows in."),
               ("STORM", "Noisy and wide."), ("FOG", "Breathy and muffled."), ("COMET", "Each note swoops in from an octave up."), ("ABYSS", "An octave down, dark. Underwater.")]},
    {"id": "pip", "name": "PIP", "cat": "chiptune",
     "intro": "An old friend of mine. Pulse waves, a stepped triangle, a little wave RAM and shift-register noise.",
     "knobs": [("SHAPE", "Pulse width, or the algorithm's own shape."), ("WOBBLE", "Vibrato that comes in after the note starts."), ("ZAP", "A pitch sweep into each note, down or up."), ("CRUNCH", "Lower sample rate and fewer bits.")],
     "algos": [("PULSE", "A square wave, width on SHAPE."), ("STAIRS", "The 16-step triangle, leaning towards a saw."), ("PWM", "The pulse width sweeps by itself."), ("TRIAD", "Every note is a chord, played one note at a time, very fast."),
               ("LEAP", "An octave blip in front of each note."), ("WAVE", "32 steps of 4-bit wave RAM, morphing through four shapes."), ("NOISE", "Shift-register noise, tuned by the key."), ("DUO", "Two pulses, detuned, then a fifth or an octave apart.")]},
    {"id": "bonk", "name": "BONK", "cat": "drum kit",
     "intro": "Twelve synthesised drums, one on every note of the octave. The octave you play in tunes the kit.",
     "knobs": [("TUNE", "Every drum up or down."), ("DECAY", "How long they ring."), ("PUNCH", "Pitch drop, click and drive."), ("DIRT", "Noise, grit and crushed samples.")],
     "algonote": "Bonk's a bit different. Each algorithm is a whole kit.",
     "algos": [("BOOM", "Deep, round and long."), ("SNAP", "Tight and bright."), ("DUST", "Soft and noisy."), ("WOOD", "High, short, knocking."),
               ("TIN", "Metallic and clangy."), ("TABLA", "Hits that bend upward."), ("ZAP", "Laser drops."), ("JUNK", "Clanks of filtered noise.")]},
    {"id": "urchin", "name": "URCHIN", "cat": "FM",
     "intro": "FM synthesis with style: two modulators crossfading under one carrier, wired eight different ways.",
     "knobs": [("RATIO", "Which overtones the modulator adds."), ("DEPTH", "How hard it modulates."), ("FUZZ", "Modulator feedback, towards noise."), ("TAIL", "How long the brightness, and the note, rings on.")],
     "algos": [("KEYS", "Electric piano."), ("BELL", "Two carriers at clashing ratios."), ("BASS", "An octave down, heavy modulation."), ("BRASS", "Swells and bite. Flares."),
               ("ORGAN", "A stack of harmonics, sustained."), ("GLASS", "High, glassy overtones."), ("METAL", "Ring modulation, inharmonic."), ("CHAOS", "Carrier feedback; it never plays it straight.")]},
    {"id": "twang", "name": "TWANG", "cat": "plucked strings",
     "intro": "Plucked strings, from recordings of real ones: harp, guitars, sitar, banjo, koto, bass, and a bowed cello.",
     "knobs": [("DAMP", "How soon the string dies, and how dull."), ("PICK", "Where it is plucked, middle to bridge."), ("TONE", "Soft thumb to hard nail."), ("BUZZ", "The string rattles on its bridge.")],
     "algos": [("HARP", "Long ringing strings on a curved neck."), ("NYLON", "Soft and warm, classical guitar."), ("TWELVE", "Each note doubled an octave up, in courses of two."), ("SITAR", "A buzzing bridge and a sympathetic drone."),
               ("BANJO", "Bright and short, picked near the bridge, across a drum."), ("KOTO", "Each note is pressed sharp and settles."), ("BASS", "An octave down, four thick strings."), ("BOW", "Keeps sounding while you hold the key. A cat's cradle.")]},
    {"id": "lava", "name": "LAVA", "cat": "wavefolder bass",
     "intro": "One oscillator through a wavefolder (drive it harder and the wave doubles back on itself, again and again), then a low-pass filter. This one is my favorite.",
     "knobs": [("FOLD", "How many times the wave folds."), ("HEAT", "The filter opens."), ("LEAN", "The fold goes lopsided."), ("SUB", "A sine an octave down.")],
     "algos": [("MOLTEN", "A folded sine."), ("ACID", "A saw with a resonant squelch."), ("SQUARE", "A folded pulse (LEAN sets its width)."), ("GROWL", "Two detuned saws, a moving filter."),
               ("REED", "A folded triangle, hollow and woody."), ("HOLLOW", "A sine that bends itself."), ("SHRED", "Folded twice, thin and bright."), ("QUAKE", "A filter wobble locked to the tempo."),
               ("HOOVER", "The rave one: two PWM saws a little apart, a swoop up into every note, a light fold. FOLD sets how far the sweep goes, LEAN how far apart the saws are. The lamp turns into a whirl.")]},
    {"id": "knot", "name": "KNOT", "cat": "additive bells",
     "intro": "Bells and pure tones built from sine partials, each dying away at its own rate.",
     "knobs": [("BLOOM", "The upper partials."), ("RING", "How long it rings."), ("TWIST", "Partials stretch out of tune."), ("WARP", "The partials bend each other.")],
     "algos": [("PURE", "Clean harmonic partials."), ("BELL", "Church bell partials."), ("GLASS", "High, inharmonic and short."), ("ORGAN", "Holds as long as you do."),
               ("GONG", "Low, washy, slow to bloom."), ("BOX", "A music box, tiny and bright."), ("CHIME", "Tubular chimes."), ("VOID", "An octave down, dark and long.")]},
    {"id": "ink", "name": "INK", "cat": "gliding lead",
     "intro": "A singing lead that slides to each pitch and shakes once it gets there, like a bowed string or a whistle.",
     "knobs": [("SLIDE", "How long a note takes to arrive."), ("SHAKE", "Vibrato."), ("PRESS", "Harder: brighter and thicker."), ("DRY", "Breath and scratch.")],
     "algos": [("BRUSH", "A saw lead."), ("REED", "Square and woody."), ("FLUTE", "Breathy sine."), ("ERHU", "Nasal, bowed, through a body."),
               ("WHISTLE", "Pure and airy."), ("THEREMIN", "A sine that bends itself."), ("FUZZ", "A distorted saw."), ("GLITCH", "Pitch moves only in jumps.")]},
    {"id": "bard", "name": "BARD", "cat": "medieval",
     "intro": "Eight old instruments over a drone, all from recordings of real ones: lute, harp, psaltery, gurdy, rebec, shawm, bagpipe and a little pipe organ.",
     "knobs": [("DRONE", "The bourdon under everything."), ("COURSE", "A second string, pipe or reed beside it."), ("BITE", "A harder quill or reed: brighter."), ("AGE", "Out of tune, breathy, dull.")],
     "algos": [("LUTE", "Plucked, warm and round."), ("HARP", "Plucked, long and open."), ("PSALTERY", "Plucked, bright and metallic."), ("GURDY", "A wheel turns the string, and the dog barks at the start of each note."),
               ("REBEC", "Bowed, with a vibrato that comes in late."), ("SHAWM", "A loud double reed."), ("BAGPIPE", "It can't stop (aaaahhhggg), and it flicks grace notes between yours."), ("ORGAN", "A little pipe organ.")]},
    {"id": "turbo", "name": "TURBO", "cat": "eighties",
     "intro": "The eighties (or so my dad says), at dusk, at speed: polysynth saws, an FM electric piano, slap bass and synth brass, all a little warped.",
     "knobs": [("CHORUS", "The oscillators spread apart."), ("TAPE", "Wow, flutter, a tired machine."), ("GLARE", "The filter opens."), ("DRIVE", "Pushed into the red.")],
     "algos": [("CRUISE", "Polysynth saws."), ("KEYS", "FM tine electric piano."), ("SLAP", "Slap bass."), ("BRASS", "Synth brass that scoops into the note."),
               ("MALL", "Slow, wide, half asleep."), ("LEAD", "A solo lead."), ("ARCADE", "Each note repeats every 16th an octave up, fading."), ("NIGHT", "A glass bell over a soft saw.")]},
    {"id": "tilt", "name": "TILT", "cat": "electronic drum kits",
     "intro": "Electronic drum kits (8-bit first) on a pinball table. See if you can activate the tilt.",
     "knobs": [("TUNE", "Every drum up or down."), ("DECAY", "How long they ring."), ("BOUNCE", "The pitch drops, then the hit comes back again and again, like a ball."), ("BITS", "Fewer samples, fewer levels.")],
     "algos": [("8BIT", "A sound chip."), ("ANALOG", "Sines and hiss, long."), ("HOUSE", "Short and hard."), ("FM", "One sine bends another."),
               ("ZAP", "Saws that dive."), ("GLITCH", "Never the same twice."), ("CLICK", "Tuned blips, hardly there."), ("RAVE", "Everything through the fuzz.")]},
    {"id": "plunk", "name": "PLUNK", "cat": "recorded drum kits",
     "intro": "Kits of recorded hits (gong, bells, darbuka, congas, timpani, anvil) on a steel tongue drum. Relaxing \U0001F60E",
     "knobs": [("TUNE", "Every hit up or down."), ("DECAY", "How long they ring."), ("WIND", "Each hit a little off its pitch and wavering, spread left to right."), ("STORM", "Every hit lands with a splash, harder. At the top, lightning.")],
     "algos": [("WORLD", "Darbuka and frame drum under bells, bars and a gong."), ("HANDS", "Congas, bongo, cajon, and what is shaken and clapped."), ("HALL", "The back row of an orchestra: bass drum, timpani, cymbal."), ("SHOP", "Whatever was lying about the workshop: anvils, brake drums."),
               ("CHIME", "Every hit a note. It snows."), ("TAPE", "WORLD slowed down, an octave lower and dull."), ("TINY", "HANDS, high and short, in a mist."), ("DICE", "Any hit of them all, anywhere. The rain falls upward.")]},
]

INSTRUMENT_NAMES = [d["name"] for d in INSTRUMENTS]
# Source guide prints each accent at ~67% brightness (e.g. COZY #ab765c). Scaling back by 255/171
# gives the artwork's own colour (COZY #ffb089 = the cat). BONK would become pure white, so it
# keeps a light grey close to its artwork.
SOURCE_COLORS = {
    "COZY": "#ab765c", "ORBIT": "#8a96ab", "KOI": "#439a61", "HAUNT": "#64ab8f", "TIDE": "#568eab",
    "PIP": "#86ab32", "BONK": "#ababab", "URCHIN": "#ab402b", "TWANG": "#ab8328", "LAVA": "#ab3071",
    "KNOT": "#836eab", "INK": "#ab9b83", "BARD": "#9c814b", "TURBO": "#9e40ab",
}
def _lift(h): return "#" + "".join(f"{min(255, round(int(h[k:k+2], 16) * 255 / 171)):02x}" for k in (1, 3, 5))
INSTRUMENT_COLORS = {n: _lift(h) for n, h in SOURCE_COLORS.items()}
INSTRUMENT_COLORS["BONK"] = "#c9c9c9"
# Added in v0.3.0. The live guide now sets each accent at full strength (CSS --c), so these are
# taken from it directly; they match the artwork the same way the lifted colours above do.
INSTRUMENT_COLORS["TILT"] = "#ff9630"
INSTRUMENT_COLORS["PLUNK"] = "#96deff"
for _d in INSTRUMENTS: _d["color"] = INSTRUMENT_COLORS[_d["name"]]

SWITCHING = {
    "intro": "One sequencer with two modes. **Loop** records what you play in real time. **Step** lets you place notes one step at a time (duh).",
    "rows": [
        (["hold", "[[SEQ]]"], "**The quick way.** Hold SEQ from anywhere and it swaps between LOOP and STEP. The new mode flashes up."),
        (["[[SEQ]]", "[[KNOB 1]]"], "**From the page.** Tap SEQ to open the sequencer page and turn KNOB 1 (MODE) to LOOP or STEP."),
    ],
    "note": "Bars and meter are shared between the two modes. The step pattern is saved with your settings, and a recorded loop is saved as soon as you close a take, even while it keeps playing.",
}

LOOP = {
    "intro": "Tap [[SEQ]] with MODE on LOOP. Four columns, one per knob:",
    "knobs": [
        ("MODE", "LOOP · STEP", "Which sequencer. Set it to LOOP."),
        ("BARS", "1 · 2 · 4 · 8 · 16 · 32 · 64 · 128", "How long a take is. The loop closes by itself when it gets there. A loop holds 1,024 notes across all its layers, however many bars it is."),
        ("METER", "4/4 · 3/4 · 5/4 · 6/8 · 7/8", "Beats in a bar. The click accents follow it: 6/8 is two groups of three, 7/8 is 2 + 2 + 3."),
        ("SNAP", "FREE · 1/16 · 1/8", "Quantize. FREE keeps your timing exactly, the others pull notes to the grid as you record."),
    ],
    "note": "Tempo is SELECT on the home screen, or TEMPO on the GLOBAL page. The line under the page title scrolls through the three sequencer hotkeys (HOLD SEQ, SEQ + REC, HOLD REC) and shows whether LAYERS is on.",
}

# All fourteen FAQs, in the site's order. The PDF export collapses them, so the answers were copied
# from the live page's FAQ text on 21 November 2026 (straight apostrophes, as on the site).
# An answer is a string, or a list of paragraphs; "\n" inside a paragraph is a line break.
# {{text|https://...}} is an external link, {{text|anchor}} an internal one, as on the site.
FAQS = [
    ("Can I put it on my FM-1 yet?",
     "Yep. h1 is live on {{The Firmware Hub|https://thefirmwarehub.com/firmware/h1/}}, where it installs in about a minute from Chrome or Edge. Every release is also {{on GitHub|https://github.com/jakehandy/h1/releases/latest}}, and you can play it first in my {{FM-1 browser sim|https://jakehandy.com/public/h1/simulator.html}}."),
    ("How will I install it?",
     ["I recommend {{The Firmware Hub|https://thefirmwarehub.com/firmware/h1/}}, in Chrome or Edge. Back up first: whatever the firmware you are leaving has saved (presets, projects, samples) may be gone or unreadable afterwards, so save it with that firmware's own backup. Charge the FM-1 and use a USB cable that carries data.",
      "1. If the FM-1 runs something older than stock V15, update it to V15 with M-VAVE's updater.\n2. Connect it over USB, open {{thefirmwarehub.com|https://thefirmwarehub.com/firmware/h1/}}, press Connect FM-1 and allow MIDI.\n3. Press Install on h1. It takes about a minute. Keep the cable in until the FM-1 restarts into h1.",
      "There's also a command-line installer in the repo. h1 is community firmware with no warranty and nothing to do with M-VAVE. Install at your own risk! (Though, it's pretty solid)"]),
    ("How do I leave h1 again?",
     "h1's package carries an update loader, so the same installers can replace it. For another custom firmware, press Install on its card at The Firmware Hub, or use that firmware's own installer. To go back to stock, press Back to official V15 in the Hub's Official firmware box. h1 only saves its own settings, so leaving it doesn't bring back what an earlier firmware had saved. That's what the backup is for."),
    ("What if an install goes wrong?",
     "If an install stops halfway, plug the FM-1 back in and press Install again, and the loader picks up where it stopped. If h1 fails to start twice, it comes up in SAFE MODE: no sound, but USB works, so the Hub can install h1 again, another firmware or V15. If nothing reaches it at all, hold REC while you switch it on. That's the chip's own update mode, and the Hub's rescue page takes it from there. The chip's bootloader is in ROM and can't be overwritten. After a start that crashed, h1 comes up once on default settings; your saved settings aren't erased."),
    ("Does it work on every FM-1?",
     "It's built to. Newer units use a different flash chip (0xB36014 instead of 0x856014), and h1 recognises both, so saves and updates work on either."),
    ("Why does nothing happen when I turn a knob on a settings page and then go home?",
     "The knobs do different jobs in different places: on the home screen they are always the instrument's four modulations, on a page they set that page's four columns. Hit HOME or the page's button to go back to playing."),
    ("A note is stuck. How do I stop it?",
     "Hold HOME. Everything goes silent. If HOLD is on (SEL lights), turn it off on the KEYS page or play a new chord to replace what is held."),
    ("Is my loop saved when I power off?",
     "Yes. From v0.3.0 the loop and all its layers are saved as soon as you close a take, even while it keeps playing, so give it a second or two before you switch off (a long loop takes a little longer). They come back when you turn the FM-1 on again. The step pattern and every instrument's knobs, algorithm and settings save by themselves."),
    ("Why does the ALGORITHM knob change the picture so much?",
     "On purpose. Each algorithm is a different character for the instrument, so the picture changes with it: TIDE's sky swaps a moon for a sun or a storm, BONK re-hangs its whole composition, TWANG's strings become a harp, a banjo or a cat's cradle. If you don't like it... sorry? There's plenty of other firmwares."),
    ("Can I play it from a MIDI keyboard?",
     "Yes. Notes in over USB or the TRS MIDI port play it at their velocity, CC 20 to 23 turn the four knobs, and CC 123 stops everything. With no computer, hold OCT − and OCT + for a second and a USB-MIDI keyboard can plug straight in (it needs its own power). MIDI out goes over USB on channel 1 (the TRS jack is input only), and there's no Bluetooth MIDI."),
    ("Can I record h1 straight into my computer or phone?",
     "Yes, from v0.2.2. Over USB the FM-1 shows up as an audio input: pick it in your DAW or recording app and you get the whole mix at the MASTER volume. The same cable carries MIDI both ways. More in {{USB audio and MIDI|usb}}."),
    ("Does it work with a screen reader?",
     "Yes. With fm1-reader, a screen reader hears the instrument, the algorithm, the page and every control's value even as you change it."),
    ("Does the simulator sound like the device?",
     "It runs the same code, so the synthesis and the pictures match as best as I can make them. But it's not running on the FM-1's speaker obviously, or its processor time and the feel of the clicking encoders. The ‹ › buttons beside each slider send single clicks, the way the real encoders step. It lives in its own repo, {{fm1-browser-simulator|https://github.com/jakehandy/fm1-browser-simulator}} (and can run other FM-1 firmwares, too!)."),
    ("Is it open source?",
     "The code is public at {{github.com/jakehandy/h1|https://github.com/jakehandy/h1}}. It's MIT licensed, and builds on fm1-base (MPL-2.0). The instrument recordings are public domain (CC0), listed in {{docs/SAMPLES.md|https://github.com/jakehandy/h1/blob/main/docs/SAMPLES.md}}. Its package identity is FM-1_481, and a release X.Y.Z answers FM-1_481XXYYZZ."),
]

# ------------------------------------------------------------------ 01 intro
INTRO = [
    "h1 (or handy-1) turns the FM-1 into sixteen instruments that feel simple but are deceptively complex. Each instrument sets the stage with a unique themed graphic that shifts and moves with everything you do: play a note for reactions, turn a knob and it changes shape. Explore. There's a lot in here.",
    "PRESETS picks the instrument. ALGORITHM picks one of its eight algorithms (LAVA has nine). We keep it simple with the four knobs working the live modulations for the instrument.",
    "Deeper settings live on small, consistent, nicely designed pages that make it clear what you're changing. Learn one page and you know them all.",
]

# ------------------------------------------------------------------ 01 intro: USB audio and MIDI (new in the source)
USB_TITLE = "USB audio and MIDI"
USB_INTRO = "Plug the FM-1 into a computer or a phone with a USB cable that carries data. It shows up as one device that's both an audio input and a MIDI port."
USB = [
    (["USB audio"], "Pick the FM-1 as the input in your DAW, recording app or sound settings and hit record. You get the whole mix at the MASTER volume, the same as the speaker. It only goes one way: the FM-1 isn't a sound card for the computer."),
    (["MIDI in"], "Over USB or the TRS jack, on any channel. Notes play the instrument in hand at their velocity: about 20 dB from softest to hardest, and darker the softer you play. CC 20 to 23 turn the four knobs, CC 123 stops everything. The FM-1's own keys still play at full."),
    (["MIDI out"], "Over USB only, on channel 1 (the FM-1's TRS jack is input only). Sends the notes from the keys, the arpeggiator and the sequencer, and CC 20 to 23 as the knobs turn, so a DAW can record your playing as MIDI or h1 can drive another synth. Notes and all-notes-off that came in over MIDI aren't sent back out, so a DAW that echoes its input won't loop."),
    (["USB host"], "No computer? Hold OCT − and OCT + together for a second and the USB port turns host: plug in a USB-MIDI keyboard or controller and play h1 from it. The screen shows its name when it connects. The FM-1 doesn't power the port, so the keyboard needs its own power, a powered hub or a powered OTG adapter. While it's a host there's no USB audio and no MIDI to a computer. Hold both again to go back. It's never saved, so the FM-1 always starts as a USB device."),
]

# ------------------------------------------------------------------ 02 reference
REF_ON_FM1 = [
    (["[[PRESETS]]"], "Next or previous instrument."),
    (["[[ALGORITHM]]"], "The instrument's eight algorithms (LAVA has nine). Each keeps its own four knob settings, so the knobs stand where you last left them on that algorithm. Dots under the name show which one you are on."),
    (["[[KNOB 1]]", "[[2]]", "[[3]]", "[[4]]"], "**Home:** the instrument's four live modulations. **On a page:** its four columns, left to right."),
    (["[[SELECT]]"], "**Home:** tempo. **On a page:** next or previous page. **Writing steps:** moves the step cursor."),
    (["[[FX]]", "[[SEL]]", "[[ENV]]", "[[LFO]]", "[[GLO]]", "[[ARP]]", "[[SEQ]]"], "Tap to open that settings page. The same button again, or HOME, goes back. GLO, SEQ, EDIT and HOME act when you let go, so holding one does only its hold (below) and never opens the page or pins the strip."),
    (["[[EDIT]]"], "Pins the knob names and values to the top of the home screen. **Writing steps:** leaves a rest."),
    (["[[REC]]", "[[PLAY]]"], "The sequencer. Loop: REC records a take, PLAY stops and starts it, and the loop is kept through a power-off. Step: REC turns step-write on and off, PLAY runs the pattern."),
    (["[[HOME]]"], "Back to the instrument. On the home screen it flashes the name again."),
    (["[[SAVE]]"], "Saves now. Everything saves by itself anyway."),
    (["[[OCT −]]", "[[OCT +]]"], "Octave down or up, two each way."),
    (["[[MASTER]]"], "Volume of everything. A ring in the middle of the screen shows it while it turns, marked GLOBAL."),
]
REF_MASTER_NOTE = "MASTER is one knob for two volumes, and it can only say where it stands. After you turn it with EDIT held, the volume of everything stays put until you turn MASTER (without EDIT) back through it. Until then the ring shows the volume that's held, and a small dot outside the ring shows where the knob is."
REF_HOLDS = [
    (["hold", "[[EDIT]]", "[[MASTER]]", "[[SELECT]]"], "Turn MASTER or SELECT while holding EDIT: the volume of the instrument in hand, 0 to 100 (it starts at full and only turns down), on the same ring, marked INSTRUMENT. MASTER sets it to where the knob stands, SELECT moves it a step a click. Works on the home screen, any settings page and while writing steps. Hold EDIT alone for a third of a second to see where it stands. It's saved with the instrument."),
    (["hold", "[[SEQ]]"], "Swaps the sequencer between LOOP and STEP, from anywhere, without opening the SEQ page."),
    (["hold", "[[GLO]]"], "Steps the metronome through CLICK REC, CLICK ON and CLICK OFF, without opening the GLOBAL page. A toast names the new setting."),
    (["[[SEQ]]", "+", "[[REC]]"], "Both together: LAYERS on and off. It's on by default. With it on, each take keeps its own instrument, algorithm and settings (see {{layers|layers}})."),
    (["hold", "[[REC]]"], "Clears the loop, or the step pattern. With LAYERS on, it clears what was recorded on the instrument in hand, and holding on to three seconds clears everything."),
    (["hold", "[[HOME]]"], "Silences everything (all notes off)."),
    (["hold", "[[SAVE]]"], "Resets the algorithm in hand: its four knobs go back to default."),
    (["hold", "[[SAVE]]", "2 s"], "Resets this instrument: every algorithm's knobs, its FX, ENV, LFO and ARP pages, and its volume."),
    (["hold", "[[SAVE]]", "4 s"], "Resets every instrument, plus the KEYS and GLOBAL pages. ALL RESET flashes up. The sequencer and what it holds are left alone."),
    (["[[OCT −]]", "+", "[[OCT +]]"], "Tap both together: back to the middle octave."),
    (["hold", "[[OCT −]]", "+", "[[OCT +]]"], "Hold both for a second: the USB port turns host for a USB-MIDI keyboard, or goes back to the computer (see {{USB host|usb}})."),
    (["MIDI CC 20–23"], "The four knobs, from a controller, and sent back out over USB as they turn. CC 123 is all notes off. See {{USB audio and MIDI|usb}}."),
]

# ------------------------------------------------------------------ 05 step settings
STEP = {
    "intro": "Tap [[SEQ]] with MODE on STEP. Same page, the last column changes:",
    "knobs": [
        ("MODE", "LOOP · STEP", "Set it to STEP."),
        ("BARS", "1 · 2 · 4 · 8 · 16 · 32 · 64 · 128", "Pattern length. A pattern holds up to 64 steps, so long bars of small steps get fewer bars, and the page shows how many you really have."),
        ("METER", "4/4 · 3/4 · 5/4 · 6/8 · 7/8", "Beats in a bar. Changes how many steps make a bar."),
        ("GRID", "1/8 · 1/16 · 1/32", "How long one step is. SWING on the GLOBAL page shuffles 1/8 and 1/16 grids."),
    ],
    "fig_caption": "a step pattern playing",
    "notch_caption": "the notches along the bottom, enlarged",
    "notches": "**Reading the notches.** Each notch is a step. Gaps split the bars, notches on a beat are taller, and a step that holds notes stands up. The step playing is brightest, and while you write, the cursor blinks under a dot.",
    "chords": "Each step holds up to eight notes, so chords work.",
}

# ------------------------------------------------------------------ 07 global settings
GLOBAL_INTRO = "Every settings page keeps the same layout to keep it simple. Four columns, each tied to the knob under it, left to right. SELECT steps to the next page. The same button or HOME goes back."
GLOBAL_FIGS = [("arp-page", "a settings page (ARP)"), ("edit-strip", "EDIT pins the knob strip")]
GLOBAL_PAGES = [
    ("GLO · GLOBAL (shared by every instrument)", "glo", [
        ("TEMPO", "40–240 BPM", "Also on SELECT from the home screen."),
        ("SWING", "0–100", "Shuffle for the arp and 1/8 or 1/16 steps."),
        ("TUNE", "−50 to +50", "Fine tuning, in cents."),
        ("BRIGHT", "20–100", "Screen brightness."),
    ]),
    ("SEL · KEYS (shared)", "keys", [
        ("ROOT", "C to B", "The scale's home note."),
        ("SCALE", "CHROM · MAJOR · MINOR · PENTA · MPENT · BLUES · DORIAN · WHOLE", "Keys will snap to the set scale (bye bye music theory)."),
        ("GLIDE", "0–100", "Portamento between notes."),
        ("HOLD", "OFF · ON", "Notes latch until your next chord. SEL stays lit while it is on."),
    ]),
    ("FX (per instrument)", "fx", [
        ("ECHO", "0–100", "Echo level."),
        ("TIME", "1/32 to 1/2", "Echo time, in tempo."),
        ("SPACE", "0–100", "Reverb."),
        ("TONE", "−50 to +50", "Darker or brighter."),
    ]),
    ("ENV (per instrument)", "env", [
        ("ATTACK", "", "How fast a note comes in."),
        ("DECAY", "", "How fast it falls to the sustain level."),
        ("SUSTAIN", "", "The level while you hold."),
        ("RELEASE", "", "How long it lasts after you let go."),
    ]),
    ("LFO (per instrument)", "lfo", [
        ("SHAPE", "SINE · TRI · RAMP · SQR · STEP · DRIFT", "The wave."),
        ("RATE", "0–100", "How fast."),
        ("DEPTH", "0–100", "How much."),
        ("TO", "PITCH · K1–K4 · LEVEL · PAN", "What it moves. K1–K4 show up as the instrument's own knob names."),
    ]),
    ("ARP (per instrument)", "arp", [
        ("MODE", "OFF · UP · DOWN · UPDN · RAND · ORDER · CHORD", "ORDER plays notes in the order you pressed them. CHORD repeats the whole chord; walking octaves."),
        ("RATE", "1/4 · 1/8 · 1/8T · 1/16 · 1/16T · 1/32", "Note length, in tempo."),
        ("RANGE", "1–4", "Octaves it climbs."),
        ("GATE", "5–100", "How long each note is held. ARP blinks on the beat while it runs."),
    ]),
]
METRONOME_INTRO = "**The metronome.** Hold [[GLO]] for about half a second to step through its three settings. The page shows the current one set (as in \"HOLD GLO: CLICK REC\")."
METRONOME = [
    (["CLICK REC"], "The default. It clicks while a take is armed, recording or overdubbing."),
    (["CLICK ON"], "It always clicks, even with nothing playing, and through loop and step playback."),
    (["CLICK OFF"], "It never clicks."),
]
METRONOME_NOTE = "The click follows METER."
SEQ_SHARED = "See loop settings and step settings."
PER_INSTRUMENT = "Per-instrument settings. The four knobs are remembered for each algorithm, and the algorithm and settings pages for each instrument, all saved by themselves a moment after you stop turning. Hold [[SAVE]] to reset the algorithm, keep holding to two seconds to reset the instrument, and to four seconds for everything."

# ------------------------------------------------------------------ 08 recording
REC_LOOP = [
    (["1 ·", "[[REC]]"], "Arms a take. REC blinks and the click starts counting straight away."),
    (["2 ·", "play"], "The take starts on your first note, lined up to the start of the bar the click is in. A line grows along the bottom of the screen. With CLICK OFF there's no bar to line up to, so it'll start exactly on your first note."),
    (["3 ·", "[[REC]]"], "Closes the loop and it plays back. Or let it run to BARS and it closes itself. The loop is saved as soon as it closes."),
    (["4 ·", "[[REC]]"], "While it plays: overdub. Play over the top and it adds to the loop. REC again goes back to just playing."),
    (["[[PLAY]]"], "Stops and starts the loop. Playing or stopped, the loop and its layers are there after you turn the FM-1 off and on."),
    (["hold", "[[REC]]"], "Clears it."),
]
REC_LOOP_NOTE = "Notes from a MIDI keyboard are recorded with their velocity and played back the same way. With LAYERS on (the default), switching instruments over a loop sets up a new layer, below. With it off, the loop plays notes, so it plays whatever instrument is up. SNAP on the SEQ page will quantize as you record. Hold GLO to set the metronome (see the GLOBAL page above)."
KEYBOARD_MAP = [
    "While the sequencer is running, the 16 white keys light up as a map of the pattern, left to right (same way FM-1's stock firmware does). A key is lit where its steps hold notes, and the step that's playing flips its key (lit goes dark, dark lights), so you can watch the position run across the keyboard. The cursor's key will blink while you're writing steps.",
    "Each key is one step for a pattern of up to 16 steps, two steps up to 32, three up to 48 and four up to 64. A loop shows the same way, counted in sixteenths: a 2-bar loop in 4/4 is 32 sixteenths (so two to a key).",
    "The map shows in STEP while the pattern plays, while you write, or with the SEQ page open. In LOOP it shows while you record, play or overdub, or with the SEQ page open while stopped. The rest of the time the keys light up for the notes that are sounding.",
]
WRITE_STEPS = [
    (["1 ·", "hold", "[[SEQ]]"], "Switch to STEP (if it is not already)."),
    (["2 ·", "[[REC]]"], "Step-write on. REC stays lit and the cursor blinks under the step it will write."),
    (["3 ·", "a key or chord"], "Lands on the blinking step. Up to eight notes per step."),
    (["[[EDIT]]"], "Leaves a rest and moves on."),
    (["[[SELECT]]"], "Moves the cursor back or forward, to fix a step."),
    (["[[PLAY]]"], "Runs the pattern. With write still on, whatever you play lands on the step going by. Yay live step recording!"),
    (["[[REC]]"], "Step-write off."),
    (["hold", "[[REC]]"], "Clears the pattern."),
]
WRITE_NOTE = "Step-write works from the home screen. The step pattern saves with your settings, so it'll still be there after you turn the FM-1 off and on. Steps keep the velocity of a MIDI keyboard too."
LAYERS = [
    "LAYERS lets you stack instruments into a whole track, and it's on by default. Record a loop, change the instrument, press [[REC]] and play over it: that take is a new layer. Record a bass line on TWANG, turn PRESETS to KOI, press REC and play a lead over it.",
    "Each layer keeps its own instrument, algorithm, four knobs, ENV and LFO, as they were when its take ended. So you can record a bass on COZY, turn the same COZY into a pad, and record over it: the bass stays a bass. Steps work the same way: each round of step-write is a layer.",
    "The screen keeps track. Changing instrument over a loop says **REC: NEW LAYER**, each take says **LAYER 2**, **LAYER 3** and so on, and a dot for each layer sits by the loop's progress line (the one recording blinks). Up to sixteen layers.",
    "Hold [[REC]] to clear only what was recorded on the instrument in hand (the toast says which). Keep holding to three seconds and everything clears. Press [[SEQ]] and [[REC]] together to turn LAYERS off, and everything recorded plays on whatever instrument or algorithm is on screen.",
    "A few limits. The effects are one chain that follows the instrument in hand. An instrument's volume is shared by its layers, so hold EDIT and turn MASTER or SELECT to sit one instrument under another. The eight voices are shared by all the layers, and each step still holds eight notes across all instruments. With ARP on, the loop records the notes the arpeggiator played. A loop holds 1,024 notes across all its layers; a note that doesn't fit says **LOOP FULL** instead of going missing.",
]
