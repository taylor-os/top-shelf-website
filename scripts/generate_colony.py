#!/usr/bin/env python3
"""Colony page generator (plan §5 "Problem/symptom" template + §6 link-sculpting). Colony
pages are easy, in-topic question pages that rank, earn clicks, and funnel that authority
into the money pages via a prominent "the fix" bridge. Lighter than a money page: H1 = one
real question, a 40-60 word AEO answer up top, 2 body sections, the bridge block (the ONE
money page the question implies + the trade hub), a 2-question FAQ, a final CTA. Schema =
FAQPage + BreadcrumbList only (colony pages don't sell one SKU). No sidebar (keeps them
distinct from money pages and light). Reuses generate_corpus.py's shell + GA4 + events.

Topics live in scripts/colony_specs_*.py (each a `TOPICS` list). Run:
  python scripts/generate_colony.py
"""
import os, re, json, sys, io, glob, importlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import generate_corpus as gc  # extract_shell, esc, EVENTS, SITE, _h2

SITE = gc.SITE
esc = gc.esc

def hero(t):
    return f'''<section class="page-hero">
  <div class="container page-hero-inner">
    <span class="eyebrow reveal">{esc(t["hub_name"])} &middot; Common Question</span>
    <h1 class="display display-lg reveal">{esc(t["h1"])}</h1>
    <p class="page-hero-sub reveal">{t["answer"]}</p>
    <div class="page-hero-actions reveal">
      <a href="{t['bridge_slug']}.html" class="btn btn-gold">{esc(t['bridge_label'])} <span class="arr">&rarr;</span></a>
      <a href="tel:+14698333033" class="btn btn-line">Call (469) 833-3033</a>
    </div>
  </div>
</section>'''

def sections(t):
    return "\n".join(f'''<section class="section rule-top">
  <div class="container">
    <h2 class="display reveal" style="margin-bottom:1.3rem">{s["h2_html"]}</h2>
    {s["body_html"]}
  </div>
</section>''' for s in t["sections"])

def bridge(t):
    return f'''<section class="section rule-top">
  <div class="container">
    <div class="reveal" style="border:1px solid var(--gold-deep);border-radius:var(--r-lg);background:var(--surface-2);padding:clamp(1.6rem,4vw,2.6rem);max-width:72ch">
      <span class="eyebrow" style="color:var(--gold)">The fix</span>
      <h2 class="display reveal" style="margin:.7rem 0 1rem">{t["bridge_h2"]}</h2>
      <p style="color:var(--ink-2);line-height:1.85">{t["bridge_text"]}</p>
      <div style="margin-top:1.5rem;display:flex;gap:.8rem;flex-wrap:wrap">
        <a href="{t['bridge_slug']}.html" class="btn btn-gold">{esc(t['bridge_label'])} <span class="arr">&rarr;</span></a>
        <a href="{t['hub_slug']}" class="btn btn-line">All {esc(t['hub_name'])}</a>
      </div>
    </div>
  </div>
</section>'''

def faq(t):
    rows = "\n".join(
        f'''      <div class="qa-row reveal"><span class="qa-num">{i:02d}</span><div><p class="qa-q">{esc(q)}</p><p class="qa-a">{a}</p></div></div>'''
        for i, (q, a) in enumerate(t["faqs"], 1))
    return f'''<section class="section rule-top">
  <div class="container">
    <span class="eyebrow reveal">Related questions</span>
    <h2 class="display reveal" style="margin:1rem 0 1.6rem">More on this</h2>
    <div class="qa-list">
{rows}
    </div>
  </div>
</section>'''

def final_cta(t):
    return f'''<section class="section rule-top">
  <div class="container" style="text-align:center">
    <h2 class="display display-lg reveal">Get a free audit of your business</h2>
    <p class="reveal" style="color:var(--ink-3);max-width:52ch;margin:1rem auto 1.8rem">We will show you exactly where calls, leads, and jobs are slipping away, whether you work with us or not. No credit card, never a call center.</p>
    <div class="reveal" style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap">
      <a href="contact.html" class="btn btn-gold">Get Your Free Audit <span class="arr">&rarr;</span></a>
      <a href="tel:+14698333033" class="btn btn-line">Call (469) 833-3033</a>
    </div>
  </div>
</section>'''

def jsonld(t):
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": t["hub_name"], "item": f"{SITE}/{t['hub_slug']}"},
        {"@type": "ListItem", "position": 3, "name": t["h1"], "item": f"{SITE}/{t['slug']}.html"}]}
    # FAQPage: the page question (H1 answered by the AEO answer) + the 2 supporting FAQs
    qs = [{"@type": "Question", "name": t["h1"], "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", t["answer"])}}]
    qs += [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in t["faqs"]]
    faqp = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qs}
    return "\n".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in (crumb, faqp))

def build_page(t, shell):
    t["meta_desc"] = gc._trim_meta(t["meta_desc"])  # cap SERP snippet at 165 chars (keyword-first tail trim)
    head = re.sub(r"site\.css\?v=[0-9a-z]+", "site.css?v=20260918a", shell["head"])
    head_extra = f'''<title>{esc(t["title"])}</title>
<meta name="description" content="{esc(t["meta_desc"])}">
<link rel="canonical" href="{SITE}/{t["slug"]}.html">
<meta name="robots" content="index,follow">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(t["h1"])}">
<meta property="og:description" content="{esc(t["meta_desc"])}">
<meta property="og:url" content="{SITE}/{t["slug"]}.html">
<meta property="og:image" content="{shell["og_img"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(t["h1"])}">
<meta name="twitter:description" content="{esc(t["meta_desc"])}">
{jsonld(t)}'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{head}
{head_extra}
</head>
<body data-trade="{esc(t.get("trade_slug",""))}">
{shell["nav"]}
<main>
{hero(t)}
{sections(t)}
{bridge(t)}
{faq(t)}
{final_cta(t)}
</main>
{shell["footer"]}
{shell["tail"]}
{gc.EVENTS}
</body>
</html>'''

def load_topics():
    topics = []
    for sf in sorted(glob.glob(os.path.join(ROOT, "scripts", "colony_specs_*.py"))):
        mod = os.path.splitext(os.path.basename(sf))[0]
        try:
            topics += getattr(importlib.import_module(mod), "TOPICS", [])
        except Exception as e:
            print(f"note: {mod} not loaded ({e})")
    return topics

def _selfcheck(topics, shell):
    assert topics, "no colony topics loaded"
    p = build_page(topics[0], shell)
    assert p.count("<h1") == 1
    assert p.count("application/ld+json") == 2, "want BreadcrumbList + FAQPage"
    assert 'rel="canonical"' in p and "og:title" in p
    assert topics[0]["bridge_slug"] + ".html" in p, "bridge link missing"
    words = len(re.sub(r"<[^>]+>", " ", re.search(r"<main>(.*?)</main>", p, re.S).group(1)).split())
    assert words >= 350, f"colony body {words} words (want >=350)"
    print(f"selfcheck OK: 1 h1, 2 schema, bridge present, {words} body words")

if __name__ == "__main__":
    shell = gc.extract_shell()
    topics = load_topics()
    if topics:
        slugs = [t["slug"] for t in topics]
        dup = sorted({s for s in slugs if slugs.count(s) > 1})
        assert not dup, f"duplicate colony slugs (would overwrite each other): {dup}"
        _selfcheck(topics, shell)
        for t in topics:
            open(f"{t['slug']}.html", "w", encoding="utf-8", newline="").write(build_page(t, shell))
        print(f"wrote {len(topics)} colony pages")
    else:
        print("no colony_specs_*.py found yet")
