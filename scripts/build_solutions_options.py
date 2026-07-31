#!/usr/bin/env python3
"""
Build preview/solutions-options.html — five style treatments for the
"One Flywheel" section, now carrying all ten services instead of five.

Same ten services, same copy, in every variant. Only the treatment changes,
so the choice is about form and not about wording.
"""
import io

# (slug, name, one-liner, svg icon path-set)
S = [
 ("websites-seo", "Websites &amp; SEO", "Get found first, then earn the click with a site that loads in under three seconds.",
  '<circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><line x1="3" y1="12" x2="21" y2="12"/>'),
 ("ai-phone", "AI Phone &amp; Chat", "Every call answered, day or night. It books the job and texts back in seconds.",
  '<path d="M6.5 3.5 9 6c.3.6.2 1.3-.3 1.8L7.3 9.2a13 13 0 0 0 7.5 7.5l1.4-1.4c.5-.5 1.2-.6 1.8-.3l2.5 2.5c.6.6.6 1.6-.1 2.1-1.2 1-2.8 1.5-4.4 1.1-5.4-1.4-9.6-5.6-11-11-.4-1.6.1-3.2 1.1-4.4.5-.7 1.5-.7 2.1-.1Z"/>'),
 ("crm", "CRM &amp; Follow-Up", "Catch every lead and follow up on its own. 78% buy from whoever answers first.",
  '<path d="M4 12a8 8 0 0 1 13.7-5.6L20 8.5"/><polyline points="20,3.5 20,8.5 15,8.5"/><path d="M20 12a8 8 0 0 1-13.7 5.6L4 15.5"/><polyline points="4,20.5 4,15.5 9,15.5"/>'),
 ("reviews", "Reviews &amp; Reputation", "The wall of 5-star reviews that makes you the obvious, safe choice.",
  '<path d="M12 3.3l2.6 5.4 5.9.8-4.3 4.2 1 5.9-5.2-2.8-5.2 2.8 1-5.9-4.3-4.2 5.9-.8Z"/>'),
 ("marketing", "Marketing &amp; Social", "Stay in front of the people who already know you, without thinking about it.",
  '<path d="M3 11v2a1 1 0 0 0 1 1h2l4 4V6L6 10H4a1 1 0 0 0-1 1Z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M18.5 5.5a9 9 0 0 1 0 13"/>'),
 ("booking", "Online Booking", "Let them book at 11pm while you sleep, then cut no-shows with reminders.",
  '<rect x="3" y="5" width="18" height="16" rx="2"/><line x1="3" y1="10" x2="21" y2="10"/><line x1="8" y1="3" x2="8" y2="7"/><line x1="16" y1="3" x2="16" y2="7"/>'),
 ("payments", "Payments &amp; Financing", "Tap, card-on-file and one-tap invoices, plus financing so big jobs close.",
  '<rect x="2.5" y="5" width="19" height="14" rx="2"/><line x1="2.5" y1="9.5" x2="21.5" y2="9.5"/><line x1="6" y1="14.5" x2="10" y2="14.5"/>'),
 ("automation", "AI &amp; Automation", "The busywork that eats your evenings, handled quietly in the background.",
  '<circle cx="12" cy="12" r="3"/><path d="M12 2.5v3M12 18.5v3M4.2 6.2l2.1 2.1M17.7 15.7l2.1 2.1M2.5 12h3M18.5 12h3M4.2 17.8l2.1-2.1M17.7 8.3l2.1-2.1"/>'),
 ("memberships", "Memberships &amp; Loyalty", "Turn one-time customers into monthly revenue you can actually count on.",
  '<path d="M20.8 5.6a5 5 0 0 0-8.8-1.9A5 5 0 0 0 3.2 5.6C1.9 9 5.5 13 12 19.5 18.5 13 22.1 9 20.8 5.6Z"/>'),
 ("pos", "POS &amp; Inventory", "Know what's on the shelf, what's selling, and what to reorder. No guessing.",
  '<path d="M3 7h18l-1.5 13H4.5Z"/><path d="M8.5 7V5a3.5 3.5 0 0 1 7 0v2"/>'),
]

# Style 1 groups the ten by what the owner actually wants out of them.
GROUPS = [
 ("Get found",            "So the people already searching for what you sell land on you.",        [0, 4, 3]),
 ("Never miss a lead",    "So nothing that reaches you falls through the cracks.",                  [1, 5, 2]),
 ("Get paid faster",      "So the money that's owed to you actually arrives.",                      [6, 9]),
 ("Keep them coming back","So a customer you won once keeps paying you for years.",                 [8, 7]),
]

def icon(i, cls="ic"):
    return (f'<span class="{cls}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{S[i][3]}</svg></span>')

def v_grouped():
    out = ['<div class="v-grouped">']
    for title, blurb, idxs in GROUPS:
        out.append('  <div class="grp">')
        out.append(f'    <div class="grp-head"><h3>{title}</h3><p>{blurb}</p></div>')
        out.append('    <div class="grp-items">')
        for i in idxs:
            s = S[i]
            out.append(f'      <a class="gi" href="../{ "solution-"+s[0] }.html">{icon(i,"gi-ic")}'
                       f'<span class="gi-t">{s[1]}</span><span class="gi-b">{s[2]}</span></a>')
        out.append('    </div>')
        out.append('  </div>')
    out.append('</div>')
    return "\n".join(out)

