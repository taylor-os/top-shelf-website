"""Concept D ("The buyer-led sample") generator.

Concept D applies what the five customer agents asked for
(docs/superpowers/specs/2026-11-27-customer-agent-findings.md). It reuses Concept A's
generator, which three of the five ranked first, and overrides the parts the reviews changed:
  - the DFW number in a bar on every page, and a phone Call / Text bar nothing covers
  - the industry picker right under the hero, then one job told start to finish in readable screens
  - owner quotes, matched to the industry where they fit
  - open answers instead of accordions; the questions only the call can answer are listed once
  - each industry page leads with the screen that sells it, full width, tap to enlarge
  - phone screens one per row on a phone; HIPAA/BAA in a heading on the dental page
Same content, pairs and captions as A, B and C. No new claims: quotes, the data line and the
HIPAA wording are the live site's own approved copy.

Run: python scripts/concepts/d/build.py
"""
import importlib.util
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("concept_a_build", os.path.join(HERE, "..", "a", "build.py"))
A = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(A)

ROOT = A.ROOT
A.HERE = HERE  # main() copies style.css and app.js from here
A.OUT = OUT = os.path.join(ROOT, "preview", "concepts-2026-11", "d")
A.CID = "D"
C, B, PAIRS, CAPS, BY_SLUG, e = A.C, A.B, A.PAIRS, A.CAPS, A.BY_SLUG, A.e
frame, crm_rel, web_rel, checks, head, ctas = A.frame, A.crm_rel, A.web_rel, A.checks, A.head, A.ctas

# ---------------------------------------------------------------- approved copy carried from the live site
# Owner quotes: solution-crm.html "Straight From the Owners" (live), verbatim.
QUOTES = {
    "gdr": ("We're a small crew, so when everyone's out on a repair the phone used to just ring out. Now every call gets answered "
            "and the job's booked before I'm back in the truck. We're on the Signature Plan and it fits us perfectly at our size. "
            "Top Shelf handles all of it behind the scenes, so I stay on the tools and off the phone.",
            "Your Neighborhood Garage Door Repair", "Owner · on the Signature Plan"),
    "tap": ("The part that changed everything for me is getting paid. Estimates go out the same day, and I can see exactly what's "
            "owed without digging through anything. We went with the Signature Plan and it's been worth every dollar. The Top Shelf "
            "team stays on top of the whole system so I can focus on the actual work.",
            "T.A.P. Services", "Owner · on the Signature Plan"),
    "reids": ("Before Top Shelf, everything felt like it was held together with sticky notes and missed calls. Now it all just runs. "
              "Leads come in, nobody falls through the cracks, and I can see where every deal stands without chasing it down. My "
              "business finally operates the way it should instead of feeling like chaos all day.",
              "Reids Auto Connection", "Owner"),
}
# Only where the quote's trade matches the page (restaurant, salon and dental reviewers: no garage-door quotes on our page).
QUOTES_FOR = {"home-services": ["gdr", "tap"], "car-lots": ["reids"]}
# pricing.html (live), verbatim.
DATA_LINE = ("Your customer data is yours:", "every name, number and job, and you can take it with you if you ever leave.")
# industry-medical-dental.html (live), verbatim sentences; "your practice stays compliant" left out on purpose.
HIPAA = ("HIPAA setup, BAA included",
         "We set your dental or medical practice up on HIPAA-compliant, BAA-backed tools, and we sign a Business Associate "
         "Agreement for your practice. Your patient calls, texts, intake forms, and records stay protected. You are responsible "
         "for confirming your own HIPAA obligations, and we configure the tools to support them.")

