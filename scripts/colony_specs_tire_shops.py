"""Colony page specs for TIRE SHOPS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a tire-shop owner would search, answered directly up top (the 40-60
word AEO answer), then two body sections, then a "the fix" bridge that funnels the page's
authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, tire-shop-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear; never a made-up tire price, always generic ("a set of four",
"what a set runs"); no em/en dashes anywhere; never "leak" as a metaphor (a tire "losing air" or
"going flat" instead). AI does scheduling/intake and answers stock/price questions per the shop's
own info only, never inventing a price or promising stock it was not given.

Auto hub, tire angle, distinct from repair (diagnosis), body (collision), and detailing (cosmetic):
a tire shop lives on a firehose of price-and-availability calls (do you have my size, how much for
four, can I come now), same-day flats and blowouts, quick services (mount/balance, rotation,
alignment, flat repair), a walk-in + appointment mix that slams the counter, fleet accounts, and
rebooking for rotations and the next set as the CRM engine, all swinging hard with the season.

Six questions, mixed cost / problem / how-to, across the four tire money pages:
  1 tire-shop-website-cost              (cost)     -> websites-seo-for-tire-shops
  2 tire-shop-answering-service-cost    (cost)     -> ai-receptionist-for-tire-shops
  3 is-a-crm-worth-it-for-a-tire-shop   (cost)     -> crm-for-tire-shops
  4 why-tire-shops-miss-calls           (problem)  -> ai-receptionist-for-tire-shops
  5 why-tire-customers-dont-return      (problem)  -> crm-for-tire-shops
  6 how-do-tire-shops-get-more-customers(how-to)   -> marketing-for-tire-shops
"""

