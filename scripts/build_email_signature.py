"""Generate the Top Shelf email signature options.

A rebrand of the Your Neighborhood GDR signature, so the same email-safety rules
apply: tables not flexbox, inline styles only (Gmail strips <style>), no web
fonts, no media queries.  Stacking on narrow screens comes from the GDR trick of
a dir="rtl" wrapper around dir="ltr" inline-block children, which reverses the
visual order without reordering the DOM and degrades to a stack on its own.

The contact facts are declared once here, so five options cannot disagree about
the phone number.

Usage: python build_email_signature.py   ->  .libgen/signatures/
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, ".libgen", "signatures")
IMG = "https://www.topshelfsolutions.io/assets/img/email"

# Verified from the live site: index.html JSON-LD + footer, contact.html.
PHONE, PHONE_HREF = "(469)&nbsp;833-3033", "tel:+14698333033"
EMAIL = "contact@topshelfsolutions.io"
SITE, SITE_HREF = "www.topshelfsolutions.io", "https://www.topshelfsolutions.io"
SLOGAN = "We Solve. You Grow."

GROUND, SURFACE = "#0B0906", "#100C08"
GOLD, GOLD_BRIGHT, GOLD_DEEP = "#C9A86A", "#E4C98A", "#A98A4E"
INK, INK2, INK3 = "#F4F0E8", "#CFC7B8", "#98907F"
HAIRLINE = "#2A2118"

# Cormorant Garamond and Jost do not exist in mail clients; Georgia and Arial are
# the closest things every client already has.
SERIF = "Georgia,'Times New Roman',serif"
SANS = "Arial,Helvetica,sans-serif"

CONTACTS = (
    ("icon-phone.png", PHONE_HREF, PHONE),
    ("icon-mail.png", "mailto:" + EMAIL, EMAIL),
    ("icon-web.png", SITE_HREF, SITE),
)


def rows(colour=INK2, size=13, align="left"):
    """The GDR icon-and-link contact block."""
    out = ['<table role="presentation" align="center" cellpadding="0" cellspacing="0" '
           'border="0" style="border-collapse:collapse;margin:0 auto;">']
    for icon, href, label in CONTACTS:
        out.append(
            '<tr><td width="30" valign="middle" style="padding:3px 0;">'
            '<img src="%s/%s" width="22" height="22" alt="" '
            'style="display:block;border:0;width:22px;height:22px;"></td>'
            '<td valign="middle" style="padding:3px 0;text-align:%s;font-family:%s;font-size:%dpx;'
            'white-space:nowrap;">'
            '<a href="%s" style="color:%s;text-decoration:none;">%s</a></td></tr>'
            % (IMG, icon, align, SANS, size, href, colour, label))
    out.append("</table>")
    return "".join(out)


def inline_contacts(colour=INK2, size=13, sep=GOLD):
    """One line, gold bullets between — no icons.

    Each item is nowrap so a narrow client breaks BETWEEN items; without it the
    phone splits at its hyphen and reads as two numbers.
    """
    parts = ['<a href="%s" style="color:%s;text-decoration:none;white-space:nowrap;">%s</a>'
             % (h, colour, l) for _, h, l in CONTACTS]
    dot = '<span style="color:%s;">&nbsp;&nbsp;&middot;&nbsp;&nbsp;</span>' % sep
    return ('<div style="font-family:%s;font-size:%dpx;line-height:1.9;">%s</div>'
            % (SANS, size, dot.join(parts)))


def shell(inner, bg=GROUND, rule_top=None, rule_bottom=None, pad="18px 20px"):
    border = ""
    if rule_top:
        border += "border-top:3px solid %s;" % rule_top
    if rule_bottom:
        border += "border-bottom:3px solid %s;" % rule_bottom
    return ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" '
            'bgcolor="%s" style="width:100%%;background-color:%s;%s">'
            '<tr><td align="center" valign="middle" style="padding:%s;">%s</td></tr></table>'
            % (bg, bg, border, pad, inner))


def port(logo="logo-email.png", w=200, h=70, slot=210):
    """A strict port of the GDR signature: only the colours, words and logo change.

    Every measurement below is GDR's — 16px/18px padding, a 19px name, an 11px
    tagline, 22px icons, 13px links, 3px rows.  Arial too, not the site's serif:
    swapping the typeface would be a redesign, and this is a swap.
    """
    text = (
        '<div style="font-family:%s;font-weight:bold;font-size:19px;line-height:1.15;'
        'color:%s;letter-spacing:.3px;">TOP SHELF<br>'
        '<span style="color:%s;">BUSINESS SOLUTIONS</span></div>'
        '<div style="font-family:%s;font-size:11px;font-style:italic;color:%s;'
        'padding:4px 0 9px;">%s</div>%s'
        % (SANS, INK, GOLD, SANS, INK3, SLOGAN, rows()))
    inner = (
        '<div style="text-align:center;" dir="rtl">'
        '<div style="display:inline-block;vertical-align:middle;max-width:%dpx;text-align:center;" dir="ltr">'
        '<img src="%s/%s" width="%d" height="%d" alt="Top Shelf Business Solutions" '
        'style="display:inline-block;border:0;width:%dpx;height:%dpx;"></div> '
        '<div style="display:inline-block;vertical-align:middle;width:100%%;max-width:340px;'
        'text-align:center;" dir="ltr">%s</div></div>'
        % (slot, IMG, logo, w, h, w, h, text))
    return shell(inner, rule_top=GOLD, pad="16px 18px")


def option_1():
    return port()


def option_1_mark():
    """Same port, emblem instead of the wordmark — the text already says the name."""
    return port(logo="logo-mark-email.png", w=84, h=84, slot=120)


def option_2():
    """Wordmark leads — the logo already says the name, so the text doesn't repeat it."""
    inner = (
        '<div style="text-align:center;">'
        '<img src="%s/logo-email.png" width="220" height="77" alt="Top Shelf Business Solutions" '
        'style="display:block;border:0;width:220px;height:77px;margin:0 auto;">'
        '<div style="font-family:%s;font-size:10px;letter-spacing:4px;color:%s;'
        'padding:2px 0 10px;text-transform:uppercase;">%s</div>'
        '<div style="border-top:1px solid %s;max-width:360px;margin:0 auto;padding-top:10px;">%s</div>'
        '</div>' % (IMG, SANS, GOLD, SLOGAN, HAIRLINE, inline_contacts()))
    return shell(inner, rule_top=GOLD, pad="20px")


