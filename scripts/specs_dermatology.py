"""Per-page content specs for the SEO corpus (plan §5), dermatology batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, dermatology-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the med-spa, dentist, chiropractor, or veterinary content
reworded.

Medical & Dental hub, alongside dentists, med spas, chiropractors, and veterinary clinics. Four
service angles are here in one file (the ai-receptionist dict carries "demo": True). Kept
deliberately distinct from specs_med_spas.py: dermatology is a physician-led MEDICAL practice
(skin-cancer screenings, suspicious moles, biopsies, acne, eczema, insurance-billed) that also
runs a cosmetic side (Botox, laser, peels, cash-pay), where a med spa is pure aesthetics. Long
new-patient waitlists, annual skin-check recall, and trusting a physician with your skin and
your face are the dermatology angles the sibling pages never touch. Each example body ends with
the literal "Illustrative example, not a client." per the honesty rule; if the generator also
appends that line, dedupe there.
"""

SPECS = [
# ========================= AI Receptionist for Dermatologists =========================
{
    "slug": "ai-receptionist-for-dermatologists", "demo": True,
    "trade_slug": "dermatology", "trade_plural": "dermatology practices",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "AI Receptionist for Dermatologists",
    "title": "AI Receptionist for Dermatologists | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Dermatologists",
    "meta_desc": "A dermatology answering service answers every new-patient and worried-mole call your front desk misses, sorts the urgent from the routine, and books it.",
    "service_schema_name": "AI Receptionist for Dermatologists",
    "eyebrow": "For Dermatology Practices",
    "h1_html": "AI Receptionist <em>for Dermatologists</em>",
    "answer_block": "A dermatology answering service answers every new-patient call the moment it rings, days, nights, and weekends, tells a patient worried about a changing mole apart from a routine acne or cosmetic question, and books the visit while your front desk is buried in referrals and insurance. You keep your number, and every patient belongs to you.",
    "sections": [
        {"h2_html": "The call your front desk misses is the patient who <em>books the next dermatologist</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A person who just noticed a mole that changed shape, a spot that started bleeding, or a rash that will not settle does not leave a voicemail and wait for a callback. They are worried now, they searched for a dermatologist near them, and they work down the list until a real person answers and says yes, we can get you in. Your front desk is not ignoring the phone. They are verifying insurance, chasing a referral or a prior authorization, checking in a patient for a procedure, or working a new-patient waitlist that already runs weeks out, so the call rings through to voicemail while their hands are full. The one that got missed was rarely a wrong number. It was a patient, and in dermatology that patient might be a skin cancer that needs to be seen, not a lead you can afford to lose to the practice down the road.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A dermatology answering service picks up the instant the phone rings, no matter what the front desk is in the middle of. It stays calm with someone who is scared, finds out what brings them in, and books the visit while they are still on the line, or flags a call that sounds urgent to your team right away. The patient is captured instead of handed to whoever answered first.</p>'},
        {"h2_html": "Built around the calls a <em>dermatology front desk</em> actually fields",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A dermatology practice lives on two kinds of calls at once, and the phone almost never stops. On the medical side people call about a spot that changed, a mole they want checked, an acne flare or a rash that is not clearing, eczema, or a referral their primary care doctor just sent over. On the cosmetic side they call about Botox, a laser consult, or a peel. A voicemail box cannot answer a single one of them, and a generic call center reading a script does not know a skin check from a filler question or which caller needs to be seen this week.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers days, evenings, and weekends, so the person who spotted something worrying on a Sunday reaches a real answer instead of a recording.</li><li>Handles the questions that tie up the front desk: your hours, where you are, whether you take their insurance, whether they need a referral, and whether you are accepting new patients.</li><li>Tells a medical visit apart from a cosmetic consult and books each onto the right kind of appointment, so your schedule is not a tangle your staff has to sort out later.</li><li>Recognizes the calls you have told it to treat as urgent, a spot changing fast or a severe reaction, and flags them to your team the moment they come in.</li></ul>'},
        {"h2_html": "It keeps your <em>medical and cosmetic schedules</em> straight",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A full-body skin exam billed to insurance and a cash-pay Botox consult are two different appointments, booked for different lengths, on different parts of your calendar, with different questions asked up front. Getting that sorting wrong is how a cosmetic consult lands in a medical slot, a new patient is booked without the referral their plan requires, and the whole day runs behind. The answering service asks the questions that decide which kind of visit a caller needs and books it into the right appointment type, the way your front desk would if it could pick up every call. It can confirm what a first visit looks like, what to bring, and whether a plan needs a referral before the patient ever arrives, so fewer people show up for the wrong visit or turn around at the desk. You decide exactly what it asks and how it answers about coverage, so nothing it says on the phone commits you to anything.</p>'},
        {"h2_html": "You own the number, the patients, and the <em>schedule it fills</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing office number, or a new one registered to your practice, not to us. Every caller, every new-patient record, and every appointment it books is yours, exportable any time, so the patient list you are building stays an asset you own instead of something you rent back month to month. Because a dermatology call means someone is describing a symptom or a spot, it is built to handle what a caller shares with the discretion a medical office is held to, collecting only what it needs to book the visit and keeping it inside your systems. The answering service is one piece of the Top Shelf platform, so a call it answers lands in the same CRM that sends your skin-check and follow-up reminders, and the patient it books today is the one your system keeps bringing back for years.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A weekend mole worry, on the schedule before <em>Monday</em>",
        "body_html": 'It is Saturday afternoon and a man notices a mole on his back that his wife says looks darker and rougher than it did a few months ago, and it caught on his shirt and bled. He searches for a dermatologist, calls the first two he finds, and both ring to a weekend voicemail. Yours answers, asks a few calm questions, sees this is one to prioritize, and books him into the soonest skin-check opening while flagging it to your team as urgent. He stops calling around because someone finally helped him. You open Monday to a new patient already on the schedule, with his name, his insurance, and what he described noted, instead of hearing he found a practice that picked up. Illustrative example, not a client.'},
    "faqs": [
        ("Does it work with my current office number?",
         'Yes. It can answer on the number your patients already call, or set up a new one registered to your practice. Either way the number and every call that comes through it belong to you and stay with you if you ever leave.'),
        ("Can it handle both medical and cosmetic calls?",
         'Yes, that is what it is built for. It tells a skin check, a rash, or a referral apart from a Botox or laser consult, answers the insurance and referral questions medical callers ask and the consult questions cosmetic callers ask, and books each onto the right kind of appointment. You decide exactly what it says about coverage and pricing.'),
        ("What about a patient worried about a changing mole or a serious reaction?",
         'It handles those the way you tell it to. A caller describing a spot that is changing quickly, a wound that will not stop bleeding, or a severe reaction gets booked into your soonest opening and flagged to your team at once, while a routine question is handled without pulling anyone off the floor. You set what counts as urgent.'),
        ("Is patient information handled carefully?",
         'Yes. It is built to treat what a caller shares with the discretion a medical practice is held to, collecting only what it needs to book the visit and keeping it inside your systems. You control what it asks and what it stores.'),
        ("How fast can it be answering?",
         'Setup is included with no separate onboarding fee. We configure your questions, your appointment types, and how it sorts medical from cosmetic for you, so it is picking up in days, not weeks. Start with a free audit and we will show you how many calls your front desk is missing right now.')],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for dermatology practices"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-dermatologists.html", "The CRM that follows up on every call you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop sending worried patients to <em>voicemail</em>",
    "cta_sub": "Get a free audit that finds the gap in your new-patient calls: how many roll to voicemail and book elsewhere while your front desk is buried in referrals and insurance, whether you work with us or not. No credit card, never a call center.",
},
# ================================ CRM for Dermatologists ================================
{
    "slug": "crm-for-dermatologists",
    "trade_slug": "dermatology", "trade_plural": "dermatology practices",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "CRM for Dermatologists",
    "title": "CRM for Dermatologists | Top Shelf Business Solutions",
    "og_title": "CRM for Dermatologists",
    "meta_desc": "A CRM for dermatology practices brings back patients due for a skin check and the cosmetic maintenance they meant to keep up, so your list fills the schedule.",
    "service_schema_name": "CRM for Dermatologists",
    "eyebrow": "For Dermatology Practices",
    "h1_html": "CRM <em>for Dermatologists</em>",
    "answer_block": "A CRM for dermatology practices keeps every patient, skin-check recall, and cosmetic maintenance cycle in one place and reaches out for you, so the patient due for an annual skin exam and the one whose Botox is wearing off both come back instead of drifting away. Your patient list quietly becomes your schedule.",
    "sections": [
        {"h2_html": "The skin check you told them to come back for is the visit you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most dermatology practices are not short on demand. They are short on follow-up. A patient comes in for a rash or a suspicious spot, and on the way out you tell them to come back in a year for a full skin exam, or in a few months so you can recheck a mole you want to watch. They mean to. Then life gets busy, no reminder ever comes, and they resurface a year or two later only when something scares them, if they come back to you at all instead of searching from scratch. The recheck was never a no. It just needed a well-timed nudge, and that is exactly the thing a front desk working a weeks-long waitlist never gets around to.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every one of those patients and what they are due for in front of you and sends the reminder for you, on the schedule you set, whether or not anyone at the desk remembers. The patient you asked to watch a spot hears from you right when the recheck is due, and the visit you already recommended actually lands on the schedule.</p>'},
        {"h2_html": "Annual skin checks and cosmetic maintenance are the <em>recall goldmine</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A dermatology practice sits on two streams of built-in repeat business, and most work neither well. On the medical side there are the annual skin exams and the patients with a history of sun damage or removed skin cancers who should never let a year lapse. On the cosmetic side there are the treatments that fade and repeat on a schedule you can predict. Both are the cheapest, easiest visits you can book, because these patients already know and trust you, and both slip away when no one is watching the dates for a few thousand people.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every patient, their history, their last visit, and what they are due for next lives in one place instead of scattered across your practice software and whatever the front desk happens to remember.</li><li>Skin-check and recheck reminders go out on schedule for the medical side, and maintenance reminders go out on the cadence cosmetic treatments run on, so both kinds of visit rebook without anyone tracking due dates by hand.</li><li>You can see exactly who has lapsed, on either side, and reach the right patient with the right reason to come back at the right time.</li></ul>'},
        {"h2_html": "The patient who <em>drifted away</em> is still yours to bring back",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A patient you have not seen in two years has usually not left on purpose. Their acne cleared and they stopped booking, they moved across town, their insurance changed, or they never rebooked the skin check you recommended after one canceled appointment. A light, steady touch, a friendly note that they are overdue, a reminder that the spot you were watching should be looked at again, or that it has been a while since their last skin exam, is often all it takes to bring them back through the door. It costs almost nothing next to chasing brand-new patients with ads, and it turns a name sitting dormant in your system into a booked exam and, often, the treatment or the finding that comes up once they are back in the room. And you do not have to send those notes one at a time. A single reactivation message to everyone overdue for a skin check can fill a quiet stretch on the schedule with patients who were always yours to bring back, without spending a dollar on a new-patient ad.</p>'},
        {"h2_html": "You own the patient list, and it works with the <em>rest of the practice</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every patient and every note is yours and exportable any time, handled with the discretion a medical practice is held to, not locked away inside software you only rent. Because the same person is often a medical patient and a cosmetic one, keeping both sides of their history on a single record matters: the front desk can see that the patient booking a Botox touch-up is also overdue for a skin exam, and mention it, instead of treating the two halves of your practice as strangers. The CRM is one piece of the Top Shelf platform. It connects to the answering service, so a new patient it books lands in your database ready for recall, and to online booking, so a scheduled visit is logged against the right record with the full history already attached. The patient list you have spent years building finally works for you instead of just sitting there recording who came in. For a practice whose value lives in its patient base, owning that list outright, and being able to take it with you, is not a small thing.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The spot she was told to <em>keep an eye on</em>",
        "body_html": 'A patient comes in about a rash, and during the exam the dermatologist notices a mole on her shoulder that looks fine now but is worth rechecking in six months, and suggests she start yearly skin exams given how much sun she got growing up. She agrees, but she leaves without booking the recheck. Normally that is the last anyone thinks of it, until the spot changes and she starts over with whoever she finds. Instead, the CRM holds the plan and sends her a friendly reminder when the recheck is due, written to sound like the practice she already trusts, with a link to book. She comes in before the spot has a chance to change unwatched. No one at the front desk had to remember. Illustrative example, not a client.'},
    "faqs": [
        ("Does it work with my practice management or EHR software?",
         'It sits alongside it as your follow-up and outreach layer. Your patients, their history, and what they are due for come in and stay yours and exportable, so the list you already have starts actively bringing people back instead of just recording who came in.'),
        ("Will it really send skin-check and recheck reminders?",
         'Yes, on the schedule you approve. A patient due for an annual skin exam gets a reminder at the right time, the person you asked to watch a spot is nudged when the recheck comes due, and both get a follow-up if they lapse, all sent for you. You can step in and message anyone yourself any time.'),
        ("Can it handle both medical recall and cosmetic maintenance?",
         'Yes. It reminds the medical side on the cadence skin exams and rechecks run on, and the cosmetic side on the cadence its treatments run on, all from the same patient record, so both streams of repeat business rebook without your team working a spreadsheet of dates.'),
        ("Is patient data kept private?",
         'Yes. Patient information is handled with the care a medical practice is held to and stays inside your systems, and it is always yours to export. You control what the CRM stores and what each message says.'),
        ("How long until it is set up?",
         'Setup is included with no separate onboarding fee. We bring in your patients, build your skin-check recall and maintenance sequences, and connect it to your phones and calendar, so it is working in days. Start with a free audit and we will show you where recall is slipping today.')],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for dermatology practices"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-dermatologists.html", "The AI receptionist that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting skin checks and recalls <em>go cold</em>",
    "cta_sub": "Get a free audit that finds the gap in your recall and reactivation: how many patients due for a skin check or cosmetic maintenance are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ============================== Marketing for Dermatologists ==============================
# ========================= Websites & SEO for Dermatologists =========================
{
    "slug": "websites-seo-for-dermatologists",
    "trade_slug": "dermatology", "trade_plural": "dermatology practices",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "Websites & SEO for Dermatologists",
    "title": "Websites & SEO for Dermatologists | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Dermatologists",
    "meta_desc": "A dermatology practice website built for SEO ranks for dermatologist near me and skin cancer screening, and books the patient instead of a directory.",
    "service_schema_name": "Websites & SEO for Dermatologists",
    "eyebrow": "For Dermatology Practices",
    "h1_html": "Websites &amp; SEO <em>for Dermatologists</em>",
    "answer_block": "A dermatology practice website built for SEO ranks for what a patient searches, dermatologist near me, skin cancer screening, acne, Botox and your city, looks credible enough to trust with their skin and face, and captures the patient the moment they land, so the booking is yours instead of a directory renting your own patients back to you.",
    "sections": [
        {"h2_html": "A patient trusting you with their skin judges your practice by your <em>website in seconds</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A patient who just found a spot that worries them, or who has finally decided to do something about their skin, is on their phone opening the first few practices they find. In a few seconds they decide whether each one looks like a place they would trust with a mole check or with their face. A site that loads slowly, looks like it was built a decade ago, or does not work right on a phone tells them the practice might be just as behind, and they back out and try the next one. For a physician practice that impression matters even more, because a dated site quietly undercuts the credibility a board-certified dermatologist has actually earned. A clean, fast, modern site does the opposite: it signals a practice that has its act together, which is exactly what someone about to let you examine their skin wants to believe.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The site does not have to be flashy. It has to load fast, put your services, your location, the insurance you take, and whether you are accepting new patients right in front of a visitor, and make calling or requesting an appointment a single tap. A beautiful site that hides how to reach you wastes the patient it just earned.</p>'},
        {"h2_html": "Rank for what a patient <em>actually searches</em>, medical and cosmetic",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national health directory this year for the broadest terms, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you serve, and for the exact searches patients make on both sides of your practice: dermatologist near me, skin cancer screening, mole check, acne, eczema, and psoriasis on the medical side, and Botox, laser treatment, or a chemical peel plus your city on the cosmetic side. Pages built around the conditions you treat and the treatments you offer are what search engines, and a patient deciding where to go, reward with the click. A page that explains, in plain language, what a full-body skin exam or a first cosmetic consult is actually like also answers the quiet questions a nervous patient is already typing, which is the kind of content that earns both the ranking and the trust. That is depth a faceless directory has no reason to write for your town.</p>'},
        {"h2_html": "Stop letting a directory <em>rent you your own patients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for a dermatologist in your town and the top of the page is often a health directory or an insurance find-a-doctor tool, not a local practice. Those sites publish thousands of pages and carry years of authority, so a new patient lands there first, picks from a list that may put whoever pays the most on top, and gets routed through a platform that treats your own patient as a lead it controls. Your site not ranking is not a vanity problem. It is the reason a patient who should have found you directly gets funneled through a middleman that lines your competitors up beside you and, in dermatology, skims the value of a relationship that could have spanned years of skin checks and treatments. A website that ranks on its own keeps the patient yours from the first click, with no middleman standing between you and the person searching for exactly what you do. It also means the patient meets your practice, your name, your physicians, your reviews, before anyone else gets the chance to put a competitor in front of them, which is exactly the head start a directory sells to the highest bidder.</p>'},
        {"h2_html": "The patients it earns are <em>yours to keep</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you put into a pay-per-lead service disappears the day you stop paying, and the patient was never really yours. A website you own keeps ranking, keeps earning bookings, and keeps compounding in value for as long as it exists, registered to your practice, not to a platform that can drop you or raise the rent. It plugs into the same CRM that follows up on every new-patient lead it captures and puts them into skin-check recall, and the answering service that picks up the calls it drives, so a patient the site earns at midnight is booked, followed up, and brought back for years instead of slipping away before morning. Unlike an ad you rent, the pages you build keep answering the same searches next year and the year after, and in a field where one patient can mean a decade of annual skin checks and the family they refer, an asset that keeps earning quietly is worth far more than a burst of paid clicks that stops the moment the invoice does.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A late-night mole worry finds <em>you, not a directory</em>",
        "body_html": 'A man new to town notices a mole on his shoulder has grown and darkened, and at eleven at night he searches for a skin cancer screening near him. Instead of a national health directory that would route his details to whoever, he finds your site ranking for that search, loading fast, with a page about full-body skin exams and skin cancer screenings and a clear way to request an appointment right at the top. He reaches out, your answering service books him for later that week, and he is a patient before he has even met you. You paid nothing per lead, no middleman ever touched the booking, and that first visit is the start of years of skin checks and care. Illustrative example, not a client.'},
    "faqs": [
        ("Will my site actually outrank the big directories?",
         'Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the condition, treatment, and screening searches a national directory has no reason to target well, which is exactly where a local practice can win.'),
        ("How is this different from paying for patient leads or a directory listing?",
         'A pay-per-lead service or directory rents you a patient it may also show to other practices, and it stops the day you stop paying. A website you own captures patients who are yours alone and keeps working long after it is built, with no per-lead fee skimming the years of visits a dermatology patient is worth.'),
        ("What should a dermatology website actually have?",
         'The essentials a patient needs, fast: your medical and cosmetic services, your location and hours, the insurance you take, whether you are accepting new patients, real photos, easy tap-to-call and a simple way to request an appointment, and pages for the conditions and treatments you want more of. It has to load quickly and work perfectly on a phone, since that is where most patients find you.'),
        ("Do I need a page for every condition and treatment?",
         'You start with the ones that matter most, the searches you want to grow on both the medical and cosmetic sides, then expand. A focused set of strong condition, treatment, and location pages ranks better than one thin page trying to cover everything at once.'),
        ("How long until it starts ranking?",
         'Local, specific searches can start moving within weeks, while broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.')],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for dermatology practices"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Get a free audit that finds the gap between your website and the directories taking your new-patient searches, whether you work with us or not. No credit card, never a call center.",
},
]
