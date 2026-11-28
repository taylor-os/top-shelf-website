# Judge brief: Top Shelf site update + design concepts (2026-11-27)

Written by the Manager, not by any builder. Grade against what Taylor (the owner) wants.

## What Taylor asked for (verbatim)

1. "lets redo the find your gap popup and brainstorm what else we could do as a pop up to get customers interested give me some options. Also We need the CRM and the websites we sell to go hand in hand when we have the cards on the website. It needs to show examples of the websites we can build them and the CRM that we can have them use for their business."
2. "The industry cards on the homepage also let me know which industries are missing and Ill see if we should make a new industry for it or not, go with option A and also for the CRM main page make sure you go over all the benefits of using our CRM and website, such as the payment processing, sending the customers estimates/invoices, having the customer pay from their phone, automatically asking for reviews, just gather an extensive list of the benifits the CRM offers, feel free to look at other CRM websites to get ideas of what to accentuate like service titan, housecall pro ect... do a deep dive is what customers are really looking for and make sure we answer all their questions and show how easy this is to use and build value for them"
3. "Option 1, same business same look, and I want you to rework the website we have now with those sections and main page with all the information and just update it. Then I want you to gain inspiration from other CRM websites and create a few visually stunning websites for TOP SHELF with all the same information so I can compare and take what I like from each. All the renders, CRM, and website products and information will be the same its just giving me different ideas for the website. Also have a few customer agents go over the websites and let me know what they think of them, also 1 of the new website designs should incorporate what the customer agent recommends so I can see the recommendation for that one as a sample to choose from."
4. Answers: build the 3 missing websites (car lots, gyms, detailing); add vet CRM screens; "the original that is being updated will stay the same font and color scheme the new 3 can do any color and font just keep the Logo Initials and style"; each concept has "Homepage Plus a CRM page and a Website page or the CRM and websites can be hand in hand as an industries page and then each industry branches off into a CRM and website page for that industry but there should also be a general CRM and General Website page that is built for each concept".

"Option 1, same business same look" = each industry is ONE sample business whose website and CRM screens share one look.

## Hard rules (fail if broken)
- No invented stats, testimonials, reviews or claims. Prices/claims only from `C:\Users\taylo\Agentic-OS\vault\platter\facts\top-shelf-business-solutions.json` ($99/mo 1-10 users, $199/mo 11-25, $50/mo phone line, $499 website, no contract, no setup fee).
- Review requests may be described as going out on their own when a job is finalized (owner-confirmed 2026-11-28), or by hand with one tap.
- No em dashes in new copy. Copy reads human (humanizer standard).
- Every sample screen and sample site is labelled as a sample. No real names; never "Sarah Laos" or "Ready Real Estate".
- Current site keeps black and gold + DM Serif Display / DM Sans. Concepts may use any palette/font but keep the Top Shelf logo initials and style.
- Concepts live under `preview/concepts-2026-11/<id>/`, carry `noindex`, and `robots.txt` disallows them.
- Nothing pushed to main or deployed.

## Where things are (repo `C:\Users\taylo\top-shelf-website-focus`, branch `feat/crm-website-focus`)
- Design doc: `docs/superpowers/specs/2026-11-26-industry-pairs-and-site-concepts-design.md`; research: `docs/superpowers/specs/2026-11-26-crm-page-research.md`.
- Current site: `index.html` (#industries cards), `solution-crm.html`, `solution-websites-seo.html`, `crm-by-industry.html`, `pricing.html`, pop-up `assets/see-your-business.js`.
- Concepts: `preview/concepts-2026-11/{a,b,c}/` (index, crm, websites, industries, industries/<slug>-crm.html and -website.html). Concept D (customer-agent recommendations) is judged separately later.
- Pairs: `renders-src/industry-crm/pairs.json`; sample sites under `websites/`.
- Tests: `python -m pytest scripts/tests -q` (expect all pass).
