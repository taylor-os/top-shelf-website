"""Pillar (trade hub) framing for GARAGE DOOR COMPANIES. generate_pillars.py owns the mechanics
(shell, schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This
file owns ONLY the unique, garage-door-specific framing prose that leads with the owner's real
world (a snapped spring with a car trapped inside, same-day work to whoever answers first), never
a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge
instead of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time
site) ever appear; no em/en dashes anywhere; "slips away" / "goes cold" / "find the gap", never
"leak" as a money metaphor.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Garage Door Companies",
    "title": "Software and Marketing Built for Garage Door Companies | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for garage door companies: an AI receptionist that answers every call, a CRM that follows up on quotes, plus booking, reviews, and SEO.",
    "answer": "When a garage door spring snaps, there is a car trapped inside and a homeowner dialing three companies. Whoever answers first books the job, and the one who calls back an hour later reaches someone already scheduled. Top Shelf answers every call you cannot take under a door, follows up on the replacement quotes, and books the tune-ups.",
    "faq_eyebrow": "garage door owners ask",
    "sections": [
        {"h2_html": "Where a garage door company <em>loses the call</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A garage door business runs on same-day work, and same-day work goes to whoever answers first. A spring lets go with a car trapped inside, a door jams shut on the way to work, and the homeowner is not shopping, they are calling straight down the list until a person picks up. If you are under a door or driving to the next job, the call rolls to voicemail and the job is gone, often to a company whose work is not as good as yours. The after-hours calls, the door stuck open at night with the house exposed, are the same story and often the most profitable of the week. And the full door replacement you quoted sits for weeks, because a new door is a considered purchase, and it books with whoever checked back.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf answers for you the moment you cannot. An <a href="ai-receptionist-for-garage-door-companies.html">AI receptionist</a> picks up every call, days, nights, and weekends, tells a snapped spring or a trapped car from routine work, and books the job on your schedule. A <a href="crm-for-garage-door-companies.html">CRM</a> keeps every replacement quote in front of you and follows up on the doors people are still deciding on. <a href="online-booking-for-garage-door-companies.html">Online booking</a> lets a seasonal tune-up schedule itself instead of dying in phone tag, and <a href="automation-for-garage-door-companies.html">automation</a> sends the thank-you, the review request, and a tune-up reminder months later, so one repair becomes repeat work.</p>'''},
        {"h2_html": "One system, not a <em>glovebox full of apps</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">None of that works if it lives in four apps that never talk to each other. Top Shelf is one system instead. The call the receptionist books lands in the same CRM that fires the tune-up reminder later and the <a href="review-software-for-garage-door-companies.html">review request</a> the moment the door is working again and the customer is relieved. Your <a href="websites-seo-for-garage-door-companies.html">website and SEO</a> get you into the map pack when a homeowner searches garage door repair near them, which is where most of these calls actually start, and your <a href="marketing-for-garage-door-companies.html">marketing</a> keeps that profile active and full of finished-door photos so you are the name they see first. You keep your own number and your own customer list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The price is easy to follow. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and quote. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. No honest company can promise a specific spot on Google, because nobody controls it, and the AI receptionist flags a true emergency like a trapped car straight to you rather than pretending to handle it. A free audit shows you how many calls you are missing right now, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a garage door company?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Will the AI receptionist know a real emergency from a routine call?",
         "Yes. It asks the questions that sort it out, whether a car is trapped inside, whether the door is stuck open and the house is exposed, and flags those to you right away while booking routine repairs and tune-ups for the next opening. You set the rules for what counts as urgent enough to reach you after hours."),
        ("Do I have to change my phone number?",
         "No. Top Shelf answers on your existing number and is built around how a garage door business already works. It fills the gaps in answering calls, following up on quotes, and getting found on the map, and your number and customer list stay yours."),
    ],
    "service_schema_name": "Business software and marketing for garage door companies",
    "cta_h2": "See what your garage door company is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, quotes, and jobs are slipping away, whether you work with us or not. No credit card, never a call center.",
}
