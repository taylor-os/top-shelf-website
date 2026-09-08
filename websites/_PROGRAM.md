# Top Shelf — Sample Websites Program

8 fictional companies, one per Top Shelf industry, each a full **5-page** premium site.
These are the flagship sample sites prospects see. Built into this repo under
`websites/<slug>/`, surfaced via a new **"Websites"** nav gallery (`websites.html`)
and featured on each matching `industry-*.html` page.

## Roster & status

| # | Industry | Company | Slug | Palette / world | Status |
|---|----------|---------|------|-----------------|--------|
| 1 | Home Services | Everline Home Services | `everline-home-services` | Midnight navy + amber · premium-industrial | ✅ **LIVE** · Judge PASS |
| 2 | Restaurants & Bars | Ember & Oak | `ember-and-oak` | Charcoal + ember gold · cinematic | ✅ **LIVE** · Judge PASS |
| 3 | Medical & Dental | Brightwater Dental | `brightwater-dental` | Aqua/teal + white · calm clinical | ✅ **LIVE** · Judge PASS |
| 4 | Law Firms | Halcourt & Vale | `halcourt-vale` | Ink/forest + brass · authoritative | ✅ **LIVE** · Judge PASS |
| 5 | Retail & Local | Field & Fawn | `field-and-fawn` | Cream + terracotta/sage · boutique | ✅ **LIVE** · Judge PASS (after 1 REVISE: sage-band WCAG) |
| 6 | Auto | Apex Auto Werks | `apex-auto-werks` | Near-black + electric red · precision | ✅ **LIVE** · Judge PASS (1st) |
| 7 | Salon, Spa & Fitness | Lumen Wellness | `lumen-wellness` | Sand/blush + plum + gold · serene | ✅ **LIVE** · Judge PASS (after 1 REVISE: image usage + featured-card contrast) |
| 8 | Your Business (Vet) | Wellspring Animal Hospital | `wellspring-animal-hospital` | Forest green + coral · caring | ✅ **LIVE** · Judge PASS (after 1 REVISE: contact-chip AA) |

## Per-site pipeline (each ends at a Judge PASS before ship)
1. **Brief** — identity, background/story, services, page IA, copy points, asset manifest → `<slug>/BRIEF.md`
2. **Assets** — hand-built SVG logo + Higgsfield photography → `<slug>/assets/`
3. **Build** — full 5 pages, premium motion stack (Lenis + GSAP), dynamic hero, real transitions, per-industry theme
4. **Verify** — every page in-browser, desktop + mobile, console clean
5. **Judge** — independent review vs. brief/intent (Apple/enterprise, ready-to-ship)
6. **Humanize** — visible copy only (public-facing)
7. **Wire** — industry-page showcase + `websites.html` gallery card
8. **Ship** — commit + push; file to Drive `Projects/Top Shelf/`

## Conventions (all sites)
- Phone: **123-456-7890** · Email: **contact@<company>.com**
- Fictional companies + fictional locales (coined neighborhoods) — never impersonate a real business
- Self-contained static: relative paths, own `styles.css` + `app.js`, own `assets/`
- 5 pages, shared header/footer, accessible (WCAG AA basics), responsive, `prefers-reduced-motion` respected
- No visible building signage/brand text in generated photos

## Deploy note
Push to `main` **auto-deploys to production** (Hostinger GitHub integration — verified: all pages +
assets return 200 at topshelfsolutions.io/websites/<slug>/). Sites live under `websites/` (not
`samples/`) to avoid the 60-day `expire-samples.yml` sweep, which only touches `demo/`.
Live sites are NOT linked from nav/industry pages yet — integration pass is deferred.

## Verify workflow note (durable)
In-app Browser pane will NOT composite content below the fold after a programmatic scroll (blank
frames even though DOM is correct). Verify with **Playwright** instead: navigate → force-reveal
`[data-reveal]` via evaluate → `browser_take_screenshot fullPage`. Lenis cdnjs path 404s — use
`https://cdn.jsdelivr.net/npm/lenis@1/dist/lenis.min.js`. Seed count-up stat values in the HTML
(not `0`) so they're correct with JS off / in static captures.
