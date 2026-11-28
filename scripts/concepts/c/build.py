"""Concept C, "Main Street editorial": builds preview/concepts-2026-11/c/ from the shared content.

Reads renders-src/site-content/content.json, renders-src/industry-crm/pairs.json and
renders-src/industry-crm/captions.json at build time. All copy comes from content.json; the
only words written here are short labels (nav, "A day at", "Sample screens", etc.).
Images that don't exist yet get a placeholder frame; re-run this script once they land.

Run: python scripts/concepts/c/build.py
"""
import html
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(ROOT, "preview", "concepts-2026-11", "c")


def load():
    j = lambda *p: json.load(open(os.path.join(ROOT, *p), encoding="utf-8"))
    return (j("renders-src", "site-content", "content.json"),
            j("renders-src", "industry-crm", "pairs.json"),
            j("renders-src", "industry-crm", "captions.json"))


C, PAIRS, CAPS = load()
B = C["brand"]


def e(s):
    return html.escape(s, quote=True)


def exists(rel):
    return os.path.isfile(os.path.join(ROOT, rel))


# ---------- hand-drawn marks (inline SVG) ----------
CIRCLE = ('<svg class="loop" viewBox="0 0 200 90" preserveAspectRatio="none" aria-hidden="true">'
          '<path pathLength="1" d="M108 6 C 40 2, 4 24, 8 48 C 12 76, 70 88, 120 84 C 170 80, 198 60, 192 36 C 186 12, 140 2, 92 8"/></svg>')
ARROW = ('<svg class="arrow" viewBox="0 0 120 60" aria-hidden="true">'
         '<path pathLength="1" d="M4 10 C 30 50, 70 54, 108 34"/><path class="head" d="M94 26 L110 33 L98 46"/></svg>')


def mark_last(text, n=2):
    """Wrap the last n words of a headline in a hand-drawn underline."""
    text = text.strip()
    punct = text[-1] if text[-1] in ".!?" else ""
    body = text[:-1] if punct else text
    words = body.split(" ")
    head, tail = " ".join(words[:-n]), " ".join(words[-n:])
    return f'{e(head)} <span class="hl">{e(tail)}</span>{e(punct)}'


# ---------- images ----------
def site_shot(p, kind="d"):
    return f"assets/img/websites/{os.path.basename(p['website_dir'])}-home-{kind}.webp"


def placeholder(p, label):
    b = p["brand"]
    return (f'<div class="ph" style="--pc:{b["chrome"]};--pa:{b["accent"]};--pi:{b["ink"]}" role="img" '
            f'aria-label="{e(label)}"><span class="ph-name">{e(p["business"])}</span>'
            f'<span class="ph-note">Screenshot on the way</span></div>')


def img(r, rel, alt, w, h, cls=""):
    """rel is repo-root relative; r is the prefix from this page to the repo root."""
    return (f'<img class="{cls}" src="{r}{rel}" alt="{e(alt)}" width="{w}" height="{h}" '
            f'loading="lazy" decoding="async">')


def website_img(r, p, kind="d"):
    rel = site_shot(p, kind)
    alt = f"Sample website: {p['business']} home page, {'phone' if kind == 'm' else 'desktop'} view"
    if not exists(rel):
        return placeholder(p, alt)
    return img(r, rel, alt, 1200 if kind == "d" else 585, 750 if kind == "d" else 1266)


def screens(slug):
    out = []
    for s in CAPS.get(slug, {}).get("screens", []):
        rel = f"assets/img/crm/industries/{slug}/{s['file']}"
        out.append(dict(s, rel=rel, ok=exists(rel)))
    return out


def screen_img(r, p, s):
    alt = f"Sample CRM screen for {p['business']}: {s['role']}. {s['caption']}"
    if not s["ok"]:
        return placeholder(p, alt)
    phone = s["device"] == "phone"
    return img(r, s["rel"], alt, 585 if phone else 1440, 1266 if phone else 900, "phone" if phone else "desk")


# Laptop C / Phone C, the owner's approved frames (gold hairline).
def laptop(inner, cls=""):
    return f'<div class="laptop {cls}"><div class="lap-screen">{inner}</div><div class="lap-base" aria-hidden="true"></div></div>'