# The software each buyer said they'd be leaving or keeping. Named as a question only: no claim about how it connects.
WORKS_WITH = {
    "home-services": "Housecall Pro, Jobber or ServiceTitan",
    "auto-repair": "Shopmonkey, Tekmetric or Mitchell 1",
    "salon-spa": "Vagaro, Square or Booksy",
    "restaurants": "Toast or OpenTable",
    "medical-dental": "Dentrix, Eaglesoft or Open Dental",
}
# The screen each industry's buyer said sells it, shown first and full width.
LEAD = {
    "home-services": "5-customer-estimate-m.webp", "car-lots": "5-pay-page-m.webp", "auto-repair": "5-customer-estimate-m.webp",
    "auto-detailing": "5-customer-booking-m.webp", "real-estate": "2-listings-d.webp", "fitness": "5-member-app-m.webp",
    "salon-spa": "1-owner-today-d.webp", "restaurants": "3-events-d.webp", "medical-dental": "6-ai-receptionist-m.webp",
    "legal": "3-intake-d.webp", "retail": "2-hold-shelf-d.webp", "vet": "5-client-page-m.webp",
}
# Answers that are only a pointer to the call. D lists these questions once instead of repeating the dodge.
ON_CALL = {
    "How long does setup take?", "Can I bring my customer list over?", "What do card payments cost?",
    "When do I get paid after a customer pays by card?", "Do my techs only see their own jobs?",
    "Does it connect to QuickBooks?", "Is it available in Spanish?", "Who sets it up?",
}
# Salon "What owners get", said in words from the salon-spa screen captions (captions.json), booth rent left out.
SALON_GET = [
    "Your own booking page shows the deposit and the 48-hour rule",
    "Checkout takes the deposit off the ticket and splits the tip by who did what",
    "Book the next visit right at checkout",
    "The stylist sees the client in the chair with her last formula and photos",
]
C["industries"]["per_industry"]["salon-spa"]["what_owners_get"] = SALON_GET  # in memory, D only
# Footer: the disclaimer covers the samples only; the quote line shows on pages that carry quotes.
SAMPLE_NOTE = ("The sample screens and sample websites show made-up businesses, people and numbers. "
               "They show the kind of setup we build for each industry.")
QUOTE_NOTE = "The owner quotes are real, from businesses that use Top Shelf."
# One job, start to finish (B's story), told with Everline's screens.
STORY = [("6-ai-call-texts-m.webp", "The call you would have missed"), ("2-dispatch-board-d.webp", "On the board before morning"),
         ("5-customer-estimate-m.webp", "The estimate, approved by text"), ("3-tech-get-paid-m.webp", "Paid before the truck leaves"),
         ("1-today-d.webp", "The owner's morning")]

SMS = B["cta_secondary_href"]


def cap_for(slug, file):
    for s in CAPS.get(slug, {}).get("screens", []):
        if s["file"] == file:
            return s
    return None


def zoom(R, slug, file, inner):
    ok, rel = crm_rel(slug, file)
    if not ok:
        return inner
    return f'<a class="zoom" href="{R}{rel}" target="_blank" rel="noopener" aria-label="Open this screen full size">{inner}<span class="zoom-hint">Tap to see it full size</span></a>'


def shot(R, slug, file, alt, label, cls=""):
    kind = "desktop" if file.endswith("-d.webp") else "phone"
    return zoom(R, slug, file, frame(R, crm_rel(slug, file), kind, alt, label, cls))


def quotes(keys, h="What owners say", eyebrow="In their words"):
    if not keys:
        return ""
    figs = "".join(f'<figure class="quote"><blockquote>{e(QUOTES[k][0])}</blockquote><figcaption><strong>{e(QUOTES[k][1])}</strong>{e(QUOTES[k][2])}</figcaption></figure>'
                   for k in keys)
    return f'<section class="sec"><div class="wrap">{head(eyebrow, h)}<div class="quotes n{len(keys)}">{figs}</div></div></section>'


def data_line():
    return f'<p class="data-line"><strong>{e(DATA_LINE[0])}</strong> {e(DATA_LINE[1])}</p>'


# ---------------------------------------------------------------- shell overrides
def nav(P, R, active):
    bar = (f'<div class="localbar"><div class="wrap localbar-in"><span class="based">{e(B["based_in"])}</span>'
           f'<span><a href="{B["phone_href"]}">Call {e(B["phone"])}</a><span class="sep">·</span><a href="{SMS}">Text us</a></span></div></div>')
    return bar + _a_nav(P, R, active)


