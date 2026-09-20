"""Pillar (trade hub) framing for PERSONAL INJURY LAWYERS. generate_pillars.py owns the mechanics
(shell, schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This
file owns ONLY the unique, personal-injury-specific framing prose that leads with the firm's real
intake world (the speed-to-lead race after a wreck, the contingency case that signs with whoever
answers first), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, clients, settlements, or
results; hedge instead of overpromise; only the real prices ($299/$899/$2,500 monthly plans,
$1,500 one-time site) ever appear; no em/en dashes anywhere; "slips away" / "goes cold", never
"leak". Attorney-advertising ethics: no promised outcome, settlement, verdict, or ranking; the AI
receptionist does intake, booking, and follow-up only, never legal advice and never evaluates a
case; Top Shelf captures and books the intake call, it never touches the legal matter.
"""

PILLAR = {
    "h1": "Personal Injury Law Firm Software and Marketing",
    "title": "Personal Injury Law Firm Software and Marketing | Top Shelf Business Solutions",
    "meta_desc": "Personal injury law firm software and marketing. An AI receptionist answers every accident call, a CRM follows up on every intake, plus websites, SEO, and reviews.",
    "answer": "After a wreck, an accident victim signs with whoever answers first, so a personal injury firm wins or loses the client in the minutes after the call. Top Shelf puts intake in one place: an AI receptionist that answers every accident call, a CRM that follows up on every lead, online booking, reviews, and a site built to rank.",
    "faq_eyebrow": "injury lawyers ask",
    "sections": [
        {"h2_html": "Where a personal injury firm actually <em>loses cases</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A personal injury firm rarely loses a potential client on price. It loses them in the minutes between someone being hurt and someone at your firm being free to pick up. You are in a hearing, in a deposition, or asleep at two in the morning when a person calls from a hospital bed or a body shop, still shaken, and that caller does not leave a voicemail. They move down the list until a real person answers, and the client signs somewhere else. The calls most likely to roll to voicemail, the nights and the weekends, are also the serious wrecks worth the most to your firm.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The other place cases slip away is after the first contact. A person weighing two or three firms after a crash often goes quiet, not because they picked someone else on the spot, but because nobody followed up while they waited on the insurance offer. Top Shelf is built to close both gaps. An <a href="ai-receptionist-for-personal-injury-lawyers.html">AI receptionist</a> answers every accident call day or night, runs the intake a case needs, and books the consultation or flags a true emergency to your on-call attorney. A <a href="crm-for-personal-injury-lawyers.html">CRM</a> keeps every open intake in front of you and sends the timed check-ins that keep a maybe from going cold. Both do intake, booking, and follow-up only. Neither gives legal advice or evaluates a claim, and your attorneys make every decision about the matter.</p>'},
        {"h2_html": "One connected system, not a <em>stack of logins</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason intake slips is that it usually lives in five disconnected places, and a trial lawyer does not have time to run five tools between hearings. Top Shelf is one connected system instead. The accident call the receptionist books lands in the same CRM that fires the follow-up, and your <a href="websites-seo-for-personal-injury-lawyers.html">website and local SEO</a> feed the whole thing by getting you into the map pack, where an injury search actually starts, ahead of firms with far bigger ad budgets. Your <a href="marketing-for-personal-injury-lawyers.html">marketing</a> keeps genuine reviews growing and the pipeline full. You keep your own number and your own client list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that answer and follow up on every intake. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and no honest firm can promise a settlement, a verdict, or any case result. A free audit is the place to start: it shows you exactly where accident calls and intakes are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a personal injury firm?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM that run intake and follow-up. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Does the AI receptionist give callers legal advice about their accident?",
         "No. It answers every call, gathers the facts a case needs, and books the consultation or flags a true emergency to your on-call attorney. It is upfront that it is an assistant, not a person, and it never gives legal advice or evaluates a claim. Your attorneys make every legal decision."),
        ("Can it really capture a serious wreck that comes in at night or on a weekend?",
         "Yes, and those are often the calls worth the most. It answers 24/7 as part of the plan, runs the intake, and books the consultation or routes a true emergency, so the accident that comes in at midnight does not roll to voicemail while another firm picks up. There is no after-hours surcharge."),
    ],
    "service_schema_name": "Business software and marketing for personal injury law firms",
    "cta_h2": "See the cases your firm is <em>missing</em>",
    "cta_sub": "Get a free audit of where accident calls and intakes are slipping away, whether you work with us or not. No credit card, never a call center.",
}
