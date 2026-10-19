"""Builds the Linewright Mobile Dent sample site (websites/linewright-mobile-dent/*.html).
Shared head/header/footer live here; each page body is below. Run: python scripts/build_linewright.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "websites" / "linewright-mobile-dent"
BASE = "https://www.topshelfsolutions.io/websites/linewright-mobile-dent/"
V = "20261019c"
PHONE = '<a href="tel:+11234567890" class="{cls}"><svg><use href="#i-phone"/></svg>123-456-7890</a>'

NAV = [("index.html", "Home"), ("services.html", "Services"), ("hail.html", "Hail"),
       ("results.html", "Results"), ("how-it-works.html", "How It Works")]

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<g fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.8.4 1.6.7 2.3a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.7-1.3a2 2 0 0 1 2.1-.4c.7.3 1.5.6 2.3.7a2 2 0 0 1 1.8 2z"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><line x1="4" y1="12" x2="19" y2="12"/><polyline points="12.5 5.5 19.5 12 12.5 18.5"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><polyline points="20 6.5 9.2 17.3 4 12.2"/></symbol>
<symbol id="i-camera" viewBox="0 0 24 24"><path d="M3 8.5A2 2 0 0 1 5 6.5h2.2l1.6-2.3h6.4l1.6 2.3H19a2 2 0 0 1 2 2V18a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><circle cx="12" cy="13" r="3.8"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M20 10.5c0 5.5-8 11-8 11s-8-5.5-8-11a8 8 0 0 1 16 0z"/><circle cx="12" cy="10.3" r="2.8"/></symbol>
<symbol id="i-home" viewBox="0 0 24 24"><path d="M3.5 10.5 12 3.5l8.5 7"/><path d="M5.5 9v11h13V9"/><path d="M10 20v-6h4v6"/></symbol>
<symbol id="i-building" viewBox="0 0 24 24"><rect x="4.5" y="3" width="15" height="18" rx="1"/><path d="M9 7h1.5M13.5 7H15M9 11h1.5M13.5 11H15M9 15h1.5M13.5 15H15M10.5 21v-3h3v3"/></symbol>
<symbol id="i-garage" viewBox="0 0 24 24"><path d="M3 9.5 12 4l9 5.5V20H3z"/><path d="M6.5 20v-8h11v8M6.5 14.5h11M6.5 17h11"/></symbol>
<symbol id="i-car" viewBox="0 0 24 24"><path d="M5 11l1.7-4.4A2 2 0 0 1 8.6 5.3h6.8a2 2 0 0 1 1.9 1.3L19 11"/><path d="M3.5 11h17v5.5h-17z"/><circle cx="7.5" cy="16.5" r="1.6"/><circle cx="16.5" cy="16.5" r="1.6"/></symbol>
<symbol id="i-truck" viewBox="0 0 24 24"><path d="M2.5 6.5h11v10h-11zM13.5 10h4l3 3v3.5h-7z"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/></symbol>
<symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 21.5s7.5-3.8 7.5-9.5V5.5L12 2.8 4.5 5.5V12c0 5.7 7.5 9.5 7.5 9.5z"/><polyline points="8.8 12 11 14.2 15.2 10"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15.4 14"/></symbol>
<symbol id="i-hail" viewBox="0 0 24 24"><path d="M7 15.5a4.5 4.5 0 0 1-.6-9 6 6 0 0 1 11.4 1.5 3.8 3.8 0 0 1-.3 7.5"/><circle cx="8.5" cy="19" r=".9"/><circle cx="12" cy="21" r=".9"/><circle cx="15.5" cy="19" r=".9"/><circle cx="12" cy="17" r=".9"/></symbol>
<symbol id="i-wheel" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2.4"/><path d="M12 3.2v6.4M12 14.4v6.4M3.6 12h6M14.4 12h6"/></symbol>
<symbol id="i-bulb" viewBox="0 0 24 24"><path d="M4 9.5c0-2.5 2.6-4.5 6-4.5 3 0 5.5 2 5.5 4.5S13 14 10 14c-3.4 0-6-2-6-4.5z"/><path d="M17.5 7.5H21M17.5 11.5H21M17 15l3 1.5"/></symbol>
<symbol id="i-spray" viewBox="0 0 24 24"><rect x="5" y="9" width="8" height="12" rx="1.5"/><path d="M7 9V6h4v3M11 6h3M16.5 5.5h.01M19.5 4h.01M19.5 7h.01M17.5 8.5h.01"/></symbol>
<symbol id="i-spark" viewBox="0 0 24 24"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></symbol>
<symbol id="i-drop" viewBox="0 0 24 24"><path d="M12 3s6.5 7 6.5 11.5a6.5 6.5 0 0 1-13 0C5.5 10 12 3 12 3z"/></symbol>
<symbol id="i-layers" viewBox="0 0 24 24"><polygon points="12 3 21 8 12 13 3 8"/><polyline points="3 12.5 12 17.5 21 12.5"/><polyline points="3 16.5 12 21.5 21 16.5"/></symbol>
<symbol id="i-tool" viewBox="0 0 24 24"><path d="M3 21 13.5 10.5M13.5 10.5c-1-2.7.5-6 3.5-6.5l-2 3 2 2 3-2c-.5 3-3.8 4.5-6.5 3.5z"/></symbol>
<symbol id="i-swap" viewBox="0 0 24 24"><polyline points="8 7 3 12 8 17"/><polyline points="16 7 21 12 16 17"/></symbol>
<symbol id="i-msg" viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/></symbol>
<symbol id="i-upload" viewBox="0 0 24 24"><path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v3a1.5 1.5 0 0 0 1.5 1.5h13A1.5 1.5 0 0 0 20 19v-3"/></symbol>
<symbol id="i-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></symbol>
<symbol id="i-key" viewBox="0 0 24 24"><circle cx="8" cy="8" r="4.2"/><path d="M11 11l8 8M16 16l2-2M18.5 18.5l1.6-1.6"/></symbol>
</g></defs></svg>"""


