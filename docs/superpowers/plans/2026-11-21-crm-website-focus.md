# CRM + Website Focus Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** topshelfsolutions.io sells only the Signature plan ($99 / $199 / call, $50 per phone line) and the $499 website, with every removed page redirected, the "Try the CRM" request form as the main button, and CRM screens for every industry.

**Architecture:** A shared catalog module (`scripts/focus_catalog.py`) holds every decision (removed slugs, redirect targets, new nav, old-price patterns). Small one-shot scripts apply it to the built HTML and to the generator spec files, and a pytest guard (`scripts/tests/test_focus.py`) fails while any old price, removed link, old nav or unredirected page remains. Hand-written pages are edited by hand. Renders are HTML mockups rendered to PNG with Playwright, the same way as the existing realtor set.

**Tech Stack:** static HTML/CSS/JS, Python 3.13 + pytest (existing `scripts/tests/`), Apache `.htaccess` on Hostinger, Playwright (already used for renders), Hostinger GitHub App deploy on push to `main`.

**Spec:** `docs/superpowers/specs/2026-11-21-crm-website-focus-design.md`

Work happens in worktree `C:\Users\taylo\top-shelf-website-focus` on branch `feat/crm-website-focus`. Pushing the branch is safe; **merging to `main` deploys the live site** and happens only at the two deploy tasks, after Taylor's go.

## Global Constraints

- Signature plan: $99/mo for 1-10 users, $199/mo for 11-25 users, 26+ "Call for pricing". Called a **plan**, never a "blend".
- Phone line: $50/mo per line; copy says it covers normal use and usage above that is billed. No caps or overage rates shown.
- Website: $499 one time, "professional website", no page count anywhere. Includes: mobile-friendly custom design, built so Google can read it, contact/booking form that feeds the CRM, a logo if they need one. Not included in Signature.
- Signature features (all of them, owner 2026-11-20/21): CRM, AI receptionist that answers and books jobs, missed-call text-back, online booking, dispatch board, customer hub, invoice by text, review requests, review replies, on-my-way texts, estimates, card payments, AI chatbot added to their current website.
- No setup fee, month to month. No refund/guarantee wording, no ranges, no lump-sum totals, hosting never in copy.
- Main button everywhere: "Try the CRM" → `contact.html` (a request form; never a login). Secondary: "Call or text (469) 833-3033".
- New copy: no em dashes; humanizer pass on every new customer-facing sentence (CLAUDE.md §0.5).
- Untouched: `demo/**`, `websites/**`, `preview/**`.
- Never on a public page: "Sarah Laos", "Ready Real Estate". Every non-shipped CRM render carries a visible "Sample screens" label.

## Review Focus

1. A kept page's "the fix" bridge or CTA links to a removed page. Expect: none; the link test in Task 1 checks every local `href` resolves to a kept file.
2. Visible price is new but the JSON-LD `Offer`/`Service` block still carries an old price. Expect: JSON-LD prices only in {99, 199, 50, 499}; Task 1's `test_jsonld_prices`.
3. The phone-width drawer (built by `assets/site.js` from `.nav-links`) still shows removed Solutions. Expect: drawer matches the new nav; Task 3 checks `.nav-links` markup and Task 7 screenshots the drawer at 390 px.
4. A removed URL is requested with a query string (from an old email: `?utm_source=...`). Expect: 301 to the target, query kept; Task 7's live redirect check includes one query-string URL.
5. The Try the CRM form is sent with a phone but no email. Expect: accepted (backend needs email OR phone); Task 6's `test_form_fields` pins `phone` required, `email` optional.

---

### Task 1: Catalog and guard tests

**Files:**
- Create: `scripts/focus_catalog.py`
- Create: `scripts/tests/test_focus.py`

