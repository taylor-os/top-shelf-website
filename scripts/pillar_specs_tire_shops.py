"""Pillar (trade hub) framing for TIRE SHOPS. generate_pillars.py owns the mechanics (shell, schema,
the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns ONLY the
unique, tire-specific framing prose that makes the pillar non-thin and leads with the tire shop's
real world (a firehose of price-and-availability calls, same-day flats, a walk-in and appointment
mix that slams the counter, fleet accounts, rebooking for rotations and the next set, all swinging
with the season), never a template.

Same honesty rules as the money/colony specs: no invented stats, no made-up tire prices (always
generic, "a set of four", "what a set runs"); hedge instead of overpromise; only the real Top Shelf
prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever appear; no em/en dashes anywhere;
"slips away" / "goes cold", never "leak" (a tire "goes flat"). The AI answers stock/price questions
per the shop's own info only, never inventing a price or promising stock it was not given.
"""

PILLAR = {
    "h1": "Tire Shop Software and Marketing, Built for the Rush",
    "title": "Tire Shop Software and Marketing, Built for the Rush | Top Shelf Business Solutions",
    "meta_desc": "Tire shop software and marketing in one platform: an AI receptionist that answers price and stock calls while bays are full, a CRM that rebooks rotations, and SEO.",
    "answer": "A tire shop lives on a firehose of price and stock calls, do you have my size, what does a set run, and they come while the bays are full and the counter is slammed. Top Shelf puts it in one place for tire shops: an AI receptionist that answers with your price and stock, a CRM that rebooks rotations, and a site that ranks.",
    "faq_eyebrow": "tire shop owners ask",
    "sections": [
        {"h2_html": "Where a tire shop actually <em>loses sales</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A tire shop loses sales at the counter and on the phone at the same time. When the phone rings your techs are on the mounting machine, spinning a balancer, or pulling a wheel, and the front counter has a line of walk-ins, so there is often nobody free to pick up. A driver pricing a set of four calls three or four shops in a row and books the first one that answers with a straight price and an open slot, so a single missed call is often a whole set, the alignment, and years of rotations gone to the shop that picked up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The rest goes cold after the sale. The free rotations bundled with a set go unused because nobody reminds the customer, and a car whose tread is wearing to a date you could predict just drifts until it goes flat. Top Shelf closes those gaps. An <a href="ai-receptionist-for-tire-shops.html">AI receptionist</a> answers every call with the sizes, prices, and stock you set and books the mounting or the same-day flat. A <a href="crm-for-tire-shops.html">CRM</a> reminds each customer when a rotation or the next set is due and follows up on every quote. And a <a href="websites-seo-for-tire-shops.html">website built to rank</a> shows your brands and catches the driver searching for tires near them.</p>'},
        {"h2_html": "One system, not a <em>stack of invoices</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The repeat work slips because it lives in a stack of paper invoices and whatever the counter remembers on a busy Saturday. Top Shelf is one connected system instead. The call the receptionist books lands in the same CRM that fires the rotation reminder and asks for the review the day the set goes on. Your <a href="marketing-for-tire-shops.html">marketing</a> keeps your Google profile active and well reviewed and times your visibility to the seasonal waves, so you are already in front of drivers before the first cold snap. You keep your own number and your own customer list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and quote. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist only ever quotes the prices and stock you set, so it never promises a driver something you cannot deliver. A free audit is the place to start, and it shows you exactly where your calls, quotes, and repeat sets are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a tire shop?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom five page site is $1,500. There is no setup fee."),
        ("Can the AI receptionist really quote a price and check stock?",
         "It gives the prices and out the door ranges you set for your common sizes and services, and tells a caller whether a size is one you stock or would order in. For anything that needs your eyes first, it takes the size and the vehicle, books the appointment, and texts you the details. It never invents a price you did not give it."),
        ("Will this bring customers back for rotations and the next set?",
         "That is what the CRM does. It remembers when each customer is due for a rotation, when a set is wearing near the end, and when a fleet account is due, and reaches out on the cadence you choose, so the repeat work comes back instead of drifting to whoever was closest that day."),
    ],
    "service_schema_name": "Business software and marketing for tire shops",
    "cta_h2": "See what your tire shop is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, quotes, and repeat sets are slipping away, whether you work with us or not. No credit card, never a call center.",
}
