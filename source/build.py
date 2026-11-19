#!/usr/bin/env python3
"""Build the h1 iPad guide.

    python3 build.py            -> h1-guide-ipad-dark.pdf
    python3 build.py --check    -> also prints per-page space left above the footer

Pipeline: content.py (verbatim text) -> guide.html + style.css -> headless Chrome -> PDF
-> post-process with PyMuPDF (bookmarks, explicit page links, metadata, compaction).
Page numbers are assigned automatically from page order, so contents, footers and
bookmarks always agree."""
import html, re, subprocess, sys, pathlib
import content as C

ROOT = pathlib.Path(__file__).parent
OUT_PDF = ROOT / f"h1-pocket-guide-v{C.EDITION}-h1-{C.FIRMWARE}.pdf"

# ======================================================================= helpers
def md(s):
    """Escape, then apply the tiny markup used in content.py: [[KEY]] keycap, **x** emphasis."""
    s = html.escape(s, quote=False)
    s = re.sub(r"\[\[(.+?)\]\]", r"<kbd>\1</kbd>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s

def keys(parts):
    out = []
    for p in parts:
        if p.startswith("[["):
            out.append(f"<kbd>{html.escape(p[2:-2])}</kbd>")
        elif p == "+":
            out.append('<span class="plus">+</span>')
        else:
            out.append(f'<span class="lbl">{html.escape(p)}</span>')
    return "".join(out)

def rows(items, cls=""):
    return f'<div class="rows {cls}">' + "".join(
        f'<div class="row"><div class="k">{keys(k)}</div><div class="v">{md(v)}</div></div>'
        for k, v in items) + "</div>"

def knobrows(items):
    out = []
    for k, (n, v, t) in enumerate(items):
        vals = f'<span class="vals">{md(v)}</span>' if v else ""
        out.append(f'<div class="knobrow"><div class="badge">KNOB<span class="d">{k+1}</span></div>'
                   f'<div class="body"><div class="top"><span class="name">{md(n)}</span>{vals}</div>'
                   f'<div class="desc">{md(t)}</div></div></div>')
    return '<div class="knobrows">' + "".join(out) + "</div>"

def paras(lst, cls=""):
    return "".join(f'<p class="{cls}">{md(t)}</p>' for t in lst)

def mix(a, b, t):
    """Solid blend of hex colour a over b at t (keeps the PDF free of transparency)."""
    pa = [int(a[k:k+2], 16) for k in (1, 3, 5)]; pb = [int(b[k:k+2], 16) for k in (1, 3, 5)]
    return "#" + "".join(f"{round(x*t + y*(1-t)):02x}" for x, y in zip(pa, pb))

def h1(title, n, anchor, style=""):
    st = f' style="{style}"' if style else ""
    return f'<h1 class="section" id="{anchor}"{st}>{html.escape(title)} <span class="n">{n}</span></h1>'

def sub(title, anchor=None):
    a = f' id="{anchor}"' if anchor else ""
    return f'<div class="sub"{a}>{html.escape(title)}</div>'

# ======================================================================= page model
class Page:
    def __init__(self, label, target, body, anchors=(), cls="", style="", foot=True, back=("contents", "contents")):
        self.label, self.target, self.body = label, target, body
        self.anchors, self.cls, self.style, self.foot, self.back = list(anchors), cls, style, foot, back
        self.num = None

    def html(self):
        f = ""
        if self.foot:
            f = (f'<div class="foot"><a class="back" href="#{self.back[0]}">{self.back[1]}</a>'
                 f'<a class="lbl" href="#{self.target}">{self.label}</a>'
                 f'<a class="num" href="#contents">{self.num:02d}</a></div>')
        st = f' style="{self.style}"' if self.style else ""
        body = self.body() if callable(self.body) else self.body
        return f'<section class="page {self.cls}"{st}>{body}{f}</section>'

PAGES = []
ANCHOR_PAGE = {}
def page_of(anchor): return ANCHOR_PAGE[anchor]

SECTIONS = [  # (number, title exactly as in the source, anchor)
    ("01", "intro", "intro"), ("02", "reference", "reference"),
    ("03", "switching between loop and step", "switching"), ("04", "loop settings", "loop"),
    ("05", "step settings", "step"), ("06", "guide for each home instrument", "instruments"),
    ("07", "guide for global settings", "global"), ("08", "guide for recording", "recording"),
    ("09", "faqs", "faqs"),
]

# ======================================================================= pages
def p_cover():
    c = C.COVER
    grid = "".join(
        f'<a href="#{n.lower()}"><img src="img/{n.lower()}.png" alt="{n}">'
        f'<span style="color:{C.INSTRUMENT_COLORS[n]}">{n}</span></a>'
        for n in C.INSTRUMENT_NAMES)
    body = f'''
  <span id="cover"></span>
  <div class="brand"><a href="{C.SITE}">{html.escape(c["brand"])}</a></div>
  <div class="logo">h1</div>
  <p class="tag"><b>Custom firmware for the M-VAVE FM-1.</b> Fourteen instruments with themed dynamic visuals.</p>
  <div class="grid">{grid}</div>
  <div class="stamp">h1 pocket guide v{C.EDITION} · documents h1 firmware {C.FIRMWARE}<br>
    For newer builds, see <a href="{C.GUIDE_URL}">jakehandy.com/h1</a></div>
  <div class="edition">
    <div>Guide matches h1's current build,<br><a href="{C.LINK_RELEASE}">v0.2.1 (5b697e5)</a>, 18 November 2026.</div>
    <div style="text-align:right">Not affiliated with M-VAVE.<br>FM-1 is their product. · <a href="{C.SITE}">jakehandy.com</a></div>
  </div>'''
    return Page("", "cover", body, ["cover"], cls="cover", foot=False)

def p_contents():
    def body():
        rws = "".join(
            f'<a class="toc-row" href="#{a}"><span class="tn">{n}</span>'
            f'<span class="tt">{html.escape(t)}</span><span class="tp">{page_of(a):02d}</span></a>'
            for n, t, a in SECTIONS)
        insts = "".join(
            f'<a class="toc-inst" href="#{d["id"]}" style="--accent:{d["color"]}">'
            f'<img src="img/{d["id"]}.png" alt=""><span class="nm">{d["name"]}</span>'
            f'<span class="ct">{html.escape(d["cat"])}</span><span class="tp">{page_of(d["id"]):02d}</span></a>'
            for d in C.INSTRUMENTS)
        return (f'<h1 class="section" id="contents">contents</h1><div class="toc">{rws}</div>'
                f'{sub("the fourteen instruments")}<div class="toc-insts">{insts}</div>')
    return Page("contents", "contents", body, ["contents"], back=("cover", "cover"))

def p_intro_ref():
    body = (h1("intro", "01", "intro") +
            f'<p class="lead">{md(C.INTRO[0])}</p>' + paras(C.INTRO[1:]) +
            h1("reference", "02", "reference", "margin-top:22px") + sub("on the FM-1") +
            rows(C.REF_ON_FM1[:5]))
    return Page("01 · 02 · intro, reference", "intro", body, ["intro", "reference"])

def p_ref2():
    body = (sub("on the FM-1 (continued)") + rows(C.REF_ON_FM1[5:]) +
            f'<p class="note">{md(C.REF_MASTER_NOTE)}</p>' +
            '<div style="height:10px"></div>' + sub("holds and combos", "holds") + rows(C.REF_HOLDS[:1]))
    return Page("02 · reference", "reference", body, ["holds"])

def p_ref3(a, b, cont=False):
    title = "holds and combos (continued)" if cont else "holds and combos"
    anchor = None if cont else "holds"
    body = sub(title, anchor) + rows(C.REF_HOLDS[a:b])
    return Page("02 · reference", "reference", body, [] if cont else ["holds"])

def p_switch_loop():
    s, l = C.SWITCHING, C.LOOP
    body = (h1("switching between loop and step", "03", "switching") +
            f'<p class="lead">{md(s["intro"])}</p>' + rows(s["rows"], "mt") +
            f'<p class="note">{md(s["note"])}</p>' +
            h1("loop settings", "04", "loop", "margin-top:28px") +
            f'<p>{md(l["intro"])}</p>' + knobrows(l["knobs"]) +
            f'<p class="note">{md(l["note"])}</p>')
    return Page("03 · 04 · sequencer", "switching", body, ["switching", "loop"])

def p_step():
    s = C.STEP
    body = (h1("step settings", "05", "step") + f'<p>{md(s["intro"])}</p>' + knobrows(s["knobs"]) +
            f'''<div class="stepfig">
  <figure><img src="img/step-pattern.png" alt="{s["fig_caption"]}" class="sq"><figcaption>{s["fig_caption"]}</figcaption></figure>
  <div>
    <figure><img src="img/notches.png" alt="{s["notch_caption"]}" class="strip"><figcaption>{s["notch_caption"]}</figcaption></figure>
    <p>{md(s["notches"])}</p><p>{md(s["chords"])}</p>
  </div>
</div>''')
    return Page("05 · step settings", "step", body, ["step"])

def p_instrument(i, d):
    knobs = "".join(
        f'<div class="knob"><div class="kn">KNOB {k+1}</div><div class="nm">{md(n)}</div><div class="ds">{md(t)}</div></div>'
        for k, (n, t) in enumerate(d["knobs"]))
    algos = "".join(
        f'<div class="algo"><div class="i">{k+1}</div><div><div class="nm">{md(n)}</div><div class="ds">{md(t)}</div></div></div>'
        for k, (n, t) in enumerate(d["algos"]))
    note = f'<p class="algonote">{md(d["algonote"])}</p>' if d.get("algonote") else ""
    first = '<span id="instruments"></span>' if i == 0 else ""
    body = f'''{first}<span id="{d["id"]}"></span>
  <div class="head">
    <div class="art"><img src="img/{d["id"]}.png" alt="{d["name"]} artwork"></div>
    <div class="meta">
      <div class="kicker"><a href="#contents">06 · instruments</a><span>{i+1:02d} / 14</span></div>
      <h2 class="name">{d["name"]}</h2>
      <div class="cat">{md(d["cat"])}</div>
      <p class="intro">{md(d["intro"])}</p>
    </div>
  </div>
  <div class="sub">knobs</div>
  <div class="knobs">{knobs}</div>
  <div class="sub">algorithms</div>
  {note}
  <div class="algos">{algos}</div>'''
    style = (f'--accent:{d["color"]};--accent-line:{mix(d["color"], "#1D2026", .7)};'
             f'--accent-edge:{mix(d["color"], "#17191E", .4)}')
    anchors = (["instruments"] if i == 0 else []) + [d["id"]]
    return Page("06 · instruments", "instruments", body, anchors, cls="inst", style=style)

def gsec(idx):
    title, anchor, items = C.GLOBAL_PAGES[idx]
    return sub(title, anchor) + knobrows(items)

def p_global1():
    figs = "".join(f'<figure><img src="img/{f}.png" alt="{cap}"><figcaption>{cap}</figcaption></figure>'
                   for f, cap in C.GLOBAL_FIGS)
    body = (h1("guide for global settings", "07", "global") + f'<p>{md(C.GLOBAL_INTRO)}</p>' +
            f'<div class="figpair">{figs}</div>' + gsec(0))
    return Page("07 · global settings", "global", body, ["global", "glo"])

def p_global5():
    body = (sub("SEQ (shared)", "seq") +
            '<p>See <a class="xref" href="#loop">loop settings</a> and <a class="xref" href="#step">step settings</a>.</p>' +
            f'<p class="note">{md(C.PER_INSTRUMENT)}</p>')
    return body

def p_rec1():
    body = (h1("guide for recording", "08", "recording") + sub("recording a loop", "rec-loop") +
            rows(C.REC_LOOP) + f'<p class="note">{md(C.REC_LOOP_NOTE)}</p>' +
            sub("the keyboard shows the pattern", "keyboard") + paras(C.KEYBOARD_MAP[:1]))
    return Page("08 · recording", "recording", body, ["recording", "keyboard"])

def p_rec2():
    body = (paras(C.KEYBOARD_MAP[1:]) + sub("writing steps", "writing") + rows(C.WRITE_STEPS) +
            f'<p class="note">{md(C.WRITE_NOTE)}</p>')
    return Page("08 · recording", "recording", body, ["writing"])

def p_rec3():
    body = sub("layers", "layers") + paras(C.LAYERS)
    return Page("08 · recording", "recording", body, ["layers"])

def p_faqs():
    qa = "".join(f'<div class="faq"><div class="q">{md(q)}</div><div class="a">{md(a)}</div></div>'
                 for q, a in C.FAQS)
    links = " · ".join(f'<a href="{u}">{html.escape(t)}</a>' for t, u in C.COVER["links"])
    body = (h1("faqs", "09", "faqs") + f'<div class="faqs">{qa}</div>' +
            f'''<div class="colophon">
  <p>Guide matches h1's current build, <a href="{C.LINK_RELEASE}">v0.2.1 (5b697e5)</a>, 18 November 2026. This page will change as h1 does.</p>
  <p>Not affiliated with M-VAVE. FM-1 is their product. · <a href="{C.SITE}">jakehandy.com</a></p>
  <p class="links">{links}</p>
  <p class="stamp2">This edition: h1 pocket guide v{C.EDITION} ({C.EDITION_DATE}), a dark, iPad-optimised layout of Jake Handy's original guide. It documents h1 firmware {C.FIRMWARE_BUILD}. For newer builds, see <a href="{C.GUIDE_URL}">jakehandy.com/h1</a>. Layout and source: <a href="{C.REPO}">github.com/slowphase/h1-pocket-guide</a>.</p>
</div>''')
    return Page("09 · faqs", "faqs", body, ["faqs"])

# ======================================================================= assemble
def assemble():
    global PAGES
    G = "07 · global settings"
    PAGES = [p_cover(), p_contents(), p_intro_ref(), p_ref2(), p_ref3(1, 11, cont=True),
             p_switch_loop(), p_step()]
    PAGES += [p_instrument(i, d) for i, d in enumerate(C.INSTRUMENTS)]
    PAGES += [p_global1(),
              Page(G, "global", lambda: sub("the metronome", "metronome") + f'<p>{md(C.METRONOME_INTRO)}</p>'
                   + rows(C.METRONOME) + f'<p class="note">{md(C.METRONOME_NOTE)}</p>', ["metronome"]),
              Page(G, "global", lambda: gsec(1) + gsec(2), ["keys", "fx"]),
              Page(G, "global", lambda: gsec(3) + gsec(4), ["env", "lfo"]),
              Page(G, "global", lambda: gsec(5) + p_global5(), ["arp", "seq"]),
              p_rec1(), p_rec2(), p_rec3(), p_faqs()]
    for n, p in enumerate(PAGES, 1):
        p.num = n
        for a in p.anchors:
            ANCHOR_PAGE.setdefault(a, n)

def toc():
    t = [[1, "Cover", 1], [1, "Contents", page_of("contents")]]
    for n, title, a in SECTIONS:
        t.append([1, f"{n}  " + ("FAQs" if a == "faqs" else title[0].upper() + title[1:]), page_of(a)])
        if a == "instruments":
            t += [[2, d["name"], page_of(d["id"])] for d in C.INSTRUMENTS]
        if a == "reference":
            t.append([2, "Holds and combos", page_of("holds")])
        if a == "global":
            for k, (title2, anc, _) in enumerate(C.GLOBAL_PAGES):
                t.append([2, title2, page_of(anc)])
                if k == 0:
                    t.append([2, "The metronome", page_of("metronome")])
            t.append([2, "SEQ (shared)", page_of("seq")])
        if a == "recording":
            t += [[2, "Recording a loop", page_of("recording")], [2, "The keyboard shows the pattern", page_of("keyboard")],
                  [2, "Writing steps", page_of("writing")], [2, "Layers", page_of("layers")]]
    return t

def document():
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<title>h1 guide: M-VAVE FM-1 custom firmware with 14 instruments</title>'
            '<link rel="stylesheet" href="style.css"></head><body>'
            + "".join(p.html() for p in PAGES) + "</body></html>")

