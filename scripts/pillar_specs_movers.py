"""Pillar (trade hub) framing for MOVERS. generate_pillars.py owns the mechanics (shell, schema,
the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns ONLY
the unique, mover-specific framing prose that makes the pillar non-thin and leads with the mover's
real world: a move is won or lost on a single date, so the family books whoever answers and can
hold the day, and trust matters because a stranger is carrying everything they own.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear, and never an invented moving price; no em/en dashes anywhere; "slips away" / "goes cold",
never "leak" as a money metaphor. The AI does scheduling and intake only, it never binds a quote.
"""

PILLAR = {
    "h1": "Moving Company Software and Marketing in One Platform",
    "title": "Moving Company Software and Marketing in One Platform | Top Shelf Business Solutions",
    "meta_desc": "Moving company software and marketing in one platform: an AI receptionist that answers every quote call, a CRM that chases every estimate, and a site that ranks.",
    "answer": "A moving job is won or lost on one date. A family with a lease ending Monday calls a few companies and books the first one that answers and can hold the day, so the move goes to whoever picked up, not the best crew. Top Shelf puts the answering, the follow-up, and the marketing in one place for movers.",
    "faq_eyebrow": "movers ask",
    "sections": [
        {"h2_html": "Where a moving company actually <em>loses the move</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A moving company rarely loses on price. It loses in the gap between a family needing a date held and you being free to pick up the phone. Your crew is carrying a couch down three flights or driving to the next stop when the quote call comes in, so it rolls to voicemail, and a family whose lease ends Monday does not leave a message. They book the mover who answered. The estimate you gave on Tuesday goes quiet while they gather two more, and the move lands with whoever checked back in. Each one is a booked weekend you had half-earned and let slip away.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps one at a time. An <a href="ai-receptionist-for-movers.html">AI receptionist</a> answers every quote call day or night, gathers the whole move, where from, where to, how big, and what day, and books the estimate instead of losing it to voicemail. A <a href="crm-for-movers.html">CRM</a> keeps every open estimate in front of you and follows up on its own while the family compares bids. And because a stranger is deciding who to trust with everything they own, your <a href="websites-seo-for-movers.html">website and local SEO</a> put your reviews and your license front and center the moment someone searches for a mover near them.</p>'},
        {"h2_html": "One system, not a <em>glovebox full of apps</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason those jobs slip is that answering, follow-up, booking, and marketing usually live in four different places, and a mover running crews all day has no time to stitch them together between loads. Top Shelf is one connected system instead. The quote call the receptionist books lands in the same CRM that sends the check-in two days later and the review request the moment the move is marked done. Your <a href="marketing-for-movers.html">marketing</a> keeps your Google profile ranking and your reviews growing, so the next family searching finds you first. You keep your own number and your own customer list, and both leave with you if you ever go.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and estimate. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist gathers the move and hands the price to you rather than binding a quote it cannot honor. A free audit is the place to start, and it shows you exactly where your calls, estimates, and moves are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a moving company?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Will the AI receptionist quote a move on the phone?",
         "No, and that is deliberate. It answers every call, asks what you would ask, where from, where to, how big, stairs or an elevator, and the date, and books the in-home or virtual estimate. It captures the move and hands the price to you, so a real quote always comes from you after you know the job."),
        ("Do I have to replace the tools I already use?",
         "No. Top Shelf runs on your existing phone number and is built around how a moving company already works. It fills the gaps in answering quote calls, following up on estimates, and getting found, and your number and customer list stay yours and leave with you if you ever go."),
    ],
    "service_schema_name": "Business software and marketing for movers",
    "cta_h2": "See which moves your company is <em>letting slip away</em>",
    "cta_sub": "Get a free audit of where your quote calls, estimates, and booked weekends are slipping away, whether you work with us or not. No credit card, never a call center.",
}
