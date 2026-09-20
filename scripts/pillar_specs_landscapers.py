"""Pillar (trade hub) framing for LANDSCAPERS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file
owns ONLY the unique, landscaper-specific framing prose that leads with the landscaper's real
world (a whole season that lands in a few weeks, season-long maintenance customers, install bids
that go cold on the route), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge
instead of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time
site) ever appear; no em/en dashes anywhere; "slips away" / "goes cold" / "find the gap", never
"leak" as a money metaphor.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Landscapers",
    "title": "Software and Marketing Built for Landscapers | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for landscapers: an AI receptionist for the spring rush, a CRM that re-signs your route, plus booking, reviews, and a ranking site.",
    "answer": "Landscaping is a whole season that lands in a few weeks. The first warm stretch, half the neighborhood decides to hire out the yard at once, while your crews are on the route with mowers running. A missed call is not a single cut, it is a season-long customer. Top Shelf answers every call and chases the install bids.",
    "faq_eyebrow": "landscapers ask",
    "sections": [
        {"h2_html": "Where a landscaping company <em>loses the season</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Landscaping demand does not arrive evenly, it arrives all at once, and that is where the season gets lost. The phone is quiet all winter, then the first warm weeks bring a whole season of quote calls at the same time your crews are out on the route with mowers running and nobody can hear a ring. A homeowner who has decided to hire a lawn service does not leave a voicemail, they call the next crew, and the one you missed was a weekly customer worth the whole season, not one cut. The patio or full install you bid sits for weeks while the homeowner compares prices, and books with whoever checked back. Even a commercial or HOA board is quietly vetting you before they ever call.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf catches the calls the mowers drown out. An <a href="ai-receptionist-for-landscapers.html">AI receptionist</a> answers every call at once, tells a weekly mowing signup from a one-off cleanup, and books the estimate or flags a high-value lead to your phone. A <a href="crm-for-landscapers.html">CRM</a> follows up on every open install bid and re-signs your maintenance customers each season instead of letting them forget you over winter. <a href="online-booking-for-landscapers.html">Online booking</a> lets a routine estimate schedule itself on your real availability, and <a href="automation-for-landscapers.html">automation</a> sends timed check-ins on every bid, written to sound like you, so the homeowner comparing crews keeps hearing from you while the others go silent.</p>'''},
        {"h2_html": "One system, not a <em>truck full of clipboards</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Run as four separate apps, all of this falls apart on a mowing week, because the follow-up competes with the actual work on the route and loses. Top Shelf is one system instead. The estimate the receptionist books lands in the same CRM that fires the reminder before the visit and the <a href="review-software-for-landscapers.html">review request</a> the moment the crew pulls back and the homeowner sees the finished yard. Landscaping has an edge most trades do not, because your work photographs well, so a nudge to attach a before-and-after builds a gallery of proof on your profile. Your <a href="websites-seo-for-landscapers.html">website and SEO</a> put a page in front of each town you serve and rank for a landscaper near me, and your <a href="marketing-for-landscapers.html">marketing</a> keeps the profile a cautious HOA board reads before it calls. Your customer list stays yours.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The numbers are simple. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and bid. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it, and no per-call meter, so the spring rush does not run up the bill. No honest company can promise a specific spot on Google, because nobody controls it. A free audit shows you where the season is slipping away, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a landscaping company?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Can the AI receptionist tell a mowing signup from a one-off cleanup?",
         "Yes. It asks what the job is, triages the way you would, and books a routine estimate while flagging a high-value maintenance contract or a commercial bid straight to your phone. It answers every call at once during the spring rush, so a season of calls does not pile up in voicemail while your crews are out."),
        ("Do I keep my number and customer list?",
         "Yes. Top Shelf answers on your existing number, and every customer, property, and note is in your name and exportable any time. The point is to make the route you already built keep producing, not to lock your list inside software you only rent."),
    ],
    "service_schema_name": "Business software and marketing for landscapers",
    "cta_h2": "See what your landscaping company is <em>missing</em>",
    "cta_sub": "Get a free audit of where seasonal calls, bids, and jobs are slipping away, whether you work with us or not. No credit card, never a call center.",
}
