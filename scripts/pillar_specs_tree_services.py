"""Pillar (trade hub) framing for TREE SERVICES. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, tree-service-specific framing prose that leads with the trade's real world: work
arrives in a storm surge where everyone with a limb on the roof calls at once, the big removals are
high-ticket estimates that draw two or three bids over weeks, and licensed-and-insured is the first
trust question a homeowner asks before a saw goes into a tree over their house.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($99/$199 Signature plan, $499 website) ever
appear, and never an invented tree price; no em/en dashes anywhere; "slips away" / "goes cold",
never "leak" as a metaphor. The AI does intake and scheduling only; it never binds a removal quote
or promises a tree is safe.
"""

PILLAR = {
    "h1": "Tree Service Software and Websites Built for Storm Season",
    "title": "Tree Service Software and Websites Built for Storm Season | Top Shelf Business Solutions",
    "meta_desc": "Tree service software and marketing built for storm season: an AI receptionist that answers every storm call, a CRM that chases every bid, and a site built so Google can read it.",
    "answer": "Tree work arrives in a surge. A storm rolls through and everyone with a limb on the roof calls at once, while your crew is sixty feet up running a saw. Big removals draw two or three bids over weeks, so follow-up wins them. Top Shelf puts answering, follow-up, and reviews in one place for tree services.",
    "faq_eyebrow": "tree crews ask",
    "sections": [
        {"h2_html": "Where a tree service actually <em>loses the removal</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A tree service loses its best work in two places, and both come while the crew has both hands full. The first is the storm surge. When the wind dies down, every homeowner with a tree on the roof or a trunk across the drive dials at once, and a homeowner staring at a cracked limb does not leave a voicemail, they call the next crew on the list. Those emergency removals are your highest-margin work of the year, and they land in the same hours your climber is tied into a canopy and cannot reach the phone. The second is the big estimate. A large removal is real money, so the homeowner gathers two or three bids and sits with it for a week or two, and the job goes to whoever checked back in, which is rarely the cheapest and almost always the crew still in front of them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes both gaps. An <a href="ai-receptionist-for-tree-services.html">AI receptionist</a> answers every call on the first ring, storm night or Sunday, tells a tree on a house from a someday trim, and books the routine work or flags a real emergency to your phone. A <a href="crm-for-tree-services.html">CRM</a> keeps every open removal and trim bid in front of you and sends timed check-ins on its own while the homeowner decides. And your <a href="websites-seo-for-tree-services.html">website</a> proves you are licensed and insured, which is the first thing a nervous homeowner checks before letting a saw into a tree over their house.</p>'},
        {"h2_html": "One system, not a <em>cab full of apps</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason that work slips is that answering, follow-up, and reviews live in separate places, and a crew clearing storm damage all day cannot run them from the bucket. Top Shelf is one connected system. The call the receptionist books lands in the same CRM that fires the follow-up on the removal bid and the review request when the yard is cleaned up, and every storm cleanup drops into one list so a one-time job can become a customer for the life of the property. You keep your own number and your customer list, and both leave with you if you ever go.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Signature plan, $99 a month for up to 10 users, includes the AI receptionist and the CRM that answer every storm call and chase every bid. A professional website is $499 one time, and you do not need a plan to buy one. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist gathers the details and hands a real emergency straight to you, it never prices a removal or promises a tree is safe.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a tree service?",
         "The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM. A professional website is $499 one time. There is no setup fee."),
        ("What happens when a storm sends a rush of calls at once?",
         "The AI receptionist answers every one on the first ring at the same moment, so a surge that would overwhelm one person is simply handled. Each caller is triaged, the emergencies are flagged to your phone, and the routine estimates are booked, all on the Signature plan. It never prices the removal or promises a tree is safe, you decide that on site."),
        ("Is a monthly plan cheaper than a live service that bills per call?",
         "For a tree service it usually is, and it is far more predictable, because a metered service charges you hardest during the storm week when the calls flood in. The Signature plan stays $99 a month for up to 10 users no matter how busy the weather gets, and the bigger saving is the emergency removal it books instead of losing to voicemail."),
    ],
    "service_schema_name": "Business software and websites for tree services",
    "cta_h2": "See which storm calls your crew is <em>letting slip away</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
}
