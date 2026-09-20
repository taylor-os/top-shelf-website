"""Colony page specs for POOL SERVICE (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a pool-service-business owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, pool-service-specific substance (the generator owns
shell, schema, events, keyword placement). Same honesty rules as the money specs: no invented
stats, prices, or clients; hedge instead of overpromise; only the real prices ($299/$899 plans,
$1,500 one-time site) ever appear and no pool prices are invented; no em/en dashes anywhere;
never "leak" as a money metaphor (a literal pool or equipment water leak is fine). The AI
receptionist does scheduling and intake only, it never diagnoses the pool.

The pool-service reality drives every page and no two converge: the recurring weekly and monthly
maintenance route is the revenue base, so retention and route density matter more than one-off
jobs; open and close seasons spike demand; pump, heater, and leak repairs sit on top of
maintenance; the tech is on a route all day; and a canceled recurring account is the biggest
single loss, which is why why-customers-cancel is the CRM retention story.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 pool-service-website-cost                       (cost)     -> websites-seo-for-pool-service
  2 pool-service-answering-service-cost             (cost)     -> ai-receptionist-for-pool-service
  3 is-a-crm-worth-it-for-a-pool-service            (cost)     -> crm-for-pool-service
  4 why-pool-service-companies-miss-calls           (problem)  -> ai-receptionist-for-pool-service
  5 why-pool-service-customers-cancel               (problem)  -> crm-for-pool-service
  6 how-do-pool-service-companies-get-more-customers (how-to)  -> marketing-for-pool-service
"""

