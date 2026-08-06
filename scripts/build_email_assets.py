"""Build the hosted images the Top Shelf email signature points at.

The signature is a rebrand of the Your Neighborhood GDR one, so the icon glyphs
are the same artwork — only recoloured.  Those icons are two-tone (brand green
on near-black), which means a recolour is an exact remap of the colour pair
rather than a redraw: every pixel sits somewhere on the line between the two,
so we find where and place it on the Top Shelf line instead.  Anti-aliased
edges and alpha come through untouched.

Writes 2x pixels for retina; the signature declares the 1x size.
"""
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "img", "email")
GDR = os.path.expanduser(r"~\FieldPro\public\email-assets")

GREEN, DARK = (0, 196, 104), (11, 26, 17)          # the GDR icon pair
GOLD, ESPRESSO = (201, 168, 106), (16, 12, 8)      # --gold, --surface

ICON = 44          # 22px displayed
LOGO_W = 440       # 220px displayed


def remap(px):
    """Where this pixel sits between GREEN and DARK, placed between GOLD and ESPRESSO."""
    span = sum((g - d) ** 2 for g, d in zip(GREEN, DARK))
    t = sum((p - d) * (g - d) for p, g, d in zip(px[:3], GREEN, DARK)) / span
    t = min(1.0, max(0.0, t))
    return tuple(round(e + (g - e) * t) for g, e in zip(GOLD, ESPRESSO)) + (px[3],)


def icon(name):
    im = Image.open(os.path.join(GDR, name)).convert("RGBA")
    im.putdata([remap(p) for p in im.getdata()])
    im = im.resize((ICON, ICON), Image.LANCZOS)
    im.save(os.path.join(OUT, name), "PNG", optimize=True)
    return name, im.size


def logo(src, dst, width):
    im = Image.open(os.path.join(ROOT, "assets", src)).convert("RGBA")
    h = round(im.height * width / im.width)
    im = im.resize((width, h), Image.LANCZOS)
    im.save(os.path.join(OUT, dst), "PNG", optimize=True)
    return dst, im.size


def main():
    os.makedirs(OUT, exist_ok=True)
    made = [icon(n) for n in ("icon-phone.png", "icon-mail.png", "icon-web.png")]
    made.append(logo("logo-full.png", "logo-email.png", LOGO_W))
    made.append(logo("logo-mark.png", "logo-mark-email.png", 160))
    for name, size in made:
        kb = os.path.getsize(os.path.join(OUT, name)) / 1024
        print("%-22s %-10s %6.1f KB   displayed %dx%d"
              % (name, "%dx%d" % size, kb, size[0] // 2, size[1] // 2))


if __name__ == "__main__":
    main()
