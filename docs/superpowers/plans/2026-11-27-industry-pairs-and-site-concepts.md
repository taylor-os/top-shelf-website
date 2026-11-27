# Industry Pairs, Site Update and Concepts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 12 one-business industry pairs (sample website + 6 CRM screens in one look), the current Top Shelf site updated around them, three new design concepts, five customer-agent reviews, and a fourth concept built from those reviews.

**Architecture:** One shared content file (`renders-src/site-content/content.json`) and one pairs registry (`renders-src/industry-crm/pairs.json`) feed everything. The current site is hand-edited HTML plus small generators. The concepts are rendered by a small Python generator per concept from the same two files, so their information can't drift. CRM screens stay plain HTML on the shared kit and are rendered to images with `render.py`.

**Tech Stack:** Static HTML/CSS/JS, Python 3.13 (generators, pytest), Playwright (renders, checks), the existing kit in `renders-src/industry-crm/kit/`.

**Spec:** `docs/superpowers/specs/2026-11-26-industry-pairs-and-site-concepts-design.md` (read its "Decisions made while Taylor was away"), with `docs/superpowers/specs/2026-11-26-crm-page-research.md` for benefits and buyer questions.

## Global Constraints
- Prices: Signature $99/mo for 1-10 users, $199/mo for 11-25, 26+ "Call for pricing"; phone line $50/mo per line, covers normal use; website $499 one time; no setup fee; month to month; custom layout or a custom industry CRM at the same price.
- CTA: "Try the CRM" → `contact.html` (form; we call, then send a demo); secondary "Call or text (469) 833-3033". Sample sites use 123-456-7890 and contact@<company>.com (`websites/_PROGRAM.md`).
- Claims only from `C:\Users\taylo\Agentic-OS\vault\platter\facts\top-shelf-business-solutions.json`. Research (b) items are not advertised. Reviews: "one tap after every job", never "automatic".
- No em dashes in new copy; humanizer on all new public copy; no invented stats, testimonials, counts or outcomes.
- Every sample screen and site carries a "Sample" label; all businesses and people fictional (web-check new names).
- Current site keeps black and gold, DM Serif Display + DM Sans. Concepts keep the Top Shelf logo initials and mark style; free colors and fonts.
- Concepts live in `preview/concepts-2026-11/<id>/`, every page `noindex`, plus `Disallow: /preview/concepts-2026-11/` in `robots.txt`.
- No paid image generation or downloads; visuals are SVG/CSS art, existing site assets, or the CRM screen renders.
- Nothing merges to `main`. Commit and push the branch after each task.

## Review Focus
1. A pair whose CRM screens still show the old business name, city or theme. Expect: zero; `test_pairs_consistent` greps each set for its old name.
2. The pop-up on a phone (390px): picker and side-by-side must stack and stay usable. Expect: no horizontal overflow; tested in Task 6.
3. A concept page whose prices or features differ from content.json. Expect: all copy comes from content.json; `test_concepts_use_content` checks prices on every concept page.
4. A sample website link from a card that 404s. Expect: every link resolves; the existing link test plus `test_cards_link_pairs`.
5. Keyboard-only use of the pop-up and the concept industry switchers. Expect: focusable controls, Escape closes the pop-up; checked in Task 6 and the concept tasks.

---

