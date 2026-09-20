"""Pillar (trade hub) framing for HOME INSPECTORS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, home-inspection-specific framing prose that leads with the inspector's real world:
a fast quote-and-schedule around a contract or closing deadline, a call missed while up in an attic
or a crawlspace, and the realtor referral network that feeds the work. Never the plumber template,
never the residential-agent world.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "slips away" / "goes cold", never "leak" as a money metaphor. The
AI receptionist does scheduling and intake only, with no inspection-outcome or "we find everything"
promise ever implied.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Home Inspectors",
    "title": "Software and Marketing Built for Home Inspectors | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for home inspectors: an AI receptionist that books every call, a CRM that keeps agents referring, and a site that ranks in your towns.",
    "answer": "Home inspection runs on speed and referrals. A buyer went under contract and needs an inspection before the option period closes, but the call comes while you are in an attic or a crawlspace, so it rolls to voicemail and the agent dials the next inspector. Top Shelf answers every call, books the inspection, and keeps your referring agents warm.",
    "faq_eyebrow": "inspectors ask",
    "sections": [
        {"h2_html": "Where a home inspection business actually <em>loses work</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A home inspection business almost never loses a job on price. It loses it in the small gaps between a buyer going under contract and you being free to pick up. You are in an attic tracing a flue, folded into a crawlspace with no signal, or on a roof with a moisture meter when the phone rings, so the agent working a closing deadline hits voicemail and calls the next inspector on the list. A quote you gave on Tuesday goes quiet because no one followed up while the buyer gathered two others. An agent who sent you one job never hears back and quietly stops referring. Each one is work you had half-earned and let slip away.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf is built to close those gaps one at a time. An <a href="ai-receptionist-for-home-inspectors.html">AI receptionist</a> answers every buyer and agent call day or night, captures the property address and the closing date, and books the inspection or texts it straight to you. A <a href="crm-for-home-inspectors.html">CRM</a> keeps every open quote, past buyer, and referring agent in front of you and sends the timed check-ins for you, so a buyer comparing inspectors keeps hearing from you, an agent who went quiet gets a genuine touch before the next deal, and a past buyer comes back for the re-inspection when the builder warranty year is almost up.</p>'},
        {"h2_html": "One system, not a <em>pile of apps</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason so much of this falls through is that it lives in five different places, and a busy inspector cannot run five tools between houses. Top Shelf is one connected system instead. The call the receptionist books lands in the same CRM that follows up with the agent and fires the review request the moment the report is delivered. Your <a href="websites-seo-for-home-inspectors.html">website and local SEO</a> feed the whole thing by ranking for home inspector near me and the towns you cover, so a buyer under a deadline finds you and books, and your <a href="marketing-for-home-inspectors.html">marketing</a> keeps you in front of the agents who send the steady work. You keep your own number and your own client list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that answer every call and follow up on every quote and agent. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five-page site outright for $1,500 one time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, and the AI receptionist books the inspection and leaves the inspection itself and the report entirely to you. A free audit is the place to start, and it shows you exactly where your calls, quotes, and referrals are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a home inspection business?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Will the AI receptionist book an inspection around a closing date?",
         "That is what it is built for. It answers on the first ring, gets the property address, the type of inspection, and the closing or option date, and either books it on your calendar or texts you the details as a priority. It handles the phone and the scheduling only, and it leaves the inspection and the report to you."),
        ("Do I have to replace my report software?",
         "No. Top Shelf runs on your existing number and works alongside the inspection and report software you already use. It fills the gaps in answering calls, following up with agents and buyers, and getting found, and your number and client list stay yours and leave with you if you ever go."),
    ],
    "service_schema_name": "Business software and marketing for home inspectors",
    "cta_h2": "See what your inspection business is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, quotes, and referrals are slipping away, whether you work with us or not. No credit card, never a call center.",
}
