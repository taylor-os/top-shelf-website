"""Guard for the CRM + website focus (spec 2026-11-21-crm-website-focus-design.md).

Fails while any page or page source still sells a removed plan or price, links to
a removed page, carries the old nav, or leaves a removed URL without a 301.
"""
import glob
import html
import json
import os
import re

import focus_catalog as cat

TAG_RE = re.compile(r"<[^>]+>")
BLOCK_RE = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.S | re.I)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


META_RE = re.compile(r'<meta\s+(?:name|property)="(?:description|og:description|og:title|twitter:title|twitter:description)"\s+content="([^"]*)"', re.I)


def visible_text(page_html):
    """Visible text plus the meta descriptions/titles search results and shares show."""
    metas = " . ".join(META_RE.findall(page_html))
    text = TAG_RE.sub(" ", BLOCK_RE.sub(" ", page_html)) + " . " + metas
    return re.sub(r"\s+", " ", html.unescape(text))


def sentences(text):
    return re.split(r"(?<=[.!?])\s+", text)


def rel(path):
    return os.path.relpath(path, cat.ROOT).replace("\\", "/")


def offenders(pattern, skip_sentences=()):
    found = []
    for page in cat.site_pages():
        for s in sentences(visible_text(read(page))):
            if pattern.search(s) and s.strip() not in skip_sentences:
                found.append("%s: %s" % (rel(page), s.strip()[:140]))
    for src in cat.source_files():
        for n, line in enumerate(read(src).splitlines(), 1):
            if pattern.search(line):
                found.append("%s:%d: %s" % (rel(src), n, line.strip()[:140]))
    return found


def test_no_old_prices():
    bad = offenders(cat.OLD_PRICE_RE, set(cat.ALLOWED_CONTEXTS))
    assert not bad, "%d old prices:\n%s" % (len(bad), "\n".join(bad[:60]))


def test_no_old_names():
    bad = offenders(cat.OLD_NAME_RE)
    assert not bad, "%d old plan/offer names:\n%s" % (len(bad), "\n".join(bad[:60]))


def test_removed_files_gone():
    left = [p for p in cat.REMOVED if os.path.exists(os.path.join(cat.ROOT, p))]
    assert not left, "still on disk: %s" % left


def htaccess_rules():
    exact, patterns = {}, []
    for line in read(os.path.join(cat.ROOT, ".htaccess")).splitlines():
        parts = line.split()
        if len(parts) == 4 and parts[0] == "Redirect" and parts[1] == "301":
            exact[parts[2]] = parts[3]
        elif len(parts) == 4 and parts[0] == "RedirectMatch" and parts[1] == "301":
            patterns.append((re.compile(parts[2]), parts[3]))
    return exact, patterns


def redirect_target(url_path, exact, patterns):
    if url_path in exact:
        return exact[url_path]
    for rx, target in patterns:
        m = rx.match(url_path)
        if m:
            return re.sub(r"\$(\d)", lambda g: m.group(int(g.group(1))), target)
    return None


def target_exists(target):
    path = target.split("#")[0].split("?")[0].lstrip("/") or "index.html"
    return os.path.exists(os.path.join(cat.ROOT, path))


def test_every_removed_url_redirected():
    exact, patterns = htaccess_rules()
    bad = []
    for path, want in cat.REMOVED.items():
        got = redirect_target("/" + path, exact, patterns)
        if got is None:
            bad.append("no 301: /%s" % path)
        elif not target_exists(got):
            bad.append("/%s -> %s (target missing)" % (path, got))
    assert not bad, "%d redirect problems:\n%s" % (len(bad), "\n".join(bad[:60]))


LINK_RE = re.compile(r'(?:href|src)="([^"]+)"')


def test_internal_links_resolve():
    bad = []
    for page in cat.site_pages():
        # links built inside <script> (JS string templates) are not real hrefs
        for url in LINK_RE.findall(re.sub(r"<script\b.*?</script>", " ", read(page), flags=re.S | re.I)):
            if re.match(r"^(https?:|mailto:|tel:|sms:|#|data:|javascript:|//)", url):
                continue
            path = html.unescape(url).split("#")[0].split("?")[0]
            if not path:
                continue
            path = path.lstrip("/") or "index.html"
            if path.endswith("/"):
                path += "index.html"
            if not os.path.exists(os.path.join(cat.ROOT, path)):
                bad.append("%s -> %s" % (rel(page), url))
    assert not bad, "%d broken links:\n%s" % (len(bad), "\n".join(bad[:60]))