TOPICS = [
# ==================== How Much Does a Tire Shop Website Cost? (cost -> websites-seo) ====================
{
    "slug": "tire-shop-website-cost",
    "h1": "How Much Does a Tire Shop Website Cost?",
    "title": "How Much Does a Tire Shop Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A tire shop website ranges from cheap templates to a custom build. What counts is whether it shows your brands, books the set, and ranks for tires near me.",
    "answer": "A tire shop website can run from a couple hundred dollars for a DIY template to several thousand for a custom build, but price matters less than whether it does the job: showing the brands you carry, taking a booking, and ranking for tires near me. Top Shelf builds one for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a tire shop site has to <em>actually do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before you compare quotes, it helps to know what a tire shop website is actually for, because a pretty brochure and a site that brings in sets of tires are different products with the same name. A tire buyer who lands on your page wants to know three things fast: do you carry my size, what does a set run, and can you get me in soon. A site that answers those turns a searcher into a booking, and one that hides them sends the buyer back to the results and the shop below you.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It shows the brands and sizes you carry, so a driver can see you have what fits their car before they ever call.</li><li>It lets them ask for a price or an out-the-door quote and book a mounting or a flat repair in a couple of taps, instead of a phone call they have to remember to make.</li><li>It loads fast and puts a tap-to-call button in front of the driver on the shoulder with a flat, who is on a phone, not a desktop.</li><li>It ranks for what people actually search when a tire goes, tires near me and cheap tires in your town, so the sale comes to you and not a directory.</li></ul>'},
        {"h2_html": "What that costs, and what you should <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Prices for a tire shop website swing widely because you are not all buying the same thing. A do-it-yourself template is cheap every month, but you build and maintain it, and it is rarely set up to rank or to show your inventory and take a booking. A custom build costs more up front and is yours to keep, but a site alone does little if nobody is doing the ongoing work to get it found. What you are really paying for is not the pages, it is whether the site ranks for the drivers near you and turns them into calls and booked appointments.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a tire site that books the set",
    "bridge_text": "A tire shop website is only worth the calls and bookings it brings in. Ours ranks for the drivers searching near you, shows the brands and sizes you carry, and turns a price shopper into a booked appointment instead of a lead a directory sells back to you.",
    "bridge_slug": "websites-seo-for-tire-shops",
    "bridge_label": "Websites & SEO for tire shops",
    "faqs": [
        ("Is a cheap template site good enough for a tire shop?",
         "It can get you online, but a template you fill in yourself is rarely built to rank, show your brands and sizes, or take a booking, and you do the upkeep. For a tire shop, a site a price shopper cannot get a quote or an appointment from is not much cheaper than no site at all, because the sale still goes to whoever made it easy."),
        ("Do I have to show tire prices on the site?",
         "You do not have to post a full price list, but giving a driver some sense of what a set runs and showing the brands and sizes you carry is what turns a searcher into a booking. People are pricing tires when they search, and a site that helps them do that beats one that makes them call to find out.")],
    "trade_slug": "tire_shops", "trade_plural": "tire shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ What Does a Tire Shop Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "tire-shop-answering-service-cost",
    "h1": "What Does a Tire Shop Answering Service Cost?",
    "title": "What Does a Tire Shop Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for tire shops often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for tire shops usually bill per call, per minute, or a retainer, so a busy season gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers 24/7, quotes the sizes and prices you set, and books the job, in the Signature plan at $899 a month flat with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy Saturday turns into a big bill. A tire shop gets a firehose of price-and-availability calls, do you have my size, what does a set of four run, can you get me in today, and a service that charges by the call or the minute climbs fastest exactly when the counter is slammed and the phone is ringing most. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a wave of price shoppers who never book still runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a caller reading a long size off the sidewall costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of calls, and you pay extra past it, usually right in your busy season.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a driver pricing a set of four calls three or four shops in a row and books the first one that picks up with a straight answer, so a missed call is a whole set gone to the shop down the road. But a generic call center reading a script cannot quote a size, cannot tell a rotation from an alignment, and does not know what you have in stock, so you can pay for coverage and still lose the sale to bad answers.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, gives the prices and stock answers you set, and books the mounting or the same-day flat, or flags anything that needs your eyes to your phone. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One set of four you would have lost while the crew had their hands full is usually worth more than the plan costs, and everything it books after that is on top. It only ever quotes the prices and stock you have given it, so it never promises a driver something you cannot deliver.</p>'}],
    "bridge_h2": "Answer every price shopper without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script and cannot quote a size, an AI receptionist answers every call 24/7, gives the price and stock you set, and books the set or the same-day flat, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-tire-shops",
    "bridge_label": "AI receptionist for tire shops",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service for a tire shop?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when your price-and-availability calls spike, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the set of four it books instead of losing to voicemail while the bays were full."),
        ("Can it really quote a price and tell a caller what is in stock?",
         "It gives the prices and out-the-door ranges you set for your common sizes and services, and tells the caller whether a size is one you normally stock or would order in. For anything that needs your eyes first, it takes the size and the vehicle, books the appointment, and texts you the details so you confirm the number. It never invents a price you did not give it.")],
    "trade_slug": "tire_shops", "trade_plural": "tire shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============== Is a CRM Worth It for a Tire Shop? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-tire-shop",
    "h1": "Is a CRM Worth It for a Tire Shop?",
    "title": "Is a CRM Worth It for a Tire Shop? | Top Shelf Business Solutions",
    "meta_desc": "For most tire shops a CRM pays for itself by rescuing one quoted set and bringing customers back for rotations. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most tire shops, yes. A CRM pays for itself the first time it wins back a set you quoted, or brings a past customer in for a rotation that turns into the next set. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a tire shop when you have more quoted sets and past customers than you can personally keep track of, which is nearly every shop that has been open a while. It is not worth it if you are a one-bay operation genuinely calling every quote back and remembering every customer who is due, though that rarely stays true as the customer list grows. The honest test is simple: how many sets did you quote last month that nobody followed up on, and how many past customers are overdue for a rotation and have not heard a word from you? Those are the sales a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a tire shop is not the software, it is the repeat work that stops slipping away. A driver sitting on a quote for four tires, a customer whose free rotations came with the set and have gone unused, a car whose tread is wearing to a date you can predict, a fleet account that buys in volume: each one is a sale you have already half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open quote on a schedule, so a buyer comparing shops keeps hearing from you while the others go quiet.</li><li>It fires rotation, alignment, and next-set reminders on the cadence you set, so recurring work comes back without you tracking a single date.</li><li>It keeps every customer, vehicle, size, and fleet account in one place instead of a stack of paper invoices and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one set of four you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your tire customers back to work",
    "bridge_text": "The sets you already quoted and the customers already in your bay are the cheapest sales you can get. A CRM follows up on every quote and reminds every customer when a rotation or the next set is due, so they call you instead of the shop that stayed in touch.",
    "bridge_slug": "crm-for-tire-shops",
    "bridge_label": "CRM for tire shops",
    "faqs": [
        ("Is a CRM overkill for a small tire shop?",
         "Not usually. Even a one or two bay shop quotes more sets and services more vehicles than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If quoted sets go cold and past customers forget your name before their tread runs out, a CRM earns its keep."),
        ("How is a CRM different from what my point-of-sale already stores?",
         "A point-of-sale records what was sold, but it does not follow up on a quote, does not remind a customer that a rotation or a new set is due, and does not tell you which fleet account has gone quiet. A CRM does all of that on a schedule, so the repeat work shows up instead of depending on you to remember.")],
    "trade_slug": "tire_shops", "trade_plural": "tire shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Why Do Tire Shops Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-tire-shops-miss-calls",
    "h1": "Why Do Tire Shops Miss So Many Calls?",
    "title": "Why Do Tire Shops Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Tire shops miss calls because they ring while the crew is mounting and balancing, and a price shopper who gets voicemail just dials the next shop.",
    "answer": "You miss calls because they ring while your crew is mounting, balancing, or pulling a wheel, and the counter is full of walk-ins, and a price shopper who reaches voicemail does not leave a message. They dial the next shop. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes when the <em>bays are full</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A tire shop is a hands-full, counter-full business. When the phone rings your techs are on the mounting machine, spinning a balancer, or pulling a wheel, and the front counter has a line of walk-ins, so there is often nobody free to pick up. The busier you are, the more calls roll past, which means your best days, a Saturday, the first cold snap, are also the ones where the most calls go unanswered. It is not a discipline problem. A crew cannot mount tires and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a tire buyer it is not one. Someone calling around to price a set or find a shop for a flat is not going to leave a message and wait for a call back. They hang up and dial the next shop on the list, and by the time you clear the bay and check the phone, the set is already sold somewhere else.</p>'},
        {"h2_html": "A price shopper is your most <em>losable customer</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal, but for a tire shop most of them are the expensive kind. A tire buyer has no loyalty yet and treats one shop like the next, so they call three or four in a row and book whoever answers with a straight price and an open slot. That means a single missed call is often a whole set of four, plus the alignment, the road-hazard warranty, and years of rotations and the next set that would have followed it, handed to the shop that happened to pick up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that answers every time and can actually help a tire caller. A voicemail box cannot quote a size, and a generic call center does not know what you stock. What works is something that answers on the first ring, tells the caller what you have in stock and what you set the price at, books the mounting or gets a same-day flat in today, and flags anything that needs your eyes to your phone, so the call is captured instead of lost while your crew had their hands full.</p>'}],
    "bridge_h2": "Stop sending tire buyers to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, even when every bay is full, tells the caller what you have in stock and the price you set, and books the set or the same-day flat, so the sale never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-tire-shops",
    "bridge_label": "AI receptionist for tire shops",
    "faqs": [
        ("Would a tire customer rather reach a real person?",
         "What a driver pricing a set or facing a flat wants most is a straight answer and a slot, and a call that gets picked up and handled beats a voicemail box every time. The AI receptionist is upfront about what it is, gives the price and stock answers you set, and hands anything that needs a human straight to you."),
        ("Can I just forward the shop phone to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are under a car, on the mounting machine, or already helping the customer at the counter. Something that always answers, quotes, and books is what catches the calls a forward would still miss.")],
    "trade_slug": "tire_shops", "trade_plural": "tire shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Why Don't My Tire Customers Come Back? (problem -> crm) ============
{
    "slug": "why-tire-customers-dont-return",
    "h1": "Why Don't My Tire Customers Come Back?",
    "title": "Why Don't My Tire Customers Come Back? | Top Shelf Business Solutions",
    "meta_desc": "Tire customers do not come back because nothing reminds them a rotation or the next set is due, so they search again and buy from whoever shows up.",
    "answer": "Usually not because they were unhappy, but because nothing reminded them. You sold the set, they drove off, and no one nudged them for the rotation or the next set, so when the tread finally went they searched again and bought from whoever showed up. A returning customer is usually just one reminder away.",
    "sections": [
        {"h2_html": "They did not leave, they just <em>drifted</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A tire customer who does not come back is usually not unhappy, they simply have no reason to think about tires until one goes flat or the tread is finally gone, and that can be years after the last set. The free rotations you bundled with that set go unused because nobody reminded them to come in. The alignment you would have caught never gets checked. And when a tire finally does go, they do not automatically remember you, they pull out a phone and search, and the relationship you earned is suddenly up for grabs against every other shop in town.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The shop that gets the next set is usually not the cheapest, it is the one that stayed in touch: a note that a rotation is due, a heads-up that the tread is getting low before the customer even notices. That light, well-timed nudge is what keeps a past customer yours, and it is exactly the thing there is no time for when the counter is three deep.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Tire shops do not skip follow-up because they do not care. They skip it because you cannot possibly remember when a few thousand past customers are each due for a rotation or a new set, and the day fills up with the cars in front of you. Doing it from memory means it only happens when things are slow, which is exactly when you have the fewest customers to bring back.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system tracking who is due for a rotation, whose tread is near the end, or which quoted set went cold.</li><li>The follow-up depends on someone at the counter remembering, so it competes with the walk-in line and loses.</li><li>By the time a customer notices a bald tire, they have already searched and booked whoever showed up first.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not an effort problem, and it is the kind of thing you set up once and then it runs. When every customer gets rotation, tread, and next-set reminders on a cadence you choose, and fleet accounts are reached on a schedule instead of waiting for a bad tire, the repeat work you already earned stops drifting to the shop that happened to be closest that day.</p>'}],
    "bridge_h2": "Bring every tire customer back around",
    "bridge_text": "A CRM remembers when every customer is due for a rotation, an alignment, or a new set, and reaches out for you before they start shopping, so the repeat work and the next set come back to you instead of the shop that happened to be closest that day.",
    "bridge_slug": "crm-for-tire-shops",
    "bridge_label": "CRM for tire shops",
    "faqs": [
        ("How do I know when a tire customer is due to come back?",
         "You set the cadence, a rotation and balance every few thousand miles, a tread heads-up as a set wears toward the end, an alignment or a road-hazard check on its own timing, and the reminders go out automatically off each customer record, so you are not tracking any of it by hand."),
        ("Will reminders annoy my customers?",
         "Not when they are useful and sent at a sensible pace. A short note that a rotation is due or that the tread is getting low reads as a shop looking out for them, not as spam, and most drivers are glad for the heads-up because they were not keeping track themselves. You can always jump in and reach anyone directly.")],
    "trade_slug": "tire_shops", "trade_plural": "tire shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ======== How Do Tire Shops Get More Customers? (how-to -> marketing) ========
{
    "slug": "how-do-tire-shops-get-more-customers",
    "h1": "How Do Tire Shops Get More Customers?",
    "title": "How Do Tire Shops Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Tire shops get more customers by being first in the Google map pack the moment a tire goes flat or the tread wears out, with reviews and seasonal visibility.",
    "answer": "Get found first in the moment a driver needs tires, which is sudden, local, and seasonal. That means an active Google Business Profile in the map pack, reviews that mention fair prices and fast service, and visibility right before the seasonal waves, so when a tire goes your name is the one they call.",
    "sections": [
        {"h2_html": "Tire demand is <em>sudden, local, and seasonal</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody shops for a tire shop weeks ahead. Demand shows up the instant a tire goes flat, a blowout leaves someone on the shoulder, or a driver finally notices the tread is down to the bars, and it is intensely local, because they want a shop they can reach today. Tires are also the one auto trade with a real calendar to them: the first cold, wet morning sends everyone who has been driving on worn tires searching at once, and spring, with road trips and inspections ahead, brings another wave. The way to get more customers is to be the shop that is easy to find first in those moments, in your own area.</p>'},
        {"h2_html": "Be the shop they can <em>see and trust</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone searches for tires near them, the map pack, those three local listings with the star ratings, is the first thing they see, above the websites and the ads. A tire buyer has usually been burned by a surprise charge or a shop that kept them waiting all afternoon, so they read the reviews for two things: honest, out-the-door pricing and how fast the shop got them in and out. A profile full of recent reviews that say exactly that, next to current hours and photos of the shop, quietly beats one that has sat untouched for a year.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting there is a matter of keeping the profile verified, complete, and active, focusing on the towns you actually serve, and building a steady flow of real reviews, then timing your visibility to the seasonal waves so you are already in front of drivers before the rush. That is the public-facing side of getting customers, aimed at drivers who are not yours yet; the private follow-up to the people already in your database is the CRM. What no one can honestly promise is a specific spot on the map, because Google decides that, but those levers are the ones that move it, and a free audit will show you where you stand today.</p>'}],
    "bridge_h2": "Get seen the moment a tire goes",
    "bridge_text": "Most tire customers start with a search the instant a tire goes flat or the tread is gone. Keeping your Google profile active, well-reviewed, and first in the map pack for the towns you serve is how you are the shop they call, not the one that let its listing go stale.",
    "bridge_slug": "marketing-for-tire-shops",
    "bridge_label": "Marketing for tire shops",
    "faqs": [
        ("What actually gets a tire shop into the map pack?",
         "A Google Business Profile that is verified, complete, and active, with accurate hours, services, and the brands and sizes you carry, plus a steady stream of recent, genuine reviews and how close you are to the searcher. Keeping it active and well-reviewed is what lifts a shop over one whose listing has gone stale."),
        ("Should I run ads, or fix my Google profile first?",
         "For most tire shops the profile and reviews come first, because the map pack is free to appear in and it is the first thing a nearby searcher sees. Ads can add reach on top once the profile is earning its keep, but paying to send traffic to a stale, thin listing tends to waste the spend.")],
    "trade_slug": "tire_shops", "trade_plural": "tire shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
]
