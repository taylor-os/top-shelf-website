# Design Spec — Top Shelf website assistant ("scripted concierge")

**Date:** 2026-07-23
**Primary repo:** `C:\Users\taylo\top-shelf-website` (static HTML/CSS/JS, deploys to **topshelfsolutions.io** via Hostinger GitHub App — push `main` → `public_html`, no build step)
**Secondary repo:** `C:\Users\taylo\top-shelf` (Laravel CRM app on Railway — one small lead-intake endpoint)
**Author:** Taylor OS Manager → Engineering

> NOTE: this is the marketing **website**, NOT the Top Shelf CRM app. Two different things.

## 1. Goal

Add a bottom-right **circular chat button + panel** to every page of topshelfsolutions.io that lets business owners / prospective customers ask questions and get helpful answers, then **captures their info** so Top Shelf can reach out. It is a **scripted retrieval assistant** (no LLM, no API key, no per-chat cost) whose knowledge **vault is the full 83-service portfolio catalog**. Its real job: be helpful, then convert the visitor into a captured lead for a free business audit.

## 2. Decisions (locked with owner)

1. **Type:** scripted bot, **no LLM / no API cost** (like the Reids "Dawn" bot), backed by a real services vault.
2. **Knowledge vault:** the full **83-service portfolio catalog** (source: `G:\My Drive\Taylor OS\Projects\Top Shelf\Portfolio\service-catalog-data.json`, 83 services across 12 sections) — the portfolio is still being built, so the vault ships as an easily-updatable data file.
3. **Placement:** the widget appears **site-wide** (all pages), injected via the shared `assets/site.js`.
4. **Lead destination:** **both** — create a Contact in the Top Shelf **CRM** *and* email the owner. Delivered via one small **public lead-intake endpoint on the app**; the existing **Formspree** is the no-lost-lead fallback.
5. **No prices:** pricing questions → "every business is different; we do a quick free audit and build a custom plan" → capture.

## 3. Confirmed environment facts

- Website is pure static: shared `assets/site.css` (espresso + gold "luxury" system) + `assets/site.js` (gold-dust bg, motion, count-up, mobile menu). Pages: `index`, `industry-*` (auto, bars, custom, dental, home-services, retail), `solution-*` (ai-phone, crm, marketing, pos, websites-seo), `pricing`, `why-us`, `contact`, `thank-you`. CDN deps (Google Fonts, GSAP); **no build step**.
- Contact form (`contact.html`) posts to `https://formspree.io/f/FORMSPREE_ID` (placeholder to be replaced). Owner email: `contact@topshelfsolutions.io`.
- Reference pattern: the Reids `assets/js/app.js` has a working scripted FAB+panel assistant ("Dawn") — keyword→answer KB + guided lead capture, ~fully client-side. Reuse its structure/UX; replace its KB with the Top Shelf services vault; add real lead delivery.
- App (`top-shelf`) has an existing public funnel-submit (`POST p/{slug}` → `PublicFunnelController@submit`) that creates a lead Contact in a location — a possible reuse path for CRM delivery (see §4.C alt).

## 4. Architecture

Two small parts.

### 4.A — Services vault (data)
- Build `assets/services-vault.json` in the website repo, compiled from the Drive catalog. Per service: `name`, `section`, `keywords` (derived from name + section + `great_for` + salient terms), and a `blurb` (a plain-English answer assembled from `what_it_is` + `how_ts_solves` + `what_it_means`), plus `great_for`. Keep the 12 sections so the bot can also answer "what do you offer for X?" at the category level.
- Committed as a data file so the portfolio can grow without code changes. (A tiny build note / script documents how it was condensed from `service-catalog-data.json`.)

