#!/usr/bin/env python3
"""
Build preview/flywheel-options.html — five refined treatments of the
"ten services, one flywheel" idea.

The first ring attempt was right in concept and weak in execution: tiny
wrapping labels, uncontained icons, a plain 1px circle, a dead centre, and
per-service copy that was written but never shown. Each option below fixes
those and pushes the idea somewhere different.
"""
import io, math

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

GROUPS = [
 ("Get found",             [0, 4, 3]),
 ("Never miss a lead",     [1, 5, 2]),
 ("Get paid faster",       [6, 9]),
 ("Keep them coming back", [8, 7]),
]

def svg_icon(i, cls):
    return (f'<span class="{cls}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{S[i][3]}</svg></span>')

# --------------------------------------------------------------------------
# 1 · Orbit with a live centre panel. Hover or focus a node and the centre
#     explains it, so the dead middle finally does work and the per-service
#     copy is actually read.
# --------------------------------------------------------------------------
def v_orbit():
    o = ['<div class="fw fw-orbit">', '  <div class="orb-stage">',
         '    <div class="orb-centre" id="orbCentre">',
         '      <span class="orb-rest">',
         '        <span class="orb-n">10</span>',
         '        <span class="orb-l">services<br>one flywheel</span>',
         '      </span>',
         '      <span class="orb-detail" aria-live="polite">',
         '        <span class="orb-d-t"></span><span class="orb-d-b"></span>',
         '        <span class="orb-d-go">Learn more &rarr;</span>',
         '      </span>',
         '    </div>']
    for i, s in enumerate(S):
        ang = (360 / len(S)) * i - 90
        o.append(f'    <a class="orb-node" style="--a:{ang}deg" href="../solution-{s[0]}.html" '
                 f'data-t="{s[1]}" data-b="{s[2]}"><span class="orb-chip">{svg_icon(i,"orb-ic")}</span>'
                 f'<span class="orb-name">{s[1]}</span></a>')
    o += ['  </div>', '</div>']
    return "\n".join(o)

# --------------------------------------------------------------------------
# 2 · Segmented dial. The ring itself carries the information: ten real arc
#     segments, gauge-like, that light as you move along them.
# --------------------------------------------------------------------------
def v_dial():
    R, C = 180, 2 * math.pi * 180
    seg = C / len(S)
    gap = 10
    o = ['<div class="fw fw-dial">', '  <div class="dial-stage">',
         f'    <svg class="dial-svg" viewBox="0 0 400 400" aria-hidden="true">',
         f'      <circle cx="200" cy="200" r="{R}" class="dial-track" fill="none" stroke-width="14"/>']
    for i in range(len(S)):
        off = -seg * i
        o.append(f'      <circle cx="200" cy="200" r="{R}" class="dial-seg" data-i="{i}" fill="none" '
                 f'stroke-width="14" stroke-linecap="butt" '
                 f'stroke-dasharray="{seg-gap:.2f} {C-seg+gap:.2f}" stroke-dashoffset="{off:.2f}" '
                 f'transform="rotate(-90 200 200)"/>')
    o.append('    </svg>')
    o.append('    <div class="dial-centre"><span class="dial-n">10</span>'
             '<span class="dial-l">services<br>one flywheel</span></div>')
    for i, s in enumerate(S):
        ang = (360 / len(S)) * i - 90 + (360 / len(S)) / 2
        o.append(f'    <a class="dial-node" style="--a:{ang}deg" data-i="{i}" href="../solution-{s[0]}.html">'
                 f'{svg_icon(i,"dial-ic")}<span class="dial-name">{s[1]}</span></a>')
    o += ['  </div>',
          '  <p class="fw-note">Ten segments, one wheel. Each one closes a different gap.</p>',
          '</div>']
    return "\n".join(o)

# --------------------------------------------------------------------------
# 3 · Momentum loop. Reads as a sequence with direction: numbered, arrowed,
#     and a light that travels the loop so it looks like it turns.
# --------------------------------------------------------------------------
def v_momentum():
    o = ['<div class="fw fw-momentum">', '  <div class="mom-stage">',
         '    <svg class="mom-svg" viewBox="0 0 400 400" aria-hidden="true">',
         '      <circle cx="200" cy="200" r="168" class="mom-track" fill="none" stroke-width="1"/>',
         '      <circle cx="200" cy="200" r="168" class="mom-run" fill="none" stroke-width="2"/>',
         '    </svg>',
         '    <div class="mom-centre"><span class="mom-l">It compounds</span>'
         '<span class="mom-b">Every service feeds the next one</span></div>']
    for i, s in enumerate(S):
        ang = (360 / len(S)) * i - 90
        o.append(f'    <a class="mom-node" style="--a:{ang}deg" href="../solution-{s[0]}.html">'
                 f'<span class="mom-num">{i+1:02d}</span><span class="mom-name">{s[1]}</span></a>')
    o += ['  </div>', '</div>']
    return "\n".join(o)