def head(title, desc, path, img="hero.jpg"):
    url = BASE + ("" if path == "index.html" else path)
    return f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="noindex,follow">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}assets/img/{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0A0E14">
<link rel="icon" href="assets/logo-mark.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,500..900&family=IBM+Plex+Mono:wght@400;500;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css?v={V}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{ICONS}
"""


def header(active):
    links = "".join(f'<a href="{h}"' + (' aria-current="page"' if h == active else "") + f">{t}</a>" for h, t in NAV)
    mlinks = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV) + '<a href="quote.html">Get a Quote</a>'
    return f"""<header class="header">
  <div class="header__inner">
    <a href="index.html" class="brand" aria-label="Linewright Mobile Dent Co., home">
      <img src="assets/logo-mark.svg" alt="" class="brand__mark" width="36" height="36">
      <span class="brand__name">Linewright<small>Mobile Dent Co.</small></span>
    </a>
    <nav class="nav" aria-label="Primary">{links}</nav>
    <div class="header__cta">
      {PHONE.format(cls="header__phone")}
      <a href="quote.html" class="btn btn--lime"><svg><use href="#i-camera"/></svg>Photo quote</a>
      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="drawer"><span></span></button>
    </div>
  </div>
</header>
<div class="drawer" id="drawer" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="drawer__top">
    <span class="brand"><img src="assets/logo-mark.svg" alt="" class="brand__mark" width="36" height="36"><span class="brand__name">Linewright<small>Mobile Dent Co.</small></span></span>
    <button class="drawer__close" aria-label="Close menu">&times;</button>
  </div>
  <nav aria-label="Mobile">{mlinks}</nav>
  <div class="drawer__foot">
    {PHONE.format(cls="drawer__phone")}
    <a href="quote.html" class="btn btn--lime btn--lg btn--block"><svg><use href="#i-camera"/></svg>Send photos for a quote</a>
  </div>
</div>
<main id="main">
"""


CTA = """<section class="section cta">
  <div class="wrap">
    <div data-reveal>
      <h2>Send three photos. Get a real number.</h2>
      <p>Take one straight on, one at an angle, and one from a few steps back. Most quotes come back the same day, and the price we quote is the price you pay.</p>
    </div>
    <div class="cta__actions" data-reveal>
      <a href="quote.html" class="btn btn--ink btn--lg"><svg><use href="#i-camera"/></svg>Start a photo quote</a>
      <a href="tel:+11234567890" class="cta__phone"><svg><use href="#i-phone"/></svg>123-456-7890</a>
      <a href="sms:+11234567890" class="btn btn--ghost" style="border-color:rgba(10,14,20,.35);color:var(--ink)"><svg><use href="#i-msg"/></svg>Or text the photos</a>
    </div>
  </div>
</section>
"""

FOOTER = """</main>
<footer class="footer">
  <div class="wrap">
    <p class="footer__big" aria-hidden="true">Every line straight.</p>
    <div class="footer__grid">
      <div>
        <a href="index.html" class="brand"><img src="assets/logo-mark.svg" alt="" class="brand__mark" width="36" height="36"><span class="brand__name">Linewright<small>Mobile Dent Co.</small></span></a>
        <p>Mobile paintless dent repair and paint repair across the Harlow Valley. No shop to drive to. We work where the car is parked.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="services.html#pdr">Paintless dent repair</a></li>
          <li><a href="hail.html">Hail damage</a></li>
          <li><a href="services.html#dent-paint">Dent + paint repair</a></li>
          <li><a href="services.html#clear-coat">Clear coat repair</a></li>
          <li><a href="services.html#correction">Paint correction</a></li>
          <li><a href="services.html#wheels">Wheels &amp; headlights</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="how-it-works.html">How it works</a></li>
          <li><a href="results.html">Before &amp; after</a></li>
          <li><a href="how-it-works.html#area">Service area</a></li>
          <li><a href="services.html#fleet">Fleet &amp; dealers</a></li>
          <li><a href="how-it-works.html#faq">FAQ</a></li>
        </ul>
      </div>
      <div>
        <h4>Book</h4>
        <ul>
          <li><a href="tel:+11234567890">123-456-7890</a></li>
          <li><a href="sms:+11234567890">Text us photos</a></li>
          <li><a href="mailto:contact@linewright.com">contact@linewright.com</a></li>
          <li><a href="quote.html">Online photo quote</a></li>
        </ul>
        <p style="margin-top:14px">By appointment only. We don't have a storefront.</p>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; <span data-year>2026</span> Linewright Mobile Dent Co. A sample site, fictional business.</span>
      <a class="footer__credit" href="https://www.topshelfsolutions.io/" aria-label="Website by Top Shelf Business Solutions"><span>Website by</span><img src="assets/topshelf-logo.png" alt="Top Shelf" width="88" height="22"></a>
    </div>
  </div>
</footer>
<div class="callbar">
  <a href="tel:+11234567890" class="btn btn--ghost"><svg><use href="#i-phone"/></svg>Call</a>
  <a href="quote.html" class="btn btn--lime"><svg><use href="#i-camera"/></svg>Photo quote</a>
</div>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="assets/app.js?v=""" + V + """" defer></script>
</body>
</html>
"""

SCHEMA = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"AutoBodyShop","name":"Linewright Mobile Dent Co.","url":"https://www.topshelfsolutions.io/websites/linewright-mobile-dent/","telephone":"+1-123-456-7890","email":"contact@linewright.com","image":"https://www.topshelfsolutions.io/websites/linewright-mobile-dent/assets/img/hero.jpg","description":"Mobile paintless dent repair, hail repair, clear coat and paint repair done at your home or workplace.","areaServed":["Harlow Springs","Cedar Hollow","Brightmoor","Kessling Park","Larkfield","Ostrander Hills","Millpond","Westvale","Dunmore Flats","Ridgecrest"],"priceRange":"$$"}</script>
"""


def ba(before, after, alt, label, start=50):
    return f"""<div class="ba" style="--pos:{start}%">
  <img src="assets/img/{after}" alt="After: {alt}, reflected lines straight" loading="lazy" width="1400" height="1045">
  <img class="ba__before" src="assets/img/{before}" alt="Before: {alt}, reflected lines bent around the damage" loading="lazy" width="1400" height="1045">
  <span class="ba__tag ba__tag--b">Before</span><span class="ba__tag ba__tag--a">After</span>
  <span class="ba__line"></span>
  <input type="range" min="0" max="100" value="{start}" aria-label="{label}: drag to compare before and after">
  <span class="ba__knob" aria-hidden="true"><svg><use href="#i-swap"/></svg></span>
</div>"""


CAR = """<svg class="car__art" viewBox="0 0 800 300" role="img" aria-label="Side view of a car with tappable damage points">
  <ellipse cx="400" cy="288" rx="370" ry="8" fill="rgba(10,14,20,.12)"/>
  <path d="M38 214C36 192 44 176 70 170L196 156C236 118 270 96 318 88L470 84C520 88 552 112 590 146L708 160C744 166 762 180 764 204L764 222C764 230 758 234 750 234L682 234A62 62 0 0 0 558 234L252 234A62 62 0 0 0 128 234L52 234C42 234 38 226 38 214Z" fill="#fff" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>
  <path d="M222 156C254 124 282 106 322 100L384 98L384 156Z" fill="#DDE2E8" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M396 98L466 97C506 100 534 118 566 148L396 156Z" fill="#DDE2E8" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round"/>
  <g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
    <path d="M390 98V232M548 152V232M222 158C220 190 228 214 250 232"/>
    <path d="M70 188C300 180 520 180 760 194" stroke-opacity=".35"/>
    <path d="M342 174h22M500 174h22" stroke-width="4"/>
    <path d="M560 142l18-7 4 11z" fill="currentColor"/>
  </g>
  <path d="M716 166C738 168 754 176 760 188L726 186Z" fill="#CCFF3D" stroke="currentColor" stroke-width="2"/>
  <path d="M42 184L72 176L74 190L40 196Z" fill="#E5484D" stroke="currentColor" stroke-width="2"/>
  <g stroke="currentColor" stroke-width="3"><circle cx="190" cy="234" r="50" fill="#1A222D"/><circle cx="190" cy="234" r="30" fill="#DDE2E8"/><circle cx="620" cy="234" r="50" fill="#1A222D"/><circle cx="620" cy="234" r="30" fill="#DDE2E8"/></g>
  <g fill="currentColor"><circle cx="190" cy="234" r="7"/><circle cx="620" cy="234" r="7"/></g>