**Interfaces:**
- Produces (`scripts/focus_catalog.py`):
  - `ROOT: str` (repo root)
  - `EXCLUDE_DIRS = ("demo", "websites", "preview", "node_modules", ".git")`
  - `REMOVED: dict[str, str]` — removed path (e.g. `"marketing-for-plumbers.html"`) → redirect target path (e.g. `"for-plumbers.html"`). Built from the spec's page table: every `marketing-for-*.html` → `for-<slug>.html` (falling back to `industry-custom.html` if missing); `get-found-package.html`, `get-found-plus.html`, `custom-5-page-website.html`, `one-page-website.html`, `take-back-your-website.html` → `pricing.html#website`; `one-time-services.html`, `get-found-listing-reviews.html`, `google-business-profile-fix.html`, `map-pack-push.html`, `review-reply-catch-up.html`, `sample-report.html`, `sample-seo-report.pdf` → `pricing.html`; `solution-marketing.html`, `solution-pos.html`, `solution-memberships.html` → `solution-crm.html`; `answers-marketing.html` → `answers-crm.html`.
  - `OLD_PRICE_RE: re.Pattern` matching `\$(299|899|2,500|599|795|1,995|345|1,250|1,500|495|150|325|95|1,695|6,215|8,475)\b` (not `$3,390`, `$452`, `$678`, which survive in the comparison table).
  - `OLD_NAME_RE: re.Pattern` matching `\b(Essentials|Platinum|Get Found|One-Time Services|Free Audit|[Bb]lend)\b`.
  - `NEW_SOLUTIONS: list[tuple[str, str]]` — `[("solution-crm.html","CRM & Follow-Up"),("solution-ai-phone.html","AI Phone & Chat"),("solution-reviews.html","Reviews"),("solution-booking.html","Online Booking"),("solution-payments.html","Payments"),("solution-automation.html","AI & Automation"),("solution-websites-seo.html","Websites")]`
  - `CTA_LABEL = "Try the CRM"`, `CTA_HREF = "contact.html"`
  - `ALLOWED_PRICES = {"$99", "$199", "$50", "$499"}`
  - `ALLOWED_CONTEXTS: list[str]` — exact sentences where an old-price number is legitimately not a Top Shelf price (e.g. a sourced industry figure like a "$150 service call"); `test_no_old_prices` skips a match only when its sentence is in this list. Starts empty; Task 4 adds entries, each one a deliberate call.
  - `def site_pages() -> list[str]` (every `*.html` at ROOT, minus EXCLUDE_DIRS), `def source_files() -> list[str]` (every `scripts/*.py` except `focus_catalog.py` and `tests/`).

- [ ] **Step 1: Write the failing tests** in `scripts/tests/test_focus.py`, each one listing every offender in its assert message:
  - `test_no_old_prices`: `OLD_PRICE_RE` finds nothing in visible text of `site_pages()` (strip `<script>`/`<style>`, keep JSON-LD out of this test) nor in `source_files()`.
  - `test_no_old_names`: `OLD_NAME_RE` finds nothing in the same sets.
  - `test_removed_files_gone`: no path in `REMOVED` exists on disk.
  - `test_every_removed_url_redirected`: `.htaccess` has a `Redirect 301` or `RedirectMatch 301` covering each `REMOVED` key, and its target exists on disk (strip `#fragment`).
  - `test_internal_links_resolve`: every local `href`/`src` in `site_pages()` (ignore `http`, `mailto:`, `tel:`, `#`) resolves to an existing file.
  - `test_nav_is_new`: every page with `id="nav"` has exactly the `NEW_SOLUTIONS` hrefs in its Solutions dropdown, a `.nav-cta` button whose text is `CTA_LABEL` and href `CTA_HREF`, and no `Get Free Audit`.
  - `test_jsonld_prices`: every `"price"` value inside `application/ld+json` blocks is in `{"99","199","50","499"}`.
  - `test_sitemap_has_no_removed`: no `REMOVED` key in `sitemap.xml`.

- [ ] **Step 2: Run to confirm they fail**
  Run: `cd C:/Users/taylo/top-shelf-website-focus && python -m pytest scripts/tests/test_focus.py -q`
  Expected: every test FAILS with offender lists (hundreds for prices and nav).

- [ ] **Step 3: Implement `scripts/focus_catalog.py`** with the values above. Build `REMOVED` by globbing the families at import, so the tests and the removal script share one list.

