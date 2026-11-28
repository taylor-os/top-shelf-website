"""Homepage screenshots of the sample websites for the industry cards, pop-up and concepts.
Usage: python scripts/shoot_websites.py [dir ...]   (opens the static pages as file:// URLs; no server needed)
Writes assets/img/websites/<dir>-home-d.webp (1600x900 view, saved 1200x675, 16:9) and -home-m.webp (390x844 view, 585 wide)."""
import sys, os
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "img", "websites")
dirs = sys.argv[1:] or sorted(d for d in os.listdir(os.path.join(ROOT, "websites")) if os.path.isfile(os.path.join(ROOT, "websites", d, "index.html")))
REVEAL = "[data-reveal],.reveal,.rv{opacity:1!important;transform:none!important}*{animation-duration:0s!important;transition:none!important}"
with sync_playwright() as p:
    b = p.chromium.launch()
    for d in dirs:
        for tag, vp, scale, width in (("d", (1600, 900), 1, 1200), ("m", (390, 844), 2, 585)):
            pg = b.new_page(viewport={"width": vp[0], "height": vp[1]}, device_scale_factor=scale)
            pg.emulate_media(reduced_motion="reduce")
            pg.goto(Path(ROOT, "websites", d, "index.html").as_uri(), wait_until="load")
            pg.add_style_tag(content=REVEAL); pg.wait_for_timeout(1200)
            raw = os.path.join(OUT, f"_{d}-{tag}.png"); pg.screenshot(path=raw); pg.close()
            im = Image.open(raw).convert("RGB"); im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
            im.save(os.path.join(OUT, f"{d}-home-{tag}.webp"), quality=80); os.remove(raw)
        print("ok", d)
    b.close()
