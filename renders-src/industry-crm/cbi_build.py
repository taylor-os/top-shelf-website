"""Build crm-by-industry.html + the industry-page strips in the website worktree. Re-runnable."""
import html, pathlib, re, json

S = pathlib.Path(__file__).parent
W = pathlib.Path(r"C:\Users\taylo\top-shelf-website-focus")
IMG = W / "assets/img/crm/industries"
# mk_board2 copies files on import, so parse the IND literal instead of running it
src = (S / "mk_board2.py").read_text(encoding="utf-8")
IND = eval(src[src.index("IND = [") + 6: src.index("\n]\n", src.index("IND = [")) + 2])

e = lambda s: html.escape(s, quote=True)
SITE = "https://www.topshelfsolutions.io"
PAGE = {"home-services": "industry-home-services.html", "car-lots": "industry-auto.html",
        "auto-repair": "industry-auto.html", "auto-detailing": "industry-auto.html",
        "real-estate": "industry-real-estate.html", "fitness": "industry-salon-spa-fitness.html",
        "salon-spa": "industry-salon-spa-fitness.html", "restaurants": "industry-restaurants.html",
        "medical-dental": "industry-medical-dental.html", "legal": "industry-legal.html",
        "retail": "industry-retail.html"}
MORE = {"home-services": "home services", "car-lots": "auto businesses", "auto-repair": "auto businesses",
        "auto-detailing": "auto businesses", "real-estate": "real estate agents",
        "fitness": "salons, spas and gyms", "salon-spa": "salons, spas and gyms",
        "restaurants": "restaurants and bars", "medical-dental": "medical and dental offices",
        "legal": "law firms", "retail": "retail and local shops"}


def files(slug):
    return sorted(p.name for p in (IMG / slug).glob("*.webp"))


def img(slug, fn, alt, lazy=True, cls=""):
    w, h = (1440, 900) if fn.endswith("-d.webp") else (585, 1266)
    return (f'<img src="assets/img/crm/industries/{slug}/{fn}" width="{w}" height="{h}"'
            f'{" loading=\"lazy\"" if lazy else ""} decoding="async" alt="{e(alt)}"{cls}>')


def device(slug, fn, alt, link=False):
    inner = img(slug, fn, alt)
    if link:
        inner = (f'<a href="assets/img/crm/industries/{slug}/{fn}" target="_blank" rel="noopener" '
                 f'aria-label="Open this screen full size in a new tab">{inner}</a>')
    if fn.endswith("-d.webp"):
        return f'<div class="cbi-lap"><div class="cbi-win">{inner}</div><div class="cbi-lap-base" aria-hidden="true"></div></div>'
    return f'<div class="cbi-phone">{inner}</div>'


# ---------------------------------------------------------------- the page
def section(slug, name, biz, why, caps):
    fns = files(slug)
    assert len(fns) == 6, slug
    biz_name, city = [x.strip() for x in biz.split("·")]
    figs, btns = [], []
    for i, (fn, (role, cap)) in enumerate(zip(fns, caps)):
        fid = f"{slug}-s{i + 1}"
        alt = f"{role} screen for {biz_name}, a sample business: {cap}"
        figs.append(f'<figure class="cbi-shot" id="{fid}"{"" if i == 0 else " hidden"}>'
                    f'<div class="cbi-dev">{device(slug, fn, alt, link=True)}</div>'
                    f'<figcaption><b>{e(role)}</b> {e(cap)}</figcaption></figure>')
        btns.append(f'<button type="button" class="cbi-btn" aria-controls="{fid}" aria-pressed="{"true" if i == 0 else "false"}">'
                    f'<span class="cbi-role">{e(role)}</span><span class="cbi-cap">{e(cap)}</span></button>')
    return f'''
<section class="cbi-sec rule-top" id="{slug}" aria-labelledby="{slug}-h">
  <div class="container">
    <div class="cbi-head">
      <span class="eyebrow reveal">Sample business: {e(biz_name)}, {e(city)}</span>
      <h2 class="display display-lg reveal" id="{slug}-h">{e(name)}</h2>
      <p class="reveal">{e(why)}</p>
    </div>
    <div class="cbi-viewer" data-viewer>
      <div class="cbi-stage">
        <span class="cbi-sample">Sample screens</span>
        {"".join(figs)}
      </div>
      <div class="cbi-list" role="group" aria-label="{e(name)} screens">
        {"".join(btns)}
      </div>
    </div>
    <p class="cbi-more"><a class="tlink" href="{PAGE[slug]}">More on Top Shelf for {MORE[slug]} <span class="arr">&rarr;</span></a></p>
  </div>
</section>'''


