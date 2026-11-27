"""Add "CRM by Industry" as the first link of the Industries nav dropdown and the
footer Industries column on every top-level page. Re-runnable: a page that
already has the link is left alone.

Usage:  python scripts/add_crm_by_industry_nav.py   (from repo root)
"""
import re

import focus_catalog as cat

LINK = '<a href="crm-by-industry.html">CRM by Industry</a>'
NAV_RE = re.compile(r'(class="nav-link">Industries <span class="nav-arrow">&#9662;</span></a>\s*<div class="nav-dropdown">)(\s*)(?=<a href="industry-home-services\.html">)')
FOOT_RE = re.compile(r'(<p class="footer-col-title">Industries</p>\s*<div class="footer-links">)(\s*)(?=<a href="industry-home-services\.html">)')


def add_link(s):
    for rx in (NAV_RE, FOOT_RE):
        m = rx.search(s)
        if m and LINK not in s[m.end():m.end() + 400]:
            s = s[:m.end(1)] + m.group(2) + LINK + s[m.end(1):]
    return s


def main():
    changed = 0
    for page in cat.site_pages():
        with open(page, encoding="utf-8", newline="") as fh:
            s = fh.read()
        new = add_link(s)
        if new != s:
            with open(page, "w", encoding="utf-8", newline="") as fh:
                fh.write(new)
            changed += 1
    print("pages changed:", changed)


if __name__ == "__main__":
    main()