</svg>"""

PICKS = [
    # id, spot (x%, y%) or None, chip label, tag, title, text, (dt, dd), (dt, dd), link
    ("pdr", (41.2, 64), "Door ding", "Doors, fenders, quarter panels", "Paintless Dent Repair",
     "If the paint isn't cracked, we can usually push the dent out from behind and keep your factory finish. Nothing gets filled or repainted, so there's nothing to color-match.",
     ("Typical time", "30 to 90 min a dent"), ("Your paint", "Stays factory"), "services.html#pdr"),
    ("hail", (81, 50.5), "Hail", "Hood, roof, trunk lid", "Hail Damage Repair",
     "Dozens or hundreds of dents, worked out one at a time in your driveway. We write the estimate under the light and deal with your adjuster directly.",
     ("Typical time", "1 to 3 days"), ("Insurance", "We talk to your adjuster"), "hail.html"),
    ("clear", (50, 29), "Peeling clear coat", "Roof, hood, pillars", "Clear Coat Repair",
     "Sun-cooked clear coat that's flaking or chalky gets sanded back, refinished and blended so the repair disappears into the panel next to it.",
     ("Typical time", "Half day to a day"), ("Method", "Sand, refinish, blend"), "services.html#clear-coat"),
    ("dentpaint", (17.5, 59), "Crease with paint damage", "Creases, cracked or chipped paint", "Dent + Paint Repair",
     "When the paint is broken, PDR alone won't finish the job. We pull the metal close, fill only what's needed, then spot refinish that one area.",
     ("Typical time", "Usually 1 day"), ("Method", "Pull, fill, spot refinish"), "services.html#dent-paint"),
    ("scuff", (5.4, 70), "Bumper scuff", "Bumper corners", "Bumper Scuff &amp; Scratch Repair",
     "Garage-wall scrapes and parking-post scuffs on plastic bumpers. We repair and refinish the damaged corner instead of painting the whole bumper.",
     ("Typical time", "2 to 4 hours"), ("Color", "Matched to your code"), "services.html#scuff"),
    ("wheel", (77.5, 78), "Curb rash", "Wheels", "Wheel Curb Rash Repair",
     "Scraped rim edges get sanded, filled and refinished right on the car. Painted and powder-coated wheels are the usual fix. Some machined faces need a lathe, and we'll tell you up front if yours does.",
     ("Typical time", "About an hour a wheel"), ("Finishes", "Painted, powder, most others"), "services.html#wheels"),
    ("headlight", (92.6, 59.5), "Hazy headlight", "Headlights", "Headlight Restoration",
     "Yellow, foggy lenses wet-sanded, polished clear and sealed with a UV coat so they stay clear for years instead of a few months.",
     ("Typical time", "About an hour"), ("Finish", "UV-sealed"), "services.html#wheels"),
    ("correction", None, "Swirls &amp; dull paint", "The whole car", "Paint Correction",
     "Machine polishing in one to three stages takes out swirl marks, haze and water spotting. We measure paint thickness first so we never polish through it.",
     ("Typical time", "1 to 2 days"), ("Stages", "1 to 3, by paint depth"), "services.html#correction"),
    ("protect", None, "Protect the finish", "The whole car", "Ceramic Coating &amp; PPF",
     "Once the panel is straight and the paint is corrected, lock it in. Ceramic coating for gloss and easy washing, clear film on the parts that take the chips.",
     ("Typical time", "1 to 2 days"), ("Lasts", "Years, not weeks"), "services.html#protect"),
]


def picker():
    spots = "".join(
        f'<button class="spot" style="left:{s[0]}%;top:{s[1]}%" data-pick="{i}" aria-pressed="false" aria-label="{t}"><span></span></button>'
        for i, s, c, tg, t, *_ in PICKS if s)
    chips = "".join(f'<button class="chipbtn" data-pick="{i}" aria-pressed="false">{c}</button>' for i, s, c, *_ in PICKS)
    panels = "".join(f"""<div class="pick" id="pick-{i}" aria-live="polite">
  <span class="pick__tag">{tg}</span>
  <h3>{t}</h3>
  <p>{txt}</p>
  <dl><div><dt>{a[0]}</dt><dd>{a[1]}</dd></div><div><dt>{b[0]}</dt><dd>{b[1]}</dd></div></dl>
  <a href="{link}" class="btn btn--ink">See how we fix it <svg><use href="#i-arrow"/></svg></a>
</div>""" for i, s, c, tg, t, txt, a, b, link in PICKS)
    return f"""<section class="section light" id="damage">
  <div class="wrap">
    <div class="head" data-reveal>
      <div><span class="eyebrow">Where's the damage?</span><h2>Tap the spot. See the fix.</h2></div>
      <p class="lede">Every repair we do, pinned to the part of the car it usually happens to. Tap a dot, or pick from the list.</p>
    </div>
    <div class="picker">
      <div data-reveal>
        <div class="car">{CAR}{spots}</div>
        <div class="picker__list" aria-label="Damage types">{chips}</div>
      </div>
      <div class="picker__panels" data-reveal>{panels}</div>
    </div>
  </div>
</section>
"""


SERVICES = [
    ("pdr", "tools.jpg", "Paintless Dent Repair", "Door dings, creases, hail, larger dents. Factory paint stays put."),
    ("hail", "hail.jpg", "Hail Damage Repair", "Storm damage worked out at your place, with your adjuster in the loop."),
    ("dent-paint", "crease-before.jpg", "Dent + Paint Repair", "Cracked paint? We pull it, fill it and spot refinish only that area."),
    ("clear-coat", "clearcoat.jpg", "Clear Coat Repair", "Peeling, chalky or scratched clear refinished and blended in."),
    ("correction", "polish.jpg", "Paint Correction", "Swirls, haze and water spots polished out in one to three stages."),
    ("scuff", "bumper.jpg", "Bumper Scuff Repair", "Corner scrapes repaired and color-matched without a full repaint."),
    ("wheels", "wheel.jpg", "Curb Rash Repair", "Scraped rims refinished on the car, usually in about an hour."),
    ("wheels", "headlight.jpg", "Headlight Restoration", "Yellow lenses sanded, polished clear and UV-sealed."),
    ("protect", "ceramic.jpg", "Ceramic &amp; Paint Film", "Protect the finish once it's straight and corrected."),
]


def svc_grid():
    cards = "".join(f"""<a class="card" href="{'hail.html' if sid == 'hail' else 'services.html#' + sid}">
  <div class="card__img"><img src="assets/img/{img}" alt="" loading="lazy" width="1400" height="930"></div>
  <div class="card__body"><span class="card__num">{n:02d}</span><h3>{t}</h3><p>{d}</p><span class="card__more">Learn more <svg><use href="#i-arrow"/></svg></span></div>
</a>""" for n, (sid, img, t, d) in enumerate(SERVICES, 1))
    return f'<div class="svc" data-reveal-stagger>{cards}</div>'


REVIEWS = [
    ("Someone opened their door into my car at the gym. I sent three photos at lunch and he fixed it in my office parking lot that afternoon. I honestly can't find where the dent was.", "Dana R.", "Door ding, Kessling Park", "DR"),
    ("Hail took out my hood and roof. Linewright wrote the estimate, talked to my adjuster, and did all of it in my driveway over two days. I paid my deductible and that was it.", "Marcus T.", "Hail repair, Cedar Hollow", "MT"),
    ("He told me straight that one of my dents had cracked paint and needed paint work, not PDR. Quoted both, did both, and the price didn't move. That's why I'll call him again.", "Priya S.", "Dent + paint, Brightmoor", "PS"),
    ("My lease turn-in was in a week and I had four dings, curb rash on two wheels and hazy headlights. One visit to my apartment garage and I got no damage charges.", "Jordan L.", "Lease-return prep, Westvale", "JL"),
    ("We run 30 service trucks. Linewright comes to our yard every other Friday and works through whatever the week did to them. Nothing comes off the road for it.", "Ellen W.", "Fleet manager, Millpond", "EW"),
    ("The paint correction on my black car is unreal. It looks deeper than the day I bought it. Took two days and I never had to drop it anywhere.", "Chris B.", "Paint correction, Larkfield", "CB"),
]


def reviews(n=3, dark=False):
    cards = "".join(f"""<article class="review"><div class="review__stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>&ldquo;{q}&rdquo;</p><footer><i>{ini}</i><div><b>{who}</b><span>{what}</span></div></footer></article>""" for q, who, what, ini in REVIEWS[:n])
    return f'<div class="reviews{" reviews--dark" if dark else ""}" data-reveal-stagger>{cards}</div>'