def phone_dev(inner, cls=""):
    return f'<div class="phone {cls}"><div class="phone-body">{inner}</div></div>'


def device(r, p, s, cls=""):
    return (phone_dev if s["device"] == "phone" else laptop)(screen_img(r, p, s), cls)


PAIR_BY_SLUG = {p["slug"]: p for p in PAIRS}


def find_screen(hint, used):
    """Resolve a content.json screen_hint to a real screen: exact match first, then by word."""
    tries = [hint] + sorted(hint.split("-"), key=len, reverse=True)
    for t in tries:
        for p in PAIRS:
            for s in screens(p["slug"]):
                key = (p["slug"], s["file"])
                if s["ok"] and t in s["file"] and key not in used:
                    used.add(key)
                    return p, s
    return None


# ---------- page chrome ----------
NAV = [("crm.html", "The CRM"), ("websites.html", "Websites"), ("industries.html", "Industries")]


def page(path, title, desc, body, current=""):
    depth = path.count("/")
    r = "../" * (depth + 3)          # to repo root
    c = "../" * depth                # to concept root
    nav = "".join(
        f'<a href="{c}{h}"{" aria-current=\"page\"" if h == current else ""}>{e(t)}</a>' for h, t in NAV)
    body = body.replace("{R}", r).replace("{C}", c)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..800;1,9..144,300..800&amp;family=Work+Sans:wght@400;500;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{c}assets/site.css">
<link rel="icon" href="{r}assets/logo-mark.png">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topline">
  <span class="tag">Concept C · design preview</span>
  <span class="topline-r">{e(B['based_in'])} <a href="{B['phone_href']}">{e(B['phone'])}</a></span>
</div>
<header class="mast">
  <a class="brand" href="{c}index.html" aria-label="Top Shelf home">
    <span class="stamp"><img src="{r}assets/logo-mark.png" alt="" width="976" height="976"></span>
    <span class="word"><span class="w1">Top Shelf</span><span class="w2">Business Solutions</span></span>
  </a>
  <nav class="nav" aria-label="Main">{nav}<a class="btn btn-sm" href="{r}{B['cta_primary_href']}">{e(B['cta_primary'])}</a></nav>
</header>
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="foot-in">
    <div class="foot-brand">
      <span class="stamp"><img src="{r}assets/logo-mark.png" alt="" width="976" height="976" loading="lazy"></span>
      <p><strong>{e(B['name'])}</strong><br>{e(B['based_in'])}</p>
    </div>
    <nav aria-label="Footer"><a href="{c}index.html">Home</a>{nav.replace(' aria-current="page"', '')}<a href="{r}{B['cta_primary_href']}">{e(B['cta_primary'])}</a></nav>
    <p class="foot-contact"><a href="{B['phone_href']}">{e(B['phone'])}</a><br><a href="mailto:{B['email']}">{e(B['email'])}</a></p>
  </div>
  <p class="fine">{e(C['sample_note'])}</p>
  <p class="fine">Concept C · design preview, not the live site.</p>
