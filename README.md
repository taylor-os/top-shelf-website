# Top Shelf Business Solutions — marketing website

Static marketing site for **topshelfsolutions.io**. Deployed to Hostinger via the
Hostinger GitHub App (same pattern as the GDR and TAP sites): pushes to `main`
auto-deploy the repo root to `public_html`.

> This is the **marketing site** only. The Top Shelf CRM app is a separate repo
> (`taylor-os/top-shelf`, a Laravel app on Railway) — do not confuse the two.

## Structure
- `index.html` + section pages (industries, solutions, pricing, why-us, contact, thank-you)
- `assets/` — `site.css` (shared design system), `site.js` (gold-dust background + motion +
  count-up + mobile menu), `logo-full.png`, `logo-mark.png`, `icon-kit.html` (SVG icon reference)
- All pages share `assets/site.css` + `assets/site.js`, so site-wide changes are one-file edits.

## Deploy (Hostinger)
1. hPanel → the `topshelfsolutions.io` website → **Advanced → GIT** (Auto-deployment).
2. Repository: `https://github.com/taylor-os/top-shelf-website` · Branch: `main`.
3. Deploy — Hostinger publishes the repo root to `public_html`. Enable auto-deploy so
   future `git push`es go live automatically (~15s), no drag-drop.

## To finish before real launch
- **Contact form:** `contact.html` posts to `https://formspree.io/f/FORMSPREE_ID` — replace
  `FORMSPREE_ID` with a real Formspree form id (or swap to Hostinger's form handler) or the
  audit form won't deliver.
- Confirm business details (phone, address, hours) across the pages before driving traffic.

Design: deep espresso + gold "luxury" system, real Top Shelf logo, GSAP motion. Third-party
runtime deps are CDN-loaded (Google Fonts, GSAP) — no build step, pure static.
