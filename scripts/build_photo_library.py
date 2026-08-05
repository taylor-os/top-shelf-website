"""Turn the raw generated PNGs in .libgen/ into the shipped photo library.

Reads .libgen/downloaded.json (index, family, vertical, file, prompt), crops each
image to an exact 16:9 hero frame, writes WebP into assets/img/library/, and emits
a manifest the site builders read to pick a photo by vertical.

Layout
    assets/img/library/home_services/<trade>/<trade>-NN-<slug>.webp   (10 trades)
    assets/img/library/<family>/<family>-NN-<slug>.webp               (family pools)

Manifest entries carry `vertical: null` for the family-level pools, so a lookup can
try the vertical first and fall back to the family.
"""
import json
import os
import re

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBGEN = os.path.join(ROOT, ".libgen")
OUT = os.path.join(ROOT, "assets", "img", "library")
BASE_URL = "https://www.topshelfsolutions.io/assets/img/library"
SKILL = os.path.expanduser(r"~\.claude\skills\topshelf-sample-site")

WIDTH, HEIGHT = 1366, 768
QUALITY = 82

# The shared style tail every prompt carries; everything before it is the scene.
TAIL = re.compile(r"\s*Photorealistic\b.*", re.S | re.I)

STOP = set("""a an the and or of in on at to with for from by into onto over under its
their his her that this is are was were be been being as it no not any all one two both
clean tidy neat bright modern professional daylight natural light sharp focus wide
composition clear space headline overlay colour color suits brand website absolutely
text signage letters words logos names readable labels people showing shows show""".split())


def describe(prompt: str) -> str:
    """The scene sentence, without the shared style boilerplate."""
    return TAIL.sub("", prompt).strip().rstrip(".,")


def tags(description: str) -> list:
    words = [w for w in re.findall(r"[a-z]+", description.lower()) if len(w) > 3 and w not in STOP]
    seen, out = set(), []
    for w in words:
        if w not in seen:
            seen.add(w)
            out.append(w)
    return out[:10]


def to_hero(src: str, dst: str) -> None:
    """Centre-crop to exactly 16:9 and write WebP."""
    im = Image.open(src).convert("RGB")
    w, h = im.size
    target = WIDTH / HEIGHT
    if w / h > target:
        new_w = int(round(h * target))
        left = (w - new_w) // 2
        im = im.crop((left, 0, left + new_w, h))
    else:
        new_h = int(round(w / target))
        top = (h - new_h) // 2
        im = im.crop((0, top, w, top + new_h))
    im = im.resize((WIDTH, HEIGHT), Image.LANCZOS)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    im.save(dst, "WEBP", quality=QUALITY, method=6)


def main():
    records = json.load(open(os.path.join(LIBGEN, "downloaded.json"), encoding="utf-8"))
    manifest = []
    for rec in sorted(records, key=lambda r: r["index"]):
        family, vertical = rec["family"], rec["vertical"]
        stem = os.path.splitext(os.path.basename(rec["file"]))[0]
        if family == vertical:                    # family-level pool
            rel = "%s/%s.webp" % (family, stem)
            vertical = None
        else:                                     # home services, per trade
            rel = "%s/%s/%s.webp" % (family, vertical, stem)

        src = os.path.join(LIBGEN, rec["file"].replace("/", os.sep))
        dst = os.path.join(OUT, rel.replace("/", os.sep))
        if not os.path.exists(dst):
            to_hero(src, dst)

        description = describe(rec["prompt"])
        manifest.append({
            "family": family,
            "vertical": vertical,
            "file": rel,
            "url": "%s/%s" % (BASE_URL, rel),
            "description": description,
            "tags": tags(description),
            "width": WIDTH,
            "height": HEIGHT,
        })

    os.makedirs(OUT, exist_ok=True)
    json.dump(manifest, open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8"), indent=1)

    # The skill reads pools, not the full manifest — write it the slim version.
    pools = {}
    for m in manifest:
        pools.setdefault(m["vertical"] or m["family"], []).append(
            {"url": m["url"], "description": m["description"], "tags": m["tags"]}
        )
    if os.path.isdir(SKILL):
        json.dump({"pools": pools}, open(os.path.join(SKILL, "photo_library.json"), "w",
                                         encoding="utf-8"), indent=1)
        print("synced ->", os.path.join(SKILL, "photo_library.json"))
    total = sum(os.path.getsize(os.path.join(OUT, m["file"].replace("/", os.sep))) for m in manifest)
    for name in sorted(pools):
        print("%-16s %d" % (name, len(pools[name])))
    print("%d images, %d pools, %.1f MB" % (len(manifest), len(pools), total / 1048576))


if __name__ == "__main__":
    main()
