"""Pillar (trade hub) framing for CRIMINAL DEFENSE LAWYERS. generate_pillars.py owns the mechanics
(shell, schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This
file owns ONLY the unique, criminal-defense-specific framing prose that leads with the firm's real
intake world (the after-hours arrest call a frightened family retains on the spot, the caller who
must be reached before the court date), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, clients, or results;
hedge instead of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time
site) ever appear; no em/en dashes anywhere; "slips away" / "goes cold", never "leak". Attorney-
advertising ethics: no promised acquittal, outcome, or ranking; the AI receptionist does intake,
booking, and follow-up only, never legal advice and never discusses the charge; Top Shelf captures
and books the intake call, it never touches the legal matter.
"""

PILLAR = {
    "h1": "Criminal Defense Law Firm Software and Marketing",
    "title": "Criminal Defense Law Firm Software and Marketing | Top Shelf Business Solutions",
    "meta_desc": "Criminal defense law firm software and marketing. An AI receptionist answers every after-hours arrest call, a CRM follows up before court, plus websites and SEO.",
    "answer": "An arrest comes at night or on a weekend, and a frightened family with someone in jail does not leave a voicemail. They call the next firm until one answers. Top Shelf puts intake in one place: an AI receptionist that answers 24/7 and stays calm, a CRM that follows up before the court date, plus online booking and reviews.",
    "faq_eyebrow": "defense lawyers ask",
    "sections": [
        {"h2_html": "Where a criminal defense firm <em>loses clients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Criminal work does not keep office hours. Arrests spike at night, on weekends, and on holidays, which is exactly when you are in trial prep, at a jail meeting with another client, or asleep, and none of those are moments you can stop and take a call. A frightened family calling from a jail parking lot does not leave a voicemail and wait until morning. They keep dialing down the list until a real person picks up, and by the time you see the missed call, the case has retained somewhere else. The after-hours calls most likely to roll to voicemail, the DWI, the domestic, the weekend booking, are frequently the cases that can carry your firm for months.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The other place cases slip away is before the court date. A caller who has not retained yet is usually gathering a retainer or calling two other firms, and retains whoever circles back in time. Top Shelf closes both gaps. An <a href="ai-receptionist-for-criminal-defense-lawyers.html">AI receptionist</a> answers every call on the first ring, day or night, stays calm with a panicked family, captures the charge, county, and custody status, and books the consultation or flags a true emergency to your on-call attorney. A <a href="crm-for-criminal-defense-lawyers.html">CRM</a> keeps every unretained caller in front of you and sends timed check-ins tied to the court date. Both handle intake, booking, and follow-up only. Neither gives legal advice or discusses the charge, and your attorneys make every decision on the case.</p>'},
        {"h2_html": "One connected system, not a <em>pile of apps</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason cases slip is that the phone, the follow-up, the site, and the reviews usually live in four disconnected places, and a defense lawyer does not have time to run four tools between hearings. Top Shelf is one connected system instead. The after-hours call the receptionist books lands in the same CRM that follows up before the setting, and your <a href="websites-seo-for-criminal-defense-lawyers.html">website and local SEO</a> feed it by getting you into the map pack, where a frightened person searches for a lawyer at midnight. Your <a href="marketing-for-criminal-defense-lawyers.html">marketing</a> keeps genuine reviews growing, because trust is the whole decision for someone handing their freedom to a stranger. You keep your own number and your own client list, and both leave with you if you ever go.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that answer and follow up on every call. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and no honest firm can promise an acquittal or any case result. A free audit is the place to start: it shows you exactly where after-hours calls and unretained callers are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a criminal defense firm?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM that run intake and follow-up. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Will it really answer the 2am arrest call?",
         "Yes, and that is often your best case. It answers 24/7 as part of the plan, stays calm with a frightened family, captures the charge, county, and custody status, and books the consultation or flags a true emergency to your on-call attorney, so the weekend booking does not roll to voicemail. There is no after-hours surcharge."),
        ("Does the AI receptionist give legal advice or discuss the charge?",
         "No. It answers, reassures, gathers the facts your intake needs, and books or routes the call. It is upfront that it is an assistant, not a person, and it never gives legal advice, never discusses the charge, and never promises a result. Your attorneys make every legal decision."),
    ],
    "service_schema_name": "Business software and marketing for criminal defense law firms",
    "cta_h2": "See what your firm is <em>missing</em> after hours",
    "cta_sub": "Get a free audit of where after-hours calls and unretained callers are slipping away, whether you work with us or not. No credit card, never a call center.",
}
