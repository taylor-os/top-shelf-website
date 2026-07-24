# Top Shelf Website — session handoff (live state)
> Read FIRST by whoever continues (Taylor OS / Claude Desktop). GitHub holds the code; this holds the thinking. (`.md` files are 404-blocked on the live site.)

**Last updated:** 2026-07-24 · **By:** Claude Code (Windows desktop)

## Goal
Add an **AI assistant ("Top Shelf Concierge")** to the static marketing site **topshelfsolutions.io** — a bottom-right circular chat button + panel that answers business-owner/customer questions and captures their info into the CRM so Taylor can follow up. (NOT the Top Shelf CRM app — that's a separate repo, `taylor-os/top-shelf`.)

## Status — ✅ SHIPPED & LIVE (2026-07-24)
Deployed **assistant-only** to production. Built subagent-driven (6 TDD/reviewed tasks); both final whole-branch reviews passed READY.

- **Website** (this repo) — `main` commit `d3b9c7a`, LIVE on topshelfsolutions.io:
  - `assets/services-vault.json` — 83-service knowledge vault (regen via `assets/build-vault.py` from the Drive `Portfolio/service-catalog-data.json`).
  - Widget appended to `assets/site.js` (FAB + panel injected site-wide, retrieval engine over the vault + site intents, guided lead capture) + `assets/site.css` (`.tsc-*` in the espresso+gold tokens). No per-page HTML edits.
  - **Scripted, no LLM / no API cost.** Never quotes prices → offers a free audit. Verified live: widget renders, vault serves 200, `/docs` 404-blocked.
- **App** (`C:\Users\taylo\top-shelf`) — `main` commit `813290e`, deployed to Railway:
  - `POST /api/website-lead` (`PublicWebsiteLeadController`, `routes/api.php`) — public, throttled `10,1`, CORS-limited to topshelfsolutions.io(+www); find-or-creates a **deduped** `Contact` in `config('website_lead.location_id')` (default first location) tagged `website-chat` + queues `WebsiteLeadMail` to `contact@topshelfsolutions.io`. Live probe returns 422 on invalid input (validates; no side effects). `WebsiteLeadTest` 3/3, full suite 92/92.

## Remaining owner to-dos to be FULLY live
1. **Set `WEBSITE_LEAD_LOCATION_ID`** env on the top-shelf Railway app to Taylor's own agency location (else it defaults to the first location — leads still land, just verify it's the right one).
2. **Replace `FORMSPREE_ID`** in `assets/site.js` (const `FORMSPREE`) and `contact.html` with the real Formspree form id — this is the fallback email path (only used if the CRM endpoint is ever unreachable). The primary CRM path works without it.
3. Optional: fire one real test lead from the live widget to see it land in the CRM + email you (creates one real Contact — clean up after).

## Notes
- **Deploy was assistant-only:** Taylor's own industry-pages work (already on `main` as `c71db15`/`06963fa`) and his uncommitted WIP (`solution-*.html`, `assets/img/service/*.jpg`) were left untouched. The assistant was added by appending its self-contained widget blocks onto current `main`.
- **Autosync hazard:** the autosync task interfered repeatedly this build (flipped branches, tangled commits). Consider pausing it during multi-repo builds. Work is safe on GitHub regardless.
- Scripted-retrieval relevance is keyword-based (owner chose no-LLM); tune matches via the vault `keywords` if desired (e.g. "more customers" currently keys to "Customer Portal").
- Spec + plan: `docs/superpowers/{specs,plans}/2026-07-23-*` (this repo; `/docs` is 404-blocked live). Reference widget pattern: Reids `assets/js/app.js` ("Dawn").
- App public URL: `https://top-shelf-production.up.railway.app` (endpoint `/api/website-lead`).
