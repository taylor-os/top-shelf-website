"""Colony page specs for AUTO REPAIR SHOPS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question an auto-repair-shop owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, auto-repair-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear; no em/en dashes anywhere. The AI does intake and scheduling
only, it never diagnoses a car or quotes a repair, and there are no repair-outcome or savings
guarantees. A literal oil or coolant leak is fine; "leak" is never a money metaphor.

Six questions, mixed cost / problem / how-to, funneled to four money pages:
  1 auto-repair-shop-website-cost               (cost)    -> websites-seo-for-auto-repair-shops
  2 auto-repair-answering-service-cost          (cost)    -> ai-receptionist-for-auto-repair-shops
  3 is-a-crm-worth-it-for-an-auto-repair-shop   (cost)    -> crm-for-auto-repair-shops
  4 why-auto-repair-shops-miss-calls            (problem) -> ai-receptionist-for-auto-repair-shops
  5 why-auto-repair-customers-dont-come-back    (problem) -> crm-for-auto-repair-shops
  6 how-do-auto-repair-shops-get-more-customers (how-to)  -> marketing-for-auto-repair-shops
"""

TOPICS = [
# ============ How Much Does an Auto Repair Shop Website Cost? (cost -> websites-seo) ============
{
    "slug": "auto-repair-shop-website-cost",
    "h1": "How Much Does an Auto Repair Shop Website Cost?",
    "title": "How Much Does an Auto Repair Shop Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "An auto repair shop website ranges from cheap templates to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "An auto repair shop website can run from a couple hundred for a DIY template to several thousand for a custom build. What matters more than the price is whether a driver searching nearby can find you and tap to call in one thumb. Top Shelf builds a custom five page site for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a repair shop website actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A driver whose check engine light just came on, or whose car is making a noise on the way to work, does the same thing everyone does now: they pull out a phone and search for a shop near them. They are in a hurry, sometimes stranded in a parking lot, and they are deciding in about ten seconds who to call. Your website has one job in that moment, to let them tap your number before they scroll past you. Everything else it does is in service of that.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Load fast on a phone and put a tap-to-call button in front of the driver before they have to scroll or pinch.</li><li>Rank for the searches drivers actually type, auto repair near me, mechanic near me, plus the specific services and the towns you cover.</li><li>Show plainly what you work on, brakes, diagnostics, oil changes, state inspection, air conditioning, so a driver knows their problem is one you handle.</li><li>Carry your real Google reviews up top, because a stranger about to hand over their car and their wallet is deciding whether to trust you.</li><li>Give an easy way to request an appointment or a quote without a call, for the driver who cannot talk right now but does not want to lose your number.</li></ul>'},
        {"h2_html": "What it costs, and what Top Shelf <em>charges</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The price you see quoted swings wildly because you are not all buying the same thing. A template you fill in yourself and a custom site built to rank in your area are different products with the same name. A do-it-yourself builder is cheap every month, but you do the work and it is rarely built to rank or to convert a driver in a hurry. A one-time custom build is yours to keep but does little if nobody is doing the ongoing SEO to get it found. The most expensive site of all is a pretty one that never ranks and buries your phone number, because you paid for it and it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that turns searches into drop-offs",
    "bridge_text": "A repair shop website is only worth the drop-offs it books. Ours is built to rank for the drivers searching nearby and turn a tap into a call, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-auto-repair-shops",
    "bridge_label": "Websites & SEO for auto repair shops",
    "faqs": [
        ("Do I even need a website if I already have a Google listing?",
         "The listing helps drivers find you, but the website is where a stranger decides whether to trust you with their car. It carries your services, your reviews, a tap-to-call button, and a way to request a quote, and it gives your Google profile something to link to. The two work together, and a good site strengthens the listing."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "auto_repair_shops", "trade_plural": "auto repair shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ========= What Does an Auto Repair Answering Service Cost? (cost -> ai-receptionist) =========
{
    "slug": "auto-repair-answering-service-cost",
    "h1": "What Does an Auto Repair Answering Service Cost?",
    "title": "What Does an Auto Repair Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for auto repair shops often bill per call or minute, which adds up fast. Top Shelf includes an AI receptionist in the Signature plan at $899/mo flat.",
    "answer": "Traditional answering services for auto repair shops usually bill per call, per minute, or a monthly retainer, so a busy stretch gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers on the first ring and books the drop-off comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy week turns into a big invoice. For an auto shop the sting is worse, because the calls you most need answered land right in the middle of the workday, when the counter is empty and every tech is under a car. It helps to know the common models before you sign one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for every call answered, so a busy stretch or a run of tire-kickers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty caller or a slow operator costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of calls or minutes, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first bill lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple. A driver whose car will not start, or who just saw a warning light on the way to work, does not leave a voicemail. They call the next shop on the list until a person picks up. The real cost of no coverage is not a monthly fee, it is the drop-off that went to the shop that answered. But a generic call center reading a script cannot tell a tow from a routine oil change, so you can pay for coverage and still get poor intake.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, whether the bay is slammed or the shop has already closed for the night. It asks whether the car is drivable or needs a tow, gathers the year, make, model, and the complaint, and books the drop-off on your schedule or flags it to your phone. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One first-time driver you would have lost to voicemail can be worth years of steady work. It does the intake and the booking only. It does not diagnose the car or price the repair, that stays with you and your techs.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers whenever the phone rings, sorts a tow from an oil change, and books the drop-off, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-auto-repair-shops",
    "bridge_label": "AI receptionist for auto repair shops",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the drop-off it books after hours instead of losing to voicemail."),
        ("Does it decide what is wrong with the car or price the repair?",
         "No. It handles intake and scheduling only: what the car is doing, whether it is drivable or needs a tow, and getting it onto your calendar with the details. Diagnosing the problem and quoting the work stay with you and your techs, where they belong.")],
    "trade_slug": "auto_repair_shops", "trade_plural": "auto repair shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Is a CRM Worth It for an Auto Repair Shop? (cost -> crm) ============
{
    "slug": "is-a-crm-worth-it-for-an-auto-repair-shop",
    "h1": "Is a CRM Worth It for an Auto Repair Shop?",
    "title": "Is a CRM Worth It for an Auto Repair Shop? | Top Shelf Business Solutions",
    "meta_desc": "For most auto repair shops a CRM pays for itself by reviving one cold estimate and bringing past customers back for service. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most auto repair shops, yes. A CRM pays for itself the first time it wins back an estimate a driver was thinking over, or brings a past customer back for an oil change, brakes, or a state inspection. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for an auto repair shop when you have more open estimates and past customers than you can keep track of in your head, which is most shops with a steady bay. It is not worth it if you are a one-bay operation doing a handful of cars a week and genuinely calling every customer back, though that rarely stays true as you grow. The honest test is simple. How many estimates from a vehicle inspection did you write last month that nobody ever followed up on, and how many past customers have not been in for a year? Those are the jobs a CRM is built to recover, and for most shops there are more of them than the owner would guess. The point is not the size of the shop, it is whether the repeat and deferred work keeps falling through the cracks between busy days.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM is not the software, it is the recurring work that stops slipping away. A driver sitting on a brake estimate, a family whose car you serviced last year, a state inspection coming due next month: each one is a job you have already half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open estimate on a schedule, so a driver deciding whether to spend the money keeps hearing from you instead of forgetting.</li><li>It fires service reminders, an oil change by mileage or by months, the state inspection before it lapses, a timing belt or fluid service at the right interval, so recurring work comes back without you tracking dates.</li><li>It keeps every customer, vehicle, and service history in one place instead of a drawer of paper tickets and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and the follow-up that feed it. The math is the same as the answering service: recover one deferred job you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your customer list to work",
    "bridge_text": "The open estimates and past customers you already have are the cheapest jobs you can book. A CRM follows up on every one for you, so the car comes back to you instead of the shop that stayed in touch.",
    "bridge_slug": "crm-for-auto-repair-shops",
    "bridge_label": "CRM for auto repair shops",
    "faqs": [
        ("Is a CRM overkill for a small auto shop?",
         "Not usually. Even a one or two bay shop services more vehicles and writes more estimates than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If estimates go cold and past customers forget your name, a CRM earns its keep."),
        ("How is a CRM different from the shop management system I already have?",
         "Most shop systems store the history but do not chase the work. A CRM follows up on cold estimates, nudges customers who are due for service, and tells you who has gone quiet, on a schedule, so the repeat and deferred work actually shows up instead of depending on someone to remember.")],
    "trade_slug": "auto_repair_shops", "trade_plural": "auto repair shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Why Do Auto Repair Shops Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-auto-repair-shops-miss-calls",
    "h1": "Why Do Auto Repair Shops Miss So Many Calls?",
    "title": "Why Do Auto Repair Shops Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "You miss calls because the phone rings while every tech is under a car, and a driver whose car will not start does not leave a voicemail. They call the next shop.",
    "answer": "Auto repair shops miss calls because the phone rings while every tech and the owner are under a car, on a lift, or out on a test drive, and nobody is free to grab the counter. A driver whose car will not start or whose check engine light just came on does not leave a voicemail. They call the next shop.",
    "sections": [
        {"h2_html": "The call comes exactly when your <em>hands are full</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Auto repair is a hands-full trade. When the phone rings you are often under a car, on a lift, out on a test drive chasing a noise, or elbow deep in a job you cannot walk away from, and neither can the one or two other people in the shop. The busier the bay is, the more calls slip past, which means your best days are also the ones where the most work goes unheard. It is not a discipline problem. A tech cannot turn a wrench and answer the counter phone at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but it is not one. A driver stranded in a parking lot with a car that will not start is not going to leave a message and wait for a callback. They move down the search results until someone picks up, and by the time you wipe your hands and check the phone, the car is already booked somewhere else.</p>'},
        {"h2_html": "The calls you miss are your <em>first-time customers</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. Some are current customers checking on a car already in the bay, but many are first-time drivers searching for a shop right now, the check engine light, the strange noise, the car that would not start this morning. That first-timer who trusts you with a diagnostic today comes back for brakes, for the state inspection, for the timing belt, and sends family and coworkers your way. So a single missed call is not one lost ticket, it is years of steady work handed to whichever shop happened to be standing by the phone.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that answers on the first ring and can do proper intake, not a voicemail box and not a script reader that does not know a tow from an oil change. What actually works is something that picks up while your hands are full, asks whether the car is drivable or needs a tow, gathers the year, make, model, and the complaint, and either books the drop-off on your schedule or flags it straight to your phone. It captures the job. It leaves the diagnosis and the price to you.</p>'}],
    "bridge_h2": "Stop sending first-time drivers to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring while your hands are full, sorts a tow from a routine drop-off, and books it or flags it to you, so a first-time customer never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-auto-repair-shops",
    "bridge_label": "AI receptionist for auto repair shops",
    "faqs": [
        ("Would a customer rather reach a real person?",
         "What a driver needs most is to know a real shop can look at their car, and a calm voice that catches the details and books the drop-off beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, and hands anything that needs your judgment straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are under a car, on a test drive, or already on another call. Something that always answers and does the intake is what catches the calls a forward would still miss.")],
    "trade_slug": "auto_repair_shops", "trade_plural": "auto repair shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Why Don't Auto Repair Customers Come Back? (problem -> crm) ============
{
    "slug": "why-auto-repair-customers-dont-come-back",
    "h1": "Why Don't Auto Repair Customers Come Back?",
    "title": "Why Don't Auto Repair Customers Come Back? | Top Shelf Business Solutions",
    "meta_desc": "Most auto repair customers do not come back because nobody reminded them. The car will not remind them until something breaks, and by then they have drifted to another shop.",
    "answer": "Most auto repair customers do not come back because nobody stayed in touch, not because they were unhappy. The car will not remind them they are due for an oil change or a state inspection until something breaks, and by then they drift to whatever shop is closest that day. A reminder is usually all it takes.",
    "sections": [
        {"h2_html": "Silence is a forgotten reminder, not <em>disloyalty</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A driver who does not come back usually did not decide against you. They meant to return, the days got away from them, and the car said nothing until a warning light or a squeal on the highway forced the issue. By then they are not thinking about the shop that changed their oil a year ago, they are searching again in a hurry, and the trust you earned goes to whoever shows up first in the results. It is the same story with a deferred repair: the brakes you flagged on the inspection that the driver put off until payday, and payday came and went with no nudge from anyone.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of that is a loyalty problem. It is that the one thing standing between you and the repeat visit, a short reminder at the right time, is exactly the thing nobody at a busy shop has time to send by hand.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Shops do not skip follow-up because they do not care. They skip it because the bay fills up. You finish one car, roll to the next, handle the tow that jumped the line, and by closing time the estimate you wrote on Tuesday and the customer who is overdue for an inspection are both out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest customers to bring back.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system tracking which estimates are still open and going cold, or which customers are overdue for service.</li><li>The follow-up depends on someone remembering, so it competes with the work in front of you and loses.</li><li>By the time anyone circles back, the car has already been serviced somewhere else.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and you fix it once. When every past customer gets a service reminder on schedule, an oil change by mileage or months, the state inspection before it lapses, the interval work when it is due, and every open estimate gets a timed check-in written to sound like your shop, the repeat work comes back on its own instead of drifting to the shop that stayed in touch.</p>'}],
    "bridge_h2": "Bring every car back on schedule",
    "bridge_text": "The customers you have already served are the cheapest work you can book. A CRM reminds each one when their car is due and follows up on every open estimate, so they come back to you instead of searching all over again.",
    "bridge_slug": "crm-for-auto-repair-shops",
    "bridge_label": "CRM for auto repair shops",
    "faqs": [
        ("How often should I reach out to past customers?",
         "Tie it to the vehicle, not a blast to the whole list. A reminder when a car is near the mileage or the months for its next service, and another before a state inspection lapses, lands as helpful because it is about their car. Timed that way it reads as a heads-up, not spam."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like your shop and tied to what the car actually needs. Most drivers appreciate the reminder because they simply forgot they were due, and a short, well-timed note reads as attentive. You can always jump in and message anyone directly.")],
    "trade_slug": "auto_repair_shops", "trade_plural": "auto repair shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ======== How Do Auto Repair Shops Get More Customers? (how-to -> marketing) ========
{
    "slug": "how-do-auto-repair-shops-get-more-customers",
    "h1": "How Do Auto Repair Shops Get More Customers?",
    "title": "How Do Auto Repair Shops Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Auto repair shops get more customers by showing up in Google's map pack with honest reviews when a driver searches nearby, then bringing past customers back for service.",
    "answer": "Auto repair shops get more customers by being easy to find and easy to trust when a driver searches nearby, then keeping the customers they already have. That means a Google Business Profile in the map pack, a steady flow of honest reviews, and reminders that bring past customers back for service instead of letting them drift.",
    "sections": [
        {"h2_html": "New customers start on the map, and <em>trust decides the call</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a driver searches for auto repair near me or a mechanic near them, the first thing Google shows is not a website. It is the map pack, the little map with three local listings, star ratings, and a call button, and most people pick from those three without scrolling further. Getting into them runs on your Google Business Profile, whether it is verified, complete, and active, and on how many recent, genuine reviews you have.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Auto repair also carries a trust problem that few trades feel as sharply. A driver is handing over an expensive machine and their wallet to someone they cannot watch work, half-worried they will be told they need repairs they do not. Reviews are how a stranger decides you are the honest shop before they ever call. A profile with a steady wall of real, recent reviews, and a shop that replies to them, is what turns a search into a call to you instead of the shop one block over.</p>'},
        {"h2_html": "The customers you already have are the <em>other half</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Chasing new drivers while your past customers quietly drift away is the most expensive way to grow a shop. The car you serviced last year is the cheapest next job you can get, but only if you are the shop that reminds them when they are due. Growth is really two levers pulled at once, getting found by new drivers and holding on to the ones you have earned.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep the Google profile verified, complete, and posting, so you show up when someone nearby searches.</li><li>Ask every happy customer for an honest review right after the job, and reply to every review, good or bad.</li><li>Bring past customers back with reminders tied to the car, the mileage service, the state inspection, the repair they deferred.</li><li>Make sure the calls and searches you already earn actually get answered and followed up, so you are not paying to bring in drivers you then send to voicemail.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">No honest company can promise you a specific spot on the map, because Google decides that, but keeping the profile active, the reviews genuine, and the follow-up running are the levers that actually move it. A free audit can show you where your shop stands today before you spend a dollar.</p>'}],
    "bridge_h2": "Get found by the drivers searching now",
    "bridge_text": "Most new customers start with a search and decide on your reviews. Keeping your Google profile active and your reviews honest and recent is how you show up and earn the call when a driver needs a shop nearby.",
    "bridge_slug": "marketing-for-auto-repair-shops",
    "bridge_label": "Marketing for auto repair shops",
    "faqs": [
        ("What is the fastest way to get more auto repair customers?",
         "Usually the map pack and your reviews, because that is where a driver searching right now is choosing a shop. A profile that gets verified, completed, and active, with a steady flow of honest reviews, can start climbing within a few weeks. Pair that with service reminders to past customers for a steadier flow than either one alone."),
        ("Do reviews really matter that much for a repair shop?",
         "They matter more here than almost anywhere, because a driver is trusting you with an expensive thing they cannot inspect themselves and cannot easily judge the work on. A stack of recent, genuine reviews, and your replies to them, is how a stranger decides you are honest before they hand over the keys.")],
    "trade_slug": "auto_repair_shops", "trade_plural": "auto repair shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
]