</footer>
</body>
</html>
"""
    dest = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8", newline="\n") as f:
        f.write(doc)


def ctas(note=True):
    n = f'<p class="cta-note">{e(B["cta_primary_note"])}</p>' if note else ""
    return (f'<div class="ctas"><a class="btn" href="{{R}}{B["cta_primary_href"]}">{e(B["cta_primary"])}</a>'
            f'<a class="btn-ghost" href="{B["phone_href"]}">{e(B["cta_secondary"])}</a></div>{n}')


def kicker(t):
    return f'<p class="kicker">{e(t)}</p>'


def steps(items):
    lis = "".join(
        f'<li><span class="num" aria-hidden="true">{e(s["step"])}</span><h3>{e(s["title"])}</h3><p>{e(s["body"])}</p>'
        f'{ARROW if i < len(items) - 1 else ""}</li>' for i, s in enumerate(items))
    return f'<ol class="steps">{lis}</ol>'


def faq(items, cls=""):
    qs = "".join(f'<div class="qa"><h3><span class="q" aria-hidden="true">Q.</span> {e(x["q"])}</h3>'
                 f'<p><span class="a" aria-hidden="true">A.</span> {e(x["a"])}</p></div>' for x in items)
    return f'<div class="faq {cls}">{qs}</div>'


def price_box():
    p = C["pricing"]
    tiers = "".join(
        f'<li><span class="t-users">{e(t["users"])}</span><span class="t-price{"" if t["price"].startswith("$") else " word-price"}">'
        + (f'<span class="circled">{e(t["price"])}{CIRCLE}</span>' if i == 0 else e(t["price"]))
        + f'</span><span class="t-per">{e(t["period"])}</span></li>' for i, t in enumerate(p["plan"]["tiers"]))
    extras = (f'<div class="extras"><p><strong>{e(p["phone_line"]["name"])}</strong> {e(p["phone_line"]["price"])} '
              f'{e(p["phone_line"]["period"])}. {e(p["phone_line"]["body"])}</p>'
              f'<p><strong>{e(p["website"]["name"])}</strong> {e(p["website"]["price"])} {e(p["website"]["period"])}. '
              f'{e(p["website"]["body"])}</p></div>')
    terms = "".join(f"<li>{e(t)}</li>" for t in p["terms"])
    return (f'<div class="classified"><p class="kicker">{e(p["plan"]["name"])}</p>'
            f'<p class="plan-sum">{e(p["plan"]["summary"])}</p><ul class="tiers">{tiers}</ul>'
            f'<ul class="terms">{terms}</ul>{extras}</div>')


def anti_trap():
    a = C["crm"]["anti_trap"]
    items = "".join(f"<li>{e(x)}</li>" for x in a["items"])
    return (f'<div class="antitrap"><h3>{e(a["h"])}</h3><ul class="xlist">{items}</ul>'
            f'<p class="small">{e(a["fine_print"])}</p></div>')


def closing(block):
    return (f'<section class="closing"><div class="wrap"><h2>{mark_last(block["h"], 2)}</h2>'
            f'<p class="lede">{e(block["body"])}</p>'
            + (f'<p class="small">{e(block["note"])}</p>' if block.get("note") else "")
            + ctas(note=False) + '</div></section>')


def poss(name):
    return name + ("'" if name.endswith("s") else "'s")


def pull(headline):
    """Drop the "Industry:" lead-in from an industry headline; the kicker already names it."""
    tail = headline.split(": ", 1)[-1]
    return tail[0].upper() + tail[1:]


def ind(slug):
    return C["industries"]["per_industry"][slug]


def label_sample(t="Sample screens"):
    return f'<span class="label">{e(t)}</span>'


# ---------- home ----------
def build_home():
    h = C["home"]
    s = h["sections"]
    first = PAIRS[0]
    sc = screens(first["slug"])
    desk = next((x for x in sc if x["device"] == "desktop"), None)
    phone = next((x for x in reversed(sc) if x["device"] == "phone"), None)
    proof = "".join(f"<li>{e(x)}</li>" for x in h["proof_points"])
    hero_art = ""
    if desk and phone:
        hero_art = (f'<figure class="hero-art">{label_sample()}'
                    f'{laptop(screen_img("{R}", first, desk))}'
                    f'{phone_dev(screen_img("{R}", first, phone), "over")}'
                    f'<figcaption><em>{e(first["business"])}</em>, {e(desk["role"])}. {e(desk["caption"])}</figcaption></figure>')
    cards = "".join(f'<li><h3>{e(c["title"])}</h3><p>{e(c["body"])}</p></li>' for c in s["crm"]["cards"])
    pairs = []
    for p in PAIRS:
        sc = screens(p["slug"])
        crm = next((x for x in sc if x["device"] == "desktop"), None)
        crm_html = screen_img("{R}", p, crm) if crm else placeholder(p, f"Sample CRM for {p['business']}")
        pairs.append(
            f'<li class="pair"><p class="kicker">{e(p["industry_label"])}</p>'
            f'<h3><a href="{{C}}industries.html#{p["slug"]}">{e(p["business"])}</a></h3>'
            f'<div class="pair-shots"><figure><span class="label">{e(s["pairs"]["card_website_label"])}</span>{laptop(website_img("{R}", p))}</figure>'
            f'<figure><span class="label">{e(s["pairs"]["card_crm_label"])}</span>{laptop(crm_html)}</figure></div>'
            f'<p class="pair-links"><a href="{{C}}industries/{p["slug"]}-website.html">Website</a>'
            f'<a href="{{C}}industries/{p["slug"]}-crm.html">CRM</a></p></li>')
    picks = [x for x in C["crm"]["faq"] if x["q"] in s["faq"]["pick"]]
    body = f"""
