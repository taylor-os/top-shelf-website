#!/usr/bin/env python3
"""Comparison / alternative pages (plan §5 "Comparison /vs/" + §3 comparison block). Bottom-of-
funnel pages that catch people choosing between Top Shelf and an incumbent tool (or an old model)
and funnel that intent into the solution / pricing / money pages. Two kinds:
  brand    -> `<brand>-alternative.html`, e.g. jobber-alternative (honest, fair, non-disparaging)
  category -> a model comparison, e.g. ai-receptionist-vs-answering-service

The SPEC (scripts/vs_specs_<slug>.py, a single PAGE dict) owns the unique, honest comparison prose.
The generator owns shell, schema, keyword placement, the bridge to pricing/solution, and (for a
brand page) an auto-appended HONESTY disclaimer: comparisons reflect public info as of publication,
and Top Shelf is not affiliated with or endorsed by the named company. Same honesty rules as every
other spec: only real Top Shelf prices ($299/$899/$2,500/$1,500), no fabricated competitor prices
or features (state a competitor spec only if publicly verifiable and hedged), no disparagement,
no em/en dashes, no "leak" metaphor.

Run:  python scripts/generate_vs.py
"""
import os, re, json, sys, glob, importlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import generate_corpus as gc
SITE, esc = gc.SITE, gc.esc
HUB_NAME, HUB_SLUG = "Alternatives", "alternatives.html"


def hero(p):
    eyebrow = "Comparison" if p.get("competitor") is None else f'{esc(p["competitor"])} alternative'
    return f'''<section class="page-hero">
  <div class="container page-hero-inner">
    <span class="eyebrow reveal">{eyebrow}</span>
    <h1 class="display display-lg reveal">{esc(p["h1"])}</h1>
    <p class="page-hero-sub reveal">{p["answer"]}</p>
    <div class="page-hero-actions reveal">
      <a href="contact.html" class="btn btn-gold">Get a Free Audit <span class="arr">&rarr;</span></a>
      <a href="pricing.html" class="btn btn-line">See What Top Shelf Includes</a>
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


def bridge(p):
    return f'''<section class="section rule-top">
  <div class="container">
    <div class="reveal" style="border:1px solid var(--gold-deep);border-radius:var(--r-lg);background:var(--surface-2);padding:clamp(1.6rem,4vw,2.6rem);max-width:72ch">
      <span class="eyebrow" style="color:var(--gold)">What Top Shelf is</span>
      <h2 class="display reveal" style="margin:.7rem 0 1rem">{p["bridge_h2"]}</h2>
      <p style="color:var(--ink-2);line-height:1.85">{p["bridge_text"]}</p>
      <div style="margin-top:1.5rem;display:flex;gap:.8rem;flex-wrap:wrap">
        <a href="{p.get('bridge_slug','pricing')}.html" class="btn btn-gold">{esc(p.get('bridge_label','See what Top Shelf includes'))} <span class="arr">&rarr;</span></a>
        <a href="contact.html" class="btn btn-line">Get a free audit</a>
      </div>
    </div>
  </div>
</section>'''


def faq(p):
    rows = "\n".join(
        f'''      <div class="qa-row reveal"><span class="qa-num">{i:02d}</span><div><p class="qa-q">{esc(q)}</p><p class="qa-a">{a}</p></div></div>'''
        for i, (q, a) in enumerate(p["faqs"], 1))
    return f'''<section class="section rule-top">
  <div class="container">
    <span class="eyebrow reveal">Common questions</span>
    <h2 class="display reveal" style="margin:1rem 0 1.6rem">More on this</h2>
    <div class="qa-list">
{rows}
    </div>
  </div>
</section>'''


def disclaimer(p):
    if p.get("competitor") is None:
        return ""
    c = esc(p["competitor"])
    return f'''<section class="section rule-top">
  <div class="container">
    <p class="reveal" style="color:var(--ink-4);font-size:.82rem;line-height:1.7;max-width:72ch">Comparison based on publicly available information as of publication; {c} may have changed its plans or features since, so check {c}'s own site for current details. {c} is a trademark of its owner. Top Shelf Business Solutions is independent and is not affiliated with, endorsed by, or sponsored by {c}.</p>
  </div>
</section>'''


def final_cta(p):
    h2 = p.get("cta_h2", "See what an all-in-one, done-for-you setup looks like")
    sub = p.get("cta_sub", "Get a free audit of where calls, leads, and jobs are slipping away, whether you work with us or not. No credit card, never a call center.")
    return f'''<section class="section rule-top">
  <div class="container" style="text-align:center">
    <h2 class="display display-lg reveal">{h2}</h2>
    <p class="reveal" style="color:var(--ink-3);max-width:54ch;margin:1rem auto 1.8rem">{esc(sub)}</p>
    <div class="reveal" style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap">
      <a href="contact.html" class="btn btn-gold">Get Your Free Audit <span class="arr">&rarr;</span></a>
      <a href="pricing.html" class="btn btn-line">See Pricing</a>
    </div>
  </div>
