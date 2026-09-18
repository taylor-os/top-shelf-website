# Top Shelf — SEO + AEO Corpus Plan (v2, blueprint LOCKED 2026-09-18)

Status: **strategy + blueprint locked. Corpus not yet built.** This is the plan the
owner asked to finish before generating any pages. v1 (2026-08-01) decided the
strategy; v2 finishes the engine: the trade list, the valid service×trade matrix, URL
structure, page templates, the uniqueness gate, internal-link sculpting, the AEO layer,
the data layer, and phasing.

Private: `.htaccess` returns 404 for `/docs/` and any `.md`, so this doc is not
web-reachable. It is an internal blueprint, not a public page.

---

## 0. What changed since v1 (read this first)

- **The v1 "site gaps — fix first" list is DONE.** The 2026-09-17 elite-SEO pass shipped
  `llms.txt`, schema on all 27 main pages (`WebSite` + `ProfessionalService` #business,
  `Service` + `Offer`, `FAQPage`, `BreadcrumbList`, `ContactPoint`, `AboutPage`,
  national `areaServed`), a real service-area statement, an accurate `sitemap.xml`
  (27 URLs), and apex→www 301. So the foundation the corpus depends on now exists.
- **The 27 main pages are verified interconnected + SEO-complete** (2026-09-18 audit,
  `scripts/seo_audit.py`: 0 blocking, 0 warnings). The corpus attaches to a clean base.
- **Data layer upgrade:** v1 blocked on "owner connects SemRush." Replaced with
  **DataForSEO** (already wired, creds on Railway; used live for the GBP ratings). It
  returns search volume, keyword difficulty, SERP, and PAA programmatically — so keyword
  validation is a script step, not an owner dependency. SemRush stays optional.
- Everything below is the LOCKED blueprint. Building starts only after the owner reviews
  this doc.

---

## 1. Strategy (locked, carried from v1)

- **Axis = trade vertical, never geography.** City pages on an offering that is
  identical everywhere are Google's textbook doorway pages; at corpus scale that risks
  site-wide quality demotion that would drag the existing 27 pages down. Trades genuinely
  differ (a plumber's after-hours emergency call ≠ a med spa's no-show ≠ a law firm's
  intake), so per-trade pages write themselves differently. Cities appear **only** in the
  metro block, **only** for large metros, **only** carrying local data no other page has.
- **Colony model (Edward Sturm).** Authority is mechanical and page-level. Manufacture it
  internally: publish a colony of easy, in-topic FAQ/answer pages → they rank → earn
  clicks → generate their own authority → **internal-link that authority into BOFU money
  pages** (the service×trade landing pages). No backlink outreach required.
- **Keyword placement rule (every page):** exact target phrase in **title + URL slug**
  (highest weight), then **H1 + first sentence**. Non-negotiable.
