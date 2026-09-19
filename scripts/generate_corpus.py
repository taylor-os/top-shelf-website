#!/usr/bin/env python3
"""Corpus page generator (plan §5/§10). Clone-and-fill: reuses the REAL site shell (head
boilerplate incl. GA4 + CSS, nav, footer, animation scripts) from a base page, and fills in
the per-page content from a spec. The generator owns the mechanics that must be uniform across
every page — GA4, the lead/call/book conversion events (§12), schema, breadcrumb, interlinks,
keyword-first title/slug/H1/first-sentence. The SPEC owns the unique per-trade substance that
makes the page non-thin (the anti-doorway requirement, §5/§7).

It does NOT invent content. Each spec is written per page (by a human/LLM) with real per-trade
workflow, dollar value, objections. Generated pages still run the full gate stack afterwards
(dupe_audit → factcheck → humanizer → seo_audit → Judge) before publish.

Run:  python scripts/generate_corpus.py           # build every spec below + self-check
"""
import os, re, json, sys, io, html as _html
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SITE = "https://www.topshelfsolutions.io"
BASE_PAGE = "solution-crm.html"   # a clean solution page = the money-page shell donor

# ---------- shell extraction (reuse the real design) ----------
def extract_shell(base_page=BASE_PAGE):
    s = open(base_page, encoding="utf-8", errors="replace").read()
    head = re.search(r"<head\b[^>]*>(.*?)</head>", s, re.S | re.I).group(1)
    og_img = (re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', head, re.I) or [None, f"{SITE}/assets/logo-full.png"])[1]
    # strip per-page tags from the head; keep charset/viewport/GA4/fonts/preconnect/style/favicon
    for pat in [r"<title>.*?</title>",
                r'<meta[^>]+name="description"[^>]*>',
                r'<link[^>]+rel="canonical"[^>]*>',
                r'<meta[^>]+property="og:[^"]*"[^>]*>',
                r'<meta[^>]+name="twitter:[^"]*"[^>]*>',
                r'<meta[^>]+name="robots"[^>]*>',
                r'<script type="application/ld\+json">.*?</script>']:
        head = re.sub(pat, "", head, flags=re.S | re.I)
    head = re.sub(r"\n\s*\n+", "\n", head).strip()
    nav = re.search(r"<nav\b.*?</nav>", s, re.S | re.I).group()
    footer = re.search(r"<footer\b.*?</footer>", s, re.S | re.I).group()
    tail = re.search(r"</footer>(.*?)</body>", s, re.S | re.I).group(1)  # reveal/animation scripts
    tail = re.sub(r'<script src="assets/events\.js[^"]*"[^>]*></script>\s*', "", tail)  # events.js is added once via EVENTS
    return {"head": head, "nav": nav, "footer": footer, "tail": tail, "og_img": og_img}

def esc(t):
    return _html.escape(t, quote=True)

def _trim_meta(s, limit=165):
    """Cap a meta description at ~165 chars so Google does not truncate it. Metas are
    keyword-first, so we trim the tail: prefer a sentence end, else the last word boundary."""
    s = " ".join(s.split())
    if len(s) <= limit:
        return s
    cut = s[:limit + 1]
    dot = max(cut.rfind(". "), cut.rfind("! "), cut.rfind("? "))
    if dot >= 80:
        return cut[:dot + 1].strip()
    sp = cut[:limit].rfind(" ")
    return (cut[:sp].rstrip(" ,;:") if sp >= 80 else cut[:limit]).strip()

# ---------- content-block builders (site CSS classes) ----------
def hero(spec):
    return f'''<section class="page-hero">
  <div class="container page-hero-inner">
    <span class="eyebrow reveal">{esc(spec["eyebrow"])}</span>
    <h1 class="display display-lg reveal">{spec["h1_html"]}</h1>
    <p class="page-hero-sub reveal">{spec["answer_block"]}</p>
    <div class="page-hero-actions reveal">
      <a href="contact.html" class="btn btn-gold">Get Your Free Audit <span class="arr">&rarr;</span></a>
      <a href="tel:+14698333033" class="btn btn-line">Call (469) 833-3033</a>
    </div>
  </div>
</section>'''

def _slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", text).lower()).strip("-")[:40] or "section"

def _toc_label(h2_html):
    t = re.sub(r"<[^>]+>", "", h2_html).strip()
    w = t.split()
    return " ".join(w[:6]) + ("..." if len(w) > 6 else "")

def _block(inner, sid, first=False):
    style = "" if first else ' style="padding-top:clamp(2rem,4.5vw,3.4rem);margin-top:clamp(2rem,4.5vw,3.4rem);border-top:1px solid var(--hairline-soft)"'
    return f'<div class="corpus-block" id="{sid}"{style}>\n{inner}\n</div>'

def _h2(h):
    return f'<h2 class="display reveal" style="margin-bottom:1.3rem">{h}</h2>'

def demo_inner():
    return f'''<span class="eyebrow reveal">See it in action</span>
{_h2("Watch it handle <em>a live call</em>")}
<div class="demo-frame reveal">
  <iframe src="https://crm.topshelfsolutions.io/e/ai-phone" title="AI receptionist live demo" loading="lazy" scrolling="no"></iframe>
</div>
<p class="demo-cap">A live demo of the AI receptionist taking a call. It is a sample, not a recording of a real customer.</p>'''

def example_inner(spec):
    ex = spec["example"]
    # dedupe: some specs end body with the disclaimer, and we append our own below — strip theirs
    body = re.sub(r"\s*(<[^>]+>\s*)?Illustrative example,?\s*not a client\.?\s*(</[^>]+>\s*)?$", "", ex["body_html"], flags=re.I).rstrip()
    return f'''<span class="eyebrow reveal">{esc(ex["eyebrow"])}</span>
{_h2(ex["h2_html"])}
<div class="reveal" style="border:1px solid var(--hairline);border-radius:var(--r-lg);background:var(--surface);padding:clamp(1.4rem,3vw,2.2rem);max-width:64ch">
  <p style="color:var(--ink-2);line-height:1.8">{body}</p>
  <p style="color:var(--ink-4);font-size:.82rem;letter-spacing:.02em;margin-top:1rem">Illustrative example, not a client.</p>
</div>'''

def faq_inner(spec):
    rows = "\n".join(
        f'''      <div class="qa-row reveal"><span class="qa-num">{i:02d}</span><div><p class="qa-q">{esc(q)}</p><p class="qa-a">{a}</p></div></div>'''
        for i, (q, a) in enumerate(spec["faqs"], 1))
    return f'''<span class="eyebrow reveal">Questions {esc(spec["trade_plural"]).title()} Ask</span>
{_h2("Common Questions")}
<div class="qa-list">
{rows}
</div>'''

def build_main(spec):
    """corpus-main column: sections, an optional moving demo, example, FAQ. Returns (html, toc)."""
    blocks, toc, first = [], [], True
    for i, s in enumerate(spec["sections"], 1):
        sid = f"s{i}-{_slugify(s['h2_html'])}"[:48]
        blocks.append(_block(_h2(s["h2_html"]) + s["body_html"], sid, first)); first = False
        toc.append((sid, _toc_label(s["h2_html"])))
        if i == 1 and spec.get("demo"):
            blocks.append(_block(demo_inner(), "see-it")); toc.append(("see-it", "See it in action"))
    blocks.append(_block(example_inner(spec), "example")); toc.append(("example", _toc_label(spec["example"]["h2_html"])))
    blocks.append(_block(faq_inner(spec), "faq")); toc.append(("faq", "Common questions"))
    return "\n".join(blocks), toc

def build_aside(spec, toc):
    toc_links = "\n".join(f'      <a href="#{sid}">{esc(label)}</a>' for sid, label in toc)
    return f'''<aside class="corpus-aside">
  <div class="aside-card aside-answer reveal">
    <h3>The short version</h3>
    <p>{spec["answer_block"]}</p>
  </div>
  <div class="aside-card aside-toc reveal">
    <h3>On this page</h3>
{toc_links}
  </div>
  <div class="aside-card aside-cta reveal">
    <h3>Free business audit</h3>
    <p>See what your current setup is missing, whether you work with us or not.</p>
    <a href="contact.html" class="btn btn-gold btn-sm">Get Your Free Audit <span class="arr">&rarr;</span></a>
    <a href="tel:+14698333033" class="btn btn-line btn-sm">Call (469) 833-3033</a>
    <a href="booking.html" class="btn btn-line btn-sm">Book a 15-minute call</a>
  </div>
</aside>'''

def related_block(spec):
    links = "\n".join(f'      <li><a href="{href}">{esc(txt)}</a></li>' for href, txt in spec["related"])
    return f'''<section class="section rule-top">
  <div class="container">
    <h2 class="display reveal" style="margin-bottom:1.2rem">Related for {esc(spec["trade_plural"]).title()}</h2>
    <ul class="reveal" style="line-height:2.1;font-size:1.02rem">
{links}
    </ul>
  </div>
</section>'''

def final_cta(spec):
    return f'''<section class="section rule-top">
  <div class="container" style="text-align:center">
    <h2 class="display display-lg reveal">{spec["cta_h2_html"]}</h2>
    <p class="reveal" style="color:var(--ink-3);max-width:52ch;margin:1rem auto 1.8rem">{esc(spec["cta_sub"])}</p>
    <div class="reveal" style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap">
      <a href="contact.html" class="btn btn-gold">Get Your Free Audit <span class="arr">&rarr;</span></a>
      <a href="tel:+14698333033" class="btn btn-line">Call (469) 833-3033</a>
    </div>
  </div>
</section>'''

# ---------- schema ----------
def jsonld(spec):
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": spec["hub_name"], "item": f"{SITE}/{spec['hub_slug']}"},
        {"@type": "ListItem", "position": 3, "name": spec["breadcrumb_leaf"], "item": f"{SITE}/{spec['slug']}.html"}]}
    service = {"@context": "https://schema.org", "@type": "Service", "name": spec["service_schema_name"],
               "serviceType": spec["service_schema_name"], "description": spec["meta_desc"],
               "provider": {"@type": "ProfessionalService", "@id": f"{SITE}/#business", "name": "Top Shelf Business Solutions",
                            "telephone": "+1-469-833-3033", "email": "contact@topshelfsolutions.io", "url": f"{SITE}/"},
               "areaServed": {"@type": "Country", "name": "United States"},
               "audience": {"@type": "Audience", "audienceType": spec["trade_plural"]}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
        for q, a in spec["faqs"]]}
    return "\n".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in (crumb, service, faq))

