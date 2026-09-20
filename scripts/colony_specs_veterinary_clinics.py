"""Colony page specs for VETERINARY CLINICS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a veterinary-practice owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, veterinary-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear; no em/en dashes anywhere; never "leak" as a metaphor;
illustrative scenarios only, no named clients or competitors.

VETERINARY REALITY (what makes these pages distinct from the human-medical trades: it is pets):
the client is the pet owner and the patient is their animal; a sick or injured pet is an urgent,
emotional "can you see him today" call, and a missed one means the owner dials the next clinic or
drives to an emergency vet; the retention engine is wellness, vaccine, and dental RECALL reminders
because pets come due on a yearly cadence; a busy front desk juggling checkouts and a barking lobby
drops calls while rooming patients.

ETHICS (hard): the AI does scheduling and intake ONLY, never veterinary or medical advice. These
pages make NO animal-health or treatment-outcome claims. A true pet emergency is flagged to the
clinic staff or on-call and pointed to the hospital the clinic trusts, it is never diagnosed. The
owner sets what counts as an emergency and where those callers are sent.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 veterinary-website-cost                    (cost)     -> websites-seo-for-veterinary-clinics
  2 veterinary-answering-service-cost          (cost)     -> ai-receptionist-for-veterinary-clinics
  3 is-a-crm-worth-it-for-a-veterinary-clinic  (cost)     -> crm-for-veterinary-clinics
  4 why-veterinary-clinics-miss-calls          (problem)  -> ai-receptionist-for-veterinary-clinics
  5 why-pet-owners-skip-wellness-visits        (problem)  -> crm-for-veterinary-clinics
  6 how-do-veterinary-clinics-get-more-clients (how-to)   -> marketing-for-veterinary-clinics
"""

