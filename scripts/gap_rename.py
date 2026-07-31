#!/usr/bin/env python3
"""
Top Shelf: retire the "leak" metaphor in favour of "the gap".

Owner decision (2026-07-31): all customer-facing copy across the Top Shelf
organization moves from "stop the leaks" to "find the gap in your business".
The hero H1 becomes "Find the Gap That's Costing You". The Leak Finder tool
is renamed Gap Finder, filenames included, with 301 redirects.

This is NOT a find/replace. "leak" appears in 70+ grammatical forms and at
least one genuinely literal sense (a car fluid leak on the auto page), so the
mapping is explicit and ordered longest-first, with protected spans.

Usage:
    python gap_rename.py --dry <dir> [<dir> ...]
    python gap_rename.py --apply <dir> [<dir> ...]
"""
import io, os, re, sys, argparse

# ---------------------------------------------------------------------------
# Spans that must never be touched. Checked before any replacement.
# ---------------------------------------------------------------------------
PROTECTED = [
    # A real car fluid leak, on the auto industry page.
    r'the worn brakes, the leak, the cracked belt',
    # External citation URL containing "revenue-leakage".
    r'https?://[^\s"\'<>]*leak[^\s"\'<>]*',
]

# ---------------------------------------------------------------------------
# Ordered replacements. Longest / most specific first.
# ---------------------------------------------------------------------------
PAIRS = [
    # --- hero + headline -----------------------------------------------------
    ("Stop Losing Money to Leaks You Can&rsquo;t See", "Find the Gap That&rsquo;s Costing You"),
    ("Stop Losing Money to Leaks You Can't See",       "Find the Gap That's Costing You"),
    ("Stop Losing Money",                              "Find the Gap"),
    ("Leaks You Can&rsquo;t See",                      "That&rsquo;s Costing You"),
    ("Leaks You Can't See",                            "That's Costing You"),

    # --- the tool ------------------------------------------------------------
    ("Business Leak Finder",  "Business Gap Finder"),
    ("Business leak finder",  "Business gap finder"),
    ("Leak Finder",           "Gap Finder"),
    ("leak finder",           "gap finder"),
    ("Leak Map",              "Gap Map"),
    ("leak map",              "gap map"),
    ("Your leak report",      "Your gap report"),
    ("Your Leak Report",      "Your Gap Report"),
    ("your leak report",      "your gap report"),
    ("Send my leak report",   "Send my gap report"),
    ("See my leak report",    "See my gap report"),
    ("leak report",           "gap report"),
    ("Leak Report",           "Gap Report"),
    ("leak audit",            "gap audit"),
    ("Leak Audit",            "Gap Audit"),
    ("Find my leaks",         "Find my gap"),
    ("Find your leaks",       "Find your gap"),
    ("find your leaks",       "find your gap"),

    # --- CTAs ---------------------------------------------------------------
    ("Show Me Where I&rsquo;m Leaking Money", "Show Me the Gap"),
    ("Show Me Where I'm Leaking Money",       "Show Me the Gap"),
    ("Show me where I&rsquo;m leaking money", "Show me the gap"),

    # --- "plug" verb becomes "close" ----------------------------------------
    ("Ready to plug the leaks?",     "Ready to close the gaps?"),
    ("What Plugging the Leaks",      "What Closing the Gaps"),
    ("Plugging the leaks",           "Closing the gaps"),
    ("plugging the leaks",           "closing the gaps"),
    ("plug the leaks",               "close the gaps"),
    ("Plug the Leaks",               "Close the Gaps"),
    ("plugs a specific leak",        "closes a specific gap"),
    ("plugged leaks",                "closed gaps"),
    ("how we plug them",             "how we close them"),
    ("Close the Leaks",              "Close the Gaps"),
    ("Leaks Are Sealed",             "Gaps Are Closed"),
    ("the leaks are sealed",         "the gaps are closed"),

    # --- "X is leaking money" ------------------------------------------------
    ("Every business leaks money somewhere", "Every business has a gap somewhere"),
    ("The Business Side Is Quietly Leaking Money.", "There&rsquo;s a Gap on the Business Side."),
    ("Your Practice Is Leaking Six Figures.",       "Your Practice Has a Six-Figure Gap."),
    ("where money is leaking out",           "where the gap is"),
    ("where it&rsquo;s leaking money",       "where the gap is"),
    ("where it's leaking money",             "where the gap is"),
    ("where your business is leaking money", "where your gap is"),
    ("your business leaking money",          "your business losing money"),
    ("where you&rsquo;re leaking customers", "where you&rsquo;re losing customers"),
    ("where you're leaking customers",       "where you're losing customers"),
    ("You&rsquo;re likely leaking",          "Your likely gap is"),
    ("You're likely leaking",                "Your likely gap is"),
    ("re likely leaking",                    "r likely gap is"),
    ("Money leaking / month",                "Gap / month"),
    ("Money leaking",                        "Gap"),
    ("is quietly leaking money",             "quietly has a gap"),
    ("leaking money",                        "losing money"),

    # --- "the money leaks" ---------------------------------------------------
    ("The money leaks somewhere else", "The money slips out somewhere else"),
    ("the money leaks somewhere else", "the money slips out somewhere else"),
    ("Where the money leaks",          "Where the money goes"),
    ("where the money leaks",          "where the money goes"),

    # --- counted leaks -------------------------------------------------------
    ("Every Leak Is Existential.", "Every Gap Is Existential."),
    ("All Five Leaks",   "All Five Gaps"),
    ("Five Leaks Draining the", "Five Gaps Draining the"),
    ("Five Leaks That Are",     "Five Gaps That Are"),
    ("Six Leaks Costing",       "Six Gaps Costing"),
    ("Seven Leaks Costing",     "Seven Gaps Costing"),
    ("Six Leaks",   "Six Gaps"),
    ("Five Leaks",  "Five Gaps"),
    ("Seven Leaks", "Seven Gaps"),
    ("Four Leaks",  "Four Gaps"),
    ("six leaks",   "six gaps"),
    ("five leaks",  "five gaps"),

    # --- remaining noun uses -------------------------------------------------
    ("From Leaky to", "From Gaps to"),
    ("Leaky",  "Gaps"),
    ("leaky",  "gaps"),
    ("the exact leaks costing", "the exact gaps costing"),
    ("The leaks every local business shares", "The gaps every local business shares"),
    ("which leaks are costing you", "which gaps are costing you"),
    ("-style leaks are costing",    "-style gaps are costing"),
    ("restaurant leaks",  "restaurant gaps"),
    ("each leak is causing", "each gap is causing"),
    ("a specific leak", "a specific gap"),
    ("LEAK FINDER", "GAP FINDER"),
    ("LEAK MAP", "GAP MAP"),
    ("THE LEAKS", "THE GAPS"),
    ("LEAKS", "GAPS"),
    ("LEAK", "GAP"),
    ("Leaks", "Gaps"),
    ("leaks", "gaps"),
    ("Leak",  "Gap"),
    ("leak",  "gap"),
]