def footer(P, R):
    cb = (f'<nav class="callbar" aria-label="Call, text or try the CRM"><a href="{B["phone_href"]}">Call</a><a href="{SMS}">Text</a>'
          f'<a class="go" href="{R}{B["cta_primary_href"]}">{e(B["cta_primary"])}</a></nav>')
    return _a_footer(P, R).replace(e(C["sample_note"]), e(SAMPLE_NOTE), 1) + cb


def faq(items, h, body=""):
    answered = [q for q in items if q["q"] not in ON_CALL]
    on_call = [q["q"] for q in items if q["q"] in ON_CALL]
    qs = "".join(f'<div class="answer"><h3>{e(q["q"])}</h3><p>{e(q["a"])}</p></div>' for q in answered)
    box = ""
    if on_call:
        box = (f'<div class="on-call"><h3>Ask us these on the call</h3><p>We answer these on the call, before you sign up. '
               f'Call or text {e(B["phone"])}.</p><ul>{"".join(f"<li>{e(x)}</li>" for x in on_call)}</ul></div>')
    return f'<section class="sec faq-sec" id="faq"><div class="wrap">{head("", h, body)}<div class="answers">{qs}</div>{box}</div></section>'


def steps(items, h="How it works"):
    items = [dict(s, title="Send your first text") if s["step"] == "3" else s for s in items]
    li = "".join(f'<li><span class="num" aria-hidden="true">{e(s["step"])}</span><h3>{e(s["title"])}</h3><p>{e(s["body"])}</p></li>' for s in items)
    return (f'<section class="sec steps-sec"><div class="wrap">{head("", h)}<ol class="steps">{li}</ol>'
            f'<p class="note">Rather text? Text {e(B["phone"])}.</p></div></section>')


def pricing(R, extra_left=""):
    return _a_pricing(R, extra_left + data_line())


