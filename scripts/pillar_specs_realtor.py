"""Pillar (trade hub) framing for REAL ESTATE AGENTS (the colony/spec suffix is 'realtor'; the URL
token and money-page slug are 'real-estate-agents'). generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, agent-specific framing prose that leads with the reality: a buyer's call is a
timer, not a message, so the agent who answers first while everyone else is mid-showing wins the
client, and leads go cold over the months before someone is ready to transact.

Uses "real estate agent(s)" as the general term; "realtor" only where it is the accurate search
term. Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge
instead of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site)
ever appear; no em/en dashes anywhere; "slips away" / "goes cold", never "leak" as a money metaphor;
no guaranteed-sale, valuation, or ROI claims. The AI captures the lead and hands over the client.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Real Estate Agents",
    "title": "Software and Marketing Built for Real Estate Agents | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for real estate agents: an AI receptionist that answers every call, a CRM that keeps leads warm, online booking, reviews, and a ranking site.",
    "answer": "A buyer's call is a timer, not a message. You are mid-showing when the phone rings, it goes to voicemail, and that buyer dials the next agent. Top Shelf answers every call on the first ring, books the showing, follows up so no lead goes cold, and gets you found without renting your buyers back from a portal.",
    "faq_eyebrow": "agents ask",
    "sections": [
        {"h2_html": "Where a real estate agent actually <em>loses clients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A real estate agent almost never loses a client on price. You lose them in the gaps between someone reaching out and you being free to answer, and in the months a lead sits without a single follow-up. A buyer calls about a listing while you are out at another showing, so the call rolls to voicemail and they hire the agent who picked up. A seller who was a year from listing forgets your name because nobody stayed in touch. A closing goes by without a review request, so the reputation that wins your next listing never gets built. Each one is a client you had half-earned and let slip away.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf is built to close those gaps one at a time. An <a href="ai-receptionist-for-real-estate-agents.html">AI receptionist</a> answers every call on the first ring, day or night, and captures the buyer while you are still in the showing. A <a href="crm-for-real-estate-agents.html">CRM</a> keeps every lead, past client, and sphere contact warm on a schedule you set, so the buyer who is months out still calls you. <a href="online-booking-for-real-estate-agents.html">Online booking</a> lets a buyer grab a showing time straight from your listing instead of playing phone tag, and <a href="review-software-for-real-estate-agents.html">review software</a> asks every happy client for a review the moment they are happiest, right after closing.</p>'},
        {"h2_html": "One system, not a <em>dozen subscriptions</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason so much of this falls through is that it lives in a dozen separate apps, and an agent running showings does not have time to wire them together. Top Shelf is one connected system instead. The call the receptionist captures lands in the same CRM that fires the follow-up and the review request after closing. Your <a href="websites-seo-for-real-estate-agents.html">website and local SEO</a> rank for your name and your neighborhoods so a buyer becomes your own contact instead of a portal lead, your <a href="marketing-for-real-estate-agents.html">marketing</a> keeps you the name a neighborhood recognizes, and <a href="automation-for-real-estate-agents.html">automation</a> keeps your past clients warm with anniversary and market touches that send themselves. You keep your own website, number, and database, and all of it goes with you if you ever change brokerages.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that answer every call and follow up on every lead. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five-page site outright for $1,500 one time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, and the AI receptionist captures the lead and hands you the client rather than pretending to be you. A free audit is the place to start, and it shows you exactly where your calls, leads, and closings are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a real estate agent?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Will the AI receptionist capture a buyer while I am in a showing?",
         "That is exactly what it is for. It answers on the first ring, day or night, greets the caller in a natural voice, answers the basic questions about a listing, captures who they are and what they want, and can book the showing, then hands you the lead so you follow up as the agent who was there first."),
        ("Do I keep my website and contacts if I switch brokerages?",
         "Yes. Your website, domain, number, and contact list are in your name from day one, so if you change offices or leave, all of it goes with you. That is not true of every provider or brokerage tool, so it is always worth confirming before you sign."),
    ],
    "service_schema_name": "Business software and marketing for real estate agents",
    "cta_h2": "See what your real estate business is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, leads, and closings are slipping away, whether you work with us or not. No credit card, never a call center.",
}
