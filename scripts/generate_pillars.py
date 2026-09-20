#!/usr/bin/env python3
"""Trade PILLAR generator (plan §3 "Trade hubs (pillar)" + §5/§6). One pillar per trade that
already has money pages: the authority sink that aggregates and internally links every one of
that trade's money pages + colony question pages into a single hub, links UP to its industry
umbrella, and is wired to RECEIVE colony/money links (wire_pillars.py). Flat slug matching the
site convention: `for-<trade>.html` (the money pages are `<service>-for-<trade>.html`).

The SPEC (scripts/pillar_specs_<suffix>.py, a single PILLAR dict) owns ONLY the unique per-trade
framing prose (h1/title/meta/answer/sections/faqs/cta). The GENERATOR owns everything mechanical
and everything that must stay correct on its own: the money-page link block and colony-question
link block are AUTO-DISCOVERED from disk (glob the real `<service>-for-<trade>.html` money files +
read that trade's colony_specs), so the link lists can never drift from what actually exists.

Discovery join (proven): each colony_specs_*.py's topics carry a `bridge_slug`
(`<service>-for-<trade>`); the trade TOKEN parsed from it is the authoritative URL slug (the
colony `trade_slug` field is inconsistent — underscores vs hyphens, detailers vs detailing — so
it is NOT used for the join). Money files are filtered to the real money-service prefixes so a
colony page like `is-a-crm-worth-it-for-<trade>.html` never counts as a money page.

Run:  python scripts/generate_pillars.py         # build every trade that has a pillar_specs_*.py
"""
import os, re, json, sys, io, glob, importlib, html as _html
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import generate_corpus as gc  # extract_shell, esc, EVENTS, SITE, _trim_meta

SITE = gc.SITE
esc = gc.esc

# The real money-service prefixes (plan §2b). A `<prefix>-for-<trade>.html` file is a money page
# ONLY when its prefix is one of these — this excludes colony pages such as
# `is-a-crm-worth-it-for-<trade>.html` and `answering-service-cost-for-<trade>.html`.
MONEY_SERVICES = {
    "ai-receptionist", "crm", "marketing", "websites-seo",
    "automation", "online-booking", "review-software", "payments", "memberships", "pos",
}
# NOTE: "best-crm" is deliberately NOT a money service — the 3 best-crm-for-*.html pages
# (landscapers/painters/handyman) are COLONY question pages ("what's the best CRM for X"),
# so they belong in the colony block, not the money block (else the pillar double-links them).
# order money links sensibly (falls back to alpha for anything unknown)
_ORDER = ["ai-receptionist", "crm", "online-booking", "review-software",
          "automation", "websites-seo", "marketing", "payments", "memberships", "pos"]


def _token(slug):
    p = slug.split("-for-", 1)
    return p[1] if len(p) == 2 else None


def _money_title(fname):
    """Exact keyword anchor from the money page's own <title> (drop the brand tail)."""
    try:
        s = open(fname, encoding="utf-8", errors="replace").read()
    except OSError:
        return None
    m = re.search(r"<title>(.*?)</title>", s, re.S)
    t = re.sub(r"\s+", " ", m.group(1)).strip() if m else fname[:-5]
    return re.sub(r"\s*\|\s*Top Shelf Business Solutions\s*$", "", t)


def discover():
    """token -> dict(token, suffix, trade_plural, hub_name, hub_slug, money[(slug,anchor)], colony[(slug,h1)])."""
    out = {}
    for sf in sorted(glob.glob(os.path.join(ROOT, "scripts", "colony_specs_*.py"))):
        suffix = os.path.basename(sf)[len("colony_specs_"):-3]
        if suffix == "category":
            continue
        try:
            topics = getattr(importlib.import_module("colony_specs_" + suffix), "TOPICS", [])
        except Exception as e:
            print(f"note: colony_specs_{suffix} not loaded ({e})"); continue
        if not topics:
            continue
        toks = Counter(_token(t.get("bridge_slug", "")) for t in topics if _token(t.get("bridge_slug", "")))
        token = toks.most_common(1)[0][0]
        colony = [(t["slug"], re.sub(r"<[^>]+>", "", t["h1"])) for t in topics]
        # money pages on disk for this token, real money-service prefixes only
        money = []
        for f in glob.glob(f"*-for-{token}.html"):
            if f.startswith("for-"):
                continue
            svc = f[:-5].split("-for-")[0]
            if svc in MONEY_SERVICES:
                money.append((f[:-5], _money_title(f), svc))
        money.sort(key=lambda x: _ORDER.index(x[2]) if x[2] in _ORDER else 99)
        money = [(s, a) for s, a, _ in money]
        if not money:
            print(f"!! {token}: no money pages found; skipping"); continue
        out[token] = dict(token=token, suffix=suffix, trade_plural=topics[0]["trade_plural"],
                          hub_name=topics[0]["hub_name"], hub_slug=topics[0]["hub_slug"],
                          money=money, colony=colony)
    return out


