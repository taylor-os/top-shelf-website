"""Pillar (trade hub) framing for ELECTRICIANS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file
owns ONLY the unique, electrician-specific framing prose that leads with the electrician's real
world (a considered panel/generator quote, both hands inside a live panel), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge
instead of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time
site) ever appear; no em/en dashes anywhere; "slips away" / "goes cold" / "find the gap", never
"leak" as a money metaphor.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Electricians",
    "title": "Software and Marketing Built for Electricians | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for electricians: an AI receptionist that answers every call, a CRM that chases every quote, plus booking, reviews, and a ranking site.",
    "answer": "An electrician wins the big work, panel upgrades and generator installs, on a quote a homeowner sits on for weeks, and loses the rest to a phone that rings while both hands are inside a live panel. Top Shelf puts it in one place: an AI receptionist, a CRM that chases every quote, booking, reviews, and a ranking site.",
    "faq_eyebrow": "electricians ask",
    "sections": [
        {"h2_html": "Where an electrical business actually <em>loses work</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An electrical business almost never loses on skill. It loses in the quiet gaps around the work. The call about a tripped panel or a dead outlet comes in while you are up a ladder or wrist deep in a junction box, so it rolls to voicemail, and a homeowner with no power in half the house dials the next electrician instead of waiting for a callback. The panel upgrade you quoted last week goes quiet too, and not because the number was wrong. A service upgrade is a considered purchase people sit on for weeks while they gather two more bids, and the job goes to whoever stayed in front of them, not the electrician who quoted first and then went silent.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf is built to close those gaps one at a time. An <a href="ai-receptionist-for-electricians.html">AI receptionist</a> answers every call the moment it rings, tells a dead panel from planned work, and texts you the details before you are off the ladder. A <a href="crm-for-electricians.html">CRM</a> keeps every open estimate in front of you and follows up on the upgrades, rewires, and generator installs that take weeks to decide. <a href="online-booking-for-electricians.html">Online booking</a> lets an inspection or an EV charger install schedule itself on your real availability, and <a href="automation-for-electricians.html">automation</a> sends the invoice the moment a job is marked done, so your cash stops waiting on a free evening that never comes.</p>'''},
        {"h2_html": "One connected system, not <em>five separate logins</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason all of that slips is that it usually lives in five different apps, and no electrician has time to run five tools between service calls. Top Shelf is one connected system instead. The call the receptionist books lands in the same CRM that fires the reminder before the appointment and the <a href="review-software-for-electricians.html">review request</a> the moment the job is closed, while the customer is still glad the power is back on. Your <a href="websites-seo-for-electricians.html">website and local SEO</a> feed the whole thing by getting you found when a homeowner searches for an electrician near them, and your <a href="marketing-for-electricians.html">marketing</a> keeps your profile active and points demand toward the panel and generator work you actually want more of. You keep your own number and your own customer list, and both leave with you if you ever go.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and quote. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist hands a real emergency straight to you rather than pretending to handle it. A free audit shows you where your calls, quotes, and jobs are slipping away, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for an electrical business?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Will the AI receptionist handle a real electrical emergency?",
         "It triages the way you would. It answers on the first ring, asks whether there is power, a burning smell, or anything sparking, gets the address, and either books the planned work or flags a true emergency straight to your phone so you decide whether to roll a truck. It is upfront that it is an assistant, not a person, and never pretends to fix a hazard on its own."),
        ("Do I have to replace the tools I already use?",
         "No. Top Shelf runs on your existing phone number and fits how an electrical business already works. It fills the gaps in answering calls, following up on quotes, and getting found, and your number and customer list stay yours and leave with you if you ever go."),
    ],
    "service_schema_name": "Business software and marketing for electricians",
    "cta_h2": "See what your electrical business is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, quotes, and jobs are slipping away, whether you work with us or not. No credit card, never a call center.",
}
