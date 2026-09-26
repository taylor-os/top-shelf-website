"""Colony page specs for PHYSICAL THERAPISTS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a physical-therapy-clinic owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, physical-therapy-specific substance (the generator owns
shell, schema, events, keyword placement). Same honesty rules as the money specs: no invented
stats, prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500
plans, $1,500 one-time site) ever appear; no em/en dashes anywhere; never "leak" as a metaphor.
Ethics: the AI receptionist does scheduling and intake only, never medical or clinical advice,
and nothing here makes a recovery, pain-relief, or treatment-outcome claim or guarantee.

What makes physical therapy different from the other medical trades (lead with this): the clinic
runs on TWO patient engines at once, physician and surgeon referrals plus direct-access
self-referrals (and a growing cash-pay wellness/performance side), and the business is a PLAN OF
CARE, a prescribed course of many visits. So a missed new-referral call hands a whole episode of
care (and the referral relationship behind it) to whoever answered, and a patient who drops off
mid-plan is the single biggest lost revenue, which is exactly what CRM check-ins and
authorization/visit-limit tracking are built to recover.

Six questions, mixed cost / problem / how-to, funneling into four money pages:
  1 physical-therapy-website-cost                    (cost)     -> websites-seo-for-physical-therapists
  2 physical-therapy-answering-service-cost          (cost)     -> ai-receptionist-for-physical-therapists
  3 is-a-crm-worth-it-for-a-physical-therapy-clinic  (cost)     -> crm-for-physical-therapists
  4 why-physical-therapy-clinics-miss-calls          (problem)  -> ai-receptionist-for-physical-therapists
  5 why-physical-therapy-patients-drop-off           (problem)  -> crm-for-physical-therapists
  6 how-do-physical-therapists-get-more-patients     (how-to)   -> marketing-for-physical-therapists
"""