TOPICS = [
# ================ How Much Does a Veterinary Clinic Website Cost? (cost -> websites-seo) ================
{
    "slug": "veterinary-website-cost",
    "h1": "How Much Does a Veterinary Clinic Website Cost?",
    "title": "How Much Does a Veterinary Clinic Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A veterinary website must show a worried owner your hours, services, and how to reach you, then book. Top Shelf builds yours for $1,500 one-time, or free on any plan.",
    "answer": "For a veterinary clinic, the website has one job before price even matters: help a worried owner quickly see your hours, your services, how to reach you, and what to do after hours, then book. A custom site that does that is $1,500 one-time with Top Shelf, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a veterinary website actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Price follows purpose, so start with what the site has to do. When a pet is sick or hurt, the owner lands on your site scared and in a hurry, and the questions are immediate: can this clinic see my pet today, are you open right now, where are you, and what do I do if it is the middle of the night. A veterinary website earns its keep by answering those before anything else, with your hours and directions up top, the after-hours guidance you set for an owner who cannot wait until morning, and a number that is one tap to call from a phone.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Makes urgency obvious: your hours, whether you are open now, how to reach you fast, and the after-hours instructions you decide to show a worried owner.</li><li>Lays out the care you offer, from wellness exams and vaccines to dental, surgery, and boarding, so an owner knows you are the right clinic before they call.</li><li>Lets a new client start on their own: request an appointment, fill out new-patient intake, and reach a pet portal, instead of a contact form that goes nowhere.</li><li>Gets found when someone searches for a vet near them or an emergency vet, and is clear about what you handle, which is where most new clients begin.</li></ul>'},
        {"h2_html": "What that costs, and what it is <em>worth</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Once the site does that job, the price is easy to reason about. A cheap template you fill in yourself can get you online, but it rarely makes the urgent details obvious or gets found for the searches that bring new owners in, and you are left to maintain it. A site built to do the work above, and to be found for it, is worth more because a single new client is years of wellness visits, vaccines, and dentals for every animal in the house, plus the owners they refer once they trust you.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps the numbers simple. A custom five page site is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that helps owners actually find you is handled for you, and the Signature plan at $899 adds the phone and follow-up that answer and rebook the clients the site brings in. There is no setup fee either way. No honest company can promise a specific ranking on a specific date, because no one controls Google, but a free audit can show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that pays for itself",
    "bridge_text": "A veterinary website is only worth what it brings in. Ours is built to be found by owners in the towns you serve and to turn searches into booked visits, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-veterinary-clinics",
    "bridge_label": "Websites & SEO for veterinary clinics",
    "faqs": [
        ("What does a veterinary website actually need?",
         "The essentials are the ones a worried owner reaches for first: your hours and directions, the after-hours guidance you set, the services you offer, one-tap calling, and a way to request an appointment or start new-patient intake, often with a pet portal. After that, being found for a vet near them is what turns a search into a new client."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "veterinary_clinics", "trade_plural": "veterinary clinics",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ What Does a Veterinary Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "veterinary-answering-service-cost",
    "h1": "What Does a Veterinary Answering Service Cost?",
    "title": "What Does a Veterinary Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for veterinary clinics often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for veterinary clinics usually bill per call, per minute, or on a monthly retainer, so a busy stretch gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call, sorts a routine question from a pet that needs to be seen now, and books it, in the Signature plan at $899 a month flat.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy month turns into a big bill. A clinic also gets its heaviest call volume at the worst moments for a live service: the midday rush when the lobby is full and the front desk is checking owners out, the evenings after people get home from work, and the weekend when you are closed. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy day or a wave of simple questions runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a worried owner who needs a moment costs you more than a quick caller.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: an owner who thinks something is wrong with their pet does not leave a voicemail, they call the next clinic or drive to the emergency hospital. The real cost of no coverage is not a monthly fee, it is the client, and the years of visits for every animal in that home, who went to the practice that picked up. But a generic call center reading a script cannot calm a scared owner or tell your team what it needs to know, so you can pay for coverage and still get a poor handoff.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, asks what your team would ask, what kind of animal it is and what is going on, and either books the routine visit or flags a true emergency to your staff and points the owner to the hospital you trust. You set what counts as an emergency and where those callers are sent. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. It handles scheduling and intake, never medical advice, and one appointment it captures can be worth well more than the plan costs.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers every time, sorts a routine question from a pet that needs to be seen, and books it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-veterinary-clinics",
    "bridge_label": "AI receptionist for veterinary clinics",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the client it books instead of losing to voicemail while your front desk is rooming patients."),
        ("Does it give owners medical advice?",
         "No. It handles scheduling and intake only. It asks what your team would ask, books routine visits, and flags anything that sounds urgent to your staff, pointing a true after-hours emergency to the hospital you trust. A person always decides how a pet is cared for, never the software.")],
    "trade_slug": "veterinary_clinics", "trade_plural": "veterinary clinics",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============== Is a CRM Worth It for a Veterinary Clinic? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-veterinary-clinic",
    "h1": "Is a CRM Worth It for a Veterinary Clinic?",
    "title": "Is a CRM Worth It for a Veterinary Clinic? | Top Shelf Business Solutions",
    "meta_desc": "For most veterinary clinics a CRM pays for itself by bringing overdue pets back for vaccines and dentals. It comes in Top Shelf's Signature plan at $899/mo, not a separate bill.",
    "answer": "For most veterinary clinics, yes. A CRM pays for itself the first time it brings back a pet overdue for its vaccines, or the dental you recommended that never got booked. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a veterinary clinic when you have more clients and pets than anyone can personally keep track of, which is most established practices. It is not worth it if you are a brand-new clinic seeing a handful of patients a week and genuinely reaching every owner yourself, though that rarely stays true as you grow. Most clinics are not short on demand, they are short on follow-up, and that gap is exactly what a CRM closes. The honest test is simple: how many pets are overdue for vaccines, a wellness exam, or a dental you recommended and never got booked, and how many owners have not been in for more than a year? Those are the visits a CRM is built to recover, the recurring, predictable work that is the closest thing a clinic has to steady production.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a clinic is not the software, it is the work that stops slipping through. A dog due for its rabies booster in the spring, a cat overdue for a dental, a puppy that still needs the last of its shots, a household you have not seen since the family moved across town: each one is a visit you have half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It sends vaccine, heartworm, wellness, and dental reminders on a schedule you set, so the visits owners already intend to book actually get booked without your team working a spreadsheet of due dates.</li><li>It finds the pets that have gone quiet and nudges their owners back, which costs far less than winning a brand-new client.</li><li>It keeps every client and every pet in one place, so the reminders and history for the dog and both cats sit together and one call is a chance to catch the whole household up.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: bring back a handful of overdue pets and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your client list to work",
    "bridge_text": "The pets you already treat are the easiest exam rooms to fill. A CRM sends the recall reminders for you, so overdue vaccines and dentals come back to you instead of drifting to another practice.",
    "bridge_slug": "crm-for-veterinary-clinics",
    "bridge_label": "CRM for veterinary clinics",
    "faqs": [
        ("Is a CRM overkill for a small veterinary clinic?",
         "Not usually. Even a small practice sees more pets and households than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If pets go overdue and owners forget to rebook, a CRM earns its keep."),
        ("How is a CRM different from my practice management software?",
         "It sits alongside it as your follow-up and outreach layer. Your practice software records what happened at the visit, while the CRM reaches out on a schedule to bring the next one in, sending recall and reactivation reminders your team has no time to work by hand.")],
    "trade_slug": "veterinary_clinics", "trade_plural": "veterinary clinics",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ Why Do Veterinary Clinics Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-veterinary-clinics-miss-calls",
    "h1": "Why Do Veterinary Clinics Miss So Many Calls?",
    "title": "Why Do Veterinary Clinics Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Clinics miss calls because the front desk is rooming patients and checking owners out while the phone rings, and a worried owner does not leave a voicemail, they call the next clinic.",
    "answer": "Clinics miss calls because they come while the front desk is rooming a patient, checking an owner out, or calming a barking lobby, and an owner who thinks something is wrong with their pet does not leave a voicemail. They hang up and call the next clinic. The fix is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes while the front desk's <em>hands are full</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A veterinary front desk is one of the busiest in any local business. When the phone rings, your team is often holding a squirming cat still for a blood draw, walking a nervous owner back to a room, ringing up a checkout, or calming a lobby full of barking dogs, and none of those are moments they can stop and take a call. The busier the clinic, the more calls slip to voicemail, which means your best days are also the ones where the most calls go unanswered. It is not a discipline problem. A front desk cannot room patients, check owners out, and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a worried owner it is not one. Someone who thinks their pet is hurt is not going to leave a message and wait. They move down the search results until a person picks up and says yes, bring the pet in, and by the time your team clears a minute to check messages, the appointment is already booked somewhere else.</p>'},
        {"h2_html": "The missed call was a client for <em>years of visits</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The call that got missed was rarely a wrong number. It was an owner, and a good owner means years of wellness visits, vaccines, and dentals for every animal in the house, plus the people they refer once they trust you. Losing that call is not a small thing, and the calls you are most likely to miss, the evening and weekend ones, are often the most worried and the most valuable.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that answers no matter what the team is doing and can sort a call the way your staff would. A voicemail box cannot ask a question, and a generic call center does not know what to ask. What works is something that answers on the first ring, asks what kind of animal it is and what is going on, and either books a routine visit or flags a true emergency to your staff and points the owner toward the hospital you trust. It handles the scheduling and hands anything urgent to a person, so the call is captured instead of lost, and no owner is left talking to a recording.</p>'}],
    "bridge_h2": "Stop losing worried owners to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring while your front desk is rooming patients, sorts a routine question from a pet that needs to be seen, and books it or flags it to your staff, so the call never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-veterinary-clinics",
    "bridge_label": "AI receptionist for veterinary clinics",
    "faqs": [
        ("Would an owner rather reach a real person?",
         "In a worried moment, what an owner needs most is to know the clinic is handling it, and a calm voice that captures the details and gets the pet on the schedule beats a voicemail box every time. The receptionist is upfront about what it is, gathers the facts, and hands anything urgent straight to your staff."),
        ("Can I just forward calls to a staff cell instead?",
         "You can, but that only helps when someone is free to answer. Forwarding still rolls to voicemail when the whole team is rooming patients or the lobby is full. Something that always answers and sorts the call is what catches the ones a forward would still miss.")],
    "trade_slug": "veterinary_clinics", "trade_plural": "veterinary clinics",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ Why Do Pet Owners Skip Wellness Visits? (problem -> crm) ============
{
    "slug": "why-pet-owners-skip-wellness-visits",
    "h1": "Why Do Pet Owners Skip Wellness Visits?",
    "title": "Why Do Pet Owners Skip Wellness Visits? | Top Shelf Business Solutions",
    "meta_desc": "Most pet owners skip wellness visits not on purpose but because nobody reminded them. Life got busy, they meant to rebook, and the pet drifted overdue. A recall reminder brings them back.",
    "answer": "Most pet owners skip wellness visits not because they stopped caring, but because nobody reminded them. Life got busy, they meant to rebook, or they never scheduled after a canceled visit, and the pet quietly drifted overdue. A pet that has gone quiet usually belongs to an owner who forgot, not one who left.",
    "sections": [
        {"h2_html": "Overdue usually means forgotten, not <em>gone</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a pet that has gone overdue as an owner who moved on, so you let the name sit and move to the next patient. But most of the time the owner did not decide against you at all. They meant to bring the dog back after its last visit, then life got in the way. A puppy grew into an adult dog, the family moved across town, an appointment got canceled and never rebooked, or they left the exam unsure about a recommended dental and put it off. A year later they could not tell you when the pet was last seen.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The owner who comes back is usually the one who got a nudge at the right moment. A short, friendly reminder that the pet is due, coming from the clinic that already knows the animal by name, is often all it takes. It lands as a helpful note from someone they trust, not an ad from a stranger, and it turns a name sitting quietly in your records into a booked visit.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Clinics do not skip recall because they do not care. They skip it because the day fills up. The front desk is rooming patients, checking owners out, and working the phones, and nobody has an afternoon free to comb the records for every pet due this month. Done by memory, it only happens when things are slow, which is exactly when you have the fewest reminders to send.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A practice with thousands of pets cannot personally remember which dog is due for a booster, which cat is overdue for a dental, or which puppy still needs its last shots.</li><li>There is no system flagging which owners have gone quiet and which visits are slipping.</li><li>By the time an owner remembers on their own, they often book wherever they land instead of with you.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a caring problem, and it is the kind of thing you fix once and then it runs. When every due and overdue pet gets a timed reminder automatically, written to sound like your clinic, and one household is caught up together, the recurring visits owners already meant to book stop slipping away.</p>'}],
    "bridge_h2": "Bring overdue pets back on schedule",
    "bridge_text": "A CRM keeps every due and overdue pet in front of you and sends the recall reminders for you, so an owner who meant to rebook hears from you at the right moment instead of drifting to another practice.",
    "bridge_slug": "crm-for-veterinary-clinics",
    "bridge_label": "CRM for veterinary clinics",
    "faqs": [
        ("How often should we remind an owner about an overdue pet?",
         "A light touch when the pet is due, then a gentle follow-up if it lapses, catches most owners without being pushy. The key is that it happens at all and on time, from the clinic they already trust, which is exactly what a CRM handles for you on a schedule you approve."),
        ("Does an automated reminder feel impersonal?",
         "Not when it is written to sound like your clinic and sent at a sensible pace. A short note that a pet is due reads as attentive, not spammy, because the owner meant to come back and simply forgot. You can always jump in and message any client directly.")],
    "trade_slug": "veterinary_clinics", "trade_plural": "veterinary clinics",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ======== How Do Veterinary Clinics Get More Clients? (how-to -> marketing) ========
{
    "slug": "how-do-veterinary-clinics-get-more-clients",
    "h1": "How Do Veterinary Clinics Get More Clients?",
    "title": "How Do Veterinary Clinics Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "Veterinary clinics get more new clients by being easy to find when someone searches for a vet nearby and easy to reach when they call. The map pack and reviews are where new clients start.",
    "answer": "Veterinary clinics get more new clients two ways: being easy to find when someone searches for a vet nearby, and being easy to reach when they call. Most new-client searches start in Google's map pack, so a verified, active, well-reviewed profile is usually where the phone starts ringing.",
    "sections": [
        {"h2_html": "New clients start when someone searches for a <em>vet nearby</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a new resident, a first-time puppy owner, or someone whose regular vet could not get them in looks for a clinic, the first thing Google shows is not a website at all. It is the map pack, the little map with three local listings, star ratings, and a call button. Most people pick from those three without scrolling to the results below. So if you are wondering why new faces are not walking in even though you do great work, the answer is often that you are not in those three, and almost nobody looks past them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting into the map pack is a different job from having a website. It runs on your Google Business Profile: whether it is verified, complete, and active, how close you are to the searcher, and how many recent, genuine reviews you have. A great clinic with a neglected profile is a well-kept secret at the exact moment an owner is choosing who to call.</p>'},
        {"h2_html": "What actually brings new clients <em>through the door</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting found is usually a handful of fixable things, not a mystery. Google tends to trust profiles that look active and legitimate, and quietly buries the ones that look abandoned.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A Google Business Profile that is verified, complete, and correct on your hours, services, and location.</li><li>A steady flow of real reviews, and a reply to each one, which reassures the next owner and helps your local ranking.</li><li>A website that loads fast and shows up for the towns you serve and the services you offer, from wellness and vaccines to dentals and surgery.</li><li>Answering the calls those searches create, so a new owner who finally reaches a person actually gets on the schedule.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this requires gimmicks or invented promises, just steady attention to the profile and the site owners actually see. Do it consistently and a neglected profile can climb over a few weeks, then compound as reviews and photos build. What no one can honestly promise is a specific spot on the map, because Google decides that, but the levers above are the ones that move it, and the cheapest new business of all is keeping the clients you already win coming back.</p>'}],
    "bridge_h2": "Get found where new clients start",
    "bridge_text": "Most new-client searches begin in the map pack. Keeping your Google profile verified, active, and full of recent reviews is how a clinic shows up when an owner nearby is choosing who to call.",
    "bridge_slug": "marketing-for-veterinary-clinics",
    "bridge_label": "Marketing for veterinary clinics",
    "faqs": [
        ("Do we need a website to show up on Google Maps?",
         "Not to appear in the map pack, which runs on your Google Business Profile. A website helps you rank in the results below the map and gives the profile something to link to, but the fastest way onto the map itself is a verified, active, well-reviewed profile."),
        ("How long until we start showing up?",
         "A neglected profile that gets verified, completed, and active can start climbing within a few weeks, and it compounds as reviews build. Nobody controls Google, so no honest company promises a specific position, but consistency on the profile is what moves it.")],
    "trade_slug": "veterinary_clinics", "trade_plural": "veterinary clinics",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
]


if __name__ == "__main__":
    # Self-check the hard rules without touching the generator. ponytail: plain asserts, no framework.
    import re

    REQUIRED_KEYS = {"slug", "h1", "title", "meta_desc", "answer", "sections", "bridge_h2",
                     "bridge_text", "bridge_slug", "bridge_label", "faqs", "trade_slug",
                     "trade_plural", "hub_name", "hub_slug"}
    EXPECTED = {
        "veterinary-website-cost": "websites-seo-for-veterinary-clinics",
        "veterinary-answering-service-cost": "ai-receptionist-for-veterinary-clinics",
        "is-a-crm-worth-it-for-a-veterinary-clinic": "crm-for-veterinary-clinics",
        "why-veterinary-clinics-miss-calls": "ai-receptionist-for-veterinary-clinics",
        "why-pet-owners-skip-wellness-visits": "crm-for-veterinary-clinics",
        "how-do-veterinary-clinics-get-more-clients": "marketing-for-veterinary-clinics",
    }
    ALLOWED_PRICES = {"299", "899", "2500", "1500"}

    def _strings(v):
        if isinstance(v, str):
            yield v
        elif isinstance(v, dict):
            for x in v.values():
                yield from _strings(x)
        elif isinstance(v, (list, tuple)):
            for x in v:
                yield from _strings(x)

    assert len(TOPICS) == 6, f"want 6 dicts, got {len(TOPICS)}"
    slugs = [t["slug"] for t in TOPICS]
    assert len(set(slugs)) == 6, f"slugs not unique: {slugs}"
    assert set(slugs) == set(EXPECTED), f"slug set mismatch: {set(slugs) ^ set(EXPECTED)}"

    for t in TOPICS:
        assert set(t) == REQUIRED_KEYS, f"{t['slug']} key mismatch: {set(t) ^ REQUIRED_KEYS}"
        assert t["bridge_slug"] == EXPECTED[t["slug"]], f"{t['slug']} bad bridge"
        assert t["trade_slug"] == "veterinary_clinics" and t["trade_plural"] == "veterinary clinics"
        assert t["hub_name"] == "Medical & Dental" and t["hub_slug"] == "industry-medical-dental.html"
        # AEO answer target band (money specs run ~40-70 words).
        assert 35 <= len(t["answer"].split()) <= 75, f"{t['slug']} answer {len(t['answer'].split())} words"
        # 350+ visible words in the page body (both section bodies, tags stripped).
        body = " ".join(re.sub(r"<[^>]+>", " ", s["body_html"]) for s in t["sections"])
        wc = len(body.split())
        assert wc >= 350, f"{t['slug']} body only {wc} words"
        # No em/en dashes anywhere; never "leak"/"leaks"; only whitelisted prices.
        for s in _strings(t):
            assert "—" not in s and "–" not in s, f"{t['slug']} has an em/en dash"
            assert not re.search(r"\bleaks?\b", s, re.I), f"{t['slug']} uses 'leak'"
            for amt in re.findall(r"\$([\d,]+)", s):
                assert amt.replace(",", "") in ALLOWED_PRICES, f"{t['slug']} bad price ${amt}"

    print(f"OK: 6 veterinary colony specs, bodies {[len(' '.join(re.sub(r'<[^>]+>', ' ', s['body_html']) for s in t['sections']).split()) for t in TOPICS]} words")
