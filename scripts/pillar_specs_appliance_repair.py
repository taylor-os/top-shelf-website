"""Pillar (trade hub) framing for APPLIANCE REPAIR. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, appliance-repair-specific framing prose that makes the pillar non-thin and leads
with the appliance-repair world, never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "slips away" / "goes cold", never "leak" as a money metaphor (a
literal washer or dishwasher water leak is the only allowed use). The AI receptionist does
scheduling and intake only, it never diagnoses the appliance or quotes the repair.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Appliance Repair Companies",
    "title": "Software and Marketing Built for Appliance Repair Companies | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for appliance repair companies: an AI receptionist that captures the brand and model, a CRM that revives past homes, and a site that ranks.",
    "answer": "Appliance repair is a same-day trade. When a fridge quits and the food is warming, the homeowner calls whoever answers and can come today, not the best shop in town. Top Shelf puts the fix in one place: an AI receptionist that captures the brand and model, a CRM that revives past homes, and a site that ranks.",
    "faq_eyebrow": "appliance repair companies ask",
    "sections": [
        {"h2_html": "Where an appliance repair business actually <em>loses jobs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An appliance repair business rarely loses a job on price. It loses it in the minutes between a homeowner watching their food warm up and you being free to pick up the phone. You are on a kitchen floor with a fridge pulled out, hands deep in a washer, or driving to the next call when it rings, so the same-day emergency rolls to voicemail and the caller moves down the list until someone can come today. And the call you miss costs you twice, because the brand and model you would have written down is what turns the first visit into the fix instead of a diagnose-today, order-the-part, come-back-next-week trip. A repair-or-replace quote on a control board goes quiet while the homeowner thinks it over, and a family whose dryer you fixed two years ago calls a stranger when the fridge finally goes.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf is built to close those gaps one at a time. An <a href="ai-receptionist-for-appliance-repair.html">AI receptionist</a> answers every call day or night, captures the brand, model, and symptom, explains your diagnostic or trip fee, and books the same-day visit so it never rolls to voicemail. A <a href="crm-for-appliance-repair.html">CRM</a> keeps every parts-on-order job and repair-or-replace quote in front of you and follows up on its own, then reaches back into every home you have already been in as its other appliances age. The intake gets handled while your hands are still in a machine, and the follow-up stops depending on whether you happen to remember it that night.</p>'},
        {"h2_html": "One system, not a <em>drawer full of apps</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason all of that slips away is that it usually lives in five different tools, and a tech with a panel off does not have time to run five apps between service calls. Top Shelf is one connected system instead. The call the receptionist books lands in the same CRM that fires the reminder and the review request the moment the repair is marked done. Your <a href="websites-seo-for-appliance-repair.html">website and local SEO</a> feed it by getting you into the map pack where a warm-fridge search actually starts and naming the brands you service so the homeowner knows they are in the right place, and your <a href="marketing-for-appliance-repair.html">marketing</a> keeps a steady flow of reviews and repeat work coming in all year, because appliances break every day, not in two seasons. You keep your own number and your own customer list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and every parts-on-order job. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the receptionist handles scheduling and intake only, it never diagnoses the appliance or quotes the repair, that stays with your tech on the visit. A free audit is the place to start, and it shows you where your same-day calls and quotes are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for an appliance repair company?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Will the AI receptionist handle a same-day breakdown?",
         "It answers on the first ring, gets the brand, model, and symptom, explains your diagnostic or trip fee, and books the same-day visit, or flags an urgent one straight to your phone. It is upfront that it is an assistant, not a person, and it never diagnoses the appliance or quotes the repair. That stays with your tech on the visit."),
        ("Do I have to replace the tools I already use?",
         "No. Top Shelf runs on your existing phone number and is built around how an appliance repair shop already works. It fills the gaps in answering calls, following up on parts and quotes, and getting found, and your number and customer list stay yours and leave with you if you ever go."),
    ],
    "service_schema_name": "Business software and marketing for appliance repair companies",
    "cta_h2": "See what your appliance repair business is <em>missing</em>",
    "cta_sub": "Get a free audit of where your same-day calls, quotes, and repeat customers are slipping away, whether you work with us or not. No credit card, never a call center.",
}
