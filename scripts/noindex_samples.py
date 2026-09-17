#!/usr/bin/env python3
"""De-index the sample websites under /websites/<slug>/. They are FICTIONAL
demo businesses; the owner does not want fake companies competing in search
(2026-09-17). We add `<meta name="robots" content="noindex,follow">` so crawlers
still reach the pages (and see the directive) but drop them from the index; they
are also removed from sitemap.xml (see build_sitemap.py). We deliberately do NOT
robots-Disallow /websites/ — a disallowed page can't be crawled, so the noindex
would never be seen and stale links could keep it indexed. Canonical/OG/Twitter
tags stay (harmless, and still help when a demo link is shared to a prospect).

Idempotent: skips a page that already has a robots meta.
Usage:  python scripts/noindex_samples.py   (from repo root)
"""
import glob, re

TAG = '<meta name="robots" content="noindex,follow">'


def process(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    if re.search(r'<meta\s+name="robots"', src, re.IGNORECASE):
        return f"skip   {path}  (already has robots meta)"
    # Insert right after the canonical if present, else after <title>.
    if 'rel="canonical"' in src:
        src = re.sub(r'(<link rel="canonical"[^>]*>)', r'\1\n' + TAG, src, count=1)
    elif "</title>" in src:
        src = src.replace("</title>", "</title>\n" + TAG, 1)
    else:
        return f"ERROR  {path}  (no canonical or title)"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(src)
    return f"ok     {path}"


if __name__ == "__main__":
    for f in sorted(glob.glob("websites/*/*.html")):
        print(process(f))