def hero(p, d):
    return f'''<section class="page-hero">
  <div class="container page-hero-inner">
    <span class="eyebrow reveal">{esc(d["hub_name"])} &middot; For {esc(d["trade_plural"]).title()}</span>
    <h1 class="display display-lg reveal">{esc(p["h1"])}</h1>
    <p class="page-hero-sub reveal">{p["answer"]}</p>
    <div class="page-hero-actions reveal">
      <a href="contact.html" class="btn btn-gold">Get Your Free Audit <span class="arr">&rarr;</span></a>
      <a href="tel:+14698333033" class="btn btn-line">Call (469) 833-3033</a>
    </div>
  </div>
</section>'''


def sections(p):
    return "\n".join(f'''<section class="section rule-top">
  <div class="container">
    <h2 class="display reveal" style="margin-bottom:1.3rem">{s["h2_html"]}</h2>
    {s["body_html"]}
  </div>
</section>''' for s in p["sections"])


def services_block(d):
    items = "\n".join(f'      <li><a href="{slug}.html">{anchor}</a></li>' for slug, anchor in d["money"])
    return f'''<section class="section rule-top">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">What we do</span>
      <h2 class="display display-lg reveal" style="margin-top:1.6rem">Everything Top Shelf does for <em>{esc(d["trade_plural"])}</em></h2>
    </div>
    <ul class="reveal" style="list-style:none;line-height:2.15;font-size:1.06rem;margin-top:1.4rem">
{items}
    </ul>
  </div>
</section>'''


def colony_block(d):
    items = "\n".join(f'      <li><a href="{slug}.html">{esc(h1)}</a></li>' for slug, h1 in d["colony"])
    return f'''<section class="section rule-top">
  <div class="container">
    <span class="eyebrow reveal">Answers</span>
    <h2 class="display reveal" style="margin:1rem 0 1.4rem">Common questions from {esc(d["trade_plural"])}</h2>
    <ul class="reveal" style="list-style:none;line-height:2.05;font-size:1.0rem">
{items}
    </ul>
    <div class="reveal" style="margin-top:1.8rem">
      <a href="{d['hub_slug']}" class="btn btn-line">See all {esc(d['hub_name'])} <span class="arr">&rarr;</span></a>
    </div>
  </div>
</section>'''


def faq(p):
    rows = "\n".join(
        f'''      <div class="qa-row reveal"><span class="qa-num">{i:02d}</span><div><p class="qa-q">{esc(q)}</p><p class="qa-a">{a}</p></div></div>'''
        for i, (q, a) in enumerate(p["faqs"], 1))
    return f'''<section class="section rule-top">
  <div class="container">
    <span class="eyebrow reveal">Questions {esc(p.get("faq_eyebrow", "owners ask"))}</span>
    <h2 class="display reveal" style="margin:1rem 0 1.6rem">Common Questions</h2>
    <div class="qa-list">
{rows}
    </div>
  </div>
</section>'''


def final_cta(p, d):
    h2 = p.get("cta_h2", f"Get a free audit of your {esc(d['trade_plural'])[:-1] if d['trade_plural'].endswith('s') else esc(d['trade_plural'])} business")
    sub = p.get("cta_sub", "We will show you exactly where calls, leads, and jobs are slipping away, whether you work with us or not. No credit card, never a call center.")
    return f'''<section class="section rule-top">
  <div class="container" style="text-align:center">
    <h2 class="display display-lg reveal">{h2}</h2>
    <p class="reveal" style="color:var(--ink-3);max-width:54ch;margin:1rem auto 1.8rem">{esc(sub)}</p>
    <div class="reveal" style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap">
      <a href="contact.html" class="btn btn-gold">Get Your Free Audit <span class="arr">&rarr;</span></a>
      <a href="tel:+14698333033" class="btn btn-line">Call (469) 833-3033</a>
    </div>
  </div>
</section>'''


def jsonld(p, d, slug):
    h1 = re.sub(r"<[^>]+>", "", p["h1"])
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": d["hub_name"], "item": f"{SITE}/{d['hub_slug']}"},
        {"@type": "ListItem", "position": 3, "name": h1, "item": f"{SITE}/{slug}.html"}]}
    service = {"@context": "https://schema.org", "@type": "Service",
               "name": p.get("service_schema_name", f"Business software and marketing for {d['trade_plural']}"),
               "serviceType": p.get("service_schema_name", f"Business software and marketing for {d['trade_plural']}"),
               "description": p["meta_desc"],
               "provider": {"@type": "ProfessionalService", "@id": f"{SITE}/#business", "name": "Top Shelf Business Solutions",
                            "telephone": "+1-469-833-3033", "email": "contact@topshelfsolutions.io", "url": f"{SITE}/"},
               "areaServed": {"@type": "Country", "name": "United States"},
               "audience": {"@type": "Audience", "audienceType": d["trade_plural"]}}
    qs = [{"@type": "Question", "name": h1, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", p["answer"])}}]
    qs += [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in p["faqs"]]
    faqp = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qs}
    items = [(s, a) for s, a in d["money"]] + [(s, _html.unescape(h)) for s, h in d["colony"]]
    itemlist = {"@context": "https://schema.org", "@type": "ItemList",
                "name": p.get("service_schema_name", f"Top Shelf for {d['trade_plural']}"),
                "itemListElement": [{"@type": "ListItem", "position": i, "url": f"{SITE}/{s}.html", "name": _html.unescape(a)}
                                    for i, (s, a) in enumerate(items, 1)]}
    return "\n".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>'
                     for o in (crumb, service, faqp, itemlist))