TEXT_EXT = {".html", ".htm", ".js", ".css", ".md", ".json", ".py", ".txt",
            ".xml", ".php", ".blade", ".vue", ".jsx", ".tsx", ".ts", ".yml", ".yaml"}
SKIP_DIRS = {".git", "node_modules", "vendor", "dist", "build", ".next", "__pycache__"}
SKIP_FILES = {"gap_rename.py"}   # never rewrite the mapping table itself


def transform(text):
    """Apply the mapping, leaving protected spans byte-identical."""
    spans = []
    for pat in PROTECTED:
        for m in re.finditer(pat, text):
            spans.append((m.start(), m.end()))
    spans.sort()
    merged = []
    for a, b in spans:
        if merged and a <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])

    # Split into alternating [editable, protected, editable, ...]
    out, cur, n = [], 0, 0
    for a, b in merged:
        chunk = text[cur:a]
        new, c = apply_pairs(chunk)
        out.append(new); n += c
        out.append(text[a:b])          # protected, untouched
        cur = b
    chunk = text[cur:]
    new, c = apply_pairs(chunk)
    out.append(new); n += c
    return "".join(out), n


def apply_pairs(chunk):
    n = 0
    for a, b in PAIRS:
        if a in chunk:
            n += chunk.count(a)
            chunk = chunk.replace(a, b)
    return chunk, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("dirs", nargs="+")
    args = ap.parse_args()

    total_files = total_hits = 0
    for root_dir in args.dirs:
        for root, dirs, files in os.walk(root_dir):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for fn in files:
                if os.path.splitext(fn)[1].lower() not in TEXT_EXT or fn in SKIP_FILES:
                    continue
                p = os.path.join(root, fn)
                try:
                    s = io.open(p, encoding="utf-8").read()
                except (UnicodeDecodeError, PermissionError):
                    continue
                if not re.search(r'leak', s, re.I):
                    continue
                new, n = transform(s)
                if new != s:
                    total_files += 1; total_hits += n
                    print(f"  {n:>4}  {p}")
                    if args.apply:
                        io.open(p, "w", encoding="utf-8", newline="").write(new)

    verb = "rewrote" if args.apply else "would rewrite"
    print(f"\n{verb} {total_hits} occurrences across {total_files} files")


if __name__ == "__main__":
    main()
