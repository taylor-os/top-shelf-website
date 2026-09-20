"""Per-page content specs for the SEO corpus (plan §5), physical therapists batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, physical-therapy-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the chiropractor, dentist, or dermatology content reworded.

Medical & Dental hub, alongside chiropractors, dentists, and dermatology. Four service angles are
here in one file (the ai-receptionist dict carries "demo": True). Kept deliberately distinct from
specs_chiropractors.py: physical therapy is episode-of-care rehab, a defined plan of care over many
visits and then a discharge, driven by physician referrals AND direct-access self-referral
(post-surgery, sports injury, back and knee rehab), not the indefinite wellness adjustments a
chiropractor sells. Referral relationships as a growth engine, empty treatment slots from no-shows,
insurance-authorized visit blocks, and reactivating a discharged patient for a new injury or a
flare-up are the physical-therapy angles the sibling pages never touch. Each example body ends with
the literal "Illustrative example, not a client." per the honesty rule; if the generator also
appends that line, dedupe there.
"""

SPECS = [
# ===================== AI Receptionist for Physical Therapists =====================
{
    "slug": "ai-receptionist-for-physical-therapists", "demo": True,
    "trade_slug": "physical_therapists", "trade_plural": "physical therapists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "AI Receptionist for Physical Therapists",
    "title": "AI Receptionist for Physical Therapists | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Physical Therapists",
    "meta_desc": "A physical therapy answering service answers every referral and new-patient call your front desk misses, screens the injury, and books the evaluation.",
    "service_schema_name": "AI Receptionist for Physical Therapists",
    "eyebrow": "For Physical Therapists",
    "h1_html": "AI Receptionist <em>for Physical Therapists</em>",
    "answer_block": "A physical therapy answering service answers every referral and new-patient call the moment it rings, day or night, works like a front desk that never leaves the floor, screens the injury and whether a physician sent them, and books the evaluation on your schedule. You keep your number, and every patient belongs to you.",
    "sections": [
        {"h2_html": "The call you miss is the referral that <em>books the next clinic on the list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone just came out of a knee replacement, or tweaked their back lifting a box, or walked out of an orthopedist appointment with a script for therapy in hand. They are motivated to start now, because they are in pain or a surgeon told them the first few weeks matter most. They call your clinic, and if no one picks up, they do not leave a voicemail and wait for a callback. A referred patient is holding a list of in-network clinics, and a self-referral just searched for physical therapy near them and is calling down the results. They book with whoever answers and gets them scheduled for an evaluation.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Your front desk is not ignoring the phone. In a lot of clinics the person who would answer it is also a therapist or an aide who is out on the floor with a patient, counting reps, setting up a machine, walking someone through a balance drill. They cannot step away in the middle of treatment to catch a ringing phone, so the call rolls to voicemail and the patient, along with the doctor who sent them, quietly goes to the clinic that picked up. Missing that call does more than cost you one evaluation. It tells a referring surgeon that their patient could not get in, and referral sources remember which clinics answer and which ones do not.</p>'},
        {"h2_html": "Built around how a <em>physical therapy clinic runs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your phone rings hardest at the exact times the front desk is most buried: first thing in the morning while you are opening and rooming the first patients of the day, over the lunch hour, and right after work when people call on the drive home. A voicemail box cannot take a referral or calm a nervous post-surgical patient, and a generic call center reading a script does not know an evaluation from a reschedule, or that a fresh rotator-cuff repair is a very different conversation than someone booking their next visit.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers around the clock, including the evenings and weekends when a self-referral in pain is searching and every clinic nearby is closed.</li><li>Knows a physician referral from a self-referral from an existing patient calling to move a visit, and handles each the way your front desk would.</li><li>Asks what is going on, a post-surgical knee, a sports injury, back or neck pain, a balance problem, and whether a doctor sent them with a script, so your intake has what it needs.</li><li>Books the evaluation on your real schedule, then sends the confirmation and reminder so the first visit actually shows.</li><li>Answers the two questions that stall a new patient, whether you take their insurance and whether they need a referral to start, the way you tell it to.</li></ul>'},
        {"h2_html": "One evaluation is a <em>whole plan of care</em>, not a single visit",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This is why a missed call costs a physical therapy clinic more than it first appears. A new patient almost never comes in once. An evaluation turns into a plan of care, a course of visits two or three times a week over several weeks, and longer still after a major surgery, until the patient is discharged. So the call you lose on a Friday afternoon is not one appointment. It is the entire episode of care, handed to whoever answered the phone, and often the referral relationship sitting behind it. You do not need to catch many of those for it to change the month, and everything the receptionist books after the first save is on top. When the phone is covered, the patient your marketing and your referring physicians worked to send you actually lands on the schedule instead of slipping away before the first visit.</p>'},
        {"h2_html": "You own the number, the patients, and the <em>schedule it fills</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing clinic number, or a new one registered to your practice, not to us. Every caller, every injury they described, and every evaluation it books is yours and exportable any time, so the patient list you are building stays an asset you own instead of something you rent back month to month. Because a caller is describing an injury or a surgery, it is built to handle what they share with the discretion a medical practice is held to, collecting only what it needs to book the visit and keeping it inside your systems. The answering service is one piece of the Top Shelf platform, and it hands every patient it books to the same CRM that follows up and brings people back, so no one you capture slips away before the evaluation.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A Friday post-op call, booked while your therapists are <em>on the floor</em>",
        "body_html": "It is late Friday afternoon and a woman two weeks out from shoulder surgery remembers her surgeon told her to start therapy right away, and the clinic he named is one of three on her referral sheet. She calls the first two. One rings out to a weekend voicemail, the other leaves her on hold. Yours answers, asks about the surgery, confirms you take her plan, and books her evaluation for Monday morning while your therapists never leave the patients they are treating. You open the schedule Monday to a new plan of care already on it, with the surgery and the referral noted, instead of a voicemail from someone who has already started somewhere else. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current clinic phone number?",
         "Yes. It can answer on your existing number, or set up a new one registered to your practice. Either way the number and every call that comes through it belong to you and go with you if you ever leave."),
        ("Can it handle referrals and new patients the way my front desk would?",
         "Yes, that is the point. It tells a physician referral from a self-referral from an existing patient rescheduling, asks what is going on and whether a doctor sent them, and books the evaluation on your schedule. You decide exactly what it asks and how it answers."),
        ("What about the insurance and referral questions every new patient asks?",
         "Whether you take their plan and whether they need a doctor's referral to start are the two that stall people, and it answers both the way you tell it to. A clear answer in the moment is what turns a caller into a booked evaluation."),
        ("Will it actually book the evaluation, or just take a message?",
         "It books. The evaluation lands on your real schedule, and the patient gets a confirmation and reminder so the first visit shows. You get the details right away, and it flags anything unusual for your team to handle."),
        ("How fast can it be answering?",
         "Setup is included with no separate onboarding fee. We configure your intake questions, your schedule, and your insurance answers for you, so it is answering in days, not weeks. Start with a free audit and we will show you how many new-patient and referral calls your current setup is missing.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for physical therapists"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-physical-therapists.html", "The CRM that follows up on every patient you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing referrals to <em>voicemail</em>",
    "cta_sub": "Get a free audit that finds the gap in your new-patient and referral calls: how many roll to voicemail and book elsewhere while your team is treating patients, whether you work with us or not. No credit card, never a call center.",
},
# ============================ CRM for Physical Therapists ============================
{
    "slug": "crm-for-physical-therapists",
    "trade_slug": "physical_therapists", "trade_plural": "physical therapists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "CRM for Physical Therapists",
    "title": "CRM for Physical Therapists | Top Shelf Business Solutions",
    "og_title": "CRM for Physical Therapists",
    "meta_desc": "A CRM for physical therapy clinics follows up on every referral and brings back past patients with a new injury, so your treatment schedule stays full.",
    "service_schema_name": "CRM for Physical Therapists",
    "eyebrow": "For Physical Therapists",
    "h1_html": "CRM <em>for Physical Therapists</em>",
    "answer_block": "A CRM for physical therapy clinics keeps every referral, active plan of care, and past patient in one place and follows up for you, so the patient who dropped out halfway through their plan and the one who finished rehab a year ago and just hurt something new both come back instead of starting over elsewhere.",
    "sections": [
        {"h2_html": "The patient who quits their plan of care early is the visits you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most physical therapy clinics do not have a referral problem so much as a follow-through problem. A patient starts a plan of care, comes in faithfully for the first week or two, and then starts to feel better. The pain eases, work gets busy, the drive starts to feel long, and they quietly stop booking the back half of the visits the therapist actually prescribed. They were not discharged. They dropped out, which means a weaker result for the patient, a worse outcome for the referring physician to see, and a block of authorized visits that never happens. That patient was not finished. They just needed a nudge to complete what they started, and that is exactly what no one at a busy front desk has time to chase by hand.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every active plan of care in front of you and reaches out on a schedule you set, with texts and emails that go out on time whether or not anyone remembers. The patient who missed this week hears from you before the gap becomes a habit, and the plan gets finished instead of abandoned, which is better for the patient, the outcome the physician sees, and the schedule all at once.</p>'},
        {"h2_html": "Discharged patients are the <em>reactivation goldmine</em> in your files",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The patients you have already treated are the cheapest visits a physical therapy clinic can book. Here is what makes physical therapy different from a one-and-done trade: you discharge people on purpose. A patient finishes a plan of care, gets better, and leaves, which is the goal, but it also means your best future patients are sitting in your files the day they walk out the door. Bodies do not stay fixed forever. The knee you rehabbed gets tweaked again, an old back injury flares up, a new sport or a new surgery sends the same person back to therapy, and their family and coworkers need a clinic too. But no one can personally remember to reach back out to a few thousand discharged patients, so most of that work drifts to whoever they find online once they have forgotten your name.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every patient, their diagnosis, their plan of care, and their discharge date live in one place instead of a chart and someone\'s memory.</li><li>Check-ins go out after discharge on the schedule you set, so a patient who tweaks something new thinks of you first instead of starting a search from scratch.</li><li>You can watch authorized visits running low and prompt the front desk to re-authorize before a patient runs out mid-plan and care gets interrupted.</li><li>A single reactivation message to your discharged list can fill a slow stretch on the schedule with patients who already know and trust your clinic.</li></ul>'},
        {"h2_html": "The referral who called but never scheduled is <em>still yours to win</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every referral turns into a booked evaluation on the first call. A patient phones to ask whether you take their insurance or whether the script their doctor wrote is enough to start, says they will check their schedule and call back, and then the day gets away from them. The physician did their part and sent the patient over, but the evaluation never made it onto the calendar, and a script sitting in a drawer helps no one. A single follow-up a day or two later, a friendly note that you have a spot for them and can answer any question about the referral or their coverage, is often all it takes to turn that maybe into a first visit. The CRM sends it for you, so the referrals that used to evaporate become plans of care on the schedule instead, and the physician who sent them sees that their patient actually got in. That reliability is its own kind of marketing, because a referral source that watches its patients get seen keeps sending more, while a clinic that lets referrals fall through the cracks quietly gets crossed off the list.</p>'},
        {"h2_html": "You own the list, and it works with the <em>rest of the clinic</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every patient and every note is yours and exportable any time, handled with the discretion a medical practice is held to, not locked inside software you only rent. The CRM is one piece of the Top Shelf platform and connects to the answering service, so a patient it books lands in your database and gets followed up on automatically, and to online booking, so a scheduled visit is logged against the right patient with the full history already attached. The list you have spent years building, and the referral relationships behind it, finally works for you instead of just recording who came in. Nothing you have earned goes cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The knee you rehabbed, back for a <em>new season</em>",
        "body_html": "You take a patient through a full plan of care for a knee, discharge him in good shape, and normally that is the last you see of him. Two years later he rolls an ankle in a weekend league. Because your CRM kept sending him the occasional check-in after discharge, yours is the clinic already in his phone, and he books an evaluation with you without searching or asking his doctor for a new name. No one at the front desk had to remember him. The same message went out to everyone discharged that quarter, and he is the one who happened to need it this month. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing patients and their plans of care?",
         "Yes. Your current patients, referrals, and visit history come in and live in one place, and everything stays yours and exportable. The point is to make the patient list you have already built actually work for you."),
        ("Can it bring patients back to finish a plan of care they dropped out of?",
         "Yes, that is where it earns its keep. It reaches patients who have stopped booking with check-in reminders on a schedule you set, so more plans of care get completed instead of abandoned halfway, which is better for the outcome and the schedule both."),
        ("Will it help me reactivate discharged patients?",
         "Yes. It sends check-ins after discharge, so when an old injury flares up or a new one happens, your clinic is the name they already have instead of a search they start over. A reactivation message to your whole discharged list can fill a quiet week."),
        ("Can it track insurance authorizations and visits remaining?",
         "It keeps each patient's plan and authorized visits in view so your front desk can see when someone is running low and re-authorize before their care gets interrupted mid-plan. You set the reminders, and the CRM surfaces who is due."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your patients, build your follow-up and reactivation sequences, and connect it to your calls and schedule, so it is working in days. Start with a free audit and we will show you where visits are slipping away today.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for physical therapists"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-physical-therapists.html", "The AI receptionist that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting plans of care and referrals <em>go cold</em>",
    "cta_sub": "Get a free audit that finds the gap in your follow-up and reactivation: how many patients dropped out of their plan and how many discharged patients are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ========================= Marketing for Physical Therapists =========================
{
    "slug": "marketing-for-physical-therapists",
    "trade_slug": "physical_therapists", "trade_plural": "physical therapists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "Marketing for Physical Therapists",
    "title": "Marketing for Physical Therapists | Top Shelf Business Solutions",
    "og_title": "Marketing for Physical Therapists",
    "meta_desc": "Physical therapy marketing keeps your Google profile and reviews strong, so a patient searching for physical therapy nearby finds and chooses you first.",
    "service_schema_name": "Marketing for Physical Therapists",
    "eyebrow": "For Physical Therapists",
    "h1_html": "Marketing <em>for Physical Therapists</em>",
    "answer_block": "Physical therapy marketing keeps you visible where patients now choose their own clinic, your Google Business Profile, your reviews, and the map pack, so when someone nearby searches for physical therapy after a surgery or an injury, your name is the active, well-reviewed one they pick instead of the clinic that let its profile go stale.",
    "sections": [
        {"h2_html": "Patients choose their own physical therapist <em>more than they used to</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Physical therapy used to run almost entirely on physician referrals, and those relationships still matter enormously. But direct access changed the game: in most places a patient can now begin therapy without waiting for a doctor to send them, which means more and more people look for a clinic the same way they look for everything else, by searching. Someone comes out of surgery, pulls something at the gym, or finally decides to deal with the back pain they have carried for months, and they search for physical therapy near them and start comparing. Even a patient a physician referred will often look the clinic up first, to see who they are about to trust with their recovery.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So the work has two halves. You still nurture the surgeons and primary-care doctors who send patients, and marketing here is about being the clinic a searching patient finds and trusts in the moment they decide to get help. It is intensely local, because a plan of care means coming in two or three times a week for weeks, and almost no one keeps that up across a whole metro. Get found and trusted first, close to where they live and work, and the patient is usually yours.</p>'},
        {"h2_html": "Your reviews and map pack <em>decide who they choose</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone searches for physical therapy near them, the map pack, those three local listings with the star ratings, is the first thing they see, above the websites and above the ads. And because handing someone the job of guiding a recovery takes trust, they read the reviews closely before they choose. A profile with recent, genuine reviews and current photos of the clinic and the team wins the click over one that has sat untouched for a year. Reviews and the map pack, more than almost anything else, decide which clinic a local searcher walks into.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The best moment to earn a review is the day a patient is discharged moving better than they arrived, back to their sport, their job, or their life without the pain that first sent them in. Asking every patient who finishes a plan of care right then, and replying to each review that comes back, feeds the profile that feeds the map pack, and the whole thing compounds: more reviews lift you in local search, which brings more patients, which brings more reviews. A review that describes walking normally again after a knee replacement, or getting back on the field, speaks straight to the next patient facing the very same thing.</p>'},
        {"h2_html": "Show up in the <em>towns you actually serve</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Marketing to a whole metro is expensive and forgettable, and it brings calls from people forty minutes away who will never keep a twice-a-week schedule that far from home. Physical therapy lives or dies on the patient actually coming in, again and again, until the plan of care is finished, so the patients worth reaching sit in a fairly tight radius around your clinic. Focusing your profile, your reviews, and your local content on the specific towns and neighborhoods you serve is what puts you in the map pack where you can win a patient who will actually complete their visits. It is a tighter, cheaper target than a citywide spend, and it is the one that turns into full plans of care rather than a single visit and a long drive nobody keeps up. A patient who books from across town might show for the evaluation and then quietly abandon the plan once the commute collides with work and life, so reaching the people genuinely near you is not only cheaper, it protects the completed plans of care your outcomes and your revenue both depend on.</p>'},
        {"h2_html": "Stay in front of the patients, and the doctors who <em>send them</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A steady local presence, current photos of your clinic, posts about what you treat, the occasional recovery tip, keeps your name familiar so that when an injury or a surgery finally sends someone looking, you are the clinic they already recognize. Familiarity is what tips a nervous first-timer toward a name they have seen before. And it works on the referral side too: a surgeon weighing where to send a patient, and a patient deciding whether to trust the clinic that surgeon named, both look you up, and a strong, active profile full of real reviews makes that an easy yes. This is the public-facing side of the clinic, aimed at people who are not your patients yet and the doctors deciding where to send them. The private follow-up and reactivation to people already in your files is the CRM, and the two work best together.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A torn something on Saturday, and you are <em>already at the top</em>",
        "body_html": "A weekend athlete feels a pop in her knee during a Saturday game and knows she will need therapy once a doctor clears her. That night she searches for physical therapy near her to see who is around. Because your Google profile has been kept active all year, with recent photos, current hours, and a steady flow of reviews from patients who got back to their sport, you sit at the top of the map pack with the rating that puts her at ease. She reads two reviews, saves your clinic, and calls you first thing Monday. The clinic a mile away that let its profile go quiet never showed up in her search, and never knew she existed. Illustrative example, not a client."},
    "faqs": [
        ("Do you manage my Google Business Profile for me?",
         "Yes. We keep it active with photos of the clinic and team, posts, and local content on a regular schedule, and keep your hours, services, and service area accurate, so it looks current and trustworthy whenever someone searches for physical therapy near them."),
        ("How much do reviews really matter for a PT clinic?",
         "A great deal. Patients trusting a clinic with their recovery lean on reviews heavily, and the map pack weighs them too. We help you ask every patient who finishes their plan of care at the right moment and reply to each review, so the reputation you have earned shows up where people decide."),
        ("Does marketing help if most of my patients come from physician referrals?",
         "Yes, on both sides. Direct access means more patients now search and choose a clinic themselves, and even a referred patient looks you up before their first visit. A strong, active profile wins the self-referral and reassures the referred one, which also makes referring doctors comfortable sending more."),
        ("How is this different from the CRM?",
         "The CRM follows up privately with people already in your files, discharged patients and referrals that did not book. Marketing is the public-facing side, your Google profile, reviews, and local visibility, aimed at patients who are not yours yet and the doctors deciding where to send them."),
        ("How long before I see it working?",
         "A neglected profile can climb in the map pack within weeks once it is active and complete, and it compounds from there as reviews and content build. Setup is included, and a free audit will show you what your current presence looks like to someone searching near you today.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for physical therapists"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-physical-therapists.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the physical therapist they <em>can already see</em>",
    "cta_sub": "Get a free audit that finds the gap in your local visibility and reviews: how easily a patient nearby can actually find and trust you right now, whether you work with us or not. No credit card, never a call center.",
},
# ======================= Websites & SEO for Physical Therapists =======================
{
    "slug": "websites-seo-for-physical-therapists",
    "trade_slug": "physical_therapists", "trade_plural": "physical therapists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "Websites & SEO for Physical Therapists",
    "title": "Websites & SEO for Physical Therapists | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Physical Therapists",
    "meta_desc": "A physical therapy website built for SEO ranks for physical therapy near me and your city, and books the evaluation instead of a directory.",
    "service_schema_name": "Websites & SEO for Physical Therapists",
    "eyebrow": "For Physical Therapists",
    "h1_html": "Websites &amp; SEO <em>for Physical Therapists</em>",
    "answer_block": "A physical therapy website built for SEO ranks for what a patient searches after an injury or surgery, physical therapy near me, post-op rehab, knee and back pain, your city, and lets them book an evaluation in one tap, so the patient is yours instead of a directory renting your own referrals back to you.",
    "sections": [
        {"h2_html": "A patient trusting you with their recovery judges your clinic by your <em>website in seconds</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A patient who has just learned they need therapy, whether a surgeon told them or they decided on their own, is on a phone opening the first few clinics they find. In a few seconds they decide whether each one looks like a place they would trust to guide months of recovery. A site that loads slowly, looks like it was built a decade ago, or does not work right on a phone tells them the clinic might be just as behind, and they back out and try the next one. It matters even more in physical therapy, because a referred patient often looks you up before the first visit, and so does the physician deciding whether to keep sending patients your way. A dated site quietly undercuts the credibility your therapists have actually earned.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The site does not have to be flashy. It has to load fast, put your location, the conditions you treat, and the insurance you take right in front of a visitor, and make calling or requesting an evaluation a single tap. A clean, fast, modern site does the opposite of a neglected one: it signals a clinic that has its act together, which is exactly what someone about to trust you with a recovery wants to believe. A beautiful site that hides how to reach you wastes the patient it just earned.</p>'},
        {"h2_html": "Rank for what a patient <em>actually searches</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national health directory this year for the broadest terms, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you serve, and for the exact searches patients make when they need you: physical therapy near me, post-surgery or post-op rehab, sports injury, back pain, knee pain, shoulder and rotator-cuff therapy, sciatica, and balance or vestibular therapy. Because direct access lets patients start without a referral, more of them are typing those searches themselves and choosing from the results. Pages built around the conditions you treat and the areas you cover are what search engines, and a patient deciding where to rehab, reward with the click. A page that explains, in plain language, what a first evaluation is like or what recovery from a common surgery actually involves also answers the quiet questions a nervous patient is already typing, which earns both the ranking and the trust. That is the ground a local clinic can win, and hold.</p>'},
        {"h2_html": "Stop letting a directory <em>rent you your own patients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for physical therapy in your town and the top of the page is often a health directory or an insurance find-a-provider tool, not a local clinic. Those sites publish thousands of pages and carry years of authority, so a patient lands there first, picks from a list that may put whoever pays the most on top, and gets routed through a platform that treats your own patient, sometimes one a physician referred straight to you, as a lead it controls. Your site not ranking is not a vanity problem. It is the reason a patient who should have found you directly gets funneled through a middleman that lines your competitors up beside you and skims the value of a whole plan of care. A website that ranks on its own keeps the patient yours from the first click, with no middleman between you and the person searching for exactly what you do, and it means the patient meets your clinic, your name, your therapists, and your reviews before anyone else can put a competitor in front of them.</p>'},
        {"h2_html": "The patients it earns are <em>yours to keep</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you put into a pay-per-lead service disappears the day you stop paying, and the patient was never really yours. A website you own keeps ranking, keeps earning evaluations, and keeps compounding in value for as long as it exists, registered to your clinic, not to a platform that can drop you or raise the rent. It plugs into the same CRM that follows up on every new-patient lead it captures and keeps discharged patients coming back, and the answering service that picks up the calls it drives, so a patient the site earns at midnight is booked, followed up, and brought back for the next injury instead of slipping away before morning. In a field where one patient can mean a full plan of care now and another one down the road, plus the family and teammates they refer, an asset that keeps earning quietly is worth far more than a burst of paid clicks that stops the moment the invoice does.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A post-surgery search finds <em>you, not a directory</em>",
        "body_html": "A man scheduled for a knee replacement is told he will need therapy afterward, so a week before surgery he searches for post-op knee rehab near him to line one up. Instead of a national directory that would route his details to whoever pays for the spot, he finds your site ranking for that search, loading fast, with a page about post-surgical rehabilitation and a clear way to request an evaluation right at the top. He reaches out, your answering service books him for the week after his operation, and he is a patient before he has even had the surgery. You paid nothing per lead, no middleman ever touched the booking, and that first visit is the start of a full plan of care. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the injury, condition, and post-surgery searches a national directory has no reason to target well, which is exactly where a local clinic can win."),
        ("How is this different from paying for patient leads or a directory listing?",
         "A pay-per-lead service or directory rents you a patient it may also show to other clinics, and it stops the day you stop paying. A website you own captures patients who are yours alone and keeps working long after it is built, with no per-lead fee skimming the value of a whole plan of care."),
        ("Can patients request their evaluation right on the site?",
         "Yes. A clear request-an-appointment or booking button lets someone start in one tap on their phone, and it lands on your real schedule with a confirmation and reminder. For the caller who would rather talk, the AI receptionist books them too."),
        ("Do I need a page for every condition I treat?",
         "You start with the ones that matter most, the surgeries and injuries you want more of, then expand. A focused set of strong condition and location pages ranks better than one thin page trying to cover everything at once."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks, while broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for physical therapists"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-physical-therapists.html", "Staying visible in your area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Get a free audit that finds the gap between your website and the directories taking your new-patient searches, whether you work with us or not. No credit card, never a call center.",
},
]