def render_pdf(html_path, pdf_path):
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu",
                    "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}", html_path.resolve().as_uri()],
                   check=True, capture_output=True)

def finish(raw, out, toc_entries):
    """Explicit page links, bookmarks, metadata, lossless compaction."""
    import pymupdf
    doc = pymupdf.open(raw)
    for page in doc:   # Chrome writes named destinations; convert to plain page jumps
        for l in page.get_links():
            if l["kind"] == pymupdf.LINK_NAMED and l.get("page", -1) >= 0:
                y = max(0, doc[l["page"]].rect.height - l["to"].y)
                page.delete_link(l)
                page.insert_link({"kind": pymupdf.LINK_GOTO, "from": l["from"], "page": l["page"],
                                  "to": pymupdf.Point(0, y), "zoom": 0})
    doc.set_toc(toc_entries)
    doc.set_metadata({
        "title": f"h1 pocket guide v{C.EDITION} (h1 firmware {C.FIRMWARE})",
        "author": "Jake Handy", "subject": f"h1 pocket guide v{C.EDITION}, documents h1 firmware {C.FIRMWARE_BUILD}",
        "keywords": "h1, M-VAVE FM-1, firmware, guide", "creator": "build.py (HTML/CSS + Chrome)",
    })
    doc.set_pagemode("UseOutlines")
    doc.save(out, garbage=4, deflate=True)

