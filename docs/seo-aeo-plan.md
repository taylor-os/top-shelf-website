# Top Shelf — SEO + AEO corpus plan (agreed 2026-08-01)

Status: **plan agreed, corpus not yet built.** Resume at step 1 below.

Private: `.htaccess` returns 404 for `/docs/` and for any `.md`, so this is not
web-reachable.

---

## The decision that shaped this

Owner's original ask was ~800 (later ~2,000) pages built on a service × city
matrix, national coverage.

Owner also said, of the service: *"all of what we do applies to every small
business."* That sentence is the problem. If the offering is identical in every
city and there is no local material, city pages are Google's textbook
definition of doorway pages — *"multiple pages with the same or similar content
designed to rank for specific queries like city or state names."* At 2,000
pages the consequence is not weak rankings on those pages, it is site-wide
quality demotion that drags the existing 29 pages down.

So the corpus is built on **trade vertical**, not geography. A plumber's
missed-call problem and a med spa's no-show problem genuinely differ in
workflow, dollar value, objection and incumbent tooling. Ten pages about ten
trades write themselves differently; ten pages about ten cities do not.

This is also the stronger AEO position. People ask an assistant *"what's the
best CRM for a plumbing company"*, never *"best CRM in Flower Mound."*

---

## Architecture — target ~2,000 pages

| Block | Pages | Source of uniqueness |
|---|---:|---|
| Service × trade | ~1,000 | 10 services × ~100 trades |
| Trade hubs | 100 | One pillar per trade |
| Problem / symptom | 150 | Distinct real questions |
| Cost & pricing | 100 | Per-trade economics |
| Comparison / alternatives | 150 | Named competitors |
| How-to / JTBD | 200 | Genuinely different tasks |
| State | 50 | SMS/TCPA rules, licensing, seasonality really do vary |
| Major metro | ~200 | Top ~50 metros × 3–4, each with local market data, local SERP analysis, and a labelled worked example |

Cities appear **only** in the last block, **only** for large metros, and **only**
carrying research no other page has.

## The five seed dimensions

1. **Service** — the 10 live services
2. **Trade** — ~100 verticals. The 8 site umbrellas do not get searched;
   sub-trades do (plumber, HVAC, roofer, med spa, chiropractor, …)
3. **Intent** — problem-aware / solution-aware / comparison / cost / how-to /
   best-of / near-me
4. **Geography** — states (compliance) and top metros only
5. **AEO question forms** — long conversational phrasings, kept as a separate
   list because they differ from Google queries

## Hard constraints

- **Uniqueness gate.** `scripts/dupe_audit.py` becomes a pre-publish check, not
  a post-hoc report. Nothing ships above ~35% shingle overlap against every
  other page. Failures get merged into an existing page rather than published
  thin.
- **Example businesses are purpose-built and labelled** *"illustrative example,
  not a client."* The existing 23 demos in `topshelf-demos/` use REAL
  trademarked names (Budget Blinds, Gerber Collision, Woodhouse Spa, Dental
  Depot) with no disclaimer. Fine as private 1:1 prospect demos; publishing
  them on public landing pages is public trademark use implying a
  relationship. Do not scale that.
- **No fabricated proof.** Invented businesses must never be presented as real
  clients. Standing rule: honest audits, no fabricated stats.
- **Phased publishing.** ~100 → measure → scale. Dumping 2,000 pages onto a
  29-page site is itself a spam signal regardless of quality.
- **Head terms are unwinnable.** "CRM software", "SEO services" belong to
  HubSpot and Salesforce. Everything here targets the long tail, which is
  where the buying intent is anyway.

## Site gaps this depends on (fix first — cheaper and faster than 2,000 pages)

- No service area stated anywhere. One mention of "Denton" across 29 pages.
- Zero city/location pages.
- `Organization` schema only. No `LocalBusiness`, `Service`, `FAQPage`, or
  `areaServed`.
- No `llms.txt`, no structured-markdown availability for AI crawlers.

---

## Next actions, in order

1. **Build the seed corpus** — all five dimensions, grouped by cluster, emitted
   as CSV + JSON for direct SemRush import. AEO question forms kept separate.
2. **Build the ~100-trade list** with rough demand expectations. This is the
   engine of the whole corpus.
3. **Write the AEO spec** — `llms.txt`, schema types per page template, 40–60
   word extractable answer blocks, entity/NAP consistency.
4. **Draw the architecture map** — which cluster earns a page, which becomes a
   section or FAQ on an existing page.
5. **Owner connects SemRush** → validate volume/KD/intent, prune everything
   with no real demand, rank survivors by easiest-win-per-volume.
6. **Extend `dupe_audit.py`** into the pre-publish gate.

Skills worth pulling: `topical-authority`, `claude-seo:seo-cluster`,
`claude-seo:seo-programmatic`, `seo-geo` (AEO), `local-landing-page`,
`seo-rank-playbook`.
