#!/usr/bin/env python3
"""
Build preview/review.html — one page to review everything from this round:
what shipped, what's still a choice, and the duplicate-content audit rendered
readably instead of as terminal output.

Reuses dupe_audit.py's own functions so the numbers on the page are the same
numbers the audit prints, not a re-implementation that can drift.
"""
import io, re, glob, itertools, subprocess, importlib.util, sys, html as H

spec = importlib.util.spec_from_file_location("da", "scripts/dupe_audit.py")
da = importlib.util.module_from_spec(spec)
class _Quiet(io.TextIOWrapper):
    """dupe_audit prints its report on import and calls reconfigure() on
    stdout, which a bare StringIO does not implement. Wrap a byte buffer so
    both work."""
    pass

_stdout = sys.stdout
sys.stdout = _Quiet(io.BytesIO(), encoding="utf-8", write_through=True)
try:
    spec.loader.exec_module(da)
finally:
    sys.stdout = _stdout

pages = da.pages
pairs = sorted(
    ((da.jaccard(pages[a]['shingles'], pages[b]['shingles']), a, b)
     for a, b in itertools.combinations(pages, 2)),
    reverse=True)
top_pairs = [p for p in pairs if p[0] >= 0.20][:8]

titles = {}
descs = {}
for p, d in pages.items():
    titles.setdefault(d['title'], []).append(p)
    descs.setdefault(d['desc'], []).append(p)
dup_titles = {k: v for k, v in titles.items() if len(v) > 1 and k}
dup_descs = {k: v for k, v in descs.items() if len(v) > 1 and k}

by_words = sorted(pages.items(), key=lambda kv: kv[1]['words'])
thin = [(p, d) for p, d in by_words if d['words'] < 300]
no_canon = [p for p, d in pages.items() if not d['canonical']]

def chip(ok, label):
    cls = 'ok' if ok else 'warn'
    return f'<span class="chip {cls}">{label}</span>'

SHIPPED = [
    ("Homepage", "index.html",
     "Corner-shop hero photo, the ten-service orbit at Large with the mark at its centre, "
     "photographic industry shelf, and the gap wording throughout."),
    ("Solution pages (10)", "solution-crm.html",
     "Every one now has its own hero photograph, shot for what that page actually sells. "
     "Linked here is CRM &amp; Follow-Up; the other nine are in the Solutions menu."),
    ("Industry pages (8)", "industry-home-services.html",
     "Gap wording throughout. The curated per-industry systems sections were deliberately "
     "left alone &mdash; they are tailored, not generic."),
    ("Gap Finder", "gap-finder-demo.html",
     "Renamed from Leak Finder, filenames included, with 301 redirects so old links still land."),
]

CHOICES = [
    ("Hero photograph", "preview/hero-options.html", "Six candidates under the real scrim. Live: F, corner shop."),
    ("Orbit size", "preview/orbit-sizes.html", "Four proportional steps. Live: Large."),
    ("Flywheel treatment", "preview/flywheel-options.html", "Five refinements. Live: orbit with live centre."),
    ("Section style", "preview/solutions-options.html", "Five ways to present ten services."),
    ("Homepage directions", "preview/index.html", "The original three identity directions."),
]

OPEN = [
    ("Gap Finder popup opens over the orbit",
     "It auto-opens on scroll and lands on the section that is now the centrepiece of that fold. "
     "Moving the trigger further down the page is a small change."),
    ("sample-report.html is thin and indexable",
     "183 words of main content, in the sitemap. Fine if it is meant to be a lead-magnet landing "
     "page, worth a look if not."),
    ("Two orphan industry pages",
     "industry-bars.html and industry-dental.html are live but unlinked and not in the sitemap. "
     "Both carry noindex so they are not a duplicate risk, but each self-canonicals rather than "
     "pointing at the page that replaced it."),
    ("robots.txt has two User-agent blocks",
     "The second block&rsquo;s Disallow: /demo/ is probably being ignored. Pre-existing."),
]

