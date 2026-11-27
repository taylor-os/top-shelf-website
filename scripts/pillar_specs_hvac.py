"""Pillar (trade hub) framing for HVAC COMPANIES. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file
owns ONLY the unique, HVAC-specific framing prose that leads with the HVAC owner's real world
(weather-driven surges, no-cool and no-heat emergencies, the maintenance base), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge
instead of overpromise; only the real prices ($99/$199 Signature plan, $499 website) ever appear; no em/en dashes anywhere; "slips away" / "goes cold" / "find the gap", never
"leak" as a money metaphor.
"""

PILLAR = {
    "h1": "Software and Websites Built for HVAC Companies",
    "title": "Software and Websites Built for HVAC Companies | Top Shelf Business Solutions",
    "meta_desc": "Software and websites for HVAC companies: an AI receptionist for the heat-wave rush, a CRM for your maintenance base, plus booking, reviews, and a site built so Google can read it.",
    "answer": "HVAC lives and dies by the weather. The first ninety degree week sends every failing AC calling at once, your techs are already on roofs, and the overflow rolls to voicemail while a sweating homeowner dials the next company. Top Shelf answers those calls, chases the replacement quotes people sit on, and books the tune-ups that carry your slow months.",
    "faq_eyebrow": "HVAC owners ask",
    "sections": [
        {"h2_html": "Where an HVAC company <em>loses the jobs it earned</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An HVAC company does not lose most of its jobs to a competitor with a better price. It loses them in bursts, at the worst possible moments. The first heat wave crosses ninety and every marginal system in town gives up in the same two days, so the calls stack three deep while one person in the office answers one line. A no-heat call comes in at ten at night and hits a voicemail box a scared homeowner will not use. The big system replacement you quoted goes quiet for a month, because a new furnace is a decision people finance and sleep on, and the tune-up customer you never followed up on renews with nobody at all.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf plugs each of those holes. An <a href="ai-receptionist-for-hvac-companies.html">AI receptionist</a> answers every call at once during the surge and around the clock after hours, sorts a no-cool emergency from a routine question, and books it in your name. A <a href="crm-for-hvac-companies.html">CRM</a> holds every maintenance member and renewal date and keeps your plan base from quietly shrinking. <a href="online-booking-for-hvac-companies.html">Online booking</a> lets a tune-up claim a real slot with the confirmations and reminders that cut no-shows, and <a href="automation-for-hvac-companies.html">automation</a> keeps every unsold replacement estimate warm with a check-in and a financing nudge until the customer is ready.</p>'''},
        {"h2_html": "One platform instead of a <em>patchwork of apps</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most shops run the answering service, the scheduler, the review tool, and the website as four disconnected things, and the seams between them are where jobs fall out. Top Shelf is one platform instead. The call the receptionist books lands in the same CRM that fires the reminder before the visit and the <a href="review-software-for-hvac-companies.html">review request</a> the moment the job is closed, while the house is comfortable again and the customer is glad they called you. Your <a href="websites-seo-for-hvac-companies.html">website</a> sends every AC and furnace request into the same CRM. You keep your own number and your own customer list.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps the money side simple. The Signature plan, $99 a month for up to 10 users, includes the AI receptionist and the CRM that follow up on every call and quote. A professional website is $499 one time, and you do not need a plan to buy one. There is no setup fee on any of it. No honest company can promise a specific ranking by a specific date, because nobody controls Google, and the AI receptionist hands a true no-heat or no-cool emergency straight to you rather than pretending to handle it.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for an HVAC company?",
         "The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM. A professional website is $499 one time. There is no setup fee."),
        ("Can the AI receptionist handle a heat wave and a no-heat night?",
         "Yes. It answers every call at once, so ten calls in a hot hour each get picked up on the first ring instead of stacking in voicemail, and it works around the clock for the after-hours no-heat calls. It sorts a real emergency from a routine question and flags the urgent ones straight to you."),
        ("Do I have to switch my phone number or my tools?",
         "No. Top Shelf runs on your existing number and is built around how an HVAC shop already works. It fills the gaps in answering the surge, following up on replacement quotes, and holding your maintenance base, and your number and customer list stay yours."),
    ],
    "service_schema_name": "Business software and websites for HVAC companies",
    "cta_h2": "See what your HVAC company is <em>missing</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
}