CSS = """
<style>
/* crm-by-industry: page-scoped. Device frames follow the homepage #cc .c-lap / .c-phone look. */
.cbi-note{display:inline-flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:.15rem .6rem;margin:2rem auto 0;padding:.55rem 1.1rem;border:1px solid var(--hairline-strong);border-radius:18px;font-size:.86rem;color:var(--ink-2);background:rgba(201,168,106,.05)}
.cbi-note b{color:var(--gold-bright);font-weight:600}
.cbi-chips{position:sticky;top:76px;z-index:50;background:var(--ground);border-block:1px solid var(--hairline)}
.cbi-chips .container{max-width:1320px;display:flex;gap:.45rem;align-items:center;overflow-x:auto;padding-block:.7rem;scrollbar-width:thin}
.cbi-chips a{flex:0 0 auto;display:inline-flex;align-items:center;min-height:38px;padding:0 .72rem;border:1px solid var(--hairline-strong);border-radius:999px;font-size:.8rem;color:var(--ink-2);white-space:nowrap;transition:color .3s,border-color .3s}
.cbi-chips a:hover,.cbi-chips a:focus-visible{color:var(--gold-bright);border-color:var(--gold)}
.cbi-sec{position:relative;z-index:2;padding-block:clamp(3.5rem,7vw,6rem);scroll-margin-top:200px}
.cbi-head{max-width:64ch;margin-bottom:clamp(1.8rem,3.5vw,2.6rem)}
.cbi-head .eyebrow{margin-bottom:1.2rem}
.cbi-head p{margin-top:1.1rem;color:var(--ink-2);line-height:1.7}
.cbi-viewer{display:grid;grid-template-columns:minmax(0,2.3fr) minmax(0,1fr);gap:clamp(1.5rem,3vw,2.75rem);align-items:start}
.cbi-stage{position:sticky;top:190px;min-width:0}
.cbi-sample{position:absolute;top:0;left:0;z-index:2;font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);padding:.3rem .65rem;border:1px solid var(--hairline-strong);border-radius:999px;background:rgba(11,9,6,.8)}
.cbi-shot[hidden]{display:none}
.cbi-dev{aspect-ratio:16/10.2;display:flex;align-items:center;justify-content:center;padding-top:2.2rem}
.cbi-dev a{display:block;border-radius:inherit}
.cbi-dev img{display:block;max-width:100%;height:auto}
.cbi-lap{width:100%}
.cbi-win{margin:0 6%;padding:7px 7px 10px;background:#060606;border-radius:13px 13px 3px 3px;box-shadow:0 0 0 1px rgba(201,168,106,.6),0 40px 80px -40px rgba(0,0,0,.9)}
.cbi-win img{border-radius:3px;width:100%}
.cbi-lap-base{position:relative;height:9px;margin-top:2px;background:linear-gradient(#2c2721,#120f0c 60%,#080706);border-top:1px solid rgba(201,168,106,.65);border-radius:1px 1px 12px 12px/1px 1px 8px 8px;box-shadow:0 30px 60px -22px rgba(201,168,106,.28)}
.cbi-lap-base::before{content:"";position:absolute;top:0;left:50%;transform:translateX(-50%);width:15%;height:3px;border-radius:0 0 7px 7px;background:#050505}
.cbi-phone{height:100%;padding:4px;border-radius:20px;background:#040404;box-shadow:0 0 0 1px rgba(201,168,106,.75),0 36px 70px -28px rgba(0,0,0,.85)}
.cbi-phone a,.cbi-phone img{height:100%}
.cbi-phone img{width:auto;border-radius:16px}
.cbi-shot figcaption{display:none}
.cbi-list{display:flex;flex-direction:column;gap:.55rem}
.cbi-btn{display:block;width:100%;text-align:left;font:inherit;color:inherit;cursor:pointer;padding:.85rem 1rem .9rem 1.1rem;border:1px solid var(--hairline);border-left:2px solid var(--hairline);border-radius:var(--r-lg);background:rgba(233,228,218,.02);transition:border-color .3s,background-color .3s}
.cbi-btn:hover{border-color:var(--hairline-strong)}
.cbi-btn:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.cbi-btn[aria-pressed="true"]{border-color:var(--hairline-strong);border-left-color:var(--gold);background:rgba(201,168,106,.08)}
.cbi-role{display:block;font-size:.9rem;font-weight:600;color:var(--ink);letter-spacing:.01em}
.cbi-btn[aria-pressed="true"] .cbi-role{color:var(--gold-bright)}
.cbi-cap{display:block;margin-top:.3rem;font-size:.84rem;line-height:1.5;color:var(--ink-3)}
.cbi-more{margin-top:clamp(1.6rem,3vw,2.2rem)}
.cbi-price{margin-top:1.6rem;font-size:.95rem;color:var(--ink-2)}
.cbi-note-sub{margin-top:.8rem;font-size:.86rem;color:var(--ink-3)}
.cbi-yours{scroll-margin-top:200px}
.cbi-yours-box{max-width:820px;margin-inline:auto;text-align:center;padding:clamp(2rem,4.5vw,3.2rem) clamp(1.3rem,4vw,3rem);border:1px solid var(--hairline-strong);border-radius:var(--r-lg);background:linear-gradient(180deg,rgba(201,168,106,.07),rgba(201,168,106,.02))}
.cbi-yours-box .eyebrow{justify-content:center;margin-bottom:1.2rem}
.cbi-yours-box p{margin:1.1rem auto 0;max-width:58ch;color:var(--ink-2);line-height:1.7}
.cbi-yours-box .cbi-yours-price{color:var(--ink)}
.cbi-yours-box .cbi-yours-price b{color:var(--gold-bright);font-weight:600}
.cbi-yours-box .btn{margin-top:1.8rem}
@media (max-width:979px){
  .cbi-viewer{grid-template-columns:minmax(0,1fr)}
  .cbi-stage{position:relative;top:auto}
  .cbi-dev{aspect-ratio:auto;height:clamp(380px,115vw,560px)}
  .cbi-dev:has(.cbi-lap){height:auto}
  .cbi-shot figcaption{display:block;margin-top:1rem;font-size:.9rem;line-height:1.55;color:var(--ink-2);min-height:4.7em}
  .cbi-shot figcaption b{display:block;color:var(--gold-bright);font-weight:600}
  .cbi-list{flex-direction:row;overflow-x:auto;padding-bottom:.4rem;scroll-snap-type:x proximity}
  .cbi-btn{flex:0 0 auto;width:auto;min-height:44px;padding:.55rem .95rem;border-left-width:1px;border-radius:999px;scroll-snap-align:start}
  .cbi-btn[aria-pressed="true"]{border-left-color:var(--gold);border-color:var(--gold)}
  .cbi-role{font-size:.85rem;white-space:nowrap}
  .cbi-cap{display:none}
}
@media (min-width:980px){.cbi-dev{aspect-ratio:auto;height:clamp(460px,64vh,640px)}}
@media (prefers-reduced-motion:reduce){.cbi-btn,.cbi-chips a{transition:none}}
</style>"""