TOPICS = [
# ============ How Much Does a Physical Therapy Website Cost? (cost -> websites-seo) ============
{
    "slug": "physical-therapy-website-cost",
    "h1": "How Much Does a Physical Therapy Website Cost?",
    "title": "How Much Does a Physical Therapy Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A physical therapy website ranges from cheap templates to several thousand for a custom build. What matters is whether it books both referred and direct-access patients. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A physical therapy website runs from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters is whether it earns trust from both channels you rely on: patients a physician or surgeon referred, and people who found you searching. Top Shelf builds one for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a physical therapy site actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Price follows the job, and a physical therapy site has a specific job a generic small-business template was never built for. Your schedule fills from two directions: patients a physician or surgeon sent for rehab after a surgery or an injury, and direct-access patients who searched for therapy on their own. A referred patient almost always looks the clinic up before calling, to see whether you are credible and whether you take their coverage, so the site has to reassure the patient and the office that referred them both. That is a different brief than a template that lists a few services and calls it done.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Make it clear which insurance plans you accept, and that you handle workers-comp and auto-injury cases, because those patients and their case managers confirm coverage before they book.</li><li>Answer the two questions that stall a new patient up front: whether you take their plan, and whether they need a physician referral to start or can come in direct.</li><li>Give a referring office a clean way to send a patient over, and give a self-referral a booking button they can tap before they close the tab.</li><li>Load fast on a phone and rank for the towns you cover, so the direct-access half of your schedule can find you at all.</li></ul>'},
        {"h2_html": "What it costs, and why one evaluation is worth an <em>episode</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Here is what changes the math for a physical therapy clinic in particular. A new patient is not a single visit, it is an episode of care: an evaluation followed by a defined course of visits over weeks that runs until the therapist discharges the patient, often longer after a major surgery. So a site that books even a few evaluations a month is not paying for appointments, it is paying for whole episodes, and for the referral relationship behind each one. That is why hiding your booking button or letting the site sit unranked is the costly mistake, not the build fee itself.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps the pricing plain. A custom five page site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that gets it ranking is handled for you, and there is no setup fee either way. Before you sign with anyone, ask who owns the site, what a change costs, and whether you keep it if you leave. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit will show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that pays for itself",
    "bridge_text": "A physical therapy website is only worth what it brings in. Ours is built to rank for the towns you cover and turn a referral or a local search into a booked evaluation, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-physical-therapists",
    "bridge_label": "Websites & SEO for physical therapists",
    "faqs": [
        ("Will the site bring in referrals, or only people searching on their own?",
         "Both, and they need different things. A referred patient usually looks you up to confirm you are credible and take their coverage before they call, so the site is built to reassure them and to make your accepted plans, workers-comp, and auto-injury cases clear. A self-referral needs to find you in search and book in one tap. The site is built for both, not just one."),
        ("Do I own the website, or am I renting it?",
         "You own it. The one-time $1,500 site is yours to keep. On a monthly plan it is built for you as part of the plan, and before you sign anything we tell you plainly what a change costs and what happens to the site if you ever leave.")],
    "trade_slug": "physical_therapists", "trade_plural": "physical therapists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ==== What Does a Physical Therapy Answering Service Cost? (cost -> ai-receptionist) ====
{
    "slug": "physical-therapy-answering-service-cost",
    "h1": "What Does a Physical Therapy Answering Service Cost?",
    "title": "What Does a Physical Therapy Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for physical therapists bill per call or minute, which punishes your busiest days and mishandles referrals. Top Shelf includes an AI receptionist that books evaluations in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for physical therapists bill per call, per minute, or a retainer, so the busy stretches cost the most, and a live script cannot tell a referral from a routine call. Top Shelf includes an AI receptionist that answers every call and books the evaluation in the Signature plan at $899 a month flat, no per-call fee.",
    "sections": [
        {"h2_html": "Why the meter is the wrong model for a <em>referral-driven clinic</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A physical therapy clinic does not get the same calls as a walk-in business, so paying by the call or the minute fits it badly. Your phone carries a scheduler from a referring surgeon sending a post-op patient, a case manager on a workers-comp or auto-injury claim who needs to confirm coverage, a self-referral whose knee gave out, and existing patients moving a visit. Those calls come in bursts at open, over lunch, and after work, the same hours the front desk is already on the floor, and a per-call or per-minute meter charges you the most in exactly those busy stretches. It helps to know the models before you sign one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: every call adds to the bill, so a good week of referrals and new patients is punished rather than rewarded.</li><li>Per-minute pricing: a case manager verifying an auto-injury claim or a nervous post-op caller with questions runs the clock and the cost.</li><li>Monthly retainer plus overage: a bucket of minutes you blow through in the busy season and pay past exactly when your volume is highest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What a dropped referral call costs, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is not the fee you save, it is the referral you keep. When a referred patient cannot get through, they book the next clinic on the sheet, and the surgeon or physician who sent them notices that their patient could not get in. Those relationships are the lifeblood of a physical therapy clinic, slow to build and quick to lose, so a call that rolls to voicemail can cost far more than one evaluation. A generic call center reading a script cannot tell a referral from a reschedule, note that you handle a workers-comp or auto-injury case, or answer whether a patient needs a referral to start, so you can pay for coverage and still lose both the booking and the referral behind it.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, tells a referral from a self-referral from an existing patient, asks whether a doctor sent them, answers the insurance and referral questions the way you tell it to, and books the evaluation on your schedule. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter. It handles scheduling and intake only and routes anything clinical to your team, it never gives medical advice or makes any promise about treatment. Because a new evaluation is a whole episode of care that runs to discharge, one booking it saves can be worth well more than the plan, and everything after that is on top.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers every call, tells a referral from a reschedule, and books the evaluation, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-physical-therapists",
    "bridge_label": "AI receptionist for physical therapists",
    "faqs": [
        ("Can it handle a physician referral or a workers-comp intake, not just take a message?",
         "Yes. It tells a referral from a self-referral from an existing patient, asks whether a doctor sent them, notes a workers-comp or auto-injury case for your team to verify, and books the evaluation on your schedule. It captures what your intake needs so the referral does not get lost to voicemail."),
        ("Does it give any medical or clinical advice?",
         "No. It does scheduling and intake only. It screens the reason for the visit so it can book the right evaluation and route the caller, and it hands anything clinical straight to your team. It never offers medical advice and makes no promise about treatment or recovery.")],
    "trade_slug": "physical_therapists", "trade_plural": "physical therapists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ======== Is a CRM Worth It for a Physical Therapy Clinic? (cost -> crm) ========
{
    "slug": "is-a-crm-worth-it-for-a-physical-therapy-clinic",
    "h1": "Is a CRM Worth It for a Physical Therapy Clinic?",
    "title": "Is a CRM Worth It for a Physical Therapy Clinic? | Top Shelf Business Solutions",
    "meta_desc": "For most physical therapy clinics a CRM pays for itself by bringing back one patient who dropped off a plan of care and reviving cold referrals. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most physical therapy clinics, yes. A CRM pays for itself the first time it brings back a patient who dropped off a plan of care, or revives a referral who called once and never scheduled. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a physical therapy clinic when you have more active plans of care, referrals, and discharged patients than anyone can personally keep track of, which is most established practices. It is not worth it if you are brand new, seeing a handful of patients a week, and genuinely following up with every referral and every patient who misses a visit, though that rarely stays true as you grow. The honest test is simple: how many patients started a plan of care and quietly stopped coming partway through, how many referrals called to ask about insurance and never booked, and how many discharged patients have not heard from you since. Those are the visits a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a physical therapy clinic is not the software, it is the work that stops slipping away. A patient who felt better and fell off partway through a plan of care, a referral who called on a lunch break and never scheduled, a patient you discharged a year ago whose old injury just flared up: each one is a visit you have already half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every referral and new-patient lead that did not book, so someone who called once keeps hearing from you instead of drifting to another clinic.</li><li>It sends check-in reminders to patients who miss a visit, so more plans of care get completed instead of abandoned halfway.</li><li>It keeps an eye on authorized visits so your front desk can re-authorize before a patient runs out mid-plan and their care is interrupted.</li><li>It sends check-ins to discharged patients, so a tweaked knee or a new injury comes back to you instead of a fresh search.</li><li>It keeps your whole patient list, referral history, and plan-of-care status in one place instead of a chart and someone remembering.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one patient who would have lapsed and it has paid for itself, and because that patient is often the back half of a plan of care, everything after that is margin.</p>'}],
    "bridge_h2": "Put your patient list to work",
    "bridge_text": "The referrals, active plans, and discharged patients you already have are the cheapest visits you can book. A CRM follows up on every one for you, so they come back to you instead of starting a search from scratch.",
    "bridge_slug": "crm-for-physical-therapists",
    "bridge_label": "CRM for physical therapists",
    "faqs": [
        ("Is a CRM overkill for a small or solo clinic?",
         "Not usually. Even a solo clinic carries more active plans of care, referrals, and discharged patients than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If patients drop off mid-plan and referrals never hear back, a CRM earns its keep."),
        ("How is a CRM different from the software I document visits in?",
         "Your documentation or EMR software records the visit and the plan. It does not reach back out to a patient who stopped coming, flag who is running low on authorized visits, or chase a referral that never scheduled. A CRM does all of that on a schedule, so the recurring visits show up instead of depending on anyone remembering.")],
    "trade_slug": "physical_therapists", "trade_plural": "physical therapists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ======== Why Do Physical Therapy Clinics Miss So Many Calls? (problem -> ai-receptionist) ========
{
    "slug": "why-physical-therapy-clinics-miss-calls",
    "h1": "Why Do Physical Therapy Clinics Miss So Many Calls?",
    "title": "Why Do Physical Therapy Clinics Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Physical therapy clinics miss calls because therapists are on the floor and the front desk is buried, and a patient holding a referral does not wait, they book the clinic that answered.",
    "answer": "Physical therapy clinics miss calls because they ring while the therapist is on the floor with a patient and the front desk is rooming, verifying benefits, or checking someone out. A patient holding a referral does not leave a voicemail, they book the clinic that answers. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when your <em>team is on the floor</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A physical therapy clinic is a hands-full place all day. When the phone rings, your therapists are out on the floor with patients, counting reps, setting up a machine, guiding someone through a balance drill, and the front desk is rooming the next patient, verifying benefits, or checking someone out. None of those are moments anyone can step away to catch a call. The busier the schedule, the more calls ring through, which means your best days are also the ones where the most new patients and referrals slip away. It is not a discipline problem. A small team cannot treat the patient in the room and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for someone who needs therapy it is not one. A patient just handed a referral by their surgeon, or a self-referral whose back locked up this morning, is not going to leave a message and wait for a callback. They work down the list until someone answers, and by the time the front desk checks the voicemail, that patient is already booked somewhere else.</p>'},
        {"h2_html": "A missed call is a lost plan of care, and a lost <em>referral source</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal, and for a physical therapy clinic the expensive ones are the new evaluations. A first evaluation rarely ends at one visit, it becomes a plan of care, a course of visits several times a week over weeks, and longer after a major surgery, until the patient is discharged. So the call you miss is not one appointment, it is a whole episode of care handed to whoever picked up. Worse, when a referred patient cannot get in, the surgeon or physician who sent them hears about it, and referral sources quietly remember which clinics answer and which ones do not.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that answers every time and knows a referral from a reschedule. A voicemail box cannot screen a caller, and a generic call center does not know an evaluation from a routine visit, or answer the insurance and referral questions that decide whether a first-timer books. What actually works is something that answers on the first ring, asks what brings the caller in and whether a doctor sent them, confirms what they need to hear about insurance and cost, and books the evaluation or routes the call to your team. It handles scheduling and intake only and never gives medical advice, so the booking is captured without the call ever going to voicemail.</p>'}],
    "bridge_h2": "Stop losing referrals to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, tells a referral from a reschedule, and books the evaluation or routes it to your team, so the patient and the referral behind them never roll to voicemail.",
    "bridge_slug": "ai-receptionist-for-physical-therapists",
    "bridge_label": "AI receptionist for physical therapists",
    "faqs": [
        ("Would a patient rather reach a real person?",
         "What a caller in pain or holding a fresh referral needs most is a calm voice that answers, hears why they are calling, and gets them booked, which beats a voicemail box every time. The AI receptionist is upfront about what it is, handles the scheduling and intake, and routes anything clinical to your team."),
        ("Can I just send calls to the front desk voicemail instead?",
         "You can, but voicemail only helps if the caller leaves one, and a patient with a list of in-network clinics usually will not. It also cannot answer the insurance or referral question or book the evaluation. Something that always answers and books is what catches the patients a voicemail would lose.")],
    "trade_slug": "physical_therapists", "trade_plural": "physical therapists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ==== Why Do Physical Therapy Patients Drop Off Partway Through Care? (problem -> crm) ====
{
    "slug": "why-physical-therapy-patients-drop-off",
    "h1": "Why Do Physical Therapy Patients Drop Off Partway Through Care?",
    "title": "Why Do Physical Therapy Patients Drop Off Partway Through Care? | Top Shelf Business Solutions",
    "meta_desc": "Physical therapy patients drop off when they feel better before the prescribed episode is done, or when insurance authorization runs out mid-plan. Both are fixable with timed reminders and re-auth alerts.",
    "answer": "Physical therapy patients drop off for two fixable reasons: they start feeling better and stop before the prescribed episode of care is finished, or their insurance authorization runs out mid-plan and no one re-authorized in time. Either way a defined course of visits ends early, and a timed nudge or a re-auth reminder is what keeps them on the schedule.",
    "sections": [
        {"h2_html": "An episode of care is meant to end in <em>discharge</em>, not drift",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A physical therapy plan of care is a defined thing. The evaluation sets a course of visits over a set number of weeks, and it is meant to end one way, with the therapist discharging the patient once the episode is complete. Dropping off is what happens when the episode ends the other way, early and not by the therapist, which is a different problem than a business where people simply come whenever they feel like it. The most common version is quiet: a patient comes in faithfully for the first week or two, starts feeling better, and decides on their own they are done, weeks before the prescribed course is finished. They were not discharged and they were not unhappy. They just stopped, and the back half of the episode, the visits already planned and authorized, never happened.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is the single biggest thing a physical therapy clinic loses, because the episode is the revenue and because the referring physician is watching whether their patient completed the course they were sent for. A patient who self-discharges early leaves authorized visits unused and shows up in the referral loop as a course that was not finished. The clinics that complete more episodes are not the ones with better luck, they are the ones where a patient who goes quiet gets a timed check-in before a missed week becomes a habit, which is exactly the work a full front desk has no time to do by hand.</p>'},
        {"h2_html": "Insurance authorization and visit limits end plans <em>before the patient does</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The second reason is one most businesses never deal with: the payer, not the patient, ends the plan. A course of physical therapy is usually authorized for a set number of visits, and when that authorization runs out or a visit cap is reached mid-plan, care stalls until someone requests more. If no one is watching the count, a patient partway through a plan gets stopped cold by paperwork and often does not come back once the visits pause. Workers-comp and auto-injury cases add another layer, where an adjuster or a claim has to keep pace or the visits halt. None of this is the patient choosing to leave. It is an administrative gap that quietly ends episodes the clinic wanted to finish.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Nobody is tracking which patients are close to their authorized visit limit until the front desk hits it at check-in.</li><li>A re-authorization request goes in late, so there is a gap in care the patient may never come back from.</li><li>A patient who felt better and one whose authorization lapsed look identical on the schedule, so both quietly fall off without a flag.</li><li>Workers-comp and auto-injury cases stall when the claim side goes quiet and no one follows up.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Both problems have the same fix, and it is a system, not more willpower. When every patient who goes quiet gets a timed check-in written to sound like your clinic, and the front desk sees who is nearing an authorized visit limit before it is reached, the episode gets a chance to finish the way it was meant to, and the schedule you already earned stops slipping away.</p>'}],
    "bridge_h2": "Bring back the patients who fell off",
    "bridge_text": "A CRM keeps every active plan of care in front of you and sends check-in reminders for you, so a patient who felt better and stopped booking hears from you before the back half of their plan slips away.",
    "bridge_slug": "crm-for-physical-therapists",
    "bridge_label": "CRM for physical therapists",
    "faqs": [
        ("Can it warn me before a patient runs out of authorized visits?",
         "Yes. It keeps each patient plan of care and authorized visit count in view, so your front desk can request a re-authorization before the limit is reached instead of discovering it at check-in. Catching it early is what keeps a plan from stalling in the middle."),
        ("Does an automated check-in feel impersonal to a patient?",
         "Not when it is written to sound like your clinic and sent at a sensible pace. A short, friendly check-in reads as a clinic that cares whether they finished, not as spam, and most patients appreciate the nudge because they meant to come back and life got in the way. You can always reach out to anyone directly.")],
    "trade_slug": "physical_therapists", "trade_plural": "physical therapists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ How Do Physical Therapists Get More Patients? (how-to -> marketing) ============
{
    "slug": "how-do-physical-therapists-get-more-patients",
    "h1": "How Do Physical Therapists Get More Patients?",
    "title": "How Do Physical Therapists Get More Patients? | Top Shelf Business Solutions",
    "meta_desc": "Physical therapists get more patients by keeping two engines full: physician referrals and direct-access local search, backed by reviews, one-tap booking, and follow-up so none slip away.",
    "answer": "Physical therapists get more patients from two engines at once: steady physician and surgeon referrals, and direct-access patients who search locally when they are in pain. In practice that means being reliable enough that referral sources keep sending, a Google profile and reviews strong enough to win the map pack, one-tap booking, and follow-up so none slip away.",
    "sections": [
        {"h2_html": "Physical therapy runs on two engines: <em>referrals and local search</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more patients is different for a physical therapy clinic than for most local businesses, because the patients come from two places at once. The first is referral relationships, the orthopedic surgeons, primary-care doctors, and specialists who send patients your way after an injury or a surgery. That business is won less by advertising and more by being the clinic that answers, gets the patient in quickly, and lets the physician see their patient was cared for, because a referral source that watches its patients get seen keeps sending more. The second engine is direct access: patients who skip the referral entirely and search for therapy near them when their back or knee gives out, along with a growing number of cash-pay wellness and performance clients who never had a referral to begin with.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">When that direct-access search happens, the map pack, those three local listings with the star ratings, is the first thing they see, above the websites and the ads. And because a patient is about to trust someone with their body, they read the reviews closely before they pick. The clinic with a current, well-reviewed profile wins the click over the one whose listing has sat untouched for a year. So more patients means keeping both engines running: staying reliable for the doctors who refer, and being easy to find and trust for the patients who search on their own.</p>'},
        {"h2_html": "The levers that actually <em>bring patients in</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more patients is less about one clever trick and more about keeping a handful of things strong at the same time, which is exactly what slips when the clinic is busy treating patients. A steady routine beats good intentions.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answer every call and follow up on every referral, so the physicians who send patients see them get in and keep sending more.</li><li>Keep your Google Business Profile verified, complete, and active with current photos and hours, so it looks legitimate to a searcher and to Google.</li><li>Ask every happy patient for a review at the right moment and reply to each one, so the reputation that wins the map pack keeps building.</li><li>Rank for the towns you serve and the searches people make in pain, so direct-access and cash-pay patients find you where they are actually looking.</li><li>Make booking an evaluation one tap on a phone, so a patient acts before they close the tab instead of calling the clinic that made it easier.</li><li>Follow up on leads, active plans, and discharged patients, so the patients you already earned keep coming back instead of only ever chasing new ones.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Done together and kept up consistently, these compound: more reviews lift you in local search, which brings more direct-access patients, while reliable intake keeps the referral pipeline warm. What no honest company can promise is a specific spot on the map or a set number of patients, because Google and your referral sources decide that, but these are the levers that move it, and a free audit will show you where you stand today.</p>'}],
    "bridge_h2": "Be the clinic they find and refer to first",
    "bridge_text": "Physical therapy patients come from referring physicians and from local search at once. Staying reliable for the doctors who send patients, and easy to find and book for the ones who search, is how you keep both engines full.",
    "bridge_slug": "marketing-for-physical-therapists",
    "bridge_label": "Marketing for physical therapists",
    "faqs": [
        ("What is the fastest way to get more new patients?",
         "There are two quick levers. Answer every referral call and get those patients in, which keeps your physician sources sending, and tighten up your Google Business Profile and reviews, which can climb in the map pack within weeks and is where most direct-access patients start. Both move faster than most other channels and compound."),
        ("Do I have to run ads to get more patients?",
         "No. Most of the levers that bring in patients, strong referral relationships, an active Google profile, steady reviews, ranking for your towns, and one-tap booking, are things you build and own rather than rent. Ads can add reach on top, but the foundation that keeps working without a daily spend is reliability, local visibility, and follow-up.")],
    "trade_slug": "physical_therapists", "trade_plural": "physical therapists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
]
