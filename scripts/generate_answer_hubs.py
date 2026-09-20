#!/usr/bin/env python3
"""Answer hubs (plan §8 AEO layer): give crawlers + AI answer engines a clean, consolidated path
to every colony question page, and cluster the questions thematically so each cluster is its own
citable page.

Structure (chosen to fully cover every colony page with NO subset-duplication):
  answers.html            = the answer center. Links the 4 major topic hubs, directly lists the
                            3 small themes (online-booking / automation / review-software) + the
                            Top Shelf "all-in-one" questions, and links the 6 industry hubs.
  answers-<service>.html  = one topic hub for each of the 4 major themes (ai-receptionist, crm,
                            websites-seo, marketing), listing that theme's questions grouped by
                            industry -> trade, linking to the matching solution page.
Every colony page is reachable: the 4 topic hubs cover the 4 big bridge services; answers.html
directly lists the 3 small services + category. Disjoint question sets => no dup between hubs.

Reuses generate_corpus for the real site shell / esc / EVENTS / SITE. Run:
  python scripts/generate_answer_hubs.py
"""
import os, re, json, sys, glob, importlib, html as _html
from collections import defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import generate_corpus as gc
SITE, esc = gc.SITE, gc.esc

HUB_ORDER = ["Home Services", "Medical & Dental", "Legal", "Real Estate", "Auto", "Salon, Spa & Fitness"]
HUB_SLUG = {  # industry hub file per hub_name (for the "by industry" links)
    "Home Services": "industry-home-services.html", "Medical & Dental": "industry-medical-dental.html",
    "Legal": "industry-legal.html", "Real Estate": "industry-real-estate.html",
    "Auto": "industry-auto.html", "Salon, Spa & Fitness": "industry-salon-spa-fitness.html",
}
# the 4 major themes get a dedicated topic hub
TOPIC_HUBS = {
    "ai-receptionist": ("answers-ai-receptionist", "AI Receptionist &amp; Missed-Call Questions",
                        "solution-ai-phone.html",
                        "Every trade loses work to calls it cannot get to. These are the questions owners actually ask about answering services, missed calls, and after-hours coverage, answered trade by trade."),
    "crm": ("answers-crm", "CRM, Follow-Up &amp; Lead Questions", "solution-crm.html",
            "Most jobs are lost after the first contact, not on price. These are the questions owners ask about following up on quotes, reviving cold leads, and whether a CRM is worth it, answered trade by trade."),
    "websites-seo": ("answers-websites-seo", "Website &amp; SEO Questions", "solution-websites-seo.html",
                     "A site only earns its keep if it gets found and turns visitors into calls. These are the questions owners ask about what a website costs and why they are not showing up on Google, answered trade by trade."),
    "marketing": ("answers-marketing", "Marketing &amp; Getting-Found Questions", "solution-marketing.html",
                  "Getting found and staying busy looks different in every trade. These are the questions owners ask about reviews, the map pack, and getting more customers, answered trade by trade."),
}
SMALL_SVC = ["online-booking", "automation", "review-software"]  # listed directly on answers.html
SMALL_LABEL = {"online-booking": "Online Booking", "automation": "Automation &amp; Reminders", "review-software": "Reviews"}


def load_colony():
    rows = []
    for sf in sorted(glob.glob("scripts/colony_specs_*.py")):
        suf = os.path.basename(sf)[len("colony_specs_"):-3]
        try:
            T = getattr(importlib.import_module("colony_specs_" + suf), "TOPICS", [])
        except Exception as e:
            print(f"note: {suf} not loaded ({e})"); continue
        for t in T:
            bs = t.get("bridge_slug", "")
            svc = bs.split("-for-", 1)[0] if "-for-" in bs else "?"
            rows.append(dict(slug=t["slug"], h1=re.sub(r"<[^>]+>", "", t["h1"]),
                             trade=t.get("trade_plural", "Top Shelf"),
                             hub=t.get("hub_name", "Top Shelf"), svc=svc, cat=(suf == "category")))
    return rows


def _hub_rank(h):
    return HUB_ORDER.index(h) if h in HUB_ORDER else 99


