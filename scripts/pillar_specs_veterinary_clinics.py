"""Pillar (trade hub) framing for VETERINARY CLINICS. generate_pillars.py owns the mechanics
(shell, schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This
file owns ONLY the unique, veterinary-specific framing prose that leads with the clinic's real
world (the worried-owner "can you see him today" call, the after-hours pet emergency, the vaccine,
wellness, and dental recalls that bring pets back, a barking-lobby front desk), never a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($99/$199 Signature plan, $499 website) ever
appear; no em/en dashes anywhere; "find the gap" / "slips away", never "leak". ETHICS: the client
is the pet owner and the patient is their animal; the AI receptionist does scheduling and intake
only, never veterinary advice; NO animal-health or treatment-outcome claim; a true emergency is
flagged to staff and pointed to the hospital the clinic trusts, with the owner setting the rules.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Veterinary Clinics",
    "title": "Software and Marketing Built for Veterinary Clinics | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing built for veterinary clinics: an AI receptionist that answers every call, a CRM for vaccine and wellness recall, and a site that ranks.",
    "answer": "A veterinary clinic runs on worried-owner calls, can you see him today, and the vaccine and wellness recalls pets come due for. A missed call sends an owner to the next clinic or the emergency vet, and pets go overdue when no recall goes out. Top Shelf fixes this: an AI receptionist, a CRM, and a site that ranks.",
    "faq_eyebrow": "veterinary teams ask",
    "sections": [
        {"h2_html": "Where a veterinary clinic actually <em>loses clients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A veterinary front desk is one of the busiest in any local business, and that is where clients slip away. When the phone rings, your team is holding a squirming cat for a blood draw, walking a nervous owner to a room, or calming a lobby full of barking dogs, so the call rings through to voicemail. An owner who thinks something is wrong with their pet does not leave a message. They call the next clinic or drive to the emergency vet, and a good client, worth years of visits for every animal in the house, is gone. The evening and weekend calls you are most likely to miss are often the most worried and the most valuable.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The exam rooms also empty from the recall list you already have. A dog due for its booster, a cat overdue for a dental, a household you have not seen since they moved across town, each drifts without a nudge. Top Shelf closes the gaps. An <a href="ai-receptionist-for-veterinary-clinics.html">AI receptionist</a> answers every call, asks what your team would ask, and books the routine visit or flags a true emergency to your staff and points the owner to the hospital you trust. A <a href="crm-for-veterinary-clinics.html">CRM</a> sends the vaccine, wellness, and dental reminders for you, and steady local marketing gets you found when a new owner searches for a vet nearby.</p>'},
        {"h2_html": "One system, not <em>a phone that rolls to voicemail</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Recalls slip and calls go unanswered because answering, follow-up, reviews, and the website usually live in separate tools that a rushed front desk cannot run at once. Top Shelf connects them. The visit the receptionist books lands in the same CRM that sends next year\'s vaccine reminder and the review request after the appointment, and your <a href="websites-seo-for-veterinary-clinics.html">website and local SEO</a> get you found in the map pack where new clients start. You keep your own number and your client and pet records, and both stay yours if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Signature plan, $99 a month for up to 10 users, includes the AI receptionist and the CRM that answer the phone and work your recall list. A professional website is $499 one time, and you do not need a plan to buy one. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist handles scheduling and intake only, never veterinary advice, with you setting what counts as an emergency and where those callers are sent. A free audit shows you exactly where calls and recalls are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a veterinary clinic?",
         "It depends on how much you want handled for you. The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM. The Signature plan is $99 a month for up to 10 users, and a professional website is $499 one time. There is no setup fee."),
        ("What happens when an owner calls with an after-hours emergency?",
         "You decide the rules. The receptionist asks what your team would ask, books routine visits, and flags anything that sounds urgent to your staff, pointing a true after-hours emergency to the hospital you trust. It never gives veterinary advice, and a person always decides how a pet is cared for."),
        ("Do we have to replace our practice management software?",
         "No. Top Shelf runs on your existing phone number and sits alongside the software you use. Your practice management system keeps the medical record, while Top Shelf answers the calls and works the recall list. Your number and client list stay yours and leave with you if you ever go."),
    ],
    "service_schema_name": "Business software and marketing for veterinary clinics",
    "cta_h2": "See what your veterinary clinic is <em>missing</em>",
    "cta_sub": "Get a free audit of where calls and recalls are slipping away, whether you work with us or not. No credit card, never a call center.",
}