</section>'''


def jsonld(p):
    h1 = re.sub(r"<[^>]+>", "", p["h1"])
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": HUB_NAME, "item": f"{SITE}/{HUB_SLUG}"},
        {"@type": "ListItem", "position": 3, "name": h1, "item": f"{SITE}/{p['slug']}.html"}]}
    qs = [{"@type": "Question", "name": h1, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", p["answer"])}}]
    qs += [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in p["faqs"]]
    faqp = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qs}
    return "\n".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in (crumb, faqp))


def build_page(p, shell):
    p["meta_desc"] = gc._trim_meta(p["meta_desc"])
    head = re.sub(r"site\.css\?v=[0-9a-z]+", "site.css?v=20260918a", shell["head"])
    head_extra = f'''<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["meta_desc"])}">
<link rel="canonical" href="{SITE}/{p["slug"]}.html">
<meta name="robots" content="index,follow">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(re.sub(r"<[^>]+>", "", p["h1"]))}">
<meta property="og:description" content="{esc(p["meta_desc"])}">
<meta property="og:url" content="{SITE}/{p["slug"]}.html">
<meta property="og:image" content="{shell["og_img"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(re.sub(r"<[^>]+>", "", p["h1"]))}">
<meta name="twitter:description" content="{esc(p["meta_desc"])}">
{jsonld(p)}'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{head}
{head_extra}
</head>
<body data-trade="">
{shell["nav"]}
<main>
{hero(p)}
{sections(p)}
{bridge(p)}
{faq(p)}
{disclaimer(p)}
{final_cta(p)}
</main>
{shell["footer"]}
{shell["tail"]}
{gc.EVENTS}
</body>
</html>'''


EXISTING_VS = [("switching-from-hibu-thryv", "Switching from Hibu or Thryv", True),
               ("marketing-agency-vs-software-small-business", "A marketing agency vs software", False)]


def build_hub(specs, shell):
    """alternatives.html: lists every comparison page (brand + approach) + the 2 pre-existing ones."""
    brands = sorted([p for p in specs.values() if p.get("competitor")], key=lambda p: p["competitor"].lower())
    cats = sorted([p for p in specs.values() if not p.get("competitor")], key=lambda p: re.sub(r"<[^>]+>", "", p["h1"]).lower())
    def li(slug, label): return f'          <li><a href="{slug}.html">{esc(label)}</a></li>'
    b_items = "\n".join(li(p["slug"], f'Top Shelf vs {p["competitor"]}') for p in brands)
    b_items += "\n" + "\n".join(li(s, l) for s, l, is_brand in EXISTING_VS if is_brand)
    c_items = "\n".join(li(p["slug"], re.sub(r"<[^>]+>", "", p["h1"])) for p in cats)
    c_items += "\n" + "\n".join(li(s, l) for s, l, is_brand in EXISTING_VS if not is_brand)
    itemrows = [(p["slug"], f'Top Shelf vs {p["competitor"]}') for p in brands] + \
               [(p["slug"], re.sub(r"<[^>]+>", "", p["h1"])) for p in cats] + \
               [(s, l) for s, l, _ in EXISTING_VS]
    head = re.sub(r"site\.css\?v=[0-9a-z]+", "site.css?v=20260918a", shell["head"])
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "Alternatives", "item": f"{SITE}/alternatives.html"}]}
    coll = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Top Shelf Alternatives and Comparisons",
            "description": "Honest comparisons of Top Shelf to popular tools and to the older ways of doing things.",
            "url": f"{SITE}/alternatives.html",
            "mainEntity": {"@type": "ItemList", "itemListElement": [
                {"@type": "ListItem", "position": i, "url": f"{SITE}/{s}.html", "name": l} for i, (s, l) in enumerate(itemrows, 1)]}}
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in (crumb, coll))
    meta = gc._trim_meta("Honest, fair comparisons of Top Shelf to popular tools like Jobber, Podium, GoHighLevel, and more, and to the older ways of running a local business.")
    head_extra = f'''<title>Top Shelf Alternatives &amp; Comparisons | Top Shelf Business Solutions</title>