### 4.B — The widget (website)
- **FAB + panel** injected site-wide by `assets/site.js` on `DOMContentLoaded` (single-file maintenance across all pages), styled in `assets/site.css` to match the espresso+gold system (gold FAB, espresso panel, luxury type). Bottom-right, mobile-friendly, respects reduced-motion.
- **Scripted retrieval engine** (`assets/chat.js`, loaded site-wide): matches the visitor's message against the vault (keyword/section scoring) + a small set of site-level intents (how-it-works, why-us, pricing→audit, industries, contact/next-step, greeting). Returns the best `blurb` (or a category list) and **quick-reply chips** to guide the conversation toward "get a free audit."
- **Guided lead capture:** a short scripted flow collecting **name → business/industry → best contact (email or phone) → what they need**. Validated client-side.
- **Off-script fallback:** no confident match → "Great question — let me get your info and a Top Shelf specialist will follow up with specifics," then enter capture.
- **Submit:** `POST` the captured lead (name, business, email, phone, need, page URL, transcript summary) to the app lead-intake endpoint (§4.C). On success → "You're all set — we'll reach out shortly" + link to `thank-you.html`. On failure → fall back to a Formspree POST so the lead still emails through.

### 4.C — Lead intake (app, one small addition)
- `POST /api/website-lead` — a public, **throttled** (`throttle:10,1`), **CORS-limited to topshelfsolutions.io** endpoint (`PublicWebsiteLeadController`). Validates the payload, then:
  1. **CRM:** create a `Contact` in the configured location (`WEBSITE_LEAD_LOCATION_ID`, default = agency's own location), `withoutGlobalScopes()` + explicit `location_id`, tagged `website-chat`, with name/email/phone/company + the need in a note.
  2. **Email:** send a notification to `contact@topshelfsolutions.io` (Mailable) with the lead details + page/transcript.
  - Returns `{ ok: true }`. Errors return a safe JSON error (the widget then uses the Formspree fallback).
- **Alt (if owner prefers):** reuse the existing funnel-submit instead of a new endpoint — but a dedicated endpoint is clearer and decoupled; default to the new endpoint.

## 5. Data flow
FAB click → chat → vault answer(s) + chips → capture (name/business/contact/need) → `POST /api/website-lead` → Contact created in CRM + email to owner → "we'll reach out" (+ thank-you link). Fallback: endpoint down → Formspree email.

## 6. Guardrails (scripted behavior)
- Never quote prices/numbers → audit + capture.
- Only represent real Top Shelf services (the vault); off-topic → redirect to how Top Shelf can help their business, or capture for a human.
- Always drive toward: helpful answer → free audit → leave your info.
- Tone: warm, confident, plain-spoken; matches the catalog's voice and the site's premium feel.

## 7. Testing / verification
- **Widget:** verified in the browser preview against the local site — FAB opens/closes, greeting shows, keyword questions return the right service blurbs, category questions list services, pricing → audit line, lead-capture flow submits, mobile layout clean, reduced-motion respected.
- **App endpoint:** a feature test — valid payload creates a Contact in the configured location (tagged `website-chat`) + sends the notification email (`Mail::fake`); throttle enforced; invalid payload rejected; CORS header present for the site origin.

## 8. Configuration
- Website: `assets/services-vault.json` (the vault); the lead-intake URL + Formspree fallback id as constants in `chat.js`.
- App: `WEBSITE_LEAD_LOCATION_ID`, `WEBSITE_LEAD_NOTIFY_EMAIL` (default `contact@topshelfsolutions.io`) in a small `config/website_lead.php`; CORS allow-list entry for `https://topshelfsolutions.io`.
- Keep planning docs out of the public site: add a `/docs` deny to the website `.htaccess`.

## 9. Non-goals (YAGNI)
- No LLM / AI model / API key anywhere.
- No streaming, no backend for the chat brain (retrieval is client-side).
- No pricing logic.
- No voice.
- No changes to the app's existing AI Employee / funnels beyond the one intake endpoint.

## 10. Open items (resolve during planning/impl — not blockers)
- Confirm the app's exact `Contact` create + `tags()` attach API and the agency/own-location id for `WEBSITE_LEAD_LOCATION_ID` (plan pins it).
- Confirm how the app registers CORS (config/cors.php) and the notification channel (Mailable vs Notification).
- Decide the vault condensation depth (how much `blurb` per service) to keep `services-vault.json` lean but useful.
- Get a real Formspree form id (or Hostinger form handler) for the fallback + the existing contact form.

## 11. Rollout
Website change deploys on push to `main` (Hostinger auto-deploy, ~15s). App endpoint deploys on the app's normal Railway pipeline. Build on a branch per repo; verify before going live. Session/handoff binds to the **website** repo (with a note pointing at the app-side endpoint commit).