- **Long-tail only.** "CRM software", "SEO services" belong to HubSpot/Salesforce. We
  target buyer-intent long tail ("ai receptionist for plumbers", "why do i keep missing
  service calls"), which is where the buying intent is anyway.

---

## 2. The trade list — the engine (~100 trades, grouped by the 9 existing umbrellas)

The 9 industry pages are **hubs**; the trades below are their **spokes** (the terms
people actually search — nobody searches "home services", they search "plumber"). Demand
tier is a first guess to be replaced by DataForSEO volume (§9); it only sets build order.

**Home Services (hub: industry-home-services)** — plumber, HVAC / air conditioning,
electrician, roofer, garage door repair, landscaper / lawn care, painter, handyman, pest
control, house cleaning / maid, appliance repair, fencing, concrete / masonry, gutters,
pressure washing, tree service, pool service, locksmith, flooring, remodeling /
general contractor, drywall, insulation, septic, chimney sweep, foundation repair,
waterproofing, junk removal, moving / movers, window / glass, garage / epoxy, irrigation,
solar install, deck / patio builder. *(~33 — the deepest umbrella; highest local demand.)*

**Auto (hub: industry-auto)** — auto repair shop, collision / body shop, auto detailing,
tire shop, oil change / quick lube, transmission shop, mobile mechanic, window tint,
auto glass, muffler / brake shop, used-car dealer.

**Medical & Dental (hub: industry-medical-dental)** — dentist, orthodontist, med spa,
chiropractor, physical therapy, optometry / eye care, dermatology, veterinary /
animal hospital, urgent care, audiology, fertility / IVF clinic.

**Salon, Spa & Fitness (hub: industry-salon-spa-fitness)** — hair salon, nail salon,
barbershop, day spa, massage therapy, gym / fitness studio, yoga studio, pilates studio,
personal trainer, tanning salon, lash / brow bar, CrossFit box, martial arts / dojo.

**Legal (hub: industry-legal)** — personal-injury attorney, family-law attorney, criminal-
defense attorney, estate-planning attorney, immigration attorney, bankruptcy attorney,
business attorney, real-estate attorney.

**Real Estate (hub: industry-real-estate)** — **realtor / real-estate agent** (the
PRIORITY spoke — owner-flagged 2026-09-18, leads phase 1; see §11), listing agent,
buyer's agent, real-estate broker / brokerage, real-estate team, luxury real-estate
agent, commercial real-estate broker, property management, mortgage broker / lender,
title company, home inspector, appraiser. *(Real estate is an actively-targeted vertical
for Top Shelf, so it gets first-class depth, not a single thin page.)*

**Restaurants & Food (hub: industry-restaurants)** — restaurant, cafe / coffee shop,
bakery, food truck, caterer, bar / brewery, pizzeria, juice / smoothie bar.

**Retail (hub: industry-retail)** — boutique / clothing, furniture store, jewelry store,
florist, gift shop, specialty grocery, vape / smoke shop.

**Custom / other (hub: industry-custom)** — the catch-all for a trade that fits none of
the above; not a spoke generator, it stays the bespoke landing hub.

> ~100 trades. Prune/extend against DataForSEO before generation. This list is the single
> most load-bearing input to the whole corpus — get it right before anything ships.
>
> **Realtor / real estate = a prioritized vertical (owner, 2026-09-18):** it leads phase 1
> alongside the top home-services trades (§11) and earns its own pillar + full money-page
> set + colony. Naming note: "Realtor®" is an NAR trademark for members — use **"real
> estate agent"** as the general term in body copy, and **"realtor"** in slugs and where it
> is the accurate, high-volume search term (`/for/realtors/`, `/crm-for-real-estate-agents/`).

### 2b. The valid service×trade matrix (prevents nonsense doorway pages)

Not every service applies to every trade — "POS system for a personal-injury lawyer" is
a garbage page that only adds doorway risk. Generate a service×trade page **only** where
the service genuinely applies:

| Service (solution page) | Applies to |
|---|---|
| AI Phone / Receptionist (`solution-ai-phone`) | **Universal** — any trade that takes calls |
| Automation (`solution-automation`) | **Universal** |
| CRM / Follow-up (`solution-crm`) | **Universal** |
| Reviews (`solution-reviews`) | **Universal** |
| Websites & SEO (`solution-websites-seo`) | **Universal** |
| Marketing (`solution-marketing`) | **Universal** |
| Payments (`solution-payments`) | **Universal** (everyone collects money) |
| Online Booking (`solution-booking`) | Appointment trades only — home services, salon/spa/fitness, medical/dental, auto, some legal/real-estate. **Not** walk-in retail/restaurant. |
| Memberships (`solution-memberships`) | Recurring-revenue trades only — fitness, salon/spa, med spa, pool service, pest control, HVAC maintenance, auto (service club). **Not** one-off trades (roofer, PI lawyer, mover). |
| POS & Inventory (`solution-pos`) | Point-of-sale trades only — retail, restaurant/food, salon (retail products), some auto. **Not** dispatch/professional services. |

Effect: 7 universal services × ~100 trades (~700) + 3 conditional services (Booking,
Memberships, POS) against only their applicable trades (~125 combined: Booking ~75,
POS ~30, Memberships ~20) ≈ **~800 valid service×trade pages**, not a naive 1,000 — and
every one is a page a real owner of that trade would actually want.

---

## 3. Architecture — ~1,800 pages (at full build, pre-DataForSEO pruning), 8 blocks

| Block | Pages | URL pattern | Source of uniqueness |
|---|---:|---|---|
| Service × trade (money) | ~800 | `/<service-slug>-for-<trade-slug>/` | per-trade workflow, dollar value, objection, incumbent tool |
| Trade hubs (pillar) | ~95 | `/for/<trade-slug>/` | one pillar per trade, links to all its service pages |
| Problem / symptom | ~150 | `/problems/<question-slug>/` | distinct real owner questions |
| Cost & pricing | ~100 | `/cost/<trade-or-service-slug>/` | per-trade economics, real ranges |
| Comparison / alternatives | ~150 | `/vs/<competitor-or-alt-slug>/` | named competitors (Hibu, Thryv, Housecall Pro, Jobber, Podium…) |
| How-to / JTBD | ~200 | `/how-to/<task-slug>/` | genuinely different tasks |
| State (compliance) | ~50 | `/<state-slug>/` | SMS/TCPA, licensing, seasonality that really vary |
| Major metro | ~200 | `/<metro-slug>/<service-or-trade-slug>/` | top ~50 metros × 3–4, each with local market data + labelled worked example |

Flat, keyword-first slugs (colony rule). The 9 existing `industry-*` pages remain the
**top hubs**; the new `/for/<trade>/` pillars sit one level under their umbrella and link
up to it.

---

## 4. URL structure (locked)

- **Money page:** `/<service>-for-<trade>/` → `/ai-receptionist-for-plumbers/`,
  `/online-booking-for-med-spas/`. Service uses the searched noun, not our product name
  ("ai-receptionist", not "ai-phone"; "review-software", not "reviews").
- **Trade pillar:** `/for/<trade>/` → `/for/plumbers/`, `/for/med-spas/`.
- **Problem:** `/problems/<slug>/` → `/problems/keep-missing-service-calls/`.
- **Cost:** `/cost/<slug>/` → `/cost/crm-for-hvac/`, `/cost/answering-service-plumber/`.
- **Comparison:** `/vs/<slug>/` → `/vs/housecall-pro/`, `/vs/podium/`, `/vs/hibu/`
  (the existing `switching-from-hibu-thryv.html` is the canonical Hibu/Thryv page; `/vs/`
  pages link to it, they don't duplicate it).
- **How-to:** `/how-to/<slug>/` → `/how-to/reduce-no-shows-at-a-salon/`.
- **State:** `/texas/`, `/oklahoma/` (compliance/seasonality only).
- **Metro:** `/dallas/<slug>/` → `/dallas/ai-receptionist/`.
- Rules: lowercase, hyphenated, trailing slash, plural trade nouns ("plumbers"), no dates,
  no stop-word stuffing, ≤ 5 slug words. Each URL is unique and permanent (301 if renamed).
- **Physical layout:** generated as real static `.html` (matches the hand-built site;
  Hostinger serves `/slug/` from `/slug/index.html` or `/slug.html` via the existing
  rewrite). Decide one convention at build time and keep it uniform.

---

## 5. Page templates (locked) — the anti-thin contract

Every template below has a **minimum unique-content spec**. A page that can't meet it does
not get generated — it becomes a section or FAQ on a parent page instead (§7).

**Money (service × trade)** — H1 `<Service> for <Trade>` · first sentence repeats it ·
≥ 600 words, of which ≥ 250 are trade-specific (the trade's real workflow, the dollar
value of the problem for that trade, the top objection, the incumbent tool it replaces) ·
3–5 trade-specific FAQs · one labelled *"illustrative example, not a client"* mini-scenario ·
BOFU CTA (free audit / call) · schema: `Service` + `FAQPage` + `BreadcrumbList` ·
40–60-word extractable answer block up top (AEO).

**Trade pillar (`/for/<trade>/`)** — the trade's whole story: every gap Top Shelf closes
for that trade, links to all that trade's service×trade pages + its problem/cost/how-to
pages. ≥ 800 words. schema: `Service` (broad) + `FAQPage` + `BreadcrumbList`. This is the
authority sink for the trade; it receives colony links and passes them to money pages.

**Problem / symptom** — one real question as H1 + slug + first sentence · a direct 40–60-
word answer first (AEO), then depth · links to the money page that solves it · schema:
`FAQPage` or `QAPage` + `BreadcrumbList`. These are the colony.

**Cost** — real ranges, per trade, with the honest "it depends" drivers · never a
fabricated number · links to `pricing.html` + the relevant money page · schema:
`FAQPage` + `BreadcrumbList` (no fake `Offer` price on editorial cost pages).

**Comparison (`/vs/`)** — honest, no straw-manning a named competitor; state what they're
good at, then the specific gap Top Shelf fills · schema: `FAQPage` + `BreadcrumbList` · the
Hibu/Thryv comparison stays on `switching-from-hibu-thryv.html`; `/vs/` pages link to it.

**How-to / JTBD** — a genuinely different task, step list, answer-first · `HowTo` schema
only when the steps are literal + accurate, else `FAQPage`.

**State** — only the parts that truly vary (TCPA/SMS consent, licensing, seasonality).
No boilerplate padding. If a state has nothing unique to say, it doesn't get a page.

**Metro** — real local market data (SERP snapshot, local demand, a labelled worked
example). Same anti-doorway bar as everything else — a metro page with no local data is
exactly the page this whole plan refuses to build.

---

## 6. Internal-link sculpting (locked)

The colony is worthless without deliberate linking. The authority flow:

```
Problem / How-to / Cost colony  ──►  Trade pillar (/for/<trade>/)  ──►  Service×trade money page  ──►  contact.html / booking.html
        (easy, rank first)              (authority sink)                  (BOFU, converts)              (the conversion)
```

Rules:
- **Every colony page links UP** to its trade pillar and ACROSS to the one money page it
  most implies (contextual, in-body, keyword-anchored — not a nav dump).
- **Every trade pillar links DOWN** to all its service×trade pages + its colony pages, and
  **UP** to its industry umbrella hub (the existing `industry-*` page).
- **Every money page links** to: its trade pillar (up), 2–4 sibling service×trade pages for
  the same trade (across), the existing solution page it extends (e.g.
  `/ai-receptionist-for-plumbers/` → `solution-ai-phone.html`), and `contact.html` (BOFU).
- **The existing 27 pages tie in:** each `industry-*` hub gets a "trades we serve" block
  linking to its `/for/<trade>/` pillars; each `solution-*` page gets a "by trade" block
  linking to its top service×trade pages. This is the bridge from the authority already on
  the main site into the corpus (and back).
- **Link budget:** 3–8 contextual internal links per colony page, 15–40 per pillar. No
  orphans — `scripts/seo_audit.py` (extended to the corpus) enforces every page has ≥ 1
  contextual inbound before it ships.
- **Anchor text = the target's keyword**, varied naturally, never "click here".

---

## 7. Uniqueness gate (locked) — the anti-doorway enforcement

- **`scripts/dupe_audit.py` becomes a PRE-publish gate, not a post-hoc report.** Shingle
  (k=8 word n-gram) Jaccard similarity of each candidate page's *body* against every other
  corpus page + the 27 existing pages.
- **Threshold: nothing ships above ~35% overlap.** A candidate over threshold is **merged**
  into the closest existing page (as a section/FAQ) — never published thin.
- Boilerplate (nav, footer, CTA, schema) is stripped before shingling so only real body
  content is compared (same nav/footer across pages must not count as duplication).
- The gate runs in the generation pipeline (§10) and blocks the build on failure, the same
  way the fact-gate does. A build that would emit 200 near-identical service×trade pages
  fails loudly instead of shipping doorway spam.
- **Per-trade material requirement** is the upstream half of this: the template minimums in
  §5 force real per-trade substance, so pages are *born* unique, not deduped after.

---

## 8. AEO layer (locked)

- **`llms.txt` extended** to index the corpus by trade + service (already live for the 27
  pages; append the pillar + top money URLs as they ship).
- **Extractable answer block** at the top of every colony/problem/cost/how-to page: a
  40–60-word, self-contained, plain-language answer to the page's question — the block an
  AI assistant lifts verbatim. Written first, before the long-form body.
- **Schema per template** as specified in §5. `FAQPage`/`QAPage` on colony pages is the AEO
  workhorse (AI answer engines parse clean Q&A even though Google restricts FAQ *rich
  results* to gov/health — do not promise Google FAQ snippets; the win is AI citation +
  valid structured data).
- **AEO question forms kept as a separate list** from Google queries — conversational
  phrasings ("what's the best way for a plumber to stop missing after-hours calls") differ
  from typed queries and seed the problem/how-to blocks.
- **Entity + NAP consistency** everywhere: same business name, phone `(469) 833-3033`,
  `contact@topshelfsolutions.io`, domain, `#business` `@id` — so the entity graph is
  unambiguous to crawlers and assistants.

---

## 9. Data layer (locked) — DataForSEO, not "owner connects SemRush"

- **Volume / KD / intent:** DataForSEO Labs + Keyword Data endpoints (creds on Railway,
  location_code 2840 US) score every candidate keyword. Prune everything with no real
  demand; rank survivors by **easiest-win-per-volume** (low KD × real volume × buyer
  intent).
- **PAA / question mining:** DataForSEO SERP `people_also_ask` (+ AlsoAsked.com as a free
  cross-check) feeds the problem/how-to/colony blocks.
- **SERP reality check:** before committing a money-page keyword, pull the live SERP — if
  page 1 is all national SaaS with the term in title/slug, deprioritize (colony rule:
  target terms competitors *don't* put in title/URL/H1/first line).
- SemRush stays an optional manual cross-check; it is no longer a blocker.

---

## 10. Generation pipeline + gates (locked)

Every page runs the same gates the main site does, wired into the generator so quality is
enforced mechanically, not by hope:

```
1. Seed        seed.csv/json (service × trade × intent × geo × AEO-form), DataForSEO-validated
2. Generate    one template-driven .html per surviving keyword (keyword in title/slug/H1/1st line)
3. Uniqueness  dupe_audit.py pre-publish gate (< 35% overlap) — over-threshold → merge, don't ship
4. Fact-gate   python -m platter.factcheck against top-shelf-business-solutions.json (no fabricated stat/price; gap-not-leak; dash-free)
5. Humanize    humanizer pass on visible prose (public-facing) — no AI tells, invents nothing
6. Schema      inject_faq_schema.py + template schema; validate all JSON-LD parses
7. Interlink   apply §6 sculpting; seo_audit.py confirms 0 orphans / 0 broken links
8. Judge       independent judge-agent on a sample of each batch before publish
9. Publish     PHASED — ~100 → measure 4–6 weeks → scale. Never dump 2,000 pages at once.
```

Reusable scripts already in `scripts/`: `build_sitemap.py`, `inject_faq_schema.py`,
`seo_audit.py`, `sample_site_seo.py`. To build: `dupe_audit.py` (extend to pre-publish
gate) + a `generate_corpus.py` template engine.

---

## 11. Phasing (locked) — the first ~100 pages

Prove the model on a tight, high-intent slice before scaling:

1. **6 priority trades** = the top 5 Home-Services trades by DFW local demand (expected:
   plumber, HVAC, electrician, roofer, garage-door — the deepest umbrella and where GDR/TAP
   already give us real domain knowledge) **+ realtor / real-estate agent** (owner-
   prioritized vertical, 2026-09-18 — Top Shelf is actively targeting real estate, so it
   leads the corpus alongside home services).
2. For each: the **trade pillar** (`/for/<trade>/`) + its **money pages**. The 5 home-
   services trades take the ~7 universal services each; **realtor** takes the 7 universal
   **+ Online Booking** (agents book showings/consults) = 8, since booking/CRM/reviews are
   especially strong for agents. ≈ 6 pillars + ~43 money pages = **~49 BOFU pages.**
3. **~55 colony pages** — the top problem/how-to/cost questions for those 6 trades
   (DataForSEO PAA), each internal-linked up into its pillar + across into a money page.
   Realtor colony examples: "best CRM for real estate agents", "how do realtors get more
   listings", "how to follow up with real estate leads", "cost of a real estate agent
   website".
4. Wire the industry hubs used in phase 1 (**home-services + real-estate**) + relevant
   solution pages to the new pillars (§6 bridge).
5. **Measure 4–6 weeks** (GSC impressions/clicks/position on the new URLs, any movement on
   money pages). Only then green-light the next trades. Kill or merge anything that draws
   zero impressions.

First-100 target ≈ 6 pillars + 43 money + 55 colony + wiring (~104). If it moves, scale
trade by trade. If it doesn't, we've risked ~100 pages, not 2,000.

---

## 12. Success metrics

- **Leading (weeks 2–6):** new URLs indexed (GSC coverage), impressions on colony pages,
  colony pages earning clicks (the authority engine turning over).
- **Mid (2–4 months):** money-page positions climbing (target: top 10 for
  `<service> for <trade>` long-tail), AI-assistant citations for the answer blocks.
- **Business (the only one that matters):** free-audit form + tap-to-call conversions
  attributable to corpus pages. A page that ranks but never converts gets its CTA/intent
  re-examined or is merged.
- **Guardrail metric:** existing-27-page rankings must NOT drop. A site-wide decline after
  a batch is the doorway-penalty signal — pause publishing and audit uniqueness.

---

## 13. Risks & the Skeptic's ledger

- **Doorway penalty (the #1 risk).** Mitigated four ways: trade-not-city axis, the §7
  uniqueness gate, the §5 per-trade material minimums, and §11 phased publishing. If the
  guardrail metric (§12) ever fires, publishing stops.
- **Thin service×trade pages.** The valid-combo matrix (§2b) + template minimums (§5) mean
  a page that can't say something real about that trade is never generated.
- **Fabricated proof.** Example businesses are purpose-built + labelled *"illustrative
  example, not a client."* Never present an invented business as a real client. The
  fact-gate enforces no invented stats/prices. (The 23 real-name prospect demos in
  `topshelf-demos/` stay PRIVATE 1:1 — never scaled onto public pages; trademarked names on
  public pages imply a relationship we don't have.)
- **Maintenance load.** 2,000 pages is a corpus to maintain, not fire-and-forget. Phasing +
  killing zero-impression pages keeps it lean; the generator + gates make regeneration
  cheap.
- **Effort vs return (CFO).** Front-loaded, but the long tail is where buyer intent lives
  and the colony ranks money pages without paid backlinks — the marginal cost per page
  after the pipeline exists is low. The first-100 phase is the ROI test before the spend.

---

## 14. Next actions, in order (start of the build phase)

1. **Lock the trade list** against DataForSEO volume (prune/extend §2).
2. **Build the valid service×trade seed** (CSV + JSON) from §2b, DataForSEO-validated.
3. **Write `generate_corpus.py`** (template engine, §5) + **extend `dupe_audit.py`** into
   the pre-publish gate (§7).
4. **Generate + gate the first ~49 BOFU pages** — 6 pillars for the 6 priority trades
   **including realtor** (the 5 home-services trades take ~7 universal services each;
   **realtor** takes 7 universal + Online Booking = 8, per §11), run the full pipeline
   (§10), Judge the batch.
5. **Generate + gate the ~55 colony pages**, apply §6 sculpting, `seo_audit.py` clean.
6. **Wire the bridge** from the 27 existing pages (§6) and **publish phase 1**.
7. **Instrument + measure 4–6 weeks** (§12) → decide scale.

Skills to pull when building: `topical-authority`, `claude-seo:seo-cluster`,
`seo-geo` (AEO), the `seo-analyzer` / `seo-fixer` agents (live DataForSEO + rubric),
`local-landing-page`, `seo-rank-playbook`.