def check(html_path):
    """Space (px) between the lowest content and the footer rule on every page. Negative = overflow."""
    from playwright.sync_api import sync_playwright
    js = """() => [...document.querySelectorAll('.page')].map((pg, i) => {
        const foot = pg.querySelector('.foot');
        const limit = foot ? foot.getBoundingClientRect().top : pg.getBoundingClientRect().bottom - 24;
        let low = 0;
        pg.querySelectorAll('*').forEach(el => { if (foot && foot.contains(el)) return;
            const r = el.getBoundingClientRect(); if (r.height > 0) low = Math.max(low, r.bottom); });
        return [i + 1, Math.round(limit - low)]; })"""
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = b.new_page(); pg.emulate_media(media="print")
        pg.goto(html_path.resolve().as_uri()); pg.wait_for_load_state("networkidle")
        res = pg.evaluate(js); b.close()
    return res

if __name__ == "__main__":
    assemble()
    out_html = ROOT / "guide.html"
    out_html.write_text(document(), encoding="utf-8")
    if "--check" in sys.argv:
        for n, gap in check(out_html):
            print(f"p{n:02d} gap {gap:4d}px {'OVERFLOW' if gap < 12 else ''}")
    raw = ROOT / "_raw.pdf"
    render_pdf(out_html, raw)
    finish(raw, OUT_PDF, toc())
    raw.unlink()
    print("wrote", OUT_PDF, len(PAGES), "pages")
