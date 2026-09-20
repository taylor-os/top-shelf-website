"""Pillar (trade hub) framing for MED SPAS (medical aesthetics: Botox, filler, laser, medical
facials, memberships and packages). generate_pillars.py owns the mechanics (shell, schema, the
auto-discovered money + colony link blocks, keyword placement, wiring). This file owns ONLY the
unique, med-spa-specific framing prose that leads with the med spa's real world (the nervous
first-time consult, after-hours and Instagram-driven interest, the memberships and packages that
keep clients on cycle), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "find the gap" / "slips away", never "leak". ETHICS: the AI
receptionist does scheduling and intake ONLY, never medical or cosmetic advice, which stays with
the licensed provider; NO cosmetic-result, weight-loss, or before-and-after outcome claims anywhere.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Med Spas",
    "title": "Software and Marketing Built for Med Spas | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing built for med spas: an AI receptionist that books consults by phone and text, a CRM for memberships and rebooking, and a site that ranks.",
    "answer": "A med spa runs on consults and memberships and packages clients rebook on cycle, and much of it arrives after hours. You lose it when a first-timer reaches voicemail, or a client who is due is never reminded. Top Shelf fixes the front desk: an AI receptionist that books by phone and text, a CRM, and a site that ranks.",
    "faq_eyebrow": "med spas ask",
    "sections": [
        {"h2_html": "Where a med spa actually <em>loses clients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A med spa loses clients less on price than on timing. Aesthetics is a look-first, trust-first business, and a lot of the interest arrives when your team cannot pick up: a first-timer who finally worked up the nerve to ask about a consult calls while your injector is mid-treatment, or fills out the form at eleven at night after seeing something on Instagram. A nervous caller does not leave a voicemail, she books with the spa that answered. Those after-hours inquiries are often the highest-intent ones you get, and they are exactly the ones that hit a dark front desk.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The other loss is quieter and more expensive: the recurring revenue you already earned. A client whose treatment has worn off, a package with sessions still on it, a membership about to lapse, none of it rebooks on its own. Top Shelf catches both. An <a href="ai-receptionist-for-med-spas.html">AI receptionist</a> answers every call and text on the first ring, warmly captures what she is interested in, and books the consult or holds it with a deposit, leaving every clinical question to your provider. A <a href="crm-for-med-spas.html">CRM</a> reminds each client on the cycle her treatment runs on and watches packages and memberships, while steady <a href="marketing-for-med-spas.html">local marketing</a> keeps you visible where clients look.</p>'},
        {"h2_html": "One system, not a <em>pile of apps</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason consults go to voicemail and rebookings slip is that booking, follow-up, reviews, and the website usually live in separate tools that do not share a client. Top Shelf is one connected system. The consult the receptionist books lands in the same CRM that reminds her when she is due and asks for a review after the visit, and your <a href="websites-seo-for-med-spas.html">website and local SEO</a> get you ranking for the treatments and towns you serve. Because it is one client record, each person is reminded on her own cycle instead of getting a blast meant for everyone. You keep your own number, your client list, and your photos, and they stay yours if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that book consults and keep clients on cycle. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist handles scheduling and intake only, never treatment or medical advice, which stays with your licensed provider. A free audit shows you exactly where consults and rebookings are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a med spa?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom five page site is $1,500. There is no setup fee."),
        ("Does the AI give clients any treatment advice?",
         "No, and it should not. It handles scheduling and intake only: what she is interested in, your consult types, your availability, and booking, and it can hold a slot with a deposit. Every medical and cosmetic question is left for your licensed provider at the consultation, where it belongs."),
        ("Can it answer by text, not just phone?",
         "Yes. Much of a med spa's interest comes in by text and after hours, so the receptionist answers by phone and text on the first ring, captures the details, and books the consult. Anything clinical is handed to your provider, and you approve how it speaks for your spa."),
    ],
    "service_schema_name": "Business software and marketing for med spas",
    "cta_h2": "See what your med spa is <em>missing</em>",
    "cta_sub": "Get a free audit of where consults and rebookings are slipping away, whether you work with us or not. No credit card, never a call center.",
}
