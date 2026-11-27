# Concept D: the buyer-led sample

Concept D is the version built from what the five customer agents recommended (`docs/superpowers/specs/2026-11-27-customer-agent-findings.md`). It starts from Concept A, which three of the five ranked first, and adds what they asked to take from C, B and the current site. Same content, same 12 sample businesses, same renders. Generator: `scripts/concepts/d/build.py` (it reuses A's generator and overrides only what changed).

Look: warm white, deep teal, Figtree, with the Top Shelf mark on its ink tile.

| Change | Asked for by | Taken from |
|---|---|---|
| The DFW number in a bar on every page, with Call and Text links | auto, dental, HVAC, salon, restaurant | C |
| A Call / Text / Try the CRM bar fixed to the bottom of the phone screen, with nothing floating over it | HVAC (the current pop-up tab covers its Call button) | Current site |
| The industry picker moves up to right under the hero, so a restaurant or salon visitor picks their business before seeing an HVAC dashboard | restaurant, dental, HVAC | Current site's "See your business" idea |
| One job start to finish (2 AM call, board, estimate, paid, owner's morning), each screen big and tap to open full size | HVAC, auto | B |
| Owner quotes back on the homepage and CRM page, and on an industry page only when the trade matches (home services, car lots). No garage-door quotes on restaurant, salon or dental pages | all five | Current site (verbatim, live copy) |
| Open answers, no tapping. The answers that only pointed to the demo call are listed once, under "Ask us these on the call", instead of repeating the dodge 7 times | all five | C |
| "Your customer data is yours: every name, number and job, and you can take it with you if you ever leave" next to pricing | auto, restaurant, dental | Current pricing page (verbatim) |
| Each industry CRM page leads with the screen its buyer said sells it, full width (estimate approval for auto, events board for restaurants, owner's day with booth rent for salons, the lunch-hour call for dental) | auto, restaurant, salon, dental | B |
| Phone screens one per row on a phone, every screen opens full size | all five | B |
| HIPAA and BAA in a heading on the dental page, without "your practice stays compliant" | dental | Current dental page (verbatim sentences); Taylor approved this wording 2026-11-27 |
| "Using Toast or OpenTable?" / Dentrix / Shopmonkey / Housecall Pro / Vagaro box on those industry pages | restaurant, dental, auto, HVAC, salon | New. It names the software as a question only and makes no claim about how it connects |
| The price on every industry CRM and website page | salon, auto (C had none on those pages) | A |
| "Websites $499, one time", never "from $499" | salon | Pricing page |
| "Rather text? Text (469) 833-3033" under How it works | salon | |
| How it works step 3 is "Send your first text", not "Send your first invoice", and its body ends "then send your first text from the app" instead of "text your first estimate or invoice" (a dental office or restaurant doesn't invoice, and the salon reviewer said "I don't send invoices") | restaurant, dental, salon | content.json, with the invoice wording swapped for the text wording |
| Salon "What owners get" says in words what the screens show: deposit and 48-hour rule on the booking page, deposit off the ticket and the tip split at checkout, booking the next visit at checkout, the last formula and photos. Wording comes from the salon screen captions only | salon (top ask) | captions.json |
| On every industry page, the HIPAA box and the "Using X?" box sit right under the intro, before the screens, so a phone visitor sees them on the second screen | dental, restaurant | |
| "HIPAA setup, BAA included" also shows on the Medical & Dental panel of the home-page picker | dental | Same approved HIPAA wording |
| On a phone the industry picker fades at the right edge and its label says "Swipe for more", so the tabs past the first few aren't missed | Judge review | |
| The footer says only the sample screens and sample websites are made up, and on pages with owner quotes adds that the quotes are real, from businesses that use Top Shelf | Judge review | |
| "Who sets it up?" moves into "Ask us these on the call", whose intro now reads "We answer these on the call, before you sign up." | all five | |

## What D left out on purpose

| Recommendation | Why D skips it |
|---|---|
| Industry-specific story beats from the current site (each industry told as its own start-to-finish job) | Only home services is told start to finish. The current industry pages' stories mix several made-up companies per page and carry trades quotes, which the findings flag for a cleanup. Writing new per-industry stories would be new copy beyond the captions. Each industry page instead leads with the screen its buyer picked, with the captions underneath |
| Booth rent, card on file and who counts as a user (salon) | Booth rent shows in the owner's screen but D doesn't say it in words until "who counts as a user" is answered (booth renters, front desk). "Card on file" isn't in the salon captions |
| A named person who calls back, support hours, call-back time | Not in the facts file. Listed under "What only Taylor can answer" |
| A written price lock next to the $99 (HVAC) | Not in the facts file |
| Maintenance agreements (HVAC) | Not in the facts file, content.json or captions.json |
| A restaurant-sized cost example ($199 + $50 for 14 logins) | Depends on who counts as a user, which isn't answered yet |
| Restaurant website answers: who updates the menu, events form into the board, hosting after the $499 | Not in the facts file |
| What the AI receptionist will and won't say, and Spanish (auto) | Not in the facts file. Spanish stays in "Ask us these on the call" |
| A "first 30 days" timeline (dental) | Setup time and who does it are unanswered owner questions, so there is nothing true to put on the timeline yet |
| A yes / not yet feature checklist: parts ordering, labor guide, VIN decode (auto) | None of these are in the facts file |
| Making the sample a general repair shop instead of a European/BMW shop (auto) | The sample business and its screens are shared by every version, so changing it is a separate render job |
| Renaming "Try the CRM" (restaurant, salon) | It's the owner-set button name in the facts file |
| Saying whether booking confirmations go out automatically or by hand (dental) | A "What only Taylor can answer" question. The dental lead screen shows the confirmation text as "Sent automatically", which is allowed because it's a confirmation, not a review request, but D can't say more until Taylor confirms how confirmations go out |

## What D could not do without Taylor

The top request from all five was real numbers in place of "we go over that on your demo call". D lists those questions honestly but cannot answer them; the answers are not in the facts file. See "What only Taylor can answer" in the findings doc: card rate and payouts, setup time and who does it, what the $50 line covers, support hours, export format, a price lock, integrations, Spanish, who counts as a user, what the AI receptionist will say, and a named person who calls back. Each one answered turns a line in that box into a plain answer on every version.
