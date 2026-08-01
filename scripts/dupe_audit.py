#!/usr/bin/env python3
"""
Near-duplicate / thin-content audit for the Top Shelf site.

Google's duplicate-content problem is about MAIN CONTENT, not boilerplate —
a shared nav, footer and chat widget across 27 pages is normal and discounted.
So this strips the chrome first, then compares what's left.

Similarity is Jaccard over 5-word shingles, which is the standard shape of
near-duplicate detection (order-sensitive, robust to reordered paragraphs)
rather than a naive character-diff ratio, which over-reports on pages that
share a vocabulary but say different things.

Also reports the things that actually trigger consolidation in Search Console:
duplicate titles, duplicate meta descriptions, thin pages, and canonical/
noindex status.
"""
import io, re, glob, itertools, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BOILERPLATE = [
    (r'<head\b.*?</head>', ' '),
    (r'<script\b.*?</script>', ' '),
    (r'<style\b.*?</style>', ' '),
    (r'<nav\b.*?</nav>', ' '),
    (r'<footer\b.*?</footer>', ' '),
    (r'<svg\b.*?</svg>', ' '),
    (r'<!--.*?-->', ' '),
]

def main_text(html):
    s = html
    for pat, rep in BOILERPLATE:
        s = re.sub(pat, rep, s, flags=re.S | re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'&[a-z]+;|&#\d+;', ' ', s)
    s = re.sub(r'[^a-z0-9 ]+', ' ', s.lower())
    return re.sub(r'\s+', ' ', s).strip()

def shingles(text, n=5):
    w = text.split()
    return {' '.join(w[i:i+n]) for i in range(max(0, len(w) - n + 1))}

def jaccard(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)

def meta(html, name=None, prop=None):
    """Match the attribute's OWN quote character.

    A ["\'] character class terminates on the first apostrophe inside the
    text, so content="You didn't open a shop..." was captured as just
    "You didn" — which made every description starting that way look
    identical and produced a false duplicate report.
    """
    attr = 'name' if name else 'property'
    val = name or prop
    m = (re.search(r'<meta[^>]+' + attr + r'=["\']' + val + r'["\'][^>]+content="([^"]*)"', html, re.I | re.S)
         or re.search(r"<meta[^>]+" + attr + r"=[\"']" + val + r"[\"'][^>]+content='([^']*)'", html, re.I | re.S))
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''

# Only audit what is actually DEPLOYED. Untracked local files (review copies,
# work in progress) can't be a duplicate-content risk because they never reach
# the server — auditing them produces false CRITICALs.
import subprocess
tracked = set(subprocess.run(["git","ls-files","*.html"], capture_output=True, text=True).stdout.split())

pages = {}
for p in sorted(glob.glob("*.html")):
    if p.startswith("google"):        # search-console verification stub
        continue
    if p not in tracked:
        print(f"  (skipping {p} — untracked, not deployed)")
        continue
    h = io.open(p, encoding="utf-8").read()
    t = main_text(h)
    title = re.search(r'<title>(.*?)</title>', h, re.S)
    canon = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']', h, re.I)
    pages[p] = {
        'text': t,
        'shingles': shingles(t),
        'words': len(t.split()),
        'title': re.sub(r'\s+',' ',title.group(1)).strip() if title else '',
        'desc': meta(h, name='description'),
        'canonical': canon.group(1) if canon else '',
        'noindex': 'noindex' in h.lower(),
    }

print(f"Audited {len(pages)} pages (nav / footer / head / scripts stripped)\n")

# ---------------------------------------------------------------- similarity
print("=" * 78)
print("NEAR-DUPLICATE PAIRS  (Jaccard on 5-word shingles of main content)")
print("=" * 78)
rows = []
for a, b in itertools.combinations(pages, 2):
    j = jaccard(pages[a]['shingles'], pages[b]['shingles'])
    if j >= 0.30:
        rows.append((j, a, b))
rows.sort(reverse=True)

def tier(j):
    if j >= 0.75: return "CRITICAL"
    if j >= 0.55: return "HIGH    "
    if j >= 0.40: return "MODERATE"
    return "low     "

if rows:
    for j, a, b in rows:
        flags = []
        if pages[a]['noindex'] or pages[b]['noindex']: flags.append("one is noindex")
        if pages[a]['title'] == pages[b]['title']: flags.append("SAME TITLE")
        if pages[a]['desc'] == pages[b]['desc']: flags.append("SAME DESC")
        print(f"  {tier(j)} {j:5.0%}  {a:32} <-> {b:32} {' | '.join(flags)}")
else:
    print("  none above 30% — no near-duplicate risk")

# ---------------------------------------------------------------- dupe meta
print("\n" + "=" * 78)
print("DUPLICATE TITLES / DESCRIPTIONS  (the thing Search Console flags)")
print("=" * 78)
for field in ('title', 'desc'):
    seen = {}
    for p, d in pages.items():
        seen.setdefault(d[field], []).append(p)
    dupes = {k: v for k, v in seen.items() if len(v) > 1 and k}
    if dupes:
        for k, v in dupes.items():
            print(f"  {field.upper()} shared by {len(v)}: \"{k[:58]}\"")
            for p in v: print(f"      {p}")
    else:
        print(f"  {field}: all unique")

# ---------------------------------------------------------------- thin pages
print("\n" + "=" * 78)
print("CONTENT DEPTH  (main-content word count)")
print("=" * 78)
for p, d in sorted(pages.items(), key=lambda kv: kv[1]['words']):
    mark = "THIN " if d['words'] < 300 else "     "
    idx  = "noindex" if d['noindex'] else ""
    print(f"  {mark}{d['words']:>5} words  {p:34} {idx}")

# ---------------------------------------------------------------- canonicals
print("\n" + "=" * 78)
print("CANONICAL SANITY")
print("=" * 78)
bad = 0
for p, d in sorted(pages.items()):
    if not d['canonical']:
        print(f"  MISSING canonical   {p}"); bad += 1
    elif not d['canonical'].rstrip('/').endswith(p.replace('index.html','').rstrip('/') or 'topshelfsolutions.io'):
        if p != 'index.html':
            print(f"  POINTS ELSEWHERE    {p:32} -> {d['canonical']}"); bad += 1
if not bad:
    print("  every page self-canonicals correctly")
