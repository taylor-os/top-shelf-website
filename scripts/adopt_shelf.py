#!/usr/bin/env python3
"""
Swap the text-only industry choosers for the photographic "shelf" pattern
adopted from the Direction B homepage study (owner decision 2026-07-31).

Touches two shapes:
  * index.html          .rowlist / .rowitem   (the Find Your Industry section)
  * solution-*.html     .mini-grid + .mini-card, but ONLY where the cards
                        link to industry-*.html (the "See This Work in Your
                        Industry" cross-link block). Solution-linking
                        mini-grids on the industry pages are left alone.
"""
import io, os, re, glob

INDUSTRIES = [
    ("industry-home-services.html",     "home-services",     "Home Services",
     "You can&rsquo;t answer the phone from under a sink."),
    ("industry-restaurants.html",       "restaurants",       "Restaurants &amp; Bars",
     "Every empty seat is gone forever."),
    ("industry-medical-dental.html",    "medical-dental",    "Medical &amp; Dental",
     "The new patient who gets voicemail books elsewhere."),
    ("industry-legal.html",             "legal",             "Law Firms",
     "The 6pm case signs with whoever answered."),
    ("industry-retail.html",            "retail",            "Retail &amp; Local",
     "They browse your shelves, then buy it on Amazon."),
    ("industry-auto.html",              "auto",              "Auto",
     "The call you miss wrist-deep in an engine."),
    ("industry-salon-spa-fitness.html", "salon-spa-fitness", "Salon, Spa &amp; Fitness",
     "The Saturday no-show you could&rsquo;ve filled five times."),
    ("industry-custom.html",            "custom",            "Your Business",
     "Don&rsquo;t see your exact trade? Start here."),
]


def shelf(indent="    ", cta="See the playbook"):
    out = [f'{indent}<div class="shelf">']
    for href, img, name, hook in INDUSTRIES:
        # alt="" — the link already carries a visible text label, so a
        # described image would double-announce for screen readers.
        out += [
            f'{indent}  <a href="{href}" class="bottle reveal">',
            f'{indent}    <span class="bottle-frame"><img src="assets/img/industry/{img}.jpg" alt="" loading="lazy" width="1000" height="1339"></span>',
            f'{indent}    <span class="bottle-plate">',
            f'{indent}      <span class="bottle-name">{name}</span>',
            f'{indent}      <span class="bottle-hook">{hook}</span>',
            f'{indent}      <span class="bottle-go">{cta} <span aria-hidden="true">&rarr;</span></span>',
            f'{indent}    </span>',
            f'{indent}  </a>',
        ]
    out.append(f'{indent}</div>')
    return "\n".join(out)


def replace_block(text, open_re, classname):
    """Replace one balanced <div class="...">...</div> block."""
    m = re.search(open_re, text)
    if not m:
        return text, False
    start = m.start()
    i, depth = m.end(), 1
    for tok in re.finditer(r'</?div\b', text[m.end():]):
        depth += 1 if tok.group(0) == "<div" else -1
        if depth == 0:
            i = m.end() + tok.end() + len("</div>") - len("</div>")
            i = m.end() + tok.start() + len("</div>")
            break
    return text[:start] + shelf() + text[i:], True


def main():
    changed = []

    # --- homepage ---------------------------------------------------------
    p = "index.html"
    s = io.open(p, encoding="utf-8").read()
    new, ok = replace_block(s, r'<div class="rowlist">', "rowlist")
    if ok:
        io.open(p, "w", encoding="utf-8", newline="").write(new)
        changed.append(p)

    # --- solution pages: only industry-linking mini-grids ------------------
    for p in sorted(glob.glob("solution-*.html")):
        s = io.open(p, encoding="utf-8").read()
        m = re.search(r'<div class="mini-grid cols-4 reveal">', s)
        if not m:
            continue
        # confirm this grid links to industries, not solutions
        tail = s[m.end():m.end() + 4000]
        if len(re.findall(r'href="industry-', tail)) < 4:
            continue
        new, ok = replace_block(s, r'<div class="mini-grid cols-4 reveal">', "mini-grid")
        if ok:
            io.open(p, "w", encoding="utf-8", newline="").write(new)
            changed.append(p)

    for c in changed:
        print("  shelf adopted:", c)
    print(f"\n{len(changed)} pages updated")


if __name__ == "__main__":
    main()
