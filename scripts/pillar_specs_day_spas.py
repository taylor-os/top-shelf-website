"""Pillar (trade hub) framing for DAY SPAS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file
owns ONLY the unique, day-spa-specific framing prose that leads with the day spa's real world: a
full-service relaxation destination whose revenue base is packages, memberships, and gift cards,
with the gifting seasons doing an outsized share of the year, and one busy front desk juggling
in-spa guests while the phone rings. Guests unwinding, not patients; a serene destination, not a
clinic or one massage room.

Honesty rules match the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear, the spa's own package and gift card pricing stays generic; no em/en dashes anywhere;
"slips away" and "find the gap", never "leak" as a money metaphor. The AI receptionist does
scheduling and booking only and nothing here promises a health or wellness outcome.
"""

PILLAR = {
    "h1": "Day Spa Software and Marketing in One Place",
    "title": "Day Spa Software and Marketing in One Place | Top Shelf Business Solutions",
    "meta_desc": "Day spa software and marketing in one place: an AI receptionist that books spa days and gift cards, a CRM that rebooks guests, and a site that ranks.",
    "answer": "A day spa lives on packages, memberships, and gift cards, with the gifting seasons carrying much of the year while one front desk juggles guests and a ringing phone. Top Shelf puts it in one place: an AI receptionist that books the room, a CRM that rebooks guests and revives gift cards, online booking, reviews, and a site that ranks.",
    "faq_eyebrow": "day spa owners ask",
    "sections": [
        {"h2_html": "Where a day spa actually <em>loses bookings</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A day spa rarely loses a guest on the quality of the treatment. It loses the booking in the gaps around a busy front desk. The phone rings while your one person is checking a guest into the lounge or turning over a room, so the caller weighing a couples massage against a full spa day, or trying to buy a gift card before a birthday, gets voicemail and books the spa that answered. A guest floats out unwound without the next visit on the calendar, and months pass before she thinks of it. And a pile of gift cards from the last gifting season sits unredeemed, money already collected that never becomes a visit.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps one at a time. An <a href="ai-receptionist-for-day-spas.html">AI receptionist</a> answers every call and text, warm and unhurried, explains what a package includes, checks the book for a couples room, and books it or captures the gift card sale. A <a href="crm-for-day-spas.html">CRM</a> reminds each guest when she is due to unwind again and chases down the unused gift cards and half-used packages before the value goes to waste. And a <a href="websites-seo-for-day-spas.html">website built to rank</a> gets you found for a day spa near me and a spa gift card, and lets a guest book a spa day or buy a card on the spot.</p>'''},
        {"h2_html": "One system, not a <em>shelf of apps</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most of this slips because it lives in a booking app, a gift card tool, a reviews tab, and a phone no one can reach, and a full front desk cannot run all of them at once. Top Shelf is one connected system instead. The visit the receptionist books lands in the same CRM that reminds the guest when she is due and flags the gift card going unused. Your <a href="marketing-for-day-spas.html">marketing</a> keeps your Google profile active and your reviews fresh, which is where guests planning an escape and shoppers hunting a gift actually look, and every new guest it brings in feeds the same list. You keep your own guest list, and it goes with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that book the room and rebook every guest. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist sticks to scheduling and hands anything that needs a person straight to your team. A free audit is the place to start: it shows exactly where your bookings, gift cards, and rebookings are slipping away, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a day spa?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Do I have to replace the booking tool I already use?",
         "No. Top Shelf is built around how a day spa actually runs, packages, memberships, gift cards, and a front desk that cannot always reach the phone. It fills the gaps in answering, rebooking, and getting found, and your guest list stays yours and leaves with you if you ever go."),
        ("Can the AI receptionist handle a gift card or package question?",
         "Yes. It answers on the first ring by phone and text, warm and unhurried, explains what a package includes, checks the book for a couples room, and books the visit or captures the details so your team can finish a gift card sale. It sticks to scheduling and booking, is upfront that it is an assistant, and hands anything that needs a person to you."),
    ],
    "service_schema_name": "Business software and marketing for day spas",
    "cta_h2": "See what your day spa is <em>missing</em>",
    "cta_sub": "Get a free audit of where bookings, gift cards, and rebookings are slipping away, whether you work with us or not. No credit card, never a call center.",
}