<section class="hero"><div class="wrap hero-grid">
  <div class="hero-copy">
    {kicker(h['eyebrow'])}
    <h1>{mark_last(h['h1'], 2)}</h1>
    <p class="lede">{e(h['sub'])}</p>
    {ctas()}
    <ul class="checks">{proof}</ul>
  </div>
  {hero_art}
</div></section>

<section class="band"><div class="wrap split">
  <div class="split-head">{kicker(s['crm']['eyebrow'])}<h2>{e(s['crm']['h'])}</h2><p>{e(s['crm']['body'])}</p>
  <p><a class="more" href="{{C}}crm.html">{e(s['crm']['link_label'])}</a></p></div>
  <ul class="ledger">{cards}</ul>
</div></section>

<section class="pairs-sec" id="pairs"><div class="wrap">
  <div class="sec-head">{kicker(s['pairs']['eyebrow'])}<h2>{mark_last(s['pairs']['h'], 1)}</h2><p class="lede">{e(s['pairs']['body'])}</p></div>
  <ul class="pairs">{''.join(pairs)}</ul>
  <p class="center"><a class="more" href="{{C}}industries.html">All industries, side by side</a></p>
</div></section>

<section class="band alt"><div class="wrap two">
  <div>{kicker(s['websites']['eyebrow'])}<h2>{e(s['websites']['h'])}</h2><p class="lede">{e(s['websites']['body'])}</p>
  <p><a class="more" href="{{C}}websites.html">{e(s['websites']['link_label'])}</a></p></div>
  <div class="aside-box"><h2 class="h3">{e(s['phone']['h'])}</h2><p>{e(s['phone']['body'])}</p></div>
</div></section>

<section class="band" id="pricing"><div class="wrap two price-row">
  <div><h2>{e(s['pricing']['h'])}</h2><p class="lede">{e(s['pricing']['body'])}</p>
  <p class="example">{e(s['pricing']['example'])}</p>{anti_trap()}</div>
  {price_box()}
</div></section>

<section class="band alt"><div class="wrap">
  <div class="sec-head"><h2>{e(s['faq']['h'])}</h2><p class="lede">{e(s['faq']['body'])}</p></div>
  {faq(picks, 'cols')}
  <p><a class="more" href="{{C}}crm.html#faq">More straight answers</a></p>
</div></section>
{closing(s['closing'])}"""
    page("index.html", "Top Shelf CRM · Run the whole business from one app (Concept C)", h["sub"], body, "")


# ---------- CRM ----------
def build_crm():
    m = C["crm"]
    used = set()
    groups = []
    for i, g in enumerate(m["benefit_groups"]):
        fig = ""
        for hint in dict.fromkeys(b["screen_hint"] for b in g["benefits"]):
            hit = find_screen(hint, used)
            if hit:
                p, s = hit
                fig = (f'<figure class="g-fig {"is-phone" if s["device"] == "phone" else ""}">{label_sample("Sample screen")}'
                       f'{device("{R}", p, s)}'
                       f'<figcaption><em>{e(p["business"])}</em>, {e(s["role"])}. {e(s["caption"])}</figcaption></figure>')
                break
        if not fig:  # no screen for this group: show the 12 trades as a contents list
            rows = "".join(f'<li><a href="{{C}}industries/{p["slug"]}-crm.html"><span>{e(p["industry_label"])}</span>'
                           f'<em>{e(p["business"])}</em></a></li>' for p in PAIRS)
            fig = f'<nav class="contents" aria-label="Sample CRMs by industry"><p class="kicker">Sample CRMs by industry</p><ul>{rows}</ul></nav>'
        bens ="".join(f'<li><h4>{e(b["title"])}</h4><p>{e(b["body"])}</p></li>' for b in g["benefits"])
        groups.append(
            f'<article class="feature {"flip" if i % 2 else ""}"><div class="f-copy"><h2>{e(g["title"])}</h2>'
            f'<p class="standfirst">{e(g["intro"])}</p><ul class="bens">{bens}</ul></div>{fig}</article>')
    moments = "".join(f"<li>{e(x)}</li>" for x in m["phone_moments"]["items"])
    day1 = "".join(f"<li>{e(x)}</li>" for x in m["day_one"]["items"])
    body = f"""