TOWNS = ["Harlow Springs", "Cedar Hollow", "Brightmoor", "Kessling Park", "Larkfield", "Ostrander Hills", "Millpond", "Westvale", "Dunmore Flats", "Ridgecrest"]

# ------------------------------------------------------------------ pages
PAGES = {}

PAGES["index.html"] = (
    "Linewright Mobile Dent Co. | Mobile Paintless Dent Repair",
    "Mobile paintless dent repair, hail repair, clear coat and paint repair at your home or office across the Harlow Valley. Send photos for a quote: 123-456-7890.",
    SCHEMA + """<section class="hero">
  <div class="hero__media"><img src="assets/img/hero.jpg" srcset="assets/img/hero-sm.jpg 900w, assets/img/hero.jpg 1920w" sizes="100vw" alt="A Linewright technician working a dent out of an SUV door in a driveway at sunset, a striped light board beside him" width="1920" height="1086" fetchpriority="high"></div>
  <div class="hero__inner">
    <div>
      <span class="eyebrow">Mobile dent &amp; paint repair</span>
      <h1>Dents out, right in your <span class="hero__rot" data-rotate='["driveway.","office lot.","garage.","dealer lot."]'>driveway.</span></h1>
      <p class="lede">We don't have a shop, and you don't need one. We bring the light board, the tools and the paint to wherever your car is parked, and the dent leaves before we do.</p>
      <div class="hero__actions">
        <a href="quote.html" class="btn btn--lime btn--lg"><svg><use href="#i-camera"/></svg>Get a photo quote</a>
        <a href="#board" class="btn btn--ghost btn--lg">See how we read a dent <svg><use href="#i-arrow"/></svg></a>
      </div>
      <div class="hero__meta"><span><svg><use href="#i-shield"/></svg>Lifetime PDR guarantee</span><span><svg><use href="#i-clock"/></svg>Most dings under an hour</span><span>&#9733; 4.9 from 600+ reviews</span></div>
    </div>
    <aside class="hero__card" aria-label="How booking works">
      <h3>Nothing to drop off</h3>
      <ol>
        <li><b>01</b>Text or upload three photos</li>
        <li><b>02</b>Get a fixed price, usually same day</li>
        <li><b>03</b>We meet your car where it's parked</li>
        <li><b>04</b>Check the lines, then pay</li>
      </ol>
    </aside>
  </div>
</section>

<div class="marquee" aria-label="Places we work">
  <div class="marquee__track" aria-hidden="true">
    <span class="marquee__item">Driveways</span><span class="marquee__item">Office parking lots</span><span class="marquee__item">Apartment garages</span><span class="marquee__item">Dealer lots</span><span class="marquee__item">Fleet yards</span><span class="marquee__item">Gym lots</span><span class="marquee__item">Under the carport</span>
    <span class="marquee__item">Driveways</span><span class="marquee__item">Office parking lots</span><span class="marquee__item">Apartment garages</span><span class="marquee__item">Dealer lots</span><span class="marquee__item">Fleet yards</span><span class="marquee__item">Gym lots</span><span class="marquee__item">Under the carport</span>
  </div>
  <span class="sr-only">Driveways, office parking lots, apartment garages, dealer lots, fleet yards, gym lots, under the carport.</span>
</div>

<section class="board" id="board" aria-labelledby="board-h">
  <div class="board__stage">
    <canvas aria-hidden="true"></canvas>
    <div class="board__copy">
      <div class="board__box">
        <span class="eyebrow">How we see a dent</span>
        <h2 id="board-h">A dent bends the light. We bend it back.</h2>
        <ol class="board__steps">
          <li class="on"><b>01</b><div><strong>Light board up</strong><span>A striped light reflects off the panel. Wherever the lines bend, the metal is out of place.</span></div></li>
          <li><b>02</b><div><strong>Work it from behind</strong><span>Steel rods slide in behind the panel and push the low spots up, a little at a time.</span></div></li>
          <li><b>03</b><div><strong>Lines run straight</strong><span>When the reflection is straight again, the dent is gone. It's still your original paint, with no filler underneath.</span></div></li>
        </ol>
        <div class="board__meter" aria-hidden="true">Dent<i></i>Straight</div>
      </div>
    </div>
    <span class="board__hint" aria-hidden="true">Move your cursor over the lines</span>
  </div>
</section>
""" + picker() + """
<section class="section">
  <div class="wrap">
    <div class="head" data-reveal>
      <div><span class="eyebrow">What we fix</span><h2>Nine repairs. One van.</h2></div>
      <p class="lede">Paintless dent repair is the core of what we do. When a job needs paint, polish or protection, we carry that too, so you aren't sent off to a body shop.</p>
    </div>
    """ + svc_grid() + """
  </div>
</section>

<section class="section ink2" id="results">
  <div class="wrap">
    <div class="ba-wrap">
      <div data-reveal>
        <div class="ba-tabs" role="tablist" aria-label="Before and after examples">
          <button role="tab" id="t-door" aria-controls="p-door" aria-selected="true">Door ding</button>
          <button role="tab" id="t-crease" aria-controls="p-crease" aria-selected="false" tabindex="-1">Crease</button>
          <button role="tab" id="t-hood" aria-controls="p-hood" aria-selected="false" tabindex="-1">Hail hood</button>
        </div>
        <div class="ba-panel" id="p-door" role="tabpanel" aria-labelledby="t-door">""" + ba("door-before.jpg", "door-after.jpg", "a white car door with a round ding", "Door ding") + """</div>
        <div class="ba-panel" id="p-crease" role="tabpanel" aria-labelledby="t-crease" hidden>""" + ba("crease-before.jpg", "crease-after.jpg", "a gray quarter panel with a long crease", "Crease") + """</div>
        <div class="ba-panel" id="p-hood" role="tabpanel" aria-labelledby="t-hood" hidden>""" + ba("hood-before.jpg", "hood-after.jpg", "a black hood covered in hail dents", "Hail hood") + """</div>
      </div>
      <div data-reveal>
        <span class="eyebrow">Before &amp; after</span>
        <h2>Drag the line.</h2>
        <p class="lede">Same panel, same light board, before and after. Look at the reflected stripes. Bent lines mean a dent, and straight lines mean it's gone.</p>
        <a href="results.html" class="btn btn--ghost btn--lg" style="margin-top:12px">More before &amp; afters <svg><use href="#i-arrow"/></svg></a>
      </div>
    </div>
  </div>
</section>

<section class="section light">
  <div class="wrap">
    <div class="split">
      <div class="split__media" data-reveal>
        <img src="assets/img/office.jpg" alt="A technician repairing a dent on a silver sedan in an office parking lot" loading="lazy" width="1600" height="1062">
        <div class="split__badge"><b>0 trips</b>to a body shop</div>
      </div>
      <div data-reveal>
        <span class="eyebrow">We come to you</span>
        <h2>Fixed while you're at work.</h2>
        <p class="lede">Leave the keys at the front desk, or don't. A lot of PDR work can be done with the car locked. You go to your meeting and we go to work on the door.</p>
        <div class="places">
          <div class="place"><svg><use href="#i-home"/></svg>Your driveway</div>
          <div class="place"><svg><use href="#i-building"/></svg>Office lots</div>
          <div class="place"><svg><use href="#i-garage"/></svg>Apartment garages</div>
          <div class="place"><svg><use href="#i-car"/></svg>Dealer lots</div>
          <div class="place"><svg><use href="#i-truck"/></svg>Fleet yards</div>
          <div class="place"><svg><use href="#i-key"/></svg>Lease returns</div>
        </div>
        <a href="how-it-works.html" class="btn btn--ink btn--lg" style="margin-top:28px">How a visit works <svg><use href="#i-arrow"/></svg></a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="stats" data-reveal-stagger>
      <div class="stat"><b><span data-count="14000">14,000</span><em>+</em></b><span>dents pushed out since 2014</span></div>
      <div class="stat"><b><span data-count="4.9">4.9</span><em>&#9733;</em></b><span>average from 600+ reviews</span></div>
      <div class="stat"><b>&lt;<span data-count="60">60</span><em>m</em></b><span>for most single door dings</span></div>
      <div class="stat"><b><span data-count="10">10</span></b><span>towns covered across the valley</span></div>
    </div>
  </div>
</section>

<section class="section light">
  <div class="wrap">
    <div class="head" data-reveal>
      <div><span class="eyebrow">Reviews</span><h2>People who never left the house.</h2></div>
      <p class="lede">Rated 4.9 from more than 600 reviews, mostly from people who had a dent fixed somewhere they were already going to be.</p>
    </div>
    """ + reviews(3) + """
  </div>
</section>
""" + CTA)