# --------------------------------------------------------------------------
# 4 · Grouped orbit. Two rings: the four outcomes on the inside, the ten
#     services arranged around their own outcome on the outside.
# --------------------------------------------------------------------------
def v_grouped_orbit():
    o = ['<div class="fw fw-go">', '  <div class="go-stage">',
         '    <div class="go-centre"><span class="go-n">10</span><span class="go-l">services</span></div>']
    # quadrant per group, services fanned inside their quadrant
    start = -90
    total = len(S)
    idx = 0
    for gi, (title, members) in enumerate(GROUPS):
        span = 360 * len(members) / total
        mid = start + span / 2
        o.append(f'    <span class="go-grp" style="--a:{mid}deg">{title}</span>')
        for k, m in enumerate(members):
            a = start + span * (k + .5) / len(members)
            s = S[m]
            o.append(f'    <a class="go-node" style="--a:{a}deg" href="../solution-{s[0]}.html">'
                     f'{svg_icon(m,"go-ic")}<span class="go-name">{s[1]}</span></a>')
        start += span
    o += ['  </div>',
          '  <p class="fw-note">Four jobs to be done. Ten services doing them.</p>',
          '</div>']
    return "\n".join(o)

# --------------------------------------------------------------------------
# 5 · Continuous track. Drops the circle but keeps the point: a loop that
#     never stops, running horizontally so it works on a phone.
# --------------------------------------------------------------------------
def v_track():
    def row(dup=False):
        out = []
        for i, s in enumerate(S):
            out.append(f'      <a class="tk-item" href="../solution-{s[0]}.html"{" aria-hidden=\"true\" tabindex=\"-1\"" if dup else ""}>'
                       f'{svg_icon(i,"tk-ic")}<span class="tk-t">{s[1]}</span>'
                       f'<span class="tk-b">{s[2]}</span></a>')
            out.append('      <span class="tk-arrow" aria-hidden="true">&rarr;</span>')
        return "\n".join(out)
    return "\n".join([
      '<div class="fw fw-track">',
      '  <div class="tk-rail">',
      '    <div class="tk-run">',
      row(), row(dup=True),
      '    </div>',
      '  </div>',
      '  <p class="fw-note">It only stops when you do. Hover to hold it still.</p>',
      '</div>'])

VARIANTS = [
 ("orbit",    "1 &middot; Orbit + live centre", v_orbit()),
 ("dial",     "2 &middot; Segmented dial",      v_dial()),
 ("momentum", "3 &middot; Momentum loop",       v_momentum()),
 ("grouped",  "4 &middot; Grouped orbit",       v_grouped_orbit()),
 ("track",    "5 &middot; Continuous track",    v_track()),
]

CSS = io.open("scripts/flywheel_options.css", encoding="utf-8").read()

sections = "\n".join(
    f'<section class="sec rule-top variant" id="v-{k}"{"" if n==0 else " hidden"}>\n'
    f'  <div class="container">\n'
    f'    <div class="section-head" style="text-align:center;max-width:62ch;margin-inline:auto">\n'
    f'      <span class="eyebrow" style="justify-content:center">The Stack</span>\n'
    f'      <h2 class="display display-lg" style="margin-top:1.6rem">Ten Services. <em>One Flywheel.</em></h2>\n'
    f'      <p style="margin-inline:auto">Each one closes a specific gap. Run together, they keep working while '
    f'you&rsquo;re on a job, at home, or asleep.</p>\n'
    f'    </div>\n{body}\n  </div>\n</section>'
    for n, (k, _, body) in enumerate(VARIANTS))

buttons = "\n".join(
    f'  <button data-v="{k}" aria-pressed="{"true" if n==0 else "false"}">{label}</button>'
    for n, (k, label, _) in enumerate(VARIANTS))

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,nofollow">
<title>Top Shelf — Flywheel Section, 5 Refined Ideas</title>
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

<p class="vnote">Five refinements of the same idea &mdash; ten services, one wheel.</p>
<div class="vpicker" role="group" aria-label="Flywheel style options">
  <span class="lbl">Idea</span>
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

  /* 1 · orbit — the centre reports whichever node has hover or focus */
  var centre = document.getElementById('orbCentre');
  if (centre) {{
    var t = centre.querySelector('.orb-d-t'), b = centre.querySelector('.orb-d-b');
    document.querySelectorAll('.orb-node').forEach(function (n) {{
      function on() {{ t.innerHTML = n.dataset.t; b.textContent = n.dataset.b; centre.classList.add('is-on'); }}
      function off() {{ centre.classList.remove('is-on'); }}
      n.addEventListener('mouseenter', on); n.addEventListener('focus', on);
      n.addEventListener('mouseleave', off); n.addEventListener('blur', off);
    }});
  }}

  /* 2 · dial — hovering a label lights its matching arc, and vice versa */
  document.querySelectorAll('.fw-dial').forEach(function (root) {{
    var segs = root.querySelectorAll('.dial-seg');
    root.querySelectorAll('.dial-node').forEach(function (n) {{
      function on() {{ segs.forEach(function (s) {{ s.classList.toggle('is-on', s.dataset.i === n.dataset.i); }}); }}
      function off() {{ segs.forEach(function (s) {{ s.classList.remove('is-on'); }}); }}
      n.addEventListener('mouseenter', on); n.addEventListener('focus', on);
      n.addEventListener('mouseleave', off); n.addEventListener('blur', off);
    }});
  }});
}})();
</script>
</body>
</html>
"""
io.open("preview/flywheel-options.html", "w", encoding="utf-8", newline="").write(html)
print("built preview/flywheel-options.html —", len(VARIANTS), "ideas x", len(S), "services")
