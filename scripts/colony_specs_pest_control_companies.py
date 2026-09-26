"""Colony page specs for PEST CONTROL COMPANIES (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a pest control owner would search, answered directly up top (the 40-60
word AEO answer), then two body sections, then a "the fix" bridge that funnels the page's
authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, pest-control-specific substance (the generator owns
shell, schema, events, keyword placement). Same honesty rules as the money specs: no invented
stats, prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500
plans, $1,500 one-time site) ever appear; no em/en dashes anywhere; "find the gap", never "leak"
as a money metaphor.

Grounded in the real "People Also Ask" themes for pest control (what CRM/software, how to get
more leads/clients, DIY vs a real website, answering-service cost), turned into nine trade-specific
question pages, mixed how-to / cost / problem, spread across all seven money pages:
  1 how-pest-control-companies-get-leads         (how-to)  -> marketing-for-pest-control-companies
  2 what-crm-pest-control-use                    (how-to)  -> crm-for-pest-control-companies
  3 pest-control-website-cost                    (cost)    -> websites-seo-for-pest-control-companies
  4 answering-service-for-pest-control-cost       (cost)    -> ai-receptionist-for-pest-control-companies
  5 get-more-pest-control-reviews                (how-to)  -> review-software-for-pest-control-companies
  6 keep-pest-control-customers-on-plan          (problem) -> automation-for-pest-control-companies
  7 stop-missing-pest-control-calls              (problem) -> ai-receptionist-for-pest-control-companies
  8 should-pest-control-offer-online-booking     (how-to)  -> online-booking-for-pest-control-companies
  9 turn-pest-treatments-into-recurring-revenue  (how-to)  -> crm-for-pest-control-companies
"""

