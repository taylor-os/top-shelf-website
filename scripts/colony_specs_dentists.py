"""Colony page specs for DENTISTS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a dental-practice owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, dentist-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear; no em/en dashes anywhere; "find the gap", never "leak".

Medical ethics (non-negotiable): the AI receptionist does scheduling, intake, and logistics
only, never dental or medical advice; no page makes a health, treatment, or outcome claim;
patient information is treated with the discretion a dental office is held to (HIPAA-aware).
Every scenario is illustrative, never a named client or competitor.

Six questions, mixed cost / problem / how-to, spread across three money pages:
  1 dentist-website-cost                  (cost)     -> websites-seo-for-dentists
  2 dental-office-answering-service-cost  (cost)     -> ai-receptionist-for-dentists
  3 is-a-crm-worth-it-for-a-dental-office (cost)     -> crm-for-dentists
  4 why-dental-offices-miss-calls         (problem)  -> ai-receptionist-for-dentists
  5 why-dental-patients-dont-rebook       (problem)  -> crm-for-dentists
  6 how-do-dentists-get-more-new-patients (how-to)   -> marketing-for-dentists
"""

TOPICS = [
# ==================== How Much Does a Dentist Website Cost? (cost -> websites-seo) ====================
{
    "slug": "dentist-website-cost",
    "h1": "How Much Does a Dentist Website Cost?",
    "title": "How Much Does a Dentist Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A dentist website should book new patients: easy appointment requests, insurance up front, trust for first-timers. Top Shelf builds yours for $1,500 or free on a plan.",
    "answer": "A dentist website is worth less for how it looks than for whether it books new patients. It has to make requesting an appointment obvious, answer the insurance question a shopper checks first, and build enough trust for a nervous first-timer to call. Top Shelf builds one for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a dental website has to do for a <em>new patient</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A patient choosing a new dentist is usually a little nervous and deciding fast. They found you on a phone, they are weighing you against two other offices, and within about a minute they are looking for a few specific things before they will call or fill anything out. A dental website earns its keep by giving them those things quickly and making the next step obvious, not by looking expensive. What it has to do is different from a generic small-business site.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Make requesting an appointment the one obvious action on every screen, with a request-an-appointment button and a tap-to-call number that follow the visitor as they scroll.</li><li>Answer the money question first, the insurance and PPO plans you accept and whether financing is offered, because that is what a shopper checks before anything else.</li><li>Build trust for a first-timer: the dentist and the team with real faces, the services you provide, and genuine patient reviews, so a stranger feels comfortable walking in.</li><li>Load fast on a phone and rank for the searches that matter, a dentist near me and a new patient dentist in your town, so the right people find you at all.</li></ul>'},
        {"h2_html": "So what should a dental practice <em>pay</em>?",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Price matters less than return. A dental website is worth exactly what it books, so a cheap template you never touch and a site built to bring in new patients can carry the same sticker price and be worth wildly different amounts. The one that turns a search into a booked appointment pays for itself many times over in a single new patient, who is worth years of cleanings, fillings, the occasional crown, and the people they refer once they trust you. The one that just sits there is the expensive one, whatever it cost.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps the number simple. A custom five page site built to do everything above is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it found is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking or a set number of new patients, because no one controls Google, but a free audit will show you exactly where your current site is losing them first.</p>'}],
    "bridge_h2": "Get a site that fills the schedule",
    "bridge_text": "A dental website is only worth the patients it books. Ours is built to rank for the towns you serve and turn a search into a booked new patient, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-dentists",
    "bridge_label": "Websites & SEO for dentists",
    "faqs": [
        ("What makes a dental website different from any other small-business site?",
         "It is built around a nervous new patient deciding fast. The insurance and PPO answer is easy to find, requesting an appointment is the obvious next step on every page, and the dentist, the team, and real reviews are front and center so a first-timer feels comfortable choosing you."),
        ("Do I own the site and the patient inquiries it brings in?",
         "Yes. If you buy the one-time $1,500 site it is yours to keep and host anywhere. On a monthly plan it is built and hosted for you, and either way the new-patient inquiries it collects are yours and handled with the care a dental office is held to, never held hostage. We tell you plainly what happens to the site if you leave, before you sign.")],
    "trade_slug": "dentists", "trade_plural": "dentists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ======== What Does a Dental Office Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "dental-office-answering-service-cost",
    "h1": "What Does a Dental Office Answering Service Cost?",
    "title": "What Does a Dental Office Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for dental offices often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for dental offices usually bill per call, per minute, or a monthly retainer, so a busy stretch gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call, handles insurance and scheduling questions, and books the visit comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy week turns into a big bill. A dental office also gets calls at the worst moments for a live front desk: while your team is checking a patient out, on hold with an insurer verifying benefits, or in the morning huddle, and after hours when a filling comes out at dinner. It helps to know the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a run of wrong numbers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a caller with a long list of insurance questions costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a first-time caller who reaches a voicemail does not leave a message, they call the next office until someone picks up and gets them scheduled. The real cost of no coverage is not a monthly fee, it is the new patient, worth years of visits, who booked down the street instead. But a generic call center reading a script cannot tell a caller whether you take their insurance or get them onto your calendar, so you can pay for coverage and still lose the booking.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, tells people your hours and whether you accept their plan, books the appointment on your calendar, and flags an urgent call to your team. It sticks to scheduling and intake and never gives dental advice, and it treats what a caller shares with the care a dental office is held to. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One new patient it books on a weekend can be worth well more than the plan costs, and everything it catches after that is on top. We will not pretend it replaces your team, it hands the calls that need a person straight to them.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers around the clock, handles insurance and scheduling questions, and books the visit, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-dentists",
    "bridge_label": "AI receptionist for dentists",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the new patient it books instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or holidays?",
         "No. It answers around the clock as part of the plan, including the Sunday search from a family new to town and the Saturday broken tooth, with no after-hours surcharge or overage.")],
    "trade_slug": "dentists", "trade_plural": "dentists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============== Is a CRM Worth It for a Dental Office? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-dental-office",
    "h1": "Is a CRM Worth It for a Dental Office?",
    "title": "Is a CRM Worth It for a Dental Office? | Top Shelf Business Solutions",
    "meta_desc": "For most dental offices a CRM pays for itself by reviving patients overdue for a cleaning and booking treatment they already accepted. It comes in the Signature plan at $899/mo.",
    "answer": "For most dental offices, yes. A CRM pays for itself the first time it brings back a patient overdue for a cleaning, or books a crown someone accepted but never scheduled. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a dental office when you have more patients, leads, and unscheduled treatment than the front desk can personally keep track of, which is nearly every established practice. It is not worth it if you are a brand-new office with a handful of patients you genuinely reach every time, though that rarely stays true as you grow. The honest test is simple: how many patients have not been in for a cleaning in over a year, and how many treatment plans did someone accept in the chair this year and never come back to book? Those are the visits a CRM is built to recover. Most established practices are not short on demand, they are short on the follow-up that turns a due patient or an accepted case into a booked visit, and that is the gap it fills.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a dental office is not the software, it is the production that stops slipping away. A family overdue for a cleaning, a patient who accepted a crown and meant to book it once their benefits reset, a hygiene visit that keeps getting put off: each one is a visit you have already half-earned and are one reminder away from filling.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It fires recall and recare reminders, the six-month cleaning, an overdue hygiene visit, the follow-up a treatment needs, so the chair fills without your team working a spreadsheet of due dates.</li><li>It follows up on unscheduled treatment on a schedule you set, so the patient who said yes to a crown hears from you again while it is still on their mind instead of aging out.</li><li>It keeps every patient, their history, and what they are due for next in one place, so your list becomes your schedule instead of just a record of who came in.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one lapsed patient or one accepted treatment and it has paid for itself, and everything after that is production you would have lost. Patient information is handled with the care a dental office is held to and stays yours to export.</p>'}],
    "bridge_h2": "Put your patient list to work",
    "bridge_text": "The patients you have already treated are the easiest chair to fill. A CRM reaches out to every one who is due or overdue, so they book with you instead of drifting to the office down the street.",
    "bridge_slug": "crm-for-dentists",
    "bridge_label": "CRM for dentists",
    "faqs": [
        ("Is a CRM overkill for a small dental practice?",
         "Not usually. Even a single-dentist office has more patients due for recall and more accepted treatment than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If patients lapse and accepted cases never get booked, a CRM earns its keep."),
        ("How is a CRM different from my practice management software?",
         "Practice software records who came in and stores the chart. A CRM sits alongside it as the outreach layer, reminding a patient they are due, following up on a treatment they accepted, and reviving one who has not been in for a year, on a schedule, so the list does the work instead of just sitting there.")],
    "trade_slug": "dentists", "trade_plural": "dentists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ Why Do Dental Offices Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-dental-offices-miss-calls",
    "h1": "Why Do Dental Offices Miss So Many Calls?",
    "title": "Why Do Dental Offices Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Dental offices miss calls because the phone rings while the front desk is chairside, and a new patient who reaches voicemail books the office that answered instead.",
    "answer": "Dental offices miss calls because the phone rings while the front desk is already busy, checking a patient out, verifying benefits, or in the morning huddle, and a first-time caller who reaches voicemail does not leave a message. They call the next office until someone answers. The fix is not a bigger front desk, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when the front desk is <em>chairside</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A dental front desk is rarely just sitting by the phone. When it rings, your team is often checking a patient out, on hold with an insurer verifying benefits, greeting someone who just walked in, or turning a room over between appointments, and the call rings through to voicemail while they are a few feet away with their hands full. The busier the schedule, the more calls slip, which means your best days are also the ones where the most new patients go unanswered. It is not a discipline problem. One or two people cannot run the front of the office and catch every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a new patient it is not one. Someone calling a dentist for the first time, comparing a couple of offices, is not going to leave a message and wait for a callback. They move down the list until a real voice picks up and gets them scheduled, and by the time anyone checks the voicemail, that patient is already booked somewhere else.</p>'},
        {"h2_html": "A missed new-patient call is your most <em>expensive miss</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A missed new patient is the most expensive one, because that first call is worth years of cleanings, fillings, the occasional crown, and the friends and family they refer once they trust you. Those calls also come at the times a front desk is least able to grab them: the lunch hour, the rush right at open, and the evenings and weekends when someone finally has a minute to deal with a tooth. So the calls you are most likely to miss are also the ones worth the most over time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never goes to voicemail and can actually help the caller. A voicemail box cannot tell a caller whether you take their insurance or get them booked, and a generic call center does not know your schedule. What works is something that answers on the first ring day or night, handles the insurance and new-patient questions, books the appointment on your calendar, and flags an urgent call to your team, all while sticking to scheduling and intake and never offering dental advice, so the new patient is booked instead of lost.</p>'}],
    "bridge_h2": "Stop sending new patients to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, handles the insurance and scheduling questions, and books the visit or flags it to your team, so a new patient never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-dentists",
    "bridge_label": "AI receptionist for dentists",
    "faqs": [
        ("Would a patient rather reach a real person?",
         "What a first-time caller needs most is a real answer and an appointment, and a calm voice that handles their insurance question and books them beats a voicemail box every time. The AI receptionist is upfront about what it is, sticks to scheduling and intake, and hands anything urgent straight to your team."),
        ("Can I just forward calls to a cell phone instead?",
         "You can, but that only helps when someone is free to answer. Forwarding still rolls to voicemail when the whole team is chairside or already on another call. Something that always answers, handles the routine questions, and books the visit is what catches the calls a forward would still miss.")],
    "trade_slug": "dentists", "trade_plural": "dentists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ Why Don't Dental Patients Rebook? (problem -> crm) ============
{
    "slug": "why-dental-patients-dont-rebook",
    "h1": "Why Don't Dental Patients Rebook?",
    "title": "Why Don't Dental Patients Rebook? | Top Shelf Business Solutions",
    "meta_desc": "Most dental patients don't rebook because nobody reminded them, not because they left. Life got busy after a cleaning, and without a recall nudge they quietly lapse.",
    "answer": "Most dental patients who do not rebook have not left you. They walked out of a cleaning meaning to schedule the next one, life got busy, and without a reminder the visit fell off their calendar the way it falls off yours. A patient who goes quiet is usually not gone, they just never got a nudge to come back.",
    "sections": [
        {"h2_html": "Not rebooking usually means forgotten, not <em>gone</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a patient who has not been in for a year as one who found another dentist, so you stop thinking about them. But most of the time they did not choose to leave at all. They came in for a cleaning, meant to book the next one on the way out, and then work, kids, and a dozen other things got in the way. A canceled appointment never got rescheduled, their benefits reset without anyone mentioning it, and six months quietly became eighteen. They are not upset with you, they simply forgot, and nobody reminded them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The same thing happens with treatment they already accepted. A patient hears in the chair that they need a crown, says yes, decides to wait until their benefits refresh in January, and walks out without a date on the calendar. Between hygiene checks and a full schedule, nobody circles back, and a case that was already a yes ages out. The rebook was never lost to a competitor. It was lost to silence.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Dental teams do not skip recall because they do not care. They skip it because the front desk is full. Someone is checking patients in and out, answering the phone, verifying benefits, and rooming the next appointment, and working a list of who is overdue for a cleaning is the thing that never rises to the top on a busy day. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest visits on the books.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system flagging which patients are due or overdue and which accepted cases were never booked.</li><li>The reminder depends on someone at the desk remembering, so it competes with the patients standing right in front of them and loses.</li><li>By the time anyone reaches out, the patient has drifted, or found another office when they finally went looking.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not an effort problem, and it is the kind of thing you set up once and it just runs. When every patient due for recall and every unscheduled treatment gets a warm, timed reminder automatically, written to sound like the office they already trust, the chair fills from the list you already have instead of the production quietly slipping away. Their information stays handled with the care a dental office is held to, and every message is one you approve.</p>'}],
    "bridge_h2": "Bring every patient back on schedule",
    "bridge_text": "A CRM keeps every patient due for a cleaning and every accepted treatment in front of you and sends the reminders for you, so your patient list fills the chair instead of drifting away.",
    "bridge_slug": "crm-for-dentists",
    "bridge_label": "CRM for dentists",
    "faqs": [
        ("How often should we remind a patient who is overdue?",
         "A couple of light touches works better than one, and better than nagging: a friendly note when they are due, another when they are overdue, and one more when their benefits reset. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated recall feel impersonal to patients?",
         "Not when it is written to sound like your office and sent at a sensible pace. A short, warm reminder that they are due for a cleaning reads as a practice that is on top of things, not a mass blast, and most patients are glad for the nudge because they meant to book and forgot. You can always reach out to anyone directly.")],
    "trade_slug": "dentists", "trade_plural": "dentists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ======== How Do Dentists Get More New Patients? (how-to -> marketing) ========
{
    "slug": "how-do-dentists-get-more-new-patients",
    "h1": "How Do Dentists Get More New Patients?",
    "title": "How Do Dentists Get More New Patients? | Top Shelf Business Solutions",
    "meta_desc": "Dentists get more new patients by showing up in the local map pack with strong reviews, a site that answers the insurance question, and a front desk that actually answers.",
    "answer": "Dentists get more new patients by being easy to find and easy to choose the moment someone searches. That means showing up in the local map pack with recent reviews, a website that loads fast and answers the insurance question, and making sure the calls that result actually get answered and booked. Most lost patients are lost before they ever reach you.",
    "sections": [
        {"h2_html": "New patients start on Google, at the <em>map pack</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone needs a dentist, a new family in town, a person whose tooth finally started hurting, someone whose insurance just changed, they almost always start the same way: a search on a phone for a dentist near them. The first thing Google shows is not a website, it is the map pack, the little map with three local offices, their star ratings, and a call button. Most people choose from those three, and the office with more recent reviews and a complete profile gets the call before anyone scrolls to the results below. If your phone is quiet, the reason is usually that you are not in those three at the moment people are deciding.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting seen there is its own job, separate from having a website, and it runs on a handful of things you can actually influence.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A Google Business Profile that is verified, complete, and active, with the right hours, location, and services listed.</li><li>A steady flow of recent, genuine reviews, which is what makes a searcher pick you over the office next door.</li><li>The insurance and PPO plans you accept stated plainly, because that is the first thing a new patient wants to know.</li><li>A consistent name, address, and phone number across the web, so Google trusts that you are one real practice.</li></ul>'},
        {"h2_html": "Getting found is wasted if the call <em>goes unanswered</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Ranking is only the first half. A new patient who finds you still has to get an answer and an appointment, and this is where practices quietly lose the patients their marketing worked to attract. They tap your listing and land on a site that does not say whether you take their plan or make booking easy, or they call and reach a voicemail while the front desk is chairside, and they move on to the next office. Getting found and then dropping the call is paying for a door nobody can open.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So more new patients is really one connected system, not a single trick: a profile and reviews that get you seen, a fast site that answers the insurance and new-patient questions and lets people book, a phone that always gets answered, and recall that turns each new patient into years of visits. Top Shelf runs those pieces together on one platform, starting at $299 a month, so a patient found on Google is one that actually gets booked and kept. What no honest company can promise is a specific ranking or a set number of patients, because no one controls Google, but a free audit will show you exactly where you are losing them today.</p>'}],
    "bridge_h2": "Get found where new patients look",
    "bridge_text": "Most new patients start with a search and pick from the map pack. Marketing that keeps your profile active, your reviews growing, and your site answering the insurance question is how you get chosen when someone nearby needs a dentist.",
    "bridge_slug": "marketing-for-dentists",
    "bridge_label": "Marketing for dentists",
    "faqs": [
        ("Do I need a new website to get more patients from Google?",
         "Not to appear in the map pack, which runs on your Google Business Profile. A verified, active, well-reviewed profile is the fastest way onto the map. A fast site that answers insurance questions and lets people book helps you rank below the map and turns those visits into appointments, so the two work together."),
        ("How long until I see more new patients?",
         "A neglected profile that gets verified, completed, and active, with reviews coming in steadily, can start climbing within a few weeks and compounds from there. Nobody controls Google, so no honest company promises a specific position or patient count, but consistency on the profile and reviews is what moves it.")],
    "trade_slug": "dentists", "trade_plural": "dentists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
]