JS = """<script>
document.querySelectorAll('[data-viewer]').forEach(function (v) {
  var btns = v.querySelectorAll('.cbi-btn');
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      btns.forEach(function (o) {
        var on = o === b;
        o.setAttribute('aria-pressed', on ? 'true' : 'false');
        document.getElementById(o.getAttribute('aria-controls')).hidden = !on;
      });
      var list = b.parentNode;
      if (list.scrollWidth > list.clientWidth) list.scrollTo({ left: b.offsetLeft - list.offsetLeft - 8, behavior: 'smooth' });
    });
  });
});
</script>"""

TITLE = "The Top Shelf CRM, Built for Your Industry | Top Shelf"
DESC = ("Sample screens of the Top Shelf CRM set up for 11 kinds of business, including home services, "
        "car lots, salons, dental offices and law firms.")
URL = f"{SITE}/crm-by-industry.html"


def build_page():
    shell = (W / "solution-crm.html").read_text(encoding="utf-8")
    head_end = shell.index("<!-- Google tag")
    head = shell[:head_end]
    head = re.sub(r"<title>.*?</title>", f"<title>{e(TITLE)}</title>", head)
    head = re.sub(r'content="Stop losing customers[^"]*"', f'content="{e(DESC)}"', head)
    head = re.sub(r'content="CRM &amp; Follow-Up \| Top Shelf Business Solutions"', f'content="{e(TITLE)}"', head)
    head = head.replace(f"{SITE}/solution-crm.html", URL)
    gtag = shell[head_end:shell.index('<script type="application/ld+json">')]
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": "The Top Shelf CRM, Built for Your Industry",
           "url": URL, "description": DESC,
           "isPartOf": {"@type": "WebSite", "name": "Top Shelf Business Solutions", "url": SITE + "/"}},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
              {"@type": "ListItem", "position": 2, "name": "CRM by Industry", "item": URL}]}]
    nav_start = shell.index("<body>")
    nav = shell[nav_start:shell.index("<!-- ============================ PAGE HERO")]
    foot = shell[shell.index('<footer class="footer">'):]
    short = {"fitness": "Fitness", "restaurants": "Restaurants", "retail": "Retail"}
    chips = "".join(f'<a href="#{s}">{e(short.get(s, n))}</a>' for s, n, *_ in IND)
    secs = "".join(section(*row) for row in IND)
    body = f'''<!-- ============================ PAGE HERO ============================ -->
<section class="page-hero">
  <div class="container page-hero-inner">
    <span class="eyebrow reveal">CRM by Industry</span>
    <h1 class="display display-lg reveal">One CRM, Set Up <em>for Your Kind of Business</em></h1>
    <p class="page-hero-sub reveal">A dental office checks different things first than a car lot or a salon does. We set up the Top Shelf CRM around how your business runs: the owner&rsquo;s first screen of the day, the screens your staff work from, and the pages your customers open on their phones. Below are sample screens for 11 industries.</p>
    <p class="cbi-note reveal"><b>Sample screens</b> The businesses, people and numbers on this page are made up.</p>
    <p class="cbi-note-sub reveal">Your own CRM can look different. See below.</p>
    <div class="page-hero-actions reveal">
      <a href="contact.html" class="btn btn-gold">Try the CRM <span class="arr">&rarr;</span></a>
      <a href="tel:+14698333033" class="btn btn-line">Call or text (469) 833-3033</a>
    </div>
  </div>
</section>

<nav class="cbi-chips" aria-label="Jump to an industry">
  <div class="container">{chips}</div>
</nav>

<section class="cbi-sec cbi-yours" id="your-way" aria-labelledby="your-way-h">
  <div class="container">
    <div class="cbi-yours-box reveal">
      <span class="eyebrow">Your Own Setup</span>
      <h2 class="display display-lg" id="your-way-h">These Screens Are <em>a Starting Point</em></h2>
      <p>Your CRM does not have to look like these. We can change the layout and the screens to fit how your business runs. We can also build a custom CRM around your specific industry.</p>
      <p class="cbi-yours-price">Either way, it is the same Signature plan: <b>$99 a month for up to 10 users.</b></p>
      <a href="contact.html" class="btn btn-gold">Try the CRM <span class="arr">&rarr;</span></a>
    </div>
  </div>
</section>
{secs}

<!-- ============================ FINAL CTA ============================ -->
<section class="cta rule-top">
  <div class="container">
    <img src="assets/logo-mark.png?v=20260804b" alt="" class="cta-mark reveal">
    <span class="eyebrow reveal">Your Business, Your Setup</span>
    <h2 class="cta-title reveal">See It Set Up<br><em>for You</em></h2>
    <p class="cta-sub reveal">Tell us what kind of business you run and how you keep track of customers today. We can use the screens on this page, change them to fit you, or build a CRM around your industry. We call you, then send you a demo.</p>
    <div class="cta-actions reveal">
      <a href="contact.html" class="btn btn-gold">Try the CRM <span class="arr">&rarr;</span></a>
      <a href="tel:+14698333033" class="btn btn-line">Call or text (469) 833-3033</a>
    </div>
    <p class="cbi-price reveal">Any of these is the same Signature plan, $99 a month for up to 10 users.</p>
  </div>
</section>

'''
    foot = foot.replace('<script src="https://cdnjs', JS + '\n<script src="https://cdnjs', 1)
    out = (head + gtag + f'<script type="application/ld+json">{json.dumps(ld)}</script>\n' + CSS + "\n</head>\n"
           + nav + body + foot)
    (W / "crm-by-industry.html").write_text(out, encoding="utf-8", newline="\n")


