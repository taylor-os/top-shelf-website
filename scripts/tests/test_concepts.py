"""Guards for the design concepts in preview/concepts-2026-11/<id>/ (A, B, C, D).

Every concept carries the same information (renders-src/site-content/content.json) and the
same 12 industry pairs (renders-src/industry-crm/pairs.json); only the design differs.
"""
import glob
import json
import os
import re

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = os.path.join(ROOT, "preview", "concepts-2026-11")
PAIRS = json.load(open(os.path.join(ROOT, "renders-src", "industry-crm", "pairs.json"), encoding="utf-8"))
CONCEPTS = sorted(d for d in os.listdir(BASE) if os.path.isdir(os.path.join(BASE, d))) if os.path.isdir(BASE) else []
OLD_PRICES = re.compile(r"\$(299|899|2,500|599|795|1,995|345|1,250|1,500|495)\b")


def pages(cid):
    return sorted(glob.glob(os.path.join(BASE, cid, "**", "*.html"), recursive=True))


def visible(html):
    html = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S)
    return re.sub(r"<[^>]+>", " ", html)


@pytest.mark.parametrize("cid", CONCEPTS)
def test_concept_has_every_page(cid):
    root = os.path.join(BASE, cid)
    need = ["index.html", "crm.html", "websites.html", "industries.html"]
    for p in PAIRS:
        need += [f"industries/{p['slug']}-crm.html", f"industries/{p['slug']}-website.html"]
    missing = [n for n in need if not os.path.isfile(os.path.join(root, n))]
    assert not missing, f"{cid} missing {missing}"


@pytest.mark.parametrize("cid", CONCEPTS)
def test_concept_pages_follow_rules(cid):
    bad = []
    for f in pages(cid):
        s = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, BASE)
        if 'name="robots" content="noindex' not in s:
            bad.append(f"{rel}: not noindex")
        t = visible(s)
        if "—" in t or "&mdash;" in s:
            bad.append(f"{rel}: em dash")
        if OLD_PRICES.search(t):
            bad.append(f"{rel}: old price")
        for href in re.findall(r'(?:href|src)="([^"#?]+)', s):
            if href.startswith(("http", "mailto:", "tel:", "data:", "//")):
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(f), href))
            if not os.path.exists(target):
                bad.append(f"{rel}: broken {href}")
    assert not bad, "\n".join(bad[:40])


@pytest.mark.parametrize("cid", CONCEPTS)
def test_concept_prices_and_pairs(cid):
    root = os.path.join(BASE, cid)
    allt = " ".join(visible(open(f, encoding="utf-8").read()) for f in pages(cid))
    for price in ("$99", "$199", "$50", "$499"):
        assert price in allt, f"{cid} never shows {price}"
    for p in PAIRS:
        crm = visible(open(os.path.join(root, "industries", f"{p['slug']}-crm.html"), encoding="utf-8").read())
        assert p["business"].replace("&", "&") in crm or p["business"].replace("&", "&amp;") in crm, f"{cid}/{p['slug']}-crm names its business"
