"""Pillar (trade hub) framing for PAINTERS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file
owns ONLY the unique, painter-specific framing prose that leads with the painter's real world
(a planned, big-ticket repaint decided over weeks, three estimates lined up, the job that slips
between the walkthrough and the signature), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge
instead of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time
site) ever appear; no em/en dashes anywhere; "slips away" / "goes cold" / "find the gap", never
"leak" as a money metaphor.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Painters",
    "title": "Software and Marketing Built for Painters | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for painters: an AI receptionist that answers every call, a CRM that keeps every estimate warm, plus booking, reviews, and a ranking site.",
    "answer": "A repaint is planned for months. A homeowner lines up three estimates, then sits on the choice while they save up or wait for dry weather, and hires whoever stayed in touch. The job slips in the quiet between the walkthrough and the signature. Top Shelf answers the estimate calls, keeps every quote warm, and books the walkthroughs.",
    "faq_eyebrow": "painters ask",
    "sections": [
        {"h2_html": "Where a painting company <em>loses the estimate</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Painting is a planned, big-ticket purchase, not a two in the morning emergency, so a painter loses jobs in a slower, quieter way. The estimate call rings while you are on a ladder cutting in a ceiling or spraying cabinets, it hits voicemail, and a homeowner lining up three painters does not wait, they book the first one who picks up and agrees to come look. Then the quote itself goes cold. You spend an hour measuring rooms and talking through colors and prep, leave a careful number, and it sits on the kitchen counter next to two others while the homeowner waits for dry weather or a free weekend. Weeks later the job goes to whoever stayed in touch, and a cold estimate is a deposit that never landed.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps you in the running the whole time they decide. An <a href="ai-receptionist-for-painters.html">AI receptionist</a> answers every call on the first ring while your hands are full, qualifies the repaint, interior or exterior, how many rooms, cabinets or trim, and books the walkthrough. A <a href="crm-for-painters.html">CRM</a> keeps every open estimate in front of you and stores the colors and sheens you used, so a touch-up or a matching repaint years later is easy to win. <a href="online-booking-for-painters.html">Online booking</a> lets a routine estimate schedule itself, and <a href="automation-for-painters.html">automation</a> puts each quote on its own timeline with painter-timed nudges, a check-in after the walkthrough and a reminder when exterior season opens, so the big jobs stay alive.</p>'''},
        {"h2_html": "One connected system, not <em>scattered tools</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Split across four tools, the follow-up is the first thing to drop, and follow-up is the whole game in painting. Top Shelf is one connected system instead. The walkthrough the receptionist books lands in the same CRM that fires the reminder before the visit and the <a href="review-software-for-painters.html">review request</a> at the reveal, the moment the last coat dries and the room looks new. Painting is one of the few trades where the proof fits in a photo, so a nudge to attach a before-and-after builds a portfolio on your listing you never had to stage. Your <a href="websites-seo-for-painters.html">website and SEO</a> rank you for the towns you cover and show the real before-and-after work that sells painting on sight, and your <a href="marketing-for-painters.html">marketing</a> makes you the familiar name a homeowner already trusts before the repaint they put off finally becomes this weekend. Your number and quotes stay yours.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is simple to read. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and estimate. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and every lead and quote stays yours. A free audit shows you where your estimates are quietly going cold, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a painting company?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("How long should I keep following up on a painting estimate?",
         "Longer than most painters do. Because the decision runs slow, an exterior quote from the spring may not book until summer and an interior can wait for a free weekend, so a real estimate is worth a nudge for weeks. Automation keeps it warm on its own timeline, so a quiet quote does not mean a lost one."),
        ("Do I have to replace the tools I already use?",
         "No. Top Shelf runs on your existing phone number and is built around how a painting business already works. It fills the gaps in answering estimate calls, following up on quotes, and getting found, and your number and quotes stay yours and leave with you if you ever go."),
    ],
    "service_schema_name": "Business software and marketing for painters",
    "cta_h2": "See what your painting company is <em>missing</em>",
    "cta_sub": "Get a free audit of where estimates and jobs are slipping away, whether you work with us or not. No credit card, never a call center.",
}