SVC_ROWS = [
    ("pdr", "tools.jpg", "Paintless Dent Repair", "The dent comes out and the paint stays.",
     "This is most of what we do. We set up the light board, find the low spots, and push them out from behind with steel rods, or pull them from the front with glue tabs where there's no access behind. Your factory paint stays, so there's nothing to match and nothing that fades differently in five years.",
     ["Door dings and parking-lot dents", "Creases and body-line dents", "Larger dents up to the size of a dinner plate, as long as the paint is intact", "Lifetime guarantee for as long as you own the car"],
     [("Time", "30 to 90 min a dent"), ("Paint", "untouched"), ("Guarantee", "lifetime")]),
    ("hail", "hail.jpg", "Hail Damage Repair", "Every dimple, one at a time.",
     "Hail repair is PDR at volume. We map every dent under the light, write a line-item estimate your insurer can read, and work through the car over a day or three in your driveway or garage.",
     ["Estimates written under the light, dent by dent", "We talk to your adjuster so you don't have to", "Roof, hood, trunk and every panel between"],
     [("Time", "1 to 3 days"), ("Insurance", "all carriers"), ("Paint", "untouched")]),
    ("dent-paint", "crease-before.jpg", "Dent + Paint Repair", "For the dents PDR can't finish.",
     "If the paint is cracked or chipped, pushing the metal out isn't enough. We pull the panel as close to straight as the metal allows, use the thinnest skim of filler we can get away with, and spot refinish just that area with paint mixed to your color code. It's still done in your driveway.",
     ["Cracked or chipped paint over a dent", "Deep creases where the metal has stretched", "Honest call up front if PDR alone won't do it"],
     [("Time", "usually 1 day"), ("Method", "pull + spot refinish"), ("Color", "matched to code")]),
    ("clear-coat", "clearcoat.jpg", "Clear Coat Repair", "Peeling, chalky, or scratched through.",
     "Clear coat fails first where the sun hits hardest: roofs, hoods, pillars. We sand back the failed area, re-clear it, and blend into the good paint around it so you can't see where the repair starts. Scratches that haven't gone through the clear can often be polished out instead.",
     ["Peeling or flaking clear coat", "Key scratches and deep scratches", "Spot refinish and blend, not a full panel repaint"],
     [("Time", "half day to 1 day"), ("Method", "sand, re-clear, blend")]),
    ("correction", "polish.jpg", "Paint Correction", "Polish out the swirls and the depth comes back.",
     "Automatic car washes and dry towels leave fine circular scratches that make paint look gray in sunlight. We measure the paint thickness first, then machine polish in one to three stages to level out the swirls without cutting too deep.",
     ["Swirl marks and wash marring", "Haze, oxidation and water spotting", "Paint depth measured before we polish"],
     [("Time", "1 to 2 days"), ("Stages", "1 to 3")]),
    ("scuff", "bumper.jpg", "Bumper Scuff &amp; Scratch Repair", "Fix the corner, not the whole bumper.",
     "Garage walls, parking posts and tight drive-thrus all go for the same bumper corners. We repair the scuffed plastic, prime it, and refinish that area color-matched to your car. Nothing comes off the car.",
     ["Corner scuffs and scrapes", "Small cracks in plastic bumpers", "Color matched to your paint code"],
     [("Time", "2 to 4 hours")]),
    ("wheels", "wheel.jpg", "Curb Rash &amp; Headlights", "The small stuff that drags a car down.",
     "Scraped rims get sanded, filled and refinished on the car, and most wheels take about an hour. If you've got a machined face that needs a lathe, we'll tell you before you book. While we're there, we can restore yellowed headlights and seal them with a UV coat so they stay clear.",
     ["Curb rash on painted and powder-coated wheels", "Headlight restoration with UV seal", "Common add-ons for lease returns"],
     [("Wheels", "about 1 hr each"), ("Headlights", "about 1 hr a pair")]),
    ("protect", "ceramic.jpg", "Ceramic Coating &amp; Paint Film", "Keep it the way we left it.",
     "Once the dents are gone and the paint is corrected, protection makes sense. A ceramic coating adds gloss and makes washing easy. Clear paint protection film goes on the front bumper, hood edge and mirrors, which are the parts that take the rock chips.",
     ["Ceramic coating, one-step or multi-year", "Paint protection film on high-impact areas", "Best done right after a correction"],
     [("Time", "1 to 2 days"), ("Lasts", "years")]),
]


ALTS = {"wheels": "Refinishing curb rash on an alloy wheel", "dent-paint": "A long crease dent across a gray quarter panel", "pdr": "Paintless dent repair rods, glue tabs and tools laid out on a mat"}


def svc_rows():
    out = []
    for n, (sid, img, title, h, body, ticks, facts) in enumerate(SVC_ROWS, 1):
        t = "".join(f'<li><svg><use href="#i-check"/></svg>{x}</li>' for x in ticks)
        f = "".join(f"<span>{k}: <b>{v}</b></span>" for k, v in facts)
        more = '<a href="hail.html" class="btn btn--ghost">The full hail process <svg><use href="#i-arrow"/></svg></a>' if sid == "hail" else '<a href="quote.html" class="btn btn--lime"><svg><use href="#i-camera"/></svg>Quote this repair</a>'
        out.append(f"""<article class="row" id="{sid}">
  <div class="row__media" data-reveal><img src="assets/img/{img}" alt="{ALTS.get(sid, title.replace('&amp;', 'and') + ' in progress')}" loading="lazy" width="1400" height="930"><span class="row__num">{n:02d}</span></div>
  <div data-reveal>
    <span class="eyebrow">{title}</span>
    <h2>{h}</h2>
    <p class="lede">{body}</p>
    <ul class="ticks">{t}</ul>
    <div class="facts">{f}</div>
    {more}
  </div>
</article>""")
    return "".join(out)


