"""Pillar (trade hub) framing for LOCKSMITHS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, locksmith-specific framing prose that makes the pillar non-thin and leads with the
lockout emergency and the commercial repeat accounts, never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear, and no locksmith service prices are invented; no em/en dashes anywhere; "slips away" / "goes
cold", never "leak" as a metaphor. The AI does intake, triage, scheduling, and an arrival window
only, it never binds a price, and nothing here promises security, because no lock or locksmith can
be guaranteed.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Locksmiths",
    "title": "Software and Marketing Built for Locksmiths | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for locksmiths: an AI receptionist that answers every lockout 24/7, a CRM that follows up on quotes and accounts, and a site that ranks.",
    "answer": "For a locksmith, speed to answer is everything. Someone stranded next to a car or shut out after dark phones down the list until a real person picks up, and books whoever answers first. Top Shelf answers every lockout 24/7, triages it, follows up on every rekey and commercial quote, and builds the reviews a trust purchase runs on.",
    "faq_eyebrow": "locksmiths ask",
    "sections": [
        {"h2_html": "Where a locksmith actually <em>loses jobs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Locksmithing is a two-hands trade, and the calls you miss are the ones worth the most. When the phone rings you are picking a lock, cutting a key, programming a fob, or working a safe, and a person stranded next to a car in a dark lot or shut out of the house after dark does not leave a voicemail, they phone down the list until someone picks up. Those after-hours lockouts are the highest-margin work you get, and they are exactly the ones most likely to roll to voicemail. The planned work slips a different way. A bid to rekey a house, change the locks on a business, or set up a master key goes quiet when the next lockout pulls you across town, and the property manager you let a tenant back in for once drifts to whoever stays in touch.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes both gaps. An <a href="ai-receptionist-for-locksmiths.html">AI receptionist</a> answers on the first ring day or night, tells a car lockout from a commercial rekey, gives a realistic arrival window, and books the job or flags a true emergency straight to your phone. A <a href="crm-for-locksmiths.html">CRM</a> keeps every open rekey and install quote in front of you and follows up on its own, so a customer comparing locksmiths keeps hearing from you while the others go quiet, and it keeps every commercial account, building, and keyway in one place so the turnover rekeys come back to you instead of drifting to whoever was free. It handles the intake and the scheduling and leaves the pricing to you.</p>'},
        {"h2_html": "One system, not a <em>ring of separate tools</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">All of that slips away because it usually lives in a ring of separate tools, and a locksmith with both hands on a lock cannot run them between jobs. Top Shelf is one connected system instead. The job the receptionist books lands in the same CRM that follows up on the quote and keeps the commercial account warm. Your <a href="websites-seo-for-locksmiths.html">website and local SEO</a> feed it by putting a tap-to-call button in front of a stranded searcher and ranking for locksmith near me and 24 hour locksmith, and your <a href="marketing-for-locksmiths.html">marketing</a> builds the recent reviews and the visible licensed, insured, and bonded trust signals a security purchase leans on harder than almost any trade. You keep your own number and your own customer list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist that answers every lockout and the CRM that follows up on every quote and account. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the receptionist triages and books and hands a true emergency straight to you, but it never sets a price, and no lock or locksmith can promise security, so we never pretend otherwise. A free audit is the place to start, and it shows you where your lockout calls and quotes are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a locksmith?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Will the AI receptionist handle a late-night lockout?",
         "It answers on the first ring, tells a car lockout from a routine rekey, gives a realistic arrival window, and books it, or flags a true emergency straight to your phone so you decide whether to roll out. It is upfront that it is an assistant, not a person, and it never sets a price."),
        ("Do I have to replace the tools I already use?",
         "No. Top Shelf runs on your existing phone number and is built around how a locksmith already works. It fills the gaps in answering lockouts, following up on quotes and commercial accounts, and getting found, and your number and customer list stay yours and leave with you if you ever go."),
    ],
    "service_schema_name": "Business software and marketing for locksmiths",
    "cta_h2": "See what your locksmith business is <em>missing</em>",
    "cta_sub": "Get a free audit of where your lockout calls and quotes are slipping away, whether you work with us or not. No credit card, never a call center.",
}
