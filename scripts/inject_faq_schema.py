#!/usr/bin/env python3
"""Generate FAQPage JSON-LD from a page's OWN visible FAQ markup and inject it
before </head>. Schema matches on-page text by construction (no hand-writing,
no fabrication). Idempotent: re-running replaces the block it wrote, never adds
a second one. Handles both FAQ patterns used on this site:

  A) <p class="qa-q">Q</p> ... <p class="qa-a">A</p>   (why-us, pricing, authored)
  B) <details ...><summary>Q</summary> A </details>    (booking)

Usage:  python scripts/inject_faq_schema.py <file.html> [<file.html> ...]
        python scripts/inject_faq_schema.py --all        # every top-level *.html
Run from the repo root. A page with no FAQ markup is skipped (reported).
"""
import sys, re, json, glob, html

MARKER = "<!-- FAQPage schema (auto-generated from on-page FAQ; see scripts/inject_faq_schema.py) -->"
BLOCK_RE = re.compile(re.escape(MARKER) + r".*?</script>", re.DOTALL)
PAT_QA = re.compile(r'<p class="qa-q">(?P<q>.*?)</p>\s*<p class="qa-a">(?P<a>.*?)</p>', re.DOTALL)
PAT_DETAILS = re.compile(r'<details[^>]*>\s*<summary>(?P<q>.*?)</summary>(?P<a>.*?)</details>', re.DOTALL)


def clean(fragment: str) -> str:
    """Strip inline tags, decode entities, collapse whitespace -> plain text."""
    text = re.sub(r'<[^>]+>', ' ', fragment)   # drop br/span/a/strong/etc.
    text = html.unescape(text)                 # &mdash; -> —, &rsquo; -> ’
    return re.sub(r'\s+', ' ', text).strip()


def extract(source: str):
    """Ordered, de-duplicated Q&A pairs across both patterns."""
    found = []
    for pat in (PAT_QA, PAT_DETAILS):
        for m in pat.finditer(source):
            q, a = clean(m.group('q')), clean(m.group('a'))
            if q and a:
                found.append((m.start(), q, a))
    found.sort(key=lambda t: t[0])
    seen, pairs = set(), []
    for _, q, a in found:
        if q not in seen:
            seen.add(q)
            pairs.append((q, a))
    return pairs


def build(pairs) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in pairs
        ],
    }
    return MARKER + '\n<script type="application/ld+json">' + \
        json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>"


def process(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    src = BLOCK_RE.sub("", src).rstrip()        # remove any prior auto block first
    pairs = extract(src)
    if not pairs:
        return f"skip   {path}  (no FAQ markup found)"
    if "</head>" not in src:
        return f"ERROR  {path}  (no </head>)"
    block = build(pairs)
    src = src.replace("</head>", block + "\n</head>", 1)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(src)
    return f"ok     {path}  ({len(pairs)} Q&A)"


def main(argv):
    if not argv:
        print(__doc__); return 1
    files = sorted(glob.glob("*.html")) if argv == ["--all"] else argv
    for f in files:
        print(process(f))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
