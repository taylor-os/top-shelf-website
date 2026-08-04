#!/usr/bin/env python3
"""
Fix the Signature Blend band.

It was dropped onto 21 pages with one piece of copy — "Everything Above,
Working Together" — regardless of what was actually above it. On most pages
nothing above it enumerated anything, so the headline referred to a list that
did not exist, and the price appeared with no context to justify it.

Three changes:
  * index.html      remove it. It sat below the case studies, several sections
                    after the tier cards, referring to nothing.
  * industry pages  MOVE it to directly after the "Every Piece Is Someone's
                    Full-Time Job" comparison, which is the only place on those
                    pages where a price lands with context. It currently sits
                    after a "Not quite your world?" cross-link block.
  * everywhere      rewrite the copy so it follows from what it actually sits
                    under. The comparison lists six separate hires, so the band
                    now says exactly that.
"""
import io, re, glob, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# --- the two copy variants -------------------------------------------------
AFTER_COMPARISON = (
    '        <span class="eyebrow">Most Popular &middot; $899/mo</span>\n'
    '        <p class="sig-band-title">One Bill Instead of <em>Six</em></p>\n'
    '        <p class="sig-band-copy">That list is six separate hires. The Signature Blend is all of it '
    'on one team and one invoice &mdash; your website, your CRM, your reviews, your follow-up, and an AI '
    'receptionist that answers at midnight &mdash; with your new website included.</p>\n'
)

AFTER_AUDIT = (
    '        <span class="eyebrow">Most Popular &middot; $899/mo</span>\n'
    '        <p class="sig-band-title">Where Most Owners <em>Start</em></p>\n'
    '        <p class="sig-band-copy">The audit tells you what&rsquo;s costing you. The Signature Blend '
    'is what closes it &mdash; website, CRM, reviews, follow-up, and an AI receptionist that answers at '
    'midnight, on one team and one invoice, with your new website included.</p>\n'
)

BAND_SECTION = re.compile(
    r'[ \t]*<section class="section rule-top">\s*\n'
    r'\s*<div class="container">\s*\n'
    r'\s*<div class="sig-band[^"]*">.*?\n\s*</section>\n',
    re.S)

def band_html(copy):
    return (
        '<section class="section rule-top">\n'
        '  <div class="container">\n'
        '    <div class="sig-band reveal">\n'
        '      <div>\n'
        f'{copy}'
        '      </div>\n'
        '      <a href="pricing.html#signature" class="btn btn-gold sig-band-cta">See the Signature Blend '
        '<span class="arr">&rarr;</span></a>\n'
        '    </div>\n'
        '  </div>\n'
        '</section>\n')

def strip_band(s):
    m = BAND_SECTION.search(s)
    return (s[:m.start()] + s[m.end():], True) if m else (s, False)

def comparison_section_end(s):
    """Index just after the </section> that closes the comparison table."""
    i = s.find('Full-Time Job')
    if i < 0:
        return None
    j = s.find('</section>', i)
    return j + len('</section>\n') if j > 0 else None

removed = moved = recopied = 0

for p in sorted(glob.glob("*.html")):
    if p == "home-centered-review.html":       # untracked local review copy, not mine
        continue
    s = io.open(p, encoding="utf-8").read()
    if 'sig-band' not in s:
        continue

    # 1 · homepage: remove outright
    if p == "index.html":
        s, ok = strip_band(s)
        if ok:
            io.open(p, "w", encoding="utf-8", newline="").write(s)
            removed += 1
            print(f"  removed   {p}")
        continue

    is_industry = p.startswith("industry-")
    has_table = 'Full-Time Job' in s
    copy = AFTER_COMPARISON if has_table else AFTER_AUDIT

    s2, ok = strip_band(s)
    if not ok:
        print(f"  !! {p}: band not matched"); continue

    if is_industry and has_table:
        # 2 · reposition to sit directly under the comparison
        end = comparison_section_end(s2)
        if end:
            s2 = s2[:end] + "\n" + band_html(copy) + s2[end:]
            moved += 1
            print(f"  moved     {p}  -> under the comparison")
        else:
            s2 = s2 + band_html(copy)
    else:
        # 3 · put it back where it was, with corrected copy
        m = BAND_SECTION.search(s)
        s2 = s2[:m.start()] + band_html(copy) + s2[m.start():]
        recopied += 1
        which = "comparison" if has_table else "audit"
        print(f"  rewrote   {p}  ({which} variant)")

    io.open(p, "w", encoding="utf-8", newline="").write(s2)

print(f"\nremoved {removed} | moved {moved} | rewrote {recopied}")