PAGES["services.html"] = (
    "Services | Linewright Mobile Dent Co.",
    "Paintless dent repair, hail repair, dent and paint repair, clear coat repair, paint correction, bumper scuffs, curb rash, headlights and ceramic coating, all done at your location.",
    """<section class="hero hero--page">
  <div class="hero__media"><img src="assets/img/van.jpg" alt="An open service van at a curb with dent repair tools racked inside" width="1600" height="905" fetchpriority="high"></div>
  <div class="hero__inner">
    <div>
      <span class="eyebrow">Services</span>
      <h1>The whole shop, in one van.</h1>
      <p class="lede">Rods, glue pullers, light boards, polishers, paint, a generator. Everything we need to fix your car where it's parked is already on board.</p>
      <div class="hero__actions"><a href="quote.html" class="btn btn--lime btn--lg"><svg><use href="#i-camera"/></svg>Get a photo quote</a><a href="#compare" class="btn btn--ghost btn--lg">PDR vs. body shop</a></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap"><div class="rows">""" + svc_rows() + """</div></div>
</section>

<section class="section light" id="compare">
  <div class="wrap">
    <div class="head" data-reveal>
      <div><span class="eyebrow">Why PDR first</span><h2>PDR vs. a body shop.</h2></div>
      <p class="lede">When the paint is intact, paintless repair is usually faster and cheaper, and it keeps your original finish. When it isn't, we'll tell you.</p>
    </div>
    <div class="table-scroll" data-reveal>
      <table class="compare">
        <thead><tr><th scope="col">&nbsp;</th><th scope="col" class="us">Linewright PDR</th><th scope="col">Traditional body shop</th></tr></thead>
        <tbody>
          <tr><td>Where it happens</td><td class="us">Your driveway or office lot</td><td>Their shop, after a drop-off</td></tr>
          <tr><td>Typical door ding</td><td class="us">Under an hour</td><td>Days, depending on the paint queue</td></tr>
          <tr><td>Your factory paint</td><td class="us">Stays on the car</td><td>Sanded, filled and repainted</td></tr>
          <tr><td>Color match risk</td><td class="us">None, nothing is painted</td><td>Possible, especially on metallics</td></tr>
          <tr><td>Rental car needed</td><td class="us">No</td><td>Often</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section" id="fleet">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media" data-reveal><img src="assets/img/van.jpg" alt="The Linewright van parked with its side door open" loading="lazy" width="1600" height="905"><div class="split__badge"><b>Every other Friday</b>standing fleet visits</div></div>
      <div data-reveal>
        <span class="eyebrow">Fleet, dealers &amp; lease returns</span>
        <h2>Standing visits for lots and fleets.</h2>
        <p class="lede">Dealers call us for reconditioning before cars hit the front line. Fleet managers book a standing day at the yard. Leaseholders call the week before turn-in. We schedule around you, and nobody drives anything anywhere.</p>
        <ul class="ticks"><li><svg><use href="#i-check"/></svg>Wholesale pricing for dealers and fleets</li><li><svg><use href="#i-check"/></svg>One invoice for the whole lot, itemized by vehicle</li><li><svg><use href="#i-check"/></svg>Lease-return walkarounds before the inspector sees it</li></ul>
        <a href="quote.html" class="btn btn--lime btn--lg"><svg><use href="#i-truck"/></svg>Set up a lot visit</a>
      </div>
    </div>
  </div>
</section>
""" + CTA)

PAGES["hail.html"] = (
    "Hail Damage Repair | Linewright Mobile Dent Co.",
    "Mobile hail damage repair with paintless dent repair. Line-item estimates, we work with your adjuster, and the repair happens in your driveway.",
    """<section class="hero hero--page hero--hail">
  <div class="hero__media"><img src="assets/img/hail.jpg" alt="A black hood covered in hail dents, the reflected stripes rippling around each one" width="1600" height="1062" fetchpriority="high"></div>
  <canvas class="hail-canvas" aria-hidden="true"></canvas>
  <div class="hero__inner">
    <div>
      <span class="eyebrow">Hail damage repair</span>
      <h1>Hail hit. Don't rush to the first tent.</h1>
      <p class="lede">After a storm, pop-up repair tents show up in every parking lot. Take a breath. Your claim isn't going anywhere, and the right repair keeps your factory paint and the value of your car.</p>
      <div class="hero__actions"><a href="quote.html" class="btn btn--lime btn--lg"><svg><use href="#i-camera"/></svg>Book a hail estimate</a><a href="tel:+11234567890" class="btn btn--ghost btn--lg"><svg><use href="#i-phone"/></svg>123-456-7890</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head" data-reveal>
      <div><span class="eyebrow">Claim to clean</span><h2>How a hail repair goes.</h2></div>
      <p class="lede">Most hail cars take one to three days, and all of it happens at your home.</p>
    </div>
    <div class="steps" data-reveal-stagger>
      <div class="step"><span class="step__n">01</span><h3>File the claim</h3><p>Call your insurer and get a claim number. Snap a few photos of the roof and hood while you're at it.</p></div>
      <div class="step"><span class="step__n">02</span><h3>Estimate under the light</h3><p>We come out, put every panel under the light board and count the dents. You get a line-item estimate.</p></div>
      <div class="step"><span class="step__n">03</span><h3>We talk to the adjuster</h3><p>We send the estimate to your insurer and sort out any supplements directly with the adjuster.</p></div>
      <div class="step"><span class="step__n">04</span><h3>Repair at home</h3><p>We work through the car in your driveway or garage. You pay your deductible, and the insurer pays the rest.</p></div>
    </div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="ba-wrap">
      <div data-reveal>""" + ba("hood-before.jpg", "hood-after.jpg", "a black hood covered in hail dents", "Hail hood") + """<p class="ba-cap">Same hood, same light. Drag to see every dimple come out.</p></div>
      <div data-reveal>
        <span class="eyebrow">Why PDR for hail</span>
        <h2>Your factory paint stays on.</h2>
        <ul class="ticks">
          <li><svg><use href="#i-check"/></svg><span>Nothing is sanded or repainted, so a buyer's paint gauge won't find anything later.</span></li>
          <li><svg><use href="#i-check"/></svg><span>Body shops get buried after a storm. We work at your place, on your schedule, and most cars are done in a few days.</span></li>
          <li><svg><use href="#i-check"/></svg><span>We do every panel, including the rails and the small pillar dents that tents tend to skip.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section light">
  <div class="wrap">
    <div class="split">
      <div data-reveal>
        <span class="eyebrow">Right after a storm</span>
        <h2>The 5-minute storm checklist.</h2>
        <ul class="ticks">
          <li><svg><use href="#i-check"/></svg>Photograph the roof, hood and trunk in daylight, at an angle</li>
          <li><svg><use href="#i-check"/></svg>Check the glass and lights. Cracked glass gets reported separately</li>
          <li><svg><use href="#i-check"/></svg>Call your insurer and write down the claim number</li>
          <li><svg><use href="#i-check"/></svg>Don't sign anything at a parking-lot tent until you've compared estimates</li>
          <li><svg><use href="#i-check"/></svg>Send us the photos, and we'll tell you honestly whether it's a PDR job</li>
        </ul>
        <p class="note"><strong>About deductibles:</strong> you pay your deductible and the insurer pays the approved repair. If anyone offers to "cover" or waive your deductible, walk away. In many states that's insurance fraud, and you're the one who signs the claim.</p>
      </div>
      <div class="split__media" data-reveal><img src="assets/img/hood-before.jpg" alt="Hail dents on a black hood under a light board" loading="lazy" width="1400" height="1045"><div class="split__badge"><b>1 to 3 days</b>for most hail cars</div></div>
    </div>
  </div>
</section>
""" + CTA)

