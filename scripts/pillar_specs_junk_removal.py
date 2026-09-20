"""Pillar (trade hub) framing for JUNK REMOVAL. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, junk-removal-specific framing prose that makes the pillar non-thin and leads with
the same-day impulse haul and the repeat referral accounts, never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear, and never an invented haul price; no em/en dashes anywhere; "slips away" / "goes cold",
never "leak" as a metaphor. The AI receptionist does scheduling and intake only and gives a ballpark
from the owner's set pricing; it never binds a firm haul price, the crew confirms once they see the
pile.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Junk Removal Companies",
    "title": "Software and Marketing Built for Junk Removal Companies | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for junk removal companies: an AI receptionist that gives a ballpark and books hauls, a CRM that revives photo quotes, and a site that ranks.",
    "answer": "Junk removal runs on same-day impulse. Something has to go now, so the caller books whoever picks up and can come today, not the best crew in town. Top Shelf answers every call while your hands are full of couch, gives a ballpark from your truck-load pricing, follows up on every photo quote, and keeps your accounts coming back.",
    "faq_eyebrow": "junk removal companies ask",
    "sections": [
        {"h2_html": "Where a junk removal company actually <em>loses hauls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Junk removal loses hauls in the most literal hands-full way there is. Someone decides the garage has to be empty by the weekend and calls right then, usually on a weeknight or a weekend, and your crew is on one end of a sleeper sofa, carrying a fridge across a lawn, or driving a loaded truck to the transfer station with no free hand, so the call goes unanswered and the haul books with whoever picked up. Then the quotes go cold. A homeowner texts a photo of the pile, gets a ballpark, means to schedule it, and gets busy, and the slow jobs, an executor settling an estate, a landlord waiting on an eviction, drift until someone checks back in. And the repeat accounts, the realtors and property managers who send cleanout after cleanout, quietly move to another crew the moment you go quiet.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps. An <a href="ai-receptionist-for-junk-removal.html">AI receptionist</a> answers on the first ring day or night, gives a sensible ballpark from the pricing you set, single item, quarter truck, half truck, full truck, gets the address and a photo of the pile, and books the haul or hands the details to the crew. A <a href="crm-for-junk-removal.html">CRM</a> keeps every open photo quote in front of you and follows up on its own, so the homeowner comparing three companies keeps hearing from you while the others go quiet, and it keeps your realtor, property-manager, and mover accounts warm so you stay the crew they call first. It never binds a firm number on a pile it cannot see, the crew confirms that once they look.</p>'},
        {"h2_html": "One system, not a <em>phone full of old texts</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">All of that slips away because it usually lives in a phone full of old texts, and a crew wrestling a couch down a staircase cannot keep up with it. Top Shelf is one connected system instead. The haul the receptionist books lands in the same CRM that follows up on the quote and asks for the review the moment the truck pulls away and the space is finally clear. Your <a href="websites-seo-for-junk-removal.html">website and local SEO</a> feed it with a photo-for-a-quote path, an obvious same-day booking option, and rankings for junk removal near me, and your <a href="marketing-for-junk-removal.html">marketing</a> builds the recent reviews that win the map pack and the repeat referral accounts, realtors, property managers, and movers, that keep a truck busy without buying leads. You keep your own number and your own customer list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and every photo quote. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the receptionist gives a ballpark from your pricing and handles the booking, but it never binds a firm number on a haul it has not seen, your crew confirms that at the pile. A free audit is the place to start, and it shows you where your same-day calls and photo quotes are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a junk removal company?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Can the AI receptionist quote a haul?",
         "It gives a sensible ballpark from the pricing you set, single item, quarter truck, half truck, full truck, so the caller is not left guessing and is more likely to book. It does not bind a firm price on a pile it cannot see. Your crew confirms the final number once they look at the job."),
        ("Do I have to replace the tools I already use?",
         "No. Top Shelf runs on your existing phone number and is built around how a junk removal company already works. It fills the gaps in answering same-day calls, following up on photo quotes, and getting found, and your number and customer list stay yours and leave with you if you ever go."),
    ],
    "service_schema_name": "Business software and marketing for junk removal companies",
    "cta_h2": "See what your junk removal business is <em>missing</em>",
    "cta_sub": "Get a free audit of where your same-day calls and photo quotes are slipping away, whether you work with us or not. No credit card, never a call center.",
}
