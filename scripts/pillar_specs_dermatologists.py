"""Pillar (trade hub) framing for DERMATOLOGISTS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, dermatology-specific framing prose that leads with a dermatology practice's real
world (a medical side and a cosmetic side at once, a new-patient waitlist weeks out, annual
skin-check recall), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "find the gap" / "slips away", never "leak". Medical ethics: the
AI receptionist does scheduling and intake only, never medical, cosmetic, or skin advice; no
health, clinical, or outcome claim; patient information is treated with the discretion a medical
office is held to (HIPAA-aware).
"""

PILLAR = {
    "h1": "Software and Marketing Built for Dermatologists",
    "title": "Software and Marketing Built for Dermatologists | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing built for dermatologists: an AI receptionist that answers every call, a CRM for skin-check recall and rebooking, and a site that ranks.",
    "answer": "A dermatology practice runs medical and cosmetic sides, with a new-patient waitlist weeks out and a front desk buried in insurance and referrals. New patients slip when a call hits voicemail, and rebookings slip when a recall never goes out. Top Shelf fixes the front desk: an AI receptionist, a CRM for recall and rebooking, and a site that ranks.",
    "faq_eyebrow": "dermatologists ask",
    "sections": [
        {"h2_html": "Where a dermatology practice actually <em>loses new patients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A dermatology practice loses patients in two places a template website never sees. The first is the phone. Your front desk is verifying insurance, chasing a referral, and working a waitlist that already runs weeks out, so when a new patient calls, whether it is a worried mole or a cosmetic consult, the call rings through to voicemail and they book the next dermatologist instead. The second is the rebooking that never goes out. A patient you told to come back for an annual skin check, or a cosmetic patient whose treatment has worn off, meant to return and drifted because no reminder reached them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Both are fixable, and both are front-desk work, not clinical work. An <a href="ai-receptionist-for-dermatologists.html">AI receptionist</a> answers every call on the first ring, day or night, sorts a medical visit from a cosmetic consult the way you tell it to, books it, and flags anything urgent to your team. A <a href="crm-for-dermatologists.html">CRM</a> holds every skin-check recall, recheck, and cosmetic maintenance date and sends the reminder for you. And because most new patients, medical and cosmetic, begin with a search, a site that ranks and steady <a href="marketing-for-dermatologists.html">local marketing</a> put you in front of them first.</p>'},
        {"h2_html": "One system, not <em>four disconnected tools</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason recalls go out late and calls reach voicemail is that answering, follow-up, reviews, and the website usually live in four places that do not talk to each other. Top Shelf connects them. The consult the receptionist books lands in the same CRM that sends the recall a year out and the review request after the visit, and your <a href="websites-seo-for-dermatologists.html">website and local SEO</a> get you found for the conditions and treatments you offer nearby. The whole thing runs on one patient record, so a cosmetic consult and a medical visit for the same person are never two disconnected files. Patient information is handled with the discretion a medical office is held to, and your number and patient list stay yours if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that sort and book calls and send every recall. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist handles scheduling and intake only, never medical, cosmetic, or skin advice. A free audit shows you exactly where calls, recalls, and new patients are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a dermatology practice?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom five page site is $1,500. There is no setup fee."),
        ("Can it tell a medical skin check from a cosmetic consult?",
         "Yes. It sorts the call the way you tell it to, books a medical visit or a cosmetic consult onto the right kind of appointment, and flags anything that sounds urgent by your rules to your team. It handles scheduling and intake only and leaves every clinical and cosmetic decision to your physicians."),
        ("Is patient information handled carefully?",
         "Yes. Top Shelf is built for the discretion a medical office is held to. It captures and books new-patient inquiries and sends the reminders you approve, and your patient list stays yours to export. It never gives medical advice and hands anything clinical to your team."),
    ],
    "service_schema_name": "Business software and marketing for dermatologists",
    "cta_h2": "See what your dermatology practice is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, recalls, and new patients are slipping away, whether you work with us or not. No credit card, never a call center.",
}
