"""Pillar (trade hub) framing for GYMS. generate_pillars.py owns the mechanics (shell, schema,
the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns ONLY
the unique, gym-specific framing prose that leads with the gym's real world: a recurring
membership and facility-access model where retention and churn ARE the business, a tour or
free-trial funnel into a join, a front desk running the floor, the New-Year surge, and group
classes. Not a yoga studio and not a personal trainer.

Honesty rules match the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear, membership pricing stays generic; no em/en dashes anywhere; "slips away" and "find the
gap", never "leak" as a money metaphor. The AI does scheduling and intake only, and nothing here
makes a fitness, weight-loss, transformation, or health-outcome claim.
"""

PILLAR = {
    "h1": "Gym Software and Marketing That Fills and Keeps Memberships",
    "title": "Gym Software and Marketing That Fills and Keeps Memberships | Top Shelf Business Solutions",
    "meta_desc": "Gym software and marketing in one place: an AI receptionist that books tours and trials, a CRM that onboards and keeps members, and a site that ranks.",
    "answer": "A gym lives on memberships, so retention and churn are everything and a cancelled member is the biggest loss. Prospects come through a tour or free trial, while the desk runs the floor. Top Shelf puts it in one place: an AI receptionist that books the tour, a CRM that onboards and keeps members, and a site that ranks.",
    "faq_eyebrow": "gym owners ask",
    "sections": [
        {"h2_html": "Where a gym actually <em>loses members</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A gym rarely loses a member over the equipment. It loses them in two places: the join inquiry nobody answered, and the member who quietly drifted toward the door. A prospect decides on a Sunday night that this is finally the week, calls or texts, and the desk is dark or running the floor, so they book the gym that answered. And a member who stops showing up is a cancellation not yet filed, drifting for weeks before the card declines, with nothing built into open-access membership to pull them back. Both are months of recurring dues walking out the door, not one-time sales, and each is far cheaper to keep than to replace.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps one at a time. An <a href="ai-receptionist-for-gyms.html">AI receptionist</a> answers every call and text day or night, answers the membership questions, and books the tour or free trial straight onto your calendar. A <a href="crm-for-gyms.html">CRM</a> runs new members through an onboarding sequence so the routine sets, flags the ones going quiet so you can reach them before they cancel, and wins back the ones who already lapsed. And a <a href="websites-seo-for-gyms.html">website built to rank</a> gets you found for gym near me the moment someone decides to start and lets them book a trial in a tap.</p>'''},
        {"h2_html": "One system, not a <em>stack of apps</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most of this slips because it lives in a billing app, a booking tool, and a phone no one can reach while the floor is busy, and none of them talk to each other. Top Shelf is one connected system instead. The trial the receptionist books lands in the same CRM that runs the onboarding and flags the member who stopped showing up. Your <a href="marketing-for-gyms.html">marketing</a> keeps your Google profile active and well reviewed, which is where people choosing a gym look first, especially in the New Year surge, and every lead it brings in feeds the same follow-up. Your member list is always yours to export.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that book the trials and keep the members. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist sticks to scheduling and hands anything that needs a person, like a billing dispute, straight to your team. A free audit is the place to start: it shows exactly where your inquiries, trials, and members are slipping away, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a gym?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Can this really help with member retention?",
         "It cannot make anyone show up, but it does the thing that quietly prevents most cancellations. The CRM onboards new members so the routine sets, flags the ones who have stopped coming so you can reach them early, and wins back the ones who lapsed. That is where a gym protects the recurring dues it runs on. It makes no promise about anyone's results, only that the drifting member hears from you in time."),
        ("Does the AI receptionist handle the New Year rush?",
         "Yes. It answers every call and text around the clock as part of the plan, including the Sunday-night resolve and the January surge when the most people decide to join, with no per-call fee or after-hours surcharge. It books the tour or trial, is upfront that it is an assistant, and hands anything that needs a person to your team."),
    ],
    "service_schema_name": "Business software and marketing for gyms",
    "cta_h2": "See what your gym is <em>missing</em>",
    "cta_sub": "Get a free audit of where inquiries, trials, and members are slipping away, whether you work with us or not. No credit card, never a call center.",
}
