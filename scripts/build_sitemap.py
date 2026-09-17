#!/usr/bin/env python3
"""Regenerate sitemap.xml from the indexable pages actually on disk, with real
lastmod dates (file mtime). Replaces the hand-maintained sitemap that had stale
2026-07-25 dates and was missing /booking and the sample sites.

Excludes: noindex utility/demo pages, the 301'd review copy, the GSC
verification file, and everything under /demo/ (robots-disallowed).

Usage:  python scripts/build_sitemap.py   (from repo root)
"""
import os, glob, datetime

SITE = "https://www.topshelfsolutions.io"
# Top-level pages that must never appear in the sitemap.
EXCLUDE = {
    "gap-finder-demo.html", "gap-map-demo.html", "preview.html", "thank-you.html",
    "home-centered-review.html", "googled4807f62c9c00ace.html",
}


def lastmod(path: str) -> str:
    return datetime.date.fromtimestamp(os.path.getmtime(path)).isoformat()


def loc_and_priority(fname: str):
    """(url, priority, changefreq) for a top-level page filename."""
    if fname == "index.html":
        return f"{SITE}/", "1.0", "weekly"
    if fname == "booking.html":
        return f"{SITE}/booking", "0.8", "weekly"
    stem = fname[:-5]
    if fname == "privacy.html":
        return f"{SITE}/{fname}", "0.3", "yearly"
    if fname in ("pricing.html", "contact.html", "why-us.html", "sample-report.html"):
        pr = "0.6" if fname == "sample-report.html" else "0.8"
        return f"{SITE}/{fname}", pr, "weekly"
    if stem.startswith(("industry-", "solution-")):
        return f"{SITE}/{fname}", "0.7", "weekly"
    return f"{SITE}/{fname}", "0.5", "monthly"   # any other indexable top-level page


def entries():
    rows = []
    for f in sorted(glob.glob("*.html")):
        if f in EXCLUDE:
            continue
        url, pr, cf = loc_and_priority(f)
        rows.append((url, lastmod(f), cf, pr))
    # The 9 sample sites under /websites/ are FICTIONAL demos and are noindex
    # (owner decision 2026-09-17: no fake companies competing in search), so
    # they are deliberately kept OUT of the sitemap.
    return rows


def main():
    rows = entries()
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, lm, cf, pr in rows:
        lines.append(f'  <url><loc>{url}</loc><lastmod>{lm}</lastmod>'
                     f'<changefreq>{cf}</changefreq><priority>{pr}</priority></url>')
    lines.append('</urlset>\n')
    with open("sitemap.xml", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"wrote sitemap.xml with {len(rows)} URLs")


if __name__ == "__main__":
    main()
