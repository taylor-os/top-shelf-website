"""Colony page specs for HOUSE CLEANING COMPANIES (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a cleaning-business owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, cleaning-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear; no em/en dashes anywhere; "find the gap", never "leak" as a
money metaphor (cleaning has no literal leaks, so the word simply does not appear).

House cleaning runs on RECURRING revenue: a weekly or biweekly client kept for years is worth far
more than any single clean, so the questions turn on winning the first call, converting a one-time
or move-out clean into a recurring plan, and keeping recurring clients from quietly churning.

Nine questions, mixed cost / how-to / problem, spread across all seven money pages:
  1 get-more-house-cleaning-clients              (how-to)   -> marketing-for-house-cleaning-companies
  2 best-software-for-cleaning-business          (how-to)   -> crm-for-house-cleaning-companies
  3 house-cleaning-website-cost                  (cost)     -> websites-seo-for-house-cleaning-companies
  4 answering-service-for-cleaning-business-cost (cost)     -> ai-receptionist-for-house-cleaning-companies
  5 get-more-house-cleaning-reviews              (how-to)   -> review-software-for-house-cleaning-companies
  6 turn-one-time-cleans-into-recurring          (how-to)   -> automation-for-house-cleaning-companies
  7 stop-missing-calls-while-cleaning            (problem)  -> ai-receptionist-for-house-cleaning-companies
  8 should-cleaning-business-book-online         (how-to)   -> online-booking-for-house-cleaning-companies
  9 cut-cleaning-cancellations-no-shows          (how-to)   -> automation-for-house-cleaning-companies
"""

