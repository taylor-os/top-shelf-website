"""Pillar (trade hub) framing for AUTO DETAILERS. generate_pillars.py owns the mechanics (shell,
schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This file owns
ONLY the unique, detailer-specific framing prose that makes the pillar non-thin and leads with the
detailer's real world (appointment and package booking, image-driven discovery, hands on a car
with a machine running, rebooking on a maintenance cadence), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; the detailer's
own package pricing stays generic with no numbers; hedge instead of overpromise; only the real
Top Shelf prices ($99/$199 Signature plan, $499 website) ever appear; no em/en dashes
anywhere; "slips away" / "goes cold", never "leak" as a money metaphor. The AI does scheduling and
intake only and hands judgment calls to the owner.
"""

PILLAR = {
    "h1": "Auto Detailing Software and Marketing That Books Cars",
    "title": "Auto Detailing Software and Marketing That Books Cars | Top Shelf Business Solutions",
    "meta_desc": "Auto detailing software and websites in one platform: an AI receptionist that books while your hands are on a car, a CRM that rebooks, and a site built so Google can read it.",
    "answer": "Detailing is sold with your eyes, booked by a customer who saw your before and after photos, and the calls come while your hands are on a car with a polisher running. Top Shelf puts it in one place for auto detailers: an AI receptionist that books the job, a CRM that rebooks the next detail, and a site that shows your work.",
    "faq_eyebrow": "detailers ask",
    "sections": [
        {"h2_html": "Where a detailing business actually <em>loses bookings</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A detailer does not usually lose a job on price. It slips away in the moments you cannot get to the phone. When it rings you are leaned into a back seat with an extractor, running a polisher across a hood, or parked in a driveway two towns over with a foam cannon in hand. A customer pricing a full detail or a coating is calling two or three shops and books whoever picks up, so the higher ticket work you most want is exactly the call you are most likely to miss.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The other half goes quiet after the job is done. A coating quote sits while the customer thinks it over, and nobody follows up. A car you detailed last season is due for its maintenance wash, but the customer forgot and drifts to whoever is easiest. Top Shelf closes those gaps. An <a href="ai-receptionist-for-auto-detailers.html">AI receptionist</a> answers while your hands stay on the car, does a real detailing intake, and books the appointment. A <a href="crm-for-auto-detailers.html">CRM</a> rebooks past customers on a maintenance cadence and chases every open quote. And a <a href="websites-seo-for-auto-detailers.html">website built to rank</a> puts your finished work in front of people the moment they search for detailing near them.</p>'},
        {"h2_html": "One system, not a <em>pile of apps</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most of this slips because it lives in a phone full of texts, a separate booking app, and a review link you keep meaning to send. Top Shelf is one connected system instead. The call the receptionist books lands in the same CRM that fires the coating care reminder and asks for the review the day the car leaves clean. You keep your own number and your own customer list, and both go with you if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Signature plan, $99 a month for up to 10 users, includes the AI receptionist and the CRM that follow up on every call and quote. A professional website is $499 one time, and you do not need a plan to buy one. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist does the scheduling and intake only, handing a judgment call like pricing a heavy correction straight to you.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a detailing business?",
         "The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM. A professional website is $499 one time. There is no setup fee."),
        ("Can the AI receptionist tell a maintenance wash from a full correction?",
         "Yes. It does a real detailing intake, asking what the vehicle needs, whether the customer wants mobile or drop off, and the condition of the car, then books it on your calendar or books a consultation for work that needs your eyes first. It handles scheduling and intake and hands a judgment call, like pricing a multi stage correction, straight to you."),
        ("Will this help my customers actually come back?",
         "That is what the CRM is for. It reminds a customer when a coating is due for its maintenance wash, when the interior is due for a refresh, and when the season calls for a protective coat, written to sound like you and sent at a sensible pace, so the repeat work comes back instead of drifting to whoever is easiest."),
    ],
    "service_schema_name": "Business software and websites for auto detailers",
    "cta_h2": "See what your detailing calendar is <em>missing</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
}
