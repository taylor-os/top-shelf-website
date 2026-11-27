# Task for each concept builder: one complete Top Shelf site concept

Worktree `C:\Users\taylo\top-shelf-website-focus` (branch feat/crm-website-focus). Do not commit or push; the orchestrator does. Never edit files outside your own concept folders, listed below.

## What Taylor asked for (verbatim)
"create a few visually stunning websites for TOP SHELF with all the same information so I can compare and take what I like from each. All the renders, CRM, and website products and information will be the same its just giving me different ideas for the website." The 3 new concepts "can do any color and font just keep the Logo Initials and style". Each concept has a "Homepage Plus a CRM page and a Website page or the CRM and websites can be hand in hand as an industries page and then each industry branches off into a CRM and website page for that industry but there should also be a general CRM and General Website page".

## Read first
- `docs/superpowers/specs/2026-11-26-industry-pairs-and-site-concepts-design.md` (spec + decisions) and `docs/superpowers/plans/2026-11-27-industry-pairs-and-site-concepts.md` (Global Constraints).
- `docs/superpowers/specs/2026-11-26-crm-page-research.md`: what buyers want and fear, how competitors present themselves, and what we must not claim.
- `renders-src/site-content/content.json`: ALL copy comes from here (headings, benefits, FAQ, prices, per-industry intros). You may shorten or split it for layout, but never add claims, stats, testimonials, counts or prices.
- `renders-src/industry-crm/pairs.json`: the 12 industry pairs (business, website_dir, slug, brand).
- `renders-src/industry-crm/captions.json`: each industry's 6 CRM screens (file, device, role, caption). The vet set will be added later with the same shape; your generator must read the file at build time, not hard-code it.

## Assets (reference by relative path; never copy into your folder)
- CRM screens: `assets/img/crm/industries/<slug>/<file>.webp` (desktop 1440x900, phone 585x1266). They are being re-skinned to their websites tonight; same filenames, so just reference them.
- Website screenshots: `assets/img/websites/<website-dir-basename>-home-d.webp` (1200 wide) and `-home-m.webp` (585 wide). Three are coming later: `bramlett-motor-co`, `larkspur-strength-club`, `kestrel-lane-detail`.
- Live sample websites to link: `websites/<dir>/index.html`.
- Logo: keep the Top Shelf initials mark and style: `assets/logo-mark.png` (and `assets/logo-full.png`). Recolor only with CSS filters or a faithful SVG trace; don't redraw it as something else.
- CTA: "Try the CRM" links to the real `contact.html`; secondary "Call or text (469) 833-3033".
- No paid image generation and no downloads. Use CSS/SVG art, the screens, and the website shots.

## Build
- Output `preview/concepts-2026-11/<id>/`:
  - `index.html`: home
  - `crm.html`: the general CRM page, all benefits, how it works, day one, anti-trap, FAQ, price
  - `websites.html`: the general website page, the $499 offer, and every sample site as a card
  - `industries.html`: the hub, where each industry shows its website and its CRM together
  - For each of the 12 slugs, `industries/<slug>-crm.html` (that business's 6 CRM screens with captions, and the industry intro) and `industries/<slug>-website.html` (that business's website shot, what the $499 site includes, and a link to the live sample site)
- Write a generator at `scripts/concepts/<id>/build.py` (plus your templates and CSS under `scripts/concepts/<id>/` and `preview/concepts-2026-11/<id>/assets/`). It reads content.json, pairs.json and captions.json and writes every page. Re-running it must give the same output.
- Every page needs `<meta name="robots" content="noindex,nofollow">`, a real `<title>`, and a small visible "Concept <id> · design preview" tag.
- Show "Sample screens" / "Sample website" labels wherever samples appear.
- Pairs are one business: a website and its CRM always appear together and are named as the same business.
- Mobile first: 390px with no horizontal overflow. Keyboard-accessible. Respects `prefers-reduced-motion`. WCAG AA contrast.
- External scripts only if pinned and from cdnjs/jsdelivr (e.g. GSAP, Lenis). Google Fonts are fine.
- Use the `frontend-design` / `impeccable` / `anti-slop-web` skills for the direction and craft pass. Make it genuinely distinct from today's black-and-gold site and from the other two concepts (your direction is given in your prompt).

## Verify
- `python -m pytest scripts/tests/test_concepts.py -q -k <id>`. Images that don't exist yet (vet screens, the 3 new website shots) may break the link test; list them and keep going.
- Serve the repo root (`python -m http.server <unique port>` in the background; stop it when done). Screenshot home, crm, websites, industries and two industry pages at 1440 and 390 into `C:\Users\taylo\AppData\Local\Temp\claude\e8a30302c63b0c61\503746ae-8215-4629-8d24-dc2bfa57ce43\scratchpad\concepts\<id>\`. Look at them, fix what looks off, and check there are no console errors.
- No em dashes; humanizer only on any glue copy you write yourself (content.json is already humanized).

Report briefly:
- the direction (palette, fonts, layout ideas, and which competitor sites inspired what)
- the page count
- test results
- screenshot folder
- anything unfinished
