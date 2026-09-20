"""Per-page content specs for the SEO corpus (plan §5), appliance repair batch. Same contract
as scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, appliance-repair-specific substance that clears the uniqueness gate.
Never templated find-and-replace, never the plumber or HVAC content reworded.

Home Services hub. Four service angles here in one file (the ai-receptionist dict carries
"demo": True). Appliance repair is its own animal, distinct from plumbing and HVAC: a dead
fridge with food spoiling, a washer that quit mid-cycle, a dryer, oven, or dishwasher is an
urgent "can you come today" call, and the homeowner books whoever answers and can give them a
slot. The tech is on the floor behind a machine with the panel off and misses the phone. The
realities that make it unlike the other trades are brand and model plus part availability, the
diagnostic or trip fee conversation, in-warranty vs out-of-warranty and manufacturer warranty
work, and honest repair-vs-replace advice. The levers are answering every same-day call,
capturing brand/model/symptom so the first visit is the fix, and reactivating past customers
for their other aging appliances and referrals.

Each example body ends with the literal "Illustrative example, not a client." per the honesty
rule; the generator strips a trailing copy and appends its own, so the dedupe is handled there.
No invented stats, prices, or clients; benefits stay hedged ("often", "usually"). A literal
washer or dishwasher water leak is the only place "leak" appears; revenue that slips is a gap,
not a leak.
"""

