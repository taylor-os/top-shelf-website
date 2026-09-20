"""Pillar (trade hub) framing for AUTO BODY SHOPS / collision repair. generate_pillars.py owns the
mechanics (shell, schema, the auto-discovered money + colony link blocks, keyword placement,
wiring). This file owns ONLY the unique, collision-specific framing prose that makes the pillar
non-thin and leads with the body shop's real world (the after-accident driver, the insurance
claim, the estimate-to-scheduled-repair gap), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "slips away" / "goes cold" / "find the gap", never "leak" as a
money metaphor. The AI does intake and scheduling only, it never decides an insurance claim or
quotes a repair.
"""

PILLAR = {
    "h1": "Auto Body Shop Software and Marketing, All in One Place",
    "title": "Auto Body Shop Software and Marketing, All in One Place | Top Shelf Business Solutions",
    "meta_desc": "Auto body shop software and marketing in one platform: an AI receptionist that captures the claim, a CRM that chases every estimate, reviews, and a site that ranks.",
    "answer": "Collision work starts with a shaken driver who just had a wreck, wants a shop that handles the insurance claim, and books whoever answers first. Top Shelf puts the fix in one place for auto body shops: an AI receptionist that captures the claim, a CRM that chases every estimate, reviews, and a site built to rank.",
    "faq_eyebrow": "body shop owners ask",
    "sections": [
        {"h2_html": "Where an auto body shop actually <em>loses jobs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An auto body shop rarely loses a car on price. It loses it in the gap between a driver needing help and someone being free to pick up. Nobody plans a collision, so the calls come at the worst moments, while your crew is masking for paint, on the frame machine, or matching color under the lights. A driver who just had a wreck is shaken, calling down a list, and will not leave a voicemail. They book the first shop that answers, and the after-accident job you never heard ring goes to someone else.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The rest slips away a little slower. An estimate you wrote goes quiet while the driver waits on the insurance claim, and nobody circles back before the car books somewhere else. A driver searching for collision repair near me right after a wreck never finds you because the site does not rank. Top Shelf is built to close those gaps one at a time. An <a href="ai-receptionist-for-auto-body-shops.html">AI receptionist</a> answers every call and captures the insurer, claim number, and vehicle before the caller moves on. A <a href="crm-for-auto-body-shops.html">CRM</a> keeps every open estimate in front of you and follows up while the claim is still in motion. And a <a href="websites-seo-for-auto-body-shops.html">website built to rank</a> puts you in front of the driver at the exact moment they search after an accident.</p>'},
        {"h2_html": "One system, not a <em>shop full of logins</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason so much of this slips is that it usually lives in five disconnected places, and a body shop owner does not have time to run five tools between cars in the booth. Top Shelf is one connected system instead. The call the receptionist captures lands in the same CRM that follows up while the claim moves and asks for the review the day the car is picked up. Your <a href="marketing-for-auto-body-shops.html">marketing</a> and local SEO feed the whole thing by getting you into the map pack where drivers look right after a wreck. You keep your own number and your own customer list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and estimate. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist does intake and scheduling only, handing the insurance decision and the actual estimate straight to you. A free audit is the place to start, and it shows you exactly where your calls, estimates, and cars are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for an auto body shop?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom five page site is $1,500. There is no setup fee."),
        ("Will the AI receptionist handle an after-accident call?",
         "It answers on the first ring, day or night, stays calm with a shaken driver, and gathers the insurer, claim number, and vehicle details before booking the estimate or flagging it to your phone. It does intake and scheduling only. It never decides an insurance claim or quotes the repair, and it is upfront that it is an assistant, not a person."),
        ("Do I keep my phone number and customer list?",
         "Yes. Top Shelf runs on your existing number and is built around how a body shop already works. Your number and your customer list stay yours and leave with you if you ever go, so nothing you have built gets locked inside our tools."),
    ],
    "service_schema_name": "Business software and marketing for auto body shops",
    "cta_h2": "See what your body shop is <em>missing</em>",
    "cta_sub": "Get a free audit of where after-accident calls, estimates, and cars are slipping away, whether you work with us or not. No credit card, never a call center.",
}