TOPICS = [
# ============ How Do Pest Control Companies Get More Leads? (how-to -> marketing) ============
{
    "slug": "how-pest-control-companies-get-leads",
    "h1": "How Do Pest Control Companies Get More Leads?",
    "title": "How Do Pest Control Companies Get More Leads? | Top Shelf Business Solutions",
    "meta_desc": "Pest control companies get more leads from the local map pack, steady Google reviews, and neighbor referrals, then win the recurring plans that are worth far more than one spray.",
    "answer": "Pest control leads come from being the first name a frightened homeowner sees when they search, which means the local map pack, and from the customers you already have. The map pack and steady reviews win the panic call, while recurring plan members and neighbor referrals turn one job into many, so your best leads cost the least.",
    "sections": [
        {"h2_html": "Where pest control leads <em>actually come from</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most new pest control leads start the same way. Someone spots a trail of ants, hears something in the attic after dark, or wakes up to bites, grabs their phone, and searches. What they see first is the local map pack, the three listings with star ratings sitting above everything else, and most people call one of those three without ever scrolling down. So the biggest lever on new leads is not a clever ad, it is simply being one of the names that shows up in that moment, in the towns your trucks already cover.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting there runs on your Google Business Profile more than your website: whether it is verified and complete, how close you are to the searcher, and how many recent, genuine reviews you have. A profile left stale reads like a company that might not even pick up, and the frightened caller quietly moves to the one that looks active. Paid local ads can add to that, but the free map listing is where the cheapest, highest-intent calls come from.</p>'},
        {"h2_html": "The best leads are worth <em>years, not one spray</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every lead is worth the same. A one-time wasp spray is a single payment, while a homeowner who signs a recurring protection plan is quarterly revenue that can run for years, plus the odd extra treatment and a termite renewal on top. That changes where your effort should go. Chasing the cheapest one-off call is a treadmill, and marketing aimed at plan members buys an account that keeps paying long after the work is done.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Go after recurring plans, not just one-time sprays, because a plan member is worth far more over time and tends to refer the neighbors.</li><li>Use the fact that pests do not respect property lines: treat one house and the whole street often has the same trouble and has just watched your truck park next door, so a yard sign, a neighborly word, and a simple referral offer can cluster jobs onto one route.</li><li>Keep your Google profile full of recent reviews and job photos, since that is what turns a nearby search into a call.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this is a big ad budget. It is being visible where the panic search lands, and being the company the neighbors already trust, which is the kind of steady local marketing that compounds instead of stopping the day you turn an ad off.</p>'}],
    "bridge_h2": "Get found where the panic search lands",
    "bridge_text": "Most pest control leads begin in the local map pack and among the neighbors who see your truck. Keeping your Google profile active and full of recent reviews is how your name is the one a frightened homeowner calls.",
    "bridge_slug": "marketing-for-pest-control-companies",
    "bridge_label": "Marketing for pest control companies",
    "faqs": [
        ("What is the cheapest way to get more pest control leads?",
         "Your Google Business Profile, and it is free. Most local searches for an exterminator get decided in the map pack, so a verified, complete profile with recent reviews and photos brings in high-intent calls with no per-lead cost. It is usually a better first move than buying ads."),
        ("Are one-time jobs or recurring plans the better lead to chase?",
         "Recurring plans, in almost every case. A one-time spray pays once, while a plan member renews for years and often refers the neighbors who watched your truck work next door, so a lead that turns into a plan is worth far more than a cheaper call that never comes back.")],
    "trade_slug": "pest-control-companies", "trade_plural": "pest control companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ================ What CRM Do Pest Control Companies Use? (how-to -> crm) ================
{
    "slug": "what-crm-pest-control-use",
    "h1": "What CRM Do Pest Control Companies Use?",
    "title": "What CRM Do Pest Control Companies Use? | Top Shelf Business Solutions",
    "meta_desc": "Pest control companies use a CRM built for recurring service, one that tracks every plan, rebooks the next visit, keeps termite warranty dates, and follows up on one-time jobs.",
    "answer": "Most pest control companies use a CRM or field service platform built for recurring service, one that tracks every plan and its cadence, rebooks the next visit, keeps termite warranty dates, and follows up on one-time jobs. The right fit for you is less about the brand name and more about whether it actually works your customer list.",
    "sections": [
        {"h2_html": "What a pest control company actually needs from a <em>CRM</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Pest control companies tend to use a CRM or field service platform built for recurring service rather than a generic contact list, because the work has a shape a plain address book cannot handle. The business runs on plans that renew on a cadence, routes that have to stay dense, termite warranties with renewal dates, and follow-ups that turn a one-time job into an account. The brand name on the software matters less than whether it actually does those jobs.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Tracks every recurring plan and its cadence, quarterly, bi-monthly, or monthly, and rebooks the next visit so a plan does not quietly lapse.</li><li>Keeps full service history and notes for every customer and address, so any tech knows what was treated and when.</li><li>Holds termite warranty and bond renewal dates, so a renewal does not slip past its deadline.</li><li>Follows up automatically on one-time jobs and open quotes, so more of them convert and fewer go cold.</li><li>Schedules with an eye on route density, so a new stop lands near where you are already working.</li></ul>'},
        {"h2_html": "The list you already have is the <em>point</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason a CRM is worth it in pest control is not the software itself, it is the revenue that stops slipping through. Every customer you have ever treated has a service history that says when they are due again, every one-time job is a protection plan waiting to be offered, and every termite warranty is a renewal with a date on it. Left in a truck full of paper tickets and your memory, all of that quietly goes cold. In one place, working for you, it becomes recurring revenue.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Whatever platform you choose, the honest test is simple: does it make the customer list you already have actually work, or is it just a place to store names? A CRM that only records contacts is a filing cabinet. One that rebooks plans, chases renewals, and follows up on one-timers is the thing that grows the business, and it should be yours to export, not locked inside software you rent.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM comes in the Signature plan at $899 a month, alongside the AI receptionist that feeds it every call, so the customer list and the follow-up that works it live in one system you own.</p>'}],
    "bridge_h2": "Put your customer list to work",
    "bridge_text": "The plans, past jobs, and warranties you already have are the cheapest revenue in pest control. A CRM built for the trade tracks every one and follows up for you, so nothing you earned goes cold.",
    "bridge_slug": "crm-for-pest-control-companies",
    "bridge_label": "CRM for pest control companies",
    "faqs": [
        ("What should a pest control CRM be able to do?",
         "At a minimum it should track recurring plans and their cadence, rebook the next visit, keep service history and termite warranty dates, and follow up on one-time jobs and quotes. If it only stores contacts and does not act on them, it is a filing cabinet, not a CRM that grows the business."),
        ("Do I need a pest-control-specific CRM or will a general one work?",
         "A general CRM can hold contacts, but recurring plans, route-aware scheduling, and warranty renewals are where pest control lives, and a tool built for recurring service handles them without a workaround. What matters most is that it actually rebooks plans and chases renewals, not what industry label it wears.")],
    "trade_slug": "pest-control-companies", "trade_plural": "pest control companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ How Much Should a Pest Control Website Cost? (cost -> websites-seo) ============
{
    "slug": "pest-control-website-cost",
    "h1": "How Much Should a Pest Control Website Cost?",
    "title": "How Much Should a Pest Control Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A pest control website needs a page for every pest and town it serves, so a bed bug or termite search finds you. Top Shelf includes one on any plan from $299, or $1,500 standalone.",
    "answer": "A pest control website earns its keep if it ranks for what a scared homeowner types, bed bugs, termites, a wasp nest, in their town, and turns that search into a booking. It can cost a few hundred for a template or several thousand custom. Top Shelf includes one on any plan from $299, or builds it standalone for $1,500.",
    "sections": [
        {"h2_html": "Built <em>pest by pest, town by town</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The searches that turn into pest control jobs are rarely generic. Almost nobody wins the bare word exterminator, and you do not need to. The jobs come from specific, anxious searches such as bed bug treatment, termite inspection, wasp nest removal, roach control, or mosquito service, each one tied to a particular town or neighborhood. So a pest control website does its best work as a set of focused pages, one for every pest you treat crossed with every area your trucks run, rather than a single home page trying to cover all of it at once.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A dedicated page for each pest you handle, from bed bugs and termites to rodents, roaches, and mosquitoes, written for the person who has that exact problem today.</li><li>A page for each town or neighborhood you serve, so you turn up in the local results where the searcher actually is.</li><li>A phone number and a booking button high on the page, because someone who just found a nest wants to reach a human now, not scroll through your story.</li><li>An obvious way to start a recurring protection plan, so a first-time visitor can become an ongoing account instead of one isolated call.</li></ul>'},
        {"h2_html": "Timed to the season, and honestly <em>priced</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Pest demand swings with the calendar, so the pages have to be live before each wave rather than scrambling once it hits. Mosquito and ant searches climb in the summer heat, rodent searches rise as the first cold nights push mice indoors, and termite swarm searches spike for a few weeks each spring. Google tends to reward a page that has been established and gathering trust for a while, so the company that published its mosquito page before June is the one sitting on top when the whole town starts searching at once.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">On price, the build itself is the cheap part; getting and keeping those pages ranked is the ongoing work, and that is where the value lives. Top Shelf folds the website into every monthly plan, which begins at $299, and handles the SEO that keeps your pest and town pages showing up. If you would rather buy it once and owe nothing after, a five page build is $1,500 flat and stays yours. Neither route carries a setup fee, and since Google answers to no one, the only honest promise is to do the work that earns rankings and show you where you stand today.</p>'}],
    "bridge_h2": "A website built to rank, pest by pest",
    "bridge_text": "The build is the easy part. Ours is designed to rank for each pest and town you serve, put your number in front of a scared homeowner, and feed every call into the follow-up that turns it into a plan.",
    "bridge_slug": "websites-seo-for-pest-control-companies",
    "bridge_label": "Websites & SEO for pest control companies",
    "faqs": [
        ("Do I really need a separate page for each pest and city?",
         "That is where a local pest control company wins. A term like termite inspection or bed bug treatment tied to your town is too specific for a national directory to serve well, so a real page about that pest in that area can rank where a broad, generic site never will."),
        ("Can a pest control website help me sell recurring plans, not just one-time jobs?",
         "Yes, when it is built for it. The page a scared homeowner lands on can lead them from the urgent fix toward a protection plan in plain terms, and every call it captures can flow into follow-up that offers the plan while the visit is still fresh.")],
    "trade_slug": "pest-control-companies", "trade_plural": "pest control companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ====== How Much Does an Answering Service for Pest Control Cost? (cost -> ai-receptionist) ======
{
    "slug": "answering-service-for-pest-control-cost",
    "h1": "How Much Does an Answering Service for Pest Control Cost?",
    "title": "How Much Does an Answering Service for Pest Control Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for pest control often bill per call or minute, which adds up fast. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Answering services for pest control usually bill per call, per minute, or a monthly retainer, so a busy season runs up the bill fast. Top Shelf takes a different route: an AI receptionist that answers every panic call 24/7 and books it comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy season turns into a big bill. Pest control also gets its most valuable calls at the worst times for a live service: nights, weekends, and the first warm week when the wasps and ants arrive all at once, when after-hours minutes tend to cost the most. It helps to know the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of price-shoppers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a rattled caller describing every detail costs more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner who just found a wasp nest by the door or a rat in the pantry does not leave a voicemail, they call the next exterminator. The real cost of no coverage is not a monthly fee, it is the panic job, and the recurring plan it could have become, that went to the company that picked up. But a generic call center reading a script cannot tell a carpenter ant from a termite or which one can wait, so you can pay for coverage and still get bad triage.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, triages the way you would, and books the job or flags a true emergency to your phone. It comes in the Signature plan at $899 a month flat, with no per-call or per-minute meter running, so the cost does not climb no matter how busy the season gets. One panic call you would have lost on a weekend, especially one that becomes a recurring account, can be worth well more than the service costs, and everything it catches after that is on top. It is upfront about what it is, and it hands the genuine emergencies straight to you.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, tells a wasp nest from a routine quarterly service, and books it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-pest-control-companies",
    "bridge_label": "AI receptionist for pest control companies",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when the season is busiest, while the AI receptionist is a flat part of the Signature plan with no meter. The bigger saving is the after-hours panic call it books instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or seasonal surges?",
         "No. It answers 24/7 as part of the Signature plan, including the Saturday wasp nest and the first cold night when the mice move in, which are often your best-paying jobs, with no after-hours surcharge or overage.")],
    "trade_slug": "pest-control-companies", "trade_plural": "pest control companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==== How Do Pest Control Companies Get More Google Reviews? (how-to -> review-software) ====
{
    "slug": "get-more-pest-control-reviews",
    "h1": "How Do Pest Control Companies Get More Google Reviews?",
    "title": "How Do Pest Control Companies Get More Google Reviews? | Top Shelf Business Solutions",
    "meta_desc": "Pest control companies get more Google reviews by asking once the pest is confirmed gone and making it one tap, so anxious homeowners see recent proof and call first.",
    "answer": "Ask every satisfied customer once the pest is confirmed gone, not right after the first spray, and make leaving a review a single tap. Most pest control companies do good work but ask too early or forget. Sending the request automatically at the moment the treatment has clearly held, with a direct link, is what steadily grows your reviews.",
    "sections": [
        {"h2_html": "The problem is timing and asking, not your <em>work</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most pest control companies have plenty of satisfied customers and not many reviews, and the gap is rarely the quality of the work. It is that asking gets forgotten, feels awkward while you are loading the sprayer, or happens at the wrong moment. Pest control has a timing twist other trades do not: the first treatment knocks down what the customer can see, but they are not truly at ease until a week or two later when nothing has come back. Ask right after the spray and you miss that feeling; ask three weeks in with no system and it never happens at all.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The second problem is friction. Even a willing customer will not hunt down your profile, log in, and figure out where to click, and every extra step loses a share of the people who meant to leave a review. If leaving one is not close to a single tap, most of the goodwill you earned never makes it online where the next nervous homeowner is looking.</p>'},
        {"h2_html": "How to actually get more, <em>consistently</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more reviews is less about a clever trick and more about doing the same simple thing after every job, which is exactly what falls apart on a busy route. A repeatable process beats good intentions.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Ask every satisfied customer, every time, not just the ones you remember, so it is never left to chance.</li><li>Ask at the right moment, once the pest is confirmed gone, when relief is highest, not right after the first spray.</li><li>Make it one tap with a direct link straight to your Google profile, by text and email.</li><li>Do not forget your recurring plan members, since someone who has stayed on quarterly service without a hitch writes the review that sells the plan itself.</li><li>Reply to every review, good or bad, discreetly on the sensitive ones, which reassures the next reader and helps your local ranking.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Doing all that by hand after each job is what slips first on a busy week. Software fixes it by sending the ask automatically at the moment you choose, so the request goes out every time without you thinking about it. One rule keeps you on the right side of Google: ask every customer honestly, and never filter out unhappy ones or pay for reviews.</p>'}],
    "bridge_h2": "Turn every cleared pest into a review",
    "bridge_text": "Review software asks every satisfied customer once the pest is confirmed gone and makes it one tap, so the reviews build on their own and the next anxious homeowner calls you first.",
    "bridge_slug": "review-software-for-pest-control-companies",
    "bridge_label": "Review software for pest control companies",
    "faqs": [
        ("Some of my treatments need a follow-up. When should I ask for the review?",
         "Wait for the moment the customer actually feels the result, which is usually the follow-up visit or the point where the pest is confirmed gone rather than right after the first spray. That timing is when they write the strongest review, and software can hold the ask until then automatically."),
        ("Is asking customers for reviews against Google policy?",
         "Asking every customer for an honest review is allowed and encouraged. What is not allowed is filtering out unhappy customers, offering incentives, or paying for reviews. Asking everyone at the right moment and making it easy is squarely within the rules.")],
    "trade_slug": "pest-control-companies", "trade_plural": "pest control companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==== How Do I Keep Pest Control Customers on a Recurring Plan? (problem -> automation) ====
{
    "slug": "keep-pest-control-customers-on-plan",
    "h1": "How Do I Keep Pest Control Customers on a Recurring Plan?",
    "title": "How Do I Keep Pest Control Customers on a Recurring Plan? | Top Shelf Business Solutions",
    "meta_desc": "Keep pest control customers on a recurring plan by rebooking the next visit automatically and catching members before they drift, so plans keep billing year after year.",
    "answer": "You keep customers on a recurring plan by making sure the next visit actually gets rebooked and by catching members before they drift. Most plans lapse not because the customer was unhappy but because nobody scheduled the next service. Automatic rebooking notices, renewal reminders, and steady on-time visits are what keep the plan billing year after year.",
    "sections": [
        {"h2_html": "Most plans lapse because nobody <em>rebooked the next visit</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A recurring plan only pays off if it stays active, and most that lapse do not leave because they were unhappy. They drift. The last visit happened, nobody scheduled the next one, a few months pass, and the customer forgets they were ever on a plan until ants come through the kitchen and they search for someone new. With hundreds of accounts and techs on full routes, remembering to rebook every member is exactly the task that slips in a busy office.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So retention in pest control is less about winning people back and more about never letting the next visit fall off in the first place. A plan that gets rebooked on schedule, every cadence, keeps billing and keeps the customer calling you first. The revenue you already earned walks out the door one forgotten visit at a time, quietly, unless something is making sure that visit gets booked.</p>'},
        {"h2_html": "What actually keeps members on the <em>plan</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Keeping members is mostly a handful of things happening reliably, which is where automation earns its place, because it does them every time without anyone in the office working a list.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A rebooking notice goes out on schedule as each member comes due, with a link to confirm or pick a time, so the next quarterly or monthly visit fills back in on its own.</li><li>A renewal reminder fires before a termite warranty or annual bond expires, so it does not quietly drop.</li><li>Confirmations, prep reminders, and an on-my-way text make each visit actually happen and feel worth paying for.</li><li>An account going quiet gets a nudge before it lapses, so you reach a drifting member while they are still yours.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Done by hand, these are the first things to slip on a full week. Automated, they run in the background and the plan proves its worth by actually getting used. A member who never has to remember their next service, and always knows when you are coming, is a member who renews without thinking about it.</p>'}],
    "bridge_h2": "Keep every plan visit on the calendar",
    "bridge_text": "Automation sends the rebooking notice, the renewal reminder, and the on-my-way text for you, so recurring visits fill back in on schedule and members stop drifting toward churn.",
    "bridge_slug": "automation-for-pest-control-companies",
    "bridge_label": "Automation for pest control companies",
    "faqs": [
        ("Why do pest control customers cancel their recurring plans?",
         "More often they do not actively cancel, they drift, because the next visit never got rebooked and they slowly forget they were on a plan. Unhappiness is a smaller cause than simple neglect, which is why keeping every visit scheduled on time is the biggest lever on retention."),
        ("Can rebooking recurring visits really be automated?",
         "Yes. The system tracks each plan and its cadence and sends the member a rebooking notice when the next service is due, with a link to confirm or pick a time, so the visits fill back in without the office chasing a list. You can always step in and talk to anyone directly.")],
    "trade_slug": "pest-control-companies", "trade_plural": "pest control companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==== How Do I Stop Missing Pest Control Calls (the Panic Call)? (problem -> ai-receptionist) ====
{
    "slug": "stop-missing-pest-control-calls",
    "h1": "How Do I Stop Missing Pest Control Calls (the Panic Call)?",
    "title": "How Do I Stop Missing Pest Control Calls (the Panic Call)? | Top Shelf Business Solutions",
    "meta_desc": "You miss pest control panic calls because they ring while techs are on route, and a homeowner with a wasp nest will not leave a voicemail. They call the next exterminator.",
    "answer": "You miss panic calls because they ring while your techs are mid-treatment, under a sink, or driving between stops, and a homeowner who just found a wasp nest or bed bugs will not leave a voicemail. They call the next exterminator. The fix is not answering faster yourself, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The panic call comes exactly when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Pest control is a hands-full trade. When the phone rings your tech is often mid-treatment under a sink, up in an attic with no signal, or driving between stops, and none of those are moments to stop and take a call. The busier the season, the more calls slip, which means your best weeks are also the ones where the most work gets missed. It is not a discipline problem. One person cannot treat the house in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a panic call it is not one. A homeowner who just found a wasp nest by a swing set where the kids play, or bed bugs in the mattress, is anxious and wants it gone today. They are not going to leave a message and wait, they move down the list until someone answers, and by the time you check your phone the job is already gone.</p>'},
        {"h2_html": "Missed panic calls are your most <em>expensive misses</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A missed panic call, a wasp nest, a rat in the kitchen, a fresh bed bug find, is often the highest-value work you can get, because it is urgent, it is same-day, and it frequently turns into a recurring protection plan on top of the one job. Those calls also tend to come after hours and on weekends, exactly when they are most likely to roll to voicemail. So the calls you are most likely to miss are also the ones worth the most.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can tell a real emergency from a call that can wait. A voicemail box cannot triage, and a generic call center does not know a carpenter ant from a termite. What actually works is something that answers on the first ring day or night, stays calm with a rattled caller, finds out whether it is stinging insects, rodents, or bed bugs, gets the address, and either books the stop or flags a true emergency straight to your phone, so you never miss the call in the first place.</p>'}],
    "bridge_h2": "Stop losing panic calls to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, tells a wasp nest from a routine service, and books it or flags it to you, so the panic call never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-pest-control-companies",
    "bridge_label": "AI receptionist for pest control companies",
    "faqs": [
        ("Would an anxious customer rather reach a real person?",
         "In a panic, what a homeowner needs most is to know a real exterminator is handling it, and a calm voice that captures the details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, and hands true emergencies straight to you."),
        ("Can I just forward the calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when your tech is under a sink, in an attic, or already on another call. Something that always answers and triages is what catches the calls a forward would still miss.")],
    "trade_slug": "pest-control-companies", "trade_plural": "pest control companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==== Should a Pest Control Company Let Customers Book Online? (how-to -> online-booking) ====
{
    "slug": "should-pest-control-offer-online-booking",
    "h1": "Should a Pest Control Company Let Customers Book Online?",
    "title": "Should a Pest Control Company Let Customers Book Online? | Top Shelf Business Solutions",
    "meta_desc": "Should a pest control company offer online booking? Yes, for routine work like quarterly service and termite inspections, while true emergencies still get sent to your phone.",
    "answer": "Yes, for the work that is not a panic. A lot of pest control, quarterly service, termite inspections, mosquito treatments, is not urgent, and those customers would happily book themselves if you let them. A booking link on your real route availability turns the phone tag into an appointment while a true emergency still gets pointed to your line.",
    "sections": [
        {"h2_html": "Not every pest call is a <em>same-day panic</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A wasp nest over the door needs a phone and a fast truck, but a lot of pest control work is not urgent at all. A homeowner wants to start a quarterly plan, book a termite inspection, get the mosquitoes handled before a backyard party, or price out rodent exclusion, and many of them would happily book it themselves if you let them. Making those customers call during business hours, wait on hold, and trade voicemails is how routine work quietly slips to the company that made booking easier.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So the answer for most pest control companies is yes, for the work that is not an emergency. A booking link lets a customer grab an open slot the moment they think of it, at night or on a lunch break, without reaching you first, and you come off a route to a visit already on the calendar instead of a missed call you now have to chase between stops.</p>'},
        {"h2_html": "Do it right and it sorts the panic from the <em>routine</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Letting customers self-schedule does not mean sending a wasp nest to a slot next week. Done properly, the booking form asks what is going on first, and a true emergency, stinging insects, a rodent indoors, a fresh bed bug find, gets pointed straight to your line to call right now, while genuinely routine work books itself. Bed bug jobs can route to an inspection slot first, since they need a look and some prep before treatment. You stay in control of the rest.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>You set which job types are bookable online, how long each takes, and how much notice you need.</li><li>It can offer the days you are already working an area, so a new quarterly stop drops into an existing route instead of sending a tech across town for one visit.</li><li>It syncs to the calendar you already use, so it cannot double-book a tech against a stop you already have.</li><li>Automatic confirmations and reminders go out with every booking, which is the single biggest lever on no-shows.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Set up that way, online booking captures the routine jobs you were losing to phone tag without ever putting a real emergency in a future slot, and the link works anywhere someone meets you: your website, your Google profile, your email signature, and the text you send after a call.</p>'}],
    "bridge_h2": "Let customers book without the callback",
    "bridge_text": "Online booking lets routine pest control work schedule itself on your real route availability, while true emergencies still get pointed to your phone, so you stop trading voicemails.",
    "bridge_slug": "online-booking-for-pest-control-companies",
    "bridge_label": "Online booking for pest control companies",
    "faqs": [
        ("Will online booking send a wasp nest to a slot three days out?",
         "Not if it is set up right. The form asks what is going on first, and a true emergency like stinging insects, a rodent indoors, or a fresh bed bug find is pointed straight to your line to call now. Only the work you mark as routine can self-schedule."),
        ("Can I control which pest control jobs customers can book?",
         "Yes. You decide which job types are bookable online, how long each runs, how much notice you need, and which days you cover which areas, so a new stop lands in a route you are already driving. Everything else still comes through a call.")],
    "trade_slug": "pest-control-companies", "trade_plural": "pest control companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==== How Do I Turn One-Time Pest Treatments Into Recurring Revenue? (how-to -> crm) ====
{
    "slug": "turn-pest-treatments-into-recurring-revenue",
    "h1": "How Do I Turn One-Time Pest Treatments Into Recurring Revenue?",
    "title": "How Do I Turn One-Time Pest Treatments Into Recurring Revenue? | Top Shelf Business Solutions",
    "meta_desc": "Turn one-time pest treatments into recurring revenue with a well-timed follow-up that offers your protection plan while the visit is fresh and the customer already trusts you.",
    "answer": "You turn a one-time treatment into recurring revenue with a well-timed follow-up that offers your protection plan while the visit is still fresh. A customer who called once for roaches or a wasp nest has already let you in and seen your work, so the plan is an easy next step, but only if someone actually follows up.",
    "sections": [
        {"h2_html": "A one-time job is a protection plan <em>waiting to happen</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner who called once for a wasp nest, a single roach treatment, or a bed bug job has already done the hard part: they let you into their home and watched your work solve a problem that scared them. That trust is the expensive thing to earn, and you already have it. The next step, the one that actually builds the business, is turning that single visit into a recurring protection plan, and it is a far easier sell than a cold one because the customer already knows you.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The catch is that the conversion depends on a follow-up that almost never happens between stops. You finish the job, collect the one-time fee, roll to the next call, and on a normal week that is the last you hear of them. The plan you could have sold is lost not because they said no, but because nobody offered it while the relief was still fresh.</p>'},
        {"h2_html": "What actually converts a one-timer into a <em>plan</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Converting one-time jobs is mostly a matter of the right message arriving at the right time, every time, which is what a CRM handles for you instead of leaving it to memory.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A friendly follow-up goes out a few days after the job, while the result is fresh, offering the protection plan and what it covers, written to sound like you.</li><li>It frames the plan around what the customer actually wants, never having to notice the problem again, since a plan treats on a schedule and catches pests before they spread instead of waiting for the next infestation to show up.</li><li>Every one-time customer, address, and service note stays in one place, so nobody who let you in the door ever falls off the list.</li><li>The same system can reach a past one-time customer before the next season, when the pest they called about last year is due to return.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this is cold-calling. It is following up with people you already served, at the moment they are most likely to say yes. Do it consistently and a steady share of your one-time jobs quietly becomes recurring revenue that bills for years, instead of a single fee you never hear from again.</p>'}],
    "bridge_h2": "Turn one-time jobs into accounts for years",
    "bridge_text": "A CRM keeps every one-time customer in front of you and follows up with the plan offer while the visit is still fresh, so more single treatments become recurring accounts instead of a fee you never hear from again.",
    "bridge_slug": "crm-for-pest-control-companies",
    "bridge_label": "CRM for pest control companies",
    "faqs": [
        ("When is the best time to offer a one-time customer a recurring plan?",
         "While the visit is still fresh, usually a few days after the job when the relief is real and they remember how easy you made it. A follow-up at that moment converts far better than one weeks later, and a CRM sends it automatically so the timing is never left to chance."),
        ("How do I convince a one-time customer a plan is worth it?",
         "Lead with what they actually want, which is never having to deal with the pest again. A recurring plan treats on a schedule so problems get caught before they spread, instead of the customer waiting to spot the next infestation and scrambling. A well-timed follow-up that makes that case, from a company they already trust, does most of the work.")],
    "trade_slug": "pest-control-companies", "trade_plural": "pest control companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