# ---------- events (§12 conversions) — shared script, one source of truth ----------
EVENTS = '<script src="assets/events.js?v=1" defer></script>'

# ---------- assemble ----------
def build_page(spec, shell=None):
    shell = shell or extract_shell()
    spec["meta_desc"] = _trim_meta(spec["meta_desc"])  # cap SERP snippet; keyword-first, so trim the tail
    head = re.sub(r"site\.css\?v=[0-9a-z]+", "site.css?v=20260918a", shell["head"])  # bump so pages get the sidebar CSS
    main_html, toc = build_main(spec)
    head_extra = f'''<title>{esc(spec["title"])}</title>
<meta name="description" content="{esc(spec["meta_desc"])}">
<link rel="canonical" href="{SITE}/{spec["slug"]}.html">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(spec["og_title"])}">
<meta property="og:description" content="{esc(spec["meta_desc"])}">
<meta property="og:url" content="{SITE}/{spec["slug"]}.html">
<meta property="og:image" content="{shell["og_img"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(spec["og_title"])}">
<meta name="twitter:description" content="{esc(spec["meta_desc"])}">
{jsonld(spec)}'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{head}
{head_extra}
</head>
<body data-trade="{esc(spec["trade_slug"])}">
{shell["nav"]}
<main>
{hero(spec)}
<section class="section rule-top">
  <div class="container">
    <div class="corpus-grid">
      <div class="corpus-main">
{main_html}
      </div>
{build_aside(spec, toc)}
    </div>
  </div>
</section>
{related_block(spec)}
{final_cta(spec)}
</main>
{shell["footer"]}
{shell["tail"]}
{EVENTS}
</body>
</html>'''