SOL_RE = re.compile(r'class="nav-link">Solutions.*?<div class="nav-dropdown">(.*?)</div>', re.S)
CTA_RE = re.compile(r'<div class="nav-cta">(.*?)</div>', re.S)


def test_nav_is_new():
    want = [href for href, _ in cat.NEW_SOLUTIONS]
    bad = []
    for page in cat.site_pages():
        src = read(page)
        if 'id="nav"' not in src:
            continue
        m = SOL_RE.search(src)
        got = re.findall(r'href="([^"]+)"', m.group(1)) if m else None
        if got != want:
            bad.append("%s: solutions %s" % (rel(page), got))
        c = CTA_RE.search(src)
        gold = re.search(r'<a href="([^"]+)" class="btn btn-gold btn-sm">([^<]+)</a>', c.group(1)) if c else None
        if not gold or gold.group(1) != cat.CTA_HREF or gold.group(2).strip() != cat.CTA_LABEL:
            bad.append("%s: cta %s" % (rel(page), gold.groups() if gold else None))
        if "Get Free Audit" in src:
            bad.append("%s: still says Get Free Audit" % rel(page))
    assert not bad, "%d nav problems:\n%s" % (len(bad), "\n".join(bad[:60]))


LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def walk_prices(node, out):
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("price", "lowPrice", "highPrice") and not isinstance(v, (dict, list)):
                out.append(str(v))
            else:
                walk_prices(v, out)
    elif isinstance(node, list):
        for v in node:
            walk_prices(v, out)


def test_jsonld_prices():
    ok = {"99", "199", "50", "499"}
    bad = []
    for page in cat.site_pages():
        for block in LD_RE.findall(read(page)):
            try:
                data = json.loads(block)
            except ValueError:
                bad.append("%s: unparseable JSON-LD" % rel(page))
                continue
            prices = []
            walk_prices(data, prices)
            for p in prices:
                norm = p.replace("$", "").replace(",", "")
                norm = norm[:-3] if norm.endswith(".00") else norm
                if norm not in ok:
                    bad.append("%s: price %s" % (rel(page), p))
    assert not bad, "%d JSON-LD price problems:\n%s" % (len(bad), "\n".join(bad[:60]))


def test_sitemap_has_no_removed():
    sm = read(os.path.join(cat.ROOT, "sitemap.xml"))
    left = [p for p in cat.REMOVED if "/" + p + "<" in sm]
    assert not left, "sitemap still lists: %s" % left


def test_no_generator_emits_removed():
    """No page source names a removed page, so a regenerated site can't bring one back."""
    bad = []
    for src in cat.source_files():
        text = read(src)
        for path in cat.REMOVED:
            slug = path.rsplit(".", 1)[0]
            # a one-word slug ("preview") is also an ordinary folder name, so require the extension
            ext = r'(\.html|\.pdf)' if "-" not in slug else r'(\.html|\.pdf)?'
            if re.search(r'["\'/]%s%s["\']' % (re.escape(slug), ext), text):
                bad.append("%s names %s" % (rel(src), path))
    assert not bad, "%d sources still name removed pages:\n%s" % (len(bad), "\n".join(bad[:60]))


SIGNATURE_FEATURES = [
    "CRM", "AI receptionist", "missed-call text-back", "online booking", "dispatch board",
    "customer hub", "invoice by text", "review requests", "review replies", "on-my-way texts",
    "estimates", "card payments", "AI chatbot",
]


def test_pricing_page():
    src = read(os.path.join(cat.ROOT, "pricing.html"))
    text = visible_text(src)
    low = text.lower()
    missing = [w for w in ("$99", "$199", "Call for pricing", "$50", "per line", "$499", cat.CTA_LABEL)
               if w not in text]
    missing += [f for f in SIGNATURE_FEATURES if f.lower() not in low]
    assert not missing, "pricing.html is missing: %s" % missing
    assert 'id="website"' in src, "pricing.html needs id=\"website\" (the 301 target for old website pages)"
    banned = [w for w in ("Essentials", "Platinum", "Get Found", "page website") if w.lower() in low]
    assert not banned, "pricing.html still says: %s" % banned


LEAD_FIELDS = {"name", "business", "email", "phone", "city", "state", "gbp", "need",
               "page", "industry", "sms_consent", "source"}


