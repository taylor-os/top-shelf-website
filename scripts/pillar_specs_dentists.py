"""Pillar (trade hub) framing for DENTISTS. generate_pillars.py owns the mechanics (shell, schema,
the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns ONLY the
unique, dentist-specific framing prose that leads with a dental practice's real world (the
new-patient phone call decided in a minute, the recall and rebooking that fill the chair), never a
template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "find the gap" / "slips away", never "leak". Medical ethics: the
AI receptionist does scheduling and intake only, never dental or medical advice; no health,
clinical, or outcome claim; patient information is treated with the discretion a dental office is
held to (HIPAA-aware).
"""

PILLAR = {
    "h1": "Software and Marketing Built for Dentists",
    "title": "Software and Marketing Built for Dentists | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing built for dentists: an AI receptionist that answers every call, a CRM that fills the recall list, reviews, and a site that ranks.",
    "answer": "For a dental office a new patient decides in a minute on the phone, and the chair fills on recall and rebooking. You lose ground when a call hits voicemail, an overdue cleaning is never reminded, or accepted treatment is never booked. Top Shelf fixes the dental front desk: an AI receptionist, a CRM, reviews, and a site that ranks.",
    "faq_eyebrow": "dentists ask",
    "sections": [
        {"h2_html": "Where a dental practice actually <em>loses new patients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A dental practice rarely loses a patient on the quality of the work. It loses them in the first minute, on the phone, and on the follow-up that never goes out. A new patient comparing two or three offices found you on a phone, and if the call rings while your front desk is chairside, verifying benefits, or checking someone out, they do not leave a voicemail. They call the next office and book where someone picked up. The insurance question they wanted answered goes unanswered, and a first-time patient worth years of cleanings, fillings, and referrals is gone before you knew they called.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The schedule also thins from the inside. A patient overdue for a cleaning who never got a reminder, an accepted crown that was never scheduled, a canceled hygiene visit nobody rebooked: each is production you already earned quietly slipping away. Top Shelf closes those gaps. An <a href="ai-receptionist-for-dentists.html">AI receptionist</a> answers every call day or night, handles the insurance and scheduling questions, and books the visit or flags an urgent one to your team. A <a href="crm-for-dentists.html">CRM</a> works your recall list and follows up on unscheduled treatment, and steady <a href="marketing-for-dentists.html">local marketing</a> keeps you in the map pack where new patients start.</p>'},
        {"h2_html": "One system, not a <em>drawer of logins</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most of this slips because it lives in separate tools that do not talk, and a busy front desk cannot run all of them between patients. Top Shelf is one connected system. The call the receptionist books lands in the same CRM that fires the six-month recall and the review request the moment a visit is marked done, and your <a href="websites-seo-for-dentists.html">website and local SEO</a> feed it by getting you found where people search for a dentist near them. Nothing waits on a busy person to remember it, and nothing falls between two apps that were never meant to share a patient. Patient information is handled with the discretion a dental office is held to, and your number and patient list stay yours if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that fill the recall list and follow up on every call. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist sticks to scheduling and intake and never gives dental or medical advice. A free audit shows you exactly where calls, recalls, and new patients are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a dental practice?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom five page site is $1,500. There is no setup fee."),
        ("Does the AI receptionist handle insurance questions without giving advice?",
         "Yes. It answers the scheduling and coverage questions you tell it to, whether you take a caller's plan and what a first visit involves, and books the appointment. It sticks to scheduling and intake, hands anything clinical or urgent to your team, and never gives dental or medical advice."),
        ("Do we have to replace our practice management software?",
         "No. Top Shelf runs on your existing phone number and sits alongside the software you chart in. Your practice management system keeps the clinical record, while Top Shelf fills the gaps in answering calls, working the recall list, and getting found. Your number and patient list stay yours."),
    ],
    "service_schema_name": "Business software and marketing for dentists",
    "cta_h2": "See what your dental practice is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, recalls, and new patients are slipping away, whether you work with us or not. No credit card, never a call center.",
}
