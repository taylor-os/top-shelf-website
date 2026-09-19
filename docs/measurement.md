# Top Shelf — Measurement & Conversion Tracking (plan §12)

How to see how the website is really doing: what's tracked, the one-time setup, and the
monthly rollup you actually read. Internal doc (`.htaccess` 404s `/docs/`), not a public page.

---

## What's tracked (live now)

Every page loads `assets/events.js`, which fires GA4 events for the actions that matter, so
performance is measured in **leads, not pageviews**. GA4 property is **`G-4QCCJ3HP11`**.

| Event | Fires when | Means |
|---|---|---|
| `generate_lead` | someone lands on `thank-you.html` | a **confirmed** free-audit request (the form submits by fetch and redirects here on success) |
| `click_to_call` | a `tel:` phone link is clicked | someone chose to call |
| `book_call` | a booking link is clicked | someone went to book a call |
| `cta_click` | a link to `contact.html` is clicked | someone headed for the audit form |

Every event carries a **`trade`** parameter (from the page's `data-trade`, e.g. `plumbers`,
`real-estate-agents`), so leads and calls are attributable to the trade page that produced
them. All 124 indexable pages + the utility pages carry the script.

---

## One-time setup (do this once, in GA4)

The events fire and collect automatically. To make them count as **conversions**, mark them
as Key Events:

1. GA4 → **Admin** → **Events** (or **Key events**).
2. Toggle **`generate_lead`**, **`click_to_call`**, and **`book_call`** on as **Key events**.
   (`cta_click` stays a normal event — it's a mid-funnel signal, not a conversion.)
3. They start counting as conversions from that point. (GA4 needs ~24h to show a new event
   the first time it fires; click each once on the live site to seed them.)

Search Console needs nothing new: `robots.txt` already points Google to `sitemap.xml`
(124 URLs). Optionally, in GSC → **Sitemaps**, submit `sitemap.xml` to speed discovery.

---

## How you SEE it — the monthly rollup

Three sources, one habit. Check them once a month (dates below are what to compare):

**1. Traffic + leads — Google Analytics 4 (`G-4QCCJ3HP11`)**
- **Reports → Engagement → Events**: the counts of `generate_lead` / `click_to_call` /
  `book_call`. This is the number that matters — leads, not visits.
- **Reports → Acquisition → Traffic acquisition**, channel = **Organic Search**: total organic
  sessions and which landing pages brought them.
- To see **leads by trade**: in Explore (or the Events report), break the events down by the
  `trade` parameter. That tells you which trades' pages actually produce business.

**2. Search performance — Google Search Console**
- **Performance → Search results**: impressions, clicks, average position. Filter Page by
  `for-` (money pages) or by a colony slug to watch the new URLs specifically.
- **Pages (Indexing)**: confirm the new URLs are getting indexed (they're all in the sitemap).
- Early on you're watching **impressions climb** (Google is showing the pages), then **clicks**,
  then **position**. Colony pages (the questions) should show first — they're the easy wins.

**3. Rankings — DataForSEO (via Taylor OS)**
- Rank/position tracking for the money-page keywords (`<service> for <trade>`) and the colony
  questions runs through **DataForSEO** on Taylor OS (the `seo-analyzer` agent, or a direct
  `business_data`/`serp` pull). Run it monthly to see position movement and map-pack presence.
- The pages are brand new as of 2026-09-18, so month 0 is essentially "not ranking yet" — that's
  the baseline. The signal is the **trend** over the following weeks.

---

## What "working" looks like (and when)

Colony strategy is slow-then-compounding. Rough shape to expect:

- **Weeks 2-6:** new URLs indexed (GSC coverage), **impressions** on colony pages start
  appearing, a few colony pages earn their first **clicks**. This is the authority engine
  turning over.
- **Months 2-4:** money-page **positions** climb (target: page 1 for `<service> for <trade>`
  long-tail), AI assistants start citing the answer blocks.
- **The one that matters:** `generate_lead` / `click_to_call` counts attributable to corpus
  pages. A page that ranks but never converts gets its CTA/intent re-examined or merged.
- **Guardrail:** the existing 27 pages' rankings must NOT drop. A site-wide decline after a
  batch is the doorway-penalty signal — pause publishing and audit uniqueness
  (`scripts/dupe_audit.py`) and reachability (`scripts/seo_audit.py`).

---

## The monthly checklist

1. GA4 Events: `generate_lead` / `click_to_call` / `book_call` this month vs last, and by `trade`.
2. GA4 Organic sessions + top corpus landing pages.
3. GSC: impressions / clicks / avg position on the `for-` and colony URLs; indexing coverage.
4. DataForSEO (Taylor OS): position movement on the money-page keywords + map-pack.
5. Guardrail: did any of the original 27 pages lose position? If yes, stop and audit.
6. Kill/merge: any corpus page with zero impressions after 6-8 weeks gets reworked or merged.
