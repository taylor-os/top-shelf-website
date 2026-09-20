"""Pillar (trade hub) framing for ORTHODONTISTS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, orthodontic-specific framing prose that leads with an orthodontic practice's real
world (consult-driven case starts, a free consult that converts over weeks, big-ticket braces and
Invisalign cases, referring dentists), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "find the gap" / "slips away", never "leak". Medical ethics: the
AI receptionist does scheduling, financing questions you allow, and intake only, never clinical or
treatment advice; no treatment, smile, or outcome guarantee; caller information is handled with
HIPAA-aware discretion.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Orthodontists",
    "title": "Software and Marketing Built for Orthodontists | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing built for orthodontists: an AI receptionist that books free consults, a CRM that follows up until the case starts, and a site that ranks.",
    "answer": "Orthodontics runs on consults that convert to case starts over weeks, and each case runs eighteen to twenty-four months. A case is lost when a consult call hits voicemail or a family who wanted to think it over never hears back. Top Shelf fixes this: an AI receptionist, a CRM that nurtures every consult, and a site that ranks.",
    "faq_eyebrow": "orthodontists ask",
    "sections": [
        {"h2_html": "Where an orthodontic practice actually <em>loses cases</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An orthodontic practice does not lose a case on the quality of its work. It loses it in the weeks between the first call and the signed case start. When a parent researching braces calls in the evening or on a weekend, the front desk is often chairside seating a patient or handing over an archwire, so the call rings to voicemail and they book the office that answered. And a consult is rarely a same-day yes. A parent hears the plan, means to talk it over, wait for the insurance year, or line up the budget, then gets busy, and between a full clinic day nobody circles back. That maybe quietly becomes a case that starts somewhere else.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Both gaps are front-desk and follow-up work, and both are fixable. An <a href="ai-receptionist-for-orthodontists.html">AI receptionist</a> answers every call days, nights, and weekends, warmly handles the cost, insurance, and financing questions a parent asks first, and books the free consult or flags a broken bracket to your team. A <a href="crm-for-orthodontists.html">CRM</a> holds every unstarted consult and sends warm, timed check-ins that reassure a family payment plans make it doable, and steady <a href="marketing-for-orthodontists.html">local marketing</a> keeps you visible to searching families and the dentists who refer.</p>'},
        {"h2_html": "One system, not <em>scattered tools</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Consults go cold because the call, the follow-up, the reviews, and the website usually live in separate tools, and a chairside team has no time to stitch them together. Top Shelf is one connected system. The consult the receptionist books lands in the same CRM that runs the follow-up sequence and asks for a review when a case finishes, and your <a href="websites-seo-for-orthodontists.html">website and local SEO</a> get you ranking for braces, Invisalign, and orthodontist near me in the towns you serve. Because it is one system, a consult, its follow-up sequence, and the review after the case finishes are never scattered across separate tools. You keep your own number and your case records, and both stay yours if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that book consults and follow up until the case starts. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist handles scheduling, the financing questions you allow, and intake only, never clinical or treatment advice. A free audit shows you exactly where consults and cases are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for an orthodontic practice?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom five page site is $1,500. There is no setup fee."),
        ("What does the AI receptionist say about cost and financing?",
         "Only what you allow. It answers the cost, insurance, and financing questions you set, books the free consult, and flags a broken bracket or real pain to your team. It handles scheduling and intake only and never gives clinical or treatment advice."),
        ("Can it follow up on a consult that did not start the same day?",
         "That is the point. Most orthodontic cases start weeks after the first visit, so the CRM holds every unstarted consult and sends warm, timed check-ins written to sound like your office, reassuring a family that payment plans make it manageable, so the case books with you instead of the office that stayed in touch."),
    ],
    "service_schema_name": "Business software and marketing for orthodontists",
    "cta_h2": "See what your orthodontic practice is <em>missing</em>",
    "cta_sub": "Get a free audit of where consults and cases are slipping away, whether you work with us or not. No credit card, never a call center.",
}
