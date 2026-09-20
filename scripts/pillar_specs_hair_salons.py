"""Pillar (trade hub) framing for HAIR SALONS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file
owns ONLY the unique, hair-salon-specific framing prose that leads with the salon's real world:
booked chairs and stylist loyalty, a five-to-eight week color and root rebooking cadence that is
the retention engine, a stylist with both hands in a client's hair while the desk phone rings out,
Instagram-driven discovery, and no-shows on booked chairs. Booked chairs, not walk-ins.

Honesty rules match the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear, the salon's own service pricing stays generic; no em/en dashes anywhere; "slips away" and
"find the gap", never "leak" as a money metaphor. The AI receptionist does scheduling and intake
only and hands anything that needs a stylist's judgment to the stylist.
"""

PILLAR = {
    "h1": "Hair Salon Software and Marketing That Books and Rebooks",
    "title": "Hair Salon Software and Marketing That Books and Rebooks | Top Shelf Business Solutions",
    "meta_desc": "Hair salon software and marketing in one place: an AI receptionist that books the right stylist, a CRM that rebooks color clients, and a site that ranks.",
    "answer": "A hair salon runs on booked chairs and stylist loyalty. A color client is a standing visit every five or six weeks, and that rebook is the retention engine. Top Shelf puts it in one place: an AI receptionist that books the right stylist, a CRM that rebooks color before the roots show, and a site that ranks.",
    "faq_eyebrow": "salon owners ask",
    "sections": [
        {"h2_html": "Where a hair salon actually <em>loses chairs</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A hair salon rarely loses a client on the work. It loses the chair in the gaps around a full column. A stylist is mid-color when the phone rings, so the new client who found her on Instagram gets voicemail and books the salon that answered. A color client leaves without her next visit booked, means to call, and six or eight weeks later her roots are showing and she is scrolling for whoever can fit her in. And a no-show or a chair that never rebooks is standing revenue, gone, because a color client is not one appointment but a year of them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps one at a time. An <a href="ai-receptionist-for-hair-salons.html">AI receptionist</a> answers calls, texts, and Instagram messages on the first ring, books the right service with the right stylist for the right amount of chair time, and hands a color correction or a consultation to you. A <a href="crm-for-hair-salons.html">CRM</a> prompts every client to rebook on the cadence her service needs, so the six week color client hears from you right before the regrowth shows, and it wins back the regulars who drifted. And a <a href="websites-seo-for-hair-salons.html">website built to rank</a> gets you found for hair salon near me, shows your work, and books her in a tap.</p>'''},
        {"h2_html": "One system, not a <em>drawer of apps</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most of this slips because it lives in a booking app, a reviews tab, an Instagram inbox, and a front desk that cannot always pick up, and none of them talk. Top Shelf is one connected system instead. The appointment the receptionist books lands in the same CRM that fires the rebooking nudge before her roots show and the review request the moment she is done. Your <a href="marketing-for-hair-salons.html">marketing</a> keeps your Google profile and your Instagram working together, which is where new clients actually decide, and every one it brings in feeds the same list. You keep your own client list and your photos, and they go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that book the right stylist and rebook every client. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist sticks to scheduling and hands anything that needs a stylist's judgment straight to you. A free audit is the place to start: it shows exactly where your calls, rebooks, and chairs are slipping away, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a hair salon?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Do I have to replace my booking software?",
         "No. Top Shelf is built around how a salon actually books, by service and by stylist, with the right chair time set aside. It fills the gaps in answering calls, rebooking color and cut clients, and getting found, and your client list and your photos stay yours and leave with you if you ever go."),
        ("Will the AI receptionist book the right stylist and service?",
         "Yes. It answers calls, texts, and messages on the first ring, books the right service with the right stylist for the right amount of chair time, and is upfront that it is an assistant. Anything that needs a stylist's judgment, like a big color correction or a consultation, it captures and hands straight to you."),
    ],
    "service_schema_name": "Business software and marketing for hair salons",
    "cta_h2": "See what your salon is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, rebooks, and chairs are slipping away, whether you work with us or not. No credit card, never a call center.",
}
