# Industry pairs, site update, and three Top Shelf design concepts (design)

Date: 2026-11-26 · Owner: Taylor · Branch: `feat/crm-website-focus` (worktree `C:\Users\taylo\top-shelf-website-focus`). Nothing merges to `main` (which deploys) without Taylor's go.
Builds on: `2026-11-21-crm-website-focus-design.md` (offer, prices, removed services) and the approved industry CRM screens (`scratchpad\industry-v2\`, mirrored to Drive `Projects/Top Shelf/renders/2026-11-26-industry-crm-screens/`).

## Intent (owner's words, verbatim where quoted)
- "We need the CRM and the websites we sell to go hand in hand when we have the cards on the website. It needs to show examples of the websites we can build them and the CRM that we can have them use for their business." The cards are the homepage industry cards.
- Pairing: "Option 1, same business same look": each industry is ONE fictional business whose sample website and CRM share the name and the look. A guest books on the website and the booking lands in that same business's CRM.
- Pop-up: replace "Find your gap" with option A, "See your business": pick your industry, see its website and CRM side by side, then Try the CRM.
- CRM page: "go over all the benefits of using our CRM and website, such as the payment processing, sending the customers estimates/invoices, having the customer pay from their phone, automatically asking for reviews ... look at other CRM websites ... like service titan, housecall pro ... what customers are really looking for and make sure we answer all their questions and show how easy this is to use and build value for them."
- "rework the website we have now with those sections and main page with all the information and just update it." The current site keeps its fonts and colors (black and gold, DM Serif Display + DM Sans).
- "create a few visually stunning websites for TOP SHELF with all the same information so I can compare and take what I like from each. All the renders, CRM, and website products and information will be the same its just giving me different ideas." The 3 new concepts "can do any color and font just keep the Logo Initials and style".
- Each concept: "Homepage Plus a CRM page and a Website page or the CRM and websites can be hand in hand as an industries page and then each industry branches off into a CRM and website page for that industry but there should also be a general CRM and General Website page."
- "have a few customer agents go over the websites and let me know what they think of them, also 1 of the new website designs should incorporate what the customer agent recommends."
- Missing industries: build sample websites for car lots, gyms/fitness and auto detailing; add a vet-clinic CRM set (Wellspring Animal Hospital already has a website).

## Goals
1. 12 industry pairs, each one fictional business with a sample website and 6 CRM screens in one shared look.
2. The current site updated: homepage industry cards show each pair; the new pop-up; a CRM page and a Websites page that sell the benefits and answer buyers' questions; the CRM by Industry page and industry-page strips re-rendered with the paired businesses.
3. Three new full design concepts of the Top Shelf site, same content and assets, different visual directions.
4. Customer-agent reviews of the updated site and the 3 concepts, reported to Taylor, and a 4th concept built from their recommendations.

## Non-goals
- No change to prices, the offer, or what the CRM does (the facts file rules; new benefits found in the code need Taylor's OK before they are advertised).
- No change to the homepage hero's emerald CRM screens (they stand for the CRM in general, not one industry). Flagged for Taylor, not changed.
- Concepts are not deployed as the live site; Taylor picks ideas from them later.
- No new industries beyond the 12 below (property management, mortgage, commercial real estate and non-dental medical stay without their own pair until Taylor decides).

## Anti-goals (a failure even if it "works")
- A CRM screen showing a different business name, city or look than its paired website.
- Any claim, stat, price or feature not in the facts file; invented testimonials or "trusted by" numbers.
- Real business or person names; sample screens or sites without a "Sample" label.
- Old offer leaking back (SEO services, audits, marketing, memberships, "blend").
- Concepts that differ in information or products (they must differ only in design).

## The 12 pairs (business name, city and brand come from the website; the CRM follows)
| Industry | Website (existing unless noted) | CRM set (approved screens, re-skinned) | Notes |
|---|---|---|---|
| Home services | Everline Home Services (navy + amber) | home-services | CRM moves from emerald to Everline's navy/amber |
| Car lots | NEW site | car-lots | site built to the CRM's lot (Bramlett Motor Co., Garland) unless Taylor prefers a new name |
| Auto repair | Apex Auto Werks (near-black + electric red) | auto-repair | ROs adjusted to fit a European-focused shop |
| Auto detailing | NEW site | auto-detailing | site built to Kestrel Lane Detail Co. |
| Real estate | Elena Marsh Real Estate | real-estate | already the same business |
| Gyms & fitness | NEW site | fitness | site built to Larkspur Strength Club |
| Salon & spa | Lumen Wellness (sand/blush + plum + gold) | salon-spa | |
| Restaurants & bars | Ember & Oak (charcoal + ember gold) | restaurants | |
| Medical & dental | Brightwater Dental (aqua/teal) | medical-dental | |
| Law firms | Halcourt & Vale (ink/forest + brass) | legal | the website's practice areas change to match the CRM's (family law, criminal defense, estate planning) |
| Retail & local | Field & Fawn (cream + terracotta/sage) | retail | |
| Vet clinic | Wellspring Animal Hospital (forest + coral) | NEW vet set | full brief → build → review like the other 11 |
Linewright Mobile Dent stays as an extra auto sample on the Websites page, not on the cards.

Rule for "same look": each CRM theme is regenerated from its website's brand colors (`make_themes.py`), keeping WCAG AA. Light or dark follows the website. The customer-facing CRM screens use the website's own header, logo and type, so they read as pages from that website.

## Approaches
**Pairing (decided by Taylor):** (1) same business, same look (chosen); (2) same name, keep the approved CRM themes; (3) leave separate. Option 1 is the only one where a visitor sees one business end to end.
**Concept structure (decided by Taylor):** each concept has Home, CRM (general), Websites (general), Industries hub, and per industry a CRM page and a Website page (12 × 2).
**How the concepts are built (builder's call, stated):** one shared content source (a JSON/YAML of every heading, paragraph, benefit, FAQ, price, industry pair and image path) plus a small generator per concept that renders its page templates. That keeps "all the same information" true by construction and makes 28 pages per concept cheap. The alternative, hand-writing each page, drifts and was rejected.
**Where concepts live (builder's call, stated):** in the worktree under `preview/concepts-2026-11/<concept>/` with `noindex` on every page and a robots `Disallow` for that folder, so they can be reviewed in a browser and on a phone after a merge without being indexed. Previews for Taylor go out as private artifact links before any merge.

## Work order
1. **Research** (running): competitor teardown, buyer wants and fears, our real feature inventory → the benefit list and buyer Q&A for the CRM and Websites pages. Benefits found in the code but not in the facts file are listed for Taylor to approve; they are not advertised until he does.
2. **Pairs:** vet CRM set (industry agent brief → build → review → fix); 3 new sample websites in the `websites/` program style (BRIEF, assets, 5 pages, Judge); re-skin and rename the 11 approved CRM sets to their websites; re-render; Taylor reviews the pairs board before they go on the site.
3. **Update the current site:** homepage industry cards (a website thumbnail + a CRM screen per industry, linking to the industry page and the website), the "See your business" pop-up (replaces `assets/gap-quiz.js` site-wide), the CRM page (`solution-crm.html`) and the Websites page (`solution-websites-seo.html`) rewritten from the research, and the CRM by Industry page and industry strips updated to the paired screens.
4. **Concepts A, B, C:** three distinct directions drawn from the competitor research (e.g. a bright, product-led SaaS look; a cinematic dark showcase; an editorial, trade-warm look), each built from the shared content.
5. **Customer agents:** 5 prospect personas (HVAC/home-services owner, auto shop owner, salon owner, dental office manager, restaurant GM) each review the updated site and concepts A-C on desktop and phone, as buyers, and write ranked findings. Report the consolidated findings to Taylor.
6. **Concept D:** built from the customer agents' recommendations, with a short note of which recommendations it applies.
7. **Gates:** humanizer on all new public copy; fact gate on every page with Top Shelf claims; Judge before each hand-back; Taylor reviews the pairs board (after step 2) and the concepts (after step 6).

## Constraints
- Facts: `C:\Users\taylo\Agentic-OS\vault\platter\facts\top-shelf-business-solutions.json`. Prices: Signature $99/mo 1-10 users, $199 11-25, 26+ call; $50/mo per phone line; $499 one-time website; no setup fee, month to month; custom layout or custom industry CRM at the same price.
- Main CTA "Try the CRM" → contact form; secondary "Call or text (469) 833-3033". Sample sites keep the program convention phone 123-456-7890.
- No em dashes in new copy; no invented stats; "Sample" labels on all sample screens and sites; fictional names checked against real businesses.
- Concepts keep the Top Shelf logo initials and mark style; colors and fonts are free. The updated current site keeps black and gold with DM Serif Display + DM Sans.

## Decisions made while Taylor was away (2026-11-27; he said "keep going till its done and only stop if you absolutely need something from me"). Each is the conservative choice; listed for his morning review.
1. **Current site keeps its 9 industry pages.** The homepage gets 12 industry cards, one per pair, each linking to the existing page (car lots, auto repair and detailing → `industry-auto.html` anchors; salon & spa and fitness → `industry-salon-spa-fitness.html` anchors; vet → `industry-custom.html`, which already features Wellspring). The pop-up picker lists the 12 pairs. No new URLs on the current site. Each concept gets 12 industry pages of its own.
2. **"Books on the website, lands in the CRM" is shown, not wired.** The sample website and CRM screens carry matching sample data; the sample sites stay static.
3. **Other fictional businesses in the current industry-page stories stay as they are** on the current site (renaming every story is large and their outcome claims need their own fact check). The concepts use only the pair businesses and no outcome stories.
4. **All CRM visuals are labeled sample screens.** No "real app" labels anywhere.
5. **Order:** pairs first (re-skin, vet set, 3 new websites), then the current-site update and the concepts on the branch, then customer agents, then concept D. Taylor reviews everything together; nothing merges to main.
6. **`for-*` sub-pages are not touched.**
7. **Claims (from the research, `2026-11-26-crm-page-research.md`):** new copy uses only facts-file items. Code-only features (good/better/best estimates, typed-name approval, automatic estimate follow-ups and overdue reminders, tips, Google Pay, deposits, techs-only-see-their-jobs, CSV import, and the rest of the (b) list) are listed for Taylor's approval and not advertised yet. Review requests are described as "one tap after every job", because automatic sending isn't built; the AI website chatbot stays advertised per Taylor's 2026-11-21 decision ("Put on the site"), even though `chat_widget` is still pending. FAQ answers we can't ground (card rate, payout timing, setup time, support hours, data export, overage rate) say "we go over it on your demo call" rather than inventing a number.
8. **Screen sources are now in the repo** at `renders-src/industry-crm/` (kit, themes generator, briefs, reviews, screens, page generator).

## Left to the builder
- Exact palettes per concept; motion level; which competitor ideas each concept borrows (cited in the concept's notes).
- Names and stories for the 3 new sample websites, following the program BRIEF format, matched to the existing CRM businesses.
- Persona details for the customer agents.
