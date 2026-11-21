"""Pillar (trade hub) framing for BARBERSHOPS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file
owns ONLY the unique, barbershop-specific framing prose that leads with the barbershop's real
world: a tight two-to-four week cut cadence, a live mix of walk-ins and regulars, booth-rent
barbers who each keep their own book, and men who ask for one chair by name. Never the six-week
color rebook or the stylist model.

Honesty rules match the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($99/$199 Signature plan, $499 website) ever
appear, the shop's own cut and fade pricing stays generic; no em/en dashes anywhere; "slips away"
and "find the gap", never "leak" as a money metaphor. The AI receptionist does scheduling and
intake only and hands anything that needs the owner's call to the owner.
"""

PILLAR = {
    "h1": "Barbershop Software and Marketing That Fills Chairs",
    "title": "Barbershop Software and Marketing That Fills Chairs | Top Shelf Business Solutions",
    "meta_desc": "Barbershop software and marketing in one place: an AI receptionist that reads the wait and books the chair, a CRM that rebooks regulars, and a site that ranks.",
    "answer": "A barbershop runs on walk-ins and regulars on a tight cadence, where a fade grows out in a couple of weeks and a man sits in one barber's chair. Top Shelf puts it in one place: an AI receptionist that reads the wait and books the chair, a CRM that rebooks regulars, online booking, reviews, and a site that ranks.",
    "faq_eyebrow": "barbershop owners ask",
    "sections": [
        {"h2_html": "Where a barbershop actually <em>loses chairs</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A barbershop rarely loses a man on the quality of the cut. It loses him in the small gaps around a chair that is always full. The phone rings while every barber is mid-fade with clippers in hand, so the man checking the wait gets voicemail and drives to the shop that answered. A regular walks out without booking his next cut, and on a two to three week cadence his fade is grown out and he has dropped into whatever shop was convenient before you think to reach him. Each one is a chair you had half-earned and let slip away.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf closes those gaps one at a time. An <a href="ai-receptionist-for-barbershops.html">AI receptionist</a> answers every call the second it rings, reads the wait honestly, and books the man with the barber he asks for by name. A <a href="crm-for-barbershops.html">CRM</a> keeps every regular tied to his barber and sends the rebooking nudge on the short cadence a cut runs on, so he comes back to your chair instead of the one down the block. And a <a href="websites-seo-for-barbershops.html">website built to rank</a> makes sure the man searching barber near me finds you first, sees the wait, and books in a tap while your barbers keep cutting.</p>'''},
        {"h2_html": "One system, not a <em>drawer full of apps</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most of this slips because it lives in five different tools, and a shop full of booth-rent barbers each keeping his own book does not have a spare hand to run them between fades. Top Shelf is one connected system instead. The chair the receptionist books lands in the same CRM that fires the rebooking nudge two weeks later. Your marketing keeps your Google profile active and full of fresh cuts and reviews, which is where men actually pick a shop, and every new client it brings in feeds the same book. You keep your own number and your own list of regulars, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Signature plan, $99 a month for up to 10 users, includes the AI receptionist and the CRM that read the wait and rebook every regular. A professional website is $499 one time, and you do not need a plan to buy one. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist sticks to scheduling and hands anything that needs your call straight to you. A free audit is the place to start: it shows exactly where your calls, rebooks, and chairs are slipping away, whether you work with us or not.</p>'''},
    ],
    "faqs": [
        ("What does Top Shelf cost for a barbershop?",
         "It depends on how much you want handled for you. The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM. The Signature plan is $99 a month for up to 10 users, and a professional website is $499 one time. There is no setup fee."),
        ("Do I have to replace the tools my shop already uses?",
         "No. Top Shelf runs on your existing number and is built around how a barbershop actually works, walk-ins, a live wait, and booth-rent barbers who each keep their own book. It fills the gaps in answering calls, rebooking regulars, and getting found, and your number and client list stay yours and leave with you if you ever go."),
        ("Will the AI receptionist book the right barber?",
         "Yes. It answers on the first ring, gives an honest read on the wait, and books the man with the barber he asks for by name or points him to the shortest open chair. It sticks to scheduling and intake, is upfront that it is an assistant, and hands anything that needs your call, like a big group before a wedding, straight to you."),
    ],
    "service_schema_name": "Business software and marketing for barbershops",
    "cta_h2": "See what your barbershop is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls, rebooks, and chairs are slipping away, whether you work with us or not. No credit card, never a call center.",
}
