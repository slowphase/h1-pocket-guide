# -*- coding: utf-8 -*-
"""All guide text, transcribed verbatim from the h1 guide (jakehandy.com/h1, v0.2.1).
Markup used inside strings:  [[SEQ]] -> keycap,  **x** -> emphasis.
Only wording from the source goes in here."""

# Edition stamp: this layout's own version, and the firmware build the text describes.
EDITION = "1.0.0"
EDITION_DATE = "November 2026"
FIRMWARE = "v0.2.1"
FIRMWARE_BUILD = "v0.2.1 (5b697e5)"
REPO = "https://github.com/slowphase/h1-pocket-guide"
GUIDE_URL = "https://jakehandy.com/h1"

SITE = "https://jakehandy.com/"
LINK_HUB = "https://thefirmwarehub.com/firmware/h1/"
LINK_GITHUB = "https://github.com/jakehandy/h1/releases/latest"
LINK_SIM = "https://jakehandy.com/public/h1/simulator.html"
LINK_RELEASE = "https://github.com/jakehandy/h1/releases/tag/v0.2.1"

COVER = {
    "brand": "jakehandy.com / h1",
    "title": "h1",
    "tagline": "Custom firmware for the M-VAVE FM-1. Fourteen instruments with themed dynamic visuals.",
    "links": [("Get it on The Firmware Hub", LINK_HUB), ("Install on GitHub", LINK_GITHUB), ("open the simulator", LINK_SIM)],
    "build": "Guide matches h1's current build, v0.2.1 (5b697e5), 18 November 2026. This page will change as h1 does.",
    "credit": "Not affiliated with M-VAVE. FM-1 is their product. · jakehandy.com",
}

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
               ("REED", "A folded triangle, hollow and woody."), ("HOLLOW", "A sine that bends itself."), ("SHRED", "Folded twice, thin and bright."), ("QUAKE", "A filter wobble locked to the tempo.")]},
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
]

INSTRUMENT_NAMES = "COZY ORBIT KOI HAUNT TIDE PIP BONK URCHIN TWANG LAVA KNOT INK BARD TURBO".split()
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
for _d in INSTRUMENTS: _d["color"] = INSTRUMENT_COLORS[_d["name"]]

SWITCHING = {
    "intro": "One sequencer with two modes. **Loop** records what you play in real time. **Step** lets you place notes one step at a time (duh).",
    "rows": [
        (["hold", "[[SEQ]]"], "**The quick way.** Hold SEQ from anywhere and it swaps between LOOP and STEP. The new mode flashes up."),
        (["[[SEQ]]", "[[KNOB 1]]"], "**From the page.** Tap SEQ to open the sequencer page and turn KNOB 1 (MODE) to LOOP or STEP."),
    ],
    "note": "Bars and meter are shared between the two modes. The step pattern is saved with your settings; a recorded loop is not.",
}

LOOP = {
    "intro": "Tap [[SEQ]] with MODE on LOOP. Four columns, one per knob:",
    "knobs": [
        ("MODE", "LOOP · STEP", "Which sequencer. Set it to LOOP."),
        ("BARS", "1 · 2 · 4 · 8", "How long a take is. The loop closes by itself when it gets there."),
        ("METER", "4/4 · 3/4 · 5/4 · 6/8 · 7/8", "Beats in a bar. The click accents follow it: 6/8 is two groups of three, 7/8 is 2 + 2 + 3."),
        ("SNAP", "FREE · 1/16 · 1/8", "Quantize. FREE keeps your timing exactly, the others pull notes to the grid as you record."),
    ],
    "note": "Tempo is SELECT on the home screen, or TEMPO on the GLOBAL page. The line under the page title scrolls through the three sequencer hotkeys (HOLD SEQ, SEQ + REC, HOLD REC) and shows whether LAYERS is on.",
}

FAQS = [
    ("Why does nothing happen when I turn a knob on a settings page and then go home?",
     "The knobs do different jobs in different places: on the home screen they are always the instrument’s four modulations, on a page they set that page’s four columns. Hit HOME or the page’s button to go back to playing."),
    ("A note is stuck. How do I stop it?",
     "Hold HOME. Everything goes silent. If HOLD is on (SEL lights), turn it off on the KEYS page or play a new chord to replace what is held."),
    ("Is my loop saved when I power off?",
     "No. The step pattern, every instrument’s knobs, algorithm and settings are saved. A recorded loop lives only until you clear it (or power off)."),
    ("Why does the ALGORITHM knob change the picture so much?",
     "On purpose. Each algorithm is a different character for the instrument, so the picture changes with it: TIDE’s sky swaps a moon for a sun or a storm, BONK re-hangs its whole composition, TWANG’s strings become a harp, a banjo or a cat’s cradle. If you don’t like it... sorry? There’s plenty of other firmwares."),
]

