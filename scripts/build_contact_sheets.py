"""Render one numbered contact sheet per library pool, for picking photos by eye.

Review artefact only - written to .libgen/contactsheets/ (gitignored), not shipped.
"""
import json
import os
from collections import OrderedDict

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(ROOT, "assets", "img", "library")
OUT = os.path.join(ROOT, ".libgen", "contactsheets")

COLS, THUMB_W, GAP, BAR = 5, 460, 10, 34


def font(size):
    for name in ("segoeui.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    manifest = json.load(open(os.path.join(LIB, "manifest.json"), encoding="utf-8"))
    pools = OrderedDict()
    for m in manifest:
        pools.setdefault(m["vertical"] or m["family"], []).append(m)

    os.makedirs(OUT, exist_ok=True)
    title_f, num_f = font(26), font(20)
    for pool, items in pools.items():
        thumb_h = round(THUMB_W * items[0]["height"] / items[0]["width"])
        rows = -(-len(items) // COLS)
        head = 46
        sheet = Image.new("RGB", (
            COLS * THUMB_W + (COLS + 1) * GAP,
            head + rows * (thumb_h + BAR + GAP) + GAP,
        ), (18, 18, 20))
        draw = ImageDraw.Draw(sheet)
        draw.text((GAP, 12), "%s  -  %d photos" % (pool, len(items)), font=title_f, fill=(240, 240, 240))

        for i, m in enumerate(items):
            r, c = divmod(i, COLS)
            x = GAP + c * (THUMB_W + GAP)
            y = head + r * (thumb_h + BAR + GAP)
            im = Image.open(os.path.join(LIB, m["file"].replace("/", os.sep)))
            sheet.paste(im.resize((THUMB_W, thumb_h), Image.LANCZOS), (x, y))
            label = "%02d  %s" % (i + 1, m["description"])
            while draw.textlength(label, font=num_f) > THUMB_W - 8 and len(label) > 8:
                label = label[:-2]
            draw.text((x + 4, y + thumb_h + 8), label, font=num_f, fill=(190, 190, 195))

        path = os.path.join(OUT, "%s.jpg" % pool)
        sheet.save(path, "JPEG", quality=86)
        print(path)


if __name__ == "__main__":
    main()