- [ ] **Step 4: Re-run** — still failing on content, but no import errors.

- [ ] **Step 5: Commit** `git add scripts/focus_catalog.py scripts/tests/test_focus.py && git commit -m "Focus: catalog and guard tests (failing)"`

### Task 2: Remove pages, retire their generators, add redirects

**Files:**
- Create: `scripts/focus_remove.py`
- Modify: `.htaccess` (append a block between `# BEGIN crm-website-focus` and `# END crm-website-focus`)
- Delete: every file in `REMOVED`; `scripts/generate_one_time.py`, `scripts/wire_one_time.py`; the spec entries that emit `marketing-for-*`, `solution-marketing`, `solution-pos`, `solution-memberships`, `answers-marketing` pages (find the emitting generator with `grep -l "marketing-for-" scripts/*.py`).

**Interfaces:**
- Consumes: `REMOVED`, `ROOT` from Task 1.
- Produces: `def redirect_rules(removed: dict[str,str]) -> list[str]` — one `RedirectMatch 301 ^/marketing-for-(.+)\.html$ /for-$1.html` family rule where every member's target exists, explicit `Redirect 301 /<path> /<target>` lines otherwise. Idempotent: re-running replaces the block.

- [ ] **Step 1:** Run `python -m pytest scripts/tests/test_focus.py -q -k "removed or redirected"` and confirm both fail.
- [ ] **Step 2:** Implement `focus_remove.py` (deletes files with `git rm`, writes the `.htaccess` block, removes the one-time wiring blocks between `<!-- one-time-links -->` markers and `PRICING_OPEN`/`PRICING_CLOSE` markers from every page).
- [ ] **Step 3:** Delete the retired generators and spec entries. Add a test `test_no_generator_emits_removed` asserting no `scripts/*.py` (except `focus_catalog.py`) contains a `REMOVED` key as a string literal.
- [ ] **Step 4:** Run `python -m pytest scripts/tests/test_focus.py -q -k "removed or redirected or generator"`. Expected: PASS.
- [ ] **Step 5: Commit** `git commit -am "Focus: remove marketing, one-time and extra service pages; 301 every one"` (include the deletions).

### Task 3: New nav, footer and main button on every page

**Files:**
- Create: `scripts/focus_chrome.py`
- Modify: every page in `site_pages()` (generated output) and the base page each generator clones its shell from (`solution-crm.html`, plus any other base page named in `generate_*.py`).

**Interfaces:**
- Consumes: `NEW_SOLUTIONS`, `CTA_LABEL`, `CTA_HREF`, `site_pages()`.
- Produces: `def rewrite_chrome(html: str) -> str` — replaces the Solutions `.nav-dropdown` contents, the `.nav-cta` gold button (`Get Free Audit` → `Try the CRM`), the footer "Solutions" column links (same list), and in the footer "Company" column drops `One-Time Services` and turns `Free Audit` into `Try the CRM`. The `CRM Demo` nav link to `https://crm.topshelfsolutions.io/8` stays (a walkthrough, not a login). Also replaces CTA button labels sitewide: `Get Your Free Audit →`, `Get My Free Audit →`, `Get your free audit →`, `Get Free Audit →`, `Get Free Audit` → `Try the CRM →` / `Try the CRM`.

- [ ] **Step 1:** Run `-k nav` and confirm it fails.
- [ ] **Step 2:** Implement `rewrite_chrome` (regex on the known markup shown in `solution-crm.html` lines 46-88 and 532-591; leave anything else on the line untouched).
- [ ] **Step 3:** Apply to every page; run `-k nav`. Expected: PASS.
- [ ] **Step 4:** Open `index.html` in the browser at 390 px, open the Menu drawer, confirm it lists the new Solutions and the Try the CRM button. Screenshot to the scratchpad.
- [ ] **Step 5: Commit** `git commit -am "Focus: new nav, footer and Try the CRM button"`

### Task 4: Reprice the generated copy and its sources