def option_3():
    """Split — a gold hairline between the mark and the details, rule on the bottom."""
    right = (
        '<div style="font-family:%s;font-size:22px;color:%s;line-height:1.1;letter-spacing:.5px;">'
        'Top Shelf <span style="color:%s;">Business Solutions</span></div>'
        '<div style="font-family:%s;font-size:10px;letter-spacing:3px;color:%s;padding:5px 0 9px;">'
        '%s</div>%s' % (SERIF, INK, GOLD, SANS, INK3, SLOGAN.upper(), rows()))
    inner = (
        '<div style="text-align:center;" dir="rtl">'
        '<div style="display:inline-block;vertical-align:middle;max-width:120px;text-align:center;'
        'padding:0 20px;" dir="ltr">'
        '<img src="%s/logo-mark-email.png" width="80" height="80" alt="Top Shelf" '
        'style="display:inline-block;border:0;width:80px;height:80px;"></div>'
        '<div style="display:inline-block;vertical-align:middle;width:100%%;max-width:350px;'
        'text-align:center;border-right:1px solid %s;padding-right:22px;" dir="ltr">%s</div>'
        '</div>' % (IMG, HAIRLINE, right))
    return shell(inner, rule_bottom=GOLD)


def option_4():
    """Editorial — the site's serif voice, no icons, maximum restraint."""
    inner = (
        '<div style="text-align:center;">'
        '<img src="%s/logo-mark-email.png" width="52" height="52" alt="Top Shelf" '
        'style="display:block;border:0;width:52px;height:52px;margin:0 auto 10px;">'
        '<div style="font-family:%s;font-size:26px;color:%s;line-height:1.1;letter-spacing:1px;">'
        'Top Shelf</div>'
        '<div style="font-family:%s;font-size:10px;letter-spacing:5px;color:%s;padding:6px 0 0;">'
        'BUSINESS SOLUTIONS</div>'
        '<div style="font-family:%s;font-size:14px;font-style:italic;color:%s;padding:8px 0 12px;">'
        '%s</div>'
        '<div style="border-top:1px solid %s;max-width:300px;margin:0 auto;"></div>%s'
        '</div>' % (IMG, SERIF, INK, SANS, GOLD, SERIF, INK3, SLOGAN, HAIRLINE,
                    inline_contacts(size=12)))
    return shell(inner, bg=GROUND, pad="22px 20px")


