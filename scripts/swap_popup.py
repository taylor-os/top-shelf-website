"""Swap the site pop-up: every page that loads assets/gap-quiz.js loads assets/see-your-business.js instead.

Idempotent: re-running only refreshes the cache string. Pages under demo/, websites/ and
preview/ are left alone. assets/gap-quiz.js itself stays in the repo, unused.

    python scripts/swap_popup.py
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = ("demo", "websites", "preview", "node_modules", ".git")
TAG_RE = re.compile(r'<script src="assets/(?:gap-quiz|see-your-business)\.js(?:\?v=[^"]*)?"></script>')
NEW = '<script src="assets/see-your-business.js?v=20261127a"></script>'


def pages():
    for path in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        if os.path.relpath(path, ROOT).replace("\\", "/").split("/")[0] not in SKIP:
            yield path


def main():
    changed = 0
    for path in pages():
        with open(path, encoding="utf-8", newline="") as fh:
            src = fh.read()
        new = TAG_RE.sub(NEW, src)
        if new != src:
            with open(path, "w", encoding="utf-8", newline="") as fh:
                fh.write(new)
            changed += 1
    print("pop-up tag written on %d pages" % changed)


if __name__ == "__main__":
    main()