<section class="hero slim"><div class="wrap">
  {kicker(m['eyebrow'])}
  <h1>{mark_last(m['h1'], 2)}</h1>
  <p class="lede">{e(m['sub'])}</p>
  {ctas()}
</div></section>
<section class="features"><div class="wrap">{''.join(groups)}</div></section>
<section class="band alt"><div class="wrap two">
  <div><h2>{e(m['phone_moments']['h'])}</h2><ul class="moments">{moments}</ul></div>
  <div class="aside-box"><h2 class="h3">{e(m['day_one']['h'])}</h2><ul class="boxes">{day1}</ul></div>
</div></section>
<section class="band" id="how"><div class="wrap">
  <div class="sec-head"><h2>How it works</h2></div>
  {steps(m['how_it_works'])}
</div></section>
<section class="band alt" id="pricing"><div class="wrap two price-row">
  <div><h2>{e(C['home']['sections']['pricing']['h'])}</h2><p class="lede">{e(C['home']['sections']['pricing']['body'])}</p>{anti_trap()}</div>
  {price_box()}
</div></section>
<section class="band" id="faq"><div class="wrap">
  <div class="sec-head"><h2>{e(C['home']['sections']['faq']['h'])}</h2><p class="lede">{e(C['home']['sections']['faq']['body'])}</p></div>
  {faq(m['faq'], 'cols')}
</div></section>
{closing(m['closing'])}"""
    page("crm.html", "The Top Shelf CRM · everything from one app (Concept C)", m["sub"], body, "crm.html")


# ---------- websites ----------
def build_websites():
    w = C["websites"]
    inc = "".join(f'<li><h3>{e(x["title"])}</h3><p>{e(x["body"])}</p></li>' for x in w["includes"])
    cards = []
    for p in PAIRS:
        cards.append(
            f'<li class="site-card"><figure>{label_sample("Sample website")}{laptop(website_img("{R}", p))}</figure>'
            f'<p class="kicker">{e(p["industry_label"])}</p><h3>{e(p["business"])}</h3>'
            f'<p>{e(ind(p["slug"])["website_intro"])}</p>'
            f'<p class="pair-links"><a href="{{R}}{p["website_dir"]}/index.html">Open the sample site</a>'
            f'<a href="{{C}}industries/{p["slug"]}-crm.html">Its CRM</a></p></li>')
    extra_dir = "websites/linewright-mobile-dent"
    if exists(f"{extra_dir}/index.html"):
        shot = "assets/img/websites/linewright-mobile-dent-home-d.webp"
        im = img("{R}", shot, "Sample website: Linewright Mobile Dent Co. home page", 1200, 900) if exists(shot) else ""
        cards.append(
            f'<li class="site-card"><figure>{label_sample("Sample website")}{laptop(im)}</figure>'
            f'<p class="kicker">Auto</p><h3>Linewright Mobile Dent Co.</h3><p>{e(w["samples"]["extra_note"])}</p>'
            f'<p class="pair-links"><a href="{{R}}{extra_dir}/index.html">Open the sample site</a></p></li>')
    body = f"""
<section class="hero slim"><div class="wrap">
  {kicker(w['eyebrow'])}
  <h1>{mark_last(w['h1'], 2)}</h1>
  <p class="lede">{e(w['sub'])}</p>
  {ctas()}
</div></section>
<section class="band"><div class="wrap split">
  <div class="split-head"><p class="bigprice"><span class="circled">$499{CIRCLE}</span></p>
  <p class="kicker">{e(C['pricing']['website']['period'])}</p><p>{e(C['pricing']['website']['body'])}</p></div>
  <ul class="ledger">{inc}</ul>
</div></section>
<section class="band alt"><div class="wrap">
  <div class="sec-head"><h2>How it works</h2></div>
  {steps(w['how_it_works'])}
</div></section>
<section class="band" id="samples"><div class="wrap">
  <div class="sec-head"><h2>{mark_last(w['samples']['h'], 1)}</h2><p class="lede">{e(w['samples']['body'])}</p></div>
  <ul class="site-cards">{''.join(cards)}</ul>