TOPICS = [
# ============ How Much Does a Pool Service Website Cost? (cost -> websites-seo) ============
{
    "slug": "pool-service-website-cost",
    "h1": "How Much Does a Pool Service Website Cost?",
    "title": "How Much Does a Pool Service Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A pool service website runs from a cheap template to a few thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A pool service website can run from a couple hundred dollars for a do-it-yourself template to several thousand for a custom build. What matters more than the price is whether it ranks for pool service near me and turns a homeowner into a recurring account. Top Shelf builds a custom five page site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What a pool service site actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A pool service website is not a brochure, it is the front door to your route. The prize is not a single repair, it is a recurring account that pays every month, so the site has to be built to sign one up. When a homeowner lands on it, they should be able to start weekly service in a couple of taps, see the neighborhoods you cover, and get a sense of your plans, all before they scroll. A site that only lists a phone number and a photo gallery leaves your most valuable customer, the weekly-route one, to work it out for themselves.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It has to rank for what people actually type when they want their pool handled: pool service near me, weekly pool cleaning, and green pool cleanup in your city.</li><li>It has to make signing up for recurring service the obvious next step, not buried behind a generic contact form.</li><li>It has to show your service area and your plans, so a homeowner knows you cover them and roughly what to expect.</li><li>It has to put your reviews and a tap-to-call button in front of a visitor fast, because trust and speed are what win the call.</li></ul>'},
        {"h2_html": "What drives the <em>price</em>, and what to pay for",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Prices swing because a cheap template you fill in yourself and a custom site built to rank and capture recurring signups are different products with the same name. A do-it-yourself builder is cheap monthly, but you do the work and it rarely ranks. A one-time custom build is yours to keep, but it does little without ongoing SEO behind it. An agency plan bundles the build with the SEO that actually gets it found, which is where most of the long-term value lives. Before you sign anything, ask who owns the site, what a change costs, and whether you keep it if you leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that gets it ranking for your towns is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that signs up recurring customers",
    "bridge_text": "A pool service website is only worth the recurring accounts it brings in. Ours is built to rank for the towns you cover and turn a pool service near me search into a signed-up route customer, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-pool-service",
    "bridge_label": "Websites & SEO for pool service companies",
    "faqs": [
        ("Do I need a website if most of my work is on a route?",
         "Yes. New route customers still find you by searching, and a site is where a homeowner signs up for recurring service, sees your plans and service area, and reads your reviews before they trust you with their pool. Word of mouth fills some of the route, but the search traffic is where the growth is."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "pool_service", "trade_plural": "pool service companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== What Does a Pool Service Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "pool-service-answering-service-cost",
    "h1": "What Does a Pool Service Answering Service Cost?",
    "title": "What Does a Pool Service Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for pool companies often bill per call or minute, which climbs in season. Top Shelf includes a 24/7 AI receptionist in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for pool companies usually bill per call, per minute, or a monthly retainer, so a busy open season gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call 24/7 and books the job comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good stretch turns into a big bill. A pool company also gets its heaviest call volume at predictable spikes: the first warm week when everyone wants their pool opened, the close-down rush in fall, and any heat wave that pushes equipment into overtime. Those are exactly the times a per-minute or after-hours meter runs hottest. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so open season and a wave of tire-kickers run up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty homeowner or a slow operator costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner who wants weekly service, or is standing over a green pool before a weekend party, does not leave a voicemail. They call the next company on the list. The real cost of no coverage is not a monthly fee, it is the recurring account or the equipment repair that went to the shop that picked up. But a generic call center reading a script cannot tell a routine weekly-service inquiry from a failing pump or heater, so you can pay for coverage and still get bad triage.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, asks the right questions, and books the routine work or flags an urgent equipment problem to your phone. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One recurring account it books over a season can be worth well more than the plan costs, and everything it catches after that is on top. It handles scheduling and intake only, it does not diagnose the pool, and it hands anything that needs your judgment straight to you.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, tells a routine weekly-service request from an equipment problem, and books it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-pool-service",
    "bridge_label": "AI receptionist for pool service companies",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs right when open season and heat waves flood your phone, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the recurring account it books instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or the busy season?",
         "No. It answers 24/7 as part of the plan, including the weekend green-pool call and the first warm week when everyone wants their pool opened at once, with no after-hours or overage surcharge.")],
    "trade_slug": "pool_service", "trade_plural": "pool service companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Is a CRM Worth It for a Pool Service Company? (cost -> crm) ============
{
    "slug": "is-a-crm-worth-it-for-a-pool-service",
    "h1": "Is a CRM Worth It for a Pool Service Company?",
    "title": "Is a CRM Worth It for a Pool Service Company? | Top Shelf Business Solutions",
    "meta_desc": "For most pool companies a CRM pays for itself by holding a route customer, closing a repair quote, or reviving a seasonal one. Included in Top Shelf Signature at $899/mo.",
    "answer": "For most pool service companies, yes. A CRM pays for itself the first time it holds a route customer who would have drifted off, closes an equipment quote a homeowner was sitting on, or brings a seasonal customer back for a spring open. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a pool service company when you have more route customers, open repair quotes, and past clients than you can personally keep track of, which is most established shops. It is not worth it if you clean a handful of pools and genuinely stay in touch with every one, though that rarely stays true as the route grows. The honest test is simple: how many equipment or repair quotes did you send in the last month that you never chased, and how many seasonal or part-year customers have not heard from you since last year? Those are the jobs and accounts a CRM is built to recover, and for a route business they add up to recurring revenue, not a one-time ticket.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a pool company is not the software, it is the recurring revenue that stops slipping through. A homeowner sitting on a heater or pump quote, a customer who dropped off last winter, a route account that has gone quiet: each one is revenue you have already half-earned and are one reminder away from keeping.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open repair and equipment quote on a schedule, so the homeowner comparing bids keeps hearing from you.</li><li>It reactivates seasonal and lapsed customers before open season, so the people you served once come back instead of calling someone else.</li><li>It fires reminders for recurring maintenance and equipment checks, so the route work comes back without you tracking dates.</li><li>It keeps your whole customer list, pool profiles, and service history in one place instead of a truck full of paper and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is simple: hold onto or recover one recurring account and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your route and your list to work",
    "bridge_text": "The route customers, repair quotes, and past clients you already have are the cheapest revenue you can get. A CRM works every one for you, so they stay on the route and come back each season instead of drifting to another company.",
    "bridge_slug": "crm-for-pool-service",
    "bridge_label": "CRM for pool service companies",
    "faqs": [
        ("Is a CRM overkill for a small pool route?",
         "Not usually. Even a modest route is more customers, repair quotes, and renewal dates than anyone tracks by memory, and the recurring accounts are exactly the ones you cannot afford to let slip. The point is not size, it is whether follow-up and reactivation are falling through."),
        ("How is a CRM different from keeping customers in my phone?",
         "A phone full of contacts does not chase a repair quote, does not remind a seasonal customer it is time to reopen, and does not tell you which route account has gone quiet. A CRM does all of that on a schedule, so the repeat and recurring work shows up instead of depending on your memory.")],
    "trade_slug": "pool_service", "trade_plural": "pool service companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do Pool Service Companies Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-pool-service-companies-miss-calls",
    "h1": "Why Do Pool Service Companies Miss So Many Calls?",
    "title": "Why Do Pool Service Companies Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Pool service companies miss calls because the tech is on a route all day. A homeowner who wants weekly service or has a dead pump calls the next company, not voicemail.",
    "answer": "You miss calls because your tech is on a route all day, hands in the water, testing chemistry, or driving between stops, and none of that stops for the phone. A homeowner who wants weekly service, or is staring at a green pool, does not leave a voicemail. They call the next company. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes while you are <em>on the route</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Pool service is a route trade, and the route does not stop for the phone. When it rings you are often skimming a pool, brushing a wall, elbow-deep in the equipment pad, or driving between stops with your hands on the wheel, and none of those are moments you can break off to take a call. The busier your route, the more calls you miss, which means your best days are also the ones where the most new work slips away. It is not a discipline problem. One person cannot service the pool in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but it is not one for a customer who is shopping. A homeowner picking a pool company, or one staring at a pump that quit before a pool party, is not going to leave a message and wait. They move down the list until someone answers, and by the time you check your phone at the end of the route, the customer has already signed with whoever picked up.</p>'},
        {"h2_html": "The missed calls that cost you the <em>most</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. Two kinds hurt the most for a pool company, and both tend to come while you are out on the route. The first is a new customer ready to sign up for weekly service, which is recurring revenue every month, not a one-time ticket, so losing that call is losing a whole account. The second is an urgent equipment problem, a dead pump, a failing heater, or a pool turning green before the weekend, which is high-value repair work that goes to whoever answers first.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can tell a routine request apart from an urgent one. A voicemail box cannot triage, and a generic call center does not know a weekly cleaning from a broken heater. What actually works is something that answers on the first ring day or night, gets the address and the pool details, and either books the routine service or flags a genuine equipment emergency straight to your phone, so you decide how to respond without ever missing the call in the first place.</p>'}],
    "bridge_h2": "Stop losing recurring accounts to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring while you are on the route, tells a new weekly-service signup from an urgent equipment issue, and books it or flags it to you, so the account never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-pool-service",
    "bridge_label": "AI receptionist for pool service companies",
    "faqs": [
        ("Would a customer rather reach a real person?",
         "Often what a pool owner needs most is to know someone is handling it, and a calm voice that captures the details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the pool details and address, and hands anything that needs your judgment straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail while you are brushing a pool, in the equipment pad, or driving to the next stop. Something that always answers and books the routine work is what catches the calls a forward would still miss.")],
    "trade_slug": "pool_service", "trade_plural": "pool service companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do Pool Service Customers Cancel? (problem -> crm) ============
{
    "slug": "why-pool-service-customers-cancel",
    "h1": "Why Do Pool Service Customers Cancel?",
    "title": "Why Do Pool Service Customers Cancel? | Top Shelf Business Solutions",
    "meta_desc": "Pool service customers usually cancel because they felt forgotten, not over price. A canceled recurring route account is the most expensive customer you can lose.",
    "answer": "Most pool service customers cancel not because of price, but because they felt forgotten. Weeks of silence between visits, one sloppy or skipped cleaning, or a repair bill with no heads-up, and a recurring account you counted on every month is gone. A canceled route customer is usually not angry, they just stopped feeling looked after.",
    "sections": [
        {"h2_html": "A canceled route customer is your biggest <em>single loss</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A pool company does not live on one-time jobs, it lives on the recurring route, so losing a route customer is not like losing a single repair. That account paid every month, and when it cancels you lose a season or a year of income at once, plus the cost and effort of finding someone to replace it. It stings twice on a dense route, because stops clustered on the same street keep your day efficient, and one cancellation can make the whole run less profitable to service. That is why churn on the recurring base quietly costs more than a slow week of new calls ever will.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">And most of it is preventable. A customer who cancels a weekly service is rarely angry about the work itself. More often they drifted, stopped feeling like they were getting anything for the money, and one day decided to try it themselves or answer a cheaper flyer. The account did not blow up, it faded, and a faded account is exactly the kind you can hold onto if you stay in front of it.</p>'},
        {"h2_html": "Why they leave, and how to <em>keep them</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reasons a route customer cancels are usually quiet ones, not a blowup. Understanding them is most of the fix, because nearly all of them come back to the same thing: the customer stopped feeling looked after.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>They almost never see the service happen, since it is done while they are at work, so it starts to feel like nothing is happening at all.</li><li>They hear nothing between visits, so a week skipped for weather reads as neglect instead of a normal call.</li><li>A repair or chemical charge lands with no heads-up, and the surprise sours the whole relationship.</li><li>Quiet months convince them they could just do it themselves, and no one gave them a reason to keep paying.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The fix is not working harder, it is staying in front of them: a quick note that the visit is done and what you found, a heads-up when weather moves a day, a reminder before a bill, and a check-in before the season turns. Done by hand after every stop, that is the first thing to fall on a full route. A CRM sends it for you on a schedule, so the recurring customer feels looked after and stays put instead of quietly drifting off.</p>'}],
    "bridge_h2": "Keep the route customers you already earned",
    "bridge_text": "A CRM keeps every route customer informed and worked for you, a note after each visit, a heads-up when weather moves a day, a check-in before the season, so the recurring account feels looked after instead of forgotten.",
    "bridge_slug": "crm-for-pool-service",
    "bridge_label": "CRM for pool service companies",
    "faqs": [
        ("How do I know why a pool customer really canceled?",
         "Most will not tell you, they just quietly stop, which is why churn is easy to miss until the route thins out. The common thread is silence: they rarely see the service happen and rarely hear from you, so it starts to feel like nothing is happening. Regular, simple communication is what prevents most of it."),
        ("Can a CRM really keep customers from canceling?",
         "It cannot fix sloppy work, but most cancellations are not about the work, they are about feeling forgotten. A short note after each visit, a heads-up when weather moves a day, and a check-in before the season keep the customer feeling looked after, and that is exactly what a CRM sends for you on a schedule.")],
    "trade_slug": "pool_service", "trade_plural": "pool service companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Do Pool Service Companies Get More Customers? (how-to -> marketing) ========
{
    "slug": "how-do-pool-service-companies-get-more-customers",
    "h1": "How Do Pool Service Companies Get More Customers?",
    "title": "How Do Pool Service Companies Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Pool service companies get more customers from the map pack, not just a website. A verified, active Google profile and steady reviews win the pool service near me search.",
    "answer": "Most new pool customers start in the map pack, the three local listings Google shows first with star ratings. You get found there with a verified, active Google Business Profile and a steady flow of recent reviews, so when someone nearby searches pool service near me or needs a spring open, your name is the one they call.",
    "sections": [
        {"h2_html": "The map pack is where pool customers <em>start</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a homeowner searches for pool service near me, or pool cleaning in your town, the first thing Google shows is not a website at all. It is the map pack, the little map with three local listings, star ratings, and a call button. Most people pick from those three without ever scrolling to the regular results below. So if the phone is quiet even though you have a website, the reason is usually that you are not in those three, and almost nobody is looking past them, especially at open season when demand spikes and everyone is choosing a company at once.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting into the map pack is a different job from having a website. It runs on your Google Business Profile: whether it is verified, complete, and active, how close you are to the searcher, and how many recent, genuine reviews you have. A great website with a neglected profile is a nice brochure that nobody sees at the moment they are choosing who to trust with their pool.</p>'},
        {"h2_html": "What actually brings in <em>new pool customers</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Growing the route is less about one clever trick and more about doing a handful of simple things steadily, which is exactly what slips when you are out servicing pools all day. A repeatable process beats good intentions.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Ask every happy customer for a review, every time, and make it one tap with a direct link, so the reviews build on their own.</li><li>Keep the Google profile active with recent posts and real photos of your work, a cleaned-up green pool or a fresh equipment install.</li><li>Keep your name, address, and phone number consistent everywhere, so Google trusts you are one real business.</li><li>Rank your site for the searches that bring recurring work: pool service near me, weekly cleaning, and green pool cleanup in your area.</li><li>Time a push around open and close season, when the most homeowners are deciding who to hire.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of it requires a gimmick. It requires getting the profile verified and complete, keeping it active, and building a steady flow of real reviews. What no one can honestly promise is a specific spot on the map, because Google decides that, but those are the levers that move it, and a free audit can show you where you stand today.</p>'}],
    "bridge_h2": "Get seen where pool customers start",
    "bridge_text": "Most new pool customers begin in the map pack. Keeping your Google profile verified, active, and full of recent reviews is how you show up there when someone nearby needs weekly service or a pool opened.",
    "bridge_slug": "marketing-for-pool-service",
    "bridge_label": "Marketing for pool service companies",
    "faqs": [
        ("Do I need a website to show up on Google Maps?",
         "Not to appear in the map pack, which runs on your Google Business Profile. A website helps you rank in the results below the map and gives the profile something to link to, but the fastest way onto the map itself is a verified, active, well-reviewed profile."),
        ("How long until my pool business shows up?",
         "A neglected profile that gets verified, completed, and active can start climbing within a few weeks, and it compounds as reviews and posts build. Nobody controls Google, so no honest company promises a specific position, but consistency on the profile is what moves it. Getting active before open season pays off most.")],
    "trade_slug": "pool_service", "trade_plural": "pool service companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
