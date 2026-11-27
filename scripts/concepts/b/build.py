"""Concept B, "Cinematic product showcase": generator.

Reads renders-src/site-content/content.json, renders-src/industry-crm/pairs.json and
renders-src/industry-crm/captions.json and writes every page into
preview/concepts-2026-11/b/. Deterministic: same inputs, same bytes out.

    python scripts/concepts/b/build.py
"""
import json
import os
import shutil
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = ROOT / "preview" / "concepts-2026-11" / "b"

C = json.loads((ROOT / "renders-src/site-content/content.json").read_text(encoding="utf-8"))
PAIRS = json.loads((ROOT / "renders-src/industry-crm/pairs.json").read_text(encoding="utf-8"))
CAPS = json.loads((ROOT / "renders-src/industry-crm/captions.json").read_text(encoding="utf-8"))
B = C["brand"]

GSAP = "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"
ST = "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"
LENIS = "https://cdn.jsdelivr.net/npm/lenis@1.1.20/dist/lenis.min.js"
FONTS = "https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@500&family=Sora:wght@500;600;700&display=swap"

e = escape  # every content string goes through this


def site_base(p):
    return os.path.basename(p["website_dir"])


def screens(slug):
    return CAPS.get(slug, {}).get("screens", [])


def first_desktop(slug):
    return next((s for s in screens(slug) if s["device"] == "desktop"), None)


class Ctx:
    """Relative path helpers for a page at a given folder depth inside the concept."""

    def __init__(self, depth):
        self.pre = "../" * depth            # to the concept root
        self.repo = self.pre + "../../../"  # to the repo root

    def crm_img(self, slug, file):
        return f"{self.repo}assets/img/crm/industries/{slug}/{file}"

    def web_img(self, p, kind="d"):
        return f"{self.repo}assets/img/websites/{site_base(p)}-home-{kind}.webp"

    def live(self, p):
        return f"{self.repo}{p['website_dir']}/index.html"


# ---------- small building blocks ----------

def split_words(text):
    words = e(text).split(" ")
    return " ".join(f'<span class="wl"><span class="w">{w}</span></span>' for w in words)


def img(src, alt, w, h, lazy=True):
    return (f'<img src="{src}" alt="{e(alt)}" width="{w}" height="{h}"'
            f'{" loading=\"lazy\"" if lazy else ""} decoding="async"'
            ' onerror="this.parentNode.classList.add(\'is-missing\')">')


def desk(src, alt, label="", lazy=True, cls=""):
    lab = f'<figcaption class="chip">{e(label)}</figcaption>' if label else ""
    return (f'<figure class="dev dev-desk {cls}" data-missing="{e(alt)}">'
            f'<div class="dev-bar" aria-hidden="true"><i></i><i></i><i></i></div>'
            f'{img(src, alt, 1440, 900, lazy)}{lab}</figure>')


def phone(src, alt, label="", lazy=True, cls=""):
    lab = f'<figcaption class="chip">{e(label)}</figcaption>' if label else ""
    return (f'<figure class="dev dev-phone {cls}" data-missing="{e(alt)}">'
            f'{img(src, alt, 585, 1266, lazy)}{lab}</figure>')


def browser(src, alt, label="", lazy=True, cls=""):
    lab = f'<figcaption class="chip">{e(label)}</figcaption>' if label else ""
    return (f'<figure class="dev dev-browser {cls}" data-missing="{e(alt)}">'
            f'<div class="dev-bar" aria-hidden="true"><i></i><i></i><i></i><span></span></div>'
            f'{img(src, alt, 1200, 750, lazy)}{lab}</figure>')


def shot(cx, slug, s, lazy=True, cls=""):
    biz = next(p["business"] for p in PAIRS if p["slug"] == slug)
    alt = f"Sample screen: {biz}, {s['role']}"
    f = desk if s["device"] == "desktop" else phone
    return f(cx.crm_img(slug, s["file"]), alt, "Sample screens · " + s["role"], lazy, cls)


