"""New nav, footer and main button on every page. Re-runnable.

Solutions menu and footer column = focus_catalog.NEW_SOLUTIONS; the gold nav
button and every audit call to action become "Try the CRM" (to contact.html,
the request form). The CRM Demo walkthrough link stays.
"""
import html
import re

import focus_catalog as cat

NAV_SOL_RE = re.compile(r'(class="nav-link">Solutions <span class="nav-arrow">&#9662;</span></a>\s*<div class="nav-dropdown">)(.*?)(\n\s*</div>)', re.S)
FOOT_SOL_RE = re.compile(r'(<p class="footer-col-title">Solutions</p>\s*<div class="footer-links">)(.*?)(\n\s*</div>)', re.S)
FOOT_CO_RE = re.compile(r'(<p class="footer-col-title">Company</p>\s*<div class="footer-links">)(.*?)(\n\s*</div>)', re.S)
GOLD_RE = re.compile(r'<a href="[^"]*" class="btn btn-gold btn-sm">[^<]*</a>')

COMPANY = [("pricing.html", "Pricing"), ("why-us.html", "Why Top Shelf"),
           ("switching-from-hibu-thryv.html", "Switching from Hibu/Thryv"),
           (cat.CTA_HREF, cat.CTA_LABEL), ("contact.html", "Contact"), ("privacy.html", "Privacy Policy")]

# Audit calls to action -> Try the CRM (exact link/button texts from a census of the site)
CTA_TEXTS = [
    ("Get a free audit of your business", "Try the CRM for your business"),
    ("Get your free business audit", "Try the CRM"),
    ("Get Your Free Business Audit", "Try the CRM"),
    ("Free business audit", "Try the CRM"),
    ("Get Your Free Audit", "Try the CRM"),
    ("Get a Free Audit", "Try the CRM"),
    ("Get a free audit", "Try the CRM"),
    ("Get My Free Audit", "Try the CRM"),
    ("Book My Free Audit", "Try the CRM"),
    ("Request Your Free Audit", "Try the CRM"),
    ("Get your free audit", "Try the CRM"),
    ("Get Free Audit", "Try the CRM"),
]


def links(items, indent):
    return "".join('\n%s<a href="%s">%s</a>' % (indent, href, html.escape(label, quote=False)) for href, label in items)


def _swap(rx, items, indent):
    def fn(m):
        return m.group(1) + links(items, indent) + m.group(3)
    return lambda s: rx.sub(fn, s)


def rewrite_chrome(s):
    s = _swap(NAV_SOL_RE, cat.NEW_SOLUTIONS, "          ")(s)
    s = _swap(FOOT_SOL_RE, cat.NEW_SOLUTIONS, "          ")(s)
    s = _swap(FOOT_CO_RE, COMPANY, "          ")(s)
    s = GOLD_RE.sub('<a href="%s" class="btn btn-gold btn-sm">%s</a>' % (cat.CTA_HREF, cat.CTA_LABEL), s)
    for old, new in CTA_TEXTS:
        # only as a whole link/button/heading text: between > and < (an arrow span may follow)
        s = re.sub(r">(\s*)%s(\s*)(<|&rarr;)" % re.escape(old), lambda m: ">%s%s%s%s" % (m.group(1), new, m.group(2), m.group(3)), s)
    return s


def main():
    for page in cat.site_pages():
        src = open(page, encoding="utf-8").read()
        out = rewrite_chrome(src)
        if out != src:
            open(page, "w", encoding="utf-8", newline="").write(out)


if __name__ == "__main__":
    main()