PAGES["results.html"] = (
    "Before &amp; After | Linewright Mobile Dent Co.",
    "Before and after photos of mobile paintless dent repair, crease repair and hail repair, plus reviews from Linewright customers.",
    """<section class="hero hero--page">
  <div class="hero__media"><img src="assets/img/door-after.jpg" alt="A white car door with perfectly straight reflected lines after repair" width="1400" height="1045" fetchpriority="high"></div>
  <div class="hero__inner">
    <div>
      <span class="eyebrow">Before &amp; after</span>
      <h1>Straight lines don't lie.</h1>
      <p class="lede">A dent can hide in plain daylight. Under a light board it can't. Every before and after here is the same panel under the same light, so you're seeing the metal itself, not a nicer photo angle.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="ba-grid" data-reveal-stagger>
      <div>""" + ba("door-before.jpg", "door-after.jpg", "a white car door with a round ding", "Door ding") + """<h3>Door ding, pearl white</h3><p>Gym-lot door ding. 40 minutes in an office parking lot.</p></div>
      <div>""" + ba("crease-before.jpg", "crease-after.jpg", "a gray quarter panel with a long crease", "Crease") + """<h3>Quarter-panel crease</h3><p>Shopping-cart crease across a body line. About two hours.</p></div>
      <div>""" + ba("hood-before.jpg", "hood-after.jpg", "a black hood covered in hail dents", "Hail hood") + """<h3>Hail hood, gloss black</h3><p>Part of a full hail car finished over two days in a garage.</p></div>
    </div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="head" data-reveal>
      <div><span class="eyebrow">On the job</span><h2>Wherever the car is.</h2></div>
      <p class="lede">Most of our work happens in driveways, office lots and apartment garages.</p>
    </div>
    <div class="wall" data-reveal>
      <figure><img src="assets/img/hero.jpg" alt="Working a door dent at sunset in a driveway" loading="lazy" width="1920" height="1086"><figcaption>Driveway, golden hour</figcaption></figure>
      <figure><img src="assets/img/tech.jpg" alt="A Linewright technician beside the service van" loading="lazy" width="1400" height="1750"><figcaption>The van is the shop</figcaption></figure>
      <figure><img src="assets/img/polish.jpg" alt="Half-corrected black hood, swirls on one side and a mirror finish on the other" loading="lazy" width="1400" height="930"><figcaption>Paint correction, 50/50</figcaption></figure>
      <figure><img src="assets/img/headlight.jpg" alt="Headlight half yellowed and half restored" loading="lazy" width="1400" height="930"><figcaption>Headlight restoration</figcaption></figure>
      <figure><img src="assets/img/office.jpg" alt="Dent repair in an office parking lot" loading="lazy" width="1600" height="1062"><figcaption>Office lot, mid-meeting</figcaption></figure>
      <figure><img src="assets/img/wheel.jpg" alt="Refinishing curb rash on an alloy wheel" loading="lazy" width="1400" height="930"><figcaption>Curb rash</figcaption></figure>
      <figure><img src="assets/img/ceramic.jpg" alt="Water beading on ceramic-coated blue paint" loading="lazy" width="1400" height="930"><figcaption>Ceramic coating</figcaption></figure>
      <figure><img src="assets/img/clearcoat.jpg" alt="Spot-repairing failed clear coat on a red roof pillar" loading="lazy" width="1400" height="930"><figcaption>Clear coat repair</figcaption></figure>
      <figure><img src="assets/img/bumper.jpg" alt="Repairing a scuffed bumper corner" loading="lazy" width="1400" height="930"><figcaption>Bumper corner</figcaption></figure>
    </div>
  </div>
</section>

<section class="section light">
  <div class="wrap">
    <div class="head" data-reveal>
      <div><span class="eyebrow">Reviews</span><div class="rating"><b>4.9</b><div><div class="review__stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</div><span style="color:var(--text-2)">from 600+ reviews</span></div></div></div>
      <p class="lede">A lot of these customers never saw us arrive. They came back from a meeting, a workout or a nap to a car with straight lines.</p>
    </div>
    """ + reviews(6) + """
  </div>
</section>
""" + CTA)

towns_li = "".join(f"<li>{t}</li>" for t in TOWNS)
# stylised area map: rings + town dots (no real geography)
DOTS = [(260, 260, "Harlow Springs"), (180, 200, "Cedar Hollow"), (340, 170, "Brightmoor"), (370, 300, "Kessling Park"), (150, 320, "Larkfield"),
        (290, 425, "Ostrander Hills"), (415, 222, "Millpond"), (110, 250, "Westvale"), (150, 395, "Dunmore Flats"), (405, 352, "Ridgecrest")]
dots = "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#CCFF3D"/><text x="{x + 11}" y="{y + 4}" font-family="IBM Plex Mono, monospace" font-size="13" fill="#C9D0D9">{n}</text>' for x, y, n in DOTS)
MAP = f"""<svg viewBox="0 0 520 520" role="img" aria-label="Map of the ten Harlow Valley towns we cover, all within about 25 miles">
  <g fill="none" stroke="#263040"><circle cx="260" cy="260" r="80"/><circle cx="260" cy="260" r="160"/><circle cx="260" cy="260" r="240" stroke-dasharray="4 6"/></g>
  <g stroke="#1A222D">{''.join(f'<line x1="0" y1="{y}" x2="520" y2="{y}"/>' for y in range(20, 520, 40))}</g>
  <circle cx="260" cy="260" r="160" fill="rgba(204,255,61,.05)"/>
  {dots}
  <text x="260" y="500" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="12" fill="#97A1AE">~25 MILE RADIUS · FARTHER BY ARRANGEMENT</text>
</svg>"""

