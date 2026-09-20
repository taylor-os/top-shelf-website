"""Pillar (trade hub) framing for HANDYMAN BUSINESSES. generate_pillars.py owns the mechanics
(shell, schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This
file owns ONLY the unique, handyman-specific framing prose that leads with the handyman's real
world (a high volume of small jobs and small quotes, scheduling little work, filling the gaps
between bigger jobs), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge
instead of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time
site) ever appear; no em/en dashes anywhere; "slips away" / "goes cold" / "find the gap", never
"leak" as a money metaphor.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Handyman Businesses",
    "title": "Software and Marketing Built for Handyman Businesses | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for handyman businesses: an AI receptionist that answers every call, a CRM that chases every small quote, plus booking, reviews, and SEO.",
    "answer": "A handyman's day is a stack of small jobs and even more small quotes, a number texted about some shelves, a rough figure in a driveway. None is big enough to chase by hand, so they pile up and go quiet, and the little jobs book with whoever answered. Top Shelf answers, logs every quote, and nudges each one.",
    "faq_eyebrow": "handymen ask",
    "sections": [
        {"h2_html": "Where a handyman <em>loses the small jobs</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A handyman does not lose one big job to a rival, they lose a dozen small ones to friction. The phone rings while you are up a ladder or under a sink, so it goes to voicemail, and a homeowner with a short to-do list does not leave a message, they call the next name until someone picks up. You give out prices all day, a text about hanging shelves, a rough number in a driveway, a punch-list on the back of a receipt, and any one of them is easy to forget when there are dozens. Chasing a small quote by hand feels like more bother than the little job is worth, so it never happens, and the work quietly drifts to whoever got back first.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf catches the work you cannot get to. An <a href="ai-receptionist-for-handyman-services.html">AI receptionist</a> answers on the first ring while your hands are full, takes down the whole list, and books it, so there is no voicemail to return. A <a href="crm-for-handyman-services.html">CRM</a> keeps every customer and leftover to-do in one place and brings the repeat work back with a seasonal nudge. <a href="online-booking-for-handyman-services.html">Online booking</a> lets a routine job like a TV mount or a short punch-list schedule itself into the gaps in your week, and <a href="automation-for-handyman-services.html">automation</a> logs every quick quote and sends each one a timed check-in, so the small tickets get chased even though none is worth stopping your day for.</p>'''},
        {"h2_html": "One place, not <em>sticky notes and text threads</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For a one-person shop, running four separate apps between jobs is a nonstarter, which is why most of this lives in your texts, your memory, and a receipt on the dash. Top Shelf is one place instead. The job the receptionist books lands in the same CRM that fires the <a href="review-software-for-handyman-services.html">review request</a> the moment a job is marked done, and a handyman review is unusually powerful because it lists everything you fixed in one visit, which is exactly the proof the next mixed-list homeowner wants. Your <a href="websites-seo-for-handyman-services.html">website and SEO</a> list the dozens of small jobs you really do, so a visitor spots their own task and finds you nearby, and your <a href="marketing-for-handyman-services.html">marketing</a> keeps you the recognized name a neighborhood already trusts. Your number and customer list stay yours.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is honest and flat. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and quote. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it, and there is no per-call meter, so a busy week does not run up the bill. No honest company can promise a specific spot on Google, because nobody controls it. A free audit shows you where the small jobs are slipping away, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a handyman business?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee, and no per-call charge on the receptionist."),
        ("Is this worth it if it is just me?",
         "Usually yes. Even a solo handyman serves more homes and gives out more small quotes than anyone can track by memory, and that is exactly where the work slips. The receptionist and follow-up handle the parts you cannot get to mid-job, so recover one job you would have lost and it more than covers itself."),
        ("Are the small quotes even worth chasing?",
         "Added up, absolutely. No single quick number is worth much, but you give out so many that the ones going quiet are real money over a month. Chasing each by hand is not worth your time, so automation nudges every one for you, whether it is a big job or a small one."),
    ],
    "service_schema_name": "Business software and marketing for handyman businesses",
    "cta_h2": "See what your handyman business is <em>missing</em>",
    "cta_sub": "Get a free audit of where small jobs and quotes are slipping away, whether you work with us or not. No credit card, never a call center.",
}