# ------------------------------------------------------------------ 01 intro
INTRO = [
    "h1 turns the FM-1 into fourteen instruments that feel simple but are deceptively complex. Each instrument sets the stage with a unique themed graphic that shifts and moves with everything you do: play a note for reactions, turn a knob and it changes shape. Explore. There's a lot in here.",
    "PRESETS picks the instrument. ALGORITHM picks one of its eight algorithms. We keep it simple with the four knobs working the live modulations for the instrument.",
    "Deeper settings live on small, consistent, nicely designed pages that make it clear what you're changing. Learn one page and you know them all.",
]

# ------------------------------------------------------------------ 02 reference
REF_ON_FM1 = [
    (["[[PRESETS]]"], "Next or previous instrument."),
    (["[[ALGORITHM]]"], "The instrument's eight algorithms. Each keeps its own four knob settings, so the knobs stand where you last left them on that algorithm. Dots under the name show which of the eight you are on."),
    (["[[KNOB 1]]", "[[2]]", "[[3]]", "[[4]]"], "**Home:** the instrument's four live modulations. **On a page:** its four columns, left to right."),
    (["[[SELECT]]"], "**Home:** tempo. **On a page:** next or previous page. **Writing steps:** moves the step cursor."),
    (["[[FX]]", "[[SEL]]", "[[ENV]]", "[[LFO]]", "[[GLO]]", "[[ARP]]", "[[SEQ]]"], "Tap to open that settings page. The same button again, or HOME, goes back. GLO, SEQ, EDIT and HOME act when you let go, so holding one does only its hold (below) and never opens the page or pins the strip."),
    (["[[EDIT]]"], "Pins the knob names and values to the top of the home screen. **Writing steps:** leaves a rest."),
    (["[[REC]]", "[[PLAY]]"], "The sequencer. Loop: REC records a take, PLAY stops and starts it. Step: REC turns step-write on and off, PLAY runs the pattern."),
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
    (["[[SEQ]]", "+", "[[REC]]"], "Both together: LAYERS on and off. With it on, what you record keeps the instrument and algorithm it was played on (see layers)."),
    (["hold", "[[REC]]"], "Clears the loop, or the step pattern. With LAYERS on, it clears what was recorded on the instrument in hand, and holding on to three seconds clears everything."),
    (["hold", "[[HOME]]"], "Silences everything (all notes off)."),
    (["hold", "[[SAVE]]"], "Resets the algorithm in hand: its four knobs go back to default."),
    (["hold", "[[SAVE]]", "2 s"], "Resets this instrument: every algorithm's knobs, its FX, ENV, LFO and ARP pages, and its volume."),
    (["hold", "[[SAVE]]", "4 s"], "Resets every instrument, plus the KEYS and GLOBAL pages. ALL RESET flashes up. The sequencer and what it holds are left alone."),
    (["[[OCT −]]", "+", "[[OCT +]]"], "Both together: back to the middle octave."),
    (["MIDI CC 20–23"], "The four knobs, from a controller. CC 123 is all notes off."),
]

# ------------------------------------------------------------------ 05 step settings
STEP = {
    "intro": "Tap [[SEQ]] with MODE on STEP. Same page, the last column changes:",
    "knobs": [
        ("MODE", "LOOP · STEP", "Set it to STEP."),
        ("BARS", "1 · 2 · 4 · 8", "Pattern length. A pattern holds up to 64 steps, so long bars of small steps get fewer bars, and the page shows how many you really have."),
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
    (["3 ·", "[[REC]]"], "Closes the loop and it plays back. Or let it run to BARS and it closes itself."),
    (["4 ·", "[[REC]]"], "While it plays: overdub. Play over the top and it adds to the loop. REC again goes back to just playing."),
    (["[[PLAY]]"], "Stops and starts the loop."),
    (["hold", "[[REC]]"], "Clears it."),
]
REC_LOOP_NOTE = "You can switch instruments, algorithms and knobs while a loop plays; it plays notes, so it plays whatever instrument is up (unless LAYERS is on, below). SNAP on the SEQ page will quantize as you record. Hold GLO to set the metronome (see the GLOBAL page above)."
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
WRITE_NOTE = "Step-write works from the home screen. The step pattern saves with your settings, so it'll still be there after you turn the FM-1 off and on (loops are never saved)."
LAYERS = [
    "Press [[SEQ]] and [[REC]] together to turn LAYERS on (and again for off). With this on, every note recorded on an instrument or algorithm (loop or step) will stay on that instrument or algorithm, even if you switch or record on another (otherwise, when you switch instruments while recording/playing, the sound will change). This will let you stack different instrument and algorithm sounds together to create a complete, multi-layer track. Record a bass line on TWANG, turn PRESETS to KOI, then play or record a lead over it.",
    "Hold [[REC]] to clear only what was recorded on the instrument in hand (the toast says which). Keep holding to three seconds and everything clears. With LAYERS off, everything recorded plays on whatever instrument or algorithm is on screen.",
    "A few limits. Each algorithm keeps its own four knobs, but an instrument's ENV and LFO are universal and apply to all of an instrument's individual layers in a layered recording. Each instrument's volume is its own too, so hold EDIT and turn MASTER or SELECT to sit one layer under another. The eight voices are shared by all the layers, and each individual step still only holds eight notes across all instruments. With ARP on, the loop records the notes the arpeggiator played.",
]
