"""Pillar (trade hub) framing for HOUSE CLEANING COMPANIES. generate_pillars.py owns the mechanics
(shell, schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This
file owns ONLY the unique, cleaning-specific framing prose that leads with the cleaning owner's
real world (recurring-route revenue, converting a one-time clean into a standing client, keeping
a route from churning), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge
instead of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time
site) ever appear; no em/en dashes anywhere; "slips away" / "goes cold" / "find the gap" (cleaning
has no literal leaks, so the word never appears).
"""

PILLAR = {
    "h1": "Software and Marketing Built for House Cleaning Companies",
    "title": "Software and Marketing Built for House Cleaning Companies | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for house cleaning companies: an AI receptionist, a CRM that turns cleans into recurring clients, plus booking, reviews, and SEO.",
    "answer": "A cleaning company does not get rich on any single clean. It gets rich on the weekly client kept for years. The money is won when a one-time or move-out clean becomes a standing route, and lost when a call hits voicemail or a recurring client drifts. Top Shelf answers the call and follows up to make it recurring.",
    "faq_eyebrow": "cleaning owners ask",
    "sections": [
        {"h2_html": "Where a cleaning company <em>loses the recurring client</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For a cleaning company the real money is not any one clean, it is the client who stays on your route for years, so the losses that hurt are the ones that cost you that standing revenue. A call comes in while your crews are inside a home with a vacuum running, it hits voicemail, and a homeowner ready to hire does not leave a message, they book the next cleaner on Google, and a weekly client worth years of work is gone. A one-time deep clean or a move-out ends without anyone asking the customer to go on a schedule, so it stays a single payment. And a recurring client who forgot a cleaning day, or whose gate code changed, becomes a locked-out trip that still costs you a paid crew.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps each of those clients from slipping. An <a href="ai-receptionist-for-house-cleaning-companies.html">AI receptionist</a> answers every call while your crews are cleaning, gathers the home size, frequency, and type of clean a quote needs, and books it. A <a href="crm-for-house-cleaning-companies.html">CRM</a> holds every recurring route, gate code, and pet note and flags a weekly client who has gone quiet before they churn. <a href="online-booking-for-house-cleaning-companies.html">Online booking</a> lets a client claim a one-time clean or lock in a recurring slot on your real availability, and <a href="automation-for-house-cleaning-companies.html">automation</a> follows up after a one-time clean to offer a weekly or biweekly plan and sends the confirmations and on-the-way texts that keep a crew from arriving to a locked door.</p>'''},
        {"h2_html": "One system that holds the <em>whole route</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Stitched together from four separate tools, none of this holds, because the follow-up that turns a clean into a standing client is the first thing to fall on a busy week. Top Shelf is one system instead. The clean the receptionist books lands in the same CRM that fires the recurring offer a day or two later, while the house still feels spotless, and the <a href="review-software-for-house-cleaning-companies.html">review request</a> right after the visit. Reviews matter more here than almost anywhere, because a homeowner is deciding whether to hand a crew a key, and a wall of recent ones is what earns that. Your <a href="websites-seo-for-house-cleaning-companies.html">website and SEO</a> get you found in the neighborhoods you already serve, so your routes stay tight, and your <a href="marketing-for-house-cleaning-companies.html">marketing</a> keeps you the trusted, well-reviewed name in the map pack. Your client list stays yours.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The plans are flat and clear. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and clean. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it, and no per-call meter, so a busy month does not run up the bill. No honest company can promise a specific ranking by a specific date, because nobody controls Google. A free audit shows you where recurring clients are slipping away, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a cleaning company?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Can clients book a recurring clean online, not just a one-time?",
         "Yes, and that is the point for a cleaning business. A client can lock in a weekly, biweekly, or monthly slot in one booking, so you fill a standing spot on your route instead of a single visit, and it repeats on the schedule they chose. The booking reads your real calendar, so it never double-books a crew."),
        ("Do I keep my client list?",
         "Yes. Every client, home detail, and recurring schedule is in your name and exportable any time. The point is to make the list you already built produce steady work, not to lock it inside software you only rent."),
    ],
    "service_schema_name": "Business software and marketing for house cleaning companies",
    "cta_h2": "See what your cleaning company is <em>missing</em>",
    "cta_sub": "Get a free audit of where recurring clients and jobs are slipping away, whether you work with us or not. No credit card, never a call center.",
}