# ---------------------------------------------------------------- industry strips
STRIP_CSS = """<style id="crm-strip-css">
.crm-strip{display:flex;gap:clamp(1rem,2.5vw,2rem);align-items:flex-end;justify-content:center}
.crm-strip .cbi-lap{flex:1 1 0;min-width:0;max-width:760px}
.crm-strip .cbi-phone{flex:0 0 auto;width:clamp(120px,13vw,165px);height:auto}
.crm-strip.crm-multi .cbi-lap{max-width:none}
.crm-strip figure{margin:0;min-width:0}
.crm-strip figcaption{margin-top:.9rem;font-size:.82rem;color:var(--ink-3);text-align:center}
.crm-strip figure.cbi-lapfig{flex:1 1 0}
.crm-strip img{display:block;width:100%;height:auto}
.cbi-win{margin:0 6%;padding:6px 6px 9px;background:#060606;border-radius:12px 12px 3px 3px;box-shadow:0 0 0 1px rgba(201,168,106,.6),0 40px 80px -40px rgba(0,0,0,.9)}
.cbi-win img{border-radius:3px}
.cbi-lap-base{position:relative;height:8px;margin-top:2px;background:linear-gradient(#2c2721,#120f0c 60%,#080706);border-top:1px solid rgba(201,168,106,.65);border-radius:1px 1px 12px 12px/1px 1px 8px 8px}
.cbi-lap-base::before{content:"";position:absolute;top:0;left:50%;transform:translateX(-50%);width:15%;height:3px;border-radius:0 0 7px 7px;background:#050505}
.cbi-phone{padding:4px;border-radius:20px;background:#040404;box-shadow:0 0 0 1px rgba(201,168,106,.75),0 36px 70px -28px rgba(0,0,0,.85)}
.cbi-phone img{border-radius:16px}
.crm-strip-foot{display:flex;flex-wrap:wrap;gap:.8rem 1.6rem;align-items:center;justify-content:center;margin-top:clamp(1.8rem,3.5vw,2.6rem)}
.crm-strip-way{margin:clamp(1.6rem,3vw,2.2rem) auto 0;max-width:60ch;text-align:center;color:var(--ink-2)}
.crm-strip-tag{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);padding:.3rem .65rem;border:1px solid var(--hairline-strong);border-radius:999px}
@media (max-width:760px){
  .crm-strip{flex-wrap:wrap}
  .crm-strip .cbi-lap,.crm-strip figure.cbi-lapfig{flex:1 1 100%}
  .crm-strip .cbi-phone{width:calc(50% - .6rem);max-width:200px}
}
</style>
"""

