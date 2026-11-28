"""Concept A ("Bright and product-led") generator.

Reads renders-src/site-content/content.json, renders-src/industry-crm/pairs.json and
renders-src/industry-crm/captions.json, then writes every page of
preview/concepts-2026-11/a/. Deterministic: same inputs, same output.

Images that don't exist yet (the vet screens, the three new website shots) render as a
labeled placeholder; re-run once they land and the real image takes its place.

Run: python scripts/concepts/a/build.py
"""
import json
import os
import shutil
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
OUT = os.path.join(ROOT, "preview", "concepts-2026-11", "a")
CID = "A"


def load(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return json.load(f)


C = load("renders-src/site-content/content.json")
PAIRS = load("renders-src/industry-crm/pairs.json")
CAPS = load("renders-src/industry-crm/captions.json")
B = C["brand"]
BY_SLUG = {p["slug"]: p for p in PAIRS}

# Which screen proves which benefit (screen_hint in content.json -> slug, file).
HINT = {
    "ai-call-texts": ("home-services", "6-ai-call-texts-m.webp"),
    "text-thread": ("salon-spa", "6-text-thread-m.webp"),
    "tech-get-paid": ("home-services", "3-tech-get-paid-m.webp"),
    "customer-pay": ("car-lots", "5-pay-page-m.webp"),
    "owner-home": ("home-services", "1-today-d.webp"),
    "customer-estimate": ("auto-repair", "5-customer-estimate-m.webp"),
    "estimates-awaiting": ("home-services", "4-estimates-awaiting-m.webp"),
    "dispatch-board": ("home-services", "2-dispatch-board-d.webp"),
    "booking-page": ("salon-spa", "5-booking-m.webp"),
    "industry": ("restaurants", "2-floor-plan-d.webp"),
    "website": ("home-services", "@website"),
}
# Home bento: card title -> hint.
BENTO = ["ai-call-texts", "customer-pay", "customer-estimate", "dispatch-board", "owner-home"]

e = escape


# ---------------------------------------------------------------- assets + frames
def site_dir(p):
    return p["website_dir"].split("/")[-1]


def asset(rel):
    """(exists, rel) for a repo-root-relative asset."""
    return os.path.isfile(os.path.join(ROOT, rel)), rel


def crm_rel(slug, file):
    return asset(f"assets/img/crm/industries/{slug}/{file}")


def web_rel(p, kind="d"):
    return asset(f"assets/img/websites/{site_dir(p)}-home-{kind}.webp")


def hint_rel(hint):
    slug, file = HINT[hint]
    p = BY_SLUG[slug]
    if file == "@website":
        return web_rel(p) + ("website", p)
    return crm_rel(slug, file) + ("desktop" if file.endswith("-d.webp") else "phone", p)


SIZES = {"desktop": (1440, 900), "website": (1200, 750), "phone": (585, 1266)}


def frame(R, found, kind, alt, label, cls="", eager=False, cap="top"):
    """Laptop C / Phone C (the owner's approved frames). The label is a chip outside the screen:
    below a phone; above a laptop, or below it with cap="bottom" where something sits above it."""
    ok, rel = found
    w, h = SIZES[kind]
    if ok:
        load_attr = 'fetchpriority="high"' if eager else 'loading="lazy"'
        inner = f'<img src="{R}{rel}" alt="{e(alt)}" width="{w}" height="{h}" {load_attr} decoding="async">'
    else:
        inner = f'<div class="ph" role="img" aria-label="{e(alt)}"><span>{e(label)}<br><small>Image on the way</small></span></div>'
    screen = f'<div class="screen" style="aspect-ratio:{w}/{h}">{inner}</div>'
    tag = f'<figcaption class="tag">{e(label)}</figcaption>'
    if kind == "phone":
        return f'<figure class="phone {cls}"><div class="phone-body">{screen}</div>{tag}</figure>'
    if cap == "bottom":
        return (f'<figure class="laptop cap-b {cls}"><div class="lap-screen">{screen}</div>'
                f'<div class="lap-base" aria-hidden="true"></div>{tag}</figure>')
    return (f'<figure class="laptop {cls}">{tag}<div class="lap-screen">{screen}</div>'
            f'<div class="lap-base" aria-hidden="true"></div></figure>')


def logo(R):
    return f'<span class="mark"><img src="{R}assets/logo-mark.png" alt="" width="976" height="976"></span>'


# ---------------------------------------------------------------- shell
def nav(P, R, active):
    items = [("index.html", "Home"), ("crm.html", "CRM"), ("websites.html", "Websites"),
             ("industries.html", "Industries"), ("index.html#pricing", "Pricing")]
    links = "".join(
        f'<a href="{P}{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in items)
    return f'''<header class="top">
  <div class="wrap top-in">
    <a class="brand" href="{P}index.html" aria-label="{e(B["name"])}, home">{logo(R)}<span class="word">Top Shelf</span></a>
    <span class="concept">Concept {CID} · design preview</span>
    <nav class="links" id="nav" aria-label="Main">{links}
      <a class="btn sm" href="{R}{B["cta_primary_href"]}">{e(B["cta_primary"])}</a>
    </nav>
    <button class="menu" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
  </div>
</header>'''


def footer(P, R):
    return f'''<footer class="foot">
  <div class="wrap foot-in">
    <div>
      <a class="brand" href="{P}index.html">{logo(R)}<span class="word">{e(B["name"])}</span></a>
      <p>{e(B["based_in"])}</p>
      <p><a href="{B["phone_href"]}">{e(B["phone"])}</a> · <a href="mailto:{B["email"]}">{e(B["email"])}</a></p>
    </div>
    <nav aria-label="Footer"><a href="{P}crm.html">CRM</a><a href="{P}websites.html">Websites</a><a href="{P}industries.html">Industries</a><a href="{R}{B["cta_primary_href"]}">{e(B["cta_primary"])}</a></nav>
  </div>
  <div class="wrap fine"><p>{e(C["sample_note"])}</p><p>Concept {CID} · design preview</p></div>
</footer>'''


def page(path, title, desc, body, active=""):
    depth = path.count("/")
    P = "../" * depth
    R = P + "../../../"
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="{R}assets/logo-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap">
<link rel="stylesheet" href="{P}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{nav(P, R, active)}
<main id="main">
{body(P, R)}
</main>
{footer(P, R)}
<script src="{P}assets/app.js" defer></script>
</body>
</html>
'''
    dest = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


# ---------------------------------------------------------------- shared blocks
def ctas(R, center=False):
    return (f'<div class="ctas{" center" if center else ""}"><a class="btn" href="{R}{B["cta_primary_href"]}">{e(B["cta_primary"])}</a>'
            f'<a class="btn ghost" href="{B["phone_href"]}">{e(B["cta_secondary"])}</a></div>')


def checks(items, cls="checks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def head(eyebrow, h, body="", tag="h2", cls="sec-head"):
    b = f"<p>{e(body)}</p>" if body else ""
    eb = f'<p class="eyebrow">{e(eyebrow)}</p>' if eyebrow else ""
    return f'<div class="{cls}">{eb}<{tag}>{e(h)}</{tag}>{b}</div>'


def steps(items, h="How it works"):
    li = "".join(
        f'<li><span class="num" aria-hidden="true">{e(s["step"])}</span><h3>{e(s["title"])}</h3><p>{e(s["body"])}</p></li>'
        for s in items)
    return f'<section class="sec steps-sec"><div class="wrap">{head("", h)}<ol class="steps">{li}</ol></div></section>'


def faq(items, h, body=""):
    qs = "".join(f'<details><summary>{e(q["q"])}</summary><p>{e(q["a"])}</p></details>' for q in items)
    return f'<section class="sec faq-sec" id="faq"><div class="wrap">{head("", h, body)}<div class="faq">{qs}</div></div></section>'


def closing(R, h, body, note=""):
    n = f'<p class="note">{e(note)}</p>' if note else ""
    return (f'<section class="sec closing"><div class="wrap closing-in"><h2>{e(h)}</h2><p>{e(body)}</p>'
            f'{ctas(R, True)}<p class="note">{e(B["cta_primary_note"])}</p>{n}</div></section>')


def price_card(R):
    pl = C["pricing"]["plan"]
    at = C["crm"]["anti_trap"]
    tiers = "".join(
        f'<li><span class="users">{e(t["users"])}</span><span class="amt">{e(t["price"])}</span>'
        f'<span class="per">{e(t["period"])}</span></li>' for t in pl["tiers"])
    return f'''<aside class="price-card" aria-label="{e(pl["name"])} price">
  <p class="eyebrow">{e(pl["name"])}</p>
  <ul class="tiers">{tiers}</ul>
  <p class="summary">{e(pl["summary"])}</p>
  <div class="trap"><h3>{e(at["h"])}</h3>{checks(at["items"], "nos")}<p class="fine-print">{e(at["fine_print"])}</p></div>
  <a class="btn block" href="{R}{B["cta_primary_href"]}">{e(B["cta_primary"])}</a>
  <p class="note">{e(B["cta_primary_note"])}</p>
</aside>'''


def pricing(R, extra_left=""):
    pr = C["pricing"]
    hp = C["home"]["sections"]["pricing"]
    pl, ph, wb = pr["plan"], pr["phone_line"], pr["website"]
    return f'''<section class="sec pricing" id="pricing"><div class="wrap pricing-in">
  <div class="pricing-left">
    {head("Pricing", hp["h"], hp["body"])}
    <p class="example">{e(hp["example"])}</p>
    {extra_left}
    <h3 class="minor">Everything in the {e(pl["name"])}</h3>
    {checks(pl["includes"], "checks two")}
    <div class="addons">
      <div class="addon"><p class="eyebrow">{e(ph["name"])}</p><p class="big">{e(ph["price"])} <span>{e(ph["period"])}</span></p><p>{e(ph["body"])}</p></div>
      <div class="addon"><p class="eyebrow">{e(wb["name"])}</p><p class="big">{e(wb["price"])} <span>{e(wb["period"])}</span></p><p>{e(wb["body"])}</p></div>
    </div>
    {checks(pr["terms"], "pills")}
  </div>
  {price_card(R)}
</div></section>'''


# ---------------------------------------------------------------- pair stage (switcher)
def first_screen(slug, device):
    for s in CAPS.get(slug, {}).get("screens", []):
        if s["device"] == device:
            return s
    return None


def pair_stage(R, p, eager=False):
    ps = C["home"]["sections"]["pairs"]
    d = first_screen(p["slug"], "desktop")
    m = first_screen(p["slug"], "phone")
    biz = p["business"]
    web = frame(R, web_rel(p), "website", f"{biz} sample website home page", ps["card_website_label"], "st-web", eager)
    crm = (frame(R, crm_rel(p["slug"], d["file"]), "desktop", f"{biz} sample CRM: {d['role']}", ps["card_crm_label"], "st-crm", eager, "bottom")
           if d else frame(R, (False, ""), "desktop", f"{biz} sample CRM", ps["card_crm_label"], "st-crm", cap="bottom"))
    ph = frame(R, crm_rel(p["slug"], m["file"]), "phone", f"{biz} sample CRM: {m['role']}", "Sample", "st-phone") if m else ""
    flow = ('<svg class="flow" viewBox="0 0 120 60" aria-hidden="true"><path d="M4 8 C 60 8, 60 52, 112 52" fill="none" '
            'stroke="currentColor" stroke-width="2" stroke-dasharray="5 5"/><path d="M106 46 L114 52 L106 58" fill="none" '
            'stroke="currentColor" stroke-width="2"/></svg>')
    return f'<div class="stage">{web}{flow}{crm}{ph}</div>'


def pair_panel(P, R, p, i):
    ind = C["industries"]["per_industry"][p["slug"]]
    hidden = "" if i == 0 else " hidden"
    return f'''<div class="panel" role="tabpanel" id="pp-{p["slug"]}" aria-labelledby="pt-{p["slug"]}" tabindex="0"{hidden}>
  {pair_stage(R, p, eager=(i == 0))}
  <div class="panel-copy">
    <p class="eyebrow">{e(p["industry_label"])} · {e(p["business"])}</p>
    <h3>{e(ind["headline"])}</h3>
    {checks(ind["what_owners_get"])}
    <div class="panel-links">
      <a class="btn sm" href="{P}industries/{p["slug"]}-crm.html">See the CRM</a>
      <a class="btn sm ghost" href="{P}industries/{p["slug"]}-website.html">See the website</a>
      <a class="text-link" href="{R}{p["website_dir"]}/index.html">Open the live sample site</a>
    </div>
  </div>
</div>'''


def switcher(P, R):
    tabs = "".join(
        f'<button type="button" role="tab" id="pt-{p["slug"]}" aria-controls="pp-{p["slug"]}" '
        f'aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{e(p["industry_label"])}</button>'
        for i, p in enumerate(PAIRS))
    panels = "".join(pair_panel(P, R, p, i) for i, p in enumerate(PAIRS))
    return (f'<div class="switcher"><p class="rail-label" id="rail-label">{e(C["industries"]["picker_label"])}</p>'
            f'<div class="rail" role="tablist" aria-labelledby="rail-label">{tabs}</div>{panels}</div>')


# ---------------------------------------------------------------- home
def home_body(P, R):
    h = C["home"]
    s = h["sections"]
    hero_d = frame(R, crm_rel("home-services", "1-today-d.webp"), "desktop",
                   "Everline Home Services sample CRM: the owner's morning", "Sample screens", "hero-d", True)
    hero_m = frame(R, crm_rel("home-services", "6-ai-call-texts-m.webp"), "phone",
                   "Everline Home Services sample CRM: a call the AI receptionist booked", "Sample", "hero-m", True)

    more_list = "".join(f"<li>{e(g['title'])}</li>" for g in C["crm"]["benefit_groups"])
    cards = []
    for idx, (card, hint) in enumerate(zip(s["crm"]["cards"], BENTO)):
        ok, rel, kind, p = hint_rel(hint)
        fig = frame(R, (ok, rel), kind, f"{p['business']} sample CRM screen", f"Sample · {p['business']}", "bento-shot")
        cards.append(f'<article class="bento-card b{idx} k-{kind}"><div class="bento-copy"><h3>{e(card["title"])}</h3>'
                     f'<p>{e(card["body"])}</p></div>{fig}</article>')
    cards.append(f'<a class="bento-card b5 more" href="{P}{s["crm"]["link_href"].replace("solution-crm.html", "crm.html")}">'
                 f'<h3>{e(s["crm"]["link_label"])}</h3>'
                 f'<ul class="more-list">{more_list}</ul>'
                 f'<span class="arrow" aria-hidden="true">&rarr;</span></a>')

    web_strip = "".join(
        f'<a class="web-thumb" href="{P}industries/{p["slug"]}-website.html" aria-label="{e(p["business"])} sample website">'
        f'{frame(R, web_rel(p, "m"), "phone", p["business"] + " sample website on a phone", "Sample website")}'
        f'<span>{e(p["business"])}</span></a>'
        for p in [BY_SLUG[x] for x in ("salon-spa", "restaurants", "medical-dental", "legal")])
    inc = C["websites"]["includes"]
    faq_items = [q for q in C["crm"]["faq"] if q["q"] in s["faq"]["pick"]]
    faq_items.sort(key=lambda q: s["faq"]["pick"].index(q["q"]))

    return f'''<section class="hero"><div class="wrap hero-in">
  <div class="hero-copy">
    <p class="eyebrow">{e(h["eyebrow"])}</p>
    <h1>{e(h["h1"])}</h1>
    <p class="lede">{e(h["sub"])}</p>
    {ctas(R)}
    {checks(h["proof_points"], "proof")}
  </div>
  <div class="hero-devices">{hero_d}{hero_m}</div>
</div></section>

<section class="sec" id="crm"><div class="wrap">
  {head(s["crm"]["eyebrow"], s["crm"]["h"], s["crm"]["body"])}
  <div class="bento">{"".join(cards)}</div>
</div></section>

{steps(C["crm"]["how_it_works"])}

<section class="sec wash" id="industries"><div class="wrap">
  {head(s["pairs"]["eyebrow"], s["pairs"]["h"], s["pairs"]["body"])}
  {switcher(P, R)}
</div></section>

<section class="sec" id="websites"><div class="wrap web-tease">
  <div>
    {head(s["websites"]["eyebrow"], s["websites"]["h"], s["websites"]["body"])}
    <ul class="mini-list">{"".join(f'<li><strong>{e(i["title"])}</strong> {e(i["body"])}</li>' for i in inc[:3])}</ul>
    <p class="price-line"><span class="big">{e(C["pricing"]["website"]["price"])}</span> {e(C["pricing"]["website"]["period"])}</p>
    <a class="text-link" href="{P}websites.html">{e(s["websites"]["link_label"])}</a>
  </div>
  <div class="web-strip">{web_strip}</div>
</div></section>

<section class="sec band"><div class="wrap band-in">
  <h2>{e(s["phone"]["h"])}</h2><p>{e(s["phone"]["body"])}</p>
</div></section>

{pricing(R)}
{faq(faq_items, s["faq"]["h"], s["faq"]["body"])}
{closing(R, s["closing"]["h"], s["closing"]["body"])}'''


# ---------------------------------------------------------------- crm
def crm_body(P, R):
    c = C["crm"]
    hero_d = frame(R, crm_rel("home-services", "2-dispatch-board-d.webp"), "desktop",
                   "Everline Home Services sample CRM: the dispatch board", "Sample screens", "hero-d", True)
    hero_m = frame(R, crm_rel("car-lots", "5-pay-page-m.webp"), "phone",
                   "Bramlett Motor Co. sample: a customer paying from a texted link", "Sample", "hero-m", True)
    jump = "".join(f'<a href="#g{i}">{e(g["title"])}</a>' for i, g in enumerate(c["benefit_groups"]))

    groups = []
    for i, g in enumerate(c["benefit_groups"]):
        hints = []
        for b in g["benefits"]:
            if b["screen_hint"] not in hints:
                hints.append(b["screen_hint"])
        figs = []
        for hnt in hints[:2]:
            ok, rel, kind, p = hint_rel(hnt)
            figs.append(frame(R, (ok, rel), kind, f"{p['business']} sample screen", f"Sample · {p['business']}", f"g-{kind}"))
        bl = "".join(f'<li><h4>{e(b["title"])}</h4><p>{e(b["body"])}</p></li>' for b in g["benefits"])
        groups.append(f'''<section class="group{" flip" if i % 2 else ""}" id="g{i}">
  <div class="group-copy"><h2>{e(g["title"])}</h2><p class="lede sm">{e(g["intro"])}</p><ul class="benefits">{bl}</ul></div>
  <div class="group-shots n{len(figs)}">{"".join(figs)}</div>
</section>''')

    pm = c["phone_moments"]
    moments_fig = frame(R, crm_rel("home-services", "3-tech-get-paid-m.webp"), "phone",
                        "Everline Home Services sample: getting paid at the door", "Sample")
    day = c["day_one"]
    day_html = f'<div class="day-one"><h3 class="minor">{e(day["h"])}</h3>{checks(day["items"], "checks boxes")}</div>'

    return f'''<section class="hero"><div class="wrap hero-in">
  <div class="hero-copy">
    <p class="eyebrow">{e(c["eyebrow"])}</p>
    <h1 class="h1-sm">{e(c["h1"])}</h1>
    <p class="lede">{e(c["sub"])}</p>
    {ctas(R)}
  </div>
  <div class="hero-devices">{hero_d}{hero_m}</div>
</div></section>
<nav class="jump" aria-label="On this page"><div class="wrap jump-in">{jump}</div></nav>
<div class="wrap groups">{"".join(groups)}</div>

<section class="sec wash"><div class="wrap moments">
  {moments_fig}
  <div>{head("", pm["h"])}<ol class="moment-list">{"".join(f"<li>{e(x)}</li>" for x in pm["items"])}</ol></div>
</div></section>

{steps(c["how_it_works"])}
{pricing(R, day_html)}
{faq(c["faq"], "Straight answers")}
{closing(R, c["closing"]["h"], c["closing"]["body"], c["closing"]["note"])}'''


# ---------------------------------------------------------------- websites
def sample_card(P, R, p):
    return f'''<article class="site-card">
  {frame(R, web_rel(p), "website", p["business"] + " sample website home page", "Sample website")}
  <div class="site-meta">
    <p class="eyebrow">{e(p["industry_label"])}</p>
    <h3>{e(p["business"])}</h3>
    <div class="site-links">
      <a class="text-link" href="{R}{p["website_dir"]}/index.html">Open the live sample site</a>
      <a class="text-link quiet" href="{P}industries/{p["slug"]}-website.html">About this site</a>
      <a class="text-link quiet" href="{P}industries/{p["slug"]}-crm.html">Its CRM</a>
    </div>
  </div>
</article>'''


def websites_body(P, R):
    w = C["websites"]
    lead = BY_SLUG["medical-dental"]
    hero_d = frame(R, web_rel(lead), "website", "Brightwater Dental sample website home page", "Sample website", "hero-d", True)
    hero_m = frame(R, web_rel(lead, "m"), "phone", "Brightwater Dental sample website on a phone", "Sample", "hero-m", True)
    inc = "".join(f'<li><h3>{e(i["title"])}</h3><p>{e(i["body"])}</p></li>' for i in w["includes"])
    cards = "".join(sample_card(P, R, p) for p in PAIRS)
    lw_ok, lw_rel = asset("assets/img/websites/linewright-mobile-dent-home-d.webp")
    extra = f'''<article class="site-card">
  {frame(R, (lw_ok, lw_rel), "website", "Linewright Mobile Dent Co. sample website home page", "Sample website")}
  <div class="site-meta"><p class="eyebrow">Auto</p><h3>Linewright Mobile Dent Co.</h3><p class="small">{e(w["samples"]["extra_note"])}</p>
  <div class="site-links"><a class="text-link" href="{R}websites/linewright-mobile-dent/index.html">Open the live sample site</a></div></div>
</article>'''
    ws = C["pricing"]["website"]
    return f'''<section class="hero"><div class="wrap hero-in">
  <div class="hero-copy">
    <p class="eyebrow">{e(w["eyebrow"])}</p>
    <h1 class="h1-sm">{e(w["h1"])}</h1>
    <p class="lede">{e(w["sub"])}</p>
    {ctas(R)}
  </div>
  <div class="hero-devices">{hero_d}{hero_m}</div>
</div></section>

<section class="sec"><div class="wrap includes-wrap">
  <div class="includes-head">{head("", f"What the {ws['price']} site includes")}
    <div class="price-tile"><p class="eyebrow">{e(ws["name"])}</p><p class="big">{e(ws["price"])} <span>{e(ws["period"])}</span></p><p>{e(ws["body"])}</p>
    <a class="btn block" href="{R}{B["cta_primary_href"]}">{e(B["cta_primary"])}</a></div>
  </div>
  <ul class="includes">{inc}</ul>
</div></section>

{steps(w["how_it_works"])}

<section class="sec wash" id="samples"><div class="wrap">
  {head("", w["samples"]["h"], w["samples"]["body"])}
  <div class="site-grid">{cards}{extra}</div>
</div></section>

{faq(w["faq"], "Website questions")}
{closing(R, w["closing"]["h"], w["closing"]["body"])}'''


# ---------------------------------------------------------------- industries hub
def industries_body(P, R):
    ind = C["industries"]
    ps = C["home"]["sections"]["pairs"]
    cards = []
    for p in PAIRS:
        d = first_screen(p["slug"], "desktop")
        crm = (frame(R, crm_rel(p["slug"], d["file"]), "desktop", f"{p['business']} sample CRM: {d['role']}", ps["card_crm_label"], "hub-crm")
               if d else frame(R, (False, ""), "desktop", f"{p['business']} sample CRM", ps["card_crm_label"], "hub-crm"))
        web = frame(R, web_rel(p), "website", f"{p['business']} sample website", ps["card_website_label"], "hub-web")
        cards.append(f'''<article class="hub-card" id="{p["slug"]}">
  <div class="hub-pair">{web}{crm}</div>
  <p class="eyebrow">{e(p["industry_label"])}</p>
  <h2 class="h3">{e(p["business"])}</h2>
  <p>{e(ind["per_industry"][p["slug"]]["headline"])}</p>
  <div class="panel-links"><a class="btn sm" href="{P}industries/{p["slug"]}-crm.html">See the CRM</a><a class="btn sm ghost" href="{P}industries/{p["slug"]}-website.html">See the website</a></div>
</article>''')
    cu = C["custom"]
    return f'''<section class="hero hero-plain"><div class="wrap">
  <p class="eyebrow">{e(ps["eyebrow"])}</p><h1 class="h1-sm">{e(ind["h1"])}</h1><p class="lede">{e(ind["sub"])}</p>
</div></section>
<section class="sec tight"><div class="wrap"><div class="hub-grid">{"".join(cards)}</div></div></section>
<section class="sec band"><div class="wrap band-in"><h2>{e(cu["h"])}</h2><p>{e(cu["body"])}</p>{ctas(R)}</div></section>'''


# ---------------------------------------------------------------- per industry
def neighbors(p):
    i = PAIRS.index(p)
    return PAIRS[i - 1], PAIRS[(i + 1) % len(PAIRS)]


def pager(P, p, kind):
    prev, nxt = neighbors(p)
    return (f'<nav class="pager wrap" aria-label="More industries"><a href="{prev["slug"]}-{kind}.html">&larr; {e(prev["industry_label"])}</a>'
            f'<a href="{P}industries.html">All industries</a><a href="{nxt["slug"]}-{kind}.html">{e(nxt["industry_label"])} &rarr;</a></nav>')


def crumbs(P, p, kind):
    return (f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{P}industries.html">Industries</a> / '
            f'<span>{e(p["industry_label"])}</span> / <span>{kind}</span></nav>')


def switch_tabs(p, kind):
    other = "website" if kind == "crm" else "crm"
    labels = {"crm": "Sample CRM", "website": "Sample website"}
    return (f'<div class="seg" aria-label="{e(p["business"])}"><a href="{p["slug"]}-crm.html"{" aria-current=\"page\"" if kind == "crm" else ""}>{labels["crm"]}</a>'
            f'<a href="{p["slug"]}-website.html"{" aria-current=\"page\"" if kind == "website" else ""}>{labels["website"]}</a></div>')


def industry_crm(p):
    ind = C["industries"]["per_industry"][p["slug"]]
    cap = CAPS.get(p["slug"], {})
    screens = cap.get("screens", [])

    def body(P, R):
        desk, phones = [], []
        for s in screens:
            alt = f"{p['business']} sample CRM: {s['role']}"
            if s["device"] == "desktop":
                desk.append(f'<div class="shot-row">{frame(R, crm_rel(p["slug"], s["file"]), "desktop", alt, "Sample screens")}'
                            f'<div class="shot-cap"><p class="role">{e(s["role"])}</p><p>{e(s["caption"])}</p></div></div>')
            else:
                phones.append(f'<div class="shot-phone">{frame(R, crm_rel(p["slug"], s["file"]), "phone", alt, "Sample")}'
                              f'<p class="role">{e(s["role"])}</p><p>{e(s["caption"])}</p></div>')
        if not screens:
            gallery = (f'<div class="pending">{frame(R, (False, ""), "desktop", p["business"] + " sample CRM", "Sample screens")}'
                       f'<p>The sample screens for {e(p["business"])} are being finished.</p></div>')
        else:
            gallery = "".join(desk) + (f'<div class="phones n{len(phones)}">{"".join(phones)}</div>' if phones else "")
        built = f'<p class="built">{e(cap["built_around"])}</p>' if cap.get("built_around") else ""
        return f'''<section class="hero hero-plain"><div class="wrap ind-head">
  <div>{crumbs(P, p, "CRM")}
  <p class="eyebrow">Sample CRM · {e(p["business"])}</p>
  <h1 class="h1-sm">{e(ind["headline"])}</h1>
  <p class="lede">{e(ind["crm_intro"])}</p>{built}
  {switch_tabs(p, "crm")}</div>
  <div class="owner-get"><h2 class="minor">What owners get</h2>{checks(ind["what_owners_get"])}{ctas(R)}</div>
</div></section>
<section class="sec tight"><div class="wrap gallery">{gallery}</div></section>
<section class="sec wash"><div class="wrap cross">
  {frame(R, web_rel(p), "website", p["business"] + " sample website", "Sample website")}
  <div><p class="eyebrow">Same business, same look</p><h2>{e(p["business"])} sample website</h2><p>{e(ind["website_intro"])}</p>
  <div class="panel-links"><a class="btn sm" href="{p["slug"]}-website.html">See the website</a><a class="text-link" href="{R}{p["website_dir"]}/index.html">Open the live sample site</a></div></div>
</div></section>
{price_strip(R)}
{pager(P, p, "crm")}'''
    page(f"industries/{p['slug']}-crm.html", f"{p['business']} sample CRM · {p['industry_label']} · Top Shelf",
         ind["crm_intro"], body, "industries.html")


def price_strip(R):
    t = C["pricing"]["plan"]["tiers"][0]
    return (f'<section class="sec band"><div class="wrap band-in"><h2>{e(C["custom"]["h"])}</h2><p>{e(C["custom"]["body"])}</p>'
            f'<p class="price-line"><span class="big">{e(t["price"])}</span> {e(t["period"])} · {e(t["users"])}</p>{ctas(R)}</div></section>')


def industry_web(p):
    ind = C["industries"]["per_industry"][p["slug"]]
    w = C["websites"]
    ws = C["pricing"]["website"]

    def body(P, R):
        inc = "".join(f'<li><h3>{e(i["title"])}</h3><p>{e(i["body"])}</p></li>' for i in w["includes"])
        d = first_screen(p["slug"], "desktop")
        crm = (frame(R, crm_rel(p["slug"], d["file"]), "desktop", f"{p['business']} sample CRM: {d['role']}", "Sample CRM")
               if d else frame(R, (False, ""), "desktop", f"{p['business']} sample CRM", "Sample CRM"))
        return f'''<section class="hero hero-plain"><div class="wrap ind-head">
  <div>{crumbs(P, p, "Website")}
  <p class="eyebrow">Sample website · {e(p["business"])}</p>
  <h1 class="h1-sm">{e(p["business"])}</h1>
  <p class="lede">{e(ind["website_intro"])}</p>
  {switch_tabs(p, "website")}
  <div class="ctas"><a class="btn" href="{R}{p["website_dir"]}/index.html">Open the live sample site</a><a class="btn ghost" href="{R}{B["cta_primary_href"]}">{e(B["cta_primary"])}</a></div></div>
</div></section>
<section class="sec tight"><div class="wrap web-show">
  {frame(R, web_rel(p), "website", p["business"] + " sample website home page", "Sample website", "ws-d", True)}
  {frame(R, web_rel(p, "m"), "phone", p["business"] + " sample website on a phone", "Sample", "ws-m", True)}
</div></section>
<section class="sec"><div class="wrap includes-wrap">
  <div class="includes-head">{head("", f"What the {ws['price']} site includes")}
    <div class="price-tile"><p class="eyebrow">{e(ws["name"])}</p><p class="big">{e(ws["price"])} <span>{e(ws["period"])}</span></p><p>{e(ws["body"])}</p>
    <a class="btn block" href="{R}{B["cta_primary_href"]}">{e(B["cta_primary"])}</a></div>
  </div>
  <ul class="includes">{inc}</ul>
</div></section>
<section class="sec wash"><div class="wrap cross">
  {crm}
  <div><p class="eyebrow">Same business, same look</p><h2>{e(p["business"])} sample CRM</h2><p>{e(ind["crm_intro"])}</p>
  <div class="panel-links"><a class="btn sm" href="{p["slug"]}-crm.html">See the CRM</a></div></div>
</div></section>
{pager(P, p, "website")}'''
    page(f"industries/{p['slug']}-website.html", f"{p['business']} sample website · {p['industry_label']} · Top Shelf",
         ind["website_intro"], body, "industries.html")


# ---------------------------------------------------------------- main
def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"))
    for f in ("style.css", "app.js"):
        shutil.copyfile(os.path.join(HERE, f), os.path.join(OUT, "assets", f))
    page("index.html", "Top Shelf CRM · Run the whole business from one app", C["home"]["sub"], home_body, "index.html")
    page("crm.html", "The Top Shelf CRM · Everything in one app", C["crm"]["sub"], crm_body, "crm.html")
    page("websites.html", "Websites from $499 · Top Shelf", C["websites"]["sub"], websites_body, "websites.html")
    page("industries.html", "Industries · A website and a CRM that go together · Top Shelf", C["industries"]["sub"],
         industries_body, "industries.html")
    for p in PAIRS:
        industry_crm(p)
        industry_web(p)
    n = sum(len(fs) for _, _, fs in os.walk(OUT) if fs and any(x.endswith(".html") for x in fs))
    missing = sorted({r for r in _missing()})
    print(f"Concept {CID}: wrote {n} files to {os.path.relpath(OUT, ROOT)}")
    if missing:
        print("Placeholders for images not on disk yet:\n  " + "\n  ".join(missing))


def _missing():
    for p in PAIRS:
        for kind in ("d", "m"):
            ok, rel = web_rel(p, kind)
            if not ok:
                yield rel
        if p["slug"] not in CAPS:
            yield f"captions.json has no '{p['slug']}' set (screens pending)"
        for s in CAPS.get(p["slug"], {}).get("screens", []):
            ok, rel = crm_rel(p["slug"], s["file"])
            if not ok:
                yield rel


if __name__ == "__main__":
    main()