FAQ = [
    ("Do you have a shop I can bring the car to?", "No. We're fully mobile, which is the whole idea. Everything we need is in the van, including our own power, so all we need is your car and a little space around it."),
    ("What hours are you open?", "We don't keep storefront hours because there's no storefront. We book by appointment and fit around your day: early mornings, lunch breaks, while you're at work. Send photos and we'll find a time."),
    ("How do I know if my dent can be fixed without paint?", "If the paint isn't cracked, chipped or flaking, there's a good chance PDR will work. Sharp creases and stretched metal can be harder. Send three photos and we'll tell you honestly, before you book."),
    ("Do I need to be there?", "Not usually. For PDR we often work with the car locked. For paint work, or when we need a door opened, we'll ask you to leave a key with someone or be around at the start."),
    ("What about bad weather?", "Dent work isn't affected much by weather, and a garage or covered parking spot is ideal. Paint, clear coat and ceramic work need dry conditions and moderate temperatures, so we'll move those if rain or cold moves in."),
    ("Do you work with insurance?", "Yes. For hail, and for any claim, we write the estimate, send it to your insurer and work directly with the adjuster. You pay your deductible, and nothing else gets waived or hidden."),
    ("What does the lifetime guarantee cover?", "If a dent we repaired with PDR comes back or shows a flaw for as long as you own the car, we'll come back and fix it at no charge. Paint work carries its own warranty, which we spell out on your quote."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
faq_schema = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(
    '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q, a.replace('"', '\\"')) for q, a in FAQ) + "]}</script>\n"

PAGES["how-it-works.html"] = (
    "How It Works | Linewright Mobile Dent Co.",
    "How mobile dent repair with Linewright works: send photos, get a fixed quote, and we fix the car at your home or office. Service area and FAQ.",
    faq_schema + """<section class="hero hero--page">
  <div class="hero__media"><img src="assets/img/tech.jpg" alt="A Linewright technician standing beside the open service van" width="1400" height="1750" style="object-position:50% 30%" fetchpriority="high"></div>
  <div class="hero__inner">
    <div>
      <span class="eyebrow">How it works</span>
      <h1>You send photos. We bring the shop.</h1>
      <p class="lede">You don't drop the car off, sit in a waiting room or rent anything. A visit starts with three photos and ends with a walkaround under the light.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="steps" data-reveal-stagger>
      <div class="step"><span class="step__n">01</span><h3>Send three photos</h3><p>Straight on, at an angle and from a few steps back. Upload them on our quote page, or just text them.</p></div>
      <div class="step"><span class="step__n">02</span><h3>Get a fixed price</h3><p>Usually the same day. If it needs paint, or if PDR won't fully fix it, we'll say so in the quote.</p></div>
      <div class="step"><span class="step__n">03</span><h3>Pick the place</h3><p>Home, work, the gym, an apartment garage. Any spot where the car can sit for the job works.</p></div>
      <div class="step"><span class="step__n">04</span><h3>Check the lines, then pay</h3><p>We put the repaired panel back under the light board with you. You pay once you're happy with it.</p></div>
    </div>
  </div>
</section>

<section class="section light">
  <div class="wrap">
    <div class="split">
      <div class="split__media" data-reveal><img src="assets/img/van.jpg" alt="The service van, side door open, tools racked inside" loading="lazy" width="1600" height="905"><div class="split__badge"><b>Self-powered</b>no outlet needed</div></div>
      <div data-reveal>
        <span class="eyebrow">What we need from you</span>
        <h2>A parking spot. That's about it.</h2>
        <ul class="ticks">
          <li><svg><use href="#i-check"/></svg><span><strong>A few feet around the car</strong> so we can set the light board up beside it.</span></li>
          <li><svg><use href="#i-check"/></svg><span><strong>Permission to work there.</strong> Most offices and HOAs are fine with it, but check if you're not sure.</span></li>
          <li><svg><use href="#i-check"/></svg><span><strong>Dry weather for paint jobs.</strong> PDR can happen under a carport in the rain. Paint and coatings can't.</span></li>
          <li><svg><use href="#i-check"/></svg><span><strong>No power, water or tools.</strong> The van brings everything.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="area">
  <div class="wrap">
    <div class="area">
      <div class="area__map" data-reveal>""" + MAP + """</div>
      <div data-reveal>
        <span class="eyebrow">Service area</span>
        <h2>All ten towns in the valley.</h2>
        <p class="lede">We cover the whole Harlow Valley, roughly 25 miles out from Harlow Springs. Farther out, fleets and multi-car jobs are worth the drive, so just ask.</p>
        <ul class="towns">""" + towns_li + """</ul>
      </div>
    </div>
  </div>
</section>

<section class="section light" id="faq">
  <div class="wrap">
    <div class="head" data-reveal>
      <div><span class="eyebrow">FAQ</span><h2>Questions people ask first.</h2></div>
      <p class="lede">Don't see yours? Text it to 123-456-7890 along with a photo of the dent.</p>
    </div>
    <div class="faq" data-reveal>""" + faq_html + """</div>
  </div>
</section>
""" + CTA)

chip = lambda name, val, label, icon, typ="checkbox": f'<label class="chip"><input type="{typ}" name="{name}" value="{val}"><span><svg><use href="#i-{icon}"/></svg>{label}</span></label>'

PAGES["quote.html"] = (
    "Get a Photo Quote | Linewright Mobile Dent Co.",
    "Upload photos of your dent, scratch or hail damage and get a fixed mobile repair quote from Linewright, usually the same day.",
    """<section class="hero hero--page" style="min-height:56svh">
  <div class="hero__media"><img src="assets/img/door-before.jpg" alt="A door ding showing as bent reflected stripes on a white door" width="1400" height="1045" fetchpriority="high"></div>
  <div class="hero__inner">
    <div>
      <span class="eyebrow">Photo quote</span>
      <h1>Show us the dent.</h1>
      <p class="lede">Three photos and a ZIP code is all we need to send you a real price. No one comes out until you say yes.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:60px">
  <div class="wrap">
    <div class="quote">
      <form class="form" data-demo-form novalidate>
        <fieldset>
          <legend><b>1</b>Photos of the damage</legend>
          <label class="drop">
            <input type="file" name="photos" accept="image/*" multiple>
            <span><svg><use href="#i-upload"/></svg><b data-count-label>Tap to add photos</b><small>Straight on, at an angle, and from a few steps back</small></span>
          </label>
          <div class="thumbs" aria-live="polite"></div>
        </fieldset>
        <fieldset>
          <legend><b>2</b>What happened?</legend>
          <div class="chips">""" + chip("damage", "ding", "Door ding", "car") + chip("damage", "crease", "Crease or big dent", "tool") + chip("damage", "hail", "Hail", "hail") + chip("damage", "paint", "Scratch or chipped paint", "spray") + chip("damage", "clear", "Peeling clear coat", "layers") + chip("damage", "scuff", "Bumper scuff", "car") + chip("damage", "wheel", "Curb rash", "wheel") + chip("damage", "headlight", "Hazy headlights", "bulb") + chip("damage", "correction", "Swirls / dull paint", "sun") + chip("damage", "protect", "Ceramic or film", "drop") + """</div>
        </fieldset>
        <fieldset>
          <legend><b>3</b>Where will the car be?</legend>
          <div class="chips">""" + chip("where", "home", "Home", "home", "radio") + chip("where", "work", "Work", "building", "radio") + chip("where", "apartment", "Apartment garage", "garage", "radio") + chip("where", "lot", "Dealer or fleet lot", "truck", "radio") + """</div>
          <div class="grid2" style="margin-top:14px">
            <div class="field"><label for="q-zip">ZIP code</label><input id="q-zip" name="zip" inputmode="numeric" autocomplete="postal-code" placeholder="5-digit ZIP"></div>
            <div class="field"><label for="q-when">Best days</label><select id="q-when" name="when"><option>As soon as possible</option><option>Weekdays</option><option>Weekends</option><option>I'm flexible</option></select></div>
          </div>
        </fieldset>
        <fieldset>
          <legend><b>4</b>About you &amp; the car</legend>
          <div class="grid2">
            <div class="field"><label for="q-name">Name</label><input id="q-name" name="name" autocomplete="name"></div>
            <div class="field"><label for="q-phone">Mobile number</label><input id="q-phone" name="phone" type="tel" autocomplete="tel"></div>
            <div class="field"><label for="q-email">Email</label><input id="q-email" name="email" type="email" autocomplete="email"></div>
            <div class="field"><label for="q-car">Year, make &amp; model</label><input id="q-car" name="car" placeholder="e.g. 2022 midsize SUV"></div>
          </div>
          <div class="field" style="margin-top:14px"><label for="q-notes">Anything else?</label><textarea id="q-notes" name="notes" placeholder="Insurance claim? Lease turn-in date? Gate code?"></textarea></div>
        </fieldset>
        <button class="btn btn--lime btn--lg btn--block" type="submit"><svg><use href="#i-camera"/></svg>Send for a quote</button>
        <div class="form__ok" data-form-ok hidden tabindex="-1"><b>Got it.</b> This is a sample site, so nothing was sent. On the real site, the photos would go straight to the tech's phone and you'd get a price back, usually the same day.</div>
      </form>
      <aside class="side">
        <div class="side__box">
          <h3>What happens next</h3>
          <ol><li>A tech looks at your photos, not a call center.</li><li>You get a fixed price by text, usually the same day.</li><li>Pick a time and a place. We show up there.</li><li>You pay after you've seen the lines straight.</li></ol>
        </div>
        <div class="side__box">
          <h3>Photo tips from the techs</h3>
          <div class="tip"><svg><use href="#i-sun"/></svg><span>Shoot in shade or on a cloudy day. Direct sun hides dents.</span></div>
          <div class="tip"><svg><use href="#i-swap"/></svg><span>Angle the phone so a straight line, like a garage door edge or a roofline, reflects across the dent. Where that line bends shows us the size.</span></div>
          <div class="tip"><svg><use href="#i-camera"/></svg><span>Add one photo from a few steps back so we can see which panel it is.</span></div>
        </div>
        <div class="side__box">
          <h3>Rather just text?</h3>
          <p style="color:var(--muted);margin-bottom:14px">Send the same three photos to our number and we'll reply with a price.</p>
          <a href="sms:+11234567890" class="btn btn--ghost btn--block"><svg><use href="#i-msg"/></svg>Text 123-456-7890</a>
        </div>
      </aside>
    </div>
  </div>
</section>
""")

for name, (title, desc, body) in PAGES.items():
    img = {"hail.html": "hail.jpg", "services.html": "van.jpg", "results.html": "door-after.jpg"}.get(name, "hero.jpg")
    html = head(title, desc, name, img) + header(name if name != "quote.html" else "") + body + FOOTER
    (OUT / name).write_text(html, encoding="utf-8", newline="\n")
    print("wrote", name, len(html))