SPECS = [
# ==================== AI Receptionist for Appliance Repair ====================
{
    "slug": "ai-receptionist-for-appliance-repair", "demo": True,
    "trade_slug": "appliance_repair", "trade_plural": "appliance repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "AI Receptionist for Appliance Repair",
    "title": "AI Receptionist for Appliance Repair | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Appliance Repair",
    "meta_desc": "An appliance repair answering service answers every same-day call, captures the brand, model, and symptom, and books the visit while your tech has a panel off.",
    "service_schema_name": "AI Receptionist for Appliance Repair",
    "eyebrow": "For Appliance Repair",
    "h1_html": "AI Receptionist <em>for Appliance Repair</em>",
    "answer_block": "An appliance repair answering service answers every call the moment it rings, day or night, while your tech is behind a fridge with the panel off, captures the brand, model, and symptom so the truck shows up with the right part, and books the same-day visit onto your calendar. You keep your own number.",
    "sections": [
        {"h2_html": "The same-day call you miss is the fridge that <em>books the next company</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A refrigerator that quits with a week of groceries inside is not a call anyone leaves a voicemail about. The food is already warming up, so the homeowner calls an appliance repair company, and if that one does not pick up they call the next, until someone says they can come today. That is how the trade works: the customer books whoever answers and can give them a slot, not necessarily the best shop in town. But you are on the floor behind a machine with the panel off or hands-deep in a washer, nowhere near the phone. So the call rings out, and the job goes to whoever was free to answer.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An appliance repair answering service picks up on the first ring, stays professional, asks what broke and what it is doing, gets the brand, model, and address, and books the visit or flags an urgent one to you on the spot. The job is captured and sitting on your schedule instead of lost to the company that answered while you had a machine apart.</p>'},
        {"h2_html": "Built around how <em>appliance repair calls come in</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your phone does not ring on a schedule, and the calls that matter most are the ones you cannot take. A dryer quits the morning someone has to leave for work, an oven dies the day before they host, a dishwasher leaks across the kitchen floor on a Sunday, and every one wants someone today. A voicemail box cannot book a same-day slot, and a call center reading a script does not know a front-loader from a top-loader, or which brand and model tells your tech what part to load on the truck.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers every call, including the packed mornings and weekends when half the appliances in town break at once and you are already on a job.</li><li>Captures the brand, model, and exactly what the appliance is doing, so your tech rolls up with the right part and fixes it on the first visit, not a second trip.</li><li>Asks whether the appliance is still under manufacturer or store warranty, so a warranty job is handled right and an out-of-warranty repair gets the diagnostic-fee talk up front.</li><li>Treats a repeat customer or referral differently from a first-time caller, so the people who trust your work never land in a voicemail box.</li></ul>'},
        {"h2_html": "The math is <em>one saved trip</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not need to catch many calls for this to pay for itself. One same-day repair you would have lost while your hands were in a machine is often worth more than the service costs for a month. And the brand and model captured on that first call is what turns a job into a first-visit fix instead of a diagnose-today, order-the-part, drive-back-next-week trip, the quiet cost that eats an appliance repair schedule alive. Everything it catches after that is on top. The point is to stop handing your same-day work to whoever answered faster.</p>'},
        {"h2_html": "You own the number, the calls, and the <em>customer list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing business number, or a new one registered in your name, not ours. Every caller, address, and appliance you have been called about is yours and exportable any time, so your customer list is an asset you keep, not something you rent back monthly. There is no long contract holding your data hostage. The answering service is one piece of the Top Shelf platform, and it hands every call to the same CRM that follows up, so a repair estimate a customer is sitting on, or a home full of aging appliances, never quietly goes cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A Saturday fridge, booked while you have a <em>panel off</em>",
        "body_html": 'It is Saturday morning and a family opens their refrigerator to find it warm and a week of groceries starting to turn. They search for appliance repair and start calling. The first shop goes to voicemail. Yours answers, even though you are on the kitchen floor of another job with a panel off, because the answering service picked up for you. It gets the brand and model off the fridge, learns it is not cooling, confirms the address, and books you for that afternoon while a note pings your phone. You arrive at a job already on your schedule, with the brand, model, and symptom attached, so you bring the right part and fix it in one visit. Illustrative example, not a client.'},
    "faqs": [
        ("Does it work with my current phone number?",
         'Yes. It can answer on your existing business number, or set up a new one registered in your name. Either way the number and every call that comes through it belong to you and go with you if you ever leave.'),
        ("Can it capture the brand and model so we fix it on the first visit?",
         'Yes, and that is one of the biggest reasons to use it. It asks for the brand, the model number, and exactly what the appliance is doing, so your tech can bring the right part and finish the job in one trip instead of diagnosing today and driving back next week.'),
        ("Can it handle the diagnostic fee and warranty questions?",
         'Yes. It can explain your diagnostic or trip fee up front so there are no surprises, and it asks whether the appliance is still under manufacturer or store warranty, so a warranty job is routed the right way and an out-of-warranty repair starts on the same page as you.'),
        ("Is it going to sound like a robot to my customers?",
         'It answers naturally and is upfront instead of pretending to be a person. Someone staring at a fridge full of spoiling food mostly wants to know a real repair company is handling it, and a steady voice that takes the details beats a voicemail box every time. You can hear it handle a live call before you decide.'),
        ("How fast can it be running?",
         'Setup is included with no separate onboarding fee. We configure your intake questions, your schedule, and your fee and warranty rules for you, so it is answering in days, not weeks. Start with a free audit and we will show you what your current setup is missing.')],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for appliance repair companies"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-appliance-repair.html", "The CRM that follows up on every call you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing same-day repairs to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many same-day calls and repairs your current setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ======================== CRM for Appliance Repair ========================
{
    "slug": "crm-for-appliance-repair",
    "trade_slug": "appliance_repair", "trade_plural": "appliance repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "CRM for Appliance Repair",
    "title": "CRM for Appliance Repair | Top Shelf Business Solutions",
    "og_title": "CRM for Appliance Repair",
    "meta_desc": "A CRM for appliance repair chases every estimate and parts-on-order job and brings past customers back as their appliances age, so one home keeps calling you.",
    "service_schema_name": "CRM for Appliance Repair",
    "eyebrow": "For Appliance Repair",
    "h1_html": "CRM <em>for Appliance Repair</em>",
    "answer_block": "A CRM for appliance repair keeps every customer, past repair, and open estimate in one place and follows up for you, so the parts-on-order job, the repair-or-replace quote a homeowner is sitting on, and the family whose washer you fixed two years ago all come back to you. Your service list becomes your pipeline.",
    "sections": [
        {"h2_html": "The estimates and parts-on-order jobs you already have are the ones <em>slipping away</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most appliance repair shops do not have a lead problem. They have a follow-up problem. You go out, diagnose a failing washer, and tell the homeowner it needs a part you have to order, or that the repair costs enough that they should think about whether to replace it instead. Then the part sits in a box, or the estimate sits in their inbox, and between a full schedule and a phone that will not stop you never circle back. The job was never dead. The part arrived, or they decided to fix it after all, but by then they called someone who followed up, or bought a new machine while waiting to hear from you.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every open estimate and every parts-on-order job in front of you and follows up on a schedule you set, with texts and emails that go out on time whether or not you remember. The homeowner waiting on a part hears the moment it is in and gets booked, the repair-or-replace quote gets a nudge while they are still deciding, and the job comes back to you instead of stalling out.</p>'},
        {"h2_html": "Every home you visit has <em>several more appliances aging</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When you fix one appliance, you are standing in a house with a refrigerator, a washer, a dryer, an oven, a dishwasher, and a water heater, all at different ages, all going to fail eventually. The customer whose dryer you repaired this year is the easiest call you will ever get when their fridge starts acting up, because you have already been in the home and they already trust your work. But you cannot personally remember every home you have been in and what you saw there, so most of that repeat work drifts to whoever they find online once they have forgotten your name.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every customer, address, appliance, and repair you have done lives in one place instead of a stack of invoices and your memory.</li><li>You can see who you served a year or two ago and reach out before their next appliance sends them searching for someone new.</li><li>Thank-you and referral asks go out automatically after a repair, so a happy customer actually gets asked while the good experience is still fresh.</li></ul>'},
        {"h2_html": "The customer who forgot your name is <em>still yours to keep</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner you helped two years ago is not disloyal when they call another shop. They just lost the magnet off the fridge and never saved your number. A steady, light touch, a seasonal tip, a check that the last repair is still holding, a reminder that you service every major brand in the house, keeps your name in their phone so the next breakdown comes to you. It costs almost nothing, and it is the difference between a one-time repair and a household that calls you for every appliance for years, and tells their neighbors to do the same.</p>'},
        {"h2_html": "You own the list, and it <em>works with the rest of the system</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every customer and every note is yours and exportable any time, not locked inside software you rent. The CRM is one piece of the Top Shelf platform and connects to the answering service, so a call it captures lands in your database with the brand and model already attached and gets followed up on automatically, and to online booking, so a scheduled visit is logged against the right home with its full repair history attached. Nothing you have earned goes cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The part comes in, and the job <em>does not stall</em>",
        "body_html": 'You diagnose a dishwasher on a Tuesday, tell the homeowner it needs a control board you will order, and head to your next call. Normally that part shows up a week later, gets buried on the truck, and the customer, tired of waiting, buys a new dishwasher before you ever call back. Instead the CRM is holding the open job, and the day the part is marked in, it prompts a text to the homeowner to get them rebooked. They are on your schedule that week, the repair is finished, and a job that used to stall out quietly closes itself. You never had to keep the part order in your head. Illustrative example, not a client.'},
    "faqs": [
        ("Does it import my existing customers and repair history?",
         'Yes. Your current customers, past repairs, open estimates, and the appliances in each home come in and live in one place, and everything stays yours and exportable. The point is to make the service list you already built actually bring work back.'),
        ("Will it follow up on estimates and parts-on-order jobs automatically?",
         'Yes, on the schedule you approve. An open repair estimate gets a check-in while the homeowner is still deciding, and a parts-on-order job prompts a rebooking text the moment the part is in, so a job never stalls out waiting on you. You can step in and message anyone directly any time.'),
        ("Can it help me get repeat work from past customers?",
         'Yes, and for appliance repair that is where the easy money is. Every home you have visited has several other appliances aging behind the one you fixed. The CRM flags customers you served a year or two ago and reaches them before their next breakdown sends them searching for someone else.'),
        ("How is this different from just having their number in my phone?",
         'A phone full of contacts does not follow up, does not remember which home has a part on order, and does not tell you which estimate is going cold. The CRM does all of that on a schedule, so the repeat work and the quotes you already gave actually turn into booked repairs.'),
        ("How long until it is set up?",
         'Setup is included with no separate onboarding fee. We bring in your customers and repair history, build your follow-up and referral sequences, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will find the gaps where repairs are slipping through today.')],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for appliance repair companies"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-appliance-repair.html", "The answering service that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting estimates and customers <em>go cold</em>",
    "cta_sub": "Get a free audit of how many of your estimates, parts-on-order jobs, and past customers are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ======================== Marketing for Appliance Repair ========================
{
    "slug": "marketing-for-appliance-repair",
    "trade_slug": "appliance_repair", "trade_plural": "appliance repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "Marketing for Appliance Repair",
    "title": "Marketing for Appliance Repair | Top Shelf Business Solutions",
    "og_title": "Marketing for Appliance Repair",
    "meta_desc": "Appliance repair marketing keeps your Google profile active in the map pack, showing the brands you fix and same-day help, so you catch every local breakdown.",
    "service_schema_name": "Marketing for Appliance Repair",
    "eyebrow": "For Appliance Repair",
    "h1_html": "Marketing <em>for Appliance Repair</em>",
    "answer_block": "Marketing for appliance repair keeps you visible where local demand shows up, your Google Business Profile and the map pack, so when an appliance quits and someone nearby searches for a repair company that fixes their brand, your name is the active, well-reviewed one they call instead of the shop that let its profile go stale.",
    "sections": [
        {"h2_html": "Appliance breakdowns are <em>local and immediate</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody shops around for weeks when their fridge dies. The demand appears the instant an appliance quits, and it is intensely local, because a homeowner wants someone who can be at their door today, not a company an hour across the metro. Unlike a trade that spikes twice a year with the weather, appliance repair breaks steadily all year long. Somebody\'s washer floods a laundry room every single day, which means the whole game is being visible and trusted in your service area the moment it happens to be their turn, not running clever ads at people whose appliances are all working fine. Get found first in that moment and the job is usually yours.</p>'},
        {"h2_html": "Your Google Business Profile is the new <em>storefront</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone searches for appliance repair near them, the map pack, those three local listings with the star ratings, is the first thing they see, above the websites and above the ads. A profile that has sat untouched for months looks abandoned next to one with recent photos of real repairs, current hours, and a steady stream of reviews. For appliance repair the profile has to answer two questions fast: do they fix my brand, and can they come today. A profile that lists the brands you service and makes your same-day availability obvious turns a searcher\'s glance into a call, in the exact spot they look when something breaks.</p>'},
        {"h2_html": "Show up in the <em>towns you actually cover</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Marketing to a whole metro is expensive and forgettable, and it sends you calls from an hour outside the range you would drive for a single-appliance repair. Focusing on the specific towns and neighborhoods you serve, with a profile, photos, and content built around those areas, is what puts you in the map pack where you can actually take the work and still make money on the trip. It is a tighter, cheaper target than a citywide spend, and it is the one that turns into repairs your tech can reach the same day without burning half the schedule in traffic.</p>'},
        {"h2_html": "Stay in front of the neighborhood, and your <em>past customers</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The strongest appliance repair businesses are the name a neighborhood already knows before anything breaks. A steady local presence, real job photos, an honest tip on whether a repair is worth it, a reminder of the brands you service, keeps you top of mind so the next breakdown and the referral to a neighbor come to you instead of whoever they saw most recently. Every home has several appliances waiting to fail, so the customer you win once is worth years of work if they remember you. This is the public-facing side of the business; the private follow-up to people already in your database is the CRM.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The washer that floods on a Sunday finds <em>you at the top</em>",
        "body_html": 'A family two neighborhoods over starts a load of laundry on a Sunday and comes back to a washer that has leaked across the floor. They grab a phone and search for appliance repair near them. Because your Google profile has been kept active all year, with recent repair photos, current hours, the brands you service listed plainly, and a steady flow of reviews, you are sitting at the top of the map pack. They can see you fix their brand and offer same-day help, so they call you first, ahead of the shop below you that let its profile go quiet. You booked a same-day job you paid nothing per lead for. Illustrative example, not a client.'},
    "faqs": [
        ("Do you post to my Google Business Profile for me?",
         'Yes. We keep it active with photos of real repairs, updates, and local content on a regular schedule, and keep your hours, the brands you service, and your service area accurate, so it looks current whenever someone searches for appliance repair near them.'),
        ("Why does listing the brands I service matter so much?",
         'Because it is the first thing a worried homeowner checks. Someone with a broken machine wants to know you fix their brand before they call, and a profile and site that name the brands you service, along with same-day availability, turn a glance into a booked repair instead of a bounce to the next shop.'),
        ("Isn't appliance repair too steady to bother marketing?",
         'Steady demand is exactly why it pays. Appliances break every day of the year, not in two big seasons, so the shop that shows up first in the map pack every single day catches a stream of work the invisible shop never even hears about.'),
        ("How is this different from the CRM follow-up?",
         'The CRM follows up privately with people already in your database. Marketing is the public-facing side, your Google profile, reviews, and local visibility, aimed at homeowners who are not your customer yet but need to find and trust you the moment an appliance quits.'),
        ("How long before I see it working?",
         'A neglected profile can climb in the map pack within weeks once it is active and complete, and it compounds from there as reviews and content build. Setup is included, and a free audit will show you what your current online presence looks like to someone searching near you today.')],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for appliance repair companies"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-appliance-repair.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the repair company they <em>can already see</em>",
    "cta_sub": "Get a free audit of how visible you actually are in your service area and on Google right now, whether you work with us or not. No credit card, never a call center.",
},
# ==================== Websites & SEO for Appliance Repair ====================
{
    "slug": "websites-seo-for-appliance-repair",
    "trade_slug": "appliance_repair", "trade_plural": "appliance repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "Websites & SEO for Appliance Repair",
    "title": "Websites & SEO for Appliance Repair | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Appliance Repair",
    "meta_desc": "An appliance repair website built for SEO ranks for refrigerator repair and appliance repair near me, names the brands you fix, and books the same-day visit.",
    "service_schema_name": "Websites & SEO for Appliance Repair",
    "eyebrow": "For Appliance Repair",
    "h1_html": "Websites &amp; SEO <em>for Appliance Repair</em>",
    "answer_block": "An appliance repair website built for SEO ranks for the searches a homeowner makes when something breaks, refrigerator repair, washer repair, appliance repair near me, shows up in the map pack for the towns you cover, lists the brands you service, and captures the same-day call before they bounce, so the repair is yours instead of a lead-seller's.",
    "sections": [
        {"h2_html": "The lead-sellers are not competing with you, they are <em>renting you back your own calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for appliance repair in your town and the top of the page is often a directory, a national booking middleman, or a pay-per-lead service, not the local shop. Those sites publish thousands of pages and carry years of authority, so when a homeowner searches, they land there first, fill out a form, and that lead gets sold, sometimes to three repair companies at once, sometimes back to you for a fee out of your own margin. Your site not ranking is not a vanity problem. It is the reason a same-day call you should have had for free gets sold to you, or handed to two competitors in the same breath.</p>'},
        {"h2_html": "Rank for the appliance and brand a homeowner <em>actually searches</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Homeowners do not search for major appliance service. They search for exactly what broke: refrigerator repair, washer repair, dryer not heating, dishwasher leaking, oven repair near me, and very often their brand along with it. You will not outrank a national directory this year for the broadest term, and you do not need to. You can rank for your own name, for the specific towns you cover, and for those exact appliance-and-city and brand-and-city searches a national directory has no reason to answer well. A page about refrigerator repair in your town, or the specific brands you are equipped to service, is something you can own outright while the directories chase the generic keyword.</p>'},
        {"h2_html": "A homeowner with a warm fridge should reach you in <em>one tap</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone whose refrigerator died an hour ago is on a phone, not a desktop, and they have no patience for a slow page or a buried number. The site has to load fast, put a tap-to-call button and your same-day availability in front of them immediately, name the brands you service so they know they are in the right place, and make requesting a visit simple. A homeowner in that spot is not going to read three paragraphs or hunt for your number. A good-looking site that hides the phone loses the very customer it just brought in, so a visitor should never leave without an easy way to reach you.</p>'},
        {"h2_html": "The calls are <em>yours</em>, permanently",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you pour into a pay-per-lead service disappears the day you stop paying, and the lead was never really yours anyway, it was sold to your competitors in the same breath. A website you own keeps ranking, keeps capturing calls, and keeps compounding in value for as long as it exists, and it is registered to you, not a platform that can drop you tomorrow. The site plugs into the same CRM that follows up on every repair it captures and the answering service that picks up the calls it drives, so nothing it earns you slips away.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A dead fridge finds <em>you</em>, not a directory",
        "body_html": 'A homeowner two towns over opens a refrigerator that stopped cooling overnight and grabs their phone to search for appliance repair near them. Instead of a national directory that would sell their details to three shops at once, they find your site ranking for that town, see the brands you service listed, that you offer same-day visits, and real reviews, and tap to call from the top of the page. Your phone rings with a job you paid nothing per lead for, the customer already knows you fix their brand, and no middleman ever touched the call. Illustrative example, not a client.'},
    "faqs": [
        ("Will my site actually outrank the big directories and lead sites?",
         'Not for the broadest national terms overnight. For the searches that matter to you, appliance-and-city terms like refrigerator repair in your town, the brands you service, and same-day appliance repair near you, a local shop can realistically rank and win, because that is exactly where a national directory has nothing local to offer.'),
        ("How is this different from buying leads from a directory?",
         'A pay-per-lead service rents you a call it also sells to your competitors, and it stops the day you stop paying. A website you own captures calls that are yours alone and keeps working long after it is built, without a per-lead fee coming out of every repair.'),
        ("Should the site list the brands I service?",
         'Yes. It is one of the first things a homeowner checks, and it helps you rank for brand-and-appliance searches at the same time. Naming the brands you are equipped to repair reassures the visitor they are in the right place and captures searches a generic directory never targets.'),
        ("Is the site built to get people to call, not just look nice?",
         'Yes. It loads fast, puts tap-to-call and your same-day availability in front of a visitor immediately, and names your brands and service area, because a homeowner with a warm fridge calls the company that is easiest to reach, not the prettiest page.'),
        ("How long until it starts ranking?",
         'Local, specific searches can start moving within weeks, and broader terms compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.')],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for appliance repair companies"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-appliance-repair.html", "Staying visible in your service area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>appliance repair near you</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and lead-sellers taking your calls, whether you work with us or not. No credit card, never a call center.",
},
]
