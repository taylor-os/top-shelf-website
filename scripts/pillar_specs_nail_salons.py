"""Pillar (trade hub) framing for NAIL SALONS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file
owns ONLY the unique, nail-salon-specific framing prose that leads with the salon's real world:
high-volume mani/pedi work, a mix of booked appointments and walk-ins, a fast two-to-three week
fill and rebooking cadence, techs working with both hands on a client, a nail-art Instagram
portfolio as the discovery driver, and groups and events that book together. Clients pick by the
work shown and switch freely; not a hair salon's years-long stylist loyalty.

Honesty rules match the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($99/$199 Signature plan, $499 website) ever
appear, the salon's own mani, pedi, gel, and acrylic pricing stays generic; no em/en dashes
anywhere; "slips away" and "find the gap", never "leak" as a money metaphor. The AI receptionist
does scheduling and intake only and hands anything that needs the owner's call to the owner.
"""

PILLAR = {
    "h1": "Nail Salon Software and Marketing That Books Every Fill",
    "title": "Nail Salon Software and Marketing That Books Every Fill | Top Shelf Business Solutions",
    "meta_desc": "Nail salon software and marketing in one place: an AI receptionist that books the right service, a CRM that rebooks on the fill cadence, and a site built so Google can read it.",
    "answer": "A nail salon runs on high volume, walk-ins and appointments, and a fast two to three week fill cadence, with techs working hands-full. Top Shelf puts it in one place: an AI receptionist that tells a gel fill from a full set and books it, a CRM that rebooks before her polish grows out, and a site built so Google can read it.",
    "faq_eyebrow": "nail salon owners ask",
    "sections": [
        {"h2_html": "Where a nail salon actually <em>loses bookings</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A nail salon rarely loses a client on the work. It loses the booking in the gaps around a room full of tables. Every tech has both hands on a client, or a client sits with her fingers under the lamp, when the phone rings, so the woman who chipped a nail before an event or wants a fresh set this afternoon books whoever answered. A group booking for a birthday or a bridal party goes to the salon that picked up. And a client leaves thrilled without rebooking, and on a two to three week fill cadence her gel lifts and she resurfaces at whatever salon was convenient.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps one at a time. An <a href="ai-receptionist-for-nail-salons.html">AI receptionist</a> answers on the first ring by phone and text, tells a quick polish change from a full set of acrylics that needs real chair time, and books it onto the right tech or holds the details. A <a href="crm-for-nail-salons.html">CRM</a> reminds each client on the short cadence nail work runs on, tracks the punch cards and prepaid packages, and revives the regulars who drifted. And a <a href="websites-seo-for-nail-salons.html">website built to rank</a> gets you found for nail salon near me, shows your nail art, and books a fill or pedicure in a tap.</p>'''},
        {"h2_html": "One system, not a <em>tray of apps</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most of this slips because it lives in a booking app, a punch card, an Instagram feed, and a phone no one at the tables can reach, and none of them talk. Top Shelf is one connected system instead. The appointment the receptionist books lands in the same CRM that watches the fill cadence and flags the package going unused. You keep your own client list and your photos, and they go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Signature plan, $99 a month for up to 10 users, includes the AI receptionist and the CRM that book the right service and rebook every client. A professional website is $499 one time, and you do not need a plan to buy one. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist sticks to scheduling and hands anything that needs your call straight to you.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a nail salon?",
         "The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM. A professional website is $499 one time. There is no setup fee."),
        ("Do I have to replace the booking app I already use?",
         "No. Top Shelf is built around how a nail salon actually runs, a mix of walk-ins and appointments on a short fill cadence, with real chair time for a full set or a spa pedicure. It fills the gaps in answering, rebooking, and getting found, and your client list and photos stay yours and leave with you if you ever go."),
        ("Will the AI receptionist book the right service?",
         "Yes. It answers on the first ring by phone and text, tells a gel fill from a full set of acrylics that needs far more chair time, and books it onto the right tech or holds the details for you. It sticks to scheduling, is upfront that it is an assistant, and hands anything that needs your call straight to you."),
    ],
    "service_schema_name": "Business software and websites for nail salons",
    "cta_h2": "See what your nail salon is <em>missing</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
}