**Files:**
- Create: `scripts/focus_reprice.py`
- Modify: generated pages and `scripts/*specs*.py`, `scripts/generate_*.py`, `scripts/wire_*.py`, `scripts/corpus_specs.py` wherever old copy lives.

**Interfaces:**
- Consumes: `site_pages()`, `source_files()`, `OLD_PRICE_RE`, `OLD_NAME_RE`.
- Produces: `REPLACEMENTS: list[tuple[str, str]]` (ordered, exact-sentence) and `def apply(text: str) -> str`. Applied to HTML text and to Python source string literals alike, so a regenerated page carries the new copy.

The top templates (from a sentence census of the live pages; counts in brackets) and their replacements. Run the humanizer over the right-hand column once before applying:

| Old sentence | New sentence |
|---|---|
| The custom 5-page website is $1,500 one time and the one-page website is $495, each built new by us with a logo if you need one. [60] | A professional website is $499 one time, built new by us, with a logo if you need one. |
| Get Found Plus is the 5-page website, the listing corrected, your reviews answered and a review card for $1,995. [60] | (delete) |
| If a past vendor holds your site or domain, take back what's yours moves them into your name for $495. [60] | (delete) |
| The Essentials plan is $299 a month and covers website upkeep, local SEO, online booking, and reviews. [57] / ...is $299 a month for website upkeep, local SEO, online booking, and reviews. [57] | (delete) |
| The Signature plan is $899 a month and adds the AI receptionist and CRM. [52] | The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM. |
| A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. [52] (and the "five-page", "one time" variants) | A professional website is $499 one time, and you do not need a plan to buy one. |
| Top Shelf includes it in the Signature plan at $899 a month. [43] | Top Shelf includes it in the Signature plan, $99 a month for up to 10 users. |
| A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. [42] (and "custom five page site") | The Signature plan is $99 a month for up to 10 users, and a professional website is $499 one time. |
| It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. [42] | It comes in the Signature plan at $99 a month for up to 10 users, with no setup fee, alongside the phone and follow-up that feed it. |
| It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. [37] (and "meter.") | It comes in the Signature plan at $99 a month for up to 10 users. Each phone line is $50 a month and covers normal use. |
| If you buy the one-time $1,500 site, it is yours to keep. [29] | If you buy the $499 website, it is yours to keep. |
| A monthly plan starting at $299 is optional. [20] | The Signature plan, from $99 a month, is optional. |
| A (custom) (five page) site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. [22+17] | A professional website on its own is $499 one time, yours to keep, with no plan and no commitment. |
| Top Shelf builds (one / a custom (five page) site) for $1,500 one-time(, and you own it / and no monthly plan is needed to buy one). [~45] | Top Shelf builds a professional website for $499 one time, and you own it. |
| A monthly plan is optional and starts at $299 a month, where the ongoing SEO that actually gets it ranking is handled for you. [11] | The Signature plan is optional and starts at $99 a month. |
| The Signature plan at $899 a month adds the AI receptionist and the CRM that ... [~25, several endings] | The Signature plan at $99 a month for up to 10 users includes the AI receptionist and the CRM that ... (keep the ending) |
| See pricing → Signature plan · $899/mo / Get your free audit → Signature plan · $899/mo | Signature plan · from $99/mo |
| The review reply catch-up ... $150 ... / The Google listing fix ... $345. / With no website, Get Found is $795. / With a poor website..., Get Found Plus is $1,995... | (delete) |
| Comparison table row "Rank in local search / SEO agency: $1,695/mo / Included" | (delete the row) |
| Comparison total "$6,215+/mo ... $899/mo" | "$4,520+/mo, and a stack of logins to juggle" vs "$99/mo. One bill, one team" ($3,390 + $452 + $678 = $4,520) |

