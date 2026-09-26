"""Colony page specs for TRANSMISSION SHOPS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a transmission-shop owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, transmission-specific substance (the generator owns
shell, schema, events, keyword placement). A transmission shop is not a general repair shop:
the work is specialty big-ticket (a rebuild or a replacement runs into the thousands), the
front door is the free diagnostic / check call, the caller is an anxious driver whose
transmission is slipping, will not shift, or is grinding, often after a dealer quote that
caused sticker shock, so they shop the big number and get second opinions, and the shop that
follows up wins them. Warranty on the rebuild and referrals from general repair shops that do
not do transmissions are part of the trade. Ethics: the AI does scheduling and intake only, it
never diagnoses or quotes the repair, and nothing promises a repair outcome.

Same honesty rules as the money specs: no invented stats, percentages, or client names; hedge
instead of overpromise; only the real Top Shelf prices ($299/$899 plans, $1,500 one-time site)
ever appear and no repair price is ever invented; no em/en dashes anywhere; "find the gap" and
"go cold", never "leak" as a money metaphor (a literal transmission-fluid leak would be fine).

Six questions, mixed cost / problem, spread across the auto money pages:
  1 transmission-shop-website-cost              (cost)    -> websites-seo-for-transmission-shops
  2 transmission-answering-service-cost         (cost)    -> ai-receptionist-for-transmission-shops
  3 is-a-crm-worth-it-for-a-transmission-shop   (cost)    -> crm-for-transmission-shops
  4 why-transmission-shops-miss-calls           (problem) -> ai-receptionist-for-transmission-shops
  5 why-transmission-quotes-go-cold             (problem) -> crm-for-transmission-shops
  6 how-do-transmission-shops-get-more-customers (problem) -> marketing-for-transmission-shops
"""

