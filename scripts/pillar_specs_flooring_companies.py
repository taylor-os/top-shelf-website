"""Pillar (trade hub) framing for FLOORING COMPANIES. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, flooring-specific framing prose that makes the pillar non-thin and leads with the
flooring company's real world, never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "slips away" / "goes cold", never "leak" as a metaphor. The AI
receptionist does scheduling and intake only, it never guesses a price or quotes the job, the owner
still walks the job and sets the number.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Flooring Companies",
    "title": "Software and Marketing Built for Flooring Companies | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing for flooring companies: an AI receptionist that books measures, a CRM that follows up as homeowners choose, and a site that shows your work.",
    "answer": "Flooring is a visual, considered purchase. A homeowner picks hardwood, luxury vinyl plank, tile, or carpet with their eyes, takes samples home, and chooses over weeks, so the company that answers, shows its floors, and books the in-home measure wins. Top Shelf answers every call while your crew is on the floor, follows up for weeks, and shows your work.",
    "faq_eyebrow": "flooring companies ask",
    "sections": [
        {"h2_html": "Where a flooring company actually <em>loses jobs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A flooring company loses jobs in the gap between a homeowner picturing a new room and a crew that has both hands on the floor. Homeowners buy floors with their eyes, often late at night after staring at a room they cannot stand anymore, and when they call, your estimator is on his knees with a trowel and your installer is mid-room with a nailer, so the call rings out and a whole room, sometimes a whole floor, books with whoever picked up. Then the measure itself goes cold. A decision about floors a homeowner will walk on every day takes weeks, so they carry sample boards home, price a company or two more, and go back and forth with a spouse, and a quote that goes quiet in that window is usually still winnable, not a no.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps. An <a href="ai-receptionist-for-flooring-companies.html">AI receptionist</a> answers every call the moment it rings, even with your whole crew on the floor, asks which rooms they want done and what material they are leaning toward, and books the in-home measure or hands you a qualified lead. A <a href="crm-for-flooring-companies.html">CRM</a> keeps every open quote in front of you and sends timed check-ins across the weeks a homeowner compares samples, so the family still deciding keeps hearing from you while the others go quiet, and it brings past customers back for the next room, the stairs, the basement, while the floor you laid is still new. It never guesses a price, you still walk the job and set the quote.</p>'},
        {"h2_html": "One system, not a <em>stack of logins</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">All of that slips through because it usually lives in a stack of separate logins, and nobody laying floor has time to run them between rooms. Top Shelf is one connected system instead. The measure the receptionist books lands in the same CRM that fires the follow-up and the review request the day the floor is done and the homeowner cannot stop looking at it. Your <a href="websites-seo-for-flooring-companies.html">website and local SEO</a> feed it with galleries of real finished rooms and rankings for the floors and towns homeowners search, because floors get shortlisted with the eyes before anyone calls, and your <a href="marketing-for-flooring-companies.html">marketing</a> turns every finished floor into the photos and honest reviews a careful buyer wants. You keep your own number and your own customer list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that follow up on every call and every open measure. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the receptionist handles scheduling and intake only, it never guesses a price or quotes the job, you still walk the job and set the number. A free audit is the place to start, and it shows you where your calls and measures are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a flooring company?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom site is $1,500. There is no setup fee."),
        ("Does the receptionist quote the job over the phone?",
         "No. It handles scheduling and intake only, which rooms, roughly how much square footage, and what material they are considering, then books the in-home measure or hands you the lead. You still walk the job and set the quote. It never guesses a price or commits you to one."),
        ("Do I have to replace the tools I already use?",
         "No. Top Shelf runs on your existing phone number and is built around how a flooring company already works. It fills the gaps in answering calls, following up on measures, and getting found, and your number and customer list stay yours and leave with you if you ever go."),
    ],
    "service_schema_name": "Business software and marketing for flooring companies",
    "cta_h2": "See what your flooring company is <em>missing</em>",
    "cta_sub": "Get a free audit of where your calls, measures, and past customers are slipping away, whether you work with us or not. No credit card, never a call center.",
}