def option_5():
    """Card — an inset panel with a gold hairline, sitting on the espresso ground."""
    text = (
        '<div style="font-family:%s;font-size:19px;color:%s;line-height:1.15;">'
        'Top Shelf <span style="color:%s;">Business Solutions</span></div>'
        '<div style="font-family:%s;font-size:10px;letter-spacing:3px;color:%s;padding:4px 0 8px;">'
        '%s</div>%s' % (SERIF, INK, GOLD, SANS, INK3, SLOGAN.upper(), rows()))
    card = (
        # width="100%" matters: a table with only max-width shrink-wraps to its
        # content, which starves the inline-blocks and stacks them.
        '<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" '
        'width="100%%" bgcolor="%s" style="width:100%%;max-width:560px;background-color:%s;'
        'border:1px solid %s;border-left:3px solid %s;"><tr><td style="padding:16px 20px;">'
        '<div style="text-align:center;" dir="rtl">'
        '<div style="display:inline-block;vertical-align:middle;max-width:110px;text-align:center;'
        'padding:0 14px;" dir="ltr">'
        '<img src="%s/logo-mark-email.png" width="72" height="72" alt="Top Shelf" '
        'style="display:inline-block;border:0;width:72px;height:72px;"></div>'
        '<div style="display:inline-block;vertical-align:middle;width:100%%;max-width:330px;'
        'text-align:center;" dir="ltr">%s</div></div>'
        '</td></tr></table>' % (SURFACE, SURFACE, HAIRLINE, GOLD, IMG, text))
    return shell(card, bg=GROUND, pad="14px 12px")


OPTIONS = [
    ("A-wordmark", "The port", "GDR's signature with three things changed: colours, words, logo.",
     option_1),
    ("B-emblem", "The port, emblem", "Identical, but the emblem stands in for the wordmark so the "
     "name is not read twice.", option_1_mark),
    ("2", "Wordmark Lead", "The logo already says the name, so nothing repeats it. Contact on one line.",
     option_2),
    ("3", "Gold Split", "Mark and details divided by a hairline; the gold rule moves to the bottom.",
     option_3),
    ("4", "Editorial", "The site's serif voice. No icons, wide letterspacing, most restrained.",
     option_4),
    ("5", "Inset Card", "A bordered card on the ground colour, with a gold edge down the left.",
     option_5),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    blocks = []
    for num, name, note, fn in OPTIONS:
        html = fn()
        path = os.path.join(OUT, "topshelf-signature-%s.html" % num)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        print("%-34s %5d bytes  %s" % (os.path.basename(path), len(html), name))
        blocks.append(
            '<section><h2><span>%s</span>%s</h2><p>%s</p>'
            '<div class="mail"><p class="body">Thanks &mdash; talk soon,</p>%s</div></section>'
            % (num, name, note, html))

    page = """<!doctype html><meta charset="utf-8"><title>Top Shelf email signature options</title>
<style>
 body{margin:0;padding:40px 24px 60px;background:#e9e6e1;font-family:Arial,Helvetica,sans-serif;color:#1a1a1a}
 .wrap{max-width:760px;margin:0 auto}
 h1{font-family:Georgia,serif;font-weight:400;font-size:30px;margin:0 0 6px}
 .sub{color:#666;font-size:14px;margin:0 0 40px}
 section{margin:0 0 44px}
 h2{font-size:15px;margin:0 0 4px;display:flex;align-items:center;gap:10px}
 h2 span{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;
   border-radius:50%%;background:#100C08;color:#C9A86A;font-size:13px;font-family:Georgia,serif}
 section>p{margin:0 0 12px;color:#666;font-size:13px;padding-left:36px}
 .mail{background:#fff;border:1px solid #d3cfc8;border-radius:4px;overflow:hidden}
 .body{margin:0;padding:22px 24px 26px;font-size:14px;color:#444}
</style>
<div class="wrap">
<h1>Top Shelf &mdash; email signature</h1>
<p class="sub">Five rebrands of the Your Neighborhood GDR signature. Each is shown the way it
lands at the bottom of a real message.</p>
%s
</div>""" % "\n".join(blocks)

    with open(os.path.join(OUT, "compare.html"), "w", encoding="utf-8") as fh:
        fh.write(page)
    print("\ncompare ->", os.path.join(OUT, "compare.html"))


if __name__ == "__main__":
    main()
