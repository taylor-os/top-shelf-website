"""Pillar (trade hub) framing for YOGA STUDIOS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file
owns ONLY the unique, yoga-studio-specific framing prose that leads with the studio's real world:
a class-based schedule, an intro offer that converts a newcomer into a member, then class packs,
memberships, retention, and lapsed-student win-back, with teachers on the mat while the phone
rings out. Not a gym facility membership and not a one-to-one personal trainer.

Honesty rules match the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear, the studio's own intro, class-pack, and membership pricing stays generic; no em/en dashes
anywhere; "slips away" and "find the gap", never "leak" as a money metaphor. The AI receptionist
does scheduling and intake only, never advice, and nothing here promises a health, fitness, or
wellness outcome of any kind.
"""

PILLAR = {
    "h1": "Yoga Studio Software and Marketing That Fills Classes",
    "title": "Yoga Studio Software and Marketing That Fills Classes | Top Shelf Business Solutions",
    "meta_desc": "Yoga studio software and marketing in one place: an AI receptionist that books the intro offer, a CRM that converts and keeps students, and a site that ranks.",
    "answer": "A yoga studio runs on a class schedule, an intro offer that turns a newcomer into a member, and class packs and memberships. Teachers are on the mat when the phone rings. Top Shelf puts it in one place: an AI receptionist that books the intro offer, a CRM that follows up before it expires, and a site that ranks.",
    "faq_eyebrow": "yoga studio owners ask",
    "sections": [
        {"h2_html": "Where a yoga studio actually <em>loses students</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A yoga studio rarely loses a student on the teaching. It loses them in two places: the newcomer inquiry nobody answered, and the intro offer that quietly expired. Someone works up the nerve to try a class, calls or sends a DM at night, and the teachers are on the mat or the studio is dark, so she books the studio that replied. And a first-timer who claimed the intro offer, came once or twice, and never heard from you again drifts off before the habit set, along with the member who got busy for a few weeks. Each one is a membership that never got the chance to begin.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps one at a time. An <a href="ai-receptionist-for-yoga-studios.html">AI receptionist</a> answers calls, texts, and DMs on the first ring, warm rather than rushed, answers the beginner questions, points to a class that fits, and books the intro offer. A <a href="crm-for-yoga-studios.html">CRM</a> follows up on every intro offer before it expires, onboards new members, flags the students who have gone quiet, and reaches the right regulars about a class pack running low or a workshop. And a <a href="websites-seo-for-yoga-studios.html">website built to rank</a> gets you found for yoga near me, puts your schedule and intro offer front and center, and books a first class in a tap.</p>'''},
        {"h2_html": "One system, not a <em>row of apps</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most of this slips because it lives in a class-booking app, a reviews tab, a DM inbox, and a phone no one can reach mid-class, and none of them follow up on their own. Top Shelf is one connected system instead. The first class the receptionist books lands in the same CRM that sends the timed intro-offer check-ins and flags the student who stopped coming. Your <a href="marketing-for-yoga-studios.html">marketing</a> keeps your Google profile active and welcoming and your social full of real classes, which is where a nervous beginner decides, and every newcomer it brings in feeds the same follow-up. Every student stays yours and exportable, not locked in software you only rent.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that book the intro offers and keep the students. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist only schedules and takes intake, never advice, handing anything that needs a person to your team. A free audit is the place to start: it shows exactly where your inquiries, intro offers, and students are slipping away, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a yoga studio?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Do I have to replace my class-booking app?",
         "No. Top Shelf is built around how a studio actually grows, an intro offer that converts a newcomer, class packs, and memberships. It fills the gaps in answering, converting the intro offer, and winning back quiet students, and every student stays yours and exportable rather than locked inside software you only rent."),
        ("Can the AI receptionist help a nervous first-timer?",
         "Yes, with the practical part. It answers calls, texts, and DMs warmly, explains how the intro offer works, points to a class on the schedule that suits a beginner, and books it. It only schedules and takes intake, never gives advice or promises any outcome, and hands anything that needs a person to your team."),
    ],
    "service_schema_name": "Business software and marketing for yoga studios",
    "cta_h2": "See what your studio is <em>missing</em>",
    "cta_sub": "Get a free audit of where inquiries, intro offers, and students are slipping away, whether you work with us or not. No credit card, never a call center.",
}