TOPICS = [
# ============ How Much Does a Transmission Shop Website Cost? (cost -> websites-seo) ============
{
    "slug": "transmission-shop-website-cost",
    "h1": "How Much Does a Transmission Shop Website Cost?",
    "title": "How Much Does a Transmission Shop Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A transmission shop website can cost a little or a lot; what matters is whether it earns trust for a big repair. Top Shelf builds yours for $1,500, or free on any plan.",
    "answer": "A transmission shop website can run from a couple hundred dollars for a template to several thousand for a custom build. What matters more than price is whether it earns a nervous driver enough trust to request your free check for a big repair. Top Shelf builds one for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a transmission shop site actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A transmission is one of the scariest, most expensive things that can go wrong with a car, so the driver searching for a shop is anxious, calling several at once, and looking for one they can trust with a repair that runs into the thousands. Your website has one job before it worries about anything else: earn enough of that trust to get them to request your free check instead of calling the next shop. Price is the wrong first question. A cheap template that loads slowly and reads like every other shop does not do that job, no matter how little it cost.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Your process and your warranty on the rebuild, so a driver handing over a big repair knows what they are getting and what stands behind it.</li><li>Real reviews from people who trusted you with the same scary repair, because that calms a nervous first-time caller more than any claim you make about yourself.</li><li>A free-diagnostic request that takes one tap, so a worried driver can ask you to look at it before committing to a dollar figure.</li><li>Pages built to rank for what people actually search, like transmission repair near me and transmission slipping, so you are found the moment a transmission starts to go.</li></ul>'},
        {"h2_html": "What it costs, and what actually <em>earns its money</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number you get quoted swings widely because a template you fill in yourself and a custom site built to win big-repair jobs are different things with the same name. A do-it-yourself builder is cheap each month, but you do the work and it is rarely built to rank or to turn a scared caller into a booked free check. A one-time custom build costs more up front and is yours to keep, though a site alone does little if nobody is doing the ongoing SEO to get it found. An agency that bundles the build with ongoing SEO carries more of the long-term value, and more of the monthly cost. Before you sign anything, ask who owns the site, what a change costs, and whether you keep it if you leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific spot on Google by a specific date, because nobody controls that, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that earns the big jobs",
    "bridge_text": "A transmission site is only worth what it books. Ours is built to rank for the drivers searching nearby and to earn enough trust that a nervous caller requests your free check instead of calling the shop down the road.",
    "bridge_slug": "websites-seo-for-transmission-shops",
    "bridge_label": "Websites & SEO for transmission shops",
    "faqs": [
        ("Is a cheap template site good enough for a transmission shop?",
         "It can get you online, but a template you fill in yourself is rarely built to rank or to earn a nervous driver enough trust to hand you a repair that runs into the thousands. If a site does not get found or turn worried callers into booked free checks, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep. On a monthly plan the site is built for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "transmission_shops", "trade_plural": "transmission shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ====== What Does a Transmission Shop Answering Service Cost? (cost -> ai-receptionist) ======
{
    "slug": "transmission-answering-service-cost",
    "h1": "What Does a Transmission Shop Answering Service Cost?",
    "title": "What Does a Transmission Shop Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for transmission shops often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call, calms an anxious driver, and books your free check comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy stretch turns into a big bill. A transmission shop has a particular problem here: the calls that matter most are anxious drivers weighing a major repair, and they land while your tech is out on a road test or buried in a job and nobody is free to pick up. It helps to know the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for every call answered, so a run of price-shoppers gathering second opinions runs up the cost.</li><li>Per-minute pricing: you pay for talk time, and a worried driver with a lot of questions about a big repair is not a quick call.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a driver whose transmission is slipping, or who just got a big number from the dealer, does not leave a voicemail. They call the next shop for a straight answer and a second opinion. The real cost of a missed call is not a monthly fee, it is the rebuild that went to the shop that picked up. But a generic call center reading a script cannot calm a scared caller or offer your free check, so you can pay for coverage and still lose the job.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, stays calm with a worried driver, offers and books your free diagnostic, and gathers the vehicle and the symptoms before texting them to you. It does the scheduling and the intake, it does not diagnose the transmission or quote the repair, that stays with your techs where it belongs. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One big job you would have lost to voicemail can be worth more than the plan costs for months, and everything it books after that is on top.</p>'}],
    "bridge_h2": "Answer every big-repair call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, calms a driver weighing a big repair, and books your free check, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-transmission-shops",
    "bridge_label": "AI receptionist for transmission shops",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the one big job it books instead of losing to voicemail while your tech is on a road test."),
        ("Does it decide what is wrong with the transmission or quote the repair?",
         "No, and it should not. It answers, calms the caller, offers and books your free check, and gathers the symptoms and the vehicle, then hands the actual diagnosis and the price to your techs. It does the scheduling and intake so your people do the work only a real transmission tech can.")],
    "trade_slug": "transmission_shops", "trade_plural": "transmission shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============== Is a CRM Worth It for a Transmission Shop? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-transmission-shop",
    "h1": "Is a CRM Worth It for a Transmission Shop?",
    "title": "Is a CRM Worth It for a Transmission Shop? | Top Shelf Business Solutions",
    "meta_desc": "For most transmission shops a CRM pays for itself the first time it wins back a big quote that went cold. It comes in Top Shelf's Signature plan at $899/mo, not a separate bill.",
    "answer": "For most transmission shops, yes. A CRM pays for itself the first time it wins back a rebuild you quoted, or a driver who left to shop a second opinion. It only stops being worth it if you already chase every free check. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a transmission shop when you give away more free diagnostics and write more big quotes than anyone at the counter can keep track of, which is most shops doing real volume. It is not worth it only if you close every job on the spot and truly follow up on every check that did not book, and almost nobody does, because the bay fills up and the car on the rack comes first. The honest test is simple: how many free checks did you run last month where the driver said they needed to think about it, and how many of those did anyone call back? Those big quotes sitting quiet are exactly what a CRM is built to recover, and on a transmission job a single one is a large ticket.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a transmission shop is not the software, it is the big work that stops slipping away. A driver sitting on a rebuild quote, weighing it against buying another car, is one honest follow-up away from booking, and the shop that stays in touch usually wins the job, not the lowest number.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every free check and open quote on a schedule, so a driver getting a second opinion keeps hearing from you while the other shops go quiet.</li><li>It can carry the things that actually unstick a big repair, that you offer financing, how the warranty works, and what the job includes, so the reasons a driver hesitates are answered instead of left to talk them out of it.</li><li>It keeps the general repair shops, dealers, and used-car lots that refer transmission work in one place, so you stay in front of the referral partners who send a specialist some of the easiest jobs to book.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is simple: recover one rebuild you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put the quotes you already wrote to work",
    "bridge_text": "The free checks and big quotes you already gave away are the cheapest rebuilds you can book. A CRM follows up on every one for you, so the driver comes back to you instead of the shop that stayed in touch.",
    "bridge_slug": "crm-for-transmission-shops",
    "bridge_label": "CRM for transmission shops",
    "faqs": [
        ("Is a CRM overkill for a small transmission shop?",
         "Not usually. Even a one or two bay shop hands out more free checks and writes more big quotes than anyone can track by memory, and a single recovered rebuild is a large ticket. The point is not size, it is whether the quotes you already wrote are going cold. If they are, a CRM earns its keep fast."),
        ("How is a CRM different from keeping notes on the counter?",
         "A stack of paper diagnostics does not follow up on a quote, does not remember who is weighing financing, and does not tell you which big job is going cold. A CRM does all of that on a schedule, so the rebuild you already diagnosed comes back instead of depending on someone at the counter to remember it.")],
    "trade_slug": "transmission_shops", "trade_plural": "transmission shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Why Do Transmission Shops Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-transmission-shops-miss-calls",
    "h1": "Why Do Transmission Shops Miss So Many Calls?",
    "title": "Why Do Transmission Shops Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Transmission shops miss calls because they ring while a tech is on a road test or under a car, and an anxious driver shopping a second opinion does not leave a voicemail.",
    "answer": "Transmission shops miss calls because they come while your tech is on a road test, under a car, or deep in a rebuild, and an anxious driver weighing a big repair does not leave a voicemail. They hang up and call the next shop. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes while your tech is <em>on a road test</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Diagnosing a transmission is not a counter job. When the phone rings your tech is often out on a road test feeling for the shift that slips, under a car, or elbow deep in a rebuild, and none of those are moments anyone can stop and take a call. The busier you are, the more calls roll past, which means your best weeks are also the ones where the most work slips away. It is not a discipline problem. A shop cannot do the job in front of it and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a transmission call it is not one. A driver whose transmission is slipping, or who just got a big number from the dealer and cannot quite believe it, is anxious and calling several shops in a row for a straight answer. They are not going to leave a message and wait. They move down the list until someone picks up, and by the time you check your phone the job is already gone.</p>'},
        {"h2_html": "The calls you miss are your <em>biggest tickets</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A missed transmission call is often the biggest ticket of the week, a driver weighing a rebuild against buying another car, and it is exactly the kind of call most likely to roll to voicemail because everyone is heads-down on the work. So the calls you are most likely to miss are also the ones worth the most, and every one that goes unanswered is a rebuild handed to the shop that happened to pick up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that answers every time and knows how a transmission shop actually works. A voicemail box cannot reassure a scared caller, and a generic call center does not know a free check from a rebuild. What works is something that answers on the first ring day or night, stays calm with a worried driver, offers your free diagnostic, gathers the vehicle and the symptoms, and books the check or texts it straight to you. It does the intake and the scheduling, not the diagnosis, so you never miss the call and your techs still do the work only they can.</p>'}],
    "bridge_h2": "Stop losing big jobs to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, calms a driver weighing a big repair, offers your free check, and books it or texts it to you, so the biggest job of the week never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-transmission-shops",
    "bridge_label": "AI receptionist for transmission shops",
    "faqs": [
        ("Would an anxious customer rather reach a real person?",
         "What a worried driver needs most is to know a real shop will look at it, and a calm voice that captures the details and books a free check beats a voicemail box every time. The AI receptionist is upfront about what it is, hears the caller out, and hands the vehicle and symptoms straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when your tech is on a road test, under a car, or already on another call. Something that always answers, reassures the caller, and books the free check is what catches the big jobs a forward would still miss.")],
    "trade_slug": "transmission_shops", "trade_plural": "transmission shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Why Do Transmission Quotes Go Cold? (problem -> crm) ============
{
    "slug": "why-transmission-quotes-go-cold",
    "h1": "Why Do Transmission Quotes Go Cold?",
    "title": "Why Do Transmission Quotes Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most transmission quotes go quiet not over price but because a big repair is a decision, and nobody followed up while the driver shopped a second opinion and sorted financing.",
    "answer": "Most transmission quotes go cold not because your price was wrong, but because a big repair is a decision, and nobody followed up. The driver left to get a second opinion and sort out financing, and the job went to whoever stayed in touch. A quiet quote is usually not a no, it is a not yet.",
    "sections": [
        {"h2_html": "A quiet quote usually means still deciding, not <em>gone</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet transmission quote as a no on price, so you write it off and move on. But most of the time the driver did not decide against you at all. Nobody says yes to a rebuild on the spot. They asked for a straight answer, got a big number, and now they are getting a second opinion, waiting on a paycheck, working out whether financing makes it doable, or deciding if a car this old is worth saving. A week later they could not tell you the difference between the shops they called.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The shop that gets the job is usually not the cheapest. It is the one that stayed in front of them: a friendly check-in a few days later, a short note answering the money question that was actually holding them up. That second touch is what turns a maybe into a booked rebuild, and it is exactly the thing there is no time for with a car up on the rack.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Transmission shops do not skip follow-up because they are lazy. They skip it because the bay fills up. You finish a job, the next car goes on the rack, and by the end of the day the big quote you wrote on Tuesday is out of sight. Doing it from memory means it only happens when things are slow, which is exactly when you have the fewest quotes to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system telling you which free checks and quotes are still open and going cold.</li><li>The follow-up depends on someone at the counter remembering, so it competes with the work in the bay and loses.</li><li>By the time anyone circles back, the driver has already booked the shop that reached out first.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and it just runs. When every open quote gets a couple of timed check-ins automatically, written to sound like you and carrying the financing and warranty answers that unstick a big repair, the driver comparing shops keeps hearing from you while the others go silent, and the rebuild you already diagnosed stops slipping away.</p>'}],
    "bridge_h2": "Follow up on every quote, automatically",
    "bridge_text": "A CRM keeps every free check and open quote in front of you and sends timed check-ins for you, carrying the financing and warranty answers that close a big repair, so the driver comes back to you while the other shops go quiet.",
    "bridge_slug": "crm-for-transmission-shops",
    "bridge_label": "CRM for transmission shops",
    "faqs": [
        ("How many times should I follow up on a transmission quote?",
         "A couple of light touches over the first week or two catches most of the maybes without being pushy: a check-in a few days after the quote, then a short note about financing or the warranty that answers what was actually holding them up. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly check-in on a big repair reads as attentive, not pushy, and most drivers appreciate it because they meant to get back to you while they sorted out the money. You can always jump in and message anyone directly.")],
    "trade_slug": "transmission_shops", "trade_plural": "transmission shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ======== How Do Transmission Shops Get More Customers? (problem -> marketing) ========
{
    "slug": "how-do-transmission-shops-get-more-customers",
    "h1": "How Do Transmission Shops Get More Customers?",
    "title": "How Do Transmission Shops Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Transmission shops get more customers by showing up on Google the moment a transmission fails nearby, earning reviews that build trust for a big repair, and working referral partners.",
    "answer": "Transmission shops get more customers by showing up on Google the moment a transmission starts to fail nearby, by having reviews that earn a nervous driver trust for a big repair, and by staying in front of the shops and lots that refer transmission work. Most of it starts in the map pack, not with more ads.",
    "sections": [
        {"h2_html": "Customers find you when the <em>transmission is already going</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A transmission shop does not get browsers, it gets drivers with a problem right now. Someone whose transmission is slipping or will not shift grabs their phone and searches transmission repair near me, and what Google shows first is not a website at all. It is the map pack, the little map with three local shops, star ratings, and a call button. Most people pick from those three without scrolling further, so if you are not in them, you are invisible at the exact moment a driver is choosing who to trust with a big repair.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Reviews carry extra weight here that they do not carry for a small job. Handing a shop a repair that runs into the thousands is scary, so a nervous driver leans hard on what other people say before they call, and a shop with recent, genuine reviews wins the click over one with none. Getting found is step one, but earning trust in that map listing is what turns the search into a call.</p>'},
        {"h2_html": "The three levers that actually <em>fill the bay</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more transmission customers is less about a clever trick and more about a few things done consistently, which is exactly what slips when the shop is busy. Three levers move it, and none of them require inventing demand that is not there.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A Google Business Profile that is verified, complete, and active, so you show up in the map pack when someone nearby searches for transmission work.</li><li>A steady flow of real reviews, asked for after the job, that reassure the next nervous driver and help you rank where the calls start.</li><li>The referral relationships that feed a specialist, the general repair shops, dealers, and used-car lots that do not do transmission work in house, kept warm so they send you the job the next time a transmission goes.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Do these consistently and a quiet shop can climb over a few weeks, then compound as the reviews and referrals build. What no one can honestly promise is a specific spot on Google or a set number of cars, because nobody controls that. But these are the levers that move it, and a free audit can show you where you stand today before you spend a dollar.</p>'}],
    "bridge_h2": "Get found where the big jobs start",
    "bridge_text": "Most transmission jobs begin with a driver searching nearby the moment it starts to go. Keeping your Google profile active, your reviews genuine, and your referral partners warm is how you show up when it happens.",
    "bridge_slug": "marketing-for-transmission-shops",
    "bridge_label": "Marketing for transmission shops",
    "faqs": [
        ("Do I need to run ads to get more transmission customers?",
         "Not to start. The fastest gains for most shops are free: a verified, active Google Business Profile and a steady flow of genuine reviews put you in the map pack where nearby searches for transmission work begin. Ads can add to that, but they are not where the first wins usually come from."),
        ("How long until I show up on Google?",
         "A neglected profile that gets verified, completed, and active can start climbing within a few weeks, and it compounds as reviews and referrals build. Nobody controls Google, so no honest company promises a specific position, but consistency on the profile and reviews is what moves it.")],
    "trade_slug": "transmission_shops", "trade_plural": "transmission shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
]