def ctas(cx, note=True):
    n = f'<p class="cta-note">{e(B["cta_primary_note"])}</p>' if note else ""
    return (f'<div class="ctas"><a class="btn btn-main" href="{cx.repo}{B["cta_primary_href"]}">{e(B["cta_primary"])}</a>'
            f'<a class="btn btn-ghost" href="{B["phone_href"]}">{e(B["cta_secondary"])}</a></div>{n}')


def eyebrow(t):
    return f'<p class="eyebrow">{e(t)}</p>'


def faq(items, h="Straight answers", sub=""):
    rows = "".join(f'<details class="qa reveal"><summary>{e(q["q"])}</summary><p>{e(q["a"])}</p></details>' for q in items)
    s = f'<p class="lede">{e(sub)}</p>' if sub else ""
    return f'<section class="sec faq" id="faq"><div class="wrap narrow"><h2 class="h2 reveal">{e(h)}</h2>{s}<div class="qas">{rows}</div></div></section>'


def steps(items, h):
    li = "".join(f'<li class="step reveal"><span class="step-n">{e(i["step"])}</span><h3>{e(i["title"])}</h3><p>{e(i["body"])}</p></li>' for i in items)
    return f'<section class="sec"><div class="wrap"><h2 class="h2 reveal">{e(h)}</h2><ol class="steps">{li}</ol></div></section>'


def pricing(cx, h=None, body=None, focus="plan"):
    pr = C["pricing"]
    plan, line, web = pr["plan"], pr["phone_line"], pr["website"]
    h = h or C["home"]["sections"]["pricing"]["h"]
    body = body or C["home"]["sections"]["pricing"]["body"]
    tiers = "".join(f'<li class="tier"><span class="tier-p">{e(t["price"])}</span><span class="tier-per">{e(t["period"])}</span><span class="tier-u">{e(t["users"])}</span></li>' for t in plan["tiers"])
    terms = "".join(f"<li>{e(t)}</li>" for t in pr["terms"])
    mega_price, mega_label = (web["price"], f'{web["name"]}, {web["period"]}') if focus == "website" else (plan["tiers"][0]["price"], f'{plan["name"]}, {plan["tiers"][0]["period"]}, {plan["tiers"][0]["users"]}')
    return f'''<section class="sec price" id="pricing" aria-labelledby="price-h">
<div class="price-glow" aria-hidden="true"></div>
<div class="wrap">
  <h2 class="h2 center reveal" id="price-h">{e(h)}</h2>
  <p class="lede center reveal">{e(body)}</p>
  <p class="mega" aria-hidden="true"><span class="mega-n">{e(mega_price)}</span></p>
  <p class="mega-label center">{e(mega_label)}</p>
  <div class="price-grid">
    <div class="pcard pcard-plan reveal">
      <h3>{e(plan["name"])}</h3><p>{e(plan["summary"])}</p>
      <ul class="tiers">{tiers}</ul>
    </div>
    <div class="pcard reveal"><h3>{e(line["name"])}</h3><p class="pcard-p"><b>{e(line["price"])}</b> {e(line["period"])}</p><p>{e(line["body"])}</p></div>
    <div class="pcard reveal"><h3>{e(web["name"])}</h3><p class="pcard-p"><b>{e(web["price"])}</b> {e(web["period"])}</p><p>{e(web["body"])}</p></div>
  </div>
  <ul class="terms reveal">{terms}</ul>
  <p class="example center reveal">{e(C["home"]["sections"]["pricing"]["example"])}</p>
  <div class="center reveal">{ctas(cx, note=False)}</div>
</div></section>'''


def closing(cx, blk):
    note = f'<p class="cta-note">{e(blk["note"])}</p>' if blk.get("note") else ""
    return f'''<section class="sec closing"><div class="wrap narrow center">
<h2 class="h2 reveal">{e(blk["h"])}</h2><p class="lede reveal">{e(blk["body"])}</p>
<div class="reveal">{ctas(cx)}</div>{note}</div></section>'''


# ---------- page shell ----------

NAV = [("index.html", "Home"), ("crm.html", "CRM"), ("websites.html", "Websites"), ("industries.html", "Industries")]


