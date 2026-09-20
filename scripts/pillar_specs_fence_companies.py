"""Pillar (trade hub) framing for FENCE COMPANIES. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, fence-specific framing prose that makes the pillar non-thin and leads with the
fence company's real world, never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "slips away" / "goes cold", never "leak" as a metaphor. The AI
receptionist does scheduling and intake only, it never sets a fence price or binds an estimate, the
owner always walks the yard and quotes it.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Fence Companies",
    "title": "Software and Marketing Built for Fence Companies | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for fence companies: an AI receptionist that answers every estimate, a CRM that follows up on every quote, and a site that shows your styles.",
    "answer": "A fence is a want, not an emergency, so the homeowner who decides to fence the yard calls three or four companies and hires whoever answers and measures soonest. Miss that call while your crew is setting posts and the job is gone. Top Shelf answers every estimate call, follows up on every quote, and gets you found.",
    "faq_eyebrow": "fence companies ask",
    "sections": [
        {"h2_html": "Where a fence company actually <em>loses jobs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A fence company loses work in two places, and neither is price. The first is the estimate call. A homeowner who has decided to fence the yard, for a new dog, for privacy, to meet pool code, or on a fresh new-build lot, calls down a list of three or four companies, and your whole crew is out setting posts in concrete, hanging panels, or in a backyard that swallows the signal, so the call rings out and the measure books with whoever picked up. The second is the quote itself. A fence is rarely a same-day decision, so the homeowner gathers other bids, talks it over with a spouse, and waits on the HOA to approve the style, and a quote that goes quiet over those weeks is usually a maybe nobody circled back on, not a no.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes both gaps. An <a href="ai-receptionist-for-fence-companies.html">AI receptionist</a> answers every call on the first ring, evenings and weekends included, asks what they want fenced, the material, and roughly how much yard, and books the measure or hands you a qualified lead, so the estimate never rolls to voicemail while the crew is on the truck. A <a href="crm-for-fence-companies.html">CRM</a> keeps every open quote in front of you and sends timed check-ins on its own through the deciding weeks, so the homeowner comparing three companies keeps hearing from you while the other two go quiet, and the yards you built years ago come back for a gate, a stain, or a repair. It never sets a price, you still walk the yard and quote it yourself.</p>'},
        {"h2_html": "One system, not a <em>pile of separate tools</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">All of that slips through because it usually lives in a pile of separate tools, and a crew stretching chain-link cannot run them between post holes. Top Shelf is one connected system instead. The measure the receptionist books lands in the same CRM that fires the follow-up and then the review request the day the fence is finished and the homeowner is standing there admiring it. Your <a href="websites-seo-for-fence-companies.html">website and local SEO</a> feed it by showing your wood, vinyl, aluminum, and chain-link work and ranking for the fence searches homeowners actually make, and your <a href="marketing-for-fence-companies.html">marketing</a> turns the most visible thing you build, a clean run on the property line, into neighbor referrals and a steady flow of reviews. You keep your own number and your own customer list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every estimate call and every open quote. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the receptionist handles scheduling and intake only, it never sets a fence price or binds an estimate, that stays with you at the measure. A free audit is the place to start, and it shows you where your estimate calls and quotes are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a fence company?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Will the receptionist quote the fence?",
         "No. It handles scheduling and intake only. It gathers what they want fenced, the material, and roughly how much yard, then books the measure or hands you the lead. You still walk the yard, set the scope, and give the price. It never binds an estimate in your name."),
        ("Do I have to replace the tools I already use?",
         "No. Top Shelf runs on your existing phone number and is built around how a fence company already works. It fills the gaps in answering estimate calls and following up on quotes, and your number and customer list stay yours and leave with you if you ever go."),
    ],
    "service_schema_name": "Business software and marketing for fence companies",
    "cta_h2": "See what your fence company is <em>missing</em>",
    "cta_sub": "Get a free audit of where your estimate calls and quotes are slipping away, whether you work with us or not. No credit card, never a call center.",
}
