"""Colony page specs for WINDOW CLEANING (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a window-cleaning-business owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, window-cleaning-specific substance (the generator owns
shell, schema, events, keyword placement). Never the plumber, pressure-washing, or home-services
content reworded. Same honesty rules as the money specs: no invented stats, prices, or clients;
hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans, $1,500 one-time site)
ever appear, and never an invented clean price; no em/en dashes anywhere; the word "leak" never
appears as a metaphor. Ethics: the AI receptionist does scheduling and intake ONLY, never a firm
price sight unseen.

The trade's reality, and what keeps each page distinct from the money pages and from the pressure
-washing colony next door: window cleaning is RECURRING glass work (streak-free interior and
exterior, screens, tracks, gutters as add-ons) run on a route cadence (quarterly, twice-a-year,
weekly and monthly storefront routes), so REBOOKING and recurring residential plus COMMERCIAL
storefront contracts ARE the whole model. It is NOT the pressure-washer's dramatic one-off before
-and-after mud reveal: clean glass barely reads in a photo, so window cleaning sells on
reliability, recurring plans, and reviews, not a transformation gallery. The website-cost page
therefore leads with the window-cleaning site job (easy recurring booking, residential plus
commercial plans, service area, reviews, "window cleaning near me"), never the generic template
-vs-custom-vs-agency lecture and never the before-and-after gallery angle.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 window-cleaning-website-cost                        (cost)    -> websites-seo-for-window-cleaning
  2 window-cleaning-answering-service-cost              (cost)    -> ai-receptionist-for-window-cleaning
  3 is-a-crm-worth-it-for-a-window-cleaning-business    (cost)    -> crm-for-window-cleaning
  4 why-window-cleaners-miss-calls                       (problem) -> ai-receptionist-for-window-cleaning
  5 why-window-cleaning-customers-dont-rebook            (problem) -> crm-for-window-cleaning
  6 how-do-window-cleaners-get-more-customers            (how-to)  -> marketing-for-window-cleaning
"""