def page(path, title, desc, body, active=""):
    _a_page(path, title, desc, body, active)
    dest = os.path.join(OUT, path)
    with open(dest, encoding="utf-8") as f:
        html = f.read()
    html = html.replace(
        "family=Plus+Jakarta+Sans:wght@600;700;800&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@500",
        "family=Figtree:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@500")
    if 'class="quote"' in html:
        html = html.replace(f"<p>{e(SAMPLE_NOTE)}</p>", f"<p>{e(SAMPLE_NOTE)} {e(QUOTE_NOTE)}</p>", 1)
    with open(dest, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


def pair_panel(P, R, p, i):
    html = _a_pair_panel(P, R, p, i)
    if p["slug"] == "medical-dental":  # the dental reviewer's deal-breaker, said in the picker too
        html = html.replace('<div class="panel-links">', f'<p class="hipaa-line">{e(HIPAA[0])}</p><div class="panel-links">', 1)
    return html


# ---------------------------------------------------------------- home
def home_body(P, R):
    h = C["home"]
    s = h["sections"]
    hero_d = frame(R, crm_rel("home-services", "1-today-d.webp"), "desktop",
                   "Everline Home Services sample CRM: the owner's morning", "Sample screens", "hero-d", True)
    hero_m = frame(R, crm_rel("home-services", "6-ai-call-texts-m.webp"), "phone",
                   "Everline Home Services sample CRM: a call the AI receptionist booked", "Sample", "hero-m", True)
    proof = [x.replace("Websites from $499, one time", "Websites $499, one time") for x in h["proof_points"]]

    steps_html = []
    for i, (file, title) in enumerate(STORY, 1):
        sc = cap_for("home-services", file)
        wide = " wide" if file.endswith("-d.webp") else ""
        steps_html.append(f'''<div class="story-step{wide}">
  <div class="story-shot">{shot(R, "home-services", file, f"Everline Home Services sample CRM: {sc['role']}", "Sample")}</div>
  <div class="story-copy"><p class="story-num">0{i} · {e(sc["role"])}</p><h3>{e(title)}</h3><p>{e(sc["caption"])}</p></div>
</div>''')

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
    {checks(proof, "proof")}
  </div>
  <div class="hero-devices">{hero_d}{hero_m}</div>
</div></section>

<section class="sec wash" id="industries"><div class="wrap">
  {head("Pick your business", s["pairs"]["h"], s["pairs"]["body"])}
  {A.switcher(P, R)}
</div></section>

<section class="sec" id="story"><div class="wrap">
  {head("One job, start to finish", "From the 2 AM call to the paid invoice", "Everline Home Services is a sample home services company. Every screen is from its CRM, and each one opens full size.")}
  <div class="story">{"".join(steps_html)}</div>
  <p class="note">Pick another business above to see its own screens.</p>
</div></section>

{steps(C["crm"]["how_it_works"])}
{quotes(["gdr", "tap", "reids"])}

<section class="sec wash" id="websites"><div class="wrap web-tease">
  <div>
    {head(s["websites"]["eyebrow"], s["websites"]["h"], s["websites"]["body"])}
    <ul class="mini-list">{"".join(f'<li><strong>{e(i["title"])}</strong> {e(i["body"])}</li>' for i in inc[:3])}</ul>
    <p class="price-line"><span class="big">{e(C["pricing"]["website"]["price"])}</span> {e(C["pricing"]["website"]["period"])}</p>
    <a class="text-link" href="{P}websites.html">{e(s["websites"]["link_label"])}</a>
  </div>
  <div class="web-strip">{web_strip}</div>
</div></section>

{pricing(R)}
{faq(faq_items, s["faq"]["h"], s["faq"]["body"])}
{A.closing(R, s["closing"]["h"], s["closing"]["body"])}'''


# ---------------------------------------------------------------- crm page: A's page plus quotes, data line, open answers
def crm_body(P, R):
    html = _a_crm_body(P, R)
    marker = '<section class="sec steps-sec">'
    return html.replace(marker, quotes(["gdr", "tap", "reids"]) + marker, 1)


# ---------------------------------------------------------------- per industry
def industry_crm(p):
    ind = C["industries"]["per_industry"][p["slug"]]
    cap = CAPS.get(p["slug"], {})
    screens = cap.get("screens", [])
    lead_file = LEAD.get(p["slug"])
    lead = next((s for s in screens if s["file"] == lead_file), screens[0] if screens else None)

    def body(P, R):
        desk, phones = [], []
        for s in screens:
            if s is lead:
                continue
            alt = f"{p['business']} sample CRM: {s['role']}"
            if s["device"] == "desktop":
                desk.append(f'<div class="shot-row">{shot(R, p["slug"], s["file"], alt, "Sample screens")}'
                            f'<div class="shot-cap"><p class="role">{e(s["role"])}</p><p>{e(s["caption"])}</p></div></div>')
            else:
                phones.append(f'<div class="shot-phone">{shot(R, p["slug"], s["file"], alt, "Sample")}'
                              f'<p class="role">{e(s["role"])}</p><p>{e(s["caption"])}</p></div>')
        lead_html = ""
        if lead:
            is_phone = lead["device"] != "desktop"
            lead_html = (f'<div class="lead-shot{" is-phone" if is_phone else ""}">'
                         f'{shot(R, p["slug"], lead["file"], p["business"] + " sample CRM: " + lead["role"], "Sample")}'
                         f'<div class="lead-copy"><p class="role">{e(lead["role"])}</p><h2>Start with this screen</h2><p>{e(lead["caption"])}</p></div></div>')
        gallery = lead_html + "".join(desk) + (f'<div class="phones n{len(phones)}">{"".join(phones)}</div>' if phones else "")
        built = f'<p class="built">{e(cap["built_around"])}</p>' if cap.get("built_around") else ""

        boxes = []
        if p["slug"] == "medical-dental":
            boxes.append(f'<div class="note-box"><p class="eyebrow">HIPAA and BAA</p><h2>{e(HIPAA[0])}</h2><p>{e(HIPAA[1])}</p></div>')
        if p["slug"] in WORKS_WITH:
            boxes.append(f'<div class="note-box"><p class="eyebrow">Switching or keeping your software</p><h2>Using {e(WORKS_WITH[p["slug"]])}?</h2>'
                         f'<p>Tell us what you use today, and on the call we tell you straight how Top Shelf fits with it.</p></div>')
        box_html = (f'<section class="sec tight"><div class="wrap note-row n{len(boxes)}">{"".join(boxes)}</div></section>') if boxes else ""

        return f'''<section class="hero hero-plain"><div class="wrap ind-head">
  <div>{A.crumbs(P, p, "CRM")}
  <p class="eyebrow">Sample CRM · {e(p["business"])}</p>
  <h1 class="h1-sm">{e(ind["headline"])}</h1>
  <p class="lede">{e(ind["crm_intro"])}</p>{built}
  {A.switch_tabs(p, "crm")}</div>
  <div class="owner-get"><h2 class="minor">What owners get</h2>{checks(ind["what_owners_get"])}{ctas(R)}</div>
</div></section>
{box_html}
<section class="sec tight"><div class="wrap gallery">{gallery}</div></section>
{quotes(QUOTES_FOR.get(p["slug"], []), "From an owner in the same line of work")}
<section class="sec wash"><div class="wrap cross">
  {frame(R, web_rel(p), "website", p["business"] + " sample website", "Sample website")}
  <div><p class="eyebrow">Same business, same look</p><h2>{e(p["business"])} sample website</h2><p>{e(ind["website_intro"])}</p>
  <div class="panel-links"><a class="btn sm" href="{p["slug"]}-website.html">See the website</a><a class="text-link" href="{R}{p["website_dir"]}/index.html">Open the live sample site</a></div></div>
</div></section>
{A.price_strip(R)}
{A.pager(P, p, "crm")}'''
    page(f"industries/{p['slug']}-crm.html", f"{p['business']} sample CRM · {p['industry_label']} · Top Shelf",
         ind["crm_intro"], body, "industries.html")


def industry_web(p):
    _a_industry_web(p)
    # the website page carries the price too (salon and auto reviewers found pages with no price)
    dest = os.path.join(OUT, "industries", f"{p['slug']}-website.html")
    with open(dest, encoding="utf-8") as f:
        html = f.read()
    marker = '<nav class="pager'
    R = "../../../../"
    html = html.replace(marker, A.price_strip(R) + "\n" + marker, 1)
    with open(dest, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


# ---------------------------------------------------------------- wire the overrides into A's module
_a_nav, _a_footer, _a_pricing, _a_page = A.nav, A.footer, A.pricing, A.page
_a_crm_body, _a_industry_web, _a_pair_panel = A.crm_body, A.industry_web, A.pair_panel
A.nav, A.footer, A.faq, A.steps, A.pricing, A.page, A.pair_panel = nav, footer, faq, steps, pricing, page, pair_panel


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"))
    for f in ("style.css", "app.js"):
        shutil.copyfile(os.path.join(HERE, f), os.path.join(OUT, "assets", f))
    page("index.html", "Top Shelf CRM · Run the whole business from one app", C["home"]["sub"], home_body, "index.html")
    page("crm.html", "The Top Shelf CRM · Everything in one app", C["crm"]["sub"], crm_body, "crm.html")
    page("websites.html", "Websites, $499 one time · Top Shelf", C["websites"]["sub"], A.websites_body, "websites.html")
    page("industries.html", "Industries · A website and a CRM that go together · Top Shelf", C["industries"]["sub"],
         A.industries_body, "industries.html")
    for p in PAIRS:
        industry_crm(p)
        industry_web(p)
    n = sum(len([x for x in fs if x.endswith(".html")]) for _, _, fs in os.walk(OUT))
    print(f"Concept D: wrote {n} pages to {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
