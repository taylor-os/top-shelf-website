#!/usr/bin/env python3
"""Uniqueness gate for the SEO corpus (plan §7). Pre-publish check, not a post-hoc report.

Shingle (k-word n-gram) Jaccard similarity of each page's VISIBLE BODY against every other
top-level page. Boilerplate (head, nav, footer, script, style) is stripped first so shared
chrome never counts as duplication. Nothing ships above THRESHOLD overlap — an over-threshold
page gets merged into the closest existing page instead of published thin (the anti-doorway
rule). Exit 1 if any candidate breaches THRESHOLD.

Usage:
  python scripts/dupe_audit.py                      # audit all top-level pages against each other
  python scripts/dupe_audit.py new1.html new2.html  # gate ONLY these candidates vs the whole corpus
"""
import os, re, sys, glob, io, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
THRESHOLD = 0.35   # plan §7: nothing ships above ~35% shingle overlap
K = 8              # shingle size (word n-gram)

def visible_body(html):
    """Strip head/nav/footer/script/style/tags → normalized word list of the real body copy."""
    h = re.sub(r"<head\b.*?</head>", " ", html, flags=re.S | re.I)
    h = re.sub(r"<nav\b[^>]*>.*?</nav>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<footer\b[^>]*>.*?</footer>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<aside\b[^>]*>.*?</aside>", " ", h, flags=re.S | re.I)  # sticky sidebar = shared chrome (CTA card etc.)
    h = re.sub(r"<script\b.*?</script>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<style\b.*?</style>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<[^>]+>", " ", h)                 # drop tags
    h = re.sub(r"&[a-z]+;|&#\d+;", " ", h)         # drop entities
    h = re.sub(r"[^a-z0-9 ]", " ", h.lower())       # keep words/numbers
    return h.split()

def shingles(words, k=K):
    return set(tuple(words[i:i + k]) for i in range(max(0, len(words) - k + 1)))

def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)

# corpus = git-tracked, INDEXABLE top-level pages (what actually competes in search) + any
# candidate passed on argv. Noindex pages (demos, concept mockups) don't compete, so overlap
# with them is irrelevant — exclude them or a noindex homepage variant false-flags every page.
def is_noindex(path):
    try:
        s = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return False
    return bool(re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', s, re.I))

tracked = subprocess.run(["git", "ls-files", "*.html"], capture_output=True, text=True).stdout.split()
corpus = sorted(f for f in tracked if "/" not in f and not is_noindex(f))
candidates = [a for a in sys.argv[1:] if a.endswith(".html")]
# candidates may be new/untracked — include them
for c in candidates:
    if c not in corpus and os.path.exists(c):
        corpus.append(c)
targets = candidates if candidates else corpus

sig = {}
for f in corpus:
    if not os.path.exists(f):
        continue
    sig[f] = shingles(visible_body(open(f, encoding="utf-8", errors="replace").read()))

breaches = []
rows = []
for t in targets:
    if t not in sig:
        continue
    worst = (0.0, None)
    for other in corpus:
        if other == t or other not in sig:
            continue
        j = jaccard(sig[t], sig[other])
        if j > worst[0]:
            worst = (j, other)
    rows.append((worst[0], t, worst[1]))
    if worst[0] > THRESHOLD:
        breaches.append((t, worst[0], worst[1]))

rows.sort(reverse=True)
print(f"Uniqueness gate — {len(targets)} candidate(s) vs {len(sig)} pages, threshold {THRESHOLD:.0%}, shingle k={K}")
print("-" * 72)
for j, t, other in rows[:40]:
    flag = "  <-- BREACH (merge, don't ship)" if j > THRESHOLD else ""
    print(f"  {j:5.1%}  {t}  ~=  {other}{flag}")

if breaches:
    print(f"\nFAIL — {len(breaches)} page(s) over {THRESHOLD:.0%}:")
    for t, j, other in breaches:
        print(f"  {t}: {j:.1%} vs {other}")
    sys.exit(1)
print(f"\nPASS — every candidate is under {THRESHOLD:.0%} overlap (unique enough to ship)")
sys.exit(0)