- [ ] **Step 1:** Run `-k "old_prices or old_names"`; save the offender count.
- [ ] **Step 2:** Implement `focus_reprice.py` with the table (regexes only where a row lists variants; sentence deletes also remove the following space).
- [ ] **Step 3:** Apply to pages and sources; re-run the two tests. Expected: far fewer offenders.
- [ ] **Step 4:** Fix the remaining offenders by hand (or add rows), page family by family, until both tests PASS. Pages that still describe SEO as a service: say "built so Google can read it" instead, never ongoing SEO. Missed-call / after-hours articles keep pointing at the AI receptionist inside Signature.
- [ ] **Step 5:** Run the full guard file; everything except `jsonld` and `sitemap` should PASS.
- [ ] **Step 6: Commit** `git commit -am "Focus: reprice generated copy and sources to Signature and the \$499 website"`

### Task 5: Rewrite the hand-written pages

**Files:**
- Modify: `pricing.html`, `index.html`, `solution-crm.html`, `solution-websites-seo.html`, `solution-ai-phone.html`, `solution-reviews.html`, `solution-booking.html`, `solution-payments.html`, `solution-automation.html`, `why-us.html`, `alternatives.html`, `industry-*.html`, `answers*.html`, `llms.txt`
- Test: add `test_pricing_page` to `scripts/tests/test_focus.py`

**Interfaces:**
- Consumes: Global Constraints copy.

- [ ] **Step 1: Write `test_pricing_page`**: `pricing.html` visible text contains `$99`, `$199`, `Call for pricing`, `$50`, `per line`, `$499`, `Try the CRM`; has an element with `id="website"` (redirect target); contains every Signature feature name from Global Constraints; contains none of `Essentials`, `Platinum`, `Get Found`, `page website`. Run it: FAIL.
- [ ] **Step 2:** Rebuild `pricing.html` in the existing page shell: one Signature card with the three user tiers, the phone line note ("$50 a month per line, covers normal use; usage above that is billed"), the full feature list, then the $499 website card (`id="website"`) with its four inclusions, then the FAQ rewritten (setup fee: none; contract: none; what you own; extra costs: the phone line, as stated; which plan: Signature by user count). JSON-LD `Offer`s: 99, 199, 50 (per line), 499. Remove the old plan comparison table and the one-time section.
- [ ] **Step 3:** Rewrite the other hand-written pages to the same facts (index hero/drawer, solution pages as Signature features, industry pages as CRM + website, `llms.txt` pricing lines, `answers*.html`). Remove any remaining JSON-LD offers with old prices.
- [ ] **Step 4:** Humanizer pass on all new copy in these pages, voice-matched to the existing site copy; no em dashes.
- [ ] **Step 5:** Run the full guard file; everything except `sitemap` PASSES.
- [ ] **Step 6: Commit** `git commit -am "Focus: rewrite pricing, home, solution and industry pages"`

### Task 6: Try the CRM request form

**Files:**
- Modify: `contact.html`, `thank-you.html` (wording only)
- Test: add `test_form_fields` to `scripts/tests/test_focus.py`

**Interfaces:**
- Consumes: backend `PublicWebsiteLeadController` fields (top-shelf-crm): `name` required; `business, email, phone, city, state, gbp, need, page, industry, sms_consent, source` optional; needs email OR phone. No backend change.

- [ ] **Step 1: Write `test_form_fields`**: the form in `contact.html` posts to `https://top-shelf-production.up.railway.app/api/website-lead`; its input names are a subset of the backend list; `name` and `phone` have `required`, `email` does not; there is no `gbp` input; there is a users select whose options are `1-10`, `11-25`, `26+` and whose value is sent inside `need` (e.g. `"Users: 11-25"`); hidden `source` = `try-crm`. Run: FAIL.
- [ ] **Step 2:** Rewrite `contact.html`: heading "Try the CRM", one line saying we'll call to set up a demo (no login on the page), fields name, business, phone, email, industry, users, SMS consent. Keep the existing fetch submit and thank-you redirect; fold the users choice into `need` in the submit handler. Remove the audit framing section.
- [ ] **Step 3:** Run `-k form`: PASS.
- [ ] **Step 4: Commit** `git commit -am "Focus: contact page becomes the Try the CRM request form"`

### Task 7: Sitemap, facts, verification, Judge, deploy push 1

