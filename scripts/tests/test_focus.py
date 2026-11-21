"""Guard for the CRM + website focus (spec 2026-11-21-crm-website-focus-design.md).

Fails while any page or page source still sells a removed plan or price, links to
a removed page, carries the old nav, or leaves a removed URL without a 301.
"""
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
            if re.search(r'["\'/]%s(\.html|\.pdf)?["\']' % re.escape(slug), text):
                bad.append("%s names %s" % (rel(src), path))
    assert not bad, "%d sources still name removed pages:\n%s" % (len(bad), "\n".join(bad[:60]))
