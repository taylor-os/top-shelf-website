"""Colony page specs for CHIROPRACTORS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a chiropractic-office owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, chiropractor-specific substance (the generator owns
shell, schema, events, keyword placement). Same honesty rules as the money specs: no invented
stats, prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500
plans, $1,500 one-time site) ever appear; no em/en dashes anywhere; never "leak" as a metaphor.
Ethics: the AI receptionist does scheduling and intake only, never medical advice, and nothing
here makes a health, pain-relief, or treatment-outcome claim.

Six questions, mixed cost / problem / how-to, funneling into four money pages:
  1 chiropractor-website-cost              (cost)     -> websites-seo-for-chiropractors
  2 chiropractic-answering-service-cost    (cost)     -> ai-receptionist-for-chiropractors
  3 is-a-crm-worth-it-for-a-chiropractor   (cost)     -> crm-for-chiropractors
  4 why-chiropractors-miss-calls           (problem)  -> ai-receptionist-for-chiropractors
  5 why-chiropractic-patients-drop-off     (problem)  -> crm-for-chiropractors
  6 how-do-chiropractors-get-more-patients (how-to)   -> marketing-for-chiropractors
"""

TOPICS = [
# ==================== How Much Does a Chiropractor Website Cost? (cost -> websites-seo) ====================
{
    "slug": "chiropractor-website-cost",
    "h1": "How Much Does a Chiropractor Website Cost?",
    "title": "How Much Does a Chiropractor Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A chiropractor website is worth what it books, turning a chiropractor near me search into a booked first visit. Top Shelf builds yours for $1,500 one-time, or free on any plan.",
    "answer": "A chiropractor website can run from a couple hundred dollars for a template to several thousand custom, but the number that matters is how many new patients it books. It has to make booking a first visit the obvious action and rank for chiropractor near me. Top Shelf builds one for $1,500 one-time, or free on any plan.",
    "sections": [
        {"h2_html": "What a chiropractic website has to <em>do first</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For a chiropractor, the website has one job before any other: turn a person searching in pain into a booked first visit. New patients are the whole game, because a first exam is usually the start of a care plan rather than a one-off, so the single most important thing on the page is a clear new-patient offer and a book your first visit button a hurting person can tap on a phone in seconds. Everything else on the site either supports that one action or it is decoration.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A first-time visitor is also nervous, because they have never been adjusted and do not know what they are signing up for. A chiropractic site earns the booking by telling them plainly what a first visit involves, the exam and consultation, and how care usually works from there, so what lies ahead feels understandable instead of open-ended. A page that answers what happens when I come in removes the hesitation that makes someone close the tab and keep scrolling down the results.</p>'},
        {"h2_html": "What actually makes it <em>worth the money</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Whether you pay a little for a template you build yourself or more for a custom site with ongoing SEO, the site is only worth what it books, and a chiropractic site books new patients when it does a handful of specific things well.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It ranks for chiropractor near me and the towns you serve, because a person whose back gave out is searching on a phone for someone close by, right now.</li><li>It answers the money question a shopper checks first: whether you take their insurance, and what cash or wellness plan options look like if you do not, so cost is not the reason they call someone else.</li><li>It builds trust before they ever walk in, with real patient reviews near the top and a plain description of the doctor and how you approach care, because letting a stranger work on their spine takes reassurance.</li><li>It loads fast and puts the book your first visit button in front of them at once, so a person in pain acts before they close the tab.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf builds a custom five page site that does all of that for $1,500 one-time, yours to keep and host anywhere, or included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that pays for itself",
    "bridge_text": "A chiropractor website is only worth what it brings in. Ours is built to rank for the towns you cover and turn a search in pain into a booked new patient, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-chiropractors",
    "bridge_label": "Websites & SEO for chiropractors",
    "faqs": [
        ("What makes a chiropractor website worth paying for?",
         "The new patients it books. A site that ranks for chiropractor near me, answers the insurance question, shows real reviews, and lets someone book a first visit in one tap earns back its cost quickly, because a new patient is usually a course of care and not a single appointment. A cheap page that does none of that is the expensive one."),
        ("Do I still need a website if most of my patients come from referrals?",
         "Yes. Referrals still look you up before they book, and a slow or bare site can lose the patient a friend just sent you. It also captures the people searching chiropractor near me who have no referral at all, and unlike a paid directory that rents you a patient it also shows your competitors, a site you own keeps booking new patients with no per-lead fee.")],
    "trade_slug": "chiropractors", "trade_plural": "chiropractors",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ What Does a Chiropractic Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "chiropractic-answering-service-cost",
    "h1": "What Does a Chiropractic Answering Service Cost?",
    "title": "What Does a Chiropractic Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for chiropractors often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for chiropractors usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call and books the new-patient visit comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. A chiropractic office also gets its calls in bursts, first thing in the morning, over the lunch break, and right after people get off work, which are the same hours the front desk is stacked with patients. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of wrong numbers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a nervous first-time caller with questions costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a person whose back just locked up does not leave a voicemail, they call the next chiropractor on the list. The real cost of no coverage is not a monthly fee, it is the new patient who booked the office that picked up, and because a new patient usually starts a whole course of care, that is a care plan lost, not one visit. But a generic call center reading a script cannot screen a new-patient consult from a routine visit, or answer the two questions that decide the call, do you take my insurance and what does the first visit cost, so you can pay for coverage and still lose the booking.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, screens what brings the caller in, answers the insurance and cost questions the way you tell it to, and books the new-patient exam on your schedule. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. It handles scheduling and intake only and hands anything clinical to your team, it never gives medical advice. One new patient it books can be worth well more than the plan costs, and everything it catches after that is on top.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers every call, screens the reason for the visit, and books the new patient, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-chiropractors",
    "bridge_label": "AI receptionist for chiropractors",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the new patient it books instead of losing to voicemail, which is often a whole care plan."),
        ("Does it give medical advice or diagnose symptoms?",
         "No. It handles scheduling and intake only. It screens the reason for the visit so it can book the right appointment and route the caller, and it hands anything clinical straight to your team. It never offers medical advice or promises about treatment.")],
    "trade_slug": "chiropractors", "trade_plural": "chiropractors",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============== Is a CRM Worth It for a Chiropractor? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-chiropractor",
    "h1": "Is a CRM Worth It for a Chiropractor?",
    "title": "Is a CRM Worth It for a Chiropractor? | Top Shelf Business Solutions",
    "meta_desc": "For most chiropractors a CRM pays for itself by bringing back one patient who dropped off a care plan and reviving cold leads. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most chiropractic offices, yes. A CRM pays for itself the first time it brings back a patient who dropped off a care plan, or revives a lead who called once and never booked. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a chiropractic office when you have more past patients and new-patient leads than you can personally keep track of, which is most established practices. It is not worth it if you are brand new, seeing a handful of patients a week, and genuinely following up with all of them, though that rarely stays true as you grow. The honest test is simple: how many patients started a care plan and quietly stopped coming partway through, and how many people called to ask about insurance and never booked? Those are the visits a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a chiropractor is not the software, it is the work that stops slipping away. A patient who started feeling better and fell off at visit six, a lead who called on their lunch break and never called back, a past patient you have not seen in a year: each one is a visit you have already half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every new-patient lead that did not book, so someone who called once keeps hearing from you instead of drifting to another office.</li><li>It sends recall and check-in messages on a schedule, so patients come back for the rest of the care their plan called for instead of only when the pain returns.</li><li>It keeps your whole patient list, visit history, and care-plan status in one place instead of a chart and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: bring back one patient who would have lapsed and it has paid for itself, and because that patient is often a full course of care, everything after that is margin.</p>'}],
    "bridge_h2": "Put your patient list to work",
    "bridge_text": "The past patients and leads you already have are the cheapest visits you can book. A CRM follows up on every one for you, so they come back to you instead of searching from scratch when the pain returns.",
    "bridge_slug": "crm-for-chiropractors",
    "bridge_label": "CRM for chiropractors",
    "faqs": [
        ("Is a CRM overkill for a small or solo practice?",
         "Not usually. Even a solo office sees more patients and takes more new-patient calls than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If patients drop off their plans and leads never hear back, a CRM earns its keep."),
        ("How is a CRM different from the software I chart in?",
         "Your charting or EHR software records the visit. It does not reach back out to a patient who stopped coming, remind you who is due, or flag a lead going cold. A CRM does all of that on a schedule, so the recurring visits show up instead of depending on anyone remembering.")],
    "trade_slug": "chiropractors", "trade_plural": "chiropractors",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ Why Do Chiropractors Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-chiropractors-miss-calls",
    "h1": "Why Do Chiropractors Miss So Many Calls?",
    "title": "Why Do Chiropractors Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Chiropractors miss calls because the doctor is adjusting and the front desk is with a patient, and a person in pain does not leave a voicemail, they call the next office.",
    "answer": "Chiropractors miss calls because they ring while the doctor is adjusting a patient and the front desk is rooming, verifying insurance, or checking someone out. A person in pain does not leave a voicemail. They hang up and call the next chiropractor. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when your <em>hands are full</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A chiropractic office is a hands-full place all day. When the phone rings the doctor is mid-adjustment with a patient on the table, and the front desk is rooming the next one, verifying benefits, or checking someone out. None of those are moments anyone can stop and take a call. The busier the schedule, the more calls ring through, which means your best days are also the ones where the most new patients slip away. It is not a discipline problem. A small team cannot care for the patient in the room and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for someone in pain it is not one. A person who woke up with a neck they cannot turn is not going to leave a message and wait for a callback. They move down the search results until someone answers, and by the time the front desk checks the voicemail, that new patient is already booked somewhere else.</p>'},
        {"h2_html": "A missed call is a lost care plan, not a <em>lost visit</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal, and for a chiropractor the expensive ones are the new patients. New-patient acquisition is the whole game, because a first exam rarely ends at one visit. It becomes an initial course of adjustments, then the maintenance visits that follow, plus the family and coworkers a happy patient sends your way. So the call you miss is not one appointment, it is a whole relationship handed to whoever picked up. The calls most likely to roll to voicemail, the ones during the morning rush or after you have closed, are exactly the ones worth the most.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that answers every time and knows a new patient from an existing one. A voicemail box cannot screen a caller, and a generic call center does not know a new-patient consult from a routine visit, or answer the insurance question that decides whether a first-timer books. What actually works is something that answers on the first ring, asks what brings the caller in, confirms what they need to hear about insurance and cost, and books the new-patient exam or routes the call to your team. It handles scheduling and intake only and never gives medical advice, so the booking is captured without the call ever going to voicemail.</p>'}],
    "bridge_h2": "Stop losing new patients to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, screens what brings the caller in, and books the new-patient visit or routes it to your team, so the patient never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-chiropractors",
    "bridge_label": "AI receptionist for chiropractors",
    "faqs": [
        ("Would a patient rather reach a real person?",
         "What a first-time caller in pain needs most is a calm voice that answers, hears why they are calling, and gets them booked, which beats a voicemail box every time. The AI receptionist is upfront about what it is, handles the scheduling and intake, and routes anything clinical to your team."),
        ("Can I just send calls to the front desk voicemail instead?",
         "You can, but voicemail only helps if the caller leaves one, and a person in pain usually will not. It also cannot answer the insurance question or book the visit. Something that always answers and books is what catches the new patients a voicemail would lose.")],
    "trade_slug": "chiropractors", "trade_plural": "chiropractors",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ Why Do Chiropractic Patients Drop Off Partway Through Care? (problem -> crm) ============
{
    "slug": "why-chiropractic-patients-drop-off",
    "h1": "Why Do Chiropractic Patients Drop Off Partway Through Care?",
    "title": "Why Do Chiropractic Patients Drop Off Partway Through Care? | Top Shelf Business Solutions",
    "meta_desc": "Most chiropractic patients drop off not because they are unhappy but because they felt better partway and nobody followed up. A nudge is what brings them back to finish care.",
    "answer": "Most chiropractic patients drop off partway through a care plan not because they are unhappy, but because they started to feel better, got busy, and nobody followed up. They meant to book the next visit and life got in the way. A patient who goes quiet is usually not gone for good, they are a lapse that never got a nudge.",
    "sections": [
        {"h2_html": "Dropping off usually means busy, not <em>unhappy</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a patient who stops booking as one who was unhappy, so you let them go and move on. But most of the time they did not decide against you at all. They started a care plan, began feeling better a few visits in, meant to keep coming, and then life crowded it out. Work, kids, and a back that no longer hurts as much all pushed the next appointment down the list, and a few weeks later they had drifted off the plan without ever deciding to. Ask them and they would say they liked coming in and just fell out of the habit.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The patients who finish a plan are usually not the ones who needed it most. They are the ones who got a nudge at the right time: a friendly reminder that they are due, a quick check-in when they went quiet. That second touch is what turns a lapse back into a booked visit, and it is exactly the thing there is no time for between patients on a full day.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Front desks do not skip follow-up because they are lazy. They skip it because the day fills up. You room the next patient, take the calls you can, handle the walk-in, and by closing the patient who missed last week is out of sight. Doing it from memory means it only happens when things are slow, which is exactly when you have the fewest patients to bring back.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system flagging which patients are due or have quietly gone quiet.</li><li>The follow-up depends on someone remembering, so it competes with the patients in front of them and loses.</li><li>By the time anyone circles back, the patient has moved on, and only searches again when the pain returns.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not an effort problem, and it is the kind of thing you fix once and it just runs. When every patient who is due or has gone quiet gets a timed recall or check-in automatically, written to sound like your office, people come back for the rest of the care their plan called for, and the schedule you already earned stops slipping away.</p>'}],
    "bridge_h2": "Bring back the patients who fell off",
    "bridge_text": "A CRM keeps every patient and care plan in front of you and sends recall and check-in messages for you, so a patient who felt better and stopped booking hears from you before their back sends them somewhere else.",
    "bridge_slug": "crm-for-chiropractors",
    "bridge_label": "CRM for chiropractors",
    "faqs": [
        ("How many times should I follow up with a patient who dropped off?",
         "A couple of light touches over a few weeks catches most of the lapses without being pushy: a reminder when they are due, then a warm check-in if they go quiet. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated recall feel impersonal?",
         "Not when it is written to sound like your office and sent at a sensible pace. A short, friendly check-in reads as caring, not spammy, and most patients appreciate the nudge because they meant to come back and forgot. You can always reach out to anyone directly.")],
    "trade_slug": "chiropractors", "trade_plural": "chiropractors",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ How Do Chiropractors Get More Patients? (how-to -> marketing) ============
{
    "slug": "how-do-chiropractors-get-more-patients",
    "h1": "How Do Chiropractors Get More Patients?",
    "title": "How Do Chiropractors Get More Patients? | Top Shelf Business Solutions",
    "meta_desc": "Chiropractors get more patients by being the visible, well-reviewed, easy-to-book option the moment someone nearby searches in pain, then following up so none slip away.",
    "answer": "Chiropractors get more patients by being the visible, trusted, easy-to-book option at the moment someone nearby searches in pain. In practice that means a Google Business Profile and reviews strong enough to win the map pack, a site that books a new patient in one tap, and follow-up so the leads and patients you earn do not slip away.",
    "sections": [
        {"h2_html": "New patients start with a local search in a moment of <em>pain</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody shops around for a chiropractor for weeks. Someone tweaks their back, wakes up with a neck they cannot turn, or feels a fender-bender the next morning, and they want to see someone close by and soon. That makes new patients intensely local, because a person in pain is not driving across the metro for a weekly adjustment, and it makes them cautious, because they are about to let a stranger work on their spine. So getting more patients is not about shouting to a whole city. It is about being the office a nearby searcher finds and trusts at the exact moment they decide to act.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">When that search happens, the map pack, those three local listings with the star ratings, is the first thing they see, above the websites and the ads. And because trust matters so much here, they read the reviews closely before they pick. The chiropractor with a current, well-reviewed profile wins the click over the one whose listing has sat untouched for a year. Get found and trusted first, and the new patient is usually yours.</p>'},
        {"h2_html": "The levers that actually <em>bring patients in</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more patients is less about one clever trick and more about keeping a handful of local basics strong at the same time, which is exactly what slips when the office is busy caring for patients. A steady routine beats good intentions.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep your Google Business Profile verified, complete, and active with current photos and hours, so it looks legitimate to a searcher and to Google.</li><li>Ask every happy patient for a review at the right moment, right after a visit, and reply to each one, so the reputation that wins the map pack keeps building.</li><li>Rank for the towns and neighborhoods you serve and the searches people make in pain, so you show up where a nearby patient is actually looking.</li><li>Make booking a first visit one tap on a phone, so a person in pain acts before they close the tab instead of calling the office that made it easier.</li><li>Follow up on leads and past patients, so the patients you earn keep coming back instead of only ever chasing new ones.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Done together and kept up consistently, these compound: more reviews lift you in local search, which brings more patients, which brings more reviews. What no honest company can promise is a specific spot on the map or a set number of patients, because Google decides that, but these are the levers that move it, and a free audit will show you where you stand today.</p>'}],
    "bridge_h2": "Be the chiropractor they find first",
    "bridge_text": "Most new patients start with a local search in a moment of pain. Keeping your Google profile active, your reviews strong, and your booking one tap is how you become the office they pick when their back gives out nearby.",
    "bridge_slug": "marketing-for-chiropractors",
    "bridge_label": "Marketing for chiropractors",
    "faqs": [
        ("What is the fastest way to get more new patients?",
         "Usually the quickest lever is your Google Business Profile and reviews. A verified, active profile with recent, genuine reviews can climb in the map pack within weeks, and the map pack is where most local patients in pain start. It moves faster than most other channels and it compounds."),
        ("Do I have to run ads to get more patients?",
         "No. Most of the levers that bring in local patients, a strong Google profile, steady reviews, ranking for your towns, and one-tap booking, are things you build and own rather than rent. Ads can add reach on top, but the foundation that keeps working without a daily spend is local visibility and follow-up.")],
    "trade_slug": "chiropractors", "trade_plural": "chiropractors",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
]
