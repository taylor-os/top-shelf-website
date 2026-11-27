# Customer-agent findings (2026-11-27)

Five buyer personas reviewed the updated current site and concepts A, B and C, phone first, then desktop. Full reviews: `customer-reviews/<id>.md`.

## Rankings

| Persona | 1st | 2nd | 3rd | 4th | Would tap "Try the CRM" |
|---|---|---|---|---|---|
| Luis, auto repair shop (`auto-shop-owner`) | A | C | B | Current | Yes, on A (would call first about card rate and leaving Shopmonkey) |
| Karen, dental office manager (`dental-manager`) | A | Current | C | B | Maybe on Current; yes on A once HIPAA/BAA and practice software are answered |
| Dwayne, HVAC owner (`hvac-owner`) | A | B | Current | C | Yes, on A |
| Andre, restaurant GM (`restaurant-gm`) | C | Current | B | A | Maybe, leaning yes on C, after a call about Toast |
| Monique, salon and spa owner (`salon-owner`) | C | A | Current | B | Probably, on C |

A wins on clarity: price and terms on every page, the 3-step "How it works", one tap to your industry. C wins on warmth: it reads local and honest, with open Q&A and the DFW number in the top bar. B has the only phone screens anyone could read. The current site has the only proof (owner quotes) and the sticky Call bar.

## What every persona asked for (5 of 5)

1. **Stop answering with "we go over that on your demo call."** It appears 9 to 12 times in the CRM FAQ. Every dodge reads as "the number is bad." The most-asked: card rate, payout timing, setup time and who does it, what "normal use" on the $50 line covers and the overage price, support hours, data export.
2. **Bring back proof.** None of the concepts has testimonials. The current site's three owner quotes are all trades or auto, so a restaurant, salon or dental page should not show them.
3. **Make the industry screens readable on a phone.** One per row, full width, tap to enlarge (B's approach). A and C put phones two across and they're unreadable.

## Asked by 3 or 4

- **"Switching from ___" for their current software**: Housecall Pro / Jobber / ServiceTitan (HVAC), Shopmonkey / Tekmetric / Mitchell 1 (auto), Vagaro / Square / Booksy (salon), Toast / OpenTable (restaurant, a deal-breaker), Dentrix / Eaglesoft (dental, "will it mess up our schedule").
- **Lead each industry page with the screen that sells it**: the line-by-line estimate approval (auto), the private-events board (restaurant), the owner's day with booth rent (salon). Today it's buried in fifth place at thumbnail size.
- **Say who calls you and how to get help**: a name, DFW, hours, call-back time, and "Text us" next to "We call you".
- **Keep the DFW number visible** (C's top bar) and a **sticky Call / Text bar** on phones that nothing covers.
- **One sample business per industry, everywhere** (the current industry pages mix three made-up companies).

## Persona-specific

- Dental: HIPAA/BAA in a heading, not a badge inside a screenshot; drop "your practice stays compliant", which contradicts the FAQ; fix "No health details anywhere" next to a schedule showing "Crown visit".
- HVAC: a written price lock next to the $99, after a Housecall Pro price hike. Mention maintenance agreements.
- Restaurant: a restaurant-sized cost example ($199 + $50 for 14 logins and one line). Website questions: who updates the menu, events form into the board, hosting after the $499.
- Salon: say deposits, card on file, rebook at checkout, formulas, tip split and booth rent in words, not only in captions. Who counts as a user (booth renters, front desk).
- Auto: say what the AI receptionist will and won't say (will it quote a price?). Spanish.

## Bugs the reviewers found (fixed or flagged)

| Issue | Where | Status |
|---|---|---|
| Ember & Oak sample says 4.9 in the hero and 4.8 lower down | `websites/ember-and-oak/index.html` | Fixed (both 4.9) |
| "See your business" tab sits on the phone Call bar | current site, `assets/see-your-business.js` | Fix with this batch |
| "Who owns my data" answered with "demo call" though the live pricing page answers it | `content.json` FAQ | Fixed: uses the pricing page's own words |
| "What you won't run into" lists "The same price every month" (reads as a negative) | `content.json` anti_trap | Fixed: heading reworded |
| "Websites from $499" while everywhere else says "$499 one time" | concept page titles | Fixed in D; A/B/C titles updated |
| "No health details anywhere" next to "Crown visit" | `captions.json` medical-dental | Fixed: "Texts and reminders never say why a patient is coming in." |
| Pop-up opens on Home Services on the salon page | current industry pages | Flag (older industry pages, outside this branch's scope) |
| Industry pages mix made-up companies (Travis / Marcus at Ridgeline / Ray at Everline; Willow & Sage vs Lumen), say "quotes that go cold" on salon/dental, list vet links on the dental page, carry trades quotes on restaurant/salon/dental | `industry-*.html` (live, pre-existing) | Flag for Taylor: a cleanup pass on the 9 industry pages |
| Concept C's salon and auto CRM pages show no price; B blurs the $99 until it animates; B has no Pricing link | concepts B, C | Noted for comparison; D fixes these |

## What only Taylor can answer (blocks the #1 request)

These are the answers buyers want in writing. Nothing in the facts file covers them, so no version invents them:

1. Card processing rate, and when payouts land.
2. Typical setup time, and who on the Top Shelf side does it.
3. What "normal use" on the $50 phone line includes, and the overage price.
4. Support hours, and whether a person answers.
5. Data export: format and how (the "your data is yours, take it with you" line is answered).
6. Price lock: how long is $99 guaranteed, or how much notice before a change.
7. Integrations: QuickBooks, Toast, OpenTable, Dentrix/Eaglesoft/Open Dental, and importing from Housecall Pro, Jobber, Shopmonkey, Vagaro.
8. Spanish texts and website.
9. Who counts as a user (booth renters, front desk, part-timers).
10. What the AI receptionist will and won't say (does it quote prices?).
11. A named person who calls back, and how fast.

## Concept D

Concept D (`preview/concepts-2026-11/d/`) is the sample that applies these recommendations. Its `NOTES.md` maps each change to the persona who asked for it.
