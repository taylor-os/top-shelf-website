#!/usr/bin/env python3
"""Technical-SEO hygiene for the sample websites under /websites/<slug>/.
These are FICTIONAL demo sites built to show Top Shelf's build quality, so we
add only NEUTRAL technical tags that assert nothing false: a self-canonical,
og:url, Twitter Card tags mirroring the existing Open Graph, and an absolute
og:image / twitter:image (the pages ship a relative og:image that social
scrapers can't resolve). We deliberately do NOT add LocalBusiness / Review /
Rating / FAQ schema to fictional businesses — that would be fabricated
structured data. Idempotent: only missing tags are added.

Usage:  python scripts/sample_site_seo.py            # all 45 pages
        python scripts/sample_site_seo.py websites/everline-home-services/index.html
Run from repo root.
"""
import sys, re, glob, os

SITE = "https://www.topshelfsolutions.io"


def page_url(path: str) -> str:
    rel = path.replace("\\", "/")
    if rel.endswith("/index.html"):
        return f"{SITE}/{rel[:-len('index.html')]}"   # .../<slug>/
    return f"{SITE}/{rel}"


def base_dir(path: str) -> str:
    rel = path.replace("\\", "/").rsplit("/", 1)[0]
    return f"{SITE}/{rel}/"


def meta(src: str, prop: str, attr: str = "property") -> str | None:
    m = re.search(rf'<meta {attr}="{re.escape(prop)}"[^>]*content="([^"]*)"', src)
    return m.group(1) if m else None


def absolutize(url: str, base: str) -> str:
    if not url or url.startswith(("http://", "https://", "//")):
        return url
    return base + url.lstrip("./")


def process(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    if "<title>" not in src or "</head>" not in src:
        return f"skip   {path}  (no head/title)"
    url, base = page_url(path), base_dir(path)
    add = []

    if 'rel="canonical"' not in src:
        add.append(f'<link rel="canonical" href="{url}">')
    if 'property="og:url"' not in src:
        add.append(f'<meta property="og:url" content="{url}">')

    # Absolutize a relative og:image in place (scrapers need an absolute URL).
    og_img = meta(src, "og:image")
    if og_img and not og_img.startswith(("http://", "https://", "//")):
        abs_img = absolutize(og_img, base)
        src = src.replace(f'<meta property="og:image" content="{og_img}">',
                          f'<meta property="og:image" content="{abs_img}">', 1)
        og_img = abs_img

    if 'name="twitter:' not in src:
        title = meta(src, "og:title") or re.search(r'<title>(.*?)</title>', src, re.DOTALL).group(1).strip()
        desc = meta(src, "og:description") or meta(src, "description", "name") or ""
        tw = ['<meta name="twitter:card" content="summary_large_image">',
              f'<meta name="twitter:title" content="{title}">']
        if desc:
            tw.append(f'<meta name="twitter:description" content="{desc}">')
        if og_img:
            tw.append(f'<meta name="twitter:image" content="{og_img}">')
        add += tw

    if not add:
        return f"ok     {path}  (already complete)"

    block = "\n".join(add)
    src = src.replace("</title>", "</title>\n" + block, 1)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(src)
    return f"ok     {path}  (+{len(add)} tags)"


def main(argv):
    files = argv or sorted(glob.glob("websites/*/*.html"))
    for f in files:
        if os.path.isfile(f):
            print(process(f))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
