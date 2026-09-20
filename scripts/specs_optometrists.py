"""Per-page content specs for the SEO corpus (plan §5), optometrists batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, optometry-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the dentist, physical-therapy, or dermatology content reworded.

Medical & Dental hub, alongside dentists, physical therapists, and dermatology. Four service
angles are here in one file (the ai-receptionist dict carries "demo": True). Kept deliberately
distinct from the sibling medical trades: an optometry practice runs on an annual eye-exam recall
AND an optical RETAIL business (glasses, frames, contact lenses) stacked on top of the exam, so
the levers no sibling touches are recall for overdue exams and contact-lens reorders, a front desk
that doubles as the optician (helping a patient pick frames or running pretesting, so booking calls
go unanswered), the vision-plan vs medical-insurance question that eats the phone, a new patient
worth years of annual exams plus eyewear plus the whole family, and a modern site with easy exam
booking and a frames showcase that keeps the eyewear sale at home. Each example body ends with the
literal "Illustrative example, not a client." per the honesty rule; if the generator also appends
that line, dedupe there.
"""

SPECS = [
# ========================= AI Receptionist for Optometrists =========================
{
    "slug": "ai-receptionist-for-optometrists", "demo": True,
    "trade_slug": "optometrists", "trade_plural": "optometrists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "AI Receptionist for Optometrists",
    "title": "AI Receptionist for Optometrists | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Optometrists",
    "meta_desc": "An optometry answering service answers every eye-exam and new-patient call your front desk misses while it is at the optical counter, and books it.",
    "service_schema_name": "AI Receptionist for Optometrists",
    "eyebrow": "For Optometrists",
    "h1_html": "AI Receptionist <em>for Optometrists</em>",
    "answer_block": "An optometry answering service answers every eye-exam and new-patient call the moment it rings, days, nights, and weekends, answers the vision-plan and insurance questions that tie up your front desk, and books the exam on your calendar while your team is at the optical counter. You keep your number, and every patient belongs to you.",
    "sections": [
        {"h2_html": "The call you miss is the eye exam that <em>books the next optometrist</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">In most practices the person who answers the phone is also running the optical. They are helping a patient choose frames, adjusting a pair that sits crooked, walking someone through pretesting on the autorefractor, or checking a patient out at the optical counter. So when the phone rings, it rings through to voicemail while the one person up front is a few feet away with their hands full. The patient calling to book a routine annual exam does not leave a message and wait. They scroll down and call the next optometrist, and the one after that, until someone picks up and gets them scheduled.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That missed call was rarely a wrong number. It was a new patient, or a whole family looking to book their yearly exams, or someone whose contacts are running low and who needs to be seen before they can reorder. Some of those calls are urgent, a chemical splash, something stuck in the eye, a sudden change in vision, and those callers will not wait on hold at all. An optometry answering service picks up on the first ring no matter what the front desk is in the middle of, gets the caller what they need, and books the exam while they are still on the line.</p>'},
        {"h2_html": "Built around the calls an <em>optometry front desk</em> actually fields",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every call is an emergency, but the phone at an eye clinic almost never stops, and the questions are specific to how you run. People call to book their annual exam, to ask whether you take their vision plan or their medical insurance, to check whether their glasses or contacts are ready to pick up, or because an eye is suddenly red and painful. A voicemail box cannot answer a single one of them, and a generic call center reading a script does not know a vision plan from medical insurance or a routine exam from an eye that needs to be seen today.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers days, evenings, and weekends, so the parent booking back-to-school exams after work and the patient with something in their eye on a Sunday reach a real answer instead of a recording.</li><li>Answers the question that eats your phone: whether you take their vision plan, whether a medical eye problem runs through their health insurance instead, and what a first exam involves.</li><li>Books the annual exam straight onto your calendar, and can tell a patient whether their glasses or contacts are ready without pulling anyone off the optical floor.</li><li>Tells a routine exam apart from an urgent eye problem, a red painful eye, a chemical splash, a sudden loss of vision, and flags the ones you have marked urgent to your team the moment they come in.</li></ul>'},
        {"h2_html": "One new patient is <em>years of exams and eyewear</em>, not one visit",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This is why a missed call costs an optometry practice more than it first looks. A new patient almost never comes in just once. A comprehensive eye exam becomes an annual habit, and on top of that exam sits the optical: a pair of glasses, prescription sunglasses, a year of contact lenses that need reordering. Then the rest of the household follows, the kids who need exams for school, a spouse who has been putting theirs off. So the call you lose on a busy afternoon is not one exam. It is the annual exams, the eyewear, and the family that come with keeping that patient for years. You do not need to catch many of those for it to change the month, and everything the receptionist books after the first save is on top. When the phone is covered, the patient your marketing and your reputation worked to earn actually lands on the schedule instead of slipping to the office that happened to answer.</p>'},
        {"h2_html": "You own the number, the patients, and the <em>schedule it fills</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing office number, or a new one registered to your practice, not to us. Every caller, every exam it books, and every patient record is yours and exportable any time, so the patient list you are building stays an asset you own instead of something you rent back month to month. Because a caller may be describing a medical eye problem, it is built to handle what they share with the discretion a medical office is held to, collecting only what it needs to book the visit and keeping it inside your systems. The answering service is one piece of the Top Shelf platform, so a call it answers lands in the same CRM that sends your annual recall and contact-lens reminders, and the patient it books today is the one your system keeps bringing back for years.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "Two back-to-school exams, booked while the front desk is <em>fitting frames</em>",
        "body_html": "It is a Tuesday in August and a mother is trying to book eye exams for two kids before school starts, because one of them squints at the board and the pediatrician said to get it checked. She calls your office. Your front desk is at the optical counter helping another patient narrow down frames, so the call would normally ring through to voicemail, and she would move on to the next optometrist while she has a free minute. Instead your answering service picks up, confirms you take her vision plan, and books both children back to back on a day she is already off work. Your optician never has to walk away from the patient in front of her. You gain two exams, and likely the rest of the family, without anyone touching the phone. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current office number?",
         "Yes. It can answer on the number your patients already call, or set up a new one registered to your practice. Either way the number and every call that comes through it belong to you and stay with you if you ever leave."),
        ("Can it answer the vision-plan and insurance questions patients always ask?",
         "Yes, those are the calls it handles best. It can tell people whether you take their vision plan, that a medical eye problem may run through their health insurance instead, your hours, where you are, and what a first exam involves, and it books the exam right on your calendar. You decide exactly what it is allowed to say about coverage."),
        ("What about a patient with something wrong with their eye?",
         "It tells an urgent call apart from a routine one. Someone with a chemical splash, something stuck in the eye, sudden vision loss, or a red painful eye gets booked into your soonest opening and flagged to your team at once, while a routine exam or a frames question is handled without pulling anyone off the optical floor. You set what counts as urgent."),
        ("Can it tell a patient whether their glasses or contacts are ready?",
         "Yes, the routine status calls that tie up the optical are exactly what it takes off your team. It can confirm an order is in or still being worked on the way you tell it to, and hand anything unusual to a person, so nobody has to leave the counter to answer the phone."),
        ("How fast can it be answering?",
         "Setup is included with no separate onboarding fee. We configure your questions, your vision-plan answers, and your scheduling rules for you, so it is picking up in days, not weeks. Start with a free audit and we will show you how many calls your front desk is missing while it is on the optical floor.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for optometrists"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-optometrists.html", "The CRM that follows up on every call you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop sending exams and eyewear to <em>voicemail</em>",
    "cta_sub": "Get a free audit that finds the gap in your new-patient calls: how many roll to voicemail and book elsewhere while your front desk is on the optical floor, whether you work with us or not. No credit card, never a call center.",
},
# ================================ CRM for Optometrists ================================
{
    "slug": "crm-for-optometrists",
    "trade_slug": "optometrists", "trade_plural": "optometrists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "CRM for Optometrists",
    "title": "CRM for Optometrists | Top Shelf Business Solutions",
    "og_title": "CRM for Optometrists",
    "meta_desc": "A CRM for optometrists sends annual eye-exam recall and contact-lens reorder reminders for you, so patients book again instead of drifting.",
    "service_schema_name": "CRM for Optometrists",
    "eyebrow": "For Optometrists",
    "h1_html": "CRM <em>for Optometrists</em>",
    "answer_block": "A CRM for optometrists keeps every patient, annual exam recall, and contact-lens reorder in one place and reaches out for you, so the patient overdue for an eye exam and the one about to run out of contacts both come back to book instead of drifting to another office. Your patient list quietly becomes your schedule.",
    "sections": [
        {"h2_html": "The annual exam you told them to come back for is the visit you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most optometry practices are not short on demand. They are short on follow-up. A patient comes in for their exam, you hand them a prescription, and you tell them to come back in a year. They mean to. Then a year passes with no reminder, the prescription quietly expires, and they only think about it again when a lens breaks or the contacts run out, if they come back to you at all instead of searching from scratch. The recall was never a no. It just needed a well-timed nudge, and that is exactly the thing a front desk splitting its time between the phone and the optical counter never gets around to.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every patient and what they are due for in front of you and sends the reminder for you, on the schedule you set, whether or not anyone at the desk remembers. The patient whose year is up hears from you right when the annual exam is due, with a link to book, and the visit you already earned once actually comes back around instead of drifting to the office down the road.</p>'},
        {"h2_html": "Recall and contact-lens reorders are the <em>goldmine</em> most practices leave sitting",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The patients you have already seen are the cheapest, easiest chair to fill, and optometry has two built-in reasons for them to come back that most practices work poorly. There is the annual exam, which a huge share of patients simply forget without a prompt. And there is the contact-lens wearer, who runs through a supply on a predictable schedule and cannot reorder once the prescription lapses, which makes an expiring prescription a reason to book the exam that renews it. Both slip away when nobody is watching the dates for a few thousand people.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every patient, their last exam, their prescription, and when they are due lives in one place instead of scattered across your practice software and whatever the front desk happens to remember.</li><li>Annual recall reminders go out on schedule, so the patient whose year is up books again without your team tracking dates by hand.</li><li>Contact-lens reorder and renewal reminders reach a wearer before they run out, right when an expiring prescription means they need an exam to keep their lenses coming.</li><li>You can see exactly who has lapsed and reach the right patient with the right reason to come back, whether that is an overdue exam, a resupply, or the second pair they meant to buy.</li></ul>'},
        {"h2_html": "The patient who <em>drifted away</em> is still yours to bring back",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A patient you have not seen in two years has usually not left on purpose. The glasses still work well enough, they moved across town, their vision plan changed, or they simply never rebooked after one canceled appointment. A light, steady touch, a friendly note that it has been a while since their last exam, a reminder that the prescription has expired, or that the sunglasses they talked about are still waiting, is often all it takes to bring them back through the door. It costs almost nothing next to chasing brand-new patients with ads, and it turns a name sitting dormant in your system into a booked exam and, often, the eyewear that gets sold once they are back in the chair. And you do not have to send those notes one at a time. A single reactivation message to everyone overdue for an exam can fill a quiet week with patients who were always yours to bring back, without spending a dollar on a new-patient ad.</p>'},
        {"h2_html": "You own the patient list, and it works with the <em>rest of the practice</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every patient and every note is yours and exportable any time, handled with the discretion a medical office is held to, not locked away inside software you only rent. Because the same person is your exam patient and your eyewear customer, keeping both sides on one record matters: the front desk can see that the patient booking a contact-lens check is also overdue for the annual exam and due to reorder, and handle all of it in one visit instead of treating the exam and the optical as strangers. The CRM is one piece of the Top Shelf platform. It connects to the answering service, so a new patient it books lands in your database ready for recall, and to online booking, so a scheduled exam is logged against the right record with the full history already attached. For a practice whose value lives in its patient base and its optical, owning that list outright, and being able to take it with you, is not a small thing.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The contacts that <em>run out</em> right on cue",
        "body_html": "A patient buys a year of contact lenses in the spring and leaves happy, and normally the next you hear from her is whenever she notices the box is empty, which might be at your office or might be at a website that does not care whether her prescription is current. Instead, your CRM knows roughly when that supply runs low and when her prescription is set to expire, so it sends her a friendly reminder that it is time for her annual exam to keep her lenses coming, with a link to book. She schedules before she runs out, sits for the exam, renews the prescription, and reorders her year from you. Nobody at the front desk had to remember her. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my practice management or EHR software?",
         "It sits alongside it as your follow-up and outreach layer. Your patients, their history, and what they are due for come in and stay yours and exportable, so the list you already have starts actively bringing people back instead of just recording who came in."),
        ("Will it really send annual recall reminders?",
         "Yes, on the schedule you approve. A patient whose year is up gets a reminder at the right time with a link to book, and a follow-up if they let it lapse, all sent for you. You can step in and message anyone yourself any time."),
        ("Can it handle contact-lens reorder reminders?",
         "Yes. It can reach a contact-lens wearer before their supply runs out and when their prescription is coming up for renewal, so they book the exam that keeps their lenses coming instead of drifting to an online seller. You set the timing and the wording."),
        ("Is patient data kept private?",
         "Yes. Patient information is handled with the care a medical office is held to and stays inside your systems, and it is always yours to export. You control what the CRM stores and what each message says."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your patients, build your recall and reorder sequences, and connect it to your phones and calendar, so it is working in days. Start with a free audit and we will show you where recall is slipping today.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for optometrists"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-optometrists.html", "The AI receptionist that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting recall and reorders <em>go cold</em>",
    "cta_sub": "Get a free audit that finds the gap in your recall and reactivation: how many patients overdue for an exam or a contact-lens reorder are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ============================== Marketing for Optometrists ==============================
{
    "slug": "marketing-for-optometrists",
    "trade_slug": "optometrists", "trade_plural": "optometrists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "Marketing for Optometrists",
    "title": "Marketing for Optometrists | Top Shelf Business Solutions",
    "og_title": "Marketing for Optometrists",
    "meta_desc": "Optometry marketing keeps your Google profile active and reviews fresh, so the patient searching for an eye exam nearby finds you first and books.",
    "service_schema_name": "Marketing for Optometrists",
    "eyebrow": "For Optometrists",
    "h1_html": "Marketing <em>for Optometrists</em>",
    "answer_block": "Optometry marketing keeps you visible where new patients look for an eye doctor, your Google Business Profile, the map, and your reviews, so the person searching for an eye exam nearby finds an active, well-reviewed practice and picks you instead of the office that let its profile go stale. It is how new patients find you before they call.",
    "sections": [
        {"h2_html": "A new patient picks the eye doctor they can <em>find and trust</em> first",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone needs an eye doctor, whether they just moved, their vision changed, or the school nurse sent a note home about their child, they do not ask around for weeks. They search for an optometrist or an eye exam near them, glance at the map, and look at who has the most reviews and the highest ratings close by. They are about to trust a stranger with their eyes and, in the same visit, buy their glasses in that same place, so those stars and that recent activity are the fastest trust they can get before they ever call. A practice with a thin, untouched profile quietly loses those searches to the office with a fuller one, and you never see the patient who scrolled right past you.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The care you deliver in the exam room is probably excellent, and your optical may carry frames worth driving for. The problem is that a great practice with a neglected online presence looks, to a stranger searching at 9pm, about the same as a mediocre one. Marketing closes that distance so the reputation you have actually earned is the one a new patient sees first.</p>'},
        {"h2_html": "Your Google Business Profile is the <em>front door</em> now",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a new patient searches for an eye doctor near them, the map with its three local listings sits at the top, above the websites and above the ads. A profile that has not been touched in months, with old hours, no recent photos, and stale reviews, looks abandoned next to an office that keeps it current. Keeping yours active, complete, and honest, real photos of the office, the doctors, and the optical, accurate hours, the vision plans and insurance you take, and the frame brands you carry, is a quiet advertisement running in the exact spot people look when they are ready to book. It matters twice over for optometry, because a patient is choosing both an exam and a place to buy eyewear, and a profile that shows a real optical with frames on the wall tells them you are somewhere they can walk out seeing better, not just a doctor who hands them a prescription and sends them elsewhere. Wrong hours or a missing phone number does more than look sloppy. It quietly sends a ready-to-book patient to an office whose information they can actually trust.</p>'},
        {"h2_html": "Win the neighborhoods you serve, on the strength of your <em>reviews</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A patient wants an eye doctor they can get to easily, close to home or work, and near enough to swing back in when their glasses need an adjustment, so the people worth reaching live in a fairly tight radius around your office. Marketing to a whole metro just brings clicks from people who will never make the drive. Focusing your profile, your reviews, and your local content on the areas you truly serve is what puts you on the map for the searches that turn into booked exams. And reviews carry real weight here, because letting someone examine your eyes and then trusting their optical to get an expensive pair of glasses right both take confidence, so a patient reads them closely before choosing. Asking every happy patient at the right moment, the day they pick up glasses they love or walk out seeing clearly, and replying to each review that comes back feeds the profile that feeds the map, and the whole thing compounds: more reviews lift you in local search, which brings more patients, which brings more reviews.</p>'},
        {"h2_html": "Time your visibility to when patients <em>actually book</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Optometry demand has a rhythm worth getting ahead of. Back-to-school season sends parents booking exams for kids all at once, because so many schools ask for a vision check. Late in the year, patients scramble to use vision benefits and flexible-spending dollars on an exam and a new pair of glasses before they reset and vanish. The new year brings people who resolved to finally deal with their vision. Being visible right before each of those waves beats scrambling once they hit. A steady local presence, timely posts, fresh reviews, and current information keeps you top of mind for the patient deciding now. This is the public-facing side of the practice, aimed at people who are not your patients yet. The private follow-up to the patients already in your system, annual recall and reorders, is the CRM, and the two work best together.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "Year-end benefits, and you are the office <em>they can see</em>",
        "body_html": "It is early December and a woman realizes her vision benefits and the flexible-spending dollars she set aside reset at the end of the month, so she finally searches for an eye exam nearby to use them on a checkup and a new pair of glasses before they disappear. Because your Google profile has been kept active all year, with recent photos of the office and the optical, accurate hours, the plans you accept listed, and a steady flow of reviews, you sit near the top of the map when she looks. She sees an office that is clearly open, busy, and trusted, with frames worth coming in for, and she calls you instead of the one two listings down with a few old reviews. The practice that let its profile go quiet never comes up. Illustrative example, not a client."},
    "faqs": [
        ("Do you keep my Google Business Profile updated for me?",
         "Yes. We keep it active with photos of the office, the doctors, and the optical, posts, and accurate information on a regular schedule, and we keep your hours, the vision plans and insurance you take, and the frame brands you carry current, so it looks alive whenever someone searches for an eye doctor nearby."),
        ("What does focusing on my area actually mean?",
         "It means building your profile, reviews, and content around the neighborhoods your patients realistically come from, instead of spreading a budget across a whole metro. That is what gets you into the local map where new patients are choosing a practice."),
        ("How is this different from the CRM?",
         "The CRM follows up privately with patients already in your system, annual recall and contact-lens reorders. Marketing is the public-facing side, your Google profile, reviews, and local visibility, aimed at new patients who need to find and trust you before they have ever been in."),
        ("Can you help me get ahead of seasonal demand?",
         "Yes. We time your visibility to the waves that matter for optometry, back-to-school exams, the year-end rush to use vision benefits and flexible-spending dollars, and the new-year resolvers, so you are visible before people start searching instead of catching up after."),
        ("How long before it starts working?",
         "A neglected profile can climb in the local map within weeks once it is active and complete, and it compounds as reviews and content build. Setup is included, and a free audit will show you exactly how visible your practice looks to someone searching nearby today.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for optometrists"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-optometrists.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the eye doctor they <em>can already see</em>",
    "cta_sub": "Get a free audit that finds the gap in your local visibility and reviews: how easily a patient nearby can actually find and trust you right now, whether you work with us or not. No credit card, never a call center.",
},
# ========================= Websites & SEO for Optometrists =========================
{
    "slug": "websites-seo-for-optometrists",
    "trade_slug": "optometrists", "trade_plural": "optometrists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "Websites & SEO for Optometrists",
    "title": "Websites & SEO for Optometrists | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Optometrists",
    "meta_desc": "An optometry website built for SEO ranks for eye exam near me and optometrist near me, showcases your frames, and books the exam instead of a directory.",
    "service_schema_name": "Websites & SEO for Optometrists",
    "eyebrow": "For Optometrists",
    "h1_html": "Websites &amp; SEO <em>for Optometrists</em>",
    "answer_block": "An optometry website built for SEO ranks for what a patient searches, eye exam near me, optometrist near me, and the frames and contacts you sell, showcases your optical, and books the exam the moment they land, so the patient is yours instead of a directory renting your own patients back to you.",
    "sections": [
        {"h2_html": "A patient trusting you with their eyes judges your practice by your <em>website in seconds</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A patient who just decided they need an eye exam, or whose child failed a school vision screening, is on their phone opening the first few practices they find. In a few seconds they decide whether each one looks like a place they would trust with their eyes and worth buying glasses from. A site that loads slowly, looks like it was built a decade ago, or does not work right on a phone tells them the practice might be just as behind, and they back out and try the next one. It matters even more for optometry, because the site is doing two jobs at once: it has to look like a credible medical office and like an optical worth walking into, and a dated one quietly undercuts both.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The site does not have to be flashy. It has to load fast, put your exam services, your location and hours, the vision plans you take, and the frames you carry right in front of a visitor, and make booking an exam a single tap. A beautiful site that hides how to book wastes the patient it just earned.</p>'},
        {"h2_html": "Rank for what a patient <em>actually searches</em>, exam and optical",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national retailer or a vision-plan directory this year for the broadest terms, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you serve, and for the exact searches patients make on both sides of your practice: optometrist near me, eye exam near me, eye doctor, and eye exams for children on the exam side, and glasses, contact lenses, and prescription sunglasses near me on the optical side. Pages built around the exams you provide and the eyewear you sell are what search engines, and a patient deciding where to go, reward with the click. A page that explains, in plain language, what a comprehensive eye exam covers or how a first contact-lens fitting works also answers the quiet questions a patient is already typing, which is the kind of content that earns both the ranking and the trust. That is depth a faceless directory has no reason to write for your town.</p>'},
        {"h2_html": "Stop letting a directory <em>rent you your own patients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for an eye doctor in your town and the top of the page is often a vision-plan provider locator or a national directory, not a local office. Those tools publish thousands of pages and carry years of authority, so a patient lands there first, picks from a list that may put whoever pays the most on top, and gets routed through a platform that treats your own patient as a lead it controls. Your site not ranking is not a vanity problem. It is the reason a patient who should have found you directly gets funneled through a middleman that lines your competitors up beside you and, in optometry, skims the value of a relationship that could have spanned years of annual exams and eyewear. A website that ranks on its own keeps the patient yours from the first click, with no middleman standing between you and the person searching for exactly what you do, and it means the patient meets your practice, your doctors, your optical, and your reviews before anyone else can put a competitor in front of them.</p>'},
        {"h2_html": "The patients it earns are <em>yours to keep</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you put into a pay-per-lead service disappears the day you stop paying, and the patient was never really yours. A website you own keeps ranking, keeps earning exams, and keeps compounding in value for as long as it exists, registered to your practice, not to a platform that can drop you or raise the rent. It plugs into the same CRM that follows up on every new-patient lead it captures and puts them into annual recall, and the answering service that picks up the calls it drives, so a patient the site earns at midnight is booked, followed up, and brought back for years instead of slipping away before morning. It also does something a pay-per-lead source never will: a good site keeps the eyewear sale at home, showing the frames and brands you carry so the patient books the exam and buys the glasses from you instead of taking the prescription to an online seller. In a field where one patient can mean a decade of annual exams and the eyewear and family that come with them, an asset that keeps earning quietly is worth far more than a burst of paid clicks that stops the moment the invoice does.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A school vision screening finds <em>you, not a directory</em>",
        "body_html": "A mother gets a note from the school nurse that her son did not pass his vision screening and needs to see an eye doctor. That evening she searches for a children's eye exam near her. Instead of a vision-plan directory that would route her to whichever office paid for the spot, she finds your site ranking for that search, loading fast, with a page about pediatric eye exams and a clear way to book right at the top. She books him for that week, and while she is there she picks his first pair of glasses from your optical. You paid nothing per lead, no middleman ever touched the booking, and that first visit is the start of years of exams and eyewear for the whole family. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the exam, eyewear, and children's-exam searches a national directory or retailer has no reason to target well, which is exactly where a local practice can win."),
        ("How is this different from paying for patient leads or a directory listing?",
         "A pay-per-lead service or directory rents you a patient it may also show to other offices, and it stops the day you stop paying. A website you own captures patients who are yours alone and keeps working long after it is built, with no per-lead fee skimming the years of exams and eyewear a patient is worth."),
        ("Can a website really help me keep the eyewear sale?",
         "Yes. Showing the frames and brands you carry, and making it easy to book the exam that comes first, gives a patient a reason to buy their glasses and contacts from you rather than take the prescription to an online seller. The site sells the optical, not just the exam."),
        ("Do I need a page for every service and brand?",
         "You start with the ones that matter most, the exam searches and the eyewear you want more of, then expand. A focused set of strong exam, optical, and location pages ranks better than one thin page trying to cover everything at once."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks, while broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for optometrists"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-optometrists.html", "Staying visible in your area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Get a free audit that finds the gap between your website and the directories taking your new-patient searches, whether you work with us or not. No credit card, never a call center.",
},
]
