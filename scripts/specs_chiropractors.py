"""Per-page content specs for the SEO corpus (plan §5), chiropractors batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, chiropractor-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the plumber content reworded.

Medical & Dental hub. Four service angles are here in one file (the ai-receptionist dict carries
"demo": True). Each example body ends with the literal "Illustrative example, not a client." per
the honesty rule; if the generator also appends that line, dedupe there.
"""

SPECS = [
# ========================= AI Receptionist for Chiropractors =========================
{
    "slug": "ai-receptionist-for-chiropractors", "demo": True,
    "trade_slug": "chiropractors", "trade_plural": "chiropractors",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "AI Receptionist for Chiropractors",
    "title": "AI Receptionist for Chiropractors | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Chiropractors",
    "meta_desc": "A chiropractic answering service answers every new-patient call day or night, screens the reason for the visit, and books it while your front desk is busy.",
    "service_schema_name": "AI Receptionist for Chiropractors",
    "eyebrow": "For Chiropractors",
    "h1_html": "AI Receptionist <em>for Chiropractors</em>",
    "answer_block": "An AI receptionist for chiropractors answers every new-patient call the moment it rings, day or night, works like a chiropractic answering service that never takes a lunch, screens what brings the caller in, and books the first visit while your front desk is rooming patients. You keep your number, and every new patient belongs to you.",
    "sections": [
        {"h2_html": "The call you miss is the new patient who <em>books the next clinic</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone who just threw out their back or woke up with a neck they cannot turn is not going to leave a voicemail and wait for a callback. They are hurting now, they searched for a chiropractor near them, and they are calling down the list until a person answers. New-patient acquisition is the whole game for a chiropractic office, and the phone is where it is won or lost. But the front desk is not sitting by the phone. They are rooming a patient, setting up the next adjustment, verifying insurance, or checking someone out, so the call rings through to voicemail and the new patient, the one who could have started a full care plan, books with the office that picked up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An AI receptionist answers on the first ring, through the morning rush and long after you have locked up, stays warm with someone in pain, finds out what brings them in and whether they have been in before, and books the new-patient exam on your schedule while your team stays with the patient in the room. The visit is captured instead of lost to the office down the road.</p>'},
        {"h2_html": "Built around how a <em>chiropractic office runs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your phone does not ring on a schedule, and it rings hardest at the exact times your team cannot reach it. People call first thing in the morning, on a lunch break, or right after they get off work, and those are the same hours you are stacked with back-to-back adjustments. A voicemail box cannot answer a nervous first-time caller, and a generic call center does not know a new-patient consult from a routine visit, or that soreness after a car accident is a different conversation than a wellness check.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers around the clock, including the evenings and weekends when someone in pain is searching and every other office is closed.</li><li>Knows a new patient from an existing one and routes each the way you would.</li><li>Asks what brings the caller in, back pain, a stiff neck, headaches, an accident, sciatica, and gathers the details your intake needs.</li><li>Books the new-patient exam on your real availability, then sends the confirmation and reminder so the first visit actually shows.</li><li>Answers the two questions that scare a first-timer off, do you take my insurance and what does the first visit cost, the way you tell it to.</li></ul>'},
        {"h2_html": "One new patient is a <em>care plan, not one visit</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This is why a missed call costs a chiropractor more than almost any other business. A new patient rarely comes in once. The first exam turns into an initial course of adjustments over the following weeks, and from there into the maintenance and wellness visits that can continue for years, along with the family members and coworkers they send you once they trust you. So the call you lose on a Saturday is not one appointment. It is the whole relationship, handed to whoever answered the phone. You do not need to catch many of those for it to change the month, and everything the receptionist books after the first save is on top.</p>'},
        {"h2_html": "You own the number, the calls, and the <em>patient list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing office number, or a new one registered in your name, not ours. Every caller, every reason for a visit, and every booked new patient is yours and exportable any time, so the list you build is an asset you keep instead of something you rent back month to month. The AI receptionist is one piece of the Top Shelf platform, and it hands every new patient it books to the same CRM that follows up and brings people back, so no one you capture slips away before their first adjustment.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A Saturday back spasm, booked while you are <em>with a patient</em>",
        "body_html": 'It is Saturday morning and someone bends to pick up a laundry basket and their lower back locks up. They search for a chiropractor and call the first three that come up. Two ring out to voicemail. Yours answers, stays calm, asks what happened and whether they have seen a chiropractor before, confirms you take their insurance, and books a new-patient exam for Monday at 9. Your front desk never left the patient they were rooming. You open the schedule Monday to a new patient already on it, with the reason for the visit and their number attached, instead of a weekend voicemail from someone who has already booked elsewhere. Illustrative example, not a client.'},
    "faqs": [
        ("Does it work with my current office phone number?",
         'Yes. It can answer on your existing number, or set up a new one registered in your name. Either way the number and every new-patient call that comes through it belong to you and go with you if you ever leave.'),
        ("Can it handle new-patient calls the way my front desk would?",
         'Yes, that is the point. It asks what brings the caller in, whether they are new or existing, and the insurance and intake questions you rely on, then books the new-patient exam on your schedule. You decide exactly what it asks and how it answers.'),
        ("What about the questions a first-time caller always asks?",
         'Do you take my insurance and what does the first visit cost are the two that scare people off, and it answers both the way you tell it to. A calm, clear answer in the moment is what turns a nervous caller into a booked new patient.'),
        ("Will it actually book the visit, or just take a message?",
         'It books. The new-patient exam lands on your real availability, and the patient gets a confirmation and reminder so the first visit shows. You get the details right away, and it flags anything unusual for your team to handle.'),
        ("How fast can it be answering?",
         'Setup is included with no separate onboarding fee. We configure your intake questions, your schedule, and your insurance answers for you, so it is answering in days, not weeks.')],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for chiropractors"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-chiropractors.html", "The CRM that follows up on every new patient you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing new patients to <em>voicemail</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
},
# ============================== CRM for Chiropractors ==============================
{
    "slug": "crm-for-chiropractors",
    "trade_slug": "chiropractors", "trade_plural": "chiropractors",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "CRM for Chiropractors",
    "title": "CRM for Chiropractors | Top Shelf Business Solutions",
    "og_title": "CRM for Chiropractors",
    "meta_desc": "A CRM for chiropractors follows up on every new-patient lead and brings back patients who dropped off their care plan, so your schedule fills back up.",
    "service_schema_name": "CRM for Chiropractors",
    "eyebrow": "For Chiropractors",
    "h1_html": "CRM <em>for Chiropractors</em>",
    "answer_block": "A CRM for chiropractors keeps every new-patient lead, active patient, and care plan in one place and follows up for you, so the person who called last week and the patient who dropped off their plan three months ago both come back to you instead of searching all over again. The schedule you already earned fills itself back up.",
    "sections": [
        {"h2_html": "The patients who dropped off their plan are the visits you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most chiropractic offices do not have a new-patient problem so much as a follow-up problem. A patient starts a care plan, feels better halfway through, and quietly stops booking. Life gets busy, the pain fades, and they never come back for the visits that would have kept them well, until it flares up again and they search for a chiropractor from scratch as if they never knew you. That patient was never really gone. They just needed a reason and a nudge to come back, and that is the thing no one at a busy front desk has time to do by hand.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every one of those patients in front of you and reaches back out on a schedule you set, with texts and emails that go out on time whether or not anyone remembers. The patient who fell off at visit six hears from you before their back sends them somewhere else, and the table fills back up with someone who already trusts you.</p>'},
        {"h2_html": "Recall and reactivation is the <em>goldmine in your files</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The patients you have already treated are the cheapest visits a chiropractor can book. They know your table, they trust your hands, and their next flare-up, their spouse, and their kids are all yours if you stay in touch. But no one can personally remember to reach back out to a few thousand past patients, so most of that recurring work drifts to whoever they find online once they have forgotten your name.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every patient, their visit history, and their care-plan status live in one place instead of a paper chart and memory.</li><li>Recall messages go out on schedule, a nudge when a patient is due and a check-in when one goes quiet, so people come back before their pain does.</li><li>You can see at a glance who has not been in for a while and reach the right patient with the right message at the right time.</li><li>A reactivation message to your inactive list can fill a slow week with patients who were always yours to bring back.</li></ul>'},
        {"h2_html": "The lead that called but never booked is <em>still yours to win</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not everyone books on the first call. Someone phones to ask whether you take their insurance, says they will check their schedule and call back, and then never does, not because they chose another office but because the day got away from them. A single follow-up a day or two later, a friendly note that you have a spot for them and can answer any question, is often all it takes to turn that maybe into a first visit. The CRM sends it for you, so the leads that used to evaporate turn into new patients on the schedule instead.</p>'},
        {"h2_html": "You own the list, and it works with the <em>rest of the system</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every patient and every note is yours and exportable any time, not locked inside software you rent. The CRM is one piece of the Top Shelf platform and connects to the AI receptionist, so a new patient it books lands in your database and gets followed up on automatically, and to online booking, so a scheduled visit is logged against the right patient with their full history already attached. Nothing you have earned goes cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The patient who fell off their plan, <em>back on the table</em>",
        "body_html": 'A patient comes in for lower-back pain, starts a care plan, and after a handful of visits feels good enough to stop booking. Normally that is the last you see of them until they hurt themselves again and start over with whoever comes up first on their phone. Instead, a few weeks after they go quiet, the CRM sends a warm check-in, and a gentle reminder a while later that you are here whenever they need a tune-up. When their back tightens up after a long weekend, yours is the name already in their phone, and they book with you without shopping around. No one at the front desk had to remember to chase them. Illustrative example, not a client.'},
    "faqs": [
        ("Does it import my existing patients and visit history?",
         'Yes. Your current patients, leads, and visit history come in and live in one place, and everything stays yours and exportable. The point is to make the patient list you have already built actually work for you.'),
        ("Can it bring back patients who dropped off their care plan?",
         'Yes, that is where it earns its keep. It reaches patients who have gone quiet with recall and check-in messages on a schedule you set, so people come back for the visits that keep them well instead of waiting until the pain returns and searching again.'),
        ("Will it follow up on new-patient leads that did not book?",
         'Yes. When someone calls to ask about insurance or says they will call back, the CRM sends a friendly follow-up a day or two later for you, so the leads that used to slip away turn into first visits.'),
        ("How is this different from the software I already chart in?",
         'Charting software records the visit. It does not reach back out to a patient who stopped coming, remind you who is due, or tell you which lead is going cold. The CRM does all of that on a schedule, so the recurring visits actually show up instead of depending on anyone remembering.'),
        ("How long until it is set up?",
         'Setup is included with no separate onboarding fee. We bring in your patients, build your recall and follow-up sequences, and connect it to your calls and schedule, so it is working in days.')],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for chiropractors"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-chiropractors.html", "The AI receptionist that feeds it every new-patient call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting patients and leads <em>go cold</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
},
# ============================ Marketing for Chiropractors ============================
# ========================= Websites for Chiropractors =========================
{
    "slug": "websites-seo-for-chiropractors",
    "trade_slug": "chiropractors", "trade_plural": "chiropractors",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "Websites for Chiropractors",
    "title": "Websites for Chiropractors | Top Shelf Business Solutions",
    "og_title": "Websites for Chiropractors",
    "meta_desc": "A chiropractor website built for SEO ranks for chiropractor near me and back pain in your city, then books the new patient in one tap, not a directory.",
    "service_schema_name": "Websites for Chiropractors",
    "eyebrow": "For Chiropractors",
    "h1_html": "Websites <em>for Chiropractors</em>",
    "answer_block": "A chiropractor website built for SEO ranks for what a person in pain types, chiropractor near me, back pain, sciatica, your city, and lets them book a new-patient visit in one tap, so the patient is yours instead of a directory renting your calls back to you.",
    "sections": [
        {"h2_html": "The directories are renting you back <em>your own patients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for a chiropractor in your town and the top of the page is often a big health directory or a booking middleman, not the local office. Those sites publish thousands of pages and have years of authority behind them, so when a person in pain searches, they land there first, pick from a list that may put the offices paying the most on top, and book through a platform that treats your own patient as a lead it owns. Your site not ranking is not a vanity problem. It is the reason a new patient who should have found you directly gets routed through a directory that lines your competitors up beside you and takes a cut of a relationship that could have lasted years.</p>'},
        {"h2_html": "Rank for what a person in pain <em>actually types</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national directory this year for the broadest terms, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you serve, and for the exact searches someone makes when they hurt: chiropractor near me, back pain relief in your city, sciatica, neck pain, headaches, or care after a car accident. Pages built around what you actually treat and the areas you actually cover are what search engines, and people in pain, reward with the click. That is the ground a local chiropractor can win, and hold.</p>'},
        {"h2_html": "A person in pain should book in <em>one tap</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone hurting is on their phone, not a desktop, and they are not going to read three screens about your technique. The site has to load fast, put your reviews and a clear new-patient booking button in front of them right away, and make starting a first visit obvious and easy. A person in pain who can pick a time and book in one tap will do it before they close the tab. Make them hunt for a phone number and call during office hours and they book with whoever made it easier. A fast site with simple new-patient booking is what turns a searcher into a patient on the schedule.</p>'},
        {"h2_html": "The patients are <em>yours, permanently</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you put into a directory listing or a pay-per-lead service disappears the day you stop paying, and the patient was never really yours anyway. A website you own keeps ranking, keeps booking new patients, and keeps compounding in value for as long as it exists, and it is registered to you, not a platform that can drop you or sell the spot beside you to another office. The site plugs into the same CRM that follows up on every new patient it books and the AI receptionist that answers the callers who would rather talk than tap, so nothing it earns you slips away.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A late-night search that finds <em>you, not a directory</em>",
        "body_html": 'Someone two neighborhoods over has been putting up with lower-back pain for a week and finally, at ten at night, searches for a chiropractor near them on their phone. Instead of a national directory that would list three offices and book through its own platform, they find your site ranking for that area, with a page about back pain, real reviews near the top, and a new-patient booking button right there. They pick Tuesday at 8am and book before they put the phone down. You wake up to a new patient on the schedule, with their name and reason for the visit attached, and no middleman ever touched it. Illustrative example, not a client.'},
    "faqs": [
        ("Will my site actually outrank the big health directories?",
         'Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the pain and condition searches a national directory has no reason to target well, which is exactly where a local chiropractor can win.'),
        ("How is this different from paying a directory or lead service?",
         'A directory or pay-per-lead service rents you a patient it also shows to your competitors, and it stops the day you stop paying. A website you own books patients who are yours alone and keeps working long after it is built, with no per-lead fee coming out of every new relationship.'),
        ("Can new patients book their first visit right on the site?",
         'Yes. A clear new-patient booking button lets someone pick a time and book in one tap on their phone, and it lands on your real schedule with a confirmation and reminder. For the caller who would rather talk, the AI receptionist books them too.'),
        ("Most of my new patients are in acute pain. Does a website even help?",
         'Especially then. A person in pain searches on their phone in the moment, and the chiropractor who shows up with a fast page, real reviews, and one-tap booking gets them. A site built for that moment is exactly what captures the new patient.'),
        ("How long until it starts ranking?",
         'Local, specific searches can start moving within weeks, while broader terms take longer and compound over months. Setup is included with no separate fee.')],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for chiropractors"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
},
]