ROLE = {r[0]: {fn: cap for fn, cap in zip(files(r[0]), r[4])} for r in IND}
BIZ = {r[0]: [x.strip() for x in r[2].split("·")][0] for r in IND}
NAME = {r[0]: r[1] for r in IND}

INTRO = {
    "home-services": ("for Home Services", "Sample screens from Prairie Air &amp; Heat, a made-up heating and air company. The owner&rsquo;s morning on a laptop, a tech getting paid at the front door, and the estimate the homeowner picks from."),
    "real-estate": ("for Real Estate", "Sample screens for Elena Marsh, a made-up agent. Her day with contract deadlines first, a buyer&rsquo;s profile on her phone, and the listing page on her own website."),
    "restaurants": ("for Restaurants", "Sample screens from Wrenfield Kitchen &amp; Bar, a made-up restaurant. Tonight&rsquo;s covers and guest notes, a server&rsquo;s own tables, and the reservation page guests use."),
    "medical-dental": ("for Dental Offices", "Sample screens from Alderbrook Family Dental, a made-up practice. The dentist&rsquo;s day, the hygienist booking the next cleaning, and the family&rsquo;s own page. No health details show anywhere."),
    "legal": ("for Law Firms", "Sample screens from Holloway &amp; Vane Law, a made-up firm. What came in since Friday, what happened while the attorney was in court, and the client&rsquo;s own page. No case facts show anywhere."),
    "retail": ("for Local Shops", "Sample screens from Larkhaven Goods, a made-up shop. The owner&rsquo;s day, the customer card at the counter, and the page that tells a customer her order is in."),
}
STRIP_PICK = lambda slug: [f for f in files(slug) if f.endswith("-d.webp")][:1] + \
    [f for f in files(slug) if f.endswith("-m.webp")][:1] + [f for f in files(slug) if f.startswith("5-")]


def head_html(eyebrow, title, p):
    return f'''    <div class="section-head" style="text-align:center;max-width:64ch;margin-inline:auto">
      <span class="eyebrow reveal" style="justify-content:center">{eyebrow}</span>
      <h2 class="display display-lg reveal" style="margin-top:1.6rem">{title}</h2>
      <p class="reveal" style="margin-inline:auto">{p}</p>
    </div>'''


