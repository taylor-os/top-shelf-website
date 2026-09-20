"""Colony page specs for OPTOMETRISTS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question an optometry-practice owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, optometry-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear; no em/en dashes anywhere; "find the gap", never "leak".

What makes optometry distinct from the other medical trades: the practice makes its money twice
from the same person, once for the eye exam and again at the optical retail dispensary (glasses,
prescription sunglasses, a year of contact lenses). So the annual-exam recall is the whole
retention engine, a CRM that reminds patients they are due is the single biggest lever, an
expiring contact-lens prescription is a built-in reason to rebook, the vision-plan versus medical-
insurance question eats the front-desk phone, and a missed call loses the exam AND the eyewear
sale to the next office. Every scenario is illustrative, never a named client or competitor.

Medical ethics (non-negotiable): the AI receptionist does scheduling, intake, and logistics only,
never eye-care or vision advice; no page makes a health, treatment, or vision-outcome claim;
patient information is treated with the discretion a medical office is held to (HIPAA-aware).

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 optometrist-website-cost                     (cost)     -> websites-seo-for-optometrists
  2 optometry-answering-service-cost             (cost)     -> ai-receptionist-for-optometrists
  3 is-a-crm-worth-it-for-an-optometry-practice  (cost)     -> crm-for-optometrists
  4 why-optometry-offices-miss-calls             (problem)  -> ai-receptionist-for-optometrists
  5 why-optometry-patients-dont-return-annually  (problem)  -> crm-for-optometrists
  6 how-do-optometrists-get-more-patients        (how-to)   -> marketing-for-optometrists
"""

