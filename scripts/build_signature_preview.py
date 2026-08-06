"""Wrap the signature fragments as standalone pages for the Taylor OS preview host.

The generated files are fragments — a bare table meant to be pasted into a mail
client.  Reviewing one on a blank white page tells you nothing about how it
lands, so each is shown here sitting under a short message the way it will in an
inbox.  Self-contained: no relative paths, since the preview host serves each
item on its own.

Usage: python build_signature_preview.py   ->  .libgen/signatures/preview/
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIGS = os.path.join(ROOT, ".libgen", "signatures")
OUT = os.path.join(SIGS, "preview")

# Lifted verbatim from FieldPro's CompanySignature.php so the comparison is
# against what actually goes out, not a copy that has drifted.
GDR = os.path.expanduser(r"~\FieldPro\app\Mail\CompanySignature.php")

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title><style>
 body{margin:0;padding:24px 16px 48px;background:#e9e6e1;
   font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif}
 .wrap{max-width:680px;margin:0 auto}
 h2{font-size:11px;font-weight:400;color:#7a746c;margin:22px 0 8px;
   text-transform:uppercase;letter-spacing:2px}
 h2:first-child{margin-top:0}
 .mail{background:#fff;border:1px solid #d3cfc8;border-radius:3px;overflow:hidden}
 .from{padding:14px 20px 0;font-size:12px;color:#8a847c;border-bottom:1px solid #eee;
   padding-bottom:12px}
 .body{margin:0;padding:20px 20px 24px;font-size:14px;line-height:1.6;color:#3a3a3a}
</style></head><body><div class="wrap">%s</div></body></html>"""

FRAME = """<h2>%s</h2>
<div class="mail">
 <div class="from">Top Shelf Business Solutions &lt;contact@topshelfsolutions.io&gt;</div>
 <p class="body">Hi Dana,<br><br>Good talking today. I've put the walkthrough together &mdash;
 have a look and tell me what you think.<br><br>Thanks &mdash; talk soon,</p>%s</div>"""


def gdr_markup():
    """The GDR signature out of the PHP heredoc that ships it."""
    src = open(GDR, encoding="utf-8").read()
    start = src.index("<table", src.index("GDR"))
    return src[start:src.index("</table>", src.rindex("</tr>", start)) + 8]


def page(path, title, frames):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(PAGE % (title, "\n".join(FRAME % f for f in frames)))
    return path


def main():
    os.makedirs(OUT, exist_ok=True)
    read = lambda n: open(os.path.join(SIGS, n), encoding="utf-8").read()
    a, b = read("topshelf-signature-A-wordmark.html"), read("topshelf-signature-B-emblem.html")

    made = [
        page(os.path.join(OUT, "A-wordmark.html"), "Option A — wordmark",
             [("Option A &mdash; wordmark in the logo slot", a)]),
        page(os.path.join(OUT, "B-emblem.html"), "Option B — emblem",
             [("Option B &mdash; emblem in the logo slot", b)]),
        page(os.path.join(OUT, "side-by-side.html"), "A and B against the GDR original",
             [("The GDR original, for reference", gdr_markup()),
              ("Option A &mdash; wordmark", a),
              ("Option B &mdash; emblem", b)]),
    ]
    for p in made:
        print("%-16s %6.1f KB" % (os.path.basename(p), os.path.getsize(p) / 1024))


if __name__ == "__main__":
    main()