def v_bento():
    # deliberately uneven: two wide anchors, the rest standard
    spans = {0: "wide", 1: "wide", 7: "tall"}
    out = ['<div class="v-bento">']
    for i, s in enumerate(S):
        cls = "bn " + spans.get(i, "")
        out.append(f'  <a class="{cls.strip()}" href="../solution-{s[0]}.html">{icon(i,"bn-ic")}'
                   f'<span class="bn-t">{s[1]}</span><span class="bn-b">{s[2]}</span>'
                   f'<span class="bn-go">Learn more <span aria-hidden="true">&rarr;</span></span></a>')
    out.append('</div>')
    return "\n".join(out)

def v_ring():
    out = ['<div class="v-ring">', '  <div class="ring-stage">',
           '    <div class="ring-core"><span class="ring-core-n">10</span>'
           '<span class="ring-core-l">services<br>one flywheel</span></div>']
    for i, s in enumerate(S):
        ang = (360 / len(S)) * i - 90
        out.append(f'    <a class="node" style="--a:{ang}deg" href="../solution-{s[0]}.html" '
                   f'data-name="{s[1]}" data-blurb="{s[2]}">{icon(i,"nd-ic")}<span class="nd-t">{s[1]}</span></a>')
    out.append('  </div>')
    out.append('  <p class="ring-note">Each one plugs a different gap. Running together, they feed each other.</p>')
    out.append('</div>')
    return "\n".join(out)

def v_photo():
    out = ['<div class="v-photo">']
    for i, s in enumerate(S):
        out.append(f'  <a class="ph" href="../solution-{s[0]}.html">'
                   f'<span class="ph-img"><picture>'
                   f'<source srcset="../assets/img/solution/{s[0]}-hero.webp" type="image/webp">'
                   f'<img src="../assets/img/solution/{s[0]}-hero.jpg" alt="" loading="lazy"></picture></span>'
                   f'<span class="ph-body"><span class="ph-t">{s[1]}</span>'
                   f'<span class="ph-b">{s[2]}</span></span></a>')
    out.append('</div>')
    return "\n".join(out)

def v_index():
    out = ['<div class="v-index">']
    for i, s in enumerate(S):
        out.append(f'  <a class="ix" href="../solution-{s[0]}.html">'
                   f'<span class="ix-n">{i+1:02d}</span>{icon(i,"ix-ic")}'
                   f'<span class="ix-t">{s[1]}</span><span class="ix-b">{s[2]}</span>'
                   f'<span class="ix-go" aria-hidden="true">&rarr;</span></a>')
    out.append('</div>')
    return "\n".join(out)

VARIANTS = [
 ("grouped", "1 &middot; Grouped by outcome", v_grouped()),
 ("bento",   "2 &middot; Bento grid",         v_bento()),
 ("ring",    "3 &middot; Flywheel ring",      v_ring()),
 ("photo",   "4 &middot; Photo mosaic",       v_photo()),
 ("index",   "5 &middot; Numbered index",     v_index()),
]

CSS = io.open("scripts/solutions_options.css", encoding="utf-8").read()

sections = "\n".join(
    f'<section class="sec rule-top variant" id="v-{k}"{"" if n==0 else " hidden"}>\n'
    f'  <div class="container">\n'
    f'    <div class="section-head" style="text-align:center;max-width:62ch;margin-inline:auto">\n'
    f'      <span class="eyebrow" style="justify-content:center">The Stack</span>\n'
    f'      <h2 class="display display-lg" style="margin-top:1.6rem">Ten Services. <em>One Flywheel.</em></h2>\n'
    f'      <p style="margin-inline:auto">Each one closes a specific gap. Run together, they keep working while '
    f'you&rsquo;re on a job, at home, or asleep.</p>\n'
    f'    </div>\n{body}\n  </div>\n</section>'
    for n, (k, _, body) in enumerate(VARIANTS)
)

buttons = "\n".join(
    f'  <button data-v="{k}" aria-pressed="{"true" if n==0 else "false"}">{label}</button>'
    for n, (k, label, _) in enumerate(VARIANTS)
)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,nofollow">
<title>Top Shelf — Solutions Section, 5 Style Options</title>
<link rel="icon" href="../assets/logo-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400;1,500;1,600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/site.css?v=20260731b">
<style>
{CSS}
</style>
</head>
<body>
<div id="page">
{sections}
</div>

<p class="vnote">Same ten services and same copy in all five &mdash; only the treatment changes.</p>
<div class="vpicker" role="group" aria-label="Section style options">
  <span class="lbl">Style</span>
{buttons}
</div>

<script>
(function () {{
  var btns = [].slice.call(document.querySelectorAll('.vpicker button'));
  function show(k) {{
    document.querySelectorAll('.variant').forEach(function (s) {{ s.hidden = (s.id !== 'v-' + k); }});
    btns.forEach(function (b) {{ b.setAttribute('aria-pressed', String(b.dataset.v === k)); }});
    try {{ history.replaceState(null, '', '#' + k); }} catch (e) {{}}
    window.scrollTo(0, 0);
  }}
  btns.forEach(function (b) {{ b.addEventListener('click', function () {{ show(b.dataset.v); }}); }});
  var h = location.hash.replace('#', '');
  if (h && document.getElementById('v-' + h)) show(h);
  window.addEventListener('keydown', function (e) {{
    var i = btns.findIndex(function (b) {{ return b.getAttribute('aria-pressed') === 'true'; }});
    if (e.key === 'ArrowRight') show(btns[(i + 1) % btns.length].dataset.v);
    if (e.key === 'ArrowLeft')  show(btns[(i - 1 + btns.length) % btns.length].dataset.v);
  }});
}})();
</script>
</body>
</html>
"""

io.open("preview/solutions-options.html", "w", encoding="utf-8", newline="").write(html)
print("built preview/solutions-options.html with", len(VARIANTS), "variants x", len(S), "services")