def group_list(rows):
    """rows -> HTML: grouped by industry hub -> trade -> question links."""
    by_hub = defaultdict(lambda: defaultdict(list))
    for r in rows:
        by_hub[r["hub"]][r["trade"]].append(r)
    cols = []
    for hub in sorted(by_hub, key=_hub_rank):
        blocks = []
        for trade in sorted(by_hub[hub]):
            items = "\n".join(f'          <li><a href="{r["slug"]}.html">{esc(r["h1"])}</a></li>'
                              for r in sorted(by_hub[hub][trade], key=lambda x: x["h1"].lower()))
            blocks.append(f'''        <div style="margin-bottom:1.2rem">
          <p style="font-family:var(--sans);font-size:.9rem;font-weight:600;color:var(--ink);margin-bottom:.3rem">{esc(trade).title()}</p>
          <ul style="list-style:none;line-height:1.7;font-size:.95rem">
{items}
          </ul>
        </div>''')
        cols.append(f'''      <div class="reveal" style="min-width:280px;flex:1 1 320px">
        <h3 style="font-family:var(--sans);font-size:.82rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin-bottom:.9rem">{esc(hub)}</h3>
{chr(10).join(blocks)}
      </div>''')
    return f'<div class="reveal" style="display:flex;flex-wrap:wrap;gap:2rem 3rem">\n{chr(10).join(cols)}\n    </div>'


def page(slug, title, h1, meta, intro, body, crumb_name, itemlist_rows):
    shell = SHELL
    head = re.sub(r"site\.css\?v=[0-9a-z]+", "site.css?v=20260918a", shell["head"])
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": crumb_name, "item": f"{SITE}/{slug}.html"}]}
    coll = {"@context": "https://schema.org", "@type": "CollectionPage", "name": _html.unescape(re.sub(r"<[^>]+>", "", h1)),
            "description": meta, "url": f"{SITE}/{slug}.html",
            "mainEntity": {"@type": "ItemList", "itemListElement": [
                {"@type": "ListItem", "position": i, "url": f"{SITE}/{s}.html", "name": _html.unescape(n)}
                for i, (s, n) in enumerate(itemlist_rows, 1)]}}
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in (crumb, coll))
    head_extra = f'''<title>{esc(title)}</title>
<meta name="description" content="{esc(meta)}">
<link rel="canonical" href="{SITE}/{slug}.html">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(re.sub(r"<[^>]+>", "", h1))}">
<meta property="og:description" content="{esc(meta)}">
<meta property="og:url" content="{SITE}/{slug}.html">
<meta property="og:image" content="{shell["og_img"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(re.sub(r"<[^>]+>", "", h1))}">
<meta name="twitter:description" content="{esc(meta)}">
{ld}'''
    hero = f'''<section class="page-hero">
  <div class="container page-hero-inner">
    <span class="eyebrow reveal">Answers</span>
    <h1 class="display display-lg reveal">{h1}</h1>
    <p class="page-hero-sub reveal">{esc(intro)}</p>
    <div class="page-hero-actions reveal">
      <a href="contact.html" class="btn btn-gold">Get Your Free Audit <span class="arr">&rarr;</span></a>
      <a href="tel:+14698333033" class="btn btn-line">Call (469) 833-3033</a>
    </div>
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
{hero}
{body}
</main>
{shell["footer"]}
{shell["tail"]}
{gc.EVENTS}
</body>
</html>'''


def section(eyebrow, h2, inner):
    return f'''<section class="section rule-top">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">{eyebrow}</span>
      <h2 class="display reveal" style="margin-top:1rem">{h2}</h2>
    </div>
    <div style="margin-top:1.6rem">{inner}</div>
  </div>
</section>'''


def build_topic_hub(svc, rows):
    slug, title_h1, sol, intro = TOPIC_HUBS[svc]
    my = [r for r in rows if r["svc"] == svc and not r["cat"]]
    body = group_list(my)
    solbtn = f'''<div class="reveal" style="margin-top:2rem;display:flex;gap:.8rem;flex-wrap:wrap">
      <a href="{sol}" class="btn btn-gold">See how it works <span class="arr">&rarr;</span></a>
      <a href="answers.html" class="btn btn-line">All answers <span class="arr">&rarr;</span></a>
    </div>'''
    full = section("By trade", "Questions, answered trade by trade", body + solbtn)
    return page(slug, f"{re.sub(r'&amp;','and',title_h1)} | Top Shelf Business Solutions",
                f"{title_h1}", meta_of(title_h1, len(my)), intro, full, "Answers",
                [(r["slug"], r["h1"]) for r in my])


