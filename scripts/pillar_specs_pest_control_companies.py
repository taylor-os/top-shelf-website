"""Pillar (trade hub) framing for PEST CONTROL COMPANIES. generate_pillars.py owns the mechanics
(shell, schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This
file owns ONLY the unique, pest-control-specific framing prose that leads with the trade's real
world: a recurring-plan business. The panic call is the way in, but the value is turning that one
job into a protection plan that renews every quarter for years, so the money lives in answering the
panic call, booking routine work, and following up until a one-timer becomes an account.

This trade has all seven money pages, so the pillar mirrors the plumber structure: section 1 weaves
the receptionist, online booking, CRM, automation, and review-software links; section 2 weaves the
website/SEO and marketing links plus the pricing. Same honesty rules as the money/colony specs: no
invented stats, prices, or clients; hedge instead of overpromise; only the real prices
($99/$199 Signature plan, $499 website) ever appear; no em/en dashes anywhere;
"slips away" / "find the gap", never "leak" as a money metaphor.
"""

PILLAR = {
    "h1": "Pest Control Software and Marketing in One Platform",
    "title": "Pest Control Software and Marketing in One Platform | Top Shelf Business Solutions",
    "meta_desc": "Pest control software and websites in one platform: an AI receptionist that answers every panic call, a CRM that builds recurring plans, and a site built so Google can read it.",
    "answer": "Pest control runs on recurring plans. A homeowner calls in a panic, but the real value is turning that one job into a protection plan that renews for years. You lose it when the panic call goes unanswered, or nobody follows up to offer the plan. Top Shelf puts all of it in one place for pest control companies.",
    "faq_eyebrow": "pest control pros ask",
    "sections": [
        {"h2_html": "Where a pest control business actually <em>loses the plan</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A pest control business rarely loses on price. It loses in the gaps between a frightened homeowner needing help and you being free to answer, and again between one job and the recurring plan it should have become. Your tech is under a sink or up in an attic when the panic call comes in, so it rolls to voicemail, and a homeowner who just found a wasp nest by the kids\' swing set does not leave a message, they call the next exterminator. The routine work, quarterly service, a termite inspection, a mosquito treatment, forces a round of phone tag when the customer would have booked it themselves. And the one-time job you did win is a protection plan waiting to happen, lost only because nobody offered it while the relief was fresh.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps one at a time. An <a href="ai-receptionist-for-pest-control-companies.html">AI receptionist</a> answers every call day or night and tells a wasp nest from a routine quarterly. <a href="online-booking-for-pest-control-companies.html">Online booking</a> lets the routine work schedule itself on your real route availability, while a real emergency is pointed to your phone. A <a href="crm-for-pest-control-companies.html">CRM</a> follows up on every one-time job with the plan offer, and <a href="automation-for-pest-control-companies.html">automation</a> rebooks each recurring visit and catches a termite renewal before it lapses. And when the pest is confirmed gone, <a href="review-software-for-pest-control-companies.html">review software</a> asks the relieved customer at the one moment they are most willing to say yes.</p>'},
        {"h2_html": "One system, not a <em>clipboard full of apps</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason all of this falls through is that it lives in five different places, and a busy exterminator does not have time to run five tools between stops. Top Shelf is one connected system instead. The panic call the receptionist answers lands in the same CRM that fires the plan offer, the rebooking notice, and the review request the moment a job is marked done. Your <a href="websites-seo-for-pest-control-companies.html">website</a> sends every service request into the same CRM. You keep your own number and your customer list, and both leave with you if you ever go.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Signature plan, $99 a month for up to 10 users, includes the AI receptionist and the CRM that follow up on every call and job. A professional website is $499 one time, and you do not need a plan to buy one. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist hands a genuine emergency straight to you rather than pretending to handle it.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a pest control company?",
         "The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM. A professional website is $499 one time. There is no setup fee."),
        ("How does this turn one-time jobs into recurring plans?",
         "The CRM keeps every one-time customer in front of you and sends a friendly follow-up a few days after the job, while the relief is fresh, offering the protection plan and what it covers. Then automation rebooks each plan visit on its cadence and reminds a termite warranty before it lapses, so more single treatments become accounts that bill for years."),
        ("Will the AI receptionist handle a real pest emergency?",
         "It triages like you would. It answers on the first ring, stays calm with a rattled caller, finds out whether it is stinging insects, rodents, or bed bugs, gets the address, and either books the stop or flags a true emergency straight to your phone. It is upfront that it is an assistant, not a person, and never pretends to solve the problem itself."),
    ],
    "service_schema_name": "Business software and websites for pest control companies",
    "cta_h2": "See which jobs and plans you are <em>letting slip away</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
}
