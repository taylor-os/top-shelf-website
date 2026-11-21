# Top Shelf site: focus on the CRM plan and the website (design)

Date: 2026-11-21 · Owner: Taylor · Branch: `feat/crm-website-focus` (worktree `C:\Users\taylo\top-shelf-website-focus`, cut from `origin/main` 1a615bb)
Status: approach and decisions approved by Taylor in chat on 2026-11-21; builder-check questions answered the same day.

## Intent

Top Shelf stops selling a menu of services and sells two things: the **Signature plan** (the Top Shelf CRM with a phone line, texting and an AI chatbot) and a **professional website**. Every page on topshelfsolutions.io has to say that, at the new prices, without breaking a link, an old email, a printed QR code or a Google result. The CRM sales pitch gets real-looking screens for every industry the site targets, so an owner can picture their own business in it.

Why now: the $99 / $199 price is already printed on the counter desk ads (2026-11-19/20); the site still sells $299 / $899 / $2,500 plans and nine one-time jobs.

## What is being sold (owner decisions, verbatim where quoted)

| Item | Price | Notes |
|---|---|---|
| Signature plan, 1-10 users | $99/mo | "we are just going to have the Signature" plan. Called a **plan**, never a blend (owner, again 2026-11-21) |
| Signature plan, 11-25 users | $199/mo | |
| Signature plan, 26+ users | Call for pricing | "26+ will be call for pricing". No price shown |
| Phone line (calling + texting from the app) | $50/mo standard rate | Owner 2026-11-21: "we will charge them $50 as a standard rate per month for our phone unless their charges exceed the $50 a month then extra charges will apply we can figure that out later". Copy says $50/mo covers normal use and usage beyond that is billed; no caps or overage rates shown yet |
| Professional website | $499 one time | "a full website take off the page requirements just put for a professional website". No page count anywhere. Not included in Signature |

Signature includes (owner 2026-11-20 in the facts file, reconfirmed 2026-11-21 "all of it is in"): the CRM (contacts, pipeline, follow-up reminders), an **AI receptionist that answers and books jobs**, missed-call text-back, online booking, dispatch board, customer hub, invoice by text, review requests, review replies, on-my-way texts, estimates, card payments, and an **AI chatbot added to the customer's current website** (owner: advertise it now, "Put on the site"). The business phone number (port the current one or get a new one) with calling and texting from the app is the $50/mo phone line above. No setup fee, month to month.

The $499 website includes (owner 2026-11-21): a mobile-friendly custom design built by us, built so Google can read it (on-page basics only; no ongoing SEO service), a contact/booking form that feeds the CRM, and a logo if they need one. Hosting stays out of customer copy.

Main call to action on every page (owner 2026-11-21): **"Try the CRM"**, with a smaller "Call or text (469) 833-3033" beside it. "Try the CRM" does NOT give a login (owner: "it doesnt give them a login it has them fill out a form and then we can contact them and I will send them a demo after talking with them"). It opens a short request form that posts to the existing website-lead endpoint (the one `contact.html` already uses, which alerts the owner by email and text); Taylor calls them, then sends a demo himself. My call: `contact.html` becomes that request form (drop the required Google Business Profile field and the audit framing; keep name, business, phone, email, industry, number of users, SMS consent), so the endpoint, thank-you page and owner alerts keep working. No page on the site links to a self-serve demo login. "Get Free Audit" leaves the nav and hero CTAs.

