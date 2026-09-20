"""Pillar (trade hub) framing for ROOFERS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file
owns ONLY the unique, roofer-specific framing prose that leads with the roofer's real world
(the post-storm surge, bids that sit for weeks on an insurance adjuster), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge
instead of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time
site) ever appear; no em/en dashes anywhere; "slips away" / "goes cold" / "find the gap", never
"leak" as a money metaphor.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Roofers",
    "title": "Software and Marketing Built for Roofers | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for roofers: an AI receptionist that catches the storm surge, a CRM that works every bid, plus booking, reviews, and a ranking site.",
    "answer": "Roofing moves in storms. A single hail night sends a whole town looking for a roofer in forty-eight hours, and half the bids you write sit for weeks waiting on an insurance adjuster. The job goes to whoever answered first and followed up last. Top Shelf answers the surge, works every bid until the claim clears, and books the inspections.",
    "faq_eyebrow": "roofers ask",
    "sections": [
        {"h2_html": "Where a roofing company <em>loses the roof</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Roofing is a feast and famine trade, and the losses cluster in the feast. After hail or high wind, a homeowner does not call one roofer, they call three and hire whoever picks up and gets someone out to look. So the calls that decide your whole month arrive while your crews are already on roofs, and the overflow rolls to a voicemail nobody leaves. The bids are worse. You climb the roof, write a careful estimate, and the homeowner says they are waiting on the adjuster, and a claim that takes weeks to clear is exactly long enough for them to forget who looked at their roof. The free inspection you booked no-shows because it was loosely agreed on a phone call and never confirmed.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf is built for exactly that week. An <a href="ai-receptionist-for-roofers.html">AI receptionist</a> answers the whole surge at once, day or night, finds out whether a roof is storm damaged or just aging, and books a free inspection on your calendar. A <a href="crm-for-roofers.html">CRM</a> keeps every bid in one place and works the ones waiting on insurance with a longer, gentler cadence, so you are the roofer they call when the check comes. <a href="online-booking-for-roofers.html">Online booking</a> lets a homeowner grab an inspection slot the moment they feel it, and <a href="automation-for-roofers.html">automation</a> sends the thank-you, the claims answer, and the well-timed check-in on every bid without anyone remembering.</p>'''},
        {"h2_html": "One system that catches the <em>whole surge</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The trouble with a storm is that it does not send a steady trickle you can staff for, it sends a season of work in two days, and four disconnected tools cannot hold it. Top Shelf is one system instead. The inspection the receptionist books lands in the same CRM that fires the reminder before the visit and the <a href="review-software-for-roofers.html">review request</a> the afternoon a roof is finished, while the homeowner is standing in the driveway looking up at it. That matters more in roofing than most trades, because there are enough storm-chasers out there that a wall of recent reviews is what a wary homeowner trusts. Your <a href="websites-seo-for-roofers.html">website and SEO</a> get you found instead of a lead directory that resells the same call, and your <a href="marketing-for-roofers.html">marketing</a> keeps you familiar in the towns you work, so you are not bidding cold at the most expensive moment.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is straightforward. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and bid. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and every lead and customer stays yours and exportable any time. A free audit shows you how many storm calls you are missing right now, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a roofing company?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Can it really handle a flood of calls after a storm?",
         "Yes, that is what it is built for. The AI receptionist answers every call at the same time, so a dozen homeowners who would have hit voicemail get a dozen inspections booked instead. It does not put people on hold or clock out at five, and it works nights and weekends when storm calls come in."),
        ("Do I keep my own number and my leads?",
         "Yes. It answers on your existing number, and every caller, bid, and customer is yours and exportable any time. Nothing about your number or your list is held hostage to keep you paying."),
    ],
    "service_schema_name": "Business software and marketing for roofers",
    "cta_h2": "See what your roofing company is <em>missing</em>",
    "cta_sub": "Get a free audit of where storm calls, bids, and jobs are slipping away, whether you work with us or not. No credit card, never a call center.",
}
