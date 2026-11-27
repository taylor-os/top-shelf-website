"""Pillar (trade hub) framing for OPTOMETRISTS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, optometry-specific framing prose that leads with the optometry practice's real
world (two storefronts in one, the eye exam plus the retail optical, annual recall and contact-lens
reorders, the vision-plan question), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($99/$199 Signature plan, $499 website) ever
appear; no em/en dashes anywhere; "find the gap" / "slips away", never "leak". Medical ethics: the
AI receptionist does scheduling, order status, and intake only, never eye-care or vision advice; no
health, clinical, or outcome claim; patient information is treated with the discretion a medical
office is held to (HIPAA-aware).
"""

PILLAR = {
    "h1": "Software and Websites Built for Optometrists",
    "title": "Software and Websites Built for Optometrists | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing built for optometrists: an AI receptionist that answers exam and eyewear calls, a CRM for annual recall and reorders, and a site built so Google can read it.",
    "answer": "An optometry practice makes its money twice from one patient, once for the eye exam and again at the optical, so a missed call loses both. Patients also drift when an annual recall or a contact-lens reorder is never sent. Top Shelf fixes the front desk: an AI receptionist, a CRM for recall and reorders, and a site built so Google can read it.",
    "faq_eyebrow": "optometrists ask",
    "sections": [
        {"h2_html": "Where an optometry practice actually <em>loses patients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Optometry is really two businesses on one floor, the eye exam in the back and a retail optical up front, and that is exactly where patients slip away. The person who answers the phone is usually on the optical floor fitting frames or checking a patient out, so when someone calls to book an exam, the call rings to voicemail and they book the next optometrist. What walks away is not one appointment. It is the exam, the glasses or contacts that ride on top of it, the vision benefits they were about to spend with you, and often the whole family.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The same money slips away from the patient list you already have. A patient whose annual exam is due, a contact-lens wearer about to run out, a shopper who priced a box against an online seller, each one drifts without a nudge. Top Shelf closes the gaps. An <a href="ai-receptionist-for-optometrists.html">AI receptionist</a> answers every call, handles the vision-plan and order-status questions, and books the exam, so nobody leaves the optical floor to pick up. A <a href="crm-for-optometrists.html">CRM</a> sends annual recall and reorder reminders before a wearer runs out.</p>'},
        {"h2_html": "One system, not <em>a phone and a spreadsheet</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Recalls slip and calls go to voicemail because answering, follow-up, reviews, and the website live in separate places, and one person cannot run the optical and all of them at once. Top Shelf connects them. The exam the receptionist books lands in the same CRM that sends next year\'s recall and the contact-lens reorder reminder, and your <a href="websites-seo-for-optometrists.html">website</a> merchandises the optical and sends its exam requests into the same place. Because it is one system, the exam, the eyewear order, and the annual recall sit on the same patient record instead of in three separate places. Patient information is handled with the discretion a medical office is held to, and your number and patient list stay yours if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Signature plan, $99 a month for up to 10 users, includes the AI receptionist and the CRM that answer the phone and work your recall and reorder list. A professional website is $499 one time, and you do not need a plan to buy one. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist sticks to scheduling, order status, and intake, never eye-care or vision advice.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for an optometry practice?",
         "The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM. A professional website is $499 one time. There is no setup fee."),
        ("Can it handle the are-my-glasses-ready calls that tie up my optical?",
         "Yes. Those routine order-status calls are exactly what it takes off your team. It can confirm whether an order of glasses or contacts is ready the way you tell it to, answer whether you take a caller's vision plan, and book the exam, so nobody leaves the optical floor to pick up. Anything unusual is handed to a person."),
        ("Does it give any eye-care advice?",
         "No. It handles scheduling, order status, and intake only. It books the exam, answers your vision-plan and hours questions, and flags an urgent eye problem to your team. It never offers eye-care or vision advice, and patient information is handled with a medical office's discretion."),
    ],
    "service_schema_name": "Business software and websites for optometrists",
    "cta_h2": "See what your optometry practice is <em>missing</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
}
