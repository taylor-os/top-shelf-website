"""Per-page content specs for the SEO corpus (plan §5), mobile mechanics batch. Same contract
as scripts/corpus_specs.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, mobile-mechanic-specific substance that clears the uniqueness gate.
Never templated find-and-replace, never the plumber, auto-repair, transmission, tire, or
auto-detailing content reworded.

Auto hub, mobile-mechanic angle. This is deliberately distinct from every fixed-shop auto trade
(no shop, no bay, no drop-off): the whole pitch is convenience, the mechanic drives to the
customer at home, work, or the roadside, and it is almost always a solo or very small operator
who is literally under a car in a driveway and physically cannot answer the next call, so the
miss goes to the next mobile mechanic or to a tow-to-shop, the exact trip the caller wanted to
avoid. The calls are can-you-come-to-me location, availability, and quote calls, often stranded
or no-start situations. The levers are answering every call while hands-on, capturing the address
and the symptom, quoting and booking a mobile slot with drive time in mind, and rebooking the
customer for future work (they love not going to a shop). Reviews about honesty, showing up on
time, and transparent pricing win, and a fast mobile site with a service-area map and an instant
quote request converts. Four service angles are here in one file (the ai-receptionist dict
carries "demo": True). Each example body ends with the literal "Illustrative example, not a
client." per the honesty rule; if the generator also appends that line, dedupe there.
"""