### Task 1: Pairs registry and content source
**Files:** Create `renders-src/industry-crm/pairs.json`, `renders-src/site-content/content.json`, `scripts/tests/test_pairs.py`.
**Interfaces — Produces:** `pairs.json` = list of 12 `{slug, industry_label, business, city, website_dir, website_index, crm_dir, mode: "light"|"dark", brand: {primary, accent, ink, bg}, industry_page, industry_anchor}`; `content.json` = `{hero, crm_benefits[], website_benefits[], how_it_works[3], faq[{q,a}], pricing{...}, anti_trap[], industries_intro}` with copy taken from the facts file and the research's recommended order.
- [ ] Write `test_pairs.py::test_pairs_registry` (12 entries, every `website_dir/index.html` and `crm_dir` exists, slugs unique) and `test_content_prices` (content.json mentions $99, $199, $50, $499 and none of the removed prices). Run: fail.
- [ ] Write both files (brand colors read from each website's CSS). Run: pass. Commit.

### Task 2: Vet CRM set
**Files:** `renders-src/industry-crm/briefs/vet.md`, `renders-src/industry-crm/screens/vet/*` (6 screens), `reviews/vet.md`.
- [ ] Persona brief (vet clinic owner, front desk, vet tech, pet owner) per `PERSONA_TASK.md`, business Wellspring Animal Hospital from its website. Build per `BUILDER_TASK.md` with a theme from the website's brand. Persona review, apply fixes. Commit.

### Task 3: Three new sample websites
**Files:** `websites/bramlett-motor-co/`, `websites/larkspur-strength-club/`, `websites/kestrel-lane-detail/` (BRIEF.md, styles.css, app.js, 5 pages, `assets/` with an SVG logo), `websites/_PROGRAM.md` roster rows.
- [ ] One builder per site following `websites/_PROGRAM.md` (no Higgsfield: SVG/CSS visuals), business details matching the CRM set's brief. Judge each. Commit.

### Task 4: Re-skin the 11 approved CRM sets to their websites
**Files:** `renders-src/industry-crm/kit/make_themes.py` (11 palettes from `pairs.json` brand colors), `screens/<slug>/*.html` (business name, city, logo tile, customer-facing header from the website), re-rendered `*.jpg`, `scripts/tests/test_pairs.py::test_pairs_consistent`.
- [ ] Write `test_pairs_consistent`: each set's HTML contains its pair `business` and none of the old names (Prairie Air & Heat, Turnbuckle Auto Repair, Studio Marlowe, Wrenfield, Alderbrook, Holloway & Vane, Larkhaven). Run: fail.
- [ ] Re-theme and rename (owner-builder per industry). Re-render. Run: pass. Contrast check passes. Commit.
- [ ] Halcourt & Vale website copy: practice areas changed to family law, criminal defense and estate planning to match its CRM.

### Task 5: Pairs board
- [ ] Publish an artifact board: per industry the website home screenshot beside its 6 CRM screens. Keep the link for the morning report.

### Task 6: Update the current site
**Files:** `index.html` (#industries cards), new `assets/see-your-business.js` replacing `assets/gap-quiz.js` on every page, `solution-crm.html`, `solution-websites-seo.html`, `crm-by-industry.html` (regenerated with `cbi_build.py` from pairs), industry-page strips, `assets/img/crm/industries/**` (re-exported WebP), tests.
- [ ] Tests first: `test_cards_link_pairs` (12 cards, each has a website image + CRM image + links that exist), `test_popup_replaced` (no page loads gap-quiz.js; every page that did loads see-your-business.js), `test_crm_page_answers` (solution-crm.html contains every content.json FAQ question and none of the (c) claims: Apple Pay, tap to pay, QuickBooks, Spanish). Run: fail.
- [ ] Build: cards, pop-up (industry chips → website shot + CRM shot side by side → Try the CRM; Escape closes; once per session; reopen tab "See your business"), CRM page (benefits by screen, 3-step how it works, anti-trap box, FAQ, price), Websites page (13 sample sites + "every form feeds your CRM"), regenerate CRM by Industry and strips. Run: pass; Playwright 390/1440 no overflow, no console errors. Humanizer, fact gate. Judge. Commit.

### Task 7-9: Concepts A, B, C
**Files:** `scripts/concepts/build_concept.py` (shared loader: `load() -> (content: dict, pairs: list)`), `scripts/concepts/<id>/templates/*` and `scripts/concepts/<id>/style.css`, output `preview/concepts-2026-11/<id>/{index,crm,websites,industries}.html` and `industries/<slug>-crm.html`, `industries/<slug>-website.html` for all 12.
- [ ] Shared test `test_concepts_use_content`: every concept page is `noindex`, shows the four prices where pricing appears, links resolve, no em dashes, logo mark present. Run: fail.
- [ ] Each concept: a different direction drawn from the research (A: bright product-led SaaS; B: cinematic dark showcase; C: editorial, warm, trade-proud), its own fonts and palette, the Top Shelf mark. Generate, verify 390/1440, Judge. Commit.

### Task 10: Customer agents
- [ ] Five prospect personas (HVAC owner, auto shop owner, salon owner, dental office manager, restaurant GM) each review the current site and concepts A-C on phone and desktop as buyers; consolidated findings in `docs/superpowers/specs/2026-11-27-customer-agent-findings.md`.

### Task 11: Concept D
- [ ] Built from the findings (same generator), with a short "what this applies" note at `preview/concepts-2026-11/d/NOTES.md`. Judge. Commit.

### Task 12: Close
- [ ] Full test suite, previews published (current site pages, each concept), Drive copies of renders, handoff updated, morning report with decisions to review.