<meta name="description" content="{esc(meta)}">
<link rel="canonical" href="{SITE}/alternatives.html">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website">
<meta property="og:title" content="Top Shelf Alternatives &amp; Comparisons">
<meta property="og:description" content="{esc(meta)}">
<meta property="og:url" content="{SITE}/alternatives.html">
<meta property="og:image" content="{shell["og_img"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Top Shelf Alternatives &amp; Comparisons">
<meta name="twitter:description" content="{esc(meta)}">
{ld}'''
    body = f'''<section class="page-hero">
  <div class="container page-hero-inner">
    <span class="eyebrow reveal">Alternatives</span>
    <h1 class="display display-lg reveal">Top Shelf Alternatives &amp; <em>Comparisons</em></h1>
    <p class="page-hero-sub reveal">Thinking about a specific tool, or the old way of doing things? Here are honest, side by side looks at how an all-in-one, done-for-you platform compares. We say what each option is good at, then where Top Shelf fits.</p>
    <div class="page-hero-actions reveal">
      <a href="contact.html" class="btn btn-gold">Get a Free Audit <span class="arr">&rarr;</span></a>
      <a href="pricing.html" class="btn btn-line">See What Top Shelf Includes</a>
    </div>
  </div>
</section>
<section class="section rule-top">
  <div class="container">
    <div class="section-head"><span class="eyebrow reveal">Vs a specific tool</span><h2 class="display reveal" style="margin-top:1rem">Compared to popular tools</h2></div>
    <ul class="reveal" style="list-style:none;line-height:2.1;font-size:1.02rem;margin-top:1.4rem;columns:2;column-gap:3rem">
{b_items}
    </ul>
  </div>
</section>
<section class="section rule-top">
  <div class="container">
    <div class="section-head"><span class="eyebrow reveal">Vs the old way</span><h2 class="display reveal" style="margin-top:1rem">Compared by approach</h2></div>
    <ul class="reveal" style="list-style:none;line-height:2.1;font-size:1.02rem;margin-top:1.4rem">
{c_items}
    </ul>
  </div>
</section>'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{head}
{head_extra}
</head>
<body data-trade="">
{shell["nav"]}
<main>
{body}
</main>
{shell["footer"]}
{shell["tail"]}
{gc.EVENTS}
</body>
</html>'''


def load_specs():
    # file names use underscores (valid module names); PAGE["slug"] carries the real hyphenated URL slug
    specs = {}
    for sf in sorted(glob.glob(os.path.join(ROOT, "scripts", "vs_specs_*.py"))):
        mod = os.path.splitext(os.path.basename(sf))[0]
        try:
            p = getattr(importlib.import_module(mod), "PAGE")
            specs[p["slug"]] = p
        except Exception as e:
            print(f"note: {mod} not loaded ({e})")
    return specs


def _check(page, p):
    probs = []
    if page.count("<h1") != 1: probs.append(f"h1={page.count('<h1')}")
    if page.count("application/ld+json") != 2: probs.append("want 2 schema (BreadcrumbList+FAQPage)")
    if not ('rel="canonical"' in page and "og:title" in page): probs.append("missing canonical/og")
    if "assets/events.js" not in page: probs.append("events.js missing")
    body = re.search(r"<main>(.*?)</main>", page, re.S).group(1)
    txt = re.sub(r"<[^>]+>", " ", body)
    if re.search(r"[–—]", body): probs.append("em/en dash")
    if re.findall(r"\bleak\w*", txt.lower()): probs.append("'leak' metaphor")
    words = len(txt.split())
    if words < 450: probs.append(f"body {words}w (<450)")
    # real Top Shelf prices only: any $NNN that is not one of the sanctioned must be flagged for review
    prices = set(re.findall(r"\$[\d,]*\d", txt))  # end on a digit so a trailing comma/period isn't captured
    ok = {"$299", "$899", "$2,500", "$1,500"}
    stray = prices - ok
    return probs, words, stray


if __name__ == "__main__":
    shell = gc.extract_shell()
    specs = load_specs()
    if not specs:
        print("no vs_specs_*.py found yet"); sys.exit(0)
    built, failed = 0, []
    for slug, p in sorted(specs.items()):
        try:
            page = build_page(p, shell)
            probs, words, stray = _check(page, p)
        except Exception as e:
            print(f"FAIL {slug}: {e}"); failed.append(slug); continue
        if probs:
            print(f"FAIL {slug}: " + "; ".join(probs)); failed.append(slug); continue
        open(f"{slug}.html", "w", encoding="utf-8", newline="").write(page)
        note = f"  (review stray $: {sorted(stray)})" if stray else ""
        print(f"  ok {slug}.html ({words}w){note}")
        built += 1
    if specs:
        open("alternatives.html", "w", encoding="utf-8", newline="").write(build_hub(specs, shell))
        print("wrote alternatives.html (hub)")
    print(f"\nwrote {built} vs page(s); {len(failed)} failed: {failed}")
    sys.exit(1 if failed else 0)
