"""Pillar (trade hub) framing for CHIROPRACTORS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file
owns ONLY the unique, chiropractor-specific framing prose that leads with a chiropractic office's
real world (new patients from a local search in pain, care plans, the visits that lapse), never a
template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "find the gap" / "slips away", never "leak". Medical ethics: the
AI receptionist does scheduling and intake only, never medical advice; no health, clinical, or
outcome claim; patient information is treated with the discretion a medical office is held to.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Chiropractors",
    "title": "Software and Marketing Built for Chiropractors | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing built for chiropractors: an AI receptionist that answers every call, a CRM that follows up on care plans, reviews, and a site that ranks.",
    "answer": "A chiropractic office lives on new patients and the visits a care plan should bring back. It loses them when a call goes unanswered or a patient who felt better is never followed up. Top Shelf fixes both for chiropractors: an AI receptionist that books every call, a CRM that follows up, plus booking, reviews, and a site that ranks.",
    "faq_eyebrow": "chiropractors ask",
    "sections": [
        {"h2_html": "Where a chiropractic office actually <em>loses new patients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A chiropractic office rarely loses a patient on price. It loses them in the small gaps around a hands-full day. When the phone rings you are mid-adjustment and the front desk is rooming the next patient or checking someone out, so a person whose back just gave out reaches voicemail and calls the next chiropractor on the list. A first-timer who never gets a call back is a whole care plan gone, not one visit. And the patient who started feeling better at visit six, meant to book the next one, and quietly drifted is revenue you already earned slipping away.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf is built to close those gaps one at a time. An <a href="ai-receptionist-for-chiropractors.html">AI receptionist</a> answers every call on the first ring, screens what brings the caller in, and books the new-patient exam or routes it to your team, sticking to scheduling and never giving medical advice. A <a href="crm-for-chiropractors.html">CRM</a> keeps every lead and care plan in front of you and sends the recall and check-in reminders that bring a lapsed patient back. And because most new patients start with a search in a moment of pain, a site that ranks and steady <a href="marketing-for-chiropractors.html">local marketing</a> are what put you in front of them before they scroll to someone else.</p>'},
        {"h2_html": "One system, not a <em>stack of logins</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason all of that falls through is that it usually lives in five different tools, and no one caring for patients all day has time to run five tools between visits. Top Shelf is one connected system instead. The call the receptionist books lands in the same CRM that fires the recall reminder and the review request the moment a visit is done, and your <a href="websites-seo-for-chiropractors.html">website and local SEO</a> feed the whole thing by getting you found in the map pack where the calls actually start. You keep your own number and your own patient list, and both stay yours if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and every care plan. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist books and answers front-desk questions only, never medical advice, handing anything clinical to your team. A free audit is the place to start, and it shows you exactly where calls, follow-ups, and new patients are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a chiropractic office?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom five page site is $1,500. There is no setup fee."),
        ("Will the AI receptionist give patients any medical advice?",
         "No. It handles scheduling and intake only. It answers on the first ring, asks what brings the caller in, and books the new-patient exam or routes the call to your team, and it hands anything clinical straight to a person. It is upfront that it is an assistant, and it never offers medical advice."),
        ("Do I have to replace the software I already use?",
         "No. Top Shelf runs on your existing phone number and fills the gaps in answering calls, following up on care plans, and getting found. Your charting or EHR keeps the clinical record, and your number and patient list stay yours and leave with you if you ever go."),
    ],
    "service_schema_name": "Business software and marketing for chiropractors",
    "cta_h2": "See what your chiropractic office is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, follow-ups, and new patients are slipping away, whether you work with us or not. No credit card, never a call center.",
}
