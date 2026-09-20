"""Pillar (trade hub) framing for AUTO REPAIR SHOPS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, repair-specific framing prose that makes the pillar non-thin and leads with the
shop's real world (phones ringing while every tech is under a car, the driver deciding in seconds
who to call, the trust problem, service reminders that bring cars back), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "slips away" / "goes cold", never "leak" as a money metaphor
(a literal oil leak would be fine). The AI does intake and scheduling only, it never diagnoses a
car or quotes a repair.
"""

PILLAR = {
    "h1": "Auto Repair Shop Software and Marketing in One System",
    "title": "Auto Repair Shop Software and Marketing in One System | Top Shelf Business Solutions",
    "meta_desc": "Auto repair shop software and marketing, all in one system: an AI receptionist that answers while techs are under a car, plus CRM, reviews, and a site that ranks.",
    "answer": "When a check engine light comes on or a car will not start, the driver decides in seconds who to call, but the phone rings while every tech is under a car. Top Shelf puts it in one place for auto repair shops: an AI receptionist that books the drop off, a CRM that brings cars back for service, and a site that ranks.",
    "faq_eyebrow": "shop owners ask",
    "sections": [
        {"h2_html": "Where a repair shop actually <em>loses work</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An auto repair shop does not lose many cars on price. It loses them in the ten seconds a stranded driver spends deciding who to call, and in the estimates nobody follows up on. When the phone rings your techs are under a car, on a lift, or out on a test drive chasing a noise, and none of them can stop to grab the counter. A driver whose car will not start does not leave a voicemail. They move down the search results until someone answers. That first timer was ready to trust you with a diagnostic today and years of oil changes, brakes, and inspections after it, and the shop that picked up gets all of it.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The slower loss is the repeat work. A brake estimate a driver was thinking over goes quiet, a family whose car you serviced last year is due again and never hears from you, and a state inspection lapses with no reminder. Top Shelf closes those gaps. An <a href="ai-receptionist-for-auto-repair-shops.html">AI receptionist</a> answers while your hands are full, sorts a tow from a routine drop off, and books it. A <a href="crm-for-auto-repair-shops.html">CRM</a> follows up on every open estimate and reminds each customer when the car is due. And a <a href="websites-seo-for-auto-repair-shops.html">website built to rank</a> puts a tap to call in front of the driver searching nearby right now.</p>'},
        {"h2_html": "One system, not a <em>drawer of tickets</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason the repeat work slips is that it lives in a drawer of paper tickets and someone remembering. Top Shelf is one connected system instead. The call the receptionist books lands in the same CRM that fires the service reminder by mileage or months and asks for the review the day the car is picked up. Your <a href="marketing-for-auto-repair-shops.html">marketing</a> and local SEO keep you in the map pack, where a driver deciding whom to trust with an expensive machine leans on your reviews. You keep your own number and your own customer list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and estimate. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist does intake and scheduling only, handing the diagnosis and the price to you and your techs. A free audit is the place to start, and it shows you exactly where your calls, estimates, and repeat cars are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for an auto repair shop?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom five page site is $1,500. There is no setup fee."),
        ("Does the AI receptionist diagnose the car or quote the repair?",
         "No. It handles intake and scheduling only: what the car is doing, whether it is drivable or needs a tow, and getting it onto your calendar with the year, make, and model. Diagnosing the problem and pricing the work stay with you and your techs, where they belong."),
        ("How does this bring past customers back?",
         "The CRM reminds each customer when the car is due, an oil change by mileage or months, a state inspection before it lapses, the interval work when it is time, and follows up on every estimate that went quiet. The car you already serviced is the cheapest next job, and a well timed reminder is usually all it takes."),
    ],
    "service_schema_name": "Business software and marketing for auto repair shops",
    "cta_h2": "See what your shop is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, estimates, and repeat cars are slipping away, whether you work with us or not. No credit card, never a call center.",
}