TOPICS = [
# ==================== How Much Does an Optometrist Website Cost? (cost -> websites-seo) ====================
{
    "slug": "optometrist-website-cost",
    "h1": "How Much Does an Optometrist Website Cost?",
    "title": "How Much Does an Optometrist Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "An optometrist website is two storefronts in one: it books the eye exam and merchandises your retail optical. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "An optometrist website can run from a couple hundred for a template to several thousand custom. Yours does two jobs a medical site never does: it books the eye exam and it is the front window of your retail optical. Top Shelf builds a custom five page site for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "Your website is a storefront for the <em>optical</em>, not just a booking page",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Optometry is unusual in the medical field, because you are running two businesses on one floor: the eye exam in the back, and a retail optical up front that sells frames, prescription lenses, sunglasses, and a year of contact lenses. Most medical offices sell a service and nothing else. You sell a service and a product line, and often half the value of a visit walks out in a bag from the optical. That changes what your website has to do. It is not just a page that books an appointment, it is the front window of a shop, and the questions people bring to it are retail questions as much as anything clinical.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Which frame brands and designer lines you carry, because a shopper deciding where to go often decides on selection.</li><li>Whether they can put their vision benefits, a VSP or EyeMed plan, toward glasses or contacts with you.</li><li>Whether a current wearer can start a contact-lens reorder or book the exam that renews an expiring prescription.</li><li>What owning the site really costs: who holds it, what a change to your frame lineup costs, and whether you keep it if you leave.</li></ul>'},
        {"h2_html": "What an optometry site has to do that a <em>service page cannot</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An optometry website earns its money twice from one visitor: it books the eye exam, and it sells the eyewear that rides on top of it. So it has to load fast, rank for the searches people actually make, an optometrist near them, one who takes their vision plan, an eye exam and glasses for the kids before school, and it has to merchandise the optical the way a retail site would, showing the frame lines you carry and making it plain that vision benefits are welcome. It should let a contact-lens wearer start a reorder or book the exam that renews an expiring prescription, so you catch them before they price a box against an online seller. A handsome site that never ranks, hides your frame selection, and buries your number is the most expensive kind, because you paid for it and it books no exams and sells no eyewear.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that fills the exam chair",
    "bridge_text": "An optometry website is only worth the patients it books. Ours is built to rank for the towns you serve and turn a search into a booked exam, then wired to follow up on every one with recall and reorder reminders.",
    "bridge_slug": "websites-seo-for-optometrists",
    "bridge_label": "Websites & SEO for optometrists",
    "faqs": [
        ("Can my website show the frames I carry, not just book exams?",
         "Yes. It can present the frame brands and lines you carry so a shopper sees your selection before they walk in, signal that vision benefits are welcome, and point contact-lens wearers to book the exam that renews an expiring prescription. It works as the front window of your optical, not just an appointment page."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "optometrists", "trade_plural": "optometrists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ======== What Does an Optometry Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "optometry-answering-service-cost",
    "h1": "What Does an Optometry Answering Service Cost?",
    "title": "What Does an Optometry Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "At an optometry front desk much of the phone is retail: glasses-ready, frame brands, VSP benefits, contact reorders. Top Shelf includes an AI receptionist that answers all of it 24/7 in the $899/mo Signature plan.",
    "answer": "Optometry answering services bill per call, per minute, or on a retainer, so a busy month gets expensive fast, and much of it is retail: are my glasses ready, do you carry this frame, does my VSP plan work here. Top Shelf includes an AI receptionist that answers all of it and books the exam in the $899 Signature plan.",
    "sections": [
        {"h2_html": "The optometry phone is a <em>retail counter</em>, not a clinical line",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An optometry front desk does not field the calls a purely clinical office does. So much of what comes in is retail: is my order of glasses ready, are my contacts in yet, do you carry a certain frame brand, can I put my VSP or EyeMed benefit toward a pair, my contact prescription expired and I need to reorder. The rest is the routine exam booking and the occasional urgent eye problem. A per-minute service reading a generic script cannot handle a single one of the retail calls, so you end up paying a meter for coverage that still lets the eyewear sale walk. It helps to know how these services usually charge before you sign up.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for every call answered, including the run of are-my-glasses-ready status calls that tie up a person but book nothing.</li><li>Per-minute pricing: you pay for talk time, so a caller working through their vision benefits or comparing frames costs more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of calls, and you pay extra past it, usually right when the optical is busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is not just the exam. A caller who reaches a voicemail does not leave a message, they call the next optometrist, and what walks away is the exam, the glasses or contacts that ride on top of it, the vision benefits they were about to spend with you, and often the whole family. The real cost of no coverage is that lost sale, not a monthly fee. But a generic call center cannot tell a caller whether you take their VSP or EyeMed plan, whether a medical eye problem runs through their health insurance instead, or whether their glasses are ready, and it cannot get them booked, so you can pay for coverage and still lose all of it.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, tells people your hours and whether their vision plan works with you, confirms whether an order of glasses or contacts is ready the way you tell it to, books the exam on your calendar, and flags an urgent eye problem to your team. It sticks to scheduling, intake, and order status, and never gives eye-care or vision advice, and it treats what a caller shares with the discretion a medical office is held to. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter. One exam and eyewear sale it saves on a weekend can be worth well more than the plan costs, and everything after that is on top. It does not replace your opticians, it hands the calls that need a person straight to them.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers around the clock, handles the vision-plan and insurance questions, and books the exam, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-optometrists",
    "bridge_label": "AI receptionist for optometrists",
    "faqs": [
        ("Can it handle the are-my-glasses-ready calls that tie up my optical?",
         "Yes, those routine order-status calls are exactly what it takes off your team. It can confirm whether an order of glasses or contacts is ready the way you tell it to, answer whether you take a caller's vision plan, and book the exam, so nobody has to leave the optical floor to pick up. It sticks to scheduling and order status and hands anything unusual to a person."),
        ("Is an AI receptionist cheaper than a live per-call service?",
         "Usually, and far more predictable. A live service that bills per call or per minute climbs exactly when the optical is busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the exam and the eyewear sale it books instead of losing to voicemail.")],
    "trade_slug": "optometrists", "trade_plural": "optometrists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============== Is a CRM Worth It for an Optometry Practice? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-an-optometry-practice",
    "h1": "Is a CRM Worth It for an Optometry Practice?",
    "title": "Is a CRM Worth It for an Optometry Practice? | Top Shelf Business Solutions",
    "meta_desc": "For most optometry practices a CRM pays for itself by reviving patients overdue for their annual exam and reminding contact-lens wearers to reorder. It comes in the Signature plan at $899/mo.",
    "answer": "For most optometry practices, yes. A CRM pays for itself the first time it brings back a patient overdue for their annual exam, or reminds a contact-lens wearer to book before their prescription lapses. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for an optometry practice when you have more patients, contact-lens wearers, and unscheduled exams than the front desk can personally keep track of, which is nearly every established office. It is not worth it if you are brand new with a handful of patients you genuinely reach every time, though that rarely stays true as you grow. The honest test is simple: how many patients have not been in for their annual exam in over a year, and how many contact-lens wearers let their prescription lapse and reordered from a website instead of booking with you? Those are the visits a CRM is built to recover. Most established practices are not short on demand, they are short on the follow-up that turns a due patient or an expiring prescription into a booked exam, and that is the gap it fills.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for an optometry practice is not the software, it is the exams and eyewear that stop slipping away. An eye exam plus an optical dispensary is the whole business, so the annual recall is the retention engine, and a patient reminded that they are due is the single biggest lever you have. A family overdue for their yearly exams, a contact-lens wearer whose supply is about to run out, a patient who talked about a second pair of sunglasses and never came back: each one is a visit you have already half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It fires annual recall reminders, so the patient whose year is up books again without your team tracking dates by hand.</li><li>It sends contact-lens reorder and renewal reminders before a wearer runs out, right when an expiring prescription means they need an exam to keep their lenses coming, instead of drifting to an online seller.</li><li>It keeps every patient, their last exam, their prescription, and when they are due in one place, so your list becomes your schedule instead of just a record of who came in.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one lapsed patient or one contact-lens reorder and it has paid for itself, and everything after that is revenue you would have lost. Patient information is handled with the care a medical office is held to and stays yours to export.</p>'}],
    "bridge_h2": "Put your patient list to work",
    "bridge_text": "The patients you have already seen are the easiest exam chair to fill. A CRM reaches out to every one who is due for their annual exam or about to run out of contacts, so they book with you instead of drifting to another office or an online seller.",
    "bridge_slug": "crm-for-optometrists",
    "bridge_label": "CRM for optometrists",
    "faqs": [
        ("Is a CRM overkill for a small optometry practice?",
         "Not usually. Even a single-doctor office has more patients due for their annual exam and more contact-lens wearers due to reorder than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If patients lapse and prescriptions expire unnoticed, a CRM earns its keep."),
        ("How is a CRM different from my practice management or EHR software?",
         "Practice software records who came in and stores the chart. A CRM sits alongside it as the outreach layer, reminding a patient their annual exam is due, nudging a contact-lens wearer before their prescription lapses, and reviving one who has not been in for a year, on a schedule, so the list does the work instead of just sitting there.")],
    "trade_slug": "optometrists", "trade_plural": "optometrists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ Why Do Optometry Offices Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-optometry-offices-miss-calls",
    "h1": "Why Do Optometry Offices Miss So Many Calls?",
    "title": "Why Do Optometry Offices Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Optometry offices miss calls because the phone rings while the front desk is on the optical floor, and a caller who reaches voicemail books the next optometrist instead.",
    "answer": "Optometry offices miss calls because the phone rings while the one person up front is on the optical floor fitting frames or checking a patient out, and a caller who reaches voicemail does not leave a message. They book the next optometrist, and the exam and eyewear sale go with them. The fix is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when the front desk is <em>on the optical floor</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">In most optometry offices the person who answers the phone is also running the optical. When it rings, they are helping a patient narrow down frames, adjusting a pair that sits crooked, walking someone through pretesting on the autorefractor, or checking a patient out at the optical counter, and the call rings through to voicemail while the one person up front is a few feet away with their hands full. The busier the optical, the more calls slip, which means your best days are also the ones where the most patients go unanswered. It is not a discipline problem. One or two people cannot run the front of the office and catch every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a patient booking an eye exam it is not one. Someone calling around, comparing a couple of offices or trying to get the kids seen before school, is not going to leave a message and wait for a callback. They move down the list until a real voice picks up and books them, and by the time anyone checks the voicemail, that patient and the eyewear that comes with them are already at another office.</p>'},
        {"h2_html": "A missed call is the exam <em>and the eyewear</em> you lose",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A missed new patient is the most expensive one, because an optometry practice makes its money twice from the same person: the exam, and then the optical that sits on top of it, a pair of glasses, prescription sunglasses, a year of contact lenses, and the household who follow once they trust you. So a single missed call is rarely one exam. It is the annual exams, the eyewear, and the family that walk to whoever answered. Those calls also come when the front desk is least able to grab them: the lunch hour, the rush at open, and the evenings and weekends when someone finally has a minute to book.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never goes to voicemail and can actually help the caller. A voicemail box cannot tell a caller whether you take their vision plan or get them booked, and a generic call center does not know a vision plan from medical insurance or a routine exam from an eye that needs to be seen today. What works is something that answers on the first ring day or night, handles the vision-plan and insurance questions, books the exam on your calendar, and flags an urgent eye problem to your team, all while sticking to scheduling and intake and never offering eye-care advice, so the patient is booked instead of lost.</p>'}],
    "bridge_h2": "Stop sending exams and eyewear to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, handles the vision-plan and scheduling questions, and books the exam or flags an urgent eye problem to your team, so a new patient never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-optometrists",
    "bridge_label": "AI receptionist for optometrists",
    "faqs": [
        ("Would a patient rather reach a real person?",
         "What a caller needs most is a real answer and an appointment, and a calm voice that handles their vision-plan question and books the exam beats a voicemail box every time. The AI receptionist is upfront about what it is, sticks to scheduling and intake, and hands anything urgent straight to your team."),
        ("Can I just forward calls to a cell phone instead?",
         "You can, but that only helps when someone is free to answer. Forwarding still rolls to voicemail when the whole team is on the optical floor or already on another call. Something that always answers, handles the routine questions, and books the exam is what catches the calls a forward would still miss.")],
    "trade_slug": "optometrists", "trade_plural": "optometrists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ Why Don't Optometry Patients Come Back Every Year? (problem -> crm) ============
{
    "slug": "why-optometry-patients-dont-return-annually",
    "h1": "Why Don't Optometry Patients Come Back Every Year?",
    "title": "Why Don't Optometry Patients Come Back Every Year? | Top Shelf Business Solutions",
    "meta_desc": "Most optometry patients don't return annually because nobody reminded them, not because they left. The prescription quietly expired, and without a recall nudge they lapse.",
    "answer": "Most optometry patients who do not come back have not left you. They walked out meaning to return in a year, the prescription quietly expired, and without a recall reminder the annual exam fell off their calendar. A patient who goes quiet is usually not gone, they just never got the nudge that they are due.",
    "sections": [
        {"h2_html": "Not returning usually means forgotten, not <em>gone</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a patient who has not been in for a year as one who found another optometrist, so you stop thinking about them. But most of the time they did not choose to leave at all. They came in for their exam, you told them to come back in a year, and then work, kids, and a dozen other things got in the way. The prescription quietly expired, a canceled appointment never got rescheduled, and one year became two. They are not upset with you, they simply forgot, and nobody reminded them their annual exam was due.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The same thing happens with contact lenses. A wearer buys a year of lenses, leaves happy, and the next you hear from them is whenever they notice the box is empty, which might be at your office or might be at a website that does not care whether the prescription is current. An expiring prescription is a built-in reason to book the exam that renews it, but only if someone reaches out before the supply runs out. Left to memory, the reorder and the exam behind it both drift away. The return was never lost to a competitor. It was lost to silence.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Optometry teams do not skip recall because they do not care. They skip it because the front desk is full. The same person is checking patients in and out, answering the phone, verifying vision plans, and running the optical floor, and working a list of who is overdue for their annual exam is the thing that never rises to the top on a busy day. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest exams on the books.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system flagging which patients are due or overdue for their annual exam and which contact-lens prescriptions are about to lapse.</li><li>The reminder depends on someone at the desk remembering, so it competes with the patients standing right in front of them and loses.</li><li>By the time anyone reaches out, the patient has drifted, or reordered contacts from an online seller when they finally went looking.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not an effort problem, and it is the kind of thing you set up once and it just runs. When every patient due for their annual exam and every contact-lens wearer nearing a reorder gets a warm, timed reminder automatically, written to sound like the office they already trust, the exam chair fills from the list you already have instead of the revenue quietly slipping away. Their information stays handled with the care a medical office is held to, and every message is one you approve.</p>'}],
    "bridge_h2": "Bring every patient back on schedule",
    "bridge_text": "A CRM keeps every patient due for their annual exam and every contact-lens wearer nearing a reorder in front of you and sends the reminders for you, so your patient list fills the exam chair instead of drifting away.",
    "bridge_slug": "crm-for-optometrists",
    "bridge_label": "CRM for optometrists",
    "faqs": [
        ("How often should we remind a patient who is overdue for an exam?",
         "A couple of light touches works better than one, and better than nagging: a friendly note when their annual exam is due, another when they are overdue, and one more if a contact-lens prescription is about to lapse. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated recall feel impersonal to patients?",
         "Not when it is written to sound like your office and sent at a sensible pace. A short, warm reminder that they are due for their annual exam reads as a practice that is on top of things, not a mass blast, and most patients are glad for the nudge because they meant to book and forgot. You can always reach out to anyone directly.")],
    "trade_slug": "optometrists", "trade_plural": "optometrists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ======== How Do Optometrists Get More Patients? (how-to -> marketing) ========
{
    "slug": "how-do-optometrists-get-more-patients",
    "h1": "How Do Optometrists Get More Patients?",
    "title": "How Do Optometrists Get More Patients? | Top Shelf Business Solutions",
    "meta_desc": "Optometrists get more patients by being found as the place to get the eye exam and buy the eyewear: rank in the map pack, name the vision plans you take, and answer every call.",
    "answer": "Optometrists get more patients by being found as the place to get the eye exam and buy the eyewear. That means ranking in the local map pack for exam-and-glasses searches, making it obvious you take their VSP or EyeMed benefits, and answering the calls that result. Most patients, and the eyewear they buy, are lost before they ever reach you.",
    "sections": [
        {"h2_html": "New patients are shopping for an exam <em>and an optical</em> at once",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more optometry patients is not the same problem as filling a purely clinical schedule, because the person searching is usually shopping for two things at once: someone to give them an eye exam, and somewhere to buy the glasses or contacts that come out of it. They search for an optometrist near them, for an eye exam and glasses, for a place that takes their VSP or EyeMed benefits, or for a contact-lens fitting. What they pick is a provider and a store in one decision. That is your opening, and it runs through what they see the moment they search.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The first thing Google shows is not a website, it is the map pack, the little map with three local practices, their star ratings, and a call button, and most people choose from those three before scrolling. Getting seen there runs on a handful of things you can actually influence.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A Google Business Profile that is verified, complete, and active, and that lists plainly that you sell eyewear and fit contacts, not just exams.</li><li>A steady flow of recent, genuine reviews, which is what makes a shopper pick you over the big-box optical down the road.</li><li>The vision plans you accept named clearly, because whether their VSP or EyeMed benefit works with you is the first thing many people check.</li><li>A consistent name, address, and phone number across the web, so Google trusts you are one real practice.</li></ul>'},
        {"h2_html": "Being found is wasted if the exam, the eyewear, or the <em>reorder</em> slips away",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Ranking is only the first half. A shopper who finds you still has to get an answer and an appointment, and this is where practices quietly lose the patients their marketing worked to attract. They tap your listing and land on a site that does not say whether their vision plan works with you or show the frames you carry, or they call and reach a voicemail while the one person up front is on the optical floor, and they move on to the next optometrist, taking the exam and the eyewear with them. Getting found and then dropping the call is paying for a door nobody can open.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So more patients is really one connected system, not a single trick: a profile and reviews that get you seen as the place to spend vision benefits and buy eyewear, a fast site that names your plans and shows your frames, a phone that always gets answered, and recall that brings a patient back each year when their prescription is up and reaches a contact-lens wearer before they reorder from a website. A reminder that unused vision benefits reset at year end can fill a slow December on its own. Top Shelf runs those pieces together on one platform, starting at $299 a month, so a patient found on Google is one that gets booked, sold, and kept. What no honest company can promise is a specific ranking or a set number of patients, because no one controls Google, but a free audit will show you exactly where you are losing them today.</p>'}],
    "bridge_h2": "Get found where new patients look",
    "bridge_text": "Most new patients start with a search and pick from the map pack. Marketing that keeps your profile active, your reviews growing, and your site answering the vision-plan question is how you get chosen when someone nearby needs an optometrist.",
    "bridge_slug": "marketing-for-optometrists",
    "bridge_label": "Marketing for optometrists",
    "faqs": [
        ("Should I market the eye exam or the eyewear?",
         "Both, because they are one decision to the shopper. The strongest pull is being the obvious place to use a VSP or EyeMed benefit and buy the frames you carry, with the exam as the reason to come in. A profile and site that make all of that clear beat one that only mentions exams."),
        ("How long until I see more new patients?",
         "A neglected profile that gets verified, completed, and active, with reviews coming in steadily, can start climbing within a few weeks and compounds from there. Nobody controls Google, so no honest company promises a specific position or patient count, but consistency on the profile and reviews is what moves it.")],
    "trade_slug": "optometrists", "trade_plural": "optometrists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
]
