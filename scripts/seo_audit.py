#!/usr/bin/env python3
"""Ground-truth on-page + interconnection SEO audit for the main (top-level) pages.
Measures, does not guess: per-page title/meta/canonical/h1/OG/Twitter/JSON-LD, the
internal link graph (orphans, broken links, contextual cross-linking), and sitemap
accuracy. Re-run after fixes. Exit 1 if any blocking issue remains.

Usage: python scripts/seo_audit.py   (run from repo root)
"""
import os, re, json, glob, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SITE = "https://www.topshelfsolutions.io"

def read(p):
    return open(p, encoding="utf-8", errors="replace").read()

def strip_boilerplate(html):
    """Remove <head>, <nav id=nav>, <footer> so we see CONTENT links only."""
    h = re.sub(r"<head\b.*?</head>", "", html, flags=re.S | re.I)
    h = re.sub(r"<nav\b[^>]*>.*?</nav>", "", h, flags=re.S | re.I)
    h = re.sub(r"<footer\b[^>]*>.*?</footer>", "", h, flags=re.S | re.I)
    return h

def local_links(html):
    """internal .html targets (basename), ignoring anchors/external/mailto/tel."""
    out = []
    for href in re.findall(r'href="([^"]+)"', html):
        if href.startswith(("http", "mailto:", "tel:", "#", "javascript:")):
            continue
        path = href.split("#")[0].split("?")[0].strip()
        if not path:
            continue
        out.append(path)
    return out

# ---- classify top-level pages (GIT-TRACKED only = what actually deploys) ----
# Hostinger deploys the git repo; local-only/gitignored files (e.g. a scratch review
# copy) do NOT ship, so audit only tracked pages or we false-flag files that aren't live.
import subprocess
tracked = subprocess.run(["git", "ls-files", "*.html"], capture_output=True, text=True).stdout.split()
top = sorted(f for f in tracked if "/" not in f)  # top-level deployed pages only
pages = {}
for f in top:
    if f.startswith("google") and len(f) > 20:   # GSC verification file
        continue
    s = read(f)
    # noindex ONLY from the robots meta tag (not a whole-file "noindex" match, which
    # would wrongly exclude any page that merely mentions the word in body copy)
    noindex = bool(re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', s, re.I))
    pages[f] = {"html": s, "noindex": noindex}

indexable = [f for f in pages if not pages[f]["noindex"]]
noindexed = [f for f in pages if pages[f]["noindex"]]

# ---- per-page signals ----
def sig(f):
    s = pages[f]["html"]
    title = (re.search(r"<title>(.*?)</title>", s, re.S) or [None, ""])
    title = re.sub(r"\s+", " ", title[1]).strip() if hasattr(title, "__getitem__") else ""
    m = re.search(r"<title>(.*?)</title>", s, re.S)
    title = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    md = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]*)"', s, re.I)
    desc = md.group(1).strip() if md else ""
    can = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', s, re.I)
    canonical = can.group(1) if can else ""
    h1 = len(re.findall(r"<h1\b", s))
    og = {k: bool(re.search(r'<meta[^>]+property="og:%s"' % k, s, re.I)) for k in ["title", "description", "url", "image", "type"]}
    tw = bool(re.search(r'<meta[^>]+name="twitter:card"', s, re.I))
    lang = bool(re.search(r"<html[^>]+lang=", s, re.I))
    # json-ld
    types, invalid = [], 0
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            d = json.loads(blk)
            def collect(o):
                if isinstance(o, dict):
                    if "@type" in o: types.append(o["@type"] if isinstance(o["@type"], str) else ",".join(o["@type"]))
                    for v in o.values(): collect(v)
                elif isinstance(o, list):
                    for v in o: collect(v)
            collect(d)
        except Exception:
            invalid += 1
    content_links = local_links(strip_boilerplate(s))
    all_links = local_links(s)
    return dict(title=title, desc=desc, canonical=canonical, h1=h1, og=og, tw=tw,
                lang=lang, jsonld_types=types, jsonld_invalid=invalid,
                content_links=content_links, all_links=all_links)

S = {f: sig(f) for f in indexable}

issues = {"BLOCK": [], "WARN": []}
def block(m): issues["BLOCK"].append(m)
def warn(m): issues["WARN"].append(m)

# ---- on-page completeness ----
for f in indexable:
    d = S[f]
    if not d["title"]: block(f"{f}: missing <title>")
    if not d["desc"]: block(f"{f}: missing meta description")
    elif not (50 <= len(d["desc"]) <= 165): warn(f"{f}: meta description {len(d['desc'])} chars (aim 50-165)")
    if not d["canonical"]: block(f"{f}: missing canonical")
    if d["h1"] != 1: block(f"{f}: h1 count = {d['h1']} (want 1)")
    miss_og = [k for k, v in d["og"].items() if not v]
    if miss_og: warn(f"{f}: missing og:{','.join(miss_og)}")
    if not d["tw"]: warn(f"{f}: missing twitter:card")
    if not d["lang"]: warn(f"{f}: <html> missing lang")
    if d["jsonld_invalid"]: block(f"{f}: {d['jsonld_invalid']} invalid JSON-LD block(s)")
    if not d["jsonld_types"]: warn(f"{f}: no JSON-LD structured data")

