"""Pillar (trade hub) framing for URGENT CARE. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, urgent-care-specific framing prose that leads with the clinic's real world
(walk-in volume, open-now hours, the flood of logistics calls, and the employer / occupational-
health accounts that recur all year), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "find the gap" / "slips away", never "leak". ETHICS (strict): the
AI receptionist answers LOGISTICS only (hours, wait, insurance, services), NEVER gives medical
advice or assesses symptoms, and sends anyone describing a serious emergency to 911 or the nearest
emergency room. No clinical or medical-outcome claim anywhere.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Urgent Care",
    "title": "Software and Marketing Built for Urgent Care | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing built for urgent care: an AI receptionist that answers hours, wait, and insurance calls, a CRM for employer accounts, and a site that ranks.",
    "answer": "Urgent care runs on walk-in volume and extended hours, so the phone floods with logistics: are you open, what is the wait. A caller who cannot get through taps the next clinic or drives to the ER. Top Shelf fixes the front desk: an AI receptionist answering 24/7, a CRM for employer accounts, and a site that ranks.",
    "faq_eyebrow": "urgent care operators ask",
    "sections": [
        {"h2_html": "Where an urgent care actually <em>loses visits</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An urgent care loses visits at the two moments it is busiest. The first is the phone during a full lobby. When someone sick or hurt calls to ask the questions that decide where they go, whether you are open, how long the wait is, whether you take their plan, whether you do X-rays or stitches, your front desk is checking in walk-ins and rooming patients, so the call rings through to voicemail. A parent watching a fever climb does not leave a message. They tap the next clinic on the map or drive to the emergency room. The calls most likely to go unanswered are your nights, weekends, and holidays, which are the whole reason patients choose you.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The second loss is the standing business a walk-in-only plan ignores: the local employers who need physicals, drug screens, and a place to send a worker hurt on the job, all year. Top Shelf catches both. An <a href="ai-receptionist-for-urgent-care.html">AI receptionist</a> answers every call on the first ring, day or night, covers the hours, wait, insurance, and services questions, and points patients to online check-in, while sending any real emergency to 911. A <a href="crm-for-urgent-care.html">CRM</a> keeps every employer account warm and reminds past patients you are open late, and steady <a href="marketing-for-urgent-care.html">local marketing</a> gets you into the map pack for urgent care near me and open now.</p>'},
        {"h2_html": "One system, not <em>a busy signal</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Calls go to voicemail and employer accounts drift because answering, follow-up, reviews, and the website live in separate places, and a slammed front desk cannot run all of them. Top Shelf connects them. The check-in the receptionist points a caller to feeds the same system that follows up with the employer whose account went quiet, and your <a href="websites-seo-for-urgent-care.html">website and local SEO</a> get you found for near-me and open-now searches with accurate hours. You keep your own number and your accounts and records, and they stay yours if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that answer the phone 24/7 and keep employer accounts booked. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist answers logistics only, never medical advice, and sends anyone describing a serious emergency to 911 or the nearest emergency room. A free audit shows you exactly where calls and accounts are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for an urgent care clinic?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom five page site is $1,500. There is no setup fee."),
        ("Does the AI receptionist give any medical advice?",
         "No, and that is deliberate. It answers logistics only, your hours, wait time, insurance, and services, and points patients to online check-in. Anyone describing a serious emergency is told to call 911 or go to the nearest emergency room, and every clinical judgment stays with your staff."),
        ("Can it handle both walk-in patients and employer accounts?",
         "Yes. It answers the walk-in logistics calls that flood your front desk, and the CRM keeps your occupational-health accounts warm, following up with employers about physicals, drug screens, and injury care so a one-time batch of screenings becomes a standing relationship."),
    ],
    "service_schema_name": "Business software and marketing for urgent care clinics",
    "cta_h2": "See what your urgent care is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls and employer accounts are slipping away, whether you work with us or not. No credit card, never a call center.",
}