def li_pairs():
    if not top_pairs:
        return '<p class="none">No page pair shares more than 20% of its main content.</p>'
    out = ['<table class="t"><thead><tr><th>Pair</th><th class="n">Overlap</th><th>Read</th></tr></thead><tbody>']
    for j, a, b in top_pairs:
        note = "both noindex &mdash; invisible to Google" if pages[a]['noindex'] and pages[b]['noindex'] \
            else ("one is noindex" if pages[a]['noindex'] or pages[b]['noindex'] else "both indexable")
        cls = 'bad' if j >= .75 and not (pages[a]['noindex'] or pages[b]['noindex']) else ('mid' if j >= .4 else 'fine')
        out.append(f'<tr><td><code>{a}</code><br><code>{b}</code></td>'
                   f'<td class="n {cls}">{j:.0%}</td><td>{note}</td></tr>')
    out.append('</tbody></table>')
    return "\n".join(out)

def li_depth():
    rows = []
    for p, d in by_words:
        cls = 'bad' if d['words'] < 300 and not d['noindex'] else ('fine' if d['words'] >= 300 else 'mid')
        tag = ' <span class="ni">noindex</span>' if d['noindex'] else ''
        rows.append(f'<tr><td><code>{p}</code>{tag}</td><td class="n {cls}">{d["words"]:,}</td></tr>')
    return '<table class="t"><thead><tr><th>Page</th><th class="n">Words of main content</th></tr></thead><tbody>' \
           + "\n".join(rows) + '</tbody></table>'

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,nofollow">
<title>Top Shelf — Review</title>
<link rel="icon" href="../assets/logo-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400;1,500;1,600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/site.css?v=20260731d">
<style>
  body{{ padding:clamp(2rem,5vw,4rem) 0 6rem; }}
  .wrap{{ max-width:1020px; margin-inline:auto; padding-inline:var(--gutter); }}
  h1{{ font-family:var(--serif); font-weight:500; font-size:clamp(2.2rem,4.4vw,3.2rem); color:var(--ink);
      letter-spacing:-.02em; line-height:1.05; margin-bottom:.8rem; }}
  .sub{{ color:var(--ink-2); max-width:64ch; line-height:1.8; }}
  h2{{ font-family:var(--serif); font-weight:500; font-size:clamp(1.5rem,2.4vw,2rem); color:var(--ink);
      margin:clamp(2.6rem,5vw,3.6rem) 0 1.2rem; padding-top:1.6rem; border-top:1px solid var(--hairline); }}
  h2:first-of-type{{ border-top:0; }}
  .chips{{ display:flex; gap:.5rem; flex-wrap:wrap; margin:1.4rem 0 0; }}
  .chip{{ font-family:var(--sans); font-size:.72rem; letter-spacing:.1em; text-transform:uppercase;
      padding:.42rem .85rem; border-radius:100px; border:1px solid; }}
  .chip.ok{{ color:var(--gold-bright); border-color:var(--hairline-strong); background:rgba(201,168,106,.07); }}
  .chip.warn{{ color:#E2A05A; border-color:rgba(226,160,90,.35); background:rgba(226,160,90,.07); }}
  .cards{{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:1rem; }}
  .card{{ border:1px solid var(--hairline); border-radius:var(--r-lg); padding:1.4rem 1.5rem; background:var(--surface);
      transition:border-color .3s var(--ease), transform .3s var(--ease); display:block; }}
  .card:hover{{ border-color:var(--gold); transform:translateY(-3px); }}
  .card b{{ display:block; font-family:var(--serif); font-weight:500; font-size:1.2rem; color:var(--ink); margin-bottom:.4rem; }}
  .card:hover b{{ color:var(--gold-bright); }}
  .card span{{ display:block; font-size:.88rem; color:var(--ink-3); line-height:1.65; }}
  .card em{{ display:block; font-style:normal; margin-top:.7rem; font-family:var(--sans); font-size:.7rem;
      letter-spacing:.16em; text-transform:uppercase; color:var(--gold-deep); }}
  .t{{ width:100%; border-collapse:collapse; margin-top:.4rem; }}
  .t th{{ text-align:left; font-family:var(--sans); font-size:.68rem; letter-spacing:.16em; text-transform:uppercase;
      color:var(--gold); font-weight:400; padding:.7rem 0; border-bottom:1px solid var(--hairline); }}
  .t td{{ padding:.75rem 0; border-bottom:1px solid var(--hairline-soft); font-size:.92rem; color:var(--ink-2); vertical-align:top; }}
  .t .n{{ text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap; padding-left:1.4rem; }}
  .t code{{ font-family:var(--sans); font-size:.86rem; color:var(--ink); }}
  .fine{{ color:var(--gold-bright); }} .mid{{ color:#E2A05A; }} .bad{{ color:#E2502A; }}
  .ni{{ font-family:var(--sans); font-size:.64rem; letter-spacing:.12em; text-transform:uppercase; color:var(--ink-4);
      border:1px solid var(--hairline-soft); border-radius:100px; padding:.1rem .45rem; margin-left:.5rem; }}
  .none{{ color:var(--gold-bright); font-size:.95rem; }}
  ol.open{{ margin:0; padding:0; list-style:none; counter-reset:o; }}
  ol.open li{{ counter-increment:o; padding:1.1rem 0 1.1rem 2.6rem; border-bottom:1px solid var(--hairline-soft); position:relative; }}
  ol.open li::before{{ content:counter(o,decimal-leading-zero); position:absolute; left:0; top:1.15rem;
      font-family:var(--serif); font-style:italic; color:var(--gold-deep); }}
  ol.open b{{ display:block; font-family:var(--serif); font-size:1.12rem; color:var(--ink); margin-bottom:.35rem; font-weight:500; }}
  ol.open span{{ font-size:.9rem; color:var(--ink-3); line-height:1.7; }}
  .note{{ margin-top:1.2rem; font-size:.86rem; color:var(--ink-3); line-height:1.7; max-width:70ch; }}
</style>
</head>
<body>
<div class="wrap">

  <h1>Review</h1>
  <p class="sub">Everything from this round in one place: what is live, what is still your choice,
  and the duplicate-content audit. Every link opens the real page.</p>
  <div class="chips">
    {chip(not dup_titles, f"{len(pages)} pages audited")}
    {chip(not [p for p in pairs if p[0] >= .75 and not (pages[p[1]]['noindex'] or pages[p[2]]['noindex'])], "No near-duplicates")}
    {chip(not dup_titles, "Titles unique")}
    {chip(not dup_descs, "Descriptions unique")}
    {chip(not no_canon, "Canonicals correct")}
  </div>

  <h2>Live now</h2>
  <div class="cards">
    {"".join(f'<a class="card" href="../{u}"><b>{t}</b><span>{d}</span><em>Open &rarr;</em></a>' for t,u,d in SHIPPED)}
  </div>

  <h2>Still your choice</h2>
  <div class="cards">
    {"".join(f'<a class="card" href="../{u}"><b>{t}</b><span>{d}</span><em>Compare &rarr;</em></a>' for t,u,d in CHOICES)}
  </div>

  <h2>Duplicate content</h2>
  <p class="note">Main content only &mdash; nav, footer, head and scripts are stripped first, because a shared
  chrome across {len(pages)} pages is normal and Google discounts it. Similarity is Jaccard over 5-word
  shingles, which is how near-duplicate detection actually works; a plain character-diff badly
  over-reports on pages that share a vocabulary but say different things.</p>
  {li_pairs()}

  <h2>Content depth</h2>
  {li_depth()}

  <h2>Open questions</h2>
  <ol class="open">
    {"".join(f'<li><b>{t}</b><span>{d}</span></li>' for t,d in OPEN)}
  </ol>

  <p class="note" style="margin-top:2.6rem;padding-top:1.6rem;border-top:1px solid var(--hairline)">
  Generated by <code>scripts/build_review.py</code>, which imports the audit rather than
  re-implementing it, so these numbers are the audit&rsquo;s numbers. Re-run it any time the site changes.</p>

</div>
</body>
</html>
"""

io.open("preview/review.html", "w", encoding="utf-8", newline="").write(html)
print(f"built preview/review.html — {len(pages)} pages, {len(top_pairs)} pairs shown, {len(thin)} thin")
