"""Export the approved industry CRM screens to the site as WebP.

renders-src/industry-crm/screens/<slug>/<name>.jpg  ->  assets/img/crm/industries/<slug>/<name>.webp
Desktop screens are 1600x900 (16:9), phone screens 585x1266. Slugs and files come from
renders-src/industry-crm/captions.json, so a new industry only needs a captions entry.
Usage: python scripts/export_crm_webp.py [slug ...]
"""
import json
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAPTIONS = json.load(open(os.path.join(ROOT, "renders-src", "industry-crm", "captions.json"), encoding="utf-8"))


def export(slug):
    src_dir = os.path.join(ROOT, "renders-src", "industry-crm", "screens", slug)
    out_dir = os.path.join(ROOT, "assets", "img", "crm", "industries", slug)
    os.makedirs(out_dir, exist_ok=True)
    n = 0
    for s in CAPTIONS[slug]["screens"]:
        jpg = os.path.join(src_dir, s["file"].replace(".webp", ".jpg"))
        Image.open(jpg).convert("RGB").save(os.path.join(out_dir, s["file"]), quality=80, method=6)
        n += 1
    return n


if __name__ == "__main__":
    slugs = sys.argv[1:] or list(CAPTIONS)
    total = sum(export(s) for s in slugs)
    print("exported", total, "screens for", len(slugs), "industries")
