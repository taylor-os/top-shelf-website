"""Colony page specs for APPLIANCE REPAIR (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question an appliance-repair-business owner would search, answered directly up
top (the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, appliance-repair-specific substance (the generator owns
shell, schema, events, keyword placement), never the plumber or HVAC colony reworded. Appliance
repair is its own animal: a dead fridge with food spoiling, a washer that quit mid-cycle, a dryer,
oven, or dishwasher is an urgent same-day "can you come today" call, and the homeowner books
whoever answers and can give them a slot, not necessarily the best shop. The realities that make
it unlike the other trades are brand and model plus part availability, the diagnostic or trip-fee
conversation, in-warranty vs out-of-warranty and manufacturer-warranty work, and honest
repair-vs-replace advice. Demand is steady all year, not seasonal. The repeat-work engine is
reactivating past customers as their OTHER aging appliances fail, since every home has several.

Same honesty rules as the money specs: no invented stats, prices, or clients; hedge instead of
overpromise; only the real prices ($299/$899/$2,500 plans, $1,500 one-time site) ever appear, and
no invented repair or diagnostic prices; no em/en dashes anywhere; "find the gap", never "leak" as
a money metaphor (a literal washer or dishwasher water leak is the only allowed use). Ethics: the
AI receptionist does scheduling and intake only; it never diagnoses the appliance or quotes the
repair, that is the tech's job on the visit.

Six questions, mixed cost / problem / how-to, spread across the four appliance money pages:
  1 appliance-repair-website-cost                     (cost)    -> websites-seo-for-appliance-repair
  2 appliance-repair-answering-service-cost           (cost)    -> ai-receptionist-for-appliance-repair
  3 is-a-crm-worth-it-for-appliance-repair            (cost)    -> crm-for-appliance-repair
  4 why-appliance-repair-companies-miss-calls         (problem) -> ai-receptionist-for-appliance-repair
  5 why-appliance-repair-customers-dont-return        (problem) -> crm-for-appliance-repair
  6 how-do-appliance-repair-companies-get-more-customers (how-to) -> marketing-for-appliance-repair
"""