def shell(cx, title, desc, body, active):
    nav = "".join(f'<a href="{cx.pre}{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV)
    foot_nav = "".join(f'<a href="{cx.pre}{h}">{t}</a>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{cx.pre}assets/style.css">
<link rel="icon" href="{cx.repo}assets/logo-mark.png">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap top-in">
    <a class="logo" href="{cx.pre}index.html"><img src="{cx.repo}assets/logo-mark.png" alt="" width="34" height="34"><span>Top Shelf</span></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <a class="btn btn-main btn-sm" href="{cx.repo}{B["cta_primary_href"]}">{e(B["cta_primary"])}</a>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="wrap foot-in">
    <div><a class="logo" href="{cx.pre}index.html"><img src="{cx.repo}assets/logo-mark.png" alt="" width="34" height="34"><span>{e(B["name"])}</span></a>
      <p>{e(B["based_in"])}</p>
      <p><a href="{B["phone_href"]}">{e(B["phone"])}</a> · <a href="mailto:{e(B["email"])}">{e(B["email"])}</a></p></div>
    <nav class="foot-nav" aria-label="Footer">{foot_nav}</nav>
  </div>
  <p class="wrap fine">{e(C["sample_note"])}</p>
</footer>
<p class="concept-tag">Concept b · design preview</p>
<script src="{GSAP}" defer></script>
<script src="{ST}" defer></script>
<script src="{LENIS}" defer></script>
<script src="{cx.pre}assets/site.js" defer></script>
</body>
</html>
'''


# ---------- pages ----------

STAGE = [  # the five beats of one job, told with Everline's screens
    ("A call comes in", 0, "6-ai-call-texts-m.webp"),
    ("It's booked", 3, "2-dispatch-board-d.webp"),
    ("The estimate goes out", 2, "5-customer-estimate-m.webp"),
    ("They pay from their phone", 1, "3-tech-get-paid-m.webp"),
    ("You ask for the review", 4, "1-today-d.webp"),
]


def home():
    cx = Ctx(0)
    h = C["home"]
    s = h["sections"]
    hs = "home-services"
    caps = {x["file"]: x for x in screens(hs)}
    proof = "".join(f"<li>{e(p)}</li>" for p in h["proof_points"])
    d1, p1 = caps.get("1-today-d.webp"), caps.get("6-ai-call-texts-m.webp")
    hero_vis = ""
    if d1 and p1:
        hero_vis = (f'<div class="hero-stage" aria-label="Sample screens">{shot(cx, hs, d1, False, "hero-desk")}'
                    f'{shot(cx, hs, p1, False, "hero-phone")}</div>')

    beats, rail = [], []
    for i, (title, card, file) in enumerate(STAGE):
        cd = s["crm"]["cards"][card]
        sc = caps.get(file)
        fig = shot(cx, hs, sc, True, "beat-dev") if sc else ""
        beats.append(f'''<li class="beat"><div class="beat-copy"><p class="beat-n">0{i + 1}</p>
<h3 class="beat-h">{e(title)}</h3><p class="beat-sub">{e(cd["title"])}</p><p>{e(cd["body"])}</p></div>
<div class="beat-shot">{fig}</div></li>''')
        rail.append(f"<li>{e(title)}</li>")

    cards = []
    for p in PAIRS:
        d = first_desktop(p["slug"])
        crm = desk(cx.crm_img(p["slug"], d["file"]), f'Sample CRM: {p["business"]}', s["pairs"]["card_crm_label"], cls="pair-crm") if d \
            else f'<figure class="dev dev-desk pair-crm is-missing" data-missing="{e(p["business"])}"></figure>'
        web = phone(cx.web_img(p, "m"), f'Sample website: {p["business"]}', s["pairs"]["card_website_label"], cls="pair-web")
        cards.append(f'''<li class="pair reveal"><div class="pair-vis">{crm}{web}</div>
<p class="pair-ind">{e(p["industry_label"])}</p><h3 class="pair-biz"><a href="industries.html#{p["slug"]}">{e(p["business"])}</a></h3>
<p class="pair-tags">{e(s["pairs"]["card_website_label"])} · {e(s["pairs"]["card_crm_label"])}</p>
<p class="pair-link" aria-hidden="true">{e(s["pairs"]["card_link_label"])} →</p></li>''')

    fan = "".join(phone(cx.web_img(p, "m"), f'Sample website: {p["business"]}', cls=f"fan-{i}") for i, p in
                  enumerate([x for x in PAIRS if x["slug"] in ("salon-spa", "home-services", "restaurants")]))
    picks = [q for q in C["crm"]["faq"] if q["q"] in s["faq"]["pick"]]

    body = f'''
<section class="hero">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="wrap hero-in">
    {eyebrow(h["eyebrow"])}
    <h1 class="h1 h-split">{split_words(h["h1"])}</h1>
    <p class="lede hero-sub">{e(h["sub"])}</p>
    {ctas(cx)}
    <ul class="proof">{proof}</ul>
  </div>
  {hero_vis}
</section>

<section class="sec stage" id="crm" aria-labelledby="stage-h">
  <div class="wrap">
    {eyebrow(s["crm"]["eyebrow"])}
    <h2 class="h2" id="stage-h">{e(s["crm"]["h"])}</h2>
    <p class="lede">{e(s["crm"]["body"])}</p>
    <p class="sample-tag">Sample screens · {e(PAIRS[0]["business"])}</p>
  </div>
  <div class="stage-pin">
    <ol class="rail" aria-hidden="true">{"".join(rail)}</ol>
    <ol class="beats wrap">{"".join(beats)}</ol>
  </div>
  <div class="wrap"><a class="more" href="crm.html">{e(s["crm"]["link_label"])} →</a></div>
</section>

<section class="sec pairs" id="pairs">
  <div class="wrap">
    {eyebrow(s["pairs"]["eyebrow"])}
    <h2 class="h2 reveal">{e(s["pairs"]["h"])}</h2>
    <p class="lede reveal">{e(s["pairs"]["body"])}</p>
    <ul class="pair-grid">{"".join(cards)}</ul>
  </div>
</section>

<section class="sec split">
  <div class="wrap split-in">
    <div>{eyebrow(s["websites"]["eyebrow"])}<h2 class="h2 reveal">{e(s["websites"]["h"])}</h2>
      <p class="lede reveal">{e(s["websites"]["body"])}</p>
      <a class="more" href="websites.html">{e(s["websites"]["link_label"])} →</a></div>
    <div class="fan" aria-label="Sample websites">{fan}</div>
  </div>
</section>

<section class="sec line-sec">
  <div class="wrap narrow center">
    <h2 class="h2 reveal">{e(s["phone"]["h"])}</h2>
    <p class="lede reveal">{e(s["phone"]["body"])}</p>
  </div>
</section>

{pricing(cx)}
{faq(picks, s["faq"]["h"], s["faq"]["body"])}
{closing(cx, s["closing"])}
'''
    return shell(cx, "Top Shelf CRM: run the whole business from one app (Concept B)", h["sub"], body, "index.html")


HINT = {"ai-call-texts": "6", "text-thread": "6", "tech-get-paid": "3", "customer-pay": "3",
        "customer-estimate": "5", "estimates-awaiting": "4", "owner-home": "1", "dispatch-board": "2"}


def crm():
    cx = Ctx(0)
    c = C["crm"]
    hs = "home-services"
    by_n = {x["file"].split("-")[0]: x for x in screens(hs)}
    groups = []
    for gi, g in enumerate(c["benefit_groups"]):
        hint = g["benefits"][0]["screen_hint"]
        if hint in HINT and HINT[hint] in by_n:
            vis = shot(cx, hs, by_n[HINT[hint]])
        elif hint in ("website", "booking-page"):
            vis = phone(cx.web_img(PAIRS[0], "m"), f'Sample website: {PAIRS[0]["business"]}', "Sample website · " + PAIRS[0]["business"])
        else:  # "industry": a small wall of other trades
            wall = "".join(desk(cx.crm_img(p["slug"], first_desktop(p["slug"])["file"]), f'Sample CRM: {p["business"]}')
                           for p in PAIRS if p["slug"] in ("auto-repair", "salon-spa", "restaurants", "legal") and first_desktop(p["slug"]))
            vis = f'<div class="wall">{wall}</div><p class="sample-tag">Sample screens</p>'
        bens = "".join(f'<li class="reveal"><h4>{e(b["title"])}</h4><p>{e(b["body"])}</p></li>' for b in g["benefits"])
        groups.append(f'''<article class="group{" flip" if gi % 2 else ""}">
<div class="group-copy"><p class="beat-n">0{gi + 1}</p><h3 class="h3 reveal">{e(g["title"])}</h3><p class="lede reveal">{e(g["intro"])}</p><ul class="bens">{bens}</ul></div>
<div class="group-vis">{vis}</div></article>''')
    moments = "".join(f'<li class="reveal"><span class="tick" aria-hidden="true"></span>{e(m)}</li>' for m in c["phone_moments"]["items"])
    day = "".join(f'<li class="reveal"><span class="tick" aria-hidden="true"></span>{e(m)}</li>' for m in c["day_one"]["items"])
    trap = "".join(f'<li class="reveal"><span class="x" aria-hidden="true"></span>{e(m)}</li>' for m in c["anti_trap"]["items"])
    incl = "".join(f"<li>{e(i)}</li>" for i in C["pricing"]["plan"]["includes"])
    body = f'''
<section class="hero hero-page">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="wrap hero-in">{eyebrow(c["eyebrow"])}<h1 class="h1 h-split">{split_words(c["h1"])}</h1>
  <p class="lede hero-sub">{e(c["sub"])}</p>{ctas(cx)}</div>
</section>
<section class="sec groups"><div class="wrap">{"".join(groups)}</div></section>
<section class="sec"><div class="wrap two">
  <div><h2 class="h2 reveal">{e(c["phone_moments"]["h"])}</h2><ul class="ticks">{moments}</ul></div>
  <div><h2 class="h2 reveal">{e(c["day_one"]["h"])}</h2><ul class="ticks">{day}</ul></div>
</div></section>
{steps(c["how_it_works"], "How it works")}
<section class="sec"><div class="wrap two">
  <div class="trap"><h2 class="h2 reveal">{e(c["anti_trap"]["h"])}</h2><ul class="xs">{trap}</ul><p class="fine">{e(c["anti_trap"]["fine_print"])}</p></div>
  <div class="incl"><h2 class="h3 reveal">{e(C["pricing"]["plan"]["name"])}</h2><p>{e(C["pricing"]["plan"]["summary"])}</p><ul class="incl-list">{incl}</ul></div>
</div></section>
{pricing(cx)}
{faq(c["faq"])}
{closing(cx, c["closing"])}
'''
    return shell(cx, "The Top Shelf CRM: every benefit, price and answer (Concept B)", c["sub"], body, "crm.html")


def websites():
    cx = Ctx(0)
    w = C["websites"]
    inc = "".join(f'<li class="inc reveal"><h3>{e(i["title"])}</h3><p>{e(i["body"])}</p></li>' for i in w["includes"])
    cards = []
    extra = {"business": "Linewright Mobile Dent Co.", "website_dir": "websites/linewright-mobile-dent", "industry_label": "Auto", "slug": ""}
    for p in PAIRS + [extra]:
        links = f'<a href="{cx.live(p)}">Open the live sample site</a>'
        if p["slug"]:
            links += f'<a href="industries/{p["slug"]}-website.html">Website page</a><a href="industries/{p["slug"]}-crm.html">Its CRM</a>'
        cards.append(f'''<li class="site reveal">{browser(cx.web_img(p, "d"), f'Sample website: {p["business"]}', "Sample website")}
<p class="pair-ind">{e(p["industry_label"])}</p><h3 class="pair-biz">{e(p["business"])}</h3><p class="site-links">{links}</p></li>''')
    body = f'''
<section class="hero hero-page">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="wrap hero-in">{eyebrow(w["eyebrow"])}<h1 class="h1 h-split">{split_words(w["h1"])}</h1>
  <p class="lede hero-sub">{e(w["sub"])}</p>{ctas(cx)}</div>
</section>
<section class="sec"><div class="wrap"><h2 class="h2 reveal">What the $499 site includes</h2><ul class="incs">{inc}</ul></div></section>
{steps(w["how_it_works"], "How it works")}
<section class="sec" id="samples"><div class="wrap">
  <h2 class="h2 reveal">{e(w["samples"]["h"])}</h2><p class="lede reveal">{e(w["samples"]["body"])}</p>
  <ul class="site-grid">{"".join(cards)}</ul><p class="fine">{e(w["samples"]["extra_note"])}</p>
</div></section>
{pricing(cx, "One price, one time.", C["pricing"]["website"]["body"], focus="website")}
{faq(w["faq"])}
{closing(cx, w["closing"])}
'''
    return shell(cx, "Top Shelf websites: $499 one time, every lead into your CRM (Concept B)", w["sub"], body, "websites.html")


def industries():
    cx = Ctx(0)
    ind = C["industries"]
    chips = "".join(f'<li><a href="#{p["slug"]}">{e(p["industry_label"])}</a></li>' for p in PAIRS)
    rows = []
    for p in PAIRS:
        pi = ind["per_industry"][p["slug"]]
        d = first_desktop(p["slug"])
        crm = desk(cx.crm_img(p["slug"], d["file"]), f'Sample CRM: {p["business"]}', "Sample CRM", cls="ind-crm") if d \
            else f'<figure class="dev dev-desk ind-crm is-missing" data-missing="{e(p["business"])}"></figure>'
        rows.append(f'''<article class="ind" id="{p["slug"]}" aria-labelledby="h-{p["slug"]}">
<div class="ind-head"><p class="pair-ind">{e(p["industry_label"])} · {e(p["business"])}</p><h2 class="h3" id="h-{p["slug"]}">{e(pi["headline"])}</h2></div>
<div class="ind-vis">{browser(cx.web_img(p, "d"), f'Sample website: {p["business"]}', "Sample website", cls="ind-web")}{crm}</div>
<p class="ind-links"><a class="btn btn-ghost btn-sm" href="industries/{p["slug"]}-website.html">The website</a><a class="btn btn-ghost btn-sm" href="industries/{p["slug"]}-crm.html">The CRM</a><a class="ind-live" href="{cx.live(p)}">Open the live sample site →</a></p>
</article>''')
    body = f'''
<section class="hero hero-page">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="wrap hero-in">{eyebrow("Industries")}<h1 class="h1 h-split">{split_words(ind["h1"])}</h1>
  <p class="lede hero-sub">{e(ind["sub"])}</p></div>
</section>
<nav class="picker" aria-label="{e(ind["picker_label"])}"><div class="wrap"><p class="picker-l">{e(ind["picker_label"])}</p><ul>{chips}</ul></div></nav>
<section class="sec inds"><div class="wrap">{"".join(rows)}</div></section>
<section class="sec closing"><div class="wrap narrow center"><h2 class="h2 reveal">{e(C["custom"]["h"])}</h2><p class="lede reveal">{e(C["custom"]["body"])}</p>{ctas(cx)}</div></section>
'''
    return shell(cx, "Industries: one business, one website, one CRM (Concept B)", ind["sub"], body, "industries.html")


def ind_crm(p):
    cx = Ctx(1)
    pi = C["industries"]["per_industry"][p["slug"]]
    cap = CAPS.get(p["slug"], {})
    sc = screens(p["slug"])
    desks = "".join(f'<li class="reveal">{shot(cx, p["slug"], s)}<p class="cap">{e(s["caption"])}</p></li>' for s in sc if s["device"] == "desktop")
    phones = "".join(f'<li class="reveal">{shot(cx, p["slug"], s)}<p class="cap">{e(s["caption"])}</p></li>' for s in sc if s["device"] == "phone")
    gets = "".join(f'<li class="reveal"><span class="tick" aria-hidden="true"></span>{e(g)}</li>' for g in pi["what_owners_get"])
    gallery = (f'<ul class="shots-d">{desks}</ul><ul class="shots-m">{phones}</ul>' if sc
               else '<p class="lede">The sample screens for this business are still being made.</p>')
    built = f'<p class="lede reveal">{e(cap["built_around"])}</p>' if cap.get("built_around") else ""
    body = f'''
<section class="hero hero-page">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="wrap hero-in"><p class="eyebrow"><a href="../industries.html#{p["slug"]}">{e(p["industry_label"])}</a> · Sample CRM</p>
  <h1 class="h1 h1-s h-split">{split_words(pi["headline"])}</h1>
  <p class="lede hero-sub">{e(pi["crm_intro"])}</p>{ctas(cx)}</div>
</section>
<section class="sec"><div class="wrap">
  <p class="sample-tag">Sample screens · {e(p["business"])}</p>{built}
  {gallery}
</div></section>
<section class="sec"><div class="wrap two">
  <div><h2 class="h2 reveal">What {e(p["business"])} gets</h2><ul class="ticks">{gets}</ul></div>
  <div class="pcard reveal"><h3>{e(C["pricing"]["plan"]["name"])}</h3><p class="pcard-p"><b>{e(C["pricing"]["plan"]["tiers"][0]["price"])}</b> {e(C["pricing"]["plan"]["tiers"][0]["period"])}, {e(C["pricing"]["plan"]["tiers"][0]["users"])}</p>
  <p>{e(C["custom"]["body"])}</p><p class="ind-links"><a class="btn btn-ghost btn-sm" href="{p["slug"]}-website.html">See its website</a><a class="btn btn-ghost btn-sm" href="../crm.html">Everything the CRM does</a></p></div>
</div></section>
{closing(cx, C["crm"]["closing"])}
'''
    return shell(cx, f'{p["business"]} sample CRM, {p["industry_label"]} (Concept B)', pi["crm_intro"], body, "industries.html")


def ind_web(p):
    cx = Ctx(1)
    pi = C["industries"]["per_industry"][p["slug"]]
    inc = "".join(f'<li class="inc reveal"><h3>{e(i["title"])}</h3><p>{e(i["body"])}</p></li>' for i in C["websites"]["includes"])
    web = C["pricing"]["website"]
    body = f'''
<section class="hero hero-page">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="wrap hero-in"><p class="eyebrow"><a href="../industries.html#{p["slug"]}">{e(p["industry_label"])}</a> · Sample website</p>
  <h1 class="h1 h1-s h-split">{split_words(p["business"])}</h1>
  <p class="lede hero-sub">{e(pi["website_intro"])}</p>
  <div class="ctas"><a class="btn btn-main" href="{cx.live(p)}">Open the live sample site</a><a class="btn btn-ghost" href="{p["slug"]}-crm.html">See its CRM</a></div></div>
</section>
<section class="sec"><div class="wrap web-pair">
  {browser(cx.web_img(p, "d"), f'Sample website: {p["business"]}, home page on a computer', "Sample website · desktop", cls="web-d")}
  {phone(cx.web_img(p, "m"), f'Sample website: {p["business"]}, home page on a phone', "Sample website · phone", cls="web-m")}
</div></section>
<section class="sec"><div class="wrap"><h2 class="h2 reveal">What your {e(web["price"])} site includes</h2><ul class="incs">{inc}</ul></div></section>
<section class="sec price price-s"><div class="price-glow" aria-hidden="true"></div><div class="wrap narrow center">
  <p class="mega" aria-hidden="true"><span class="mega-n">{e(web["price"])}</span></p>
  <h2 class="h2">{e(web["name"])}, {e(web["period"])}</h2><p class="lede">{e(web["body"])}</p>{ctas(cx)}
</div></section>
'''
    return shell(cx, f'{p["business"]} sample website, {p["industry_label"]} (Concept B)', pi["website_intro"], body, "industries.html")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    (OUT / "industries").mkdir()
    for f in ("style.css", "site.js"):
        shutil.copyfile(HERE / f, OUT / "assets" / f)
    out = {"index.html": home(), "crm.html": crm(), "websites.html": websites(), "industries.html": industries()}
    for p in PAIRS:
        out[f'industries/{p["slug"]}-crm.html'] = ind_crm(p)
        out[f'industries/{p["slug"]}-website.html'] = ind_web(p)
    for name, html in out.items():
        assert "—" not in html, f"em dash in {name}"
        (OUT / name).write_text(html, encoding="utf-8", newline="\n")
    print(f"wrote {len(out)} pages to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