SPECS = [
# ==================== AI Receptionist for Mobile Mechanics ====================
{
    "slug": "ai-receptionist-for-mobile-mechanics", "demo": True,
    "trade_slug": "mobile_mechanics", "trade_plural": "mobile mechanics",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "AI Receptionist for Mobile Mechanics",
    "title": "AI Receptionist for Mobile Mechanics | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Mobile Mechanics",
    "meta_desc": "A mobile mechanic answering service answers every call while you work under a car, gets the address and symptom, gives a quote, and books the mobile visit.",
    "service_schema_name": "AI Receptionist for Mobile Mechanics",
    "eyebrow": "For Mobile Mechanics",
    "h1_html": "AI Receptionist <em>for Mobile Mechanics</em>",
    "answer_block": "A mobile mechanic answering service answers every call the moment it rings, even when you are under a car in a customer's driveway. It reassures a stranded caller, captures the address and the symptom, gives the quote you set, and books the mobile visit, so the job is yours instead of the next mechanic who answered.",
    "sections": [
        {"h2_html": "The call you miss is the driver who <em>calls the next mobile mechanic</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The phone rings while you are flat on your back under a car in a driveway, greasy to the elbows, or lying in a parking lot next to a no-start. There is no counter, no helper, and no free hand, so the call goes to voicemail. And a driver whose car will not start is not going to leave a message. They dial the next mobile mechanic on the list, and the one after that, until someone picks up, or they give up and call a tow truck to haul the car to a shop, the exact trip they called you to avoid.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An answering service picks up on the first ring while your hands stay on the car. It stays calm with a stranded caller, finds out what the car is doing and where it is sitting, and either books the mobile visit on your schedule or flags a true roadside emergency to your phone at once. The job is captured instead of handed to the mechanic down the road who happened to be free to talk.</p>'},
        {"h2_html": "Built around how a <em>mobile mechanic actually gets calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The calls that hit a mobile mechanic are not counter questions. They are can you come to me today, how much to look at it, and can you get to where I am, and every one lands while you are under a car somewhere with a wrench in your hand. A voicemail box cannot reassure a stranded driver or quote a job, and a generic call center reading a script does not know a no-start from a dead battery, or whether the address is even inside the area you cover.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers every call while your hands are on a car, so a stranded driver reaches a real answer instead of a voicemail and books with you.</li><li>Triages the way you would: whether the car will start or move at all, whether it is safe where it sits, what it is doing, and how soon they need you there.</li><li>Captures the address and the symptom, checks it against the area you cover, and books the visit on your calendar with drive time in mind, so the day routes instead of scattering.</li><li>Answers the money and coverage questions that decide a mobile job, roughly what a repair runs and whether you come to their home, work, or the roadside, from the answers you set, and treats a repeat customer differently from a first-time caller.</li></ul>'},
        {"h2_html": "The math is <em>one job you would have lost</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not need to catch many calls for this to pay for itself. A single stranded driver who books with you instead of the mechanic who answered, or one repeat customer who signs on for the next repair because you came to them, is often worth more than the service costs for months. A driver who learns they can get the car fixed in their own driveway rarely goes back to arranging a ride and a waiting room, so that first save is the start of years of work, not one ticket. Everything the service captures after that is on top. The point is to stop handing your best jobs to whoever was free to pick up while your hands were full.</p>'},
        {"h2_html": "You own the number, the calls, and the <em>customer list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on the business number you already hand out, or a new one registered in your name, not ours. Every caller, every address, and every vehicle stays yours and exportable any time, so the customer list you build is an asset you own instead of something you rent back month to month, and no long contract holds your data hostage. The answering service is one piece of the Top Shelf platform, and paired with the CRM on the Signature plan it drops every call it captures into the same system that follows up, so a quote or a return visit never quietly slips.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A no-start in the driveway, booked while you were <em>under another car</em>",
        "body_html": "A driver goes out before work and the car will not turn over in the driveway. They search for a mobile mechanic and call the first three they find. Two go to voicemail, because those mechanics are flat under cars on other jobs. Yours answers, asks whether it cranks or is completely dead, confirms the address is inside your area, and books you for early afternoon while texting the details to your phone. You slide out from under the car you are on to find the next job already on your calendar, with the address, the symptom, and the customer's number attached, instead of hearing about a driver who called a tow truck instead. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current number?",
         "Yes. It can answer on the number you already use, or set up a new one registered in your name. Either way the number and every call that comes through it belong to you and go with you if you ever leave."),
        ("Can it handle a stranded driver and get the location?",
         "Yes, that is the point. It stays calm with someone whose car will not start, asks whether it cranks, whether it is safe where it sits, and exactly where it is, then checks the spot against the area you cover and either books the visit or flags a true roadside emergency to you right away."),
        ("Will it actually book the visit on my schedule with drive time?",
         "Yes. It books against your real availability and leaves room to get across town, so a mobile day routes in a sensible order instead of sending you back and forth. You get a text with the address, the vehicle, and the symptom so you arrive ready for the job."),
        ("Is it going to sound like a robot to my customers?",
         "It answers naturally and is upfront instead of pretending to be a person. A driver stuck with a car that will not start mostly needs to know a real mechanic is coming, and a steady voice that captures the address and the problem beats a voicemail box every time. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your triage questions, your service area, and your booking rules for you, so it is answering in days, not weeks. Start with a free audit and we will show you what your current phone setup is missing.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for mobile mechanics"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-mobile-mechanics.html", "The CRM that follows up on every call you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop sending stranded drivers to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many calls and mobile jobs your current phone setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ========================= CRM for Mobile Mechanics =========================
{
    "slug": "crm-for-mobile-mechanics",
    "trade_slug": "mobile_mechanics", "trade_plural": "mobile mechanics",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "CRM for Mobile Mechanics",
    "title": "CRM for Mobile Mechanics | Top Shelf Business Solutions",
    "og_title": "CRM for Mobile Mechanics",
    "meta_desc": "A CRM for mobile mechanics follows up on quotes and past customers and sends service reminders, so a driver you fixed in a driveway calls you back next.",
    "service_schema_name": "CRM for Mobile Mechanics",
    "eyebrow": "For Mobile Mechanics",
    "h1_html": "CRM <em>for Mobile Mechanics</em>",
    "answer_block": "A CRM for mobile mechanics keeps every lead, past customer, and open quote in one place and follows up for you, so the repair a driver is weighing and the customer whose car you fixed in their driveway both come back to you instead of the mechanic who stayed in touch. Your customer list becomes your route.",
    "sections": [
        {"h2_html": "The quotes you gave in the driveway are the jobs you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most mobile mechanics do not have a lead problem so much as a follow-up problem. You get to a car, find the fault, and give the driver a price for the alternator or the brakes or the timing job, and because it is more than they hoped, they say they want to think about it, wait for payday, or check what a shop would charge. Then you are off to the next job across town and never circle back. They call two more mechanics, and the work goes to whoever followed up, not always the lowest number. The quote was never dead. It just needed one more text a few days later, and that is the thing there is never time for from the road between stops.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every open quote in front of you and follows up on a schedule you set, by text and email, whether or not you remember from the road. The driver weighing a repair hears from you again while the other mechanics go quiet, and the job comes back to you.</p>'},
        {"h2_html": "Every driveway you work in is a customer <em>for years</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A mobile mechanic has the strongest repeat hook in the trade, and most never use it. A driver who found out they could get the car fixed in their own driveway on a work-from-home Tuesday is not eager to go back to arranging a ride and sitting in a waiting room. The next oil change, the next brake job, the next no-start is yours if you stay in touch. But you cannot keep a few hundred past customers and their cars in your head while you are under a hood, so most of that repeat work rolls to whoever they stumble onto when they finally need someone.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every customer, address, vehicle, and job note lives in one place instead of a truck full of texts, receipts, and your memory.</li><li>Service reminders go out on the cadence you set, an oil change by months or mileage, a brake check, a state inspection before it lapses, so the work comes back around without you tracking dates from the road.</li><li>The repair a driver put off to next time gets a nudge when next time comes, so the deferred job does not quietly go to a shop.</li><li>You can see who has not had you out in a while and reach the right customer with the right reminder at the right time.</li></ul>'},
        {"h2_html": "The convenience is the moat, if you <em>stay in front of them</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A customer who loved not going to a shop is not being disloyal when they call someone else. They just lost your number and forgot the name of the mechanic who came out that one time. A steady, light touch, a service reminder, a seasonal note, a quick check that the last repair is still holding, keeps you saved in their phone as the mechanic who comes to them, so the next breakdown comes to you. It costs almost nothing, and it is the difference between a one-time job and a customer who calls you for every car in the household for years. Households with more than one car, and small outfits with a couple of work vans, are the same story, they love that you come to the lot, and they are worth reaching on a schedule instead of by accident.</p>'},
        {"h2_html": "You own the list, and it runs the <em>rest of your day</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every customer and every vehicle record is yours and exportable any time, not locked inside software you rent. The CRM is one piece of the Top Shelf platform and connects to the answering service, so a call it takes lands in your database and gets followed up on automatically, and to online booking, so a scheduled visit is logged against the right customer with their address and history already attached. The CRM and the answering service come together on the Signature plan, so nothing you have earned on the road goes cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The repair they put off, <em>rebooked for you</em>",
        "body_html": "You get called out for a no-start and find the battery, but while you are there you spot brakes that are close to done and quote them on the spot. The driver wants to wait for payday, so normally that is the last you hear of it. Instead the CRM sends a friendly check-in the following week and a short note after that, both written to sound like you, reminding them you can come back out to the house. The other mechanic they called never followed up, so when the brakes finally start to grind, yours is the only name still in their phone, and they book the return visit without shopping around. You never sat down to chase it. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing customers and past jobs?",
         "Yes. Your current customers, their addresses, vehicles, and job history come in and live in one place, and everything stays yours and exportable. The point is to make the customer list you already have actually work for you."),
        ("Will it really follow up on quotes automatically?",
         "Yes, on the schedule you approve. A quote you gave in the driveway gets a check-in a few days later and another after that, all sent for you, so a driver deciding on a repair keeps hearing from you while the other mechanics go quiet. You can jump in and message anyone directly any time."),
        ("Can it remind customers about service and rebook them for future work?",
         "Yes. You set the cadence, an oil change by months or mileage, a brake check, an inspection before it lapses, and the reminders go out automatically, so the recurring work and the repairs a driver deferred come back to you without you tracking a single date from the road."),
        ("How is this different from just having their number in my phone?",
         "A phone full of contacts does not follow up, does not know whose car is due, and does not tell you which quote is going cold. The CRM does all of that on a schedule, so the repeat and deferred work actually shows up instead of depending on you to remember between jobs."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your customers and vehicles, build your follow-up and reminder sequences, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will show you where jobs are slipping through today.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for mobile mechanics"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-mobile-mechanics.html", "The AI receptionist that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting quotes and customers <em>go cold</em>",
    "cta_sub": "Get a free audit of how many of your quotes and past customers are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ======================= Marketing for Mobile Mechanics =======================
{
    "slug": "marketing-for-mobile-mechanics",
    "trade_slug": "mobile_mechanics", "trade_plural": "mobile mechanics",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "Marketing for Mobile Mechanics",
    "title": "Marketing for Mobile Mechanics | Top Shelf Business Solutions",
    "og_title": "Marketing for Mobile Mechanics",
    "meta_desc": "Mobile mechanic marketing keeps your Google profile and service area first in the map pack, so a driver who wants a mechanic that comes to them calls you.",
    "service_schema_name": "Marketing for Mobile Mechanics",
    "eyebrow": "For Mobile Mechanics",
    "h1_html": "Marketing <em>for Mobile Mechanics</em>",
    "answer_block": "Mobile mechanic marketing keeps you visible where a stranded or busy driver looks, your Google Business Profile, your service area, and the map pack, so when someone nearby searches for a mechanic who comes to them, your name is the active, well-reviewed one they call instead of the mechanic who let his profile go stale.",
    "sections": [
        {"h2_html": "Mobile mechanic demand is <em>local, urgent, and wants you to come to them</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody shops for a mobile mechanic weeks ahead. Demand shows up the instant a car will not start in the driveway, dies in a parking lot, or fails on the shoulder, and it is intensely local, because a mechanic who has to drive an hour to reach the car is no use at all. On top of that, the searcher wants the one thing a corner shop cannot offer, someone who will come to them instead of making them arrange a tow and a ride. So the whole game is being visible and trusted in the towns you can actually reach, at the exact moment a nearby driver needs someone to come out, not running clever ads to people whose cars are running fine. Get found first in that moment and the job is usually yours.</p>'},
        {"h2_html": "With no shop, your Google profile is the <em>whole storefront</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A mobile mechanic has no building for a driver to walk into and no sign on a busy road, so the Google Business Profile is not part of the storefront, it is the entire storefront. When someone searches for a mobile mechanic near them, the map pack, those three local listings with the star ratings, is the first thing they see, and a driver about to let a stranger fix their car in their own driveway does not just glance at the stars. They read the reviews for one thing above all, whether you show up when you say you will and charge what you quoted. A profile full of recent reviews that say exactly that, next to a clear service area and photos of real work, quietly beats one that has sat untouched for a year. Keeping it active and honest is a standing advertisement in the exact spot a worried driver looks.</p>'},
        {"h2_html": "Set the service area you can reach, and <em>own it</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Because you drive to every job, the towns you list are not a vanity radius, they are a promise you have to keep, and drive time is margin you never get back. Marketing to a whole metro brings calls from drivers thirty minutes past where it makes sense to go, and turning those down is a bad look that still costs you the time to find out. Setting your service area to the towns and neighborhoods you can actually reach quickly, and building your profile and content around those areas, is what puts you in the map pack where the reachable work is, and it is a tighter, cheaper target than a citywide spend. It is the difference between being seen by drivers you can get to and paying to reach ones you cannot.</p>'},
        {"h2_html": "Stay ready for the season, and stay in front of <em>past customers</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Mobile work swings with the calendar, no-starts and dead batteries in the first hard cold, air conditioning when the heat lands, and the pre-trip once-over before a holiday drive, and being visible right before each wave beats scrambling once it hits. A steady local presence, seasonal posts, photos of a repair done in a driveway, the occasional honest tip, keeps you top of mind for the next breakdown and reminds past customers you are still the one who comes to them. This is the public-facing side of the business, aimed at drivers who are not your customer yet; the private follow-up to the people already in your database, the service and rebooking reminders, is the CRM.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The first cold morning, and you are <em>already at the top</em>",
        "body_html": "The first hard cold morning of the year hits and half the town goes out to a car that will not start in the driveway. They pull out their phones and search for a mobile mechanic near them all at once, because nobody wants to wait for a tow. Because your Google profile has been kept active all year, with a clear service area, recent photos of real work, and a steady stream of reviews about showing up on time and charging what you quoted, you sit at the top of the map pack when the whole town searches together. The drivers who need someone that morning call the names they can see and trust first, and yours is right there. The mechanic who let his profile go quiet is nowhere on the map. Illustrative example, not a client."},
    "faqs": [
        ("Do you post to my Google Business Profile for me?",
         "Yes. We keep it active with photos of your work, updates, and local content on a regular schedule, and keep your hours, services, and service area accurate, so it looks current whenever a driver searches for a mobile mechanic near them."),
        ("What does setting my service area actually mean?",
         "As a mobile business your profile is built around the towns and neighborhoods you cover rather than a storefront address, and your content is built around those same areas. That keeps you in the map pack where the reachable calls are and keeps you from paying to be seen by drivers too far out to reach."),
        ("How is this different from the CRM follow-up?",
         "The CRM follows up privately with people already in your database, your service and rebooking reminders. Marketing is the public-facing side, your Google profile, your reviews, and your local visibility, aimed at drivers who are not your customer yet but need to find and trust you the moment a car will not start."),
        ("Reviews matter a lot for me. Can you help me get more?",
         "Yes. Reviews about showing up on time and charging what you quoted are what convince a stranger to let you fix their car in their own driveway, so a steady flow of recent ones is one of the most valuable things you can build. We keep your profile active and make it easy for happy customers to leave a review, so your reputation is working for you the moment a driver is deciding who to call."),
        ("How long before I see it working?",
         "A neglected profile can climb in the map pack within weeks once it is active and complete, and it compounds from there as reviews and content build. Setup is included, and a free audit will show you what your current online presence looks like to someone searching near you today.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for mobile mechanics"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-mobile-mechanics.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the mobile mechanic they <em>can already see</em>",
    "cta_sub": "Get a free audit of how visible you actually are in your service area and on Google right now, whether you work with us or not. No credit card, never a call center.",
},
# ==================== Websites & SEO for Mobile Mechanics ====================
{
    "slug": "websites-seo-for-mobile-mechanics",
    "trade_slug": "mobile_mechanics", "trade_plural": "mobile mechanics",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "Websites & SEO for Mobile Mechanics",
    "title": "Websites & SEO for Mobile Mechanics | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Mobile Mechanics",
    "meta_desc": "A mobile mechanic website built for SEO ranks for mobile mechanic near me, shows the service area you cover, and captures the call instead of a lead-seller.",
    "service_schema_name": "Websites & SEO for Mobile Mechanics",
    "eyebrow": "For Mobile Mechanics",
    "h1_html": "Websites &amp; SEO <em>for Mobile Mechanics</em>",
    "answer_block": "A mobile mechanic website built for SEO ranks for what a driver searches when the car will not start, mobile mechanic near me, mechanic that comes to you, shows the service area you cover and a way to request a quote, so the job comes to you instead of a directory renting your own calls back to you.",
    "sections": [
        {"h2_html": "The lead-sellers are not competing with you, they are <em>renting you back your own calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for a mobile mechanic in your area and the top of the page is often a directory, a national booking middleman, or a pay-per-lead service, not the local mechanic. Those sites publish thousands of pages and have years of authority behind them, so a driver who searches lands there first, fills out a form, and that lead gets sold, sometimes to several mechanics at once, sometimes back to you for a fee out of your own margin. Your site not ranking is not a vanity problem. It is the reason a call you should have gotten for free gets sold to you, or handed to whoever is paying that week.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It stings for a mobile mechanic in particular, because the whole draw is that a driver reaches a local person who will come to them, and a middleman page drops a form and a lead fee into the middle of a call that was local and urgent to begin with. The driver has no loyalty yet, is often stranded, and just wants someone nearby, so the request gets routed wherever the site sends it rather than to the mechanic who could actually be there soonest. A site of your own turns that same search into a call that lands with you and nobody else, with the address and the problem in your hands from the first ring.</p>'},
        {"h2_html": "Rank for what a driver types when the <em>car will not start</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national directory this year for the broadest term, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you cover, and for the exact searches a driver makes when they are stuck: mobile mechanic near me, mechanic that comes to you, mobile car repair, and car will not start. You can also rank for the work that is pure mobile, a pre-purchase inspection done where the car is for sale, and a brake or battery job at the house. Pages built around the services you actually run and the areas you actually drive to are what search engines, and a driver who needs someone now, reward with the click.</p>'},
        {"h2_html": "A stranded driver needs to know you cover them, in <em>one tap</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone whose car will not start is on a phone, standing next to it, and they are not going to read three paragraphs. The site has to load fast, put a tap-to-call button in front of them right away, and answer the first question a mobile customer always has, do you even come to where I am. A clear service area, a simple map or list of the towns you cover, settles that before they bounce to the next result. An instant quote request, tell us the car, what it is doing, and where you are, turns a stranded driver into a lead on your phone in a couple of taps instead of a call they have to remember to make. A slow site that hides the phone number and never says where you go sends the driver straight back to the search results and the mechanic below you.</p>'},
        {"h2_html": "The calls are <em>yours</em>, permanently",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you put into a pay-per-lead service disappears the day you stop paying, and the lead was never really yours anyway. A website you own keeps ranking, keeps capturing calls and quote requests, and keeps compounding in value for as long as it exists, and it is registered to you, not a platform that can drop you or route your driver to a chain. The site plugs into the same CRM that follows up on every lead it captures and the answering service that answers the calls it drives, so nothing it earns you slips away.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A no-start finds <em>you</em>, not a directory",
        "body_html": "A driver a couple of towns over goes out to a car that will not start and searches mobile mechanic near me on their phone. Instead of a national directory that would sell the lead to three mechanics, they find your site ranking for that town, with the service area laid out so they can see you cover their street, a tap-to-call button right at the top, and a quote request a couple of taps down the page. They can see you come to them, so they call you directly, tell you the car and the address, and you head over. You paid nothing per lead, and no middleman ever touched it. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the mobile-mechanic and come-to-you searches a national directory has no reason to target well, which is exactly where a local mobile mechanic can win."),
        ("How is this different from paying for leads?",
         "A pay-per-lead service rents you a call that it also sells to other mechanics, and it stops the day you stop paying. A website you own captures calls and quote requests that are yours alone and keeps working long after it is built, without a per-lead fee coming out of every job."),
        ("How will a driver know if I cover their area?",
         "That is one of the most important things the site does. We lay out your service area plainly, with a map or a list of the towns you cover, so a stranded driver can confirm you come to them before they call, which cuts the wasted calls from people too far out and wins the ones who are in range."),
        ("Most of my calls are people stuck right now. Does a website even help?",
         "Especially then. A no-start search happens on a phone in the moment, and the mobile mechanic who shows up in the results with a clear service area, a tap-to-call button, and real reviews gets the call. A site built for that moment is exactly what captures it, and the quote request catches the ones who would rather type than talk."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks; broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for mobile mechanics"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-mobile-mechanics.html", "Staying visible in your service area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and lead-sellers taking your calls, whether you work with us or not. No credit card, never a call center.",
},
]