def meta_of(title_h1, n):
    t = re.sub(r"<[^>]+>", "", title_h1).replace("&amp;", "and")
    return gc._trim_meta(f"{t} for local businesses, answered trade by trade. {n} straight, no-jargon answers from Top Shelf Business Solutions.")


def build_answers(rows):
    # topic-hub cards
    cards = []
    for svc, (slug, title_h1, sol, intro) in TOPIC_HUBS.items():
        n = len([r for r in rows if r["svc"] == svc and not r["cat"]])
        cards.append(f'''      <a href="{slug}.html" class="reveal" style="display:block;flex:1 1 320px;min-width:280px;border:1px solid var(--hairline);border-radius:var(--r-lg);background:var(--surface);padding:1.4rem 1.6rem;text-decoration:none">
        <h3 style="font-family:var(--sans);font-size:1.05rem;color:var(--ink);margin-bottom:.4rem">{title_h1}</h3>
        <p style="color:var(--ink-3);font-size:.92rem">{n} questions <span class="arr" style="color:var(--gold)">&rarr;</span></p>
      </a>''')
    topic = f'<div class="reveal" style="display:flex;flex-wrap:wrap;gap:1.2rem">\n{chr(10).join(cards)}\n    </div>'
    # small-service questions listed directly + category
    small = [r for r in rows if r["svc"] in SMALL_SVC and not r["cat"]]
    cat = [r for r in rows if r["cat"]]
    # industry links
    ind = "\n".join(f'      <li><a href="{HUB_SLUG[h]}">{esc(h)}</a></li>' for h in HUB_ORDER if h in HUB_SLUG)
    body = (section("Browse by topic", "Answers by <em>theme</em>", topic)
            + section("More questions", "Booking, reminders &amp; reviews", group_list(small))
            + (section("Top Shelf overall", "About the all-in-one platform",
                       '<ul class="reveal" style="list-style:none;line-height:1.9;font-size:.98rem">\n'
                       + "\n".join(f'      <li><a href="{r["slug"]}.html">{esc(r["h1"])}</a></li>' for r in sorted(cat, key=lambda x: x["h1"].lower()))
                       + '\n    </ul>') if cat else "")
            + section("Browse by industry", "Answers by <em>industry</em>",
                      f'<ul class="reveal" style="list-style:none;line-height:2;font-size:1.02rem">\n{ind}\n    </ul>'))
    intro = ("Straight, no-jargon answers to what local business owners actually ask us, about missed calls, "
             "cold leads, websites, reviews, and getting found. Browse by theme or by your industry.")
    itemrows = [(TOPIC_HUBS[s][0], re.sub(r"&amp;", "and", TOPIC_HUBS[s][1])) for s in TOPIC_HUBS] + \
               [(r["slug"], r["h1"]) for r in small + cat]
    return page("answers", "Answers for Local Business Owners | Top Shelf Business Solutions",
                "Answers for <em>Local Business Owners</em>",
                gc._trim_meta("Straight answers to the questions local business owners ask, about missed calls, cold leads, websites, reviews, and getting found. Browse by theme or industry."),
                intro, body, "Answers", itemrows)


SHELL = gc.extract_shell()

if __name__ == "__main__":
    rows = load_colony()
    print(f"loaded {len(rows)} colony questions ({len([r for r in rows if r['cat']])} category)")
    open("answers.html", "w", encoding="utf-8", newline="").write(build_answers(rows))
    print("wrote answers.html")
    for svc in TOPIC_HUBS:
        slug = TOPIC_HUBS[svc][0]
        open(f"{slug}.html", "w", encoding="utf-8", newline="").write(build_topic_hub(svc, rows))
        print(f"wrote {slug}.html ({len([r for r in rows if r['svc']==svc and not r['cat']])} questions)")
    # selfcheck: every colony page reachable from answers.html or a topic hub
    reach = set()
    a = open("answers.html", encoding="utf-8").read()
    reach |= set(re.findall(r'href="([a-z0-9-]+)\.html"', a))
    for svc in TOPIC_HUBS:
        h = open(f"{TOPIC_HUBS[svc][0]}.html", encoding="utf-8").read()
        reach |= set(re.findall(r'href="([a-z0-9-]+)\.html"', h))
    missing = [r["slug"] for r in rows if r["slug"] not in reach]
    assert not missing, f"colony pages NOT reachable from answer hubs: {missing[:10]} ({len(missing)})"
    print(f"selfcheck OK: all {len(rows)} colony pages reachable via answers.html + 4 topic hubs")
