"""Pillar (trade hub) framing for PLUMBERS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file
owns ONLY the unique, plumber-specific framing prose that makes the pillar non-thin and leads
with the plumber's real world, never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge
instead of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time
site) ever appear; no em/en dashes anywhere; "find the gap" / "slips away", never "leak" as a
money metaphor (a literal burst pipe is fine).
"""

PILLAR = {
    "h1": "Software and Marketing Built for Plumbers",
    "title": "Software and Marketing Built for Plumbers | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing built for plumbers: an AI receptionist that answers every call, a CRM that follows up on every quote, online booking, reviews, and a site that ranks.",
    "answer": "Plumbing runs on the phone, and the jobs you lose are the calls you could not get to and the quotes nobody circled back on. Top Shelf puts the whole fix in one place for plumbers: an AI receptionist that answers every call, a CRM that chases every quote, online booking, review requests, and a website built to rank in your service area.",
    "faq_eyebrow": "plumbers ask",
    "sections": [
        {"h2_html": "Where a plumbing business actually <em>loses jobs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A plumbing business almost never loses work on price. It loses it in the small gaps between a homeowner needing help and you being free to answer. You are under a sink, in a crawlspace, or driving to the next call when the phone rings, so the emergency rolls to voicemail and the caller moves down the list. A water heater quote you sent Tuesday goes quiet because nobody followed up while the homeowner gathered two other bids. A routine drain cleaning turns into two days of phone tag and books with whoever was easier to reach. Each one is a job you had half-earned and let slip away.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf is built to close those gaps one at a time. An <a href="ai-receptionist-for-plumbers.html">AI receptionist</a> answers every call day or night and tells a burst pipe from a drip. A <a href="crm-for-plumbers.html">CRM</a> keeps every open quote in front of you and follows up on its own. <a href="online-booking-for-plumbers.html">Online booking</a> lets routine work schedule itself, while <a href="automation-for-plumbers.html">automatic reminders</a> cut the empty-house trips. And when the crisis is over, <a href="review-software-for-plumbers.html">review software</a> asks the happy customer at the one moment they are most willing to say yes.</p>'},
        {"h2_html": "One system, not a <em>truck full of apps</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason most of this falls through is that it lives in five different places, and a busy plumber does not have time to run five tools between service calls. Top Shelf is one connected system instead. The call the receptionist books lands in the same CRM that fires the reminder the day before and the review request the moment the job is marked done. Your <a href="websites-seo-for-plumbers.html">website and local SEO</a> feed the whole thing by getting you found in the map pack where the calls actually start, and your <a href="marketing-for-plumbers.html">marketing</a> keeps the pipeline full. You keep your own number and your own customer list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and quote. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist hands a real emergency straight to you rather than pretending to handle it. A free audit is the place to start: it shows you exactly where your calls, quotes, and jobs are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a plumbing company?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Do I have to throw out the tools I already use?",
         "No. Top Shelf runs on your existing phone number and is built around how a plumbing business already works. It fills the gaps in answering calls, following up on quotes, and getting found, and your number and customer list stay yours and leave with you if you ever go."),
        ("Will the AI receptionist actually handle a plumbing emergency?",
         "It triages like you would. It answers on the first ring, asks whether the water is shut off, gets the address, and either books the routine visit or flags a true emergency straight to your phone so you decide whether to roll a truck. It is upfront that it is an assistant, not a person, and it never pretends to fix a crisis on its own."),
    ],
    "service_schema_name": "Business software and marketing for plumbers",
    "cta_h2": "See what your plumbing business is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, quotes, and jobs are slipping away, whether you work with us or not. No credit card, never a call center.",
}