def test_form_fields():
    src = read(os.path.join(cat.ROOT, "contact.html"))
    m = re.search(r'<form\b([^>]*)>(.*?)</form>', src, re.S)
    assert m, "contact.html has no form"
    attrs, form = m.groups()
    assert 'action="https://top-shelf-production.up.railway.app/api/website-lead"' in attrs
    fields = {}
    for tag in re.findall(r'<(?:input|select|textarea)\b[^>]*>', form):
        name = re.search(r'\bname="([^"]+)"', tag)
        if name:
            fields[name.group(1)] = tag
    extra = set(fields) - LEAD_FIELDS
    assert not extra, "form sends fields the lead endpoint does not take: %s" % sorted(extra)
    assert "gbp" not in fields, "the Google Business Profile field is gone from the Try the CRM form"
    for req in ("name", "phone"):
        assert req in fields and re.search(r'\brequired\b', fields[req]), "%s must be required" % req
    assert "email" in fields and not re.search(r'\brequired\b', fields["email"]), "email must be optional"
    assert re.search(r'name="source"\s+value="try-crm"', form), "hidden source must be try-crm"
    users = re.search(r'<select\b[^>]*id="users"[^>]*>(.*?)</select>', form, re.S)
    assert users, "a users select (id=users) is required"
    assert re.findall(r'value="([^"]*)"', users.group(1)) == ["1-10", "11-25", "26+"]
    # the users choice has no field of its own: it rides inside need ("Users: 11-25")
    script = src[m.end():]
    assert re.search(r"need:\s*'Users: '\s*\+\s*users", script), "users must be folded into need"


def test_crm_by_industry():
    page = os.path.join(cat.ROOT, "crm-by-industry.html")
    assert os.path.exists(page)
    src = read(page)
    refs = set(re.findall(r'assets/img/crm/industries/[\w-]+/[\w-]+\.webp', src))
    assert len(refs) == 72, len(refs)  # 12 industries x 6 screens (vet added 2026-11-27)
    missing = [r for r in refs if not os.path.exists(os.path.join(cat.ROOT, r))]
    assert not missing, missing
    assert "Sample screens" in src
    no_link = [os.path.basename(p) for p in sorted(glob.glob(os.path.join(cat.ROOT, "industry-*.html")))
               if not p.endswith("industry-custom.html") and 'href="crm-by-industry.html#' not in read(p)]
    assert not no_link, no_link


JS_COMMENT_RE = re.compile(r"/\*.*?\*/|(?<!:)//[^\n]*", re.S)  # (?<!:) keeps https:// in strings
JS_BANNED_RE = re.compile(r"SEO report|Local SEO|Map Pack|Google Business Profile|deep-dive|\baudit\b|—|&mdash;", re.I)


def test_site_scripts_sell_nothing_removed():
    """assets/*.js (gap quiz, chat assistant) must not sell SEO/audits or use em dashes.

    Comments are stripped first: only strings a visitor can see count.
    """
    bad = []
    for path in sorted(glob.glob(os.path.join(cat.ROOT, "assets", "*.js"))):
        code = JS_COMMENT_RE.sub("", read(path))
        for line in code.splitlines():
            for m in JS_BANNED_RE.finditer(line):
                bad.append("%s: %r in %s" % (rel(path), m.group(0), line.strip()[:120]))
    assert not bad, "%d hits:\n%s" % (len(bad), "\n".join(bad[:40]))


def test_gap_quiz_shows_no_dollars_and_sends_contact():
    """Owner 2026-11-26: no dollar estimates in the Gap Finder; and the lead must carry email/phone the CRM accepts."""
    js = read(os.path.join(cat.ROOT, "assets", "gap-quiz.js"))
    assert "showDollars: false" in js
    assert "monthly:" not in js, "per-symptom dollar figures came back"
    assert "/mo<" not in js and "a year, a rough estimate" not in js
    assert "email:isEmail?contact:''" in js and "phone:isEmail?'':contact" in js, "quiz lead must send email/phone, not 'contact'"
    for demo in ("gap-finder-demo.html", "gap-map-demo.html"):
        s = read(os.path.join(cat.ROOT, demo))
        assert "showDollars: false" in s or "showDollars:false" in s, demo
        assert "Your likely gap is" not in s and "a year, a rough estimate" not in s, demo
        assert "\x01" not in s, demo


