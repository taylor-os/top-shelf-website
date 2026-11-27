"""Render the 2026-11-27 site update from the shared content (all copy lives in content.json).

Writes, idempotently:
  index.html                 the #industries section (12 pair cards) and its CSS
  assets/see-your-business.js  the PAIRS data block of the pop-up
  solution-crm.html          everything but the nav, the BY-TRADE block, owner quotes and footer
  solution-websites-seo.html the same, with the 13-site gallery

Copy: renders-src/site-content/content.json. Pairs: renders-src/industry-crm/pairs.json.
Screens: renders-src/industry-crm/captions.json. Short glue labels (link text, alt text)
are the only words written here.

Run from anywhere:  python scripts/build_site_update.py
Then refresh the FAQ schema:  python scripts/inject_faq_schema.py solution-crm.html solution-websites-seo.html
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = json.load(open(os.path.join(ROOT, "renders-src", "site-content", "content.json"), encoding="utf-8"))
PAIRS = json.load(open(os.path.join(ROOT, "renders-src", "industry-crm", "pairs.json"), encoding="utf-8"))
CAPS = json.load(open(os.path.join(ROOT, "renders-src", "industry-crm", "captions.json"), encoding="utf-8"))

EXTRA_SITE = {"business": "Linewright Mobile Dent Co.", "label": "Mobile Dent Repair",
              "website_dir": "websites/linewright-mobile-dent"}
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="4,12.5 9.5,18 20,6"/></svg>'
ARR = ' <span class="arr" aria-hidden="true">&rarr;</span>'


def t(s):
    return html.escape(s, quote=False)


def at(s):
    return html.escape(s, quote=True)


def em(text, tail):
    """Wrap the closing words of a heading in <em> (the site's gold italic)."""
    assert text.endswith(tail), (text, tail)
    return t(text[: -len(tail)]) + "<em>" + t(tail) + "</em>"


def site_shot(p):
    return "assets/img/websites/%s-home-d.webp" % os.path.basename(p["website_dir"])


def crm_screen(p):
    """First (owner-home) screen in captions.json. The vet set has no captions entry yet."""
    cap = CAPS.get(p["slug"])
    if cap:
        s = cap["screens"][0]
        return "assets/img/crm/industries/%s/%s" % (p["slug"], s["file"]), s["role"]
    return "assets/img/crm/industries/%s/1-today-d.webp" % p["slug"], "Today"


def industry_href(p):
    return p["industry_page"] + ("#" + p["industry_anchor"] if p["industry_anchor"] else "")


def screen(slug, file):
    """A captions.json screen: (path, caption, business, is_mobile)."""
    for s in CAPS[slug]["screens"]:
        if s["file"] == file:
            biz = next(p["business"] for p in PAIRS if p["slug"] == slug)
            return "assets/img/crm/industries/%s/%s" % (slug, file), s["caption"], biz, file.endswith("-m.webp")
    raise KeyError((slug, file))


def replace_between(src, start, end, new):
    i, j = src.index(start), src.index(end)
    return src[:i] + new + src[j:]


CRLF = {}


def read(path):
    """Text with LF line ends; write() puts back the file's own line ends (the pages use CRLF)."""
    with open(os.path.join(ROOT, path), encoding="utf-8", newline="") as fh:
        raw = fh.read()
    CRLF[path] = "\r\n" in raw
    return raw.replace("\r\n", "\n")


def write(path, src):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8", newline="\r\n" if CRLF.get(path) else "\n") as fh:
        fh.write(src)


# ---------------------------------------------------------------- homepage cards
CARDS_CSS = """/* PAIR-CARDS:start (scripts/build_site_update.py) */
#cc .c-pairs{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(16px,2vw,24px)}
#cc .c-pair{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:var(--r);background:var(--card);box-shadow:var(--shadow);overflow:hidden;transition:border-color 200ms ease}
#cc .c-pair-shots{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:12px 12px 0}
#cc .c-pair-shots figure{margin:0;min-width:0}
#cc .c-pair-shots img{display:block;width:100%;height:auto;aspect-ratio:16/10;object-fit:cover;object-position:top;border-radius:8px;border:1px solid var(--line-2);background:var(--bg-2);color:var(--muted);font-size:.75rem}
#cc .c-pair-shots figcaption{margin-top:7px;font-size:.6875rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
#cc .c-pair-body{display:flex;flex-direction:column;gap:2px;flex:1;padding:14px 18px 18px}
#cc .c-pair-ind{font-size:.8125rem;letter-spacing:.1em;text-transform:uppercase;color:var(--blue)}
#cc .c-pair h3{font-family:var(--serif);font-weight:600;font-size:1.5rem;line-height:1.2;letter-spacing:-.01em}
#cc .c-pair-note{font-size:.875rem;color:var(--muted)}
#cc .c-pair-links{display:flex;flex-wrap:wrap;gap:6px 22px;margin-top:auto;padding-top:14px}
#cc .c-pair-links a{display:inline-flex;align-items:center;gap:6px;min-height:32px;color:var(--ink);font-size:.9375rem;font-weight:500;text-decoration:none;border-bottom:1px solid transparent;transition:color 200ms ease,border-color 200ms ease}
#cc .c-pair-links a span{color:var(--blue)}
@media (hover:hover){
#cc .c-pair:hover{border-color:rgba(201,168,106,.4)}
#cc .c-pair-links a:hover{color:var(--blue);border-bottom-color:var(--blue)}
}
#cc .c-pair-links a:focus-visible{outline:2px solid var(--blue);outline-offset:3px;border-radius:4px}
@media (max-width:760px){#cc .c-pairs{grid-template-columns:1fr}}
/* PAIR-CARDS:end */
"""


def cards_section():
    h = CONTENT["home"]["sections"]["pairs"]
    custom = CONTENT["custom"]["h"]
    lis = []
    for p in PAIRS:
        crm, role = crm_screen(p)
        biz = t(p["business"])
        lis.append(
            '        <li class="c-pair c-rv">\n'
            '          <div class="c-pair-shots">\n'
            '            <figure><img src="%s" width="1200" height="750" loading="lazy" decoding="async" alt="Home page of the %s sample website"><figcaption>%s</figcaption></figure>\n'
            '            <figure><img src="%s" width="1440" height="900" loading="lazy" decoding="async" alt="%s sample CRM, %s screen"><figcaption>%s</figcaption></figure>\n'
            '          </div>\n'
            '          <div class="c-pair-body">\n'
            '            <p class="c-pair-ind">%s</p>\n'
            '            <h3>%s</h3>\n'
            '            <p class="c-pair-note">Sample website &middot; Sample CRM</p>\n'
            '            <p class="c-pair-links"><a href="%s">%s <span aria-hidden="true">&rarr;</span></a><a href="%s/index.html" target="_blank" rel="noopener">Visit the sample website <span aria-hidden="true">&nearr;</span></a></p>\n'
            '          </div>\n'
            '        </li>' % (site_shot(p), at(p["business"]), t(h["card_website_label"]),
                              crm, at(p["business"]), at(role), t(h["card_crm_label"]),
                              t(p["industry_label"]), biz, at(industry_href(p)), t(h["card_link_label"]),
                              p["website_dir"]))
    return (
        '<section class="c-sec" id="industries" aria-labelledby="ind-h">\n'
        '    <div class="c-wrap">\n'
        '      <div class="c-sec-head c-rv">\n'
        '        <h2 id="ind-h">%s</h2>\n'
        '        <p class="c-lede">%s</p>\n'
        '      </div>\n'
        '      <ul class="c-pairs">\n%s\n      </ul>\n'
        '      <p class="c-ind-sub c-rv">%s <a class="c-link" href="industry-custom.html">Tell us what you do <span aria-hidden="true">&rarr;</span></a></p>\n'
        '    </div>\n'
        '  </section>' % (h["h"].replace("that go together", '<span class="c-hl">that go together</span>'),
                         t(h["body"]), "\n".join(lis), t(custom)))


def build_index():
    src = read("index.html")
    src = re.sub(r'<section class="c-sec" id="industries".*?</section>', lambda m: cards_section(), src, count=1, flags=re.S)
    src = re.sub(r"/\* PAIR-CARDS:start.*?/\* PAIR-CARDS:end \*/\n", "", src, flags=re.S)
    i = src.index("</style>", src.index('<style id="cc-css">'))
    src = src[:i] + CARDS_CSS + src[i:]
    write("index.html", src)


# ---------------------------------------------------------------- pop-up data
def build_popup():
    path = os.path.join("assets", "see-your-business.js")
    rows = []
    for p in PAIRS:
        crm, role = crm_screen(p)
        rows.append(" " + json.dumps({
            "slug": p["slug"], "label": p["industry_label"], "business": p["business"],
            "site": p["website_dir"] + "/index.html", "web": site_shot(p), "crm": crm,
            "crm_role": role, "page": industry_href(p)}, ensure_ascii=False, separators=(",", ":")))
    block = "/*PAIRS:start*/\nvar PAIRS = [\n" + ",\n".join(rows) + "\n];\n"
    write(path, replace_between(read(path), "/*PAIRS:start*/", "/*PAIRS:end*/", block))


# ---------------------------------------------------------------- shared page pieces
PAGE_CSS = """<style id="focus-css">
.fx-sec{padding-block:clamp(4rem,8vw,7rem)}
.fx-jump{display:flex;flex-wrap:wrap;gap:.55rem;justify-content:center;margin-top:2.4rem}
.fx-jump a{font-size:.86rem;color:var(--ink-2);border:1px solid var(--hairline);border-radius:999px;padding:.55rem 1rem;text-decoration:none;transition:border-color .2s,color .2s}
.fx-jump a:hover{border-color:var(--gold);color:var(--gold-bright)}
.fx-sample{max-width:64ch;margin:0 auto clamp(1rem,3vw,2rem);text-align:center;font-size:.9rem;color:var(--ink-3);line-height:1.7}
.fx-sample b{color:var(--gold);font-weight:500;letter-spacing:.12em;text-transform:uppercase;font-size:.75rem;margin-right:.4rem}
.fx-group{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(2rem,5vw,4.5rem);align-items:center;padding-block:clamp(3rem,6vw,5rem);border-top:1px solid var(--hairline-soft);scroll-margin-top:110px}
.fx-group.fx-flip .fx-shot{order:-1}
.fx-group.fx-solo{grid-template-columns:1fr}
.fx-num{font-family:var(--serif);font-style:italic;color:var(--gold-deep);font-size:1.2rem}
.fx-group h2{font-family:var(--serif);font-weight:400;font-size:clamp(1.8rem,3.2vw,2.6rem);line-height:1.1;color:var(--ink);margin:.35rem 0 1rem;letter-spacing:-.01em}
.fx-intro{color:var(--ink-2);line-height:1.75;max-width:58ch}
.fx-list{list-style:none;margin:1.8rem 0 0;padding:0;display:grid;gap:1.3rem}
.fx-list li{display:grid;grid-template-columns:22px minmax(0,1fr);gap:.9rem}
.fx-list svg{width:20px;height:20px;color:var(--gold);margin-top:.25rem}
.fx-list h3{font-family:var(--sans);font-weight:500;font-size:1.05rem;color:var(--ink);margin:0 0 .3rem;line-height:1.4}
.fx-list p{font-size:.93rem;color:var(--ink-2);line-height:1.7;margin:0}
.fx-shot{margin:0;min-width:0}
.fx-shot img{display:block;width:100%;height:auto;border-radius:14px;border:1px solid var(--hairline-strong);box-shadow:0 30px 70px -40px rgba(0,0,0,.9);background:var(--surface)}
.fx-shot.is-m img{max-width:300px;margin-inline:auto;border-radius:30px}
.fx-shot figcaption{margin:1rem auto 0;max-width:46ch;font-size:.86rem;color:var(--ink-3);line-height:1.6;text-align:center}
.fx-shot figcaption b{display:block;font-weight:500;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:.35rem}
.fx-thumbs{display:grid;grid-template-columns:1fr 1fr;gap:.9rem}
.fx-thumbs img{border-radius:10px}
.fx-checks{list-style:none;margin:1.6rem 0 0;padding:0;display:grid;gap:.95rem}
.fx-checks li{display:grid;grid-template-columns:22px minmax(0,1fr);gap:.8rem;color:var(--ink-2);line-height:1.6}
.fx-checks svg{width:19px;height:19px;color:var(--gold);margin-top:.2rem}
.fx-moments{list-style:none;margin:1.6rem 0 0;padding:0;counter-reset:m;display:grid;gap:1rem}
.fx-moments li{counter-increment:m;display:grid;grid-template-columns:2.2rem minmax(0,1fr);gap:.8rem;color:var(--ink-2);line-height:1.6;padding-bottom:1rem;border-bottom:1px solid var(--hairline-soft)}
.fx-moments li::before{content:counter(m,decimal-leading-zero);font-family:var(--serif);font-style:italic;color:var(--gold-deep);font-size:1.15rem;line-height:1.3}
.fx-h{font-family:var(--serif);font-weight:400;font-size:clamp(1.7rem,3vw,2.3rem);color:var(--ink);line-height:1.15;margin-top:1.2rem}
.fx-price{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:24px;align-items:start}
.fx-side{display:grid;gap:24px}
.fx-side .pricing-card{padding:30px 30px}
.fx-tiers{list-style:none;margin:1.4rem 0 0;padding:0;border-top:1px solid var(--hairline)}
.fx-tiers li{display:flex;justify-content:space-between;align-items:baseline;gap:1rem;padding:.8rem 0;border-bottom:1px solid var(--hairline-soft);color:var(--ink-2);font-size:.95rem}
.fx-tiers b{font-family:var(--serif);font-weight:400;font-size:1.35rem;color:var(--ink)}
.fx-summary{color:var(--ink-2);font-size:.95rem;line-height:1.7;margin-top:.4rem}
.fx-trap{border:1px solid var(--gold);border-radius:var(--r-lg);padding:30px;background:linear-gradient(180deg,rgba(201,168,106,.08),transparent)}
.fx-trap h3{font-family:var(--serif);font-weight:400;font-size:1.6rem;color:var(--ink);margin:0}
.fx-trap .fx-checks{margin-top:1.2rem}
.fx-fine{margin-top:1.1rem;font-size:.85rem;color:var(--ink-3);line-height:1.6}
.fx-gallery{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}
.fx-site{display:flex;flex-direction:column;border:1px solid var(--hairline);border-radius:16px;background:var(--surface);overflow:hidden;transition:border-color .3s}
.fx-site:hover{border-color:var(--hairline-strong)}
.fx-site img{display:block;width:100%;height:auto;aspect-ratio:16/10;object-fit:cover;object-position:top;border-bottom:1px solid var(--hairline);background:var(--surface-2);color:var(--ink-3);font-size:.8rem}
.fx-site-body{display:flex;flex-direction:column;gap:.2rem;padding:1.1rem 1.25rem 1.3rem;flex:1}
.fx-site-tag{align-self:flex-start;font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);border:1px solid var(--hairline-strong);border-radius:999px;padding:.25rem .6rem;margin-bottom:.5rem}
.fx-site-ind{font-size:.8rem;color:var(--ink-3)}
.fx-site h3{font-family:var(--serif);font-weight:400;font-size:1.35rem;color:var(--ink);margin:0;line-height:1.25}
.fx-site-links{display:flex;flex-wrap:wrap;gap:.3rem 1.2rem;margin-top:auto;padding-top:.9rem}
.fx-site-links a{font-size:.9rem;color:var(--gold-bright);text-decoration:none}
.fx-site-links a:hover{text-decoration:underline}
.fx-foot{margin-top:1.6rem;font-size:.9rem;color:var(--ink-3)}
@media (max-width:980px){.fx-gallery{grid-template-columns:repeat(2,minmax(0,1fr))}.fx-price{grid-template-columns:1fr}}
@media (max-width:900px){.fx-group{grid-template-columns:1fr}.fx-group.fx-flip .fx-shot{order:0}}
@media (max-width:620px){.fx-gallery{grid-template-columns:1fr}.fx-side .pricing-card,.fx-trap{padding:24px 20px}}
</style>
"""


def hero(src, eyebrow, h1, sub):
    photo = re.search(r'  <div class="page-hero-photo".*?</div>\n', src, re.S).group(0)
    icon = re.search(r'    <span class="page-hero-icon reveal">.*?</span>\n', src, re.S).group(0)
    b = CONTENT["brand"]
    return (
        '<!-- ============================ PAGE HERO ============================ -->\n'
        '<section class="page-hero">\n%s'
        '  <div class="container page-hero-inner">\n%s'
        '    <span class="eyebrow reveal">%s</span>\n'
        '    <h1 class="display display-lg reveal">%s</h1>\n'
        '    <p class="page-hero-sub reveal">%s</p>\n'
        '    <div class="page-hero-actions reveal">\n'
        '      <a href="%s" class="btn btn-gold">%s%s</a>\n'
        '      <a href="%s" class="btn btn-line">%s</a>\n'
        '    </div>\n' % (photo, icon, t(eyebrow), h1, t(sub), b["cta_primary_href"], t(b["cta_primary"]), ARR,
                         b["phone_href"], t(b["cta_secondary"])))


def steps(items):
    out = []
    for s in items:
        out.append('      <div class="step reveal"><span class="step-num">0%s</span><p class="step-title">%s</p><p class="step-body">%s</p></div>'
                   % (s["step"], t(s["title"]), t(s["body"])))
    return '    <div class="steps">\n%s\n    </div>\n' % "\n".join(out)


def faq(items, eyebrow, h2, body):
    rows = []
    for n, qa in enumerate(items, 1):
        rows.append('      <div class="qa-row reveal"><span class="qa-num">%02d</span><div><p class="qa-q">%s</p><p class="qa-a">%s</p></div></div>'
                    % (n, t(qa["q"]), t(qa["a"])))
    return (
        '<!-- ============================ FAQ ============================ -->\n'
        '<section class="section rule-top fx-sec" id="faq">\n'
        '  <div class="container">\n'
        '    <div class="section-head">\n'
        '      <span class="eyebrow reveal">%s</span>\n'
        '      <h2 class="display display-lg reveal" style="margin-top:1.6rem">%s</h2>\n'
        '      <p class="reveal">%s</p>\n'
        '    </div>\n'
        '    <div class="qa-list">\n%s\n    </div>\n'
        '  </div>\n'
        '</section>\n\n' % (eyebrow, h2, t(body), "\n".join(rows)))


def closing(eyebrow, title_html, body):
    b = CONTENT["brand"]
    return (
        '<!-- ============================ FINAL CTA ============================ -->\n'
        '<section class="cta rule-top">\n'
        '  <div class="container">\n'
        '    <img src="assets/logo-mark.png?v=20260804b" alt="" class="cta-mark reveal">\n'
        '    <span class="eyebrow reveal">%s</span>\n'
        '    <h2 class="cta-title reveal">%s</h2>\n'
        '    <p class="cta-sub reveal">%s</p>\n'
        '    <div class="cta-actions reveal">\n'
        '      <a href="%s" class="btn btn-gold">%s%s</a>\n'
        '      <a href="%s" class="btn btn-line">%s</a>\n'
        '    </div>\n'
        '    <p class="cta-fine reveal">%s</p>\n'
        '  </div>\n'
        '</section>\n\n' % (t(eyebrow), title_html, t(body), b["cta_primary_href"], t(b["cta_primary"]), ARR,
                            b["phone_href"], t(b["cta_secondary"]), t(b["cta_primary_note"])))


def figure(slug, file, extra_cls=""):
    path, cap, biz, mobile = screen(slug, file)
    w, h = (585, 1266) if mobile else (1440, 900)
    return ('<figure class="fx-shot%s%s"><img src="%s" width="%d" height="%d" loading="lazy" decoding="async" alt="%s"><figcaption><b>Sample screen &middot; %s</b>%s</figcaption></figure>'
            % (" is-m" if mobile else "", extra_cls, path, w, h, at(biz + ": " + cap), t(biz), t(cap)))


def set_meta(src, desc):
    src = re.sub(r'(<meta (?:name|property)="(?:description|og:description|twitter:description)" content=")[^"]*(")',
                 lambda m: m.group(1) + at(desc) + m.group(2), src)
    return re.sub(r'("@type": "Service".*?"description": )"[^"]*"', lambda m: m.group(1) + json.dumps(desc), src, count=1, flags=re.S)


def frame_page(path, top, bottom, desc):
    """Swap the hero-to-BY-TRADE region and the FAQ-to-footer region; keep nav, BY-TRADE, owner quotes, footer."""
    src = read(path)
    a0 = "<!-- FOCUS-TOP:start (scripts/build_site_update.py) -->\n"
    a1 = "<!-- FOCUS-TOP:end -->\n"
    b0 = "<!-- FOCUS-BOTTOM:start (scripts/build_site_update.py) -->\n"
    b1 = "<!-- FOCUS-BOTTOM:end -->\n"
    if a0 not in src:  # first run: mark the old regions
        i = src.index("<!-- ============================ PAGE HERO")
        j = src.index("<!-- BY-TRADE:start")
        src = src[:i] + a0 + src[i:j] + a1 + "\n" + src[j:]
        k = src.index("<!-- BY-TRADE:end -->\n") + len("<!-- BY-TRADE:end -->\n")
        m = src.index("<!-- ============================ FOOTER ============================ -->")
        src = src[:k] + "\n" + b0 + src[k:m] + b1 + src[m:]
    old_top = src[src.index(a0):src.index(a1)]
    src = replace_between(src, a0, a1, a0 + top(old_top))
    src = replace_between(src, b0, b1, b0 + bottom())
    src = re.sub(r'<style id="focus-css">.*?</style>\n', "", src, flags=re.S)
    src = src.replace("</head>", PAGE_CSS + "</head>", 1)
    write(path, set_meta(src, desc))


# ---------------------------------------------------------------- CRM page
# One screen per benefit group, each from a different pair where it fits. Picked so the
# caption only shows facts-file features (no tips, deposits or good/better/best).
GROUP_SCREENS = [
    ("home-services", "6-ai-call-texts-m.webp"),
    ("car-lots", "5-pay-page-m.webp"),
    ("home-services", "4-estimates-awaiting-m.webp"),
    ("real-estate", "1-today-d.webp"),
    ("home-services", "2-dispatch-board-d.webp"),
    ("restaurants", "5-reserve-m.webp"),
    None,  # reviews: no review screen in the sets yet
    [("salon-spa", "2-day-by-chair-d.webp"), ("restaurants", "2-floor-plan-d.webp"),
     ("fitness", "2-classes-week-d.webp"), ("legal", "2-matters-d.webp")],
]


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def crm_top(old):
    c = CONTENT["crm"]
    groups = c["benefit_groups"]
    assert len(groups) == len(GROUP_SCREENS)
    jump = "".join('<a href="#%s">%s</a>' % (slugify(g["title"]), t(g["title"])) for g in groups)
    out = [hero(old, c["eyebrow"], em(c["h1"], "done from one app."), c["sub"]),
           '    <nav class="fx-jump reveal" aria-label="On this page">%s</nav>\n  </div>\n</section>\n\n' % jump]
    out.append('<!-- ============================ BENEFITS ============================ -->\n'
               '<section class="section rule-top fx-sec" style="padding-top:clamp(3rem,6vw,5rem)">\n  <div class="container">\n'
               '    <p class="fx-sample reveal"><b>Sample screens</b>%s</p>\n' % t(CONTENT["sample_note"]))
    flip = False
    for n, (g, shot) in enumerate(zip(groups, GROUP_SCREENS), 1):
        items = "\n".join('        <li>%s<div><h3>%s</h3><p>%s</p></div></li>' % (CHECK, t(b["title"]), t(b["body"]))
                          for b in g["benefits"])
        text = ('      <div>\n        <span class="fx-num">%02d</span>\n        <h2>%s</h2>\n        <p class="fx-intro">%s</p>\n'
                '        <ul class="fx-list">\n%s\n        </ul>\n' % (n, t(g["title"]), t(g["intro"]), items))
        if isinstance(shot, list):
            text += '        <p style="margin-top:1.6rem"><a class="tlink" href="crm-by-industry.html" style="color:var(--gold)">See the CRM for each industry%s</a></p>\n' % ARR
            thumbs = "".join(figure(s, f) for s, f in shot)
            pic = '      <div class="fx-thumbs">%s</div>\n' % thumbs
        elif shot:
            pic = "      %s\n" % figure(*shot)
        else:
            pic = ""
        cls = "fx-group reveal" + (" fx-flip" if flip and pic else "")
        if not pic:
            cls += " fx-solo"
        out.append('    <div class="%s" id="%s">\n%s      </div>\n%s    </div>\n' % (cls, slugify(g["title"]), text, pic))
        if pic:
            flip = not flip
    out.append('  </div>\n</section>\n\n')

    out.append('<!-- ============================ HOW IT WORKS ============================ -->\n'
               '<section class="section rule-top fx-sec" id="how-it-works">\n  <div class="container">\n'
               '    <div class="section-head">\n      <span class="eyebrow reveal">How it works</span>\n'
               '      <h2 class="display display-lg reveal" style="margin-top:1.6rem">From the form to <em>your first invoice</em></h2>\n'
               '    </div>\n%s  </div>\n</section>\n\n' % steps(c["how_it_works"]))

    d, pm = c["day_one"], c["phone_moments"]
    out.append('<!-- ============================ DAY ONE + FROM A PHONE ============================ -->\n'
               '<section class="section rule-top fx-sec">\n  <div class="container two-col">\n'
               '    <div class="reveal">\n      <span class="eyebrow">Day one</span>\n      <h2 class="fx-h">%s</h2>\n'
               '      <ul class="fx-checks">\n%s\n      </ul>\n    </div>\n'
               '    <div class="reveal">\n      <span class="eyebrow">In the field</span>\n      <h2 class="fx-h">%s</h2>\n'
               '      <ol class="fx-moments">\n%s\n      </ol>\n    </div>\n'
               '  </div>\n</section>\n\n' % (
                   t(d["h"]), "\n".join('        <li>%s<span>%s</span></li>' % (CHECK, t(i)) for i in d["items"]),
                   t(pm["h"]), "\n".join('        <li>%s</li>' % t(i) for i in pm["items"])))

    pr, hp, trap = CONTENT["pricing"], CONTENT["home"]["sections"]["pricing"], c["anti_trap"]
    plan, line, web = pr["plan"], pr["phone_line"], pr["website"]
    tiers = "\n".join('          <li><span>%s</span><b>%s%s</b></li>' % (
        t(x["users"]), t(x["price"]), (' <small style="font-family:var(--sans);font-size:.8rem;color:var(--ink-3)">%s</small>' % t(x["period"])) if x["period"] else "")
        for x in plan["tiers"])
    incl = "\n".join('          <div class="pricing-feature"><span class="icon">%s</span>%s</div>' % (CHECK, t(i)) for i in plan["includes"])
    out.append(
        '<!-- ============================ PRICING ============================ -->\n'
        '<section class="section rule-top fx-sec" id="pricing">\n  <div class="container">\n'
        '    <div class="section-head">\n      <span class="eyebrow reveal">Pricing</span>\n'
        '      <h2 class="display display-lg reveal" style="margin-top:1.6rem">%s</h2>\n      <p class="reveal">%s</p>\n    </div>\n'
        '    <div class="fx-price">\n'
        '      <div class="pricing-card featured reveal">\n'
        '        <p class="pricing-name">%s</p>\n        <p class="fx-summary">%s</p>\n'
        '        <ul class="fx-tiers">\n%s\n        </ul>\n'
        '        <div class="pricing-divider"></div>\n        <div class="pricing-features">\n%s\n        </div>\n'
        '        <a href="%s" class="btn btn-gold w-full">%s</a>\n'
        '        <p class="fx-fine" style="text-align:center">%s</p>\n'
        '      </div>\n'
        '      <div class="fx-side">\n'
        '        <div class="fx-trap reveal">\n          <h3>%s</h3>\n          <ul class="fx-checks">\n%s\n          </ul>\n'
        '          <p class="fx-fine">%s</p>\n        </div>\n'
        '        <div class="pricing-card reveal">\n          <p class="pricing-name">%s</p>\n'
        '          <p class="pricing-price"><sup>$</sup>%s<span class="pricing-price-note">%s</span></p>\n'
        '          <p class="fx-summary" style="margin-top:1rem">%s</p>\n        </div>\n'
        '        <div class="pricing-card reveal">\n          <p class="pricing-name">%s</p>\n'
        '          <p class="pricing-price"><sup>$</sup>%s<span class="pricing-price-note">%s</span></p>\n'
        '          <p class="fx-summary" style="margin-top:1rem">%s</p>\n'
        '          <p style="margin-top:1rem"><a href="solution-websites-seo.html" style="color:var(--gold-bright)">See the sample websites%s</a></p>\n'
        '        </div>\n'
        '      </div>\n'
        '    </div>\n'
        '    <p class="pricing-note reveal">%s <a href="%s">%s</a></p>\n'
        '  </div>\n</section>\n\n' % (
            em(hp["h"], "No contract."), t(hp["body"]),
            t(plan["name"]), t(plan["summary"]), tiers, incl,
            CONTENT["brand"]["cta_primary_href"], t(CONTENT["brand"]["cta_primary"]), t(CONTENT["brand"]["cta_primary_note"]),
            t(trap["h"]), "\n".join('            <li>%s<span>%s</span></li>' % (CHECK, t(i)) for i in trap["items"]), t(trap["fine_print"]),
            t(line["name"]), line["price"].lstrip("$"), t(line["period"]), t(line["body"]),
            t(web["name"]), web["price"].lstrip("$"), t(web["period"]), t(web["body"]), ARR,
            t(hp["example"]), hp["link_href"], t(hp["link_label"])))
    return "".join(out)


def crm_bottom():
    c, f = CONTENT["crm"], CONTENT["home"]["sections"]["faq"]
    return (faq(c["faq"], "Common questions", em(f["h"], "answers"), f["body"])
            + closing(c["closing"]["note"], em(c["closing"]["h"], "on your business."), c["closing"]["body"]))


# ---------------------------------------------------------------- Websites page
def websites_top(old):
    w = CONTENT["websites"]
    cards = "\n".join(
        '      <div class="mini-card reveal"><span class="mini-card-icon">%s</span><p class="mini-card-title">%s</p><p class="mini-card-body">%s</p></div>'
        % (CHECK, t(i["title"]), t(i["body"])) for i in w["includes"])
    sites = []
    for p in PAIRS + [EXTRA_SITE]:
        label = p.get("industry_label") or p["label"]
        d = p["website_dir"]
        links = '<a href="%s/index.html" target="_blank" rel="noopener">Open the sample site <span aria-hidden="true">&nearr;</span></a>' % d
        if "slug" in p:
            links += '<a href="%s">%s</a>' % (at(industry_href(p)), t(CONTENT["home"]["sections"]["pairs"]["card_link_label"]))
        sites.append(
            '      <li class="fx-site reveal"><img src="%s" width="1200" height="750" loading="lazy" decoding="async" alt="Home page of the %s sample website">'
            '<div class="fx-site-body"><span class="fx-site-tag">Sample website</span><span class="fx-site-ind">%s</span><h3>%s</h3>'
            '<p class="fx-site-links">%s</p></div></li>' % (site_shot(p), at(p["business"]), t(label), t(p["business"]), links))
    s = w["samples"]
    return (hero(old, w["eyebrow"], em(w["h1"], "sends every lead to your CRM."), w["sub"])
            + '  </div>\n</section>\n\n'
            '<!-- ============================ WHAT YOU GET ============================ -->\n'
            '<section class="section rule-top fx-sec" id="included">\n  <div class="container">\n'
            '    <div class="section-head">\n      <span class="eyebrow reveal">What you get</span>\n'
            '      <h2 class="display display-lg reveal" style="margin-top:1.6rem">What the <em>$499 site</em> includes</h2>\n    </div>\n'
            '    <div class="mini-grid cols-3">\n%s\n    </div>\n  </div>\n</section>\n\n'
            '<!-- ============================ SAMPLE SITES ============================ -->\n'
            '<section class="section rule-top fx-sec" id="samples">\n  <div class="container">\n'
            '    <div class="section-head">\n      <span class="eyebrow reveal">Sample websites</span>\n'
            '      <h2 class="display display-lg reveal" style="margin-top:1.6rem">%s</h2>\n      <p class="reveal">%s</p>\n    </div>\n'
            '    <ul class="fx-gallery">\n%s\n    </ul>\n'
            '    <p class="fx-foot reveal">%s</p>\n  </div>\n</section>\n\n'
            '<!-- ============================ HOW IT WORKS ============================ -->\n'
            '<section class="section rule-top fx-sec" id="how-it-works">\n  <div class="container">\n'
            '    <div class="section-head">\n      <span class="eyebrow reveal">How it works</span>\n'
            '      <h2 class="display display-lg reveal" style="margin-top:1.6rem">From a call to <em>a live site</em></h2>\n    </div>\n'
            '%s  </div>\n</section>\n\n' % (cards, em(s["h"], "we've built"), t(s["body"]), "\n".join(sites), t(s["extra_note"]),
                                            steps(w["how_it_works"])))


def websites_bottom():
    w = CONTENT["websites"]
    return (faq(w["faq"], "Common questions", "Website <em>questions</em>", "What owners ask before we build.")
            + closing("One price, paid once.", em(w["closing"]["h"], "your website."), w["closing"]["body"]))


def main():
    build_index()
    build_popup()
    frame_page("solution-crm.html", crm_top, crm_bottom, CONTENT["crm"]["sub"] + " Signature plan from $99 a month.")
    frame_page("solution-websites-seo.html", websites_top, websites_bottom, CONTENT["websites"]["sub"])
    print("built index.html #industries, see-your-business.js data, solution-crm.html, solution-websites-seo.html")


if __name__ == "__main__":
    main()