TOPICS = [
# ============ How Do I Get More House Cleaning Clients? (how-to -> marketing) ============
{
    "slug": "get-more-house-cleaning-clients",
    "h1": "How Do I Get More House Cleaning Clients?",
    "title": "How Do I Get More House Cleaning Clients? | Top Shelf Business Solutions",
    "meta_desc": "The most reliable way to get more house cleaning clients is to be the active, well-reviewed name in the Google map pack the moment a nearby homeowner decides to hire.",
    "answer": "The steadiest way to get more house cleaning clients is to be the visible, well-reviewed name in the map pack when a nearby homeowner finally decides to hire a cleaner. That moment is local and about trust, so showing up first, and looking trustworthy, on Google is what turns a search into a call.",
    "sections": [
        {"h2_html": "Cleaning clients decide fast, and <em>locally</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">People do not shop for a cleaner for weeks. Something triggers it, a new baby, a move, a return to the office, a holiday about to fill the house with guests, or just a spring where enough is enough, and then they decide quickly. In that moment the search is intensely local, because they want someone who already serves their street, and it is intensely about trust, because they are about to let strangers into their home. Get found first, and found trustworthy, in that window and the client is usually yours.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is why chasing a whole metro rarely works for a cleaning company. The clients worth having are the ones near the routes you already run, where a new home sits close to the ones you clean and your crews spend less of the day driving.</p>'},
        {"h2_html": "Where cleaning clients actually <em>find you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The channels that reliably bring a cleaning company new clients are less exciting than they sound, and that is the point. A handful of them, done consistently, beat any clever trick.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A complete, active Google Business Profile, so you show up in the map pack when someone nearby searches for a cleaner and picks from the first three listings.</li><li>A steady flow of recent reviews, which is what a homeowner actually reads before trusting a crew in their home.</li><li>Focus on the neighborhoods you serve, so new clients land near the ones you already clean and your routes stay dense.</li><li>Happy past clients, who refer and rebook when you stay in front of them, the private side handled by your CRM.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Buying leads can fill a slow week, but a bought lead is often sold to three cleaners at once and vanishes the day you stop paying. Nobody controls Google, so no honest company promises a specific spot, but the levers above are the ones that move it.</p>'}],
    "bridge_h2": "Be the cleaner they find first",
    "bridge_text": "Most cleaning clients start on Google the day they decide to hire someone. Keeping your profile active, well-reviewed, and focused on the neighborhoods you serve is how you are the name they see and trust in that moment.",
    "bridge_slug": "marketing-for-house-cleaning-companies",
    "bridge_label": "Marketing for house cleaning companies",
    "faqs": [
        ("What is the fastest way to get house cleaning clients?",
         "The fastest reliable channel is local search: a complete, active Google Business Profile with recent reviews so you appear in the map pack when someone nearby decides to hire a cleaner. Paired with asking happy clients for reviews and referrals, it compounds. Buying leads works only while you keep paying."),
        ("Should I buy house cleaning leads?",
         "You can, but a bought lead is usually sold to several cleaners at once and disappears the moment you stop paying. Money put into your own Google presence, reviews, and website keeps working and brings clients who are yours alone. It is the difference between renting clients and owning the channel that finds them.")],
    "trade_slug": "house-cleaning-companies", "trade_plural": "house cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== What's the Best Software for a Cleaning Business? (how-to -> crm) ========
{
    "slug": "best-software-for-cleaning-business",
    "h1": "What's the Best Software for a Cleaning Business?",
    "title": "What's the Best Software for a Cleaning Business? | Top Shelf Business Solutions",
    "meta_desc": "The best software for a cleaning business is a CRM that turns one-time cleans into recurring clients, holds your schedules, and catches clients before they churn.",
    "answer": "The best software for a cleaning business is whatever reliably turns one-time cleans into recurring clients and keeps your schedule, clients, and follow-up in one place, which is a CRM built for the trade. Fancy features matter less than whether it actually follows up and holds your recurring routes.",
    "sections": [
        {"h2_html": "The feature list is not what <em>makes you money</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to compare cleaning software by feature checklists and pick whichever has the longest one. But almost none of those features are what actually grows a cleaning business. The money is not in any single clean, it is in the client who stays on your schedule for a year or two, and the one job the software has to do well is turn a one-time clean into that recurring client and keep them from quietly drifting away.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A tool packed with features you never touch is not better than a simple one that reliably follows up after a deep clean, holds every recurring route, and warns you when a weekly client goes quiet. Judge the software by whether it does that, not by the length of its menu.</p>'},
        {"h2_html": "What to actually look for in <em>cleaning software</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Strip it back to what a cleaning company genuinely needs, and the list is short. If a tool does these well it will earn its keep, and if it does not, no other feature makes up for it.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Follows up automatically to turn one-time cleans, deep cleans, and move-outs into recurring plans while the house still feels spotless.</li><li>Holds every recurring schedule, address, gate or alarm code, product preference, and pet note in one place instead of your memory.</li><li>Flags a recurring client who has gone quiet or skipped two cleans, so you can win them back before they are gone.</li><li>Connects to your phone and online booking so a captured call or a new booking lands against the right client automatically.</li><li>Keeps your client list yours and exportable, not locked inside software you only rent.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate app you bolt on. It lives in the Signature plan at $899 a month, with the AI receptionist and monthly SEO, while plans start at $299 a month. Recover one recurring client it would have saved and it has paid for itself.</p>'}],
    "bridge_h2": "Software that turns cleans into recurring revenue",
    "bridge_text": "The right CRM for a cleaning business follows up to turn one-time cleans into recurring plans, holds every recurring schedule and home detail, and catches clients before they quietly drift away.",
    "bridge_slug": "crm-for-house-cleaning-companies",
    "bridge_label": "CRM for house cleaning companies",
    "faqs": [
        ("Do I really need cleaning software, or is a spreadsheet fine?",
         "A spreadsheet holds names, but it does not follow up to turn a one-time clean into a recurring client, does not remember who is due, and does not warn you when a weekly client goes quiet. Once you have more clients and cleans than you can track by memory, software that does the follow-up pays for itself."),
        ("What should cleaning software actually do for me?",
         "Turn one-time cleans into recurring plans with timed follow-up, keep every client, home detail, and recurring schedule in one place, flag clients who are drifting before they churn, and connect to your phone and booking so nothing slips. Features beyond that are nice, but those are the ones that hold your revenue.")],
    "trade_slug": "house-cleaning-companies", "trade_plural": "house cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ How Much Should a House Cleaning Website Cost? (cost -> websites-seo) ============
{
    "slug": "house-cleaning-website-cost",
    "h1": "How Much Should a House Cleaning Website Cost?",
    "title": "How Much Should a House Cleaning Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "How much should a house cleaning website cost? Less about page count, more about whether it books recurring cleans and proves your crews are trustworthy. Free on any plan from $299/mo, or $1,500 to own outright.",
    "answer": "A house cleaning website should do two things first: let a homeowner book a standard, deep, or move-out clean in a tap, and prove your crews are safe to let inside. Those two jobs decide whether it earns anything. Top Shelf includes it on every plan from $299 a month, or builds it standalone for $1,500.",
    "sections": [
        {"h2_html": "What a <em>cleaning</em> website has to do",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before you weigh a price, be clear on what a cleaning website is actually for, because it is not the same job as a site for most trades. A homeowner is deciding whether to let your crew into their house, often while they are at work, and whether you are worth switching to from the cleaner they already have. The site has to answer both in about the time it takes to scroll once, and that is the bar to buy against, not a page count.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Let a client book a one-time clean or lock in a recurring weekly or biweekly slot right on the page, so the standing revenue starts the moment they decide.</li><li>Show the trust signals a homeowner needs before handing over a key: insured, bonded, background-checked crews and a wall of recent reviews.</li><li>Lay out your service tiers, standard, deep, move-in and move-out, so a visitor picks the clean they want instead of calling to ask.</li><li>Carry a page for each area you cover, so you surface when someone nearby searches and your routes stay tight.</li></ul>'},
        {"h2_html": "So what should you <em>pay</em>?",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You can spend almost nothing or several thousand, but for a cleaning company the price only means something next to what the site brings back. A do-it-yourself page you put together on a weekend can look fine and still never rank in your area or convince a homeowner to trust a crew with their key, so it books nothing and the money you saved quietly disappears. What you are really buying is a site that fills your route with recurring clients, and that is worth paying for.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf builds the cleaning-specific site described above and includes it on any monthly plan. Plans begin at $299 a month and carry the ongoing SEO that keeps a site ranking. Prefer to own it outright with no plan? A standalone build runs $1,500, and it is yours to keep. Either way there is nothing to pay up front to get started, and no one can honestly guarantee a ranking by a set date, since Google decides that, though a free audit will show you where you stand and find the gap your current site is leaving.</p>'}],
    "bridge_h2": "Turn your website into a booking engine",
    "bridge_text": "For a cleaning company the site is where a recurring client signs up. Ours ranks for the neighborhoods you serve, proves your crews are background-checked and insured, and lets a homeowner lock in a standard, deep, or move-out clean on the spot.",
    "bridge_slug": "websites-seo-for-house-cleaning-companies",
    "bridge_label": "Websites & SEO for house cleaning companies",
    "faqs": [
        ("What makes a cleaning company website different from a generic one?",
         "Two things. It has to let a client book a recurring, deep, or move-out clean without calling, and it has to earn trust fast, since a homeowner is deciding whether to let a crew into their home. A generic template usually does neither, so it quietly costs you booked recurring work even when it was cheap to build."),
        ("Should I just use a free website builder instead?",
         "You can, and it does put you online. But a free builder leaves the work to you and rarely ranks in your area or books a recurring clean by itself. With Top Shelf the site is included on any plan from $299 a month, with the SEO that gets it found, or you can own one outright for $1,500 if you would rather skip a plan.")],
    "trade_slug": "house-cleaning-companies", "trade_plural": "house cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==== How Much Does an Answering Service for a Cleaning Business Cost? (cost -> ai-receptionist) ====
{
    "slug": "answering-service-for-cleaning-business-cost",
    "h1": "How Much Does an Answering Service for a Cleaning Business Cost?",
    "title": "How Much Does an Answering Service for a Cleaning Business Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for a cleaning business often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for a cleaning business usually bill per call, per minute, or on a retainer, so a busy month gets pricey fast. Top Shelf takes a different route: an AI receptionist that answers every call, gathers the quote, and books the clean is included in the Signature plan at $899 a month, flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy month turns into a big bill. A cleaning company also gets calls at the worst times to answer them: during the day while crews are inside homes, and in the evenings and on weekends when a busy family finally sits down to line up a cleaner. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of price-shoppers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty caller or a slow operator costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner who wants a cleaner does not leave a voicemail, they call the next company on the list. And in cleaning the call you just lost is rarely one job. Someone who wanted weekly or biweekly service is months, sometimes years, of cleans, and all of it goes to whoever picked up. A generic call center reading a script cannot tell a standard clean from a move-out, so you can pay for coverage and still get a lead you cannot quote.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, gathers what a quote needs, the size of the home, how often they want service, and the type of clean, and books the visit or hands you a ready lead. It is included in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One recurring client you would have lost on a weekend often covers the plan for a long stretch, and everything it captures after that is on top.</p>'}],
    "bridge_h2": "Answer every quote call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers while your crews are inside homes, gathers what a clean needs to be quoted, and books it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-house-cleaning-companies",
    "bridge_label": "AI receptionist for house cleaning companies",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service for cleaners?",
         "Usually, and far more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the recurring client it books instead of losing to voicemail while your crews are inside homes."),
        ("Does it cost extra for evenings and weekends?",
         "No. It answers around the clock as part of the plan, including the evenings and weekends when busy families finally sit down to book a cleaner, with no after-hours surcharge or per-call overage.")],
    "trade_slug": "house-cleaning-companies", "trade_plural": "house cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ How Do House Cleaners Get More Google Reviews? (how-to -> review-software) ============
{
    "slug": "get-more-house-cleaning-reviews",
    "h1": "How Do House Cleaners Get More Google Reviews?",
    "title": "How Do House Cleaners Get More Google Reviews? | Top Shelf Business Solutions",
    "meta_desc": "House cleaners get more Google reviews by asking every happy client the moment a clean is done and making it one tap, so the next homeowner trusts your crew first.",
    "answer": "House cleaners get more Google reviews by asking every happy client right after a clean, when they walk into a spotless home, and making it a single tap. Most cleaners do great work but forget to ask or ask too late. Sending the request automatically at that moment, with a direct link, is what steadily builds them.",
    "sections": [
        {"h2_html": "For a cleaner, reviews are <em>permission to enter a home</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Choosing a cleaning company is an unusually personal decision. You are letting people into your home, often when you are not there, sometimes with a key, an alarm code, or a garage code. So a homeowner comparing cleaners does not just glance at the star rating, they read the recent reviews to decide whether they trust these people in their house at all. A company with a few old reviews quietly loses those clients to the one with a fresh, steady wall of them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The problem is almost never that your clients are unhappy. It is that a thrilled client walks into a spotless home, feels great for an hour, and never thinks to post about it, while asking in person feels awkward. Fix the timing and the awkwardness and the reputation your crews have already earned finally shows up where new clients are deciding.</p>'},
        {"h2_html": "How to get more, <em>consistently</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more reviews is less about a clever trick and more about doing the same simple thing after every clean, which is exactly what falls apart on a busy week. A repeatable process beats good intentions.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Ask every happy client, every time, not just the ones you remember, so it is never left to chance.</li><li>Ask at the right moment, right after the clean, when the client walks into a spotless home and is happiest.</li><li>Make it one tap with a direct link straight to your Google profile, sent by text and email.</li><li>Pace recurring clients, so a weekly customer is invited when they are new and only occasionally after that, never nagged.</li><li>Reply to every review, good or bad, which reassures the next reader and helps your local ranking.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Doing all that by hand after each job is the first thing to slip when you are busy. Software fixes it by sending the ask automatically the moment a clean is marked done. One rule keeps you on the right side of Google: ask every client honestly, and never filter out unhappy ones or pay for reviews.</p>'}],
    "bridge_h2": "Turn every finished clean into a review",
    "bridge_text": "Review software asks every happy client the moment a clean is done and makes leaving one a single tap, so the next homeowner deciding who to trust with a key finds a wall of recent reviews and calls you first.",
    "bridge_slug": "review-software-for-house-cleaning-companies",
    "bridge_label": "Review software for house cleaning companies",
    "faqs": [
        ("Is asking cleaning clients for reviews against Google policy?",
         "Asking every client for an honest review is allowed and encouraged. What is not allowed is filtering out unhappy clients, offering incentives, or paying for reviews. Asking everyone right after a clean and making it one tap is squarely within the rules."),
        ("How do I ask recurring clients without nagging them?",
         "Pace it. A recurring client should be invited once when they are new and then only occasionally after that, not after every single visit. Good review software spaces the ask automatically, so a weekly client is never pestered while new clients are still invited.")],
    "trade_slug": "house-cleaning-companies", "trade_plural": "house cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Do I Turn One-Time Cleans Into Recurring Clients? (how-to -> automation) ========
{
    "slug": "turn-one-time-cleans-into-recurring",
    "h1": "How Do I Turn One-Time Cleans Into Recurring Clients?",
    "title": "How Do I Turn One-Time Cleans Into Recurring Clients? | Top Shelf Business Solutions",
    "meta_desc": "Turn one-time cleans into recurring clients by following up while the house still feels spotless and offering a weekly or biweekly plan, sent automatically for you.",
    "answer": "Turn one-time cleans into recurring clients by following up within a day or two of the job, while the house still feels spotless, and offering a weekly or biweekly plan. The client already loves the result; the recurring plan closes when someone actually makes the ask, which is exactly what gets forgotten between jobs.",
    "sections": [
        {"h2_html": "The most valuable conversation is the one there is <em>no time for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most cleaning companies do not have a lead problem, they have a follow-up problem. You do a great deep clean or a move-out, the client is thrilled, and then nobody ever asks them to go on a schedule. A one-time clean stays a one-time payment unless someone follows up and offers weekly or biweekly service while the memory of a spotless house is still fresh. That is the single most valuable conversation in the business, and it is the one there is never time for between crews and quotes.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It is not that owners do not want to. You finish the job, roll to the next, handle the quote that came in during lunch, and by evening the client who would have said yes never got asked. Left to memory, the ask only happens when things are slow, which is exactly when you have the fewest cleans to convert.</p>'},
        {"h2_html": "Make the recurring ask <em>happen every time</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The fix is not trying harder to remember, it is a follow-up that fires on its own after every one-time clean. A day or two later, while the house still feels perfect, the client gets a warm, personal note asking if they would like to keep it that way every week or every other week, written to sound like you. The ones who meant to set something up finally do, and a single job becomes a standing slot on your route.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>After a one-time clean, deep clean, or move-out, an automatic ask to go recurring while the result is fresh.</li><li>A timed nudge on a quote that went quiet, so a client comparing cleaners keeps hearing from you.</li><li>A seasonal check-in to a client who paused over the holidays and never restarted, bringing that work back around.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Because it runs against the same client list as your CRM, nothing gets double-messaged, and every touch is logged where you can see it. You are not adding work, you are making sure the most profitable ask in the business stops depending on a good memory.</p>'}],
    "bridge_h2": "Make the recurring ask happen on its own",
    "bridge_text": "Automation follows up after every one-time clean, while the house still feels spotless, to offer a weekly or biweekly plan, and revives cold quotes and paused clients, so recurring revenue builds without you keeping a mental list.",
    "bridge_slug": "automation-for-house-cleaning-companies",
    "bridge_label": "Automation for house cleaning companies",
    "faqs": [
        ("When is the best time to ask a one-time client to go recurring?",
         "Within a day or two of the clean, while the house still feels spotless and the client is happiest with the result. Wait a few weeks and the feeling fades along with the yes. A short, friendly ask at that moment is what converts a one-time deep clean into a standing slot."),
        ("Does an automated recurring offer feel pushy?",
         "Not when it is written to sound like you and sent once at the right moment. Most clients who loved the clean simply never thought to set up a schedule, so a warm nudge reads as helpful, not salesy. You can always jump in and message anyone yourself.")],
    "trade_slug": "house-cleaning-companies", "trade_plural": "house cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Do I Stop Missing Calls While My Crews Are Cleaning? (problem -> ai-receptionist) ========
{
    "slug": "stop-missing-calls-while-cleaning",
    "h1": "How Do I Stop Missing Calls While My Crews Are Cleaning?",
    "title": "How Do I Stop Missing Calls While My Crews Are Cleaning? | Top Shelf Business Solutions",
    "meta_desc": "You miss calls because your hands are full inside homes, and a homeowner does not leave a voicemail. Make sure every call is answered while your crews are cleaning.",
    "answer": "You miss calls because your hands are full inside a home, running a vacuum or a mop, and a homeowner who wants a cleaner does not leave a voicemail, they call the next company on Google. The fix is not answering more yourself, it is making sure every call gets answered while you clean.",
    "sections": [
        {"h2_html": "The call comes exactly when your <em>hands are full</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Cleaning is a hands-full trade. When the phone rings you are usually inside a home with a vacuum or a mop, wearing gloves, driving between stops, or off the clock in the evening when a busy family finally has a minute to line up a cleaner. None of those are moments you can stop and take a call. The busier you are, the more calls you miss, so your best weeks are also the ones where the most work slips away. It is not a discipline problem; one person cannot clean a house and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but it is not one. A homeowner ready to hire a cleaner is not going to leave a message and wait, they move down the list until someone answers. And the call you just lost was rarely a single clean; a new client who wanted weekly service was years of work that just went to the company that picked up.</p>'},
        {"h2_html": "Coverage that answers while you <em>work</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Closing the gap takes coverage that never sleeps and can do more than take a message. A voicemail box cannot gather a quote, and a generic call center does not know a standard clean from a deep clean or a move-out. What actually works is something that answers on the first ring, day or night, asks the size of the home, how often they want service, and the type of clean, and either books the visit or hands you a lead you can price the moment you come off the job.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It also has to tell your people apart. A current client calling to reschedule, skip a week, or add the inside of the fridge is a different conversation from a brand-new prospect, and the ones who already trust you should never hit a voicemail. Answer both well and the calls you used to lose while cleaning turn back into booked cleans.</p>'}],
    "bridge_h2": "Never miss a call while your hands are full",
    "bridge_text": "An AI receptionist answers every call on the first ring while your crews are inside homes, gathers what a quote needs, and books the clean or hands you a ready lead, so the call never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-house-cleaning-companies",
    "bridge_label": "AI receptionist for house cleaning companies",
    "faqs": [
        ("Can I just forward calls to my cell while I clean?",
         "You can, but that only helps when a hand is free. Forwarding still rolls to voicemail when you are running a vacuum, wearing gloves, or already on another call, which is most of the day. Something that always answers and gathers the quote is what catches the calls a forward would still miss."),
        ("Would a client rather reach a real person?",
         "What a homeowner deciding who to let into their home wants most is a real answer and a time on the calendar, which beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the details, and hands anything unusual straight to you.")],
    "trade_slug": "house-cleaning-companies", "trade_plural": "house cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== Should a Cleaning Business Let Customers Book Online? (how-to -> online-booking) ========
{
    "slug": "should-cleaning-business-book-online",
    "h1": "Should a Cleaning Business Let Customers Book Online?",
    "title": "Should a Cleaning Business Let Customers Book Online? | Top Shelf Business Solutions",
    "meta_desc": "Should a cleaning business let customers book online? For most, yes. It ends phone tag and lets clients claim a one-time clean or a recurring slot on your real availability.",
    "answer": "Yes, for most cleaning businesses. A lot of cleaning is not urgent, and those clients would happily pick a time themselves instead of playing phone tag while your crews are inside homes. Online booking on your real availability lets them claim a one-time clean or a recurring slot, and it lands on your calendar ready.",
    "sections": [
        {"h2_html": "Phone tag quietly costs you the <em>easy bookings</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A lot of cleaning is not urgent, and that is exactly why it slips. Someone decides they finally want a regular cleaner or a one-time deep clean, they call during the day, you are inside a home and cannot pick up, and now it is voicemail, a callback tomorrow, another missed call, and two days of tag for a job they were ready to book on the spot. Make people work that hard and the client you should have signed books the company that let them do it themselves.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">For a cleaning business the cost is bigger than one visit. A client who wanted a recurring clean is a standing spot on your route, week after week, and losing that to phone tag is losing years of work, not an afternoon. Every missed handoff is a place a motivated client can quietly drop out.</p>'},
        {"h2_html": "Booking that protects your <em>calendar and route</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Letting clients book themselves does not mean anyone can drop anything onto your calendar. A good booking flow asks what matters for a clean first, the size of the home, the number of bedrooms and bathrooms, one-time or recurring and how often, the type of clean, and any add-ons like the inside of the oven or interior windows, so a standard job books itself and an unusual one, a large home or a post-construction clean, gets a quick call to price. You set the rules: which visit types are bookable, how long each takes, how much notice you need, and how much drive-time buffer to leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It syncs to the calendar you already use, so it cannot double-book a crew or stack two jobs across town with no time to drive between them, and best of all a client can lock in a recurring slot, so one booking fills a standing spot on your route. The link lives everywhere someone finds you: your website, your Google profile, your email signature, and the text you send after a quote.</p>'}],
    "bridge_h2": "Let clients book while you clean",
    "bridge_text": "Online booking lets clients claim a one-time clean or a recurring slot on your real availability, gathers the details your crew needs, and drops it on your calendar, so you stop trading voicemails and win the easy bookings.",
    "bridge_slug": "online-booking-for-house-cleaning-companies",
    "bridge_label": "Online booking for house cleaning companies",
    "faqs": [
        ("Will online booking let someone drop a huge job on my calendar?",
         "Not if it is set up right. The form asks the home size, the type of clean, and any add-ons first, so a standard clean books itself and an unusual one, like a large home or a post-construction clean, is routed to a quick call to price before it is scheduled. You decide which types are bookable."),
        ("Can clients book a recurring clean online, not just a one-time?",
         "Yes, and that is the point for a cleaning business. A client can lock in a weekly, biweekly, or monthly slot in one booking, so you fill a standing spot on your route instead of a single visit, and it repeats on the schedule they chose.")],
    "trade_slug": "house-cleaning-companies", "trade_plural": "house cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Do I Cut Last-Minute Cleaning Cancellations and No-Shows? (how-to -> automation) ========
{
    "slug": "cut-cleaning-cancellations-no-shows",
    "h1": "How Do I Cut Last-Minute Cleaning Cancellations and No-Shows?",
    "title": "How Do I Cut Last-Minute Cleaning Cancellations and No-Shows? | Top Shelf Business Solutions",
    "meta_desc": "Cut last-minute cleaning cancellations and no-shows with automatic confirmations, reminders, and on-the-way texts, so crews stop arriving to locked, empty houses.",
    "answer": "Cut last-minute cleaning cancellations and no-shows with automatic confirmations and reminders before every clean, plus an on-the-way text when the crew heads out. Most are not deliberate; a client forgot the day or a gate code changed. A timed reminder is the single biggest lever on empty, locked-out trips that still cost you a paid crew.",
    "sections": [
        {"h2_html": "Most no-shows are forgotten, not <em>deliberate</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a client forgets a cleaning day, the cost is not just an awkward call. Your crew drives out, and the door is locked, the gate code was changed, or the alarm is armed and nobody is home, and now two or three people you pay by the hour are standing in a driveway with a hole in the route no one can fill on short notice. It is tempting to blame flaky clients, but most no-shows are not deliberate. The appointment was made days ago, nobody reminded them, and it fell off their calendar the same way a quote falls off yours.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That means most wasted trips are preventable with information, not enforcement. A client who gets a clear confirmation, a reminder the day before, and a heads-up when the crew is on the way is far more likely to have the door open when you pull up. The gap is not the client, it is that nobody told them what to expect.</p>'},
        {"h2_html": "The reminders that keep your <em>crews working</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A last-minute cancellation is the most expensive thing on a cleaning schedule, because a slot dropped the morning of is almost impossible to refill and the crew still gets paid. The reason the reminders that prevent it do not happen is simple: you are running crews and answering quotes all day, and stopping to text every client to confirm tomorrow is the first thing to slip. Automating it means it happens every time without anyone working the phones.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A confirmation when the clean is booked, so it lands on their calendar.</li><li>A reminder the night before, with an easy way to reschedule instead of just not being home.</li><li>An on-the-way text with a realistic arrival window when the crew heads out, so the door is open and the alarm is off.</li><li>A quick note if the schedule slips, so a running-late crew does not turn into a missed clean.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">For an owner running a couple of crews, that is a fuller, tighter route without anyone stopping to make confirmation calls. The same automation can carry the follow-up after the clean, a review request and a nudge to go recurring, so the visit keeps paying off long after the crew pulls away.</p>'}],
    "bridge_h2": "Keep your crews cleaning, not idling",
    "bridge_text": "Automation sends confirmations, reminders, and on-the-way texts for you, so clients are home with the door open when your crew arrives and last-minute cancellations stop leaving a paid crew with nothing to do.",
    "bridge_slug": "automation-for-house-cleaning-companies",
    "bridge_label": "Automation for house cleaning companies",
    "faqs": [
        ("Do reminder texts really cut cleaning cancellations and no-shows?",
         "They are the single biggest lever on it. A confirmation, a reminder the night before, and an on-the-way text keep the clean top of mind and give the client an easy way to reschedule in advance instead of a locked door on the day. Fewer wasted, crew-idling trips is usually the first thing owners notice."),
        ("What happens when a client cancels last minute anyway?",
         "You will still get the occasional one, but far fewer, and the system can nudge the client to rebook and surface the open slot so you can try to fill it. The goal is to find the gap early, not after a paid crew has already driven to an empty house.")],
    "trade_slug": "house-cleaning-companies", "trade_plural": "house cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
