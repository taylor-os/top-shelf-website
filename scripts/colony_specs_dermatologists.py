"""Colony page specs for DERMATOLOGISTS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a dermatology-practice owner or office manager would search, answered
directly up top (the 40-60 word AEO answer), then two body sections, then a "the fix" bridge
that funnels the page's authority into the ONE money page the question implies. Lighter than a
money page.

Each dict here owns UNIQUE, hand-written, dermatology-specific substance (the generator owns
shell, schema, events, keyword placement). Same honesty rules as the money specs and the
sibling colony files: no invented stats, percentages, prices, or clients; hedge instead of
overpromise; only the real prices ($299/$899/$2,500 plans, $1,500 one-time site) ever appear,
with the CRM and AI receptionist bundled in the $899 Signature plan; no em/en dashes anywhere;
never "leak" as a metaphor. Dermatology ethics on top: the AI does scheduling and intake only,
never medical, cosmetic, or skin advice, makes no medical or outcome claims, and is HIPAA-aware.

What keeps these distinct from other medical trades: a dermatology practice runs a MEDICAL side
(skin checks, changing moles, biopsies, acne, eczema, rashes, insurance and referrals) and a
COSMETIC side (self-pay Botox, laser, peels) at once; new-patient waitlists run weeks out so
phone volume and rescheduling are heavy; annual skin-check recall and cosmetic rebooking are the
retention engines; referrals come from primary care doctors; and a missed call means the patient
books the next dermatologist. Never the med-spa, dentist, or plumber content reworded.

Six questions, mixed cost / problem / how-to, across four money pages:
  1 dermatologist-website-cost                     (cost)    -> websites-seo-for-dermatologists
  2 dermatology-answering-service-cost             (cost)    -> ai-receptionist-for-dermatologists
  3 is-a-crm-worth-it-for-a-dermatology-practice   (cost)    -> crm-for-dermatologists
  4 why-dermatology-practices-miss-calls           (problem) -> ai-receptionist-for-dermatologists
  5 why-dermatology-patients-dont-rebook           (problem) -> crm-for-dermatologists
  6 how-do-dermatologists-get-more-patients        (how-to)  -> marketing-for-dermatologists
"""