def build_page(p, d, shell):
    slug = f"for-{d['token']}"
    p["meta_desc"] = gc._trim_meta(p["meta_desc"])
    head = re.sub(r"site\.css\?v=[0-9a-z]+", "site.css?v=20260918a", shell["head"])
    head_extra = f'''<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["meta_desc"])}">
<link rel="canonical" href="{SITE}/{slug}.html">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(re.sub(r'<[^>]+>', '', p["h1"]))}">
<meta property="og:description" content="{esc(p["meta_desc"])}">
<meta property="og:url" content="{SITE}/{slug}.html">
<meta property="og:image" content="{shell["og_img"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(re.sub(r'<[^>]+>', '', p["h1"]))}">
<meta name="twitter:description" content="{esc(p["meta_desc"])}">
{jsonld(p, d, slug)}'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{head}
{head_extra}
</head>
<body data-trade="{esc(d["token"])}">
{shell["nav"]}
<main>
{hero(p, d)}
{sections(p)}
{services_block(d)}
{colony_block(d)}
{faq(p)}
{final_cta(p, d)}
</main>
{shell["footer"]}
{shell["tail"]}
{gc.EVENTS}
</body>
</html>'''


def load_specs():
    specs = {}
    for sf in sorted(glob.glob(os.path.join(ROOT, "scripts", "pillar_specs_*.py"))):
        suffix = os.path.basename(sf)[len("pillar_specs_"):-3]
        try:
            specs[suffix] = getattr(importlib.import_module("pillar_specs_" + suffix), "PILLAR")
        except Exception as e:
            print(f"note: pillar_specs_{suffix} not loaded ({e})")
    return specs


def _check(page, p, d):
    """Return a list of problems (empty = clean). Every pillar is validated, not just the first."""
    probs = []
    if page.count("<h1") != 1:
        probs.append(f"h1 count = {page.count('<h1')} (want 1)")
    if page.count("application/ld+json") != 4:
        probs.append("want 4 schema blocks (BreadcrumbList+Service+FAQPage+ItemList)")
    if not ('rel="canonical"' in page and "og:title" in page and "twitter:card" in page):
        probs.append("missing canonical/og/twitter")
    if "assets/events.js" not in page:
        probs.append("events.js missing")
    for slug, _ in d["money"]:
        if f'href="{slug}.html"' not in page:
            probs.append(f"money link {slug} missing")
    for slug, _ in d["colony"]:
        if f'href="{slug}.html"' not in page:
            probs.append(f"colony link {slug} missing")
    if f'href="{d["hub_slug"]}"' not in page:
        probs.append("hub up-link missing")
    body = re.search(r"<main>(.*?)</main>", page, re.S).group(1)
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    if words < 800:
        probs.append(f"body {words} words (want >=800, plan §5)")
    if re.search(r"[–—]", body):
        probs.append("em/en dash in body (banned)")
    if re.findall(r"\bleak\w*", re.sub(r"<[^>]+>", " ", body).lower()):
        probs.append("'leak' used as a metaphor (banned)")
    return probs, words


if __name__ == "__main__":
    shell = gc.extract_shell()
    disc = discover()
    specs = load_specs()
    if not specs:
        print("no pillar_specs_*.py found yet"); sys.exit(0)
    by_suffix = {d["suffix"]: d for d in disc.values()}
    built, failed = 0, []
    for suffix, p in sorted(specs.items()):
        d = by_suffix.get(suffix)
        if not d:
            print(f"!! pillar_specs_{suffix}: no matching trade in discovery; skip"); failed.append(suffix); continue
        try:
            page = build_page(p, d, shell)
            probs, words = _check(page, p, d)
        except Exception as e:
            print(f"FAIL {suffix}: build error {e}"); failed.append(suffix); continue
        if probs:
            print(f"FAIL for-{d['token']}: " + "; ".join(probs)); failed.append(suffix); continue
        open(f"for-{d['token']}.html", "w", encoding="utf-8", newline="").write(page)
        print(f"  ok for-{d['token']}.html ({len(d['money'])}m+{len(d['colony'])}c links, {words}w)")
        built += 1
    print(f"\nwrote {built} pillar page(s); {len(failed)} failed: {failed}")
    sys.exit(1 if failed else 0)