TOPICS = [
# ============ How Much Does an Appliance Repair Website Cost? (cost -> websites-seo) ============
{
    "slug": "appliance-repair-website-cost",
    "h1": "How Much Does an Appliance Repair Website Cost?",
    "title": "How Much Does an Appliance Repair Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "An appliance repair website ranges from cheap templates to a custom build. What matters is whether it ranks and books the same-day call. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "An appliance repair website can run from a couple hundred dollars for a DIY template to several thousand for a custom build, but the price matters far less than whether it ranks for the repairs people search and books the same-day call before they bounce. Top Shelf builds a custom five page site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What an appliance repair site actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before you compare quotes, it helps to know what you are paying for, because for appliance repair the job of the site is specific. Someone whose refrigerator died an hour ago is on a phone, not a desktop, searching for exactly what broke, and they call the company that is easiest to reach and can come today. A site earns its money by being that company. That means it has to show up and then get out of the way of a homeowner in a hurry.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Ranks for the searches people actually type when an appliance quits, refrigerator repair, washer repair, dryer not heating, appliance repair near me, and the brand-and-city searches a national directory has no reason to answer well.</li><li>Names the brands you are equipped to service, because whether you fix their brand is one of the first things a worried homeowner checks.</li><li>Loads fast and puts a tap-to-call button and your same-day availability in front of them before they scroll, so a warm-fridge call reaches you in one tap.</li><li>Makes requesting a visit simple and captures the brand, model, and symptom, so the first trip is set up to be the fix.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A good-looking site that never ranks and buries your number is the most expensive kind, because you paid for it and it brings you nothing.</p>'},
        {"h2_html": "What actually drives the price, and what you should <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number swings so widely because you are not all buying the same thing. A DIY builder you fill in yourself is cheap monthly, but you do the work and it is rarely built to rank or to convert a homeowner in a hurry. A one-time custom build is yours to keep, but a site alone does little if nobody is doing the ongoing SEO that gets it found for those appliance-and-city searches. An agency that bundles the build with ongoing SEO carries more monthly cost, and also more of the long-term value. Before you sign anything, ask who owns the site, what a change costs, and whether you keep it if you leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that books the same-day call",
    "bridge_text": "An appliance repair website is only worth what it books. Ours is built to rank for the repairs people search in the towns you cover, name the brands you fix, and turn a warm-fridge search into a call on your phone.",
    "bridge_slug": "websites-seo-for-appliance-repair",
    "bridge_label": "Websites & SEO for appliance repair",
    "faqs": [
        ("Should my appliance repair website list the brands I service?",
         "Yes. It is one of the first things a homeowner checks before they call, and it helps you rank for brand-and-appliance searches at the same time. Naming the brands you are equipped to repair reassures the visitor they are in the right place and captures searches a generic directory never targets."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep. On a monthly plan the site is built for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "appliance_repair", "trade_plural": "appliance repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ====== What Does an Appliance Repair Answering Service Cost? (cost -> ai-receptionist) ======
{
    "slug": "appliance-repair-answering-service-cost",
    "h1": "What Does an Appliance Repair Answering Service Cost?",
    "title": "What Does an Appliance Repair Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for appliance repair often bill per call or minute, which climbs when you are busiest. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for appliance repair usually bill per call, per minute, or a monthly retainer, so a busy stretch gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call, captures the brand and model, and books the same-day visit comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good stretch turns into a big bill. Appliance repair gets its heaviest call volume in bursts, the packed Monday morning after a weekend of breakdowns, the run of failures when a heat wave takes out fridges across town, and those are exactly the times a per-use meter runs up the cost. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of tire-kickers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty caller or a slow operator costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner staring at a fridge full of spoiling food does not leave a voicemail, they call the next company that can come today. The real cost of no coverage is not a monthly fee, it is the same-day repair that went to whoever picked up. But a generic call center reading a script does not know a front-loader from a top-loader, and cannot capture the brand and model that tells your tech what part to load on the truck, so you can pay for coverage and still get bad intake.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, gets the brand, model, and symptom, explains your diagnostic or trip fee up front, asks whether the appliance is still under warranty, and books the visit onto your calendar. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One same-day repair you would have lost while your hands were in a machine can be worth well more than the plan costs, and everything it catches after that is on top. It handles scheduling and intake only, it does not diagnose the appliance or quote the repair, that stays with your tech on the visit.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, captures the brand and model so the first trip is the fix, and books it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-appliance-repair",
    "bridge_label": "AI receptionist for appliance repair",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when the breakdowns cluster and you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the same-day repair it books instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or holidays?",
         "No. It answers 24/7 as part of the plan, including the Sunday dishwasher that leaked across a kitchen floor and the holiday oven that quit before a dinner, with no after-hours surcharge or overage.")],
    "trade_slug": "appliance_repair", "trade_plural": "appliance repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ========= Is a CRM Worth It for an Appliance Repair Company? (cost -> crm) =========
{
    "slug": "is-a-crm-worth-it-for-appliance-repair",
    "h1": "Is a CRM Worth It for an Appliance Repair Company?",
    "title": "Is a CRM Worth It for an Appliance Repair Company? | Top Shelf Business Solutions",
    "meta_desc": "For most appliance repair companies a CRM pays for itself by rebooking one parts-on-order job and reviving past customers as their other appliances age. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most appliance repair companies, yes. A CRM pays for itself the first time it rebooks a parts-on-order job you would have let stall, or brings a past customer back when their next appliance fails. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for an appliance repair company when you have more open estimates, parts-on-order jobs, and past customers than you can personally keep track of, which is most established shops. It is not worth it if you are a one-person operation doing a handful of repairs a week and genuinely calling everyone back, though that rarely stays true as you grow. The honest test is simple: how many repair estimates have you handed out in the last month that you never followed up on, how many parts came in and sat on the truck while the customer went quiet, and how many homes you have been inside have not heard from you in a year? Those are the jobs a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for appliance repair is not the software, it is the work that stops slipping through. A homeowner sitting on a repair-or-replace quote, a control board that arrived and is still in the box, a family whose dryer you fixed two years ago whose fridge is now getting old: each one is a job you have already half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open estimate on a schedule, and prompts a rebooking text the moment a part you ordered is marked in, so the job does not stall waiting on you to remember.</li><li>It reaches past customers before their next appliance sends them searching, because every home you have visited has several more machines quietly aging.</li><li>It keeps every customer, address, appliance, and repair in one place instead of a stack of invoices and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one job you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your service list to work",
    "bridge_text": "The estimates and past customers you already have are the cheapest jobs you can get. A CRM chases every open quote, rebooks every parts-on-order job, and brings homes back as their other appliances age.",
    "bridge_slug": "crm-for-appliance-repair",
    "bridge_label": "CRM for appliance repair",
    "faqs": [
        ("Is a CRM overkill for a small appliance repair business?",
         "Not usually. Even a one-truck shop hands out more estimates and services more homes than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If quotes go cold, parts sit on the truck, and past customers forget your name, a CRM earns its keep."),
        ("How is a CRM different from keeping numbers in my phone?",
         "A phone full of contacts does not follow up on an estimate, does not remember which home has a part on order, and does not tell you which customer is due for a check-in. A CRM does all of that on a schedule, so the repeat work and the quotes you already gave actually turn into booked repairs.")],
    "trade_slug": "appliance_repair", "trade_plural": "appliance repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== Why Do Appliance Repair Companies Miss So Many Calls? (problem -> ai-receptionist) ========
{
    "slug": "why-appliance-repair-companies-miss-calls",
    "h1": "Why Do Appliance Repair Companies Miss So Many Calls?",
    "title": "Why Do Appliance Repair Companies Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Appliance repair companies miss calls because they ring while your hands are inside a machine, and a homeowner with a warm fridge does not leave a voicemail, they call the next company that can come today.",
    "answer": "You miss calls because they come when your hands are inside a machine, on the floor behind a fridge with the panel off or driving to the next job, and a homeowner with a warm fridge full of spoiling food does not leave a voicemail. They hang up and call the next company that can come today. The fix is not working harder, it is making sure every same-day call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Appliance repair is a hands-full trade. When the phone rings you are often on a kitchen floor with a fridge pulled out and the panel off, hands-deep in a washer, or driving between jobs, and none of those are moments you can stop and take a call. The busier you are, the more calls you miss, which means your best days are also the ones where the most work slips away. It is not a discipline problem. One person cannot have a machine apart in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a same-day breakdown it is not one. A homeowner watching a week of groceries warm up is not going to leave a message and wait. They move down the list until someone answers and can give them a slot, and by the time you check your phone, the job is already booked with whoever picked up.</p>'},
        {"h2_html": "The missed same-day call is your most <em>expensive miss</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A missed same-day call, a dead fridge, a flooded dishwasher, an oven out the day before someone hosts, is the work with the most urgency and the least patience, and it books the next company the instant you do not answer. Worse, the brand and model you would have captured on that call is what turns the job into a first-visit fix instead of a diagnose-today, order-the-part, drive-back-next-week trip, so the call you miss costs you twice.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and knows what to ask. A voicemail box cannot book a slot, and a generic call center does not know a front-loader from a top-loader or which model tells you what part to bring. What actually works is something that answers on the first ring day or night, gets the brand, model, and symptom, explains your diagnostic or trip fee, confirms the address, and books the visit or flags an urgent one to your phone, so you never miss the call in the first place. It handles the intake and the booking only, your tech still does the diagnosis and the quote on the visit.</p>'}],
    "bridge_h2": "Stop losing same-day repairs to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, captures the brand, model, and symptom, and books it or flags it to you, so the same-day repair never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-appliance-repair",
    "bridge_label": "AI receptionist for appliance repair",
    "faqs": [
        ("Would a customer rather reach a real person?",
         "When an appliance quits, what a homeowner needs most is to know a real repair company is handling it and can come today, and a steady voice that captures the brand, model, and details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, and books the visit or hands an urgent one straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are behind a fridge with the panel off, under a washer, or already on another call. Something that always answers and captures the brand and model is what catches the calls a forward would still miss.")],
    "trade_slug": "appliance_repair", "trade_plural": "appliance repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== Why Don't My Appliance Repair Customers Come Back? (problem -> crm) ========
{
    "slug": "why-appliance-repair-customers-dont-return",
    "h1": "Why Don't My Appliance Repair Customers Come Back?",
    "title": "Why Don't My Appliance Repair Customers Come Back? | Top Shelf Business Solutions",
    "meta_desc": "Most appliance repair customers do not come back because they lost your number and forgot your name, not because they were unhappy. Every home has several more appliances aging, and whoever they find gets the call.",
    "answer": "Most appliance repair customers do not come back because they lost your number and forgot your name, not because they were unhappy. Every home you have visited has several more appliances aging behind the one you fixed, and when the next one quits, whoever they find online gets the call instead of you. A light, steady touch is what keeps them yours.",
    "sections": [
        {"h2_html": "It is usually memory, not <em>loyalty</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a customer who called someone else as a customer you lost on quality, so you shrug and move on. But most of the time they did not decide against you at all. The customer whose dryer you repaired two years ago is the easiest call you will ever get when their fridge starts acting up, because you have already been in the home and they already trust your work. They just lost the magnet off the fridge and never saved your number.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So when the next appliance quits, they do what everyone does: they grab a phone and search, and they land on whoever ranks or answers first. It was never a complaint about your work. It is that nothing kept your name in front of them between the repair two years ago and the breakdown today, and every home holds a refrigerator, a washer, a dryer, an oven, and a dishwasher, all at different ages, all going to fail eventually.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Appliance repair owners do not skip staying in touch because they are lazy. They skip it because the day fills up. You finish a repair, roll to the next, handle the same-day call that jumped the line, and by evening the home you were in this morning is out of sight, let alone the one from two years ago. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest customers to reach.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system tracking which past customers you have not touched in a year, or which homes have other appliances getting old.</li><li>The follow-up depends on you remembering, so it competes with the actual work and loses.</li><li>By the time their next appliance quits, they have already found and booked someone else.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. A light, steady touch written to sound like you, a seasonal tip, a check that the last repair is still holding, a reminder that you service every major brand in the house, keeps your name in their phone so the next breakdown and the referral to a neighbor come to you.</p>'}],
    "bridge_h2": "Keep the homes you have already earned",
    "bridge_text": "A CRM remembers every home you have been in and the appliances still aging there, and reaches out on a schedule for you, so the next breakdown comes back to you instead of whoever they find online.",
    "bridge_slug": "crm-for-appliance-repair",
    "bridge_label": "CRM for appliance repair",
    "faqs": [
        ("How often should I follow up with a past appliance repair customer?",
         "A light touch a couple of times a year is plenty, not a hard sell. A seasonal tip, a quick check that the last repair is holding, or a reminder of the brands you service keeps your name in their phone without being pushy, so you are the one they think of when the next appliance quits. A CRM handles the timing for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly seasonal check-in reads as attentive, not spammy, and most homeowners appreciate the reminder because they meant to save your number and never did. You can always jump in and message anyone directly.")],
    "trade_slug": "appliance_repair", "trade_plural": "appliance repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==== How Do Appliance Repair Companies Get More Customers? (how-to -> marketing) ====
{
    "slug": "how-do-appliance-repair-companies-get-more-customers",
    "h1": "How Do Appliance Repair Companies Get More Customers?",
    "title": "How Do Appliance Repair Companies Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Appliance repair companies get more customers by being the visible, well-reviewed name in the map pack the moment an appliance quits nearby, and by staying in front of past customers as their other appliances age.",
    "answer": "The steadiest way is to be the visible, well-reviewed name in your service area the moment an appliance quits, because the demand is local and immediate. Show up first in the map pack when someone nearby searches, name the brands you fix, and keep a steady flow of reviews. Then work the customers you already have, whose other appliances are always aging.",
    "sections": [
        {"h2_html": "Get found in the <em>moment it breaks</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody shops around for weeks when their fridge dies. The demand appears the instant an appliance quits, and it is intensely local, because a homeowner wants someone at their door today, not a company an hour across the metro. Unlike a trade that spikes twice a year with the weather, appliance repair breaks steadily all year long, so the whole game is being visible and trusted in your service area the moment it happens to be someone\'s turn.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">When someone searches for appliance repair near them, the first thing they see is the map pack, those three local listings with the star ratings, above the websites and the ads. A profile that has sat untouched for months looks abandoned next to one with recent photos of real repairs, current hours, and a steady stream of reviews. For appliance repair, the profile has to answer two questions fast: do they fix my brand, and can they come today. Get found first in that moment and the job is usually yours.</p>'},
        {"h2_html": "Then work the customers you <em>already have</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting found is only half of it. The other half is free, and most shops leave it on the table. Every happy customer is a review you did not ask for and a home full of other appliances that will fail in time, and a steady, simple habit around both is what compounds into a full schedule.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Ask every happy customer for a review the moment the repair is done and the appliance is running again, because a steady flow of recent reviews is one of the strongest levers on your map-pack ranking.</li><li>Keep the profile active and focused on the specific towns you actually cover, not a whole metro, so the calls you get are jobs your tech can reach the same day.</li><li>Stay top of mind with a light local presence and honest, useful posts, so the referral and the next breakdown come to you instead of whoever they saw most recently.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is the public-facing side, your Google profile, reviews, and local visibility. The private follow-up to people already in your database, the estimates and past customers, is the CRM. No honest company can promise a specific spot on the map, because Google decides that, but showing up steadily is what moves it.</p>'}],
    "bridge_h2": "Be the repair company they can already see",
    "bridge_text": "Most appliance repair calls begin in the map pack. Keeping your Google profile active, focused on the towns you cover, and full of recent reviews is how you show up first when an appliance quits nearby.",
    "bridge_slug": "marketing-for-appliance-repair",
    "bridge_label": "Marketing for appliance repair",
    "faqs": [
        ("What is the fastest way for an appliance repair company to get more calls?",
         "Get into the map pack. A verified, complete, active Google Business Profile that lists the brands you service and makes your same-day availability obvious, backed by a steady flow of recent reviews and focused on the towns you cover, is what a homeowner sees and calls the moment their appliance quits. It sits above the websites and the ads."),
        ("Does marketing even work for appliance repair if demand is already steady?",
         "Steady demand is exactly why it pays. Appliances break every day of the year, not in two big seasons, so the shop that shows up first in the map pack every single day catches a stream of work the invisible shop never even hears about. Nobody controls Google, so no honest company promises a specific ranking, but consistency is what moves it.")],
    "trade_slug": "appliance_repair", "trade_plural": "appliance repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
