"""Per-page content specs for the SEO corpus (plan §5), tire shops batch. Same contract
as scripts/corpus_specs.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, tire-shop-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the plumber, auto-repair, auto-body, or auto-detailing content
reworded.

Auto hub, tire angle. This is deliberately distinct from the general auto-repair batch
(mechanical diagnosis, drop-offs, warning lights), the auto-body batch (collision, insurance
claims), and the detailing batch (cosmetic, appointment-based). A tire shop lives on a firehose
of price-and-availability calls (do you have my size, how much for four, can I come now), the
same-day flat or blowout, and the caller who books whoever answers with a price and a slot. The
money is in the attach (alignment, rotation, road-hazard, TPMS) and in getting the customer back
for rotations and the next set; reactivating customers by mileage or season and holding fleet
accounts is the goldmine; demand spikes hard with the season. Four service angles are here in one
file (the ai-receptionist dict carries "demo": True). Each example body ends with the literal
"Illustrative example, not a client." per the honesty rule; if the generator also appends that
line, dedupe there.
"""

SPECS = [
# ====================== AI Receptionist for Tire Shops ======================
{
    "slug": "ai-receptionist-for-tire-shops", "demo": True,
    "trade_slug": "tire_shops", "trade_plural": "tire shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "AI Receptionist for Tire Shops",
    "title": "AI Receptionist for Tire Shops | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Tire Shops",
    "meta_desc": "A tire shop answering service answers every call while your crew is mounting and balancing, quotes the size in stock, and books the flat or the new set.",
    "service_schema_name": "AI Receptionist for Tire Shops",
    "eyebrow": "For Tire Shops",
    "h1_html": "AI Receptionist <em>for Tire Shops</em>",
    "answer_block": "A tire shop answering service answers every call the moment it rings, even when every bay is busy mounting and balancing. It tells the price shopper what you have in stock, gives a straight quote, and books the flat or the new set on your schedule, so the sale is yours instead of the shop that picked up.",
    "sections": [
        {"h2_html": "The call you miss is the price shopper who <em>books the next shop</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A tire buyer is calling to ask three things: do you have my size, what does a set run, and can you get me in today. They are calling three or four shops in a row to ask the same thing, and they book with the first one that picks up and gives a straight answer, because tires feel like a commodity and speed and a price win the sale. But your crew is on the mounting machine, spinning a balancer, or pulling a wheel in the bay, so the call rolls to voicemail, and a buyer who wanted four tires today does not leave a message. They dial the next shop.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An answering service answers on the first ring, tells the caller whether the size is in stock, gives the quote you set, and books the appointment or the flat right then. The sale is captured instead of handed to the shop down the road that happened to be near the counter.</p>'},
        {"h2_html": "Built around how a <em>tire shop actually gets calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The calls that hit a tire shop are not service riddles. They are people who want a price, a size, and a slot: do you have my size in stock, what does a set of four run out the door, can you patch a flat this afternoon, how long is the wait. They land in the middle of the day when every bay is full and the counter has a line of walk-ins. A voicemail box cannot quote a set, and a generic call center reading a script does not know a rotation from an alignment or which size fits the car on the phone.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers every call during the busy bays, so a price shopper reaches a real answer and a straight quote instead of a voicemail, and books with you.</li><li>Handles the same-day need, a flat, a blowout, or a tire losing air, and gets the customer in today instead of sending them to whoever answered.</li><li>Takes the size off the sidewall or the year, make, and model, tells them what you have, quotes what you set, and books the mounting or the repair on your calendar.</li><li>Treats a fleet account or a repeat customer differently from a first-time caller, so the accounts that keep your bays full never hit a voicemail.</li></ul>'},
        {"h2_html": "The math is <em>one set of four</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not need to catch many calls for this to pay for itself. One customer who wanted four tires today, and would have bought them from whoever answered, is often worth more than the system costs for months, because a set of four usually brings an alignment, a road-hazard warranty, and a new valve or sensor, and that customer comes back for rotations and the next set. A single fleet account you catch on the phone can be steady work for years. Everything it books after that first save is on top. The point is to stop handing your best buyers to the shop that answered faster while your crew had their hands full.</p>'},
        {"h2_html": "You own the number, the calls, and the <em>customer list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing shop number, or a new one registered in your name, not ours. Every caller, every vehicle, and every size you quoted stays yours and exportable any time, so the customer list you build is an asset you own instead of something you rent back month to month, and no long contract holds your data hostage. The answering service is one piece of the Top Shelf platform, and paired with the CRM on the Signature plan it drops every call it captures into the same system that follows up, so a quote or a rotation reminder never slips.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "Four tires, booked while your crew was <em>on the balancer</em>",
        "body_html": "A driver notices two tires are down to the wear bars and calls around on their lunch break to price a new set. Yours is the second shop they try. Every bay is full, one tech is on the mounting machine and another is spinning a balancer, so on any other day the call goes to voicemail and they book whoever picks up next. Instead the service answers, gets the size off the car, tells them you have it in stock, gives the out-the-door quote you set, and books a mounting appointment for the next morning while texting you the details. You look up from the balancer to a set already sold and on the calendar, with the vehicle, the size, and the quote attached, instead of hearing about a customer who bought somewhere else. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current shop number?",
         "Yes. It can answer on the number you already use, or set up a new one registered in your name. Either way the number and every call that comes through it belong to you and go with you if you ever leave."),
        ("Can it quote a price and tell a caller what is in stock?",
         "It gives the prices and out-the-door ranges you set for your common sizes and services, and tells the caller whether a size is one you normally stock or would order in. For anything that needs your eyes first, it captures the size and the vehicle, books the appointment, and texts you the details so you can confirm the number."),
        ("Can it get a same-day flat or blowout in today?",
         "Yes. It treats a flat, a blowout, or a tire losing air as the same-day job it is, checks how drivable the car is, and books the repair or gets them in today instead of sending them to the shop that answered. You set what counts as a drop-everything job."),
        ("Is it going to sound like a robot to my customers?",
         "It answers naturally and is upfront instead of pretending to be a person. A driver who just wants to know you have their size and can get them in today cares that the call was answered and the quote was straight, not that a receptionist picked up. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We load your sizes, your pricing rules, and your booking rules for you, so it is answering in days, not weeks. Start with a free audit and we will show you what your current phone setup is missing.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for tire shops"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-tire-shops.html", "The CRM that follows up on every call you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop sending tire buyers to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many price-and-availability calls and same-day flats your current phone setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ============================ CRM for Tire Shops ============================
{
    "slug": "crm-for-tire-shops",
    "trade_slug": "tire_shops", "trade_plural": "tire shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "CRM for Tire Shops",
    "title": "CRM for Tire Shops | Top Shelf Business Solutions",
    "og_title": "CRM for Tire Shops",
    "meta_desc": "A CRM for tire shops follows up on every quote, reminds customers when rotations and the next set are due, and keeps fleet accounts coming back to you.",
    "service_schema_name": "CRM for Tire Shops",
    "eyebrow": "For Tire Shops",
    "h1_html": "CRM <em>for Tire Shops</em>",
    "answer_block": "A CRM for tire shops keeps every customer, vehicle, and quote in one place and follows up for you, so the set a driver is pricing, the customer whose tires are wearing thin, and the fleet down the road all come back to you instead of the shop that stayed in touch. Your customer list becomes your bay schedule.",
    "sections": [
        {"h2_html": "The sets you already quoted are the sales you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A tire shop does not usually have a traffic problem so much as a follow-up problem. Someone calls or walks in, you price a set of four, they say they want to think about it or check a price online, and then the bays fill up and nobody circles back. They call two more shops, forget which was cheapest, and buy from whoever reached out, not always the lowest number. The quote was never dead. It just needed one more text a couple of days later, and that is the thing there is never time for when the counter is three deep.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every open quote in front of you and follows up on a schedule you set, by text and email, whether or not anyone at the counter remembers. The buyer comparing four shops hears from you again while the others go quiet, and the set comes back to you.</p>'},
        {"h2_html": "Every set you sell is a customer <em>on a clock</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A set of tires is not a one-time sale, it is the start of a schedule. The customer you sold four tires owes you a rotation every few thousand miles, especially if the rotations came free with the set, the tread is wearing to a date you can predict, and the next set is yours if you are the shop that reaches out before they start shopping. But you cannot personally remember when a few thousand past customers are each due, so most of that repeat work rolls to whoever is closest or cheapest the day they finally notice a bald tire.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every customer, vehicle, the size and set they bought, and the mileage live in one place instead of a drawer of paper invoices and your memory.</li><li>Rotation and balance reminders go out on the cadence you set, so the free rotations you bundled with the set actually bring the customer back through your door.</li><li>The tread wears on a clock, so a customer coming due for a new set gets a nudge from you before a competitor catches them searching.</li><li>Road-hazard warranties and alignments have their own timing, and the reminders go out on schedule so the attach work comes back around too.</li></ul>'},
        {"h2_html": "Fleet accounts and customers due for a set are a <em>goldmine sitting idle</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A customer whose tires are wearing out is not being disloyal, they just have not looked yet, and nothing forces the issue until a tire is bald or fails an inspection. A steady, light touch, a note that a rotation is due, a heads-up that the tread is getting low, keeps you the shop they call before they start comparing prices across town. And the fleet accounts, the contractor with a handful of trucks, the local business with a few vans, are some of the most valuable customers a tire shop can hold, because they buy on repeat and they buy in volume. Managing those accounts and reaching them on a schedule, instead of waiting for a truck to roll in on a bad tire, is some of the easiest work you will book all month, and it is sitting in the customer list you already have.</p>'},
        {"h2_html": "You own the list, and it works with the <em>rest of the shop</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every customer and every vehicle record is yours and exportable any time, not locked inside software you rent. The CRM is one piece of the Top Shelf platform and connects to the answering service, so a call it takes lands in your database and gets followed up on automatically, and to online booking, so a mounting appointment is logged against the right customer with their size and history already attached. The CRM and the answering service come together on the Signature plan, so nothing you have earned goes cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The rotation reminder that becomes <em>the next set</em>",
        "body_html": "You sell a customer four tires in the spring with free rotations bundled in. Normally they drive off and you do not see them again until something goes wrong. Instead the CRM reminds them a few months later that a rotation is due, so they come back in, and while the car is on the lift your tech notices the fronts are wearing faster than the rears. Because the visit happened at all, you catch it early, sell an alignment, and stay the shop they think of. A couple of years on, when the tread is finally down, the CRM nudges them before anyone else does, and the next set is yours without a price war. You never sat down to track any of it. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing customers and their tire history?",
         "Yes. Your current customers, their vehicles, and the sets and sizes they bought come in and live in one place, and everything stays yours and exportable. The point is to make the customer list you already have actually work for you."),
        ("Will it really follow up on quotes automatically?",
         "Yes, on the schedule you approve. A set you priced gets a check-in a couple of days later and another after that, all sent for you, so a buyer comparing shops keeps hearing from you while the others go quiet. You can jump in and message anyone directly any time."),
        ("Can it remind customers about rotations and when they are due for new tires?",
         "Yes. You set the cadence, a rotation and balance every few thousand miles, a heads-up as the tread wears down, an alignment or a road-hazard check on its own timing, and the reminders go out automatically so the recurring and the next-set work come back without you tracking a single date."),
        ("Does it handle fleet accounts?",
         "Yes. You can group a fleet account and its vehicles together, keep the sizes and service history for each truck or van in one place, and reach the account on a schedule instead of waiting for a bad tire to bring one in. Those repeat, high-volume customers are exactly the ones worth managing this way."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your customers and vehicles, build your follow-up and reminder sequences, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will show you where sales are slipping through today.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for tire shops"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-tire-shops.html", "The AI receptionist that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting quotes and customers <em>go cold</em>",
    "cta_sub": "Get a free audit of how many of your quotes, past customers, and fleet accounts are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ========================= Marketing for Tire Shops =========================
{
    "slug": "marketing-for-tire-shops",
    "trade_slug": "tire_shops", "trade_plural": "tire shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "Marketing for Tire Shops",
    "title": "Marketing for Tire Shops | Top Shelf Business Solutions",
    "og_title": "Marketing for Tire Shops",
    "meta_desc": "Tire shop marketing keeps your Google Business Profile active and first in the map pack, so a driver on a worn or flat tire calls you first when they search.",
    "service_schema_name": "Marketing for Tire Shops",
    "eyebrow": "For Tire Shops",
    "h1_html": "Marketing <em>for Tire Shops</em>",
    "answer_block": "Tire shop marketing keeps you visible where drivers actually look, your Google Business Profile and the map pack, so when someone nearby searches for tires the moment a tire goes flat, the tread is gone, or the first cold snap hits, your name is the active, well-reviewed one they call instead of the shop that let its listing go stale.",
    "sections": [
        {"h2_html": "Tire demand is <em>local, sudden, and seasonal</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody shops for a tire shop weeks ahead. Demand shows up the instant a tire goes flat, a blowout leaves someone on the shoulder, or a driver finally notices the tread is down to the bars, and it is intensely local, because they want a shop they can reach today. But tires are also the one auto trade with a real calendar to them: the first cold, wet morning sends everyone who has been driving on worn tires searching at once, and spring, with road trips and inspections ahead, brings another wave. Get found first in those moments, in your own area, and the car usually comes to you.</p>'},
        {"h2_html": "Your Google profile is where a driver picks the shop with <em>honest prices and no wait</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone searches for tires near them, the map pack, those three local listings with the star ratings, is the first thing they see, above the websites and the ads. A tire buyer has usually been burned by a surprise charge or a shop that kept them waiting all afternoon, so they do not just glance at the stars, they read the reviews for two things: honest, out-the-door pricing and how fast the shop got them in and out. A profile full of recent reviews that say exactly that, next to current hours and photos of the shop, quietly beats one that has sat untouched for a year. Keeping it active and honest is a standing advertisement in the exact spot people look when a tire goes.</p>'},
        {"h2_html": "Show up in the <em>towns you actually serve</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Marketing to a whole metro is expensive and forgettable, and it brings calls from drivers too far out to bother making the trip for a set of tires. Focusing on the specific towns and neighborhoods your customers actually drive from, with a profile, photos, and content built around those areas, is what puts you in the map pack where the nearby, ready-to-buy searches are, and it is a tighter, cheaper target than a citywide spend. It is the difference between being seen by people who will actually roll into your bay and paying to reach people who never will.</p>'},
        {"h2_html": "Stay ready for the season, and stay in front of <em>past customers</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Tire demand swings with the calendar, the first freeze and the first slick roads, the spring road-trip and inspection season, the changeover for anyone running winter tires, and being visible right before each wave beats scrambling once it lands. A steady local presence, seasonal posts, photos of real work, the occasional reminder to check tread before a trip, keeps you top of mind for the next flat and reminds past customers you are still the shop to call. This is the public-facing side of the business, aimed at drivers who are not your customer yet; the private follow-up to the people already in your database, the rotation and next-set reminders, is the CRM.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The first slick morning, and you are <em>already at the top</em>",
        "body_html": "The first cold, wet morning of the season hits and half the town that has been putting off worn tires suddenly feels them slip at a stop sign. They pull out their phones and search for tires near them all at once. Because your Google profile has been kept active all year, with recent photos of the shop, current hours, and a steady stream of reviews about fair prices and a fast turnaround, you sit at the top of the map pack when the whole town searches together. The drivers who want tires that day call the names they can see and trust first, and yours is right there. The shop that let its profile go quiet is nowhere on the map. Illustrative example, not a client."},
    "faqs": [
        ("Do you post to my Google Business Profile for me?",
         "Yes. We keep it active with photos of the shop and the work, updates, and local content on a regular schedule, and keep your hours, services, and the brands and sizes you carry accurate, so it looks current whenever a driver searches for tires near them."),
        ("What does focusing on my service area actually mean?",
         "It means building your profile and content around the specific towns and neighborhoods your customers actually drive from, instead of spreading a budget across a whole metro. That is what gets you into the map pack where the local, ready-to-buy searches are."),
        ("Can you help me get ahead of the seasonal waves?",
         "Yes. We time your visibility to the swings that matter for tires, the first cold and slick roads, spring road trips and inspection season, the winter changeover, so you are already in front of drivers before the rush instead of scrambling once the calls start."),
        ("How is this different from the CRM follow-up?",
         "The CRM follows up privately with people already in your database, your rotation and next-set reminders. Marketing is the public-facing side, your Google profile, your reviews, and your local visibility, aimed at drivers who are not your customer yet but need to find and trust you the moment a tire goes."),
        ("How long before I see it working?",
         "A neglected profile can climb in the map pack within weeks once it is active and complete, and it compounds from there as reviews and content build. Setup is included, and a free audit will show you what your current online presence looks like to someone searching near you today.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for tire shops"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-tire-shops.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the tire shop they <em>can already see</em>",
    "cta_sub": "Get a free audit of how visible you actually are in your service area and on Google right now, whether you work with us or not. No credit card, never a call center.",
},
# ====================== Websites & SEO for Tire Shops ======================
{
    "slug": "websites-seo-for-tire-shops",
    "trade_slug": "tire_shops", "trade_plural": "tire shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "Websites & SEO for Tire Shops",
    "title": "Websites & SEO for Tire Shops | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Tire Shops",
    "meta_desc": "A tire shop website built for SEO ranks for tires near me and your city, shows the brands you carry, and books the appointment instead of a lead-seller.",
    "service_schema_name": "Websites & SEO for Tire Shops",
    "eyebrow": "For Tire Shops",
    "h1_html": "Websites &amp; SEO <em>for Tire Shops</em>",
    "answer_block": "A tire shop website built for SEO ranks for what a driver searches when they need tires, tires near me and cheap tires in your city, shows the brands and sizes you carry, and lets them get a price or book a slot, so the sale comes to you instead of a directory renting your own calls back to you.",
    "sections": [
        {"h2_html": "The lead-sellers are not competing with you, they are <em>renting you back your own calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for tires in your town and the top of the page is often a directory, a national tire-buying site, or a pay-per-lead service, not the local shop. Those sites publish thousands of pages and have years of authority behind them, so a driver who searches lands there first, picks a tire or fills out a form, and that sale or that lead gets routed, sometimes to a chain, sometimes sold back to you for a fee out of your own margin. Your site not ranking is not a vanity problem. It is the reason a customer who is a few minutes from your bay gets handed to a middleman, or to whoever is paying that week.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It stings more for tires than most trades, because a tire buyer has no loyalty yet and treats one shop like the next, so the search gets shopped around and the sale goes wherever the site sends it, not to the shop with the better price or the open bay. A site of your own turns that same search into a call or a booking that lands with you and nobody else, with the customer and the vehicle in your hands from the first click.</p>'},
        {"h2_html": "Rank for what a driver types when they <em>need tires</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national tire site this year for the broadest term, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you cover, and for the exact searches a driver makes when they need rubber: tires near me, cheap tires in your city, new tires, flat tire repair near me, used tires, and often a specific size or the brand they already have in mind. Pages built around the services you actually run, mounting and balancing, rotations, alignments, and flat repair, and the areas you actually serve, are what search engines, and a driver who needs tires now, reward with the click.</p>'},
        {"h2_html": "Show the brands, the price, and a <em>slot they can book</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A tire buyer wants two things before they commit: some idea of what it will cost and confidence you carry what fits their car. Someone on the shoulder with a flat is on a phone, not a desktop, and they are not going to read three paragraphs. The site has to load fast, put a tap-to-call button and your service area in front of them right away for the same-day flat, and for the driver who is just pricing a set, show the brands and sizes you carry and make getting a quote or booking a mounting appointment a couple of taps, not a phone call they have to remember to make. A slow site that hides the phone number and shows no prices sends the buyer back to the search results and the shop below you.</p>'},
        {"h2_html": "The calls are <em>yours</em>, permanently",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you put into a pay-per-lead service or a national tire portal disappears the day you stop paying, and the customer was never really yours anyway. A website you own keeps ranking, keeps capturing calls and bookings, and keeps compounding in value for as long as it exists, and it is registered to you, not a platform that can drop you or route your buyer to a chain. The site plugs into the same CRM that follows up on every lead it captures and the answering service that answers the calls it drives, so nothing it earns you slips away.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A search for tires finds <em>you</em>, not a directory",
        "body_html": "A driver a couple of towns over is down to the wear bars and searches for tires near them on their phone. Instead of a national portal that would route the sale to a chain, they find your site ranking for that town, with the brands and sizes you carry laid out, a sense of what a set runs, and a booking form a couple of taps down the page. They can see you have what fits their car, so they book a mounting appointment with you directly, with no per-lead fee and no middleman anywhere in the chain. You wake up to the set already sold and on the calendar. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big tire sites and directories?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the local tire and flat-repair searches a national portal has no reason to target well, which is exactly where a local shop can win."),
        ("How is this different from paying for leads or a tire portal?",
         "A pay-per-lead service or a national portal rents you a customer it also sends to a chain or your competitors, and it stops the day you stop paying. A website you own captures calls and bookings that are yours alone and keeps working long after it is built, without a fee coming out of every sale."),
        ("Do I need to show prices on the site?",
         "You do not have to post a full price list, but giving a driver some sense of what a set runs and showing the brands and sizes you carry is what turns a searcher into a booking. People are pricing tires, and a site that helps them do that beats one that makes them call to find out."),
        ("Do people really book tires online?",
         "Plenty do, especially for a planned set rather than a roadside flat. When someone can see the brands you carry and pick a mounting slot without a phone call, many will, and the ones with a same-day flat still get a tap-to-call button at the top."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks; broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for tire shops"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-tire-shops.html", "Staying visible in your service area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and tire portals taking your calls, whether you work with us or not. No credit card, never a call center.",
},
]