</div></section>
<section class="band alt"><div class="wrap">
  <div class="sec-head"><h2>{e(C['home']['sections']['faq']['h'])}</h2></div>
  {faq(w['faq'], 'cols')}
</div></section>
{closing(w['closing'])}"""
    page("websites.html", "Websites by Top Shelf · $499 one time (Concept C)", w["sub"], body, "websites.html")


# ---------- industries hub ----------
def build_industries():
    i = C["industries"]
    chips = "".join(f'<li><a href="#{p["slug"]}">{e(p["industry_label"])}</a></li>' for p in PAIRS)
    feats = []
    for n, p in enumerate(PAIRS):
        d = ind(p["slug"])
        sc = screens(p["slug"])
        crm = next((x for x in sc if x["device"] == "desktop"), None)
        crm_html = screen_img("{R}", p, crm) if crm else placeholder(p, f"Sample CRM for {p['business']}")
        gets = "".join(f"<li>{e(x)}</li>" for x in d["what_owners_get"])
        feats.append(f"""
<article class="day {'flip' if n % 2 else ''}" id="{p['slug']}">
  <header class="day-head"><p class="kicker">{e(p['industry_label'])}</p>
  <h2><span class="aday">A day at</span> {e(p['business'])}</h2>
  <p class="pull">{e(pull(d['headline']))}</p></header>
  <div class="spread">
    <figure>{label_sample('Sample website')}{laptop(website_img('{R}', p))}
      <figcaption><a href="{{C}}industries/{p['slug']}-website.html">The website</a></figcaption></figure>
    <figure>{label_sample('Sample CRM')}{laptop(crm_html)}
      <figcaption><a href="{{C}}industries/{p['slug']}-crm.html">The CRM</a></figcaption></figure>
  </div>
  <div class="day-copy"><p>{e(d['crm_intro'])}</p><ul class="checks">{gets}</ul>
  <p class="pair-links"><a href="{{C}}industries/{p['slug']}-crm.html">See {e(poss(p['business']))} CRM</a>
  <a href="{{C}}industries/{p['slug']}-website.html">See its website</a></p></div>
</article>""")
    body = f"""
<section class="hero slim"><div class="wrap">
  <h1>{mark_last(i['h1'], 2)}</h1>
  <p class="lede">{e(i['sub'])}</p>
  <nav class="chips" aria-label="{e(i['picker_label'])}"><p class="kicker">{e(i['picker_label'])}</p><ul>{chips}</ul></nav>
</div></section>
<section class="days"><div class="wrap">{''.join(feats)}</div></section>
<section class="band alt"><div class="wrap narrow"><h2>{e(C['custom']['h'])}</h2><p class="lede">{e(C['custom']['body'])}</p>{ctas(False)}</div></section>"""
    page("industries.html", "Industries · one business, one website, one CRM (Concept C)", i["sub"], body, "industries.html")


def next_link(n):
    q = PAIRS[(n + 1) % len(PAIRS)]
    return (f'<p class="nextup"><span class="kicker">Next</span> '
            f'<a href="{{C}}industries/{q["slug"]}-crm.html">A day at {e(q["business"])}</a></p>')


def build_industry_pages():
    for n, p in enumerate(PAIRS):
        d = ind(p["slug"])
        cap = CAPS.get(p["slug"])
        sc = screens(p["slug"])
        gets = "".join(f"<li>{e(x)}</li>" for x in d["what_owners_get"])
        if sc:
            def fig(s, cls):
                return (f'<figure class="shot {cls}">{device("{R}", p, s)}'
                        f'<figcaption><span class="role">{e(s["role"])}</span> {e(s["caption"])}</figcaption></figure>')
            desks = "".join(fig(s, "is-desk") for s in sc if s["device"] != "phone")
            phones = "".join(fig(s, "is-phone") for s in sc if s["device"] == "phone")
            gallery = (f'<div class="gallery-head">{label_sample()}</div><div class="g-desks">{desks}</div>'
                       f'<div class="g-phones">{phones}</div>')
        else:
            gallery = (f'<div class="gallery-head">{label_sample()}</div><div class="pending">'
                       f'{placeholder(p, "Sample CRM screens for " + p["business"])}'
                       f'<p>The sample screens for {e(p["business"])} are on the way.</p></div>')
        built = f'<p class="standfirst">{e(cap["built_around"])}</p>' if cap else ""
        body = f"""
