"""Render a kit page to the site's screenshot format.

  python render.py <page.html> <out.jpg> d|m      one page (d = desktop 1440x900 @2x, m = phone 390x844 @3x)
  python render.py --all <folder>                 every *-d.html / *-m.html in <folder>, written beside it as .jpg
  add --no-strip to skip the sample strip (used for side-by-side checks against the real captures)

The raw PNG is kept beside the JPEG (<out>.png). A dark strip reading
"Sample screens · sample data, not a real business" is appended below the page:
the viewport is shortened by the strip height, so nothing on the page is covered.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

FINAL = {"d": (1440, 900), "m": (585, 1266)}
STRIP = {"d": 24, "m": 30}  # final-image pixels (phone: 20 CSS px at 1.5 final px per CSS px)
CSS_STRIP = {"d": 24, "m": 20}
DEVICES = {
    "d": dict(viewport={"width": 1440, "height": 900}, device_scale_factor=2),
    "m": dict(viewport={"width": 390, "height": 844}, device_scale_factor=3, is_mobile=True, has_touch=True),
}
STRIP_TEXT = "Sample screens \u00b7 sample data, not a real business"
FONTS = ["C:/Windows/Fonts/segoeui.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]


def font(size):
    for f in FONTS:
        if Path(f).exists():
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


def render(browser, page_path: Path, out: Path, device: str, strip: bool = True) -> None:
    opts = dict(DEVICES[device])
    if strip:
        vp = opts["viewport"]
        opts["viewport"] = {"width": vp["width"], "height": vp["height"] - CSS_STRIP[device]}
    ctx = browser.new_context(**opts)
    page = ctx.new_page()
    page.goto(page_path.resolve().as_uri(), wait_until="networkidle")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(250)
    raw = out.with_suffix(".png")
    page.screenshot(path=str(raw))
    ctx.close()

    w, h = FINAL[device]
    s = STRIP[device] if strip else 0
    img = Image.open(raw).convert("RGB").resize((w, h - s), Image.LANCZOS)
    final = Image.new("RGB", (w, h), (17, 24, 20))
    final.paste(img, (0, 0))
    if strip:
        d = ImageDraw.Draw(final)
        f = font(13 if device == "d" else 14)
        tw = d.textlength(STRIP_TEXT, font=f)
        d.text(((w - tw) / 2, h - s / 2), STRIP_TEXT, font=f, fill=(214, 226, 219), anchor="lm")
    final.save(out, "JPEG", quality=85, optimize=True)
    print(out, final.size)


def main(argv):
    strip = "--no-strip" not in argv
    argv = [a for a in argv if a != "--no-strip"]
    if argv and argv[0] == "--all":
        folder = Path(argv[1])
        jobs = [(p, p.with_suffix(".jpg"), p.stem[-1]) for p in sorted(folder.glob("*.html")) if p.stem[-2:] in ("-d", "-m")]
    elif len(argv) == 3 and argv[2] in FINAL:
        jobs = [(Path(argv[0]), Path(argv[1]), argv[2])]
    else:
        sys.exit(__doc__)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for src, out, dev in jobs:
            render(b, src, out, dev, strip)
        b.close()


if __name__ == "__main__":
    main(sys.argv[1:])