Removed from sale everywhere: Essentials ($299), the old Signature ($899) feature list, Platinum ($2,500), the Operate reserve ($599), the three Get Found packages ($795 / $1,995 / $500), the one-time jobs (listing fix $345, map-pack push $1,250, 5-page site $1,500, one-page site $495, take back what's yours $495, review reply catch-up $150, extra page $325, review card $95), and the services that are not CRM or website features: ongoing SEO, Google Business Profile work, map-pack push, ads, social media, marketing, POS & Inventory, memberships, and the free SEO/Google audit as the lead-in.

## Goals

1. Every page offers only Signature ($99 / $199 / call, plus the $50/mo phone line) and the $499 website, and every main button leads to the Try the CRM request form.
2. No removed page returns a 404 or keeps serving old prices: each one 301-redirects to its closest surviving page.
3. Old prices cannot come back on the next generator run: the change is made in the sources (`offer.py`, the page generators and their spec files), then pages are rebuilt.
4. The real-estate CRM renders (9 screens) appear on the site paired with the matching website pages, under a fictional agent.
5. New "Sample screens" CRM renders for each site industry that has no CRM yet, built with sample data.
6. The outreach audit tool and the CRM's in-app audit stop recommending removed jobs (after the site push).

## Non-goals

- No change to the 299 prospect demos under `demo/` (they keep their own noindex pages).
- No building of the actual industry CRMs (owner: "we will build them" later); the renders are sample screens.
- No building of the per-client AI chat widget in top-shelf-crm here (it is still `pending` in `config/essentials.php`; owner chose to advertise it now). Tracked as a separate follow-up.
- No new visual redesign of the site; existing templates, styles and the Signature-gold look stay.

## Anti-goals (would make this a failure even if it "works")

- Any page, schema block, `llms.txt` line or sitemap entry still showing a removed price or plan.
- Any internal link pointing at a removed page.
- A removed URL that still loads at 200 (this host never deletes files on deploy, see `.htaccess`).
- A real person's name (Sarah Laos) on a public Top Shelf marketing page.
- Sample screens presented as a shipped product without the "Sample screens" label.
- Calling it a "blend" anywhere.

## Constraints

- Hostinger GitHub App deploys `main` to `public_html` on push (about 15 s). The push is the deploy, so the work stays on the branch until every check passes.
- The host adds and updates files on deploy but never deletes them. Removal = delete from repo AND a `Redirect`/`RedirectMatch 301` in `.htaccess` (existing pattern in that file).
- About 760 HTML pages, most generated: colony, pillar, corpus, answer-hub, vs and one-time generators in `scripts/`, plus `wire_*.py` passes that must re-run after any generator. Hand-written pages: `index.html`, `pricing.html`, `solution-*.html`, `industry-*.html`, `why-us.html`, `contact.html` and a few others.
- `offer.py` (`~/.claude/skills/topshelf-seo-audit/scripts/topshelf/offer.py`) is the authoritative price list and has an amount linter (`AUTHORIZED_AMOUNTS`, `RETIRED_PRICES`). Its rules still apply: single prices never ranges, no lump-sum totals, no setup fee, no refund wording, hosting never in copy.
- Public copy gets the humanizer pass (CLAUDE.md §0.5) and must stay em-dash free in new copy. Facts about Top Shelf go through the fact gate against `vault/platter/facts/top-shelf-business-solutions.json` (already holds $99 / $199).
- The Artifact tool can't publish pages with a real person's name; Sarah Laos material is previewed on localhost only.

## Approaches considered

1. **Source-first rebuild with redirects (chosen).** Change `offer.py`, generator templates and spec files; delete the generators/specs for removed families; regenerate; hand-edit the static pages; add family-level `RedirectMatch 301` rules; verify with a link checker, an old-price sweep and a post-deploy redirect test. Survives the next generator run and keeps search credit through redirects.
2. **Find-and-replace across the built HTML.** Fast, but the next generator run restores old prices, and it can't decide which pages to remove. Rejected.
3. **Strip to about 20 core pages and redirect everything else to the homepage.** Simplest site, but throws away almost all long-tail search traffic, and redirecting hundreds of pages to `/` reads as soft-404s to Google. Rejected.

## Page decisions (by family)

Counts are from `origin/main` 1a615bb.

| Family | Count | Decision | Redirect target if removed |
|---|---|---|---|
| `marketing-for-*` | 57 | Remove | `/for-<same>.html` (industry page) |
| One-time job + Get Found pages (`one-time-services`, `get-found-package`, `get-found-plus`, `get-found-listing-reviews`, `google-business-profile-fix`, `map-pack-push`, `custom-5-page-website`, `one-page-website`, `take-back-your-website`, `review-reply-catch-up`, `sample-report`, `sample-seo-report.pdf`) | ~12 | Remove | website ones to `/pricing.html#website`, the rest to `/pricing.html` |
| `solution-marketing`, `solution-pos`, `solution-memberships` | 3 | Remove | `/solution-crm.html` |
| `answers-marketing` | 1 | Remove | `/answers-crm.html` |
| `ai-receptionist-for-*` | 57 | Keep as CRM feature pages; price is Signature $99 / $199 | |
| `*-answering-service-cost`, `answering-service-for-*` | 47 | Keep; the answer is the AI receptionist inside Signature | |
| `automation-for-*`, `review-software-for-*`, `online-booking-for-*` | 33 | Keep as CRM feature pages | |
| `solution-ai-phone`, `solution-reviews`, `solution-booking`, `solution-payments`, `solution-automation` | 5 | Keep, rewrite as Signature features | |
| receptionist vs pages (`ai-receptionist-vs-answering-service`, `in-house-vs-ai-receptionist`, `smith-ai-alternative`) | 3 | Keep, re-price | |
| `crm-for-*` | 60 | Keep, rewrite CTAs and prices | |
| `*-website-cost` | 57 | Keep, reprice to $499, drop page counts | |
| `websites-seo-for-*` | 57 | Keep slug; website pages. May say "built so Google can read it"; no ongoing SEO service | |
| `for-*` industry pages, `industry-*` | 66 | Keep, rewrite to CRM + website | |
| `how-do-*`, `why-*`, `is-a-crm-worth-it*`, other articles | ~200 | Keep; their "the fix" bridge points at Signature or the website | |
| remaining vs/alternative pages (Jobber, Housecall Pro, ServiceTitan, GoHighLevel, Thryv, Podium, Birdeye, Weave, Vagaro, Mindbody, Clio, all-in-one) | 12 | Keep, re-price against $99 / $199 | |
| `pricing.html`, `index.html`, `solution-crm.html`, `solution-websites-seo.html`, `why-us.html`, `contact.html` (becomes the Try the CRM form), `alternatives.html` | | Rewrite | |
| `demo/**`, `websites/**`, `preview/**` | | Untouched | |

Every removed URL gets a 301. Family rules use `RedirectMatch 301 ^/ai-receptionist-for-(.+)\.html$ /crm-for-$1.html` style; any slug whose target doesn't exist gets an explicit rule (the builder generates the list and checks each target exists on disk).

Shared pieces rewritten everywhere: the nav (Solutions menu down to the Signature CRM features and Websites; Pricing; the main button becomes "Try the CRM" to the request form; no self-serve demo login link), the footer, homepage service drawer, the comparison table ("hire it out" $6,215 vs $899) re-based on $99, FAQ answers, JSON-LD `Offer`/`Service` price data, `llms.txt`, `sitemap.xml` (via `build_sitemap.py`), the "telecom billed at pass-through cost" line (replaced by the $50/mo phone line), and the CRM-only-on-Signature/Platinum contradiction.

## Renders

**Real estate (existing, 9 screens).** Source: `G:\My Drive\Taylor OS\Projects\Top Shelf\renders\sarah-laos-crm\screens-html\` (`build_crm.py`, `crm.css`, `img/`): today, listings, listing-edit, contacts, contact, pipeline, deal, mobile-today, mobile-contact. Re-render all 9 with the agent renamed to **Elena Marsh** (the fictional agent already shown on `industry-real-estate.html` via `websites/elena-marsh-realty/`) and a made-up brokerage replacing every "Sarah Laos" and "Ready Real Estate" string (and her photo if present); listing photos and screen content stay. The website half of each pair is a screenshot of a renamed local copy of the realtor sample site's matching page (Elena Marsh, no real brokerage), saved as a new image only; nothing under `demo/` or `websites/` is edited or published. These 9 also carry the "Sample screens" label. Fold in the round-1 realtor-review blockers only if cheap (Texas MLS status words); otherwise leave as is. Placement: `industry-real-estate.html` and `solution-crm.html`, each CRM screen beside the matching sample-website page (listing in the CRM next to the same listing on the website) to show "edit it in the CRM, it shows on your website".

**New sample screens.** Industries on the site with no Top Shelf CRM yet: Restaurants & Bars, Medical & Dental, Law Firms, Retail & Local, Salon & Spa. (Have real CRMs, not rebuilt: home services, car lots and auto shops, auto detailing, gyms, real estate.) For each: about 6 screens built the same way as the realtor set (HTML + shared CSS, rendered to PNG at desktop 1440 and phone 390): today, customers, one customer, pipeline or bookings, a text thread, a phone view, filled with plausible sample data and no real businesses or people. Each screen carries a visible "Sample screens" label (owner: "label them sample screens, we will build them and use sample data"). Placement: the matching `industry-*.html` page and its `for-*` sub-pages where a CRM section exists (Restaurants and Retail have no `for-*` pages, so only the industry page).

**Industries with real CRMs (my call).** Reuse captures we already have, no new captures: home services from `renders/crm-desk-ad-2026-11-19/` (dashboard + job screens per trade), car lots and auto shops from `renders/dealer-program-shots/` (already carry a "Sample data" strip), gyms from `renders/repkin/`. `industry-salon-spa-fitness.html` labels its two sections separately: Salon & Spa = "Sample screens", fitness = the real app.

Render output and sources are filed to Drive `Projects/Top Shelf/renders/<date>-crm-sample-screens/`; the web-ready images go in `assets/img/crm/`.

## Delivery order

1. Site cleanup + repricing + redirects + shared pieces + the Try the CRM form (one push, so no page ever mixes old and new prices). `offer.py` is NOT changed in this push (it drives the live outreach audits and its linter would reject their quotes); instead the repo gets an old-price test (`scripts/tests/`) that fails if any removed price or plan name appears outside `demo/`, `websites/`, `preview/`. The facts file gets the $499 site, the $50 phone line and the Signature feature list before the fact gate runs. The CRM backend's website-lead validation must accept the form without the `gbp` field (verify; change it in top-shelf-crm if it requires it).
2. Renders (second push).
3. Straight after push 1: audit tool (`topshelf-seo-audit` skill: `offer.py` PLANS/amounts incl. removing $499 from `RETIRED_PRICES` and authorizing $50, recommend rules, PDF copy) and the CRM's in-app audit (`top-shelf-crm/app/Services/Audit/OneTimeOffer.php`) recommend Signature or the $499 website only.

## Verification (before each push, and after deploy)

- Internal link checker over every kept page: zero links to missing files.
- Old-price and old-name sweep outside `demo/`, `websites/`, `preview/`: no $299, $899, $2,500, $599, $795, $1,995, $345, $1,250, $1,500, $495, $150, $325, $95, $6,215-based comparisons, "Essentials", "Platinum", "Get Found", "blend". (The builder whitelists legitimate non-price numbers it finds.)
- `sitemap.xml` lists only kept, indexable pages.
- The repo old-price test passes (the offer.py linter passes once step 3 updates it).
- A test submission of the Try the CRM form reaches the CRM backend and the owner alert (use a clearly labelled test lead).
- Desktop and phone screenshots of home, pricing, solution-crm, one industry page, one crm-for page, one website-cost page.
- After deploy: request every removed URL on the live site and confirm 301 to a URL that returns 200.
- Judge gate before handing back each push; fact gate on the pricing/home copy; humanizer pass on new copy.

## Left to the builder

- Exact mapping of generator/spec files to families, and whether to delete removed families' generators or gate them off.
- The made-up brokerage name for Elena Marsh (plausible, clearly not a real DFW brokerage).
- Sample data for the new industry screens.
- Wording of the Signature feature list and the $499 website card within the rules above.
- Whether `websites-seo-for-*` keeps its URL slug (yes by default, to keep search credit) while dropping SEO-service claims.

## Follow-ups outside this design

- Build the per-client AI chat widget in top-shelf-crm (`chat_widget: pending`) so the advertised chatbot can be installed.
- Build the industry CRMs the sample screens depict.
- `feat/dealers-walkthrough` (dealer walkthrough page) is unmerged and separate; it carries no prices (checked). It will need the new nav when it merges.
- Set the overage rule for the $50 phone line (owner: "we can figure that out later").
