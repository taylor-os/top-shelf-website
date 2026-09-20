"""Pillar (trade hub) framing for PHYSICAL THERAPISTS. generate_pillars.py owns the mechanics
(shell, schema, the auto-discovered money + colony link blocks, keyword placement, wiring). This
file owns ONLY the unique, physical-therapy-specific framing prose that leads with the clinic's
real world (two patient engines at once, physician referrals plus direct-access self-referrals; a
plan of care that runs many visits to discharge; drop-off mid-plan and authorization limits), never
a template.

Same honesty rules as the money/colony specs: no invented stats, prices, or clients; hedge instead
of overpromise; only the real prices ($299/$899/$2,500 monthly plans, $1,500 one-time site) ever
appear; no em/en dashes anywhere; "find the gap" / "slips away", never "leak". Medical ethics: the
AI receptionist does scheduling and intake only, routing anything clinical to the team, never
medical advice; no recovery, pain-relief, or treatment-outcome claim.
"""

PILLAR = {
    "h1": "Software and Marketing Built for Physical Therapists",
    "title": "Software and Marketing Built for Physical Therapists | Top Shelf Business Solutions",
    "meta_desc": "Software and marketing built for physical therapists: an AI receptionist that books referrals, a CRM that keeps plans of care on track, and a site that ranks.",
    "answer": "A physical therapy clinic fills from two engines, referrals and direct-access search, and a new evaluation is a whole plan of care. A missed referral call hands that episode and the referral relationship to another clinic, and patients drop off when nobody follows up mid-plan. Top Shelf fixes this: an AI receptionist, a CRM, and a site that ranks.",
    "faq_eyebrow": "physical therapists ask",
    "sections": [
        {"h2_html": "Where a physical therapy clinic actually <em>loses patients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A physical therapy clinic loses patients in places a generic template never sees, because your schedule fills from two directions and empties from a third. New evaluations come from physicians and surgeons who refer, and from direct-access patients who search when their back or knee gives out. When either one calls while your therapists are on the floor and the front desk is verifying benefits, the call rings to voicemail, and a patient holding a referral simply books the next in-network clinic. Worse, the surgeon who sent them notices their patient could not get in, and referral sources quietly remember which clinics answer.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The third loss is the patient who drops off partway through a plan of care, either because they felt better and stopped, or because an insurance authorization ran out mid-plan and no one caught it. Top Shelf closes all three. An <a href="ai-receptionist-for-physical-therapists.html">AI receptionist</a> answers every call, tells a referral from a reschedule, notes a workers-comp or auto-injury case, and books the evaluation. A <a href="crm-for-physical-therapists.html">CRM</a> follows up on referrals that never scheduled, checks in with patients who miss a visit, and keeps an eye on authorized visits, while steady <a href="marketing-for-physical-therapists.html">local marketing</a> feeds the direct-access side.</p>'},
        {"h2_html": "One system, not <em>a stack of tools</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Referrals go cold and plans of care end early because intake, follow-up, reviews, and the website usually live in separate tools that no busy clinic can run at once. Top Shelf connects them. The evaluation the receptionist books lands in the same CRM that flags a patient nearing an authorized visit limit and checks in with one who goes quiet, and your <a href="websites-seo-for-physical-therapists.html">website and local SEO</a> get you found by the direct-access patients searching nearby. Because it is one system, an evaluation, its authorization count, and the check-ins that keep a plan on track live on the same record. You keep your own number and your patient and referral records, and both stay yours if you ever leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The pricing is plain. The Essentials plan is $299 a month and covers the website, local SEO, online booking, and reviews. The Signature plan at $899 a month adds the AI receptionist and the CRM that book referrals and keep plans of care on track. A fully done-for-you plan runs $2,500 a month, or you can buy a custom five page site outright for $1,500 one-time with no plan at all. There is no setup fee on any of it. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, and the AI receptionist handles scheduling and intake only, routing anything clinical to your team and never giving medical advice. A free audit shows you exactly where referrals, evaluations, and plans of care are slipping away, whether you work with us or not.</p>'},
    ],
    "faqs": [
        ("What does Top Shelf cost for a physical therapy clinic?",
         "It depends on how much you want handled for you. The Essentials plan is $299 a month for the website, local SEO, online booking, and reviews. The Signature plan is $899 a month and adds the AI receptionist and CRM. A done-for-you plan is $2,500 a month, or a one-time custom five page site is $1,500. There is no setup fee."),
        ("Can it handle a physician referral or a workers-comp intake?",
         "Yes. It tells a referral from a self-referral from an existing patient, asks whether a doctor sent them, notes a workers-comp or auto-injury case for your team to verify, and books the evaluation. It captures what your intake needs so a referral does not roll to voicemail, and it never gives medical advice."),
        ("Will it help patients finish a plan of care?",
         "Indirectly, on the front-desk side. The CRM checks in with patients who miss a visit and keeps each authorized visit count in view so your team can request a re-authorization before it runs out. It handles scheduling and reminders only, and every clinical decision stays with your therapists."),
    ],
    "service_schema_name": "Business software and marketing for physical therapists",
    "cta_h2": "See what your physical therapy clinic is <em>missing</em>",
    "cta_sub": "Get a free audit of where referrals, evaluations, and plans of care are slipping away, whether you work with us or not. No credit card, never a call center.",
}