# ================= SPECS (unique per-trade content, written per page) =================
SPECS = [{
    "slug": "ai-receptionist-for-real-estate-agents", "demo": True,
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "breadcrumb_leaf": "AI Receptionist for Real Estate Agents",
    "title": "AI Receptionist for Real Estate Agents | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Real Estate Agents",
    "meta_desc": "An AI receptionist for real estate agents answers every buyer and seller call, qualifies the lead, and books the showing while you are with a client.",
    "service_schema_name": "AI Receptionist for Real Estate Agents",
    "eyebrow": "For Real Estate Agents",
    "h1_html": "AI Receptionist <em>for Real Estate Agents</em>",
    "answer_block": "An AI receptionist for real estate agents answers every call the moment it comes in, day or night, qualifies the buyer or seller, and books the showing or consult straight onto your calendar while you are in a closing or another showing. You keep your own number, and every lead is yours.",
    "sections": [
        {"h2_html": "The call you miss is the client who <em>hires the next agent</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Real estate runs on speed. A buyer scrolls three listings, calls all three agents, and lists with whoever picks up first. But you are in a showing, at a closing table, or driving with a client in the car, so the call rolls to voicemail and most people never leave one. That is not a small miss. In real estate a single missed call can be a buy-side or listing commission, and it walks straight to the agent who answered.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An AI receptionist closes that gap. It answers on the first ring, sounds calm and professional, finds out whether the caller is buying or selling, which property or area, and their timeline, then books a showing or a listing consult on your calendar and texts you the details before you are out of your meeting. The lead is captured and scheduled instead of lost.</p>'},
        {"h2_html": "Built around how <em>agents actually work</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your day is not a desk with a phone on it. You are mobile, you work nights and weekends because that is when buyers tour, and the leads that matter most often come in after hours from a yard sign or a listing portal. A voicemail box does not qualify anyone, and a call center reading a script does not know a pre-approval from a pocket listing.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers 24/7, including the Saturday-night sign call and the Sunday open-house follow-up.</li><li>Asks the questions you would ask: buying or selling, price range, area, are they already working with an agent, how soon.</li><li>Books the showing or listing appointment on your real calendar and sends you the lead by text on the spot.</li><li>Handles seller leads differently from buyer leads, so a listing opportunity never gets treated like a tire-kicker.</li></ul>'},
        {"h2_html": "The math is <em>one commission</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not need to recover many calls for this to pay for itself. One captured buyer who would have called the next agent, or one listing appointment you would have missed on a weekend, is typically worth several thousand dollars in commission, which is more than the whole system costs for a long time. Everything else it catches after that is margin. The goal is to stop handing your pipeline to the agent who answers faster.</p>'},
        {"h2_html": "You own the number, the leads, and the list",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing phone number, or a new one that is registered in your name, not ours. Every caller, every lead, and every contact detail is yours and stays yours, exportable any time. There is no long contract and no holding your data hostage to keep you paying. The AI receptionist is one piece of the Top Shelf platform, and it plugs into the same CRM that follows up on every lead so nothing you capture goes cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A Saturday sign call, while you are <em>mid-showing</em>",
        "body_html": 'It is 2 p.m. on Saturday. You are walking a family through a listing when another buyer drives past one of your yard signs and calls about it. Instead of voicemail, your AI receptionist answers, confirms the buyer likes the neighborhood and is pre-approved, and books a showing for Sunday at 11. Before you finish the tour you are in, your phone has a text with the buyer name, number, the property they asked about, and the appointment already on your calendar. You never stopped what you were doing, and you did not lose the buyer to the agent who happened to be free.'},
    "faqs": [
        ("Does it work with my current phone number?",
         'Yes. It can answer on your existing number, or set up a new number that is registered in your name. Either way the number and every lead that comes through it belong to you and go with you if you ever leave.'),
        ("Can it actually book showings and listing appointments?",
         'Yes. It books straight onto your calendar based on your availability, sends you the details by text right away, and can send the caller a confirmation. You decide the rules, like how much notice you need and which time blocks are open for tours.'),
        ("What does it say to a seller lead versus a buyer?",
         'It handles them differently. A buyer gets qualified on price range, area, timeline, and whether they are already working with an agent. A seller lead gets treated as a listing opportunity, captures the property and their timeline, and books a listing consult, so a potential listing is never brushed off.'),
        ("Is this going to sound like a robot to my clients?",
         'It answers naturally and professionally, and it is upfront rather than pretending to be a person. Most callers care about one thing, that someone picked up and is handling their request, which beats a voicemail box every time. You can hear how it handles a live call before you decide.'),
        ("How fast can it be running?",
         'Setup is included and there is no separate onboarding fee. We configure the questions, your calendar, and the buyer and seller flows for you, so it is answering your calls in days, not weeks. Start with a free audit and we will show you exactly what your current setup is missing.')],
    "related": [
        ("industry-real-estate.html", "Everything Top Shelf does for real estate agents"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("solution-crm.html", "The CRM that follows up on every lead you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing clients to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many calls and leads your current setup is missing, whether you work with us or not. No credit card, never a call center.",
}]

# additional per-trade specs: corpus_specs.py (realtor) + any scripts/specs_*.py (trade batches)
import importlib, glob as _glob
try:
    from corpus_specs import SPECS as _MORE
    SPECS = SPECS + _MORE
except Exception as _e:
    print(f"note: corpus_specs not loaded ({_e})")
for _sf in sorted(_glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "specs_*.py"))):
    _mod = os.path.splitext(os.path.basename(_sf))[0]
    try:
        SPECS = SPECS + getattr(importlib.import_module(_mod), "SPECS", [])
    except Exception as _e:
        print(f"note: {_mod} not loaded ({_e})")


def _selfcheck():
    shell = extract_shell()
    for req in ("head", "nav", "footer", "tail"):
        assert shell[req] and len(shell[req]) > 50, f"shell.{req} looks empty"
    assert "G-4QCCJ3HP11" in shell["head"], "GA4 not in reused head"
    page = build_page(SPECS[0], shell)
    assert page.count("<h1") == 1, "must have exactly one h1"
    assert page.count("application/ld+json") == 3, "expected 3 schema blocks"
    assert 'rel="canonical"' in page and "og:title" in page and "twitter:card" in page
    assert 'assets/events.js' in page, "events.js (conversion tracking) not linked"
    assert 'class="corpus-grid"' in page and 'class="corpus-aside"' in page, "missing sidebar layout"
    assert "aside-toc" in page and 'href="#faq"' in page, "missing jump-link TOC"
    assert "site.css?v=20260918a" in page, "site.css version not bumped (sidebar CSS won't load)"
    assert "demo-frame" in page and "crm.topshelfsolutions.io/e/ai-phone" in page, "demo missing on demo spec"
    import re as _r
    words = len(_r.sub(r"<[^>]+>", " ", _r.search(r"<main>(.*?)</main>", page, _r.S).group(1)).split())
    assert words >= 600, f"body only {words} words (need >=600, anti-thin)"
    print(f"selfcheck OK: 1 h1, 3 schema, sidebar+TOC+demo present, css bumped, {words} body words")

if __name__ == "__main__":
    _selfcheck()
    shell = extract_shell()
    for spec in SPECS:
        out = f"{spec['slug']}.html"
        open(out, "w", encoding="utf-8", newline="").write(build_page(spec, shell))
        print(f"wrote {out}")