# ---- uniqueness ----
def dupes(key):
    seen = {}
    for f in indexable:
        v = S[f][key].strip().lower()
        if not v: continue
        seen.setdefault(v, []).append(f)
    return {v: fs for v, fs in seen.items() if len(fs) > 1}
for v, fs in dupes("title").items(): block(f"duplicate <title> across {fs}: {v[:50]!r}")
for v, fs in dupes("desc").items(): block(f"duplicate meta description across {fs}")
for v, fs in dupes("canonical").items(): block(f"duplicate canonical {v} across {fs}")

# ---- canonical correctness ----
for f in indexable:
    c = S[f]["canonical"]
    if not c: continue
    if not c.startswith("https://www.topshelfsolutions.io"): warn(f"{f}: canonical not absolute https://www ({c})")
    expected_paths = {f, f.replace(".html", "")}
    if f == "index.html": expected_paths |= {"", "index.html"}
    tail = c.rstrip("/").split("/")[-1] if c.rstrip("/").split("/")[-1] else "index.html"
    if f != "index.html" and tail not in (f, f.replace(".html", "")):
        warn(f"{f}: canonical tail {tail!r} != filename")

# ---- broken internal links (all pages, all links) ----
def resolve(target):
    t = target.lstrip("./")
    if t.endswith("/"): t += "index.html"
    return t
existing = set(glob.glob("**/*.html", recursive=True)) | {"", "/"}
broken = {}
for f in list(pages):
    for lnk in local_links(pages[f]["html"]):
        r = resolve(lnk)
        if r in ("", "/"): continue
        if r not in existing and not os.path.exists(r):
            broken.setdefault(f, set()).add(lnk)
for f, ls in broken.items(): block(f"{f}: broken internal link(s) -> {sorted(ls)}")

# ---- reachability (orphans) BFS from index following ALL links ----
def norm(t):
    r = resolve(t)
    return r if r else "index.html"
reached, stack = set(), ["index.html"]
while stack:
    cur = stack.pop()
    if cur in reached or cur not in pages: continue
    reached.add(cur)
    for lnk in local_links(pages[cur]["html"]):
        stack.append(norm(lnk))
orphans = [f for f in indexable if f not in reached]
for f in orphans: block(f"ORPHAN (unreachable from index by any link): {f}")

# ---- contextual interlinking (inbound links OUTSIDE nav/footer) ----
inbound_ctx = {f: 0 for f in indexable}
for f in indexable:
    for lnk in set(S[f]["content_links"]):
        tgt = norm(lnk)
        if tgt in inbound_ctx and tgt != f:
            inbound_ctx[tgt] += 1
weak = [f for f in indexable if inbound_ctx[f] == 0 and f != "index.html"]

# ---- sitemap accuracy ----
sm = read("sitemap.xml") if os.path.exists("sitemap.xml") else ""
sm_locs = re.findall(r"<loc>(.*?)</loc>", sm)
sm_files = set()
for loc in sm_locs:
    tail = loc.rstrip("/").split("/")[-1]
    sm_files.add("index.html" if (loc.rstrip("/") == SITE or tail == "") else (tail if tail.endswith(".html") else tail + ".html"))
missing_from_sm = [f for f in indexable if f not in sm_files]
extra_in_sm = [f for f in sm_files if f in pages and pages[f]["noindex"]]
for f in missing_from_sm: block(f"indexable page NOT in sitemap: {f}")
for f in extra_in_sm: block(f"NOINDEX page leaked into sitemap: {f}")

# ---- report ----
print("=" * 72)
print(f"INDEXABLE main pages: {len(indexable)}   |   noindex/excluded: {len(noindexed)} -> {noindexed}")
print(f"Sitemap URLs: {len(sm_locs)}")
print("=" * 72)
print(f"\nBLOCKING issues: {len(issues['BLOCK'])}")
for m in issues["BLOCK"]: print("  X", m)
print(f"\nWARNINGS: {len(issues['WARN'])}")
for m in issues["WARN"]: print("  !", m)
print(f"\nContextual interlinking (inbound links outside nav/footer):")
for f in sorted(indexable, key=lambda x: inbound_ctx[x]):
    flag = "  <-- weak" if inbound_ctx[f] == 0 and f != "index.html" else ""
    print(f"  {inbound_ctx[f]:3d}  {f}{flag}")
print(f"\nJSON-LD types per page:")
for f in indexable:
    print(f"  {f}: {sorted(set(S[f]['jsonld_types']))}")

blocking = len(issues["BLOCK"])
print("\n" + ("PASS - no blocking issues" if blocking == 0 else f"FAIL - {blocking} blocking issue(s)"))
sys.exit(0 if blocking == 0 else 1)