TOPICS = [
# ============ How Much Does a Dermatologist Website Cost? (cost -> websites-seo) ============
{
    "slug": "dermatologist-website-cost",
    "h1": "How Much Does a Dermatologist Website Cost?",
    "title": "How Much Does a Dermatologist Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A dermatology website should book skin checks and cosmetic consults and rank for dermatologist near me. Top Shelf builds yours for $1,500, or free on any monthly plan.",
    "answer": "A dermatology practice website can cost a few hundred dollars for a template or several thousand for a custom build, but the real question is whether it books skin checks and cosmetic consults instead of just sitting there. Top Shelf builds a custom five page site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "A dermatology site has to serve two practices at <em>once</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">What a dermatology website has to do is not what a generic small-business site does, and that is what you are really paying for. Your practice runs two fronts at once, and the site has to make both obvious in the first few seconds. On the medical side a visitor needs to see skin checks, mole and skin-cancer screenings, acne, eczema, and rashes, the insurance plans you take, whether you are accepting new patients, and what a first visit involves. On the cosmetic side someone weighing a self-pay treatment wants the Botox, laser, and peel services laid out clearly, with honest price context and before-and-after examples that help them decide whether to book a consult. A single muddled page that treats those two very different visitors the same sends both to a practice whose site spoke to them directly.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It also has to turn that visitor into an appointment without a phone call, which matters more for dermatology than for almost any other practice, because when you are booked out weeks a patient will not wait on hold. A clear button to book a skin check or schedule a cosmetic consult, tap-to-call, and a simple request form on every page catch the patient the moment they decide, day or night. And none of it works if you cannot be found, so the site has to show up when someone nearby searches for a dermatologist near me or a skin cancer screening, so the practice they reach first is yours and not a directory that lines three other practices up beside you.</p>'},
        {"h2_html": "What it should cost, and what makes it <em>worth it</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Price matters, but for a physician practice it comes second to whether the site earns trust and stays yours. A patient about to let you examine their skin or treat their face judges your credibility in seconds, so a fast, current, clearly professional site does quiet work a cheap template cannot, while a dated one undercuts the reputation your physicians have actually earned. Just as important is who owns it. A site you own outright keeps ranking and booking patients for as long as it exists, registered to your practice, where a rented template or a pay-per-lead arrangement stops the day you stop paying and never really made those patients yours.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps the pricing simple. A custom five page site is $1,500 one-time, yours to keep, or it is included free on any monthly plan starting at $299, where the ongoing SEO that gets it ranking for the searches your patients make is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit will show you exactly where your current site stands and how many searches it is missing today.</p>'}],
    "bridge_h2": "Get a site that pays for itself",
    "bridge_text": "A dermatology website is only worth what it brings in. Ours is built to rank for the towns you cover and the treatments you offer, look credible to a new patient, and turn searches into booked visits, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-dermatologists",
    "bridge_label": "Websites & SEO for dermatologists",
    "faqs": [
        ("What should a dermatology website have that a generic one does not?",
         "It has to speak to both sides of your practice at once: the medical visitor checking whether you take their insurance, are accepting new patients, and handle skin checks or a worrying mole, and the cosmetic visitor weighing a self-pay Botox, laser, or peel consult who wants clear services and honest price context. It should let either one book or request a visit in a tap, and it should show up when someone nearby searches for a dermatologist near them."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep, registered to your practice. On a monthly plan the site is built for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "dermatologists", "trade_plural": "dermatologists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ======== What Does a Dermatology Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "dermatology-answering-service-cost",
    "h1": "What Does a Dermatology Answering Service Cost?",
    "title": "What Does a Dermatology Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Dermatology answering services often bill per call or minute, which adds up. Top Shelf's AI receptionist answers 24/7 in the Signature plan at $899 a month.",
    "answer": "Traditional answering services for dermatology practices usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call 24/7 and books the visit comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy month turns into a big bill. A dermatology practice gets calls at every hour, the worried patient who spots something on a Sunday, the new patient calling after work, so after-hours minutes, which tend to cost the most, are exactly the ones you cannot skip. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of cosmetic price-shoppers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a nervous patient with a lot of questions costs more than a quick booking.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a patient who just noticed a changing mole, or finally decided to book a consult, does not leave a voicemail, they call the next dermatologist. The real cost of no coverage is not a monthly fee, it is the new patient who booked elsewhere, and in dermatology that patient can mean years of skin checks and the family they refer. But a generic call center reading a script cannot tell a skin check from a cosmetic question, or sort which caller your team has said to treat as urgent, so you can pay for coverage and still get poor triage.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, sorts a medical visit from a cosmetic consult the way you tell it to, and books the appointment or flags a call that sounds urgent to your team. It handles scheduling and intake only, never medical or skin advice, and you decide what it says about insurance and coverage. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One new patient it books after hours can be worth well more than the plan costs, and everything it catches after that is on top.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, sorts a skin check from a cosmetic consult, books it, and flags anything urgent to your team, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-dermatologists",
    "bridge_label": "AI receptionist for dermatologists",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter and no after-hours surcharge. The bigger saving is the new patient it books instead of losing to voicemail on a night or a weekend."),
        ("Does it give patients medical or skin advice over the phone?",
         "No. It handles scheduling and intake only, the same questions your front desk would ask to book a visit, and it never offers medical or cosmetic advice. A call that sounds urgent by the rules you set is flagged straight to your team, and your physicians make every clinical decision.")],
    "trade_slug": "dermatologists", "trade_plural": "dermatologists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ======== Is a CRM Worth It for a Dermatology Practice? (cost -> crm) ========
{
    "slug": "is-a-crm-worth-it-for-a-dermatology-practice",
    "h1": "Is a CRM Worth It for a Dermatology Practice?",
    "title": "Is a CRM Worth It for a Dermatology Practice? | Top Shelf Business Solutions",
    "meta_desc": "For most dermatology practices a CRM pays for itself by rebooking one lapsed skin-check or cosmetic patient. It comes in Top Shelf's Signature plan at $899 a month.",
    "answer": "For most dermatology practices, yes. A CRM pays for itself the first time it brings back a patient due for an annual skin check, or a cosmetic patient who meant to keep up and drifted. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a dermatology practice when you have more patients and recalls than anyone at the front desk can track, which is most established practices. It is not worth it if you are a brand-new solo practice seeing a handful of patients a week and genuinely reaching every one when they are due, though that rarely stays true as you grow. The honest test is simple: how many patients did you tell to come back for a skin check or to recheck a spot who never got a reminder, and how many cosmetic patients meant to keep up and quietly drifted? Those are the visits a CRM is built to recover, and they are visits you have already earned once.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a dermatology practice is not the software, it is the repeat business that stops slipping away. A patient overdue for an annual skin exam, someone you asked to watch a spot and recheck in six months, a cosmetic patient whose treatment has worn off: each one is a visit you have already half-earned and are one well-timed reminder away from rebooking. On their own these patients quietly fall off the schedule, because no one at a busy front desk has time to watch the dates for a few thousand people.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It sends skin-check and recheck reminders on the schedule you set, so the visit you already recommended actually lands instead of being forgotten.</li><li>It fires cosmetic maintenance reminders on the cadence those treatments run on, so that side of the practice rebooks without anyone tracking dates.</li><li>It keeps every patient, their history, and what they are due for in one place, and lets you reactivate everyone overdue with a single message instead of chasing new patients with ads.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: bring back one patient you would have lost and it has paid for itself. In a field where a single patient can mean a decade of annual skin checks and the cosmetic visits that come up along the way, everything after that first recovered visit is margin.</p>'}],
    "bridge_h2": "Put your patient list to work",
    "bridge_text": "The patients you have already seen are the cheapest visits you can book. A CRM reminds every one when a skin check or a cosmetic touch-up is due, so they come back to you instead of drifting to whoever reaches them first.",
    "bridge_slug": "crm-for-dermatologists",
    "bridge_label": "CRM for dermatologists",
    "faqs": [
        ("Is a CRM overkill for a small dermatology practice?",
         "Not usually. Even a small practice sees more patients and owes more skin-check recalls than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If recalls go out late or not at all and lapsed patients never hear from you, a CRM earns its keep."),
        ("How is a CRM different from my practice management or EHR software?",
         "Your EHR records who came in and stores the clinical chart. A CRM sits alongside it as the follow-up layer: it knows who is due for a skin check or a cosmetic touch-up and reaches out for you on schedule, so the patient list you already have actively brings people back instead of just recording history.")],
    "trade_slug": "dermatologists", "trade_plural": "dermatologists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ======== Why Do Dermatology Practices Miss So Many Calls? (problem -> ai-receptionist) ========
{
    "slug": "why-dermatology-practices-miss-calls",
    "h1": "Why Do Dermatology Practices Miss So Many Calls?",
    "title": "Why Do Dermatology Practices Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Dermatology practices miss calls because the front desk is buried in insurance, referrals, and a weeks-long waitlist, and a worried patient just calls the next one.",
    "answer": "Dermatology practices miss calls because they come while the front desk is buried, verifying insurance, chasing a referral, checking a patient in, or working a waitlist that already runs weeks out, and a worried patient does not leave a voicemail. They call the next dermatologist. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes while your front desk is <em>already buried</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A dermatology front desk is rarely idle. When the phone rings, someone is usually verifying insurance, chasing down a referral or a prior authorization, checking in a patient for a procedure, or working a new-patient waitlist that already runs weeks out. Every one of those tasks needs their full attention, and none of them can stop mid-sentence to catch a call, so the phone rings through to voicemail while their hands are full. The busier the practice, the more calls slip past, which means your best stretches are also when the most new patients go unanswered. It is not a discipline problem. A front desk cannot do the work in front of it and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a worried patient it is not one. Someone who just noticed a mole that changed, a spot that started bleeding, or a rash that will not settle is anxious now and is not going to leave a message and wait. They move down the search results until a real person answers and says yes, we can get you in, and by the time anyone checks the voicemail, that patient is already booked somewhere else.</p>'},
        {"h2_html": "The calls you miss are the new patients you can <em>least afford to lose</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. The one that rolls to voicemail is often a brand-new patient: a worried-mole call, a referral a primary care doctor just sent over, or a cosmetic consult ready to book. In dermatology, one new patient can mean years of annual skin checks, the treatments that come up along the way, and the family they refer, so a missed call is not a small thing lost, it is a long relationship handed to the practice that picked up. And the calls most likely to be missed, after hours, over lunch, during a packed clinic, are exactly the ones you want most.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that answers no matter what the front desk is in the middle of, and can sort one kind of call from another. A voicemail box cannot triage, and a generic call center does not know a skin check from a filler question, or which caller your team has said to treat as urgent. What actually works is something that answers on the first ring, day or night, asks what brings the patient in, books a medical visit or a cosmetic consult onto the right kind of appointment, and flags a call that sounds urgent straight to your team. It handles the scheduling and intake, and leaves every clinical decision to your physicians, so the patient is captured instead of lost.</p>'}],
    "bridge_h2": "Stop sending new patients to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, no matter how buried the front desk is, sorts a skin check from a cosmetic consult, books it, and flags anything urgent to your team, so the patient never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-dermatologists",
    "bridge_label": "AI receptionist for dermatologists",
    "faqs": [
        ("Would a patient rather reach a real person?",
         "What a worried patient needs most is to reach someone who takes down what is going on and gets them booked, and a calm answer beats a voicemail box every time. The AI receptionist is upfront about what it is, handles the scheduling and intake, and hands a call that sounds urgent straight to your team so a person follows up."),
        ("Can I just send overflow to the front desk voicemail or my staff cells?",
         "That only helps when someone is free, and the whole problem is that your front desk is buried. Overflow still rolls to voicemail during a packed clinic or after hours, which is when the most new-patient calls come in. Something that always answers and sorts the call is what catches the ones a voicemail would lose.")],
    "trade_slug": "dermatologists", "trade_plural": "dermatologists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ======== Why Don't Dermatology Patients Rebook? (problem -> crm) ========
{
    "slug": "why-dermatology-patients-dont-rebook",
    "h1": "Why Don't Dermatology Patients Rebook?",
    "title": "Why Don't Dermatology Patients Rebook? | Top Shelf Business Solutions",
    "meta_desc": "Most dermatology patients don't rebook because no reminder ever reached them, not because they chose to leave. The skin check you recommended just needed a timed nudge.",
    "answer": "Most dermatology patients do not rebook because no reminder ever reached them, not because they chose to leave. You told them to come back for a skin check or to recheck a spot, they meant to, life got busy, and no nudge came. A missed rebook is usually a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "Silence usually means forgotten, not a <em>decision to leave</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a patient who never rebooked as someone who moved on, so you let it go. But most of the time they did not decide against you at all. On the way out you told them to come back in a year for a full skin exam, or in a few months so you could recheck a mole you wanted to watch. They meant to. Then life filled up, no reminder ever came, and they resurface a year or two later only when something scares them, if they come back to you at all instead of searching from scratch.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The cosmetic side works the same way. A patient whose treatment has worn off meant to keep it up, but nothing prompted them at the right moment, so the booking they intended to make quietly never happened. In both cases the visit was never a no. It just needed a well-timed nudge, and that is exactly the thing a front desk working a weeks-long waitlist never gets around to sending.</p>'},
        {"h2_html": "Why the reminder <em>never goes out</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Practices do not skip recall because they do not care. They skip it because the day fills up. The front desk is booking the patients in front of them, verifying insurance, and working a waitlist that already runs weeks out, and the reminder for a skin check a year away is always the thing that can wait until later, which never comes. Done by memory, recall only happens when the schedule is quiet, which is exactly when you least need it.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system tracking who is due for a skin check, whose recheck is coming up, or which cosmetic patient has lapsed.</li><li>The reminder depends on a person remembering, so it competes with the patients standing at the desk and loses.</li><li>By the time anyone circles back, the patient has drifted, and often started over with whoever they found in a search.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not an effort problem, and it is the kind of thing you fix once and then it just runs. When every skin-check recall, every recheck, and every cosmetic maintenance date gets a timed reminder automatically, written to sound like the practice the patient already trusts, the visit you recommended in the room actually lands on the schedule, and the patients you have already earned stop drifting away.</p>'}],
    "bridge_h2": "Bring every patient back on schedule",
    "bridge_text": "A CRM holds every skin-check recall, recheck, and cosmetic maintenance date and sends the reminder for you, written to sound like your practice, so the visit you recommended in the room actually lands instead of being forgotten.",
    "bridge_slug": "crm-for-dermatologists",
    "bridge_label": "CRM for dermatologists",
    "faqs": [
        ("How often should I remind a patient about a skin check?",
         "A reminder when the recall is actually due catches most of them, then a gentle follow-up if they lapse. The point is that it happens at all and on time, which is what a CRM handles for you, so the annual exam or the recheck you recommended goes out on schedule without anyone at the desk tracking dates."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like your practice and sent at a sensible pace. A short, friendly reminder that a skin check is due reads as attentive, not pushy, and most patients are glad for the nudge because they meant to rebook and forgot. You can always step in and reach out to anyone yourself.")],
    "trade_slug": "dermatologists", "trade_plural": "dermatologists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ======== How Do Dermatologists Get More Patients? (how-to -> marketing) ========
{
    "slug": "how-do-dermatologists-get-more-patients",
    "h1": "How Do Dermatologists Get More Patients?",
    "title": "How Do Dermatologists Get More Patients? | Top Shelf Business Solutions",
    "meta_desc": "Dermatologists get more patients by being easy to find and trust the moment someone searches: an active Google profile, fresh reviews, and a website that ranks nearby.",
    "answer": "Dermatologists get more patients by being easy to find and trust the moment someone searches, a complete, active Google Business Profile, a steady flow of genuine reviews, and a website that ranks for the conditions and treatments you offer nearby. New patients, medical and cosmetic, almost always start with a search and pick the practice they can find first.",
    "sections": [
        {"h2_html": "New patients almost all start with a <em>search</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Dermatology demand comes in two flavors, and both begin the same way. Someone finds a spot that worries them, or a stubborn case of acne or eczema they finally want handled, and they search for a dermatologist near them. Or someone has been thinking about Botox, a laser treatment, or a peel and goes looking for a practice they trust to do it. Either way they glance at the map, read who has the most reviews and the strongest ratings close by, and decide in that moment, because they are about to trust a stranger with their skin and, on the cosmetic side, their face.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Referrals from primary care doctors still matter, and they always will, but even a referred patient usually searches your name and reads a review or two before they call. So whether a patient comes from a search, a referral, or a neighbor, the practice that is easy to find and clearly trusted online is the one that turns that interest into a booked visit. A great practice with a thin, neglected online presence quietly loses those patients to the one that looks active, and you never see the person who scrolled past.</p>'},
        {"h2_html": "What actually brings dermatology patients <em>in</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more patients is less about one clever trick and more about being present and credible everywhere a patient looks before they book. A handful of things move the needle, and they compound on each other.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep your Google Business Profile complete and active: real photos of the office and physicians, accurate hours, the insurance you take, whether you are accepting new patients, and the medical and cosmetic services you offer.</li><li>Build a steady flow of genuine reviews by asking every satisfied patient at the right moment and replying to each one, because letting someone examine your skin or treat your face takes trust, and patients read reviews closely before they choose.</li><li>Focus on the neighborhoods you actually serve, so your visibility reaches the patients close enough to become regulars rather than a whole metro that never makes the drive.</li><li>Rank a website for the conditions, treatments, and towns you want more of, so a patient searching finds you directly instead of a national directory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Dermatology demand also has a rhythm worth getting ahead of, sun and summer push skin-check worry, the year-end rush brings patients who have finally met their deductible, and weddings and the holidays send the cosmetic side searching, so being visible right before each wave beats scrambling once it hits. What no honest company can promise is a specific spot on Google, because no one controls that, but keeping your profile active, your reviews fresh, and your site ranking is what moves it. A free audit can show you how easily a patient nearby can find and trust you today.</p>'}],
    "bridge_h2": "Be the practice they find first",
    "bridge_text": "Most new patients, medical and cosmetic, start with a search. Keeping your Google profile active, your reviews fresh, and your local presence strong is how you show up and earn the booking when someone nearby is choosing a dermatologist.",
    "bridge_slug": "marketing-for-dermatologists",
    "bridge_label": "Marketing for dermatologists",
    "faqs": [
        ("What is the single best way to get more dermatology patients?",
         "There is no one silver bullet, but for most practices the fastest lever is a complete, active Google Business Profile with a steady flow of genuine reviews, because that is exactly where patients look when they are choosing a dermatologist nearby. A website that ranks for your conditions and treatments compounds it over time."),
        ("How much do reviews really matter for a dermatology practice?",
         "A lot, because trust is the whole decision here. A patient about to let someone examine their skin or treat their face reads reviews closely before they book. Asking every satisfied patient at the right moment and replying to each review feeds both your ranking in the local map and the trust a new patient needs, as long as you keep it honest and never filter or pay for reviews.")],
    "trade_slug": "dermatologists", "trade_plural": "dermatologists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
]
