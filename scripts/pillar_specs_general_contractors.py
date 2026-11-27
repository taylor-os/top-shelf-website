"""Pillar (trade hub) framing for GENERAL CONTRACTORS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, general-contractor-specific framing prose that makes the pillar non-thin and leads
with the long project bid cycle, never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($99/$199 Signature plan, $499 website) ever
appear, and no project prices are ever invented; no em/en dashes anywhere; "slips away" / "goes
cold", never "leak" as a metaphor. The AI does intake and scheduling only, it never quotes a price
or binds a bid.
"""

PILLAR = {
    "h1": "Software and Websites Built for General Contractors",
    "title": "Software and Websites Built for General Contractors | Top Shelf Business Solutions",
    "meta_desc": "Software and websites for general contractors: an AI receptionist that captures the scope, a CRM that follows up on every bid, and a site that shows your projects.",
    "answer": "General contracting is a long-cycle, high-trust sale. A homeowner planning a kitchen remodel or an addition lines up three or four builders, weighs the bids for weeks, and hands the job to whoever answered and stayed in touch. Top Shelf answers every project call from the job site, follows up on every bid, and shows your finished work.",
    "faq_eyebrow": "general contractors ask",
    "sections": [
        {"h2_html": "Where a general contractor actually <em>loses work</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A general contractor does not lose a small service ticket, you lose a whole remodel or addition to whoever answered. The calls come while you are walking a framing crew through a change, coordinating a sub who showed up late, meeting an inspector, or pricing the next job from the truck, and a homeowner about to spend a large sum lines up three or four builders and leans toward the one who picks up and sounds organized. Those inquiries also tend to land in the evenings and on weekends, when people finally sit down to research a remodel, which is exactly when a call rolls to voicemail. Then the bids you do send go cold slowly, over the weeks a homeowner weighs two or three numbers, talks it over, and lines up financing, and the project goes to whoever stayed in front of them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps. An <a href="ai-receptionist-for-general-contractors.html">AI receptionist</a> answers on the first ring day or night, asks what the homeowner wants built, roughly when, and whether they have plans or a budget, then books the consult on your calendar or hands you a qualified lead. A <a href="crm-for-general-contractors.html">CRM</a> keeps every open bid in front of you and sends timed check-ins across the weeks a homeowner takes to decide, so the buyer comparing three contractors keeps hearing from you while the others go quiet, and it keeps your past clients and referral sources, the designers, architects, and agents who send you work, warm. It never quotes a price or binds a bid, you always set the scope and the number yourself.</p>'},
        {"h2_html": "One system, not a <em>truck console full of apps</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">All of that slips away because it usually lives in a truck console full of separate apps, and a builder running three active sites cannot keep up with them by hand. Top Shelf is one connected system instead. The consult the receptionist books lands in the same CRM that follows up until the contract is signed and keeps the referral sources warm after it is. Your <a href="websites-seo-for-general-contractors.html">website</a> shows a portfolio of finished kitchens, additions, and whole-home renovations and proof you are licensed and insured, because most remodels are still won on trust. You keep your own number and your own client list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Signature plan, $99 a month for up to 10 users, includes the AI receptionist and the CRM that follow up on every project call and every open bid. A professional website is $499 one time, and you do not need a plan to buy one. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the receptionist handles intake and scheduling only, it never quotes a price or binds a bid, you set the scope yourself.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a general contractor?",
         "The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM. A professional website is $499 one time. There is no setup fee."),
        ("Can it price a job or commit me to a bid?",
         "No, and that is on purpose. It captures what a consult needs, what they want built, roughly when, and whether they have plans or a budget, then books the appointment or hands you the lead. You still walk the project and set the scope and the price yourself, so nothing is quoted or promised in your name."),
        ("Do I have to replace the tools I already use?",
         "No. Top Shelf runs on your existing phone number and is built around how a general contractor already works. It fills the gaps in answering project calls, following up on bids, and getting found, and your number and client list stay yours and leave with you if you ever go."),
    ],
    "service_schema_name": "Business software and websites for general contractors",
    "cta_h2": "See what your contracting business is <em>missing</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
}