**Files:**
- Modify: `sitemap.xml` (via `python scripts/build_sitemap.py`), `C:\Users\taylo\Agentic-OS\vault\platter\facts\top-shelf-business-solutions.json`

- [ ] **Step 1:** Run `python scripts/build_sitemap.py`; run the full guard file. Expected: all PASS.
- [ ] **Step 2:** Add to the facts file: `$499` website and its inclusions, `$50` per phone line, Signature `$199` and "Call for pricing" for 26+, the Try the CRM form. Run the fact gate from `C:\Users\taylo\Ledger Pro\docs\taylor-os`: `python -m platter.factcheck <worktree>/pricing.html <facts.json>` and the same for `index.html`, `solution-crm.html`. Expected: exit 0.
- [ ] **Step 3:** Serve the worktree locally (`python -m http.server 8190` from the worktree, via a `.claude/launch.json` entry) and screenshot at 1280 and 390: home, pricing, solution-crm, industry-home-services, crm-for-plumbers, plumber-website-cost, contact, and the open phone drawer.
- [ ] **Step 4:** Run `judge-agent` against the spec with the screenshots and test output. REVISE → fix → re-judge (cap 3).
- [ ] **Step 5:** Show Taylor the screenshots and the removed-page count; get his go to deploy.
- [ ] **Step 6:** In the worktree: `git fetch origin && git merge origin/main` (pull in anything that landed on main since 1a615bb, e.g. new demos), re-run the guard file, then `git push origin feat/crm-website-focus:main` (this deploys). If main moved again before the push, repeat.
- [ ] **Step 7:** After about a minute, request every `REMOVED` URL on `https://www.topshelfsolutions.io` with `curl -s -o /dev/null -w "%{http_code} %{redirect_url}"`, plus `marketing-for-plumbers.html?utm_source=test`. Expected: `301` to a target that returns `200`, query kept. Spot-check live pricing.html for `$99`.
- [ ] **Step 8:** Submit one Try the CRM form on the live site with name `TEST - Claude, please ignore`, then confirm the lead arrived (ask Taylor to confirm the alert, or check the CRM's house account).
- [ ] **Step 9:** File the changed live pages to Drive `Projects/Top Shelf/Website/` and commit.

### Task 8: Real estate CRM screens (renamed, paired with website pages)

**Files:**
- Create: `renders-src/real-estate/` (copy of Drive `renders/sarah-laos-crm/screens-html/`: `build_crm.py`, `crm.css`, the 9 screen HTML files, `img/`), `scripts/render_screens.py`
- Create: `assets/img/crm/real-estate/<screen>-d.png` (1440 wide) and `<screen>-m.png` (390 wide) for the 9 screens, plus `assets/img/crm/real-estate/site-<page>.png` website halves
- Modify: `industry-real-estate.html`, `solution-crm.html`
- Test: add `test_real_estate_screens`

**Interfaces:**
- Produces: `def render(html_path: str, out_png: str, width: int) -> None` in `scripts/render_screens.py` (Playwright Chromium, device scale 2, full page). Reused by Tasks 9 and 10.

- [ ] **Step 1: Write `test_real_estate_screens`**: the 9 `-d.png` files exist; no file under `renders-src/` or any site page contains `Laos` or `Ready Real Estate`; `industry-real-estate.html` references all 9 screens and shows the text `Sample screens`. Run: FAIL.
- [ ] **Step 2:** Copy the sources in, rename the agent to `Elena Marsh` and the brokerage to a made-up name throughout (`build_crm.py`, screen HTML, alt text), and add a "Sample screens" tag to each screen.
- [ ] **Step 3:** Make a renamed local copy of `demo/sarah-laos-realtor/` in the scratchpad (never in the repo), render its matching pages (listings, a listing detail) to `site-*.png`.
- [ ] **Step 4:** Implement `render_screens.py`; render the 9 screens at both widths.
- [ ] **Step 5:** Add a "Run it from your phone, it shows on your website" section to `industry-real-estate.html` and a short gallery to `solution-crm.html`: each CRM screen beside its website half, lazy-loaded `<img>` with alt text and width/height set.
- [ ] **Step 6:** Run the test: PASS. Run the full guard file: PASS.
- [ ] **Step 7: Commit**

### Task 9: Sample screens for the five industries without a CRM

**Files:**
- Create: `renders-src/sample-crm/build_sample_crm.py`, `renders-src/sample-crm/data/{restaurants,medical-dental,legal,retail,salon-spa}.json`, screen templates reusing `renders-src/real-estate/crm.css`
- Create: `assets/img/crm/<industry>/<screen>-d.png` / `-m.png` for screens `today`, `customers`, `customer`, `pipeline` (or `bookings` for restaurants, medical-dental, salon-spa), `texts`, `mobile-today`
- Modify: `industry-restaurants.html`, `industry-medical-dental.html`, `industry-legal.html`, `industry-retail.html`, `industry-salon-spa-fitness.html` (Salon & Spa section), and the matching `for-*.html` pages that already have a CRM section
- Test: add `test_sample_screens`

**Interfaces:**
- Consumes: `render()` from Task 8.
- Produces: `def build(industry: str) -> list[str]` (writes the screen HTML files, returns their paths).

- [ ] **Step 1: Write `test_sample_screens`**: for each of the five industries, the 6 `-d.png` files exist, its industry page references them and shows `Sample screens`; no data file contains a real business name (keep a small denylist check against names in `vault/platter/facts/*.json`). Run: FAIL.
- [ ] **Step 2:** Write the five data files with plausible sample data (made-up people and businesses, DFW-plausible, industry-correct: reservations and tabs for restaurants, appointments and recalls for medical-dental, matters and consultations for legal, orders and repeat customers for retail, bookings and rebooks for salon-spa).
- [ ] **Step 3:** Implement `build()`; render all screens at both widths.
- [ ] **Step 4:** Place them on the pages with the "Sample screens" label; on `industry-salon-spa-fitness.html` label only the Salon & Spa section.
- [ ] **Step 5:** Run the test and the full guard file: PASS. **Commit.**

### Task 10: Real CRM screens for home services, auto and gyms

**Files:**
- Create: `assets/img/crm/{home-services,auto,fitness}/*` (copied and resized from Drive `renders/crm-desk-ad-2026-11-19/` dashboard + job images, `renders/dealer-program-shots/dealer` + `shop`, `renders/repkin/`)
- Modify: `industry-home-services.html`, `industry-auto.html`, `industry-salon-spa-fitness.html` (fitness section)
- Test: add `test_real_crm_screens`

- [ ] **Step 1: Write the test**: each of the three pages references at least 3 images under its folder and all exist. Run: FAIL.
- [ ] **Step 2:** Copy and resize (WebP, 1600 px max, keep the existing "Sample data" strips on dealer shots). Place a short screen strip on each page. No "Sample screens" label on these (real product), but sample data stays marked as it already is.
- [ ] **Step 3:** Run the test and the full guard file: PASS. **Commit.**

### Task 11: Verification, Judge, deploy push 2

- [ ] **Step 1:** Full guard file PASS; screenshots at 1280 and 390 of each industry page; check image weight (each page under 2 MB of images, lazy-loaded below the fold).
- [ ] **Step 2:** `judge-agent` against the spec's Renders section. Fix and re-judge on REVISE (cap 3).
- [ ] **Step 3:** Taylor's go, then merge to `main` and push (deploys), spot-check two industry pages live, file renders and sources to Drive `Projects/Top Shelf/renders/2026-11-21-crm-sample-screens/`, update the handoff.

### Task 12: Audit tools (separate plan)

Write a short follow-on plan after push 1 for: `~/.claude/skills/topshelf-seo-audit/scripts/topshelf/offer.py` (PLANS = Signature $99/$199/call; $50 per line; $499 website; remove `$499` from `RETIRED_PRICES`; retire the one-time catalog and `recommend_one_time`; audit copy recommends Signature or the website), the audit PDF copy, and `top-shelf-crm/app/Services/Audit/OneTimeOffer.php`. Those live in two other repos with their own tests and cloud sync, so they get their own plan and review.
