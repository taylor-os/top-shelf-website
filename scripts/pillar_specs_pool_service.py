"""Pillar (trade hub) framing for POOL SERVICE. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, pool-service-specific framing prose that leads with the trade's real world: the
recurring weekly route is the revenue base, so signing up and KEEPING a route account matters more
than any one-off job, and a canceled recurring customer is the biggest single loss.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($99/$199 Signature plan, $499 website) ever
appear, and never an invented pool price; no em/en dashes anywhere; "slips away" / "goes cold",
never "leak" as a money metaphor. The AI does scheduling and intake only, it never diagnoses a pool.
"""

PILLAR = {
    "h1": "Pool Service Software and Websites Built for Your Route",
    "title": "Pool Service Software and Websites Built for Your Route | Top Shelf Business Solutions",
    "meta_desc": "Pool service software and marketing built for your route: an AI receptionist that answers every call, a CRM that keeps recurring customers, and a site built so Google can read it.",
    "answer": "A pool company lives on the recurring route, so the money is in winning a weekly account and keeping it. You lose it two ways: the signup call that rings while you are on the route, and the customer who quietly cancels because they felt forgotten. Top Shelf puts answering, follow-up, and reviews in one place for pool companies.",
    "faq_eyebrow": "pool pros ask",
    "sections": [
        {"h2_html": "Where a pool service business actually <em>loses the account</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A pool business does not lose most of its money on one-off jobs, it loses it on the recurring route, which is exactly what makes the losses so quiet. The call from a homeowner ready to start weekly service rings while you are elbow-deep in an equipment pad or driving between stops, so it rolls to voicemail, and a whole account, revenue every month for years, goes to the company that answered. Meanwhile a route customer you already had stops feeling looked after, sees nothing happen while they are at work, and cancels. On a dense route, one cancellation can make the whole run less profitable to service.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes both gaps. An <a href="ai-receptionist-for-pool-service.html">AI receptionist</a> answers every call while you are on the route, books the new weekly signup, and flags an urgent equipment problem to your phone. A <a href="crm-for-pool-service.html">CRM</a> keeps each route customer informed for you, a note after the visit, a heads-up when weather moves a day, a check-in before the season, so the recurring account feels cared for instead of forgotten. And your <a href="websites-seo-for-pool-service.html">website</a> sends the next route customer’s request into the same place.</p>'},
        {"h2_html": "One system, not a <em>stack of apps that do not talk</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason retention and new signups slip is that they live in separate tools, and a route owner servicing pools all day cannot run four of them from the pool deck. Top Shelf is one connected system. The signup the receptionist books lands in the same CRM that sends the after-visit note, the weather heads-up, and the review request when the account is happy. New accounts land near the stops you already run, so the route stays dense. You keep your own number and your customer list, and both leave with you if you ever go.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Signature plan, $99 a month for up to 10 users, includes the AI receptionist and the CRM that answer every call and work every account. A professional website is $499 one time, and you do not need a plan to buy one. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist handles scheduling and intake rather than diagnosing a pool it cannot see.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a pool service company?",
         "The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM. A professional website is $499 one time. There is no setup fee."),
        ("Can the AI receptionist handle a call about a green pool or a dead pump?",
         "It handles the call, not the diagnosis. It answers on the first ring, gets the address and the pool details, books routine and weekly service, and flags a genuine equipment problem straight to your phone so you decide how to respond. It is upfront that it is an assistant and never guesses at what is wrong with the pool."),
        ("Will this help me keep the route customers I already have?",
         "That is where a lot of the value is. Most route customers cancel because they felt forgotten, not because of the work, so the CRM sends a note after each visit, a heads-up when weather moves a day, and a check-in before the season, which keeps the recurring account feeling looked after and on your route."),
    ],
    "service_schema_name": "Business software and websites for pool service companies",
    "cta_h2": "See which accounts your route is <em>letting slip away</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
}