def alt_for(slug, fn):
    role, cap = ROLE[slug][fn]
    return f"{role}: {cap} Sample screen for {BIZ[slug]}, a made-up business."


def strip_single(slug):
    em, p = INTRO[slug]
    devs = "".join(device(slug, fn, alt_for(slug, fn)) for fn in STRIP_PICK(slug))
    return f'''<section class="section rule-top">
  <div class="container">
{head_html("See It for Your Business", f"What the CRM Looks Like <em>{em}</em>", p)}
    <div class="crm-strip reveal">{devs}</div>
    <p class="crm-strip-way reveal">Want it laid out your way? We can change the screens, or build one around your business. Same $99 a month for up to 10 users.</p>
    <div class="crm-strip-foot reveal"><span class="crm-strip-tag">Sample screens</span><a class="tlink" href="crm-by-industry.html#{slug}">See all the screens <span class="arr">&rarr;</span></a></div>
  </div>
</section>'''


def strip_multi(slugs, em, p):
    figs = "".join(
        f'<figure class="cbi-lapfig">{device(s, files(s)[0], alt_for(s, files(s)[0]))}'
        f'<figcaption>{e(NAME[s])} &middot; <a class="tlink" href="crm-by-industry.html#{s}">See all the screens <span class="arr">&rarr;</span></a></figcaption></figure>'
        for s in slugs)
    return f'''<section class="section rule-top">
  <div class="container">
{head_html("See It for Your Business", f"What the CRM Looks Like <em>{em}</em>", p)}
    <div class="crm-strip crm-multi reveal">{figs}</div>
    <p class="crm-strip-way reveal">Want it laid out your way? We can change the screens, or build one around your business. Same $99 a month for up to 10 users.</p>
    <div class="crm-strip-foot reveal"><span class="crm-strip-tag">Sample screens</span></div>
  </div>
</section>'''


CUSTOM = '''<section class="section rule-top">
  <div class="container">
    <div class="section-head" style="text-align:center;max-width:64ch;margin-inline:auto">
      <span class="eyebrow reveal" style="justify-content:center">Built Around Your Business</span>
      <h2 class="display display-lg reveal" style="margin-top:1.6rem">A CRM Built for <em>Your Industry</em></h2>
      <p class="reveal" style="margin-inline:auto">We can build a custom CRM around your specific industry, laid out around how your business runs. It is the same Signature plan, $99 a month for up to 10 users.</p>
    </div>
    <div class="reveal" style="display:flex;flex-wrap:wrap;gap:1rem 1.6rem;align-items:center;justify-content:center">
      <a href="contact.html" class="btn btn-gold">Try the CRM <span class="arr">&rarr;</span></a>
      <a class="tlink" href="crm-by-industry.html">See sample screens for 11 industries <span class="arr">&rarr;</span></a>
    </div>
  </div>
</section>'''

STRIPS = {
    **{f"industry-{s}.html": strip_single(s) for s in ("home-services", "real-estate", "restaurants", "medical-dental", "legal", "retail")},
    "industry-auto.html": strip_multi(["car-lots", "auto-repair", "auto-detailing"], "for Auto Businesses",
        "Car lots, repair shops and detailers each get their own setup. Here is the owner&rsquo;s home screen for three made-up businesses."),
    "industry-salon-spa-fitness.html": strip_multi(["salon-spa", "fitness"], "for Salons and Gyms",
        "A salon and a gym each get their own setup. Here is the owner&rsquo;s first screen for a made-up salon and a made-up gym."),
    "industry-custom.html": CUSTOM,
}
SLOT_RE = re.compile(r"<!-- crm-screens-slot -->(?:\n.*?<!-- /crm-screens-slot -->)?", re.S)


def build_strips():
    for page, block in STRIPS.items():
        p = W / page
        s = p.read_text(encoding="utf-8")
        assert s.count("<!-- crm-screens-slot -->") == 1, page
        s = SLOT_RE.sub(lambda m: "<!-- crm-screens-slot -->\n" + block + "\n<!-- /crm-screens-slot -->", s)
        if page != "industry-custom.html":
            s = re.sub(r'<style id="crm-strip-css">.*?</style>\n', "", s, flags=re.S)
            s = s.replace("</head>", STRIP_CSS + "</head>", 1)
        p.write_text(s, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    build_page()
    build_strips()
    print("ok")