# ---- 2026-11-27 site update: industry pair cards, "See your business" pop-up, CRM page ----
PAIRS = json.load(open(os.path.join(cat.ROOT, "renders-src", "industry-crm", "pairs.json"), encoding="utf-8"))
CONTENT = json.load(open(os.path.join(cat.ROOT, "renders-src", "site-content", "content.json"), encoding="utf-8"))

# Images other tasks are still making (2026-11-27). The cards point at them already;
# delete each line once its file lands. Nothing else may be missing.
PENDING_IMAGES = {
    "assets/img/websites/bramlett-motor-co-home-d.webp",
    "assets/img/websites/larkspur-strength-club-home-d.webp",
    "assets/img/websites/kestrel-lane-detail-home-d.webp",
    "assets/img/crm/industries/vet/1-today-d.webp",  # vet has no captions.json entry yet
}


def test_cards_link_pairs():
    src = read(os.path.join(cat.ROOT, "index.html"))
    sec = re.search(r'<section class="c-sec" id="industries".*?</section>', src, re.S).group(0)
    cards = re.findall(r'<li class="c-pair\b.*?</li>', sec, re.S)
    assert len(cards) == 12, len(cards)
    bad = []
    for card, p in zip(cards, PAIRS):
        if html.escape(p["business"], quote=False) not in card:
            bad.append("card out of order or missing %s" % p["business"])
        if "Sample website &middot; Sample CRM" not in card:
            bad.append("%s: no sample label" % p["business"])
        web = "assets/img/websites/%s-home-d.webp" % os.path.basename(p["website_dir"])
        if 'src="%s"' % web not in card:
            bad.append("%s: no website shot" % p["business"])
        if 'src="assets/img/crm/industries/%s/' % p["slug"] not in card:
            bad.append("%s: no CRM screen" % p["business"])
        want = p["industry_page"] + ("#" + p["industry_anchor"] if p["industry_anchor"] else "")
        if 'href="%s"' % want not in card or 'href="%s/index.html"' % p["website_dir"] not in card:
            bad.append("%s: industry or website link missing" % p["business"])
        for url in re.findall(r'(?:href|src)="([^"]+)"', card):
            path = html.unescape(url).split("#")[0]
            if path not in PENDING_IMAGES and not os.path.exists(os.path.join(cat.ROOT, path)):
                bad.append("%s -> %s missing" % (p["business"], url))
    assert not bad, "\n".join(bad)


def test_popup_replaced():
    loaders, old = [], []
    for path in glob.glob(os.path.join(cat.ROOT, "**", "*.html"), recursive=True):
        if rel(path).split("/")[0] in ("demo", "websites", "preview", "node_modules"):
            continue
        s = read(path)
        if "gap-quiz.js" in s:
            old.append(rel(path))
        if "assets/see-your-business.js?v=20261127a" in s:
            loaders.append(rel(path))
    assert not old, "%d pages still load gap-quiz.js: %s" % (len(old), old[:10])
    assert len(loaders) >= 684, len(loaders)
    for page in ("index.html", "solution-crm.html", "solution-websites-seo.html", "pricing.html"):
        assert page in loaders, page
    js = read(os.path.join(cat.ROOT, "assets", "see-your-business.js"))
    assert "See your business" in js and 'role="dialog"' in js and "Escape" in js
    assert os.path.exists(os.path.join(cat.ROOT, "assets", "gap-quiz.js")), "keep gap-quiz.js in the repo"
    for p in PAIRS:
        assert json.dumps(p["business"], ensure_ascii=False) in js, "pop-up is missing %s" % p["business"]


def test_crm_page_answers():
    text = visible_text(read(os.path.join(cat.ROOT, "solution-crm.html")))
    questions = [qa["q"] for qa in CONTENT["crm"]["faq"]]
    missing = [q for q in questions if q not in text]
    assert not missing, "FAQ questions missing: %s" % missing
    # The FAQ asks "Does it connect to QuickBooks?" and "Is it available in Spanish?" and
    # answers without claiming either, so the questions themselves are taken out first.
    rest = text
    for q in questions:
        rest = rest.replace(q, " ")
    claims = [w for w in ("Apple Pay", "tap to pay", "QuickBooks", "Spanish", "automatic review")
              if w.lower() in rest.lower()]
    assert not claims, "solution-crm.html claims: %s" % claims
