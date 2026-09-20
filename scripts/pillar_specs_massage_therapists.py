"""Pillar (trade hub) framing for MASSAGE THERAPISTS. generate_pillars.py owns the mechanics
(shell, schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This
file owns ONLY the unique, massage-specific framing prose that leads with the practice's real
world: a licensed single-modality bodywork practice, most often a solo practitioner with no front
desk, so a call during a session goes to voicemail while the hands are literally busy; per-visit
sessions where the monthly rebooking cadence, prepaid packages, and gift certificates are the
retention engine. Not a multi-service day-spa destination.

Honesty rules match the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear, session pricing stays generic; no em/en dashes anywhere; "slips away" and "find the gap",
never "leak" as a money metaphor. The AI does scheduling and intake only; the copy makes no
health, medical, pain-relief, or treatment-outcome claim, because massage here is relaxation and
wellness, not medical treatment.
"""

PILLAR = {
    "h1": "Massage Therapist Software and Marketing in One System",
    "title": "Massage Therapist Software and Marketing in One System | Top Shelf Business Solutions",
    "meta_desc": "Massage therapist software and marketing in one place: an AI receptionist that books while you are in session, a CRM that rebooks regulars, and a site that ranks.",
    "answer": "A massage practice is appointment-driven and usually solo, so a call mid-session goes to voicemail while you are on the table. Repeat business runs on a monthly rhythm, packages, and gift certificates. Top Shelf puts it in one place: an AI receptionist that books while your hands are full, a CRM that rebooks regulars, and a site that ranks.",
    "faq_eyebrow": "massage therapists ask",
    "sections": [
        {"h2_html": "Where a massage practice actually <em>loses bookings</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A massage practice rarely loses a client on the session itself. It loses the booking in the gaps a solo schedule creates. Your hands are on a client in a quiet room when the phone rings, and a sixty or ninety minute session has no break to step out, so the new client comparing a few practices books whoever answered. A regular leaves without the next visit set, the monthly rhythm quietly fades, and no one reaches back out. And prepaid packages and gift certificates sit unused because there is no front desk tracking who still has sessions left.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps one at a time. An <a href="ai-receptionist-for-massage-therapists.html">AI receptionist</a> answers calls and texts on the first ring, day or night, sorts a booking from a quick question, and puts the right session on your calendar while your hands are full. A <a href="crm-for-massage-therapists.html">CRM</a> sends the rebooking nudge on whatever rhythm each client keeps, reaches the ones who drifted off, and tracks the packages and gift certificates people paid for ahead. And a <a href="websites-seo-for-massage-therapists.html">website built to rank</a> gets you found for a massage near me and lets a client book on their own while you are on the table.</p>'''},
        {"h2_html": "One system, not a <em>pile of apps</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most of this slips because it lives in a booking link, a notebook, a reviews tab, and a phone you cannot answer mid-session, and there is no front desk to tie them together. Top Shelf is one connected system instead. The session the receptionist books lands in the same CRM that sends the rebooking nudge a few weeks later and the review request once the client is off the table. Your <a href="marketing-for-massage-therapists.html">marketing</a> keeps your Google profile active and your reviews fresh, which is where a new client sizes you up on trust before booking, and every one it brings in feeds the same list. You keep your own client list, and it goes with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that book the sessions and rebook every regular. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist only schedules and takes intake, handing anything that needs your judgment to you. A free audit is the place to start: it shows exactly where your calls, rebooks, and sessions are slipping away, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a massage practice?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("I work solo with no front desk. Is this built for me?",
         "Especially for you. With one set of hands, a call during a session simply cannot be answered, and there is no one minding the rebooking or the packages people prepaid. Top Shelf answers the calls, books the sessions, and sends the rebooking nudges for you, so the practice keeps running while your hands are full."),
        ("Does the AI receptionist give any health or treatment advice?",
         "No. It only schedules and takes intake details. It sorts a new booking from a quick question, puts the right session length on your calendar, and is upfront that it is an assistant. Anything that needs your judgment it captures and hands straight to you. It never gives advice or promises any outcome."),
    ],
    "service_schema_name": "Business software and marketing for massage therapists",
    "cta_h2": "See what your practice is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, rebooks, and sessions are slipping away, whether you work with us or not. No credit card, never a call center.",
}