TOPICS = [
# ============ How Much Does a Window Cleaning Website Cost? (cost -> websites-seo) ============
{
    "slug": "window-cleaning-website-cost",
    "h1": "How Much Does a Window Cleaning Website Cost?",
    "title": "How Much Does a Window Cleaning Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A window cleaning website ranges from a cheap template to a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A window cleaning website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more is whether it makes booking a recurring plan easy, shows residential and commercial work, and ranks for window cleaning near me. Top Shelf builds a custom site for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a window cleaning site actually <em>has to do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A window cleaning website has one job, and it is not to win a design award. It is to take a homeowner tired of spotted glass, or a shop manager tired of fingerprints on the front door, and make it easy for them to ask you for a price and, ideally, put themselves on a regular schedule. Before you think about what to spend, know what you are actually paying for, because a site that cannot do these things is not cheap, it is wasted money no matter the price tag.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Dead-simple booking and quote requests. Most of these searches happen on a phone, so a visitor should be able to say whether it is a house or a storefront, how many windows and how often they want it, and ask for a price in under a minute.</li><li>Both sides of the business, shown clearly. Inside-and-out home cleans, recurring residential plans, and storefront or office routes, plus add-ons like screens, tracks, and gutters, so a caller sees at a glance that you do their specific job and that you offer regular service.</li><li>Reviews and a clear service area up front. Clean glass barely reads in a photo, so window cleaning does not sell on a dramatic before-and-after the way some trades do. It sells on trust: recent reviews, the towns you cover, and looking like the reliable local name someone wants on a standing schedule.</li><li>Pages built to rank for window cleaning near me and the neighborhoods you serve, so the person searching in a hurry finds you instead of a national directory.</li></ul>'},
        {"h2_html": "What a window cleaning site should actually <em>cost you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Once the site does those things, the price question gets simpler. A do-it-yourself builder is cheap every month, but you do the work and it is rarely built to rank or to turn a visitor into a booked plan. A one-time custom build costs more up front and is yours to keep, though a site alone does little if nobody is doing the ongoing SEO to get it found. An agency that bundles the build with ongoing SEO carries a monthly cost, and that is where most of the long-term value lives.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it plain. A custom site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that gets it ranking is handled for you. There is no setup fee either way. Before you sign with anyone, ask who owns the site, what a change costs, and whether you keep it if you leave. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that books the recurring plan",
    "bridge_text": "A window cleaning website is only worth the accounts it brings in. Ours makes booking a recurring plan easy, shows your residential and commercial work, and ranks for the towns you cover, so the call is yours instead of a directory's.",
    "bridge_slug": "websites-seo-for-window-cleaning",
    "bridge_label": "Websites & SEO for window cleaning",
    "faqs": [
        ("Is a cheap template site good enough to start with?",
         "It can get you online, but a template you fill in yourself rarely ranks, and it usually buries the easy booking and the reviews that actually turn a window cleaning visitor into a recurring account. If a site is not getting found or turning visitors into booked plans, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep. On a monthly plan the site is built for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "window_cleaning", "trade_plural": "window cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== What Does a Window Cleaning Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "window-cleaning-answering-service-cost",
    "h1": "What Does a Window Cleaning Answering Service Cost?",
    "title": "What Does a Window Cleaning Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for window cleaning bill per call or minute. Top Shelf's AI receptionist answers 24/7 and books the recurring plan, $899/mo Signature.",
    "answer": "Traditional answering services for window cleaning companies usually bill per call, per minute, or a monthly retainer, so a busy stretch gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call and books the estimate or the recurring plan comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good stretch turns into a big bill. A window cleaner also gets estimate and scheduling calls at the worst moments to answer, while the crew is up a ladder or working down a route, and the calls cluster in spring and the weeks before the holidays when everyone notices their glass at once. It is worth knowing the common models before you sign one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy week of homeowners and storefronts pricing a clean runs the bill straight up.</li><li>Per-minute pricing: you pay for talk time, so a caller asking about a whole-house inside-and-out with screens and tracks costs more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of calls, and you pay extra past it, usually right when the season picks up and you blow through the bucket.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner or a shop manager pricing a clean is calling a few companies and books whoever picks up and sounds professional. The real cost of no coverage is not a monthly fee, it is the account that went to the company that answered while your crew was mid-squeegee. And the prize is rarely one clean. It is a standing plan, a quarterly home or a weekly storefront, that renews on its own for years, so a single missed call can be a whole account lost. A generic call center reading a script cannot tell an inside-and-out house clean from a monthly storefront route, so you can pay for coverage and still hand the caller a poor first impression.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, asks whether it is a home or a storefront, how many windows and stories, and how often they want it, then books the estimate or the recurring visit onto your calendar. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running, and it does the scheduling and intake only, never a firm price sight unseen. One storefront route you would have lost while your hands were full can be worth more than the plan costs, and everything it books after that is on top.</p>'}],
    "bridge_h2": "Answer every account without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7 even while your crew is up a ladder, tells a one-time clean from a standing route, and books it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-window-cleaning",
    "bridge_label": "AI receptionist for window cleaning",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the recurring account it books instead of losing to voicemail while your crew is up a ladder."),
        ("Does it cost extra for nights, weekends, or the busy season?",
         "No. It answers 24/7 as part of the plan, including the spring rush and the pre-holiday weeks when every homeowner notices their glass at once, with no after-hours surcharge and no overage for a heavy month.")],
    "trade_slug": "window_cleaning", "trade_plural": "window cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ========= Is a CRM Worth It for a Window Cleaning Business? (cost -> crm) =========
{
    "slug": "is-a-crm-worth-it-for-a-window-cleaning-business",
    "h1": "Is a CRM Worth It for a Window Cleaning Business?",
    "title": "Is a CRM Worth It for a Window Cleaning Business? | Top Shelf Business Solutions",
    "meta_desc": "For most window cleaning companies a CRM pays for itself by turning one-time cleans into standing plans. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most window cleaning companies, yes. Glass gets dirty again on a schedule, so a CRM pays for itself the first time it turns a one-time clean into a standing plan or rebooks a past customer. It only stops being worth it if you never follow up. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a window cleaning company when you have more past customers and recurring accounts than you can keep in your head, which is most crews past their first year. It is not worth it if you are one person doing a handful of cleans a week and genuinely calling everyone back, though that rarely lasts as you grow. The honest test is simple: how many homes did you clean last spring that have not heard from you since, and how many storefronts are you cleaning on a handshake with no set rotation?</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Those two questions point straight at the money a CRM is built to recover, and window cleaning has an unusual amount of it. Unlike a repair that is done and forgotten, glass starts spotting and filming the moment you leave, so every customer you have ever cleaned for is a re-clean waiting to be booked, and every storefront is a standing route waiting to be set. That is what makes the worth-it math lean so hard toward yes in this trade.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a window cleaner is not the software, it is the work that stops slipping away. A homeowner sitting on a quote, a family whose windows you did two springs ago, a storefront that should be on a monthly rotation: each one is a job you have already half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open quote on a schedule, so a homeowner comparing a few companies keeps hearing from you while the others go quiet.</li><li>It prompts you to offer a plan when someone books a single clean, and fires the residential reminders, a quarterly, a twice-a-year, a touch-up before the holidays, so the cleans that always come due again turn into standing bookings.</li><li>It holds your commercial and storefront accounts and their cadence, and lets you see them by area, so the weekly storefront and the monthly office stay on a dense route and get invoiced instead of slipping.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: turn one clean into a standing plan, or rebook one past customer, and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Turn one clean into a standing plan",
    "bridge_text": "The glass always spots again, so every home you have cleaned is a re-clean waiting to be booked and every storefront is a route waiting to be set. A CRM follows up on every quote and reminds every past customer for you, so they stay on your schedule instead of searching Google again.",
    "bridge_slug": "crm-for-window-cleaning",
    "bridge_label": "CRM for window cleaning",
    "faqs": [
        ("Is a CRM overkill for a small window cleaning business?",
         "Not usually. Even a one or two person crew cleans more homes and storefronts in a season than anyone can track by memory, and every one of those windows gets dirty again on a schedule. The point is not size, it is whether follow-up is falling through. If quotes go cold and past customers forget your name, a CRM earns its keep."),
        ("How is a CRM different from keeping numbers in my phone?",
         "A phone full of contacts does not follow up on a quote, does not remember which house is due for its quarterly, and does not track a storefront rotation. A CRM does all of that on a schedule, so the repeat cleans and the recurring accounts show up instead of depending on you to remember.")],
    "trade_slug": "window_cleaning", "trade_plural": "window cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do Window Cleaners Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-window-cleaners-miss-calls",
    "h1": "Why Do Window Cleaners Miss So Many Calls?",
    "title": "Why Do Window Cleaners Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Window cleaners miss calls because they ring while the crew is up a ladder or mid-squeegee. A shopper does not leave a voicemail, they call the next company.",
    "answer": "Window cleaners miss calls because they come while your hands are full, up a ladder, mid-squeegee, or driving between stops on the route, and a homeowner or manager shopping for a clean does not leave a voicemail. They call the next company on their list. The fix is not working harder, it is making sure every estimate call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Window cleaning is a hands-full trade. When the phone rings you are usually up a ladder with both hands on a pole, running a squeegee down a storefront pane, working a scrubber through a track, or driving between the stops on the day route, and none of those are moments you can stop and take a call. The busier you are, the more calls you miss, which means your best weeks are also the ones where the most work slips away. It is not a discipline problem. One crew cannot clean the glass in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for someone shopping around it is not one. A homeowner who just noticed spotted windows, or a shop manager tired of fingerprints on the front door, is not loyal to anyone yet. They found a few companies on Google, they are dialing down the list, and they book the first one that answers and sounds professional. They will not leave a message and wait. By the time you check your phone, the job is already gone.</p>'},
        {"h2_html": "A missed call is a standing account that <em>signs with someone else</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. In most trades a missed call is one lost job. In window cleaning the caller often wants regular service, a quarterly home, a weekly or monthly storefront, so the miss is not one clean, it is a standing account that renews on its own for years, handed to whichever company happened to be free to answer. That is the most expensive kind of miss there is, and it is invisible, because you never knew the call came in.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and knows the trade. A voicemail box cannot ask a question, and a generic call center does not know an inside-and-out house clean from a monthly storefront route, or why a three-story home with hard-to-reach glass is a different quote than a single-story ranch. What actually works is something that answers on the first ring, asks whether it is a home or a storefront, how many windows and stories, and how often they want it, then books the estimate or the recurring visit onto your calendar, all as scheduling and intake, never a firm price sight unseen. The account gets captured instead of lost, even when both your hands are on the glass.</p>'}],
    "bridge_h2": "Stop losing standing accounts to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, even while your crew is up a ladder, asks whether it is a home or a storefront route, and books it or flags it to you, so the account never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-window-cleaning",
    "bridge_label": "AI receptionist for window cleaning",
    "faqs": [
        ("Would a customer rather reach a real person?",
         "A homeowner or manager pricing a clean mostly needs to know a real company is handling it and someone will come give a price, and a steady voice that captures the address, the windows, and how often they want it beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the details, and hands the job to you to quote."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are up a ladder, mid-squeegee, or already on another call, which is most of the day. Something that always answers and gathers the details is what catches the calls a forward would still miss.")],
    "trade_slug": "window_cleaning", "trade_plural": "window cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Don't My Window Cleaning Customers Rebook? (problem -> crm) ============
{
    "slug": "why-window-cleaning-customers-dont-rebook",
    "h1": "Why Don't My Window Cleaning Customers Rebook?",
    "title": "Why Don't My Window Cleaning Customers Rebook? | Top Shelf Business Solutions",
    "meta_desc": "Most window cleaning customers don't rebook because nobody reminded them, not because they were unhappy. The glass spots up again and they forget your name.",
    "answer": "Most window cleaning customers do not rebook because nobody reminded them, not because they were unhappy. The glass spots up again months later, they mean to call, they forget your name, and they search and hire whoever turns up first. A happy one-time customer who never hears from you is not loyal, they are just unbooked.",
    "sections": [
        {"h2_html": "They were happy, they just <em>forgot you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to assume a customer who never rebooked was unhappy, so you write them off and chase new ones. But most of the time they loved the spotless glass and simply moved on with their life. Three or four months later the rain spots, the dust film, and the fingerprints are back, and they think it is time to get the windows done again. Then they cannot remember the name of the company that did them last time. So they do what everyone does, they search, and they hire whoever turns up first, which is rarely the crew that already did a great job for them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is the quiet reality of this trade: the customer was never lost on quality, they were lost to forgetting. A happy one-time customer who never hears from you again is not loyal, they are just unbooked, and every one of them is a standing plan you already earned and never asked for. The company that gets the rebook is not the best cleaner, it is the one that reached out before the customer went searching.</p>'},
        {"h2_html": "Why the rebooking <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Window cleaners do not skip the rebook because they are lazy. They skip it because the day fills up. You finish a house, drive to the next stop, squeeze in an estimate, and by evening the customer you cleaned for in the spring is out of sight and out of mind until they happen to call, if they ever do. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest customers coming due anyway.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system tracking which homes are due for their next quarterly and which storefronts are overdue on the route.</li><li>The reminder depends on you remembering months later, so it competes with the actual cleaning and loses.</li><li>By the time the customer thinks of it themselves, they have forgotten your name and booked whoever came up in search.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and it just runs. When every past customer gets a friendly reminder at the moment the glass is spotting up again, written to sound like you, and every recurring account sits on a cadence that books the next visit before the last one fades, the rebooking that used to depend on luck happens on its own, and one-time cleans quietly become standing plans.</p>'}],
    "bridge_h2": "Bring every past customer back on schedule",
    "bridge_text": "A CRM remembers who is due and reminds every past customer for you at the moment the glass is spotting up again, so a one-time clean becomes a standing plan and your customer list turns into recurring revenue instead of names you forgot.",
    "bridge_slug": "crm-for-window-cleaning",
    "bridge_label": "CRM for window cleaning",
    "faqs": [
        ("How do I get window cleaning customers to rebook?",
         "Reach out before they go searching. A friendly reminder a few months out, timed to when the glass is spotting up again, catches most of them while the memory of your good work is still fresh, and offering a standing plan at the first clean is what turns a one-off into a schedule. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does an automated reminder feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly note reads as attentive, not spammy, and most customers appreciate the nudge because they meant to get the windows done again and forgot. You can always jump in and message anyone directly.")],
    "trade_slug": "window_cleaning", "trade_plural": "window cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======= How Do Window Cleaners Get More Customers? (how-to -> marketing) =======
{
    "slug": "how-do-window-cleaners-get-more-customers",
    "h1": "How Do Window Cleaners Get More Customers?",
    "title": "How Do Window Cleaners Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Window cleaners get more customers by ranking in the map pack with recent reviews and turning each new customer into a standing plan and referrals.",
    "answer": "Window cleaners get more customers by being the reliable name that shows up in the map pack when someone searches window cleaning near them. Clean glass does not sell on a dramatic photo, so reviews and a complete Google profile do the convincing, and the recurring model does the rest, turning each new customer into a standing plan and referrals.",
    "sections": [
        {"h2_html": "Reviews and the map pack are the <em>engine</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone wants their windows done, the first thing they see on Google is not a website. It is the map pack, the three local listings with star ratings that sit at the top when they search for window cleaning near them. Most people choose from those three without scrolling. Getting more customers starts with being one of them, and in this trade the thing that puts you there and wins the click is reviews. Clean glass does not sell on a dramatic before-and-after the way some trades do, a spotless window barely reads in a photo, so a steady stream of recent, genuine reviews is what tells a stranger you are reliable and worth trusting on a schedule.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A profile that is verified, complete, and stacked with fresh reviews looks like the obvious choice next to one with two old photos and no recent activity. The mistake is doing great work for years and never asking anyone to leave a review, because a happy customer who was never asked is trust you earned and threw away. Ask every satisfied customer right when the glass is gleaming and they are standing there pleased, make it one tap, and the reviews build on their own, which is what quietly moves you up the map.</p>'},
        {"h2_html": "Cover your towns, land recurring accounts, and <em>rebook what you have</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Chasing a whole metro is expensive and sends you calls an hour outside your range. Focusing on the specific towns and neighborhoods you serve, with a profile, reviews, and content built around those areas, is what puts you in the map pack where you can actually take the work, and it turns into a route of jobs close together instead of a day lost to driving. Landing one storefront on a busy block is also a door to the row beside it, and one home on a street where the neighbors can see the difference tends to bring the neighbors.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The real multiplier, though, is that window cleaning is a recurring business, so growth is not only new customers, it is keeping the ones you win. The glass always spots again, so every customer you clean for is a standing plan waiting to be set, and a reliable crew that shows up on schedule earns the referrals that cost nothing. Getting more customers is the visible side of this, your Google profile, your reviews, and your local presence, while the website that makes booking easy and the follow-up that turns one-time cleans into standing plans finish the job.</p>'}],
    "bridge_h2": "Be the window cleaner they can already trust",
    "bridge_text": "Most window cleaning jobs start with a search and a glance at the map pack, and reviews decide the click. Keeping your Google profile active and stacked with recent reviews in the towns you serve is how you become the name a customer calls when the glass needs doing.",
    "bridge_slug": "marketing-for-window-cleaning",
    "bridge_label": "Marketing for window cleaning",
    "faqs": [
        ("What is the single best way to get more window cleaning customers?",
         "Be visible in the map pack with recent reviews front and center. That is where local searches start, and because clean glass does not sell on a photo, reviews are what convince a stranger you are reliable enough to put on a schedule. Everything else, your website and your follow-up, builds on being found there first."),
        ("Do before-and-after photos work for window cleaning?",
         "Less than you would think. A clean window barely reads in a picture next to the dramatic reveal some trades get, so photos do little of the selling here. Your Google reviews and a complete, active profile carry far more weight, because reliability, not a single image, is what someone is judging when they pick a window cleaner.")],
    "trade_slug": "window_cleaning", "trade_plural": "window cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