<section class="hero slim ind"><div class="wrap">
  <p class="crumbs"><a href="{{C}}industries.html">Industries</a> / {e(p['industry_label'])}</p>
  <p class="kicker">{e(p['industry_label'])} · Sample CRM</p>
  <h1><span class="aday">A day at</span> <span class="hl">{e(p['business'])}</span></h1>
  <p class="pull">{e(pull(d['headline']))}</p>
  <div class="two"><p class="lede">{e(d['crm_intro'])}</p>{built}</div>
</div></section>
<section class="band"><div class="wrap">{gallery}</div></section>
<section class="band alt"><div class="wrap two">
  <div><h2>What owners get</h2><ul class="checks">{gets}</ul>{ctas()}</div>
  <a class="pairbox" href="{{C}}industries/{p['slug']}-website.html">
    <span class="kicker">The same business</span><span class="h3">{e(poss(p['business']))} website</span>
    <div class="pb-img">{laptop(website_img('{R}', p))}</div><span class="more">See the website</span></a>
</div></section>
<section class="band"><div class="wrap">{next_link(n)}</div></section>"""
        page(f"industries/{p['slug']}-crm.html", f"A day at {p['business']} · sample CRM (Concept C)",
             d["crm_intro"], body, "industries.html")

        inc = "".join(f'<li><h3>{e(x["title"])}</h3><p>{e(x["body"])}</p></li>' for x in C["websites"]["includes"])
        first_crm = next((s for s in sc if s["device"] == "desktop"), None)
        crm_tile = screen_img("{R}", p, first_crm) if first_crm else placeholder(p, f"Sample CRM for {p['business']}")
        body = f"""
<section class="hero slim ind"><div class="wrap">
  <p class="crumbs"><a href="{{C}}industries.html">Industries</a> / {e(p['industry_label'])}</p>
  <p class="kicker">{e(p['industry_label'])} · Sample website</p>
  <h1><span class="hl">{e(p['business'])}</span>, on the web</h1>
  <p class="lede">{e(d['website_intro'])}</p>
  <p class="pair-links"><a href="{{R}}{p['website_dir']}/index.html">Open the live sample site</a></p>
</div></section>
<section class="band"><div class="wrap site-spread">
  <figure class="wide">{label_sample('Sample website')}{laptop(website_img('{R}', p, 'd'))}</figure>
  <figure class="narrowfig">{label_sample('Sample website')}{phone_dev(website_img('{R}', p, 'm'))}</figure>
</div></section>
<section class="band alt"><div class="wrap split">
  <div class="split-head"><p class="bigprice"><span class="circled">$499{CIRCLE}</span></p>
  <p class="kicker">{e(C['pricing']['website']['period'])}</p><h2>What the $499 site includes</h2></div>
  <ul class="ledger">{inc}</ul>
</div></section>
<section class="band"><div class="wrap two">
  <div><h2>{e(C['home']['sections']['websites']['h'])}</h2><p class="lede">{e(C['home']['sections']['websites']['body'])}</p>{ctas()}</div>
  <a class="pairbox" href="{{C}}industries/{p['slug']}-crm.html">
    <span class="kicker">The same business</span><span class="h3">{e(poss(p['business']))} CRM</span>
    <div class="pb-img">{laptop(crm_tile)}</div><span class="more">See the CRM</span></a>
</div></section>"""
        page(f"industries/{p['slug']}-website.html", f"{p['business']} · sample website (Concept C)",
             d["website_intro"], body, "industries.html")


def main():
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "site.css"), os.path.join(OUT, "assets", "site.css"))
    build_home()
    build_crm()
    build_websites()
    build_industries()
    build_industry_pages()
    missing = sorted({site_shot(p) for p in PAIRS if not exists(site_shot(p))}
                     | {f"screens: {p['slug']}" for p in PAIRS if p["slug"] not in CAPS})
    print(f"built {sum(len(f) for _, _, f in os.walk(OUT) if f) } files in {OUT}")
    if missing:
        print("placeholders for (re-run when they exist):", ", ".join(missing))


if __name__ == "__main__":
    main()
