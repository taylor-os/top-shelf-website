"""Pillar (trade hub) framing for PERSONAL TRAINERS. generate_pillars.py owns the mechanics
(shell, schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This
file owns ONLY the unique, trainer-specific framing prose that leads with the coach's real world:
a solo coach selling one-on-one or small-group coaching, whose funnel runs inquiry to free
consult to a signed package, who is mid-session on the floor when the phone rings, whose money is
in package sales and long-term retention, and whose easiest wins are the clients who fell off. Not
a gym membership and not a class studio.

Honesty rules match the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear, the trainer's own package pricing stays generic; no em/en dashes anywhere; "slips away"
and "find the gap", never "leak" as a money metaphor. The AI does scheduling and intake only, and
nothing here makes a guaranteed-results, weight-loss, transformation, or health-outcome claim.
"""

PILLAR = {
    "h1": "Personal Trainer Software and Marketing That Books Consults",
    "title": "Personal Trainer Software and Marketing That Books Consults | Top Shelf Business Solutions",
    "meta_desc": "Personal trainer software and marketing in one place: an AI receptionist that books consults, a CRM that follows up and wins back clients, and a site that ranks.",
    "answer": "A personal trainer sells coaching, so the business runs on a roster, session packages, and a funnel from inquiry to consult to a signed package, while you are mid-session. Top Shelf puts it in one place: an AI receptionist that books the consult, a CRM that follows up and wins back clients who fell off, and a site that ranks.",
    "faq_eyebrow": "personal trainers ask",
    "sections": [
        {"h2_html": "Where a personal trainer actually <em>loses clients</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A personal trainer rarely loses a client on the coaching. You lose them in two places: the inquiry you could not answer, and the client who quietly drifted off. A prospect who just decided to get serious calls or messages two or three trainers and hires whoever replies first, and you are mid-session with your hands full when it comes in. Meanwhile a client whose package ran out with no renewal, or who skipped two weeks and lost the thread, fades away without ever saying so. Both are whole packages and coaching months walking out, not single sessions, and each one would have paid out over weeks.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps one at a time. An <a href="ai-receptionist-for-personal-trainers.html">AI receptionist</a> answers calls, texts, and social messages the moment they land, speaks to your coaching and rates, and books the free consult straight onto your calendar. A <a href="crm-for-personal-trainers.html">CRM</a> follows up on every consult that went quiet, checks in with new clients through their first weeks, prompts the renewal before a package runs out, and wins back the clients who fell off months ago. And a <a href="websites-seo-for-personal-trainers.html">website built to rank</a> gets you found for personal trainer near me and turns the search into a booked consult.</p>'''},
        {"h2_html": "One system, not a <em>handful of apps</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most of this slips because it lives in a training app, a notes screen, a DM inbox, and a phone you cannot answer mid-session, and none of them follow up on their own. Top Shelf is one connected system instead. The consult the receptionist books lands in the same CRM that runs the check-ins and flags the client who has gone quiet. Your <a href="marketing-for-personal-trainers.html">marketing</a> keeps you findable where people look for a trainer and where they scroll, and every inquiry it brings in feeds the same follow-up. You keep your own client list, and it goes with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that book the consults and follow up on every client. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist only schedules and takes intake, handing a medical question or a program request straight to you and never promising anyone a result. A free audit is the place to start: it shows exactly where your inquiries, consults, and clients are slipping away, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a personal trainer?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("A lot of my leads text or DM instead of calling. Does this catch those?",
         "Yes. The AI receptionist answers calls, texts, and social messages the moment they land, day or night, which is exactly where a lot of new-client interest arrives after someone sees a training clip at night. It speaks to your coaching and rates and books the consult, so the fast reply is the one that wins the client."),
        ("Does the AI receptionist promise clients results?",
         "No. It only schedules and takes intake, books the free consult, and is upfront that it is an assistant. A medical question or a custom program request it captures and hands straight to you, and it never pretends to be a person or promises anyone an outcome."),
    ],
    "service_schema_name": "Business software and marketing for personal trainers",
    "cta_h2": "See what your training business is <em>missing</em>",
    "cta_sub": "Get a free audit of where inquiries, consults, and clients are slipping away, whether you work with us or not. No credit card, never a call center.",
}
