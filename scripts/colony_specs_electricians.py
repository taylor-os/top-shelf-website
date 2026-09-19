"""Colony page specs for ELECTRICIANS (Home Services hub). generate_colony.py loads TOPICS
from every colony_specs_*.py. Each dict is ONE real question an electrical-business owner
would search, answered directly up top, with two short body sections, then funneled to the
one money page that solves it via the "the fix" bridge. Nine distinct questions, a mix of
problem/symptom, how-to, and cost, spread across all seven electrician money pages.

Voice matches corpus_specs.py / specs_electricians.py: direct, plain, peer-to-owner, honest
(hedged, no invented stats/prices/clients), no em or en dashes, and it uses "the gap" or
"slipping/going cold", never "leak". Prices are limited to Top Shelf's real ladder; only the
Essentials entry ($299/mo, which includes the website) is cited, and only where it is true.
"""

TOPICS = [
# ============================ 1. Panel-upgrade quotes go cold -> CRM ============================
{
    "slug": "panel-upgrade-quotes-go-cold",
    "trade_slug": "electricians", "trade_plural": "electricians",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "title": "Why Do My Panel Upgrade Quotes Go Cold? | Top Shelf Business Solutions",
    "h1": "Why Do My Panel Upgrade Quotes Go Cold?",
    "meta_desc": "Panel upgrade quotes go cold because these considered purchases take weeks to approve and nobody follows up. Here is how to keep them warm and win the job.",
    "answer": "Panel upgrade quotes go cold because a service upgrade is a considered purchase homeowners sit on for weeks, comparing bids while nobody stays in touch. The price was rarely the problem. The quote just needed a steady follow-up you never had time for between service calls, so it quietly went to whoever checked back.",
    "sections": [
        {"h2_html": "It is almost never the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A panel or service upgrade is a considered purchase. It is a big number, it is not urgent the day you quote it, and the homeowner wants to talk it over, get another bid or two, and wait for the timing to feel right. Weeks pass. By the time they are finally ready, the electrician who stayed in touch is the one they call, and it is usually not the one who quoted first and then went silent.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So the quote did not die because your number was too high. It died because nothing kept you in front of them while they made up their mind. That gap between "let me think about it" and "let us do it" is where most upgrade jobs are won or lost, and it has almost nothing to do with the estimate itself. The bid that wins is often just the one that was still there at the moment the homeowner decided.</p>'},
        {"h2_html": "Steady follow-up wins the jobs that <em>take weeks to decide</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The jobs electricians quote and wait on, panel upgrades, rewires, generator and EV charger installs, are exactly the ones a patient follow-up wins. A quick check-in the next day, a note answering the permit or timeline question they were stuck on, one last nudge before it goes cold, that is usually all it takes to be the name they remember. The trouble is that nobody has time to do that by hand for every quote, week after week, in between running actual service calls.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Write down every quote and the day you sent it, so none of them quietly fall off your radar.</li><li>Reach back out on a schedule, not whenever you happen to remember, which for most owners is close to never.</li><li>Answer the usual questions about permit, timeline, and disruption before the homeowner has to ask, so you look like the easy choice.</li></ul>'}],
    "bridge_h2": "Put every quote on a follow-up that runs itself",
    "bridge_text": 'A CRM for electricians keeps every quote and past customer in one place and follows up for you, on the schedule you approve, so the upgrade someone is still deciding on comes back to you instead of the electrician who happened to check back. Your customer list quietly becomes your pipeline.',
    "bridge_slug": "crm-for-electricians",
    "bridge_label": "See the CRM for electricians",
    "faqs": [
        ("How long should I keep following up on a panel upgrade quote?",
         'Longer than most electricians think. These are considered purchases people sit on for weeks, so a light touch every few days for a few weeks, then an occasional check-in after that, tends to win more than one call and then silence. The goal is simply to still be there when they are finally ready to move.'),
        ("Will following up too much annoy the customer?",
         'Not if it is helpful instead of pushy. A quick answer to the permit or timeline question they were weighing, or a note that you can hold a slot next week, reads as good service, not pressure. A good system spaces the touches out so you stay useful without turning into noise.')],
},
# ==================== 2. Miss calls when hands are full -> AI receptionist ====================
{
    "slug": "miss-calls-hands-full",
    "trade_slug": "electricians", "trade_plural": "electricians",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "title": "Why Do I Miss Calls When My Hands Are Full On A Job? | Top Shelf Business Solutions",
    "h1": "Why Do I Miss Calls When My Hands Are Full On A Job?",
    "meta_desc": "You miss calls because electrical work fills both hands while your phone sits out in the truck. Here is how to catch those jobs without stopping mid-task.",
    "answer": "You miss calls because electrical work uses both hands in places a phone cannot follow, inside a panel, up a ladder, in an attic, with the phone out in the truck. The call comes in while you physically cannot answer, rolls to voicemail, and a homeowner who needs an electrician simply calls the next one.",
    "sections": [
        {"h2_html": "Your trade does not let you <em>stop and answer</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Electrical work uses both hands, and it happens in places a ringing phone cannot reach you: inside a live panel, up a ladder, in a crawl space or an attic, with a drill running and your phone sitting out in the truck. The calls that come in during the workday are not calls you are choosing to ignore. They are calls you physically cannot take without stopping something you should not stop in the middle of.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So they roll to voicemail. And a homeowner who needs an electrician does not sit and wait for a callback, they scroll to the next name and dial again. The job you lost was not lost on price or on reputation. It was lost because you were doing the last job at the exact moment the next one called, which is the everyday reality of running the truck yourself.</p>'},
        {"h2_html": "Catch the call without <em>climbing down the ladder</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The answer is not to carry your phone into every panel, and it is not to hire a full-time person to sit by it. It is to make sure every call gets answered by something that can take the details and hand them to you, so you finish the task in front of you and then call back to a lead that is already captured, instead of a voicemail that might be a wrong number or might be a full panel replacement.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every call gets picked up on the first ring, including the ones that land while you are mid-job.</li><li>The caller name, number, address, and problem come to you by text, so you can judge what is worth stopping for.</li><li>Routine work gets booked or noted for later, and a true emergency gets flagged to you right away.</li></ul>'}],
    "bridge_h2": "Let an AI receptionist answer while your hands are busy",
    "bridge_text": 'An AI receptionist for electricians answers every call the moment it comes in, day or night, finds out whether it is a sparking outlet, a dead panel, or planned work, and texts you the details before you are off the ladder. You keep your own number, and every lead stays yours.',
    "bridge_slug": "ai-receptionist-for-electricians",
    "bridge_label": "See the AI receptionist",
    "faqs": [
        ("What happens to the call while I am still on the job?",
         'It gets answered and handled without you. The caller talks to a receptionist that takes their details and either books the visit or flags an emergency, and you get a text with everything you need. You call back when you are down and safe, to a lead that is already captured instead of a hang-up.'),
        ("Is a cheap voicemail greeting enough?",
         'Usually not. Voicemail does not triage anything, and most people will not leave one, especially with an urgent electrical problem. They hang up and call the next electrician. Something that actually answers and captures the details is the difference between losing that call and keeping the job.')],
},
# ==================== 3. Get more Google reviews -> Review software ====================
{
    "slug": "get-more-electrician-reviews",
    "trade_slug": "electricians", "trade_plural": "electricians",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "title": "How Do I Get More Google Reviews As An Electrician? | Top Shelf Business Solutions",
    "h1": "How Do I Get More Google Reviews As An Electrician?",
    "meta_desc": "Get more Google reviews by asking every happy customer the moment the job is done, with a one-tap link. Here is the timing and the system that makes it stick.",
    "answer": "Ask every satisfied customer the moment the job is done and the power is back on, when they are most grateful, and make leaving a review a single tap with a direct link to your Google profile. Doing it by hand rarely lasts, so most electricians use software that sends the ask automatically after every job.",
    "sections": [
        {"h2_html": "Timing is <em>everything</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason you do not have more reviews is almost never that customers are unhappy. It is that the happy ones forget, and by the time you think to ask, the moment has passed. The best time to ask is right when you finish, when the power is back on, the panel is clean and labeled, and the customer is standing there relieved and grateful. Ask then, in person or with a message that goes out that same hour, and most people are glad to say yes.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Wait until you are back at the shop that night, or three weeks later, and the same customer who would have gladly left five stars just never gets around to it. Nothing changed about their opinion of you. You simply missed the short window when it was easy for them to act on it, and that window is why so much genuine goodwill never makes it online.</p>'},
        {"h2_html": "Make it a <em>single tap</em>, and make it consistent",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Even a happy customer will not hunt for your Google page, sign in, and figure out where to click. The easier you make it, the more reviews you get, so the ask should be a text or email with one link that drops them straight onto your review form. And it has to happen every time, not just when you remember, because consistency is what turns a handful of old reviews into a steady, recent stream that homeowners and Google both notice. A profile that gains a few reviews every month, without you thinking about it, quietly pulls ahead of the electrician who only asks now and then.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Ask right after the job, by text and email, while the relief is still fresh.</li><li>Send one direct link so leaving a review takes seconds, not a search.</li><li>Do it after every completed job, not only the memorable ones, so the reviews keep coming.</li></ul>'}],
    "bridge_h2": "Automate the ask so it happens after every job",
    "bridge_text": 'Review software for electricians sends the request automatically the moment a job is marked complete, by text and email, with a one-tap link to your Google profile, and helps you reply to each review that lands. It captures the goodwill you already earn instead of leaving it to whoever happens to remember.',
    "bridge_slug": "review-software-for-electricians",
    "bridge_label": "See the review software",
    "faqs": [
        ("Is it against the rules to automate review requests?",
         'Asking every real customer for an honest review is fine and encouraged. What is not allowed is filtering out unhappy customers or paying for reviews. Sending everyone the same friendly ask at the right moment, and taking whatever they honestly write, stays well inside the rules each platform sets.'),
        ("How many reviews do I actually need?",
         'There is no magic number, and a steady stream of recent reviews usually matters more than one big pile from years ago. A profile that keeps gaining fresh reviews tends to look more trustworthy to homeowners, and to Google, than one that clearly stopped growing a long time ago.')],
},
# ==================== 4. What does an electrician website cost -> Websites & SEO ====================
{
    "slug": "electrician-website-cost",
    "trade_slug": "electricians", "trade_plural": "electricians",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "title": "How Much Does An Electrician Website Cost? | Top Shelf Business Solutions",
    "h1": "How Much Does An Electrician Website Cost?",
    "meta_desc": "An electrician website ranges from a cheap DIY template to a custom build, and a site that never ranks is the costly one. Top Shelf includes yours from $299 a month.",
    "answer": "It depends on what you need. A basic template you build yourself is cheap but rarely ranks or captures calls, while a custom, done-for-you site that ranks locally and turns visitors into booked jobs costs more. Top Shelf folds the site into its plans from $299 a month instead of charging a large upfront build fee.",
    "sections": [
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An electrician website can cost almost nothing or quite a lot, and the number comes down to a few real things: whether you build a template yourself or have it built for you, whether it is just an online business card or is engineered to rank in local search and capture calls, and whether it is a one-time build or comes with the ongoing SEO that keeps it showing up. A cheap template and a site built to bring you jobs are not the same product, even though both get called "a website".</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is why a flat quote with no context does not tell you much. The useful question is not "what does a website cost", it is "what does a website that actually brings me calls cost", because a site nobody finds is the most expensive option of all. You paid for it, and it earns you nothing while a competitor whose site does rank quietly takes the jobs.</p>'},
        {"h2_html": "The cheap site nobody finds is the <em>expensive one</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The real trap is spending a little on a site that looks fine and does nothing. It does not rank, it does not turn visitors into calls, and it quietly costs you every job that went to an electrician whose site did the work. Whatever you spend, the site has to do three things: show up when a homeowner searches, make calling or requesting a quote effortless, and feed those leads somewhere they get followed up instead of forgotten.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf takes a different path from a big upfront build fee. The website is included in the monthly plan, starting at $299 a month, alongside the tools that answer the calls it brings in and follow up on the quotes it captures. That way the site is part of a system that earns, rather than a one-time cost that sits there looking nice and doing very little.</p>'}],
    "bridge_h2": "Get a site built to rank and capture calls",
    "bridge_text": 'Websites and SEO for electricians builds a site that ranks for electrician near me in your city, puts click-to-call and a quote request on every page, and feeds every lead into your CRM. It is included in the plan from $299 a month instead of a large upfront fee, so the site earns its keep.',
    "bridge_slug": "websites-seo-for-electricians",
    "bridge_label": "See websites and SEO for electricians",
    "faqs": [
        ("Is a one-time website build or a monthly plan better?",
         'It depends on what you want the site to do. A one-time build is a fixed cost, but a site that ranks needs ongoing SEO to stay visible, which a build-and-leave rarely includes. A monthly plan bundles the site with that upkeep and the tools that capture its leads, so it keeps working instead of aging out.'),
        ("Do I really need to pay for SEO, or just a website?",
         'A website with no SEO is a business card nobody looks up. SEO is what makes it show up when a homeowner searches for an electrician near them, which is the entire point of having one. Paying for a site without it usually means paying for something that never actually gets found.')],
},
# ==================== 5. Get more generator installs -> Marketing ====================
{
    "slug": "get-more-generator-installs",
    "trade_slug": "electricians", "trade_plural": "electricians",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "title": "How Do I Get More Generator Installation Jobs? | Top Shelf Business Solutions",
    "h1": "How Do I Get More Generator Installation Jobs?",
    "meta_desc": "Get more generator installs by keeping your Google Business Profile active and showcasing that work, so homeowners find you when the power goes out.",
    "answer": "Show up where homeowners look when the power goes out. Keep your Google Business Profile active with photos of finished generator installs, feature that work in your local content, and gather reviews that mention it, so you build a reputation for generators and appear when someone nearby searches for one after an outage.",
    "sections": [
        {"h2_html": "Generator demand shows up <em>when the power goes out</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Whole-home and standby generator installs are a considered purchase, but the interest often spikes on a schedule you do not control: after a storm, a grid outage, or a stretch of extreme weather, when a lot of homeowners are suddenly thinking about backup power all at once. The electricians who land those jobs are usually not the cheapest. They are the ones the homeowner already recognizes, or the ones who show up first the moment that homeowner finally sits down to search.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So getting more generator work is less about one clever ad and more about being visibly, consistently in the generator business before the lights ever flicker. Then, when demand arrives all at once, you are the obvious name to call rather than one more search result a nervous homeowner is comparing at nine at night. The work you want more of goes to the shop that was already visible for it, not the one starting from scratch the week demand spikes.</p>'},
        {"h2_html": "Build a visible reputation for the <em>work you want</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">If most of what people see from you is general electrical work, that is what they will call you for. If your Google profile, your photos, and your local content lean into generators, you start to be known for generators, and you show up when someone searches for a generator installer nearby. Marketing lets you point demand toward the higher-value jobs you actually want more of, instead of taking whatever happens to come in.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Post finished generator installs to your Google Business Profile with clear, real photos.</li><li>Answer the common questions about sizing, fuel type, transfer switches, and permits in local content, so you rank for them and look like the expert.</li><li>Gather reviews that mention generator work, so the next homeowner sees you have done it before.</li></ul>'}],
    "bridge_h2": "Get known for generators before the next outage",
    "bridge_text": 'Marketing for electricians keeps your Google Business Profile active and leans your photos, posts, and local content toward the work you want more of, so you build a reputation for generator installs and show up when a homeowner searches after the power goes out. You become the name they already know to call.',
    "bridge_slug": "marketing-for-electricians",
    "bridge_label": "See marketing for electricians",
    "faqs": [
        ("Are ads or a strong local presence better for generator jobs?",
         'Both can work, but a consistent local presence tends to compound while ads stop the day you stop paying. A homeowner who has seen your generator work for months calls you from memory when the power goes out, which is cheaper and more durable than buying that same click over and over again.'),
        ("How do I compete with the big generator companies?",
         'You will not outspend a national brand, and you do not have to. Homeowners often prefer a local electrician they can find, read real reviews on, and reach directly. Showing up in local search with genuine reviews and photos of your own generator installs is exactly where a local shop can win.')],
},
# ==================== 6. Let customers book online -> Online booking ====================
{
    "slug": "book-electrical-work-online",
    "trade_slug": "electricians", "trade_plural": "electricians",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "title": "How Do I Let Customers Book Electrical Work Online? | Top Shelf Business Solutions",
    "h1": "How Do I Let Customers Book Electrical Work Online?",
    "meta_desc": "Let customers book electrical work online with a link that shows your real availability, offers planned jobs only, and drops straight onto your calendar.",
    "answer": "Put a booking link on your website, Google profile, and follow-up texts that shows your real availability and only offers planned work, like installs, inspections, and quotes. A homeowner picks an open slot in one tap, it lands on your calendar with the details, and true emergencies are still pointed to call you.",
    "sections": [
        {"h2_html": "Booking online only fits <em>the work that can wait</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every electrical call belongs in an online booking form, and getting that right is the first step. A no-power emergency or a burning smell should reach a person who can triage it, not a calendar. But planned work, an EV charger install, a panel inspection before a sale, adding a circuit or a ceiling fan, a quote for an upgrade, is a perfect fit, because the homeowner is happy to pick a time and you are happy to schedule it in advance.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The gap most electricians live with is phone tag on exactly that easy, plannable work. You are on a job, you call back that evening, they miss it, and two days later they booked whoever could lock in a time on the spot. Letting them self-schedule closes that gap without you touching the phone at all, and it tends to be the low-stakes jobs that quietly slip away this way. These are the jobs you would happily take, which is exactly what makes losing them to a missed callback so frustrating.</p>'},
        {"h2_html": "What a booking link needs to <em>do right</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A booking tool is only useful if it protects your day instead of filling it with chaos. It has to read your real calendar so it never double-books you against a job you already have, offer only the appointment types you choose, and leave you enough notice and drive time between visits. Put the link everywhere a customer already meets you, and planned work starts landing on your schedule while you are heads-down inside a panel.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Sync to the calendar you already use, so it can only ever offer times you are actually free.</li><li>Offer planned jobs only, and point anyone with a true emergency to call you instead.</li><li>Send an automatic confirmation and reminder, which is what cuts down no-shows on scheduled work.</li></ul>'}],
    "bridge_h2": "Let customers book the easy jobs themselves",
    "bridge_text": 'Online booking for electricians lets a homeowner pick a time for planned work straight from your website or a text link, on your real availability, so it never double-books you and every job lands on your calendar with the details you need. Emergencies still reach a person, and the routine work books itself.',
    "bridge_slug": "online-booking-for-electricians",
    "bridge_label": "See online booking for electricians",
    "faqs": [
        ("Will homeowners try to book real emergencies online?",
         'Only if you let the form offer that, and you should not. Set it up for planned work like installs, inspections, and quotes, and point anyone with a true no-power or safety problem to call you, where a person can triage how urgent it really is before anything goes on the calendar.'),
        ("Can it stop customers from booking back-to-back with no drive time?",
         'Yes. You set how much notice you need, how long each visit runs, and how much buffer to leave between jobs, so the calendar never books you into two places at once or with no time to get across town to the next one.')],
},
# ==================== 7. Invoices go out late -> Automation ====================
{
    "slug": "why-invoices-go-out-late",
    "trade_slug": "electricians", "trade_plural": "electricians",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "title": "Why Do My Invoices Always Go Out Late? | Top Shelf Business Solutions",
    "h1": "Why Do My Invoices Always Go Out Late?",
    "meta_desc": "Invoices go out late because you roll straight to the next job and billing waits for a free evening. Here is how to send them the moment a job is done.",
    "answer": "Invoices go out late because you finish a job and immediately roll to the next one, so billing waits for a quiet evening that rarely comes, and slow invoices mean slow cash. The fix is to send the invoice automatically the moment a job is marked done, then chase any unpaid ones without you remembering.",
    "sections": [
        {"h2_html": "The invoice loses to the <em>next job</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Late invoices are rarely a discipline problem. You finish a job, and the next one is already waiting, so billing gets pushed to the evening, and the evening fills up too. A stack of invoices sits waiting for a quiet hour that a busy electrician almost never gets, and every day one goes unsent is a day later you get paid. Slow billing quietly becomes slow cash, even when the work itself is going great and the schedule is packed.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The deeper cost is not only timing. An invoice sent a week late, after the memory of the job has faded, is harder to collect and easier for a customer to sit on. The closer the bill goes out to the moment the work was finished, the fresher it feels to the customer, and the faster and more reliably it tends to get paid. Cash that shows up a week sooner, on job after job, adds up to real breathing room for a small shop.</p>'},
        {"h2_html": "Send it the moment the job is <em>marked done</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The fix is to take the invoice out of your evening entirely. When a job is marked complete, the invoice can go out on its own, right then, while the work is fresh and the customer is satisfied. If it is not paid, a polite reminder can follow on a schedule without you keeping a mental list of who still owes you. You approve how it works once, and billing stops depending on you finding a free hour that never seems to arrive.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Trigger the invoice off job completion, not off you remembering to sit down and send it later.</li><li>Let unpaid invoices get automatic, polite reminders, so you are not chasing them by hand.</li><li>Keep it tied to the customer record, so the bill, the job, and the payment all live in one place.</li></ul>'}],
    "bridge_h2": "Take billing and follow-up off your evenings",
    "bridge_text": 'Automation for electricians sends the invoice the moment a job is marked done, chases unpaid ones with polite reminders, and follows up on your quotes and appointments, so nothing waits on you finding a free hour. Your cash comes in faster because the billing stops sitting in a pile on the dash.',
    "bridge_slug": "automation-for-electricians",
    "bridge_label": "See automation for electricians",
    "faqs": [
        ("Can the invoice really go out without me doing it?",
         'Yes. When you mark a job complete, the invoice can send on its own, and you can still review or adjust it first if you want to. The point is that billing happens right when the work is done instead of waiting for an evening that, for a busy electrician, never really comes.'),
        ("What about customers who do not pay on time?",
         'Unpaid invoices can get automatic, polite reminders on a schedule you set, so a late payer keeps hearing from you without you having to track it by hand. Steady, low-effort nudges tend to collect more than a bill that gets sent once and then quietly forgotten.')],
},
# ==================== 8. Not showing up on Google -> Websites & SEO ====================
{
    "slug": "not-showing-up-on-google",
    "trade_slug": "electricians", "trade_plural": "electricians",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "title": "Why Doesn't My Electrical Business Show Up On Google? | Top Shelf Business Solutions",
    "h1": "Why Doesn't My Electrical Business Show Up On Google?",
    "meta_desc": "Electricians miss Google usually because directories outrank a thin site and a stale Business Profile. Here is what to fix to rank locally for your city.",
    "answer": "Usually because directories like Angi outrank a thin or missing website, your Google Business Profile is incomplete or stale, and you have no pages built around your city and services. Google shows the electricians who look most established and local, so filling those gaps is what gets you into the results homeowners actually see.",
    "sections": [
        {"h2_html": "The usual reasons you are <em>invisible</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When an electrical business does not show up on Google, it is usually a handful of gaps stacked together, not one single mistake. The good news is that the common ones are simple to name, and every one of them is fixable once you know it is there.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Your website is thin, slow, or missing, so Google has little reason to rank it above a directory.</li><li>Your Google Business Profile is incomplete, unverified, or has not been touched in months, so it looks abandoned.</li><li>You have no pages built around your city and the services you offer, so you never match what homeowners actually type.</li><li>You have very few recent reviews, which is one of the signals that decides who appears in the local map results.</li></ul>'},
        {"h2_html": "Directories rank because they <em>work at it</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It can feel like Angi, Thumbtack, and Yelp have some unfair advantage, and in a way they do: they publish constantly and have years of authority behind them, so they outrank a site that was built once and then left alone. You are not going to beat them at their own game across the whole country, and you do not need to. What you can do is win the searches that are genuinely yours.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A homeowner searching for an electrician in your specific city, or for a panel upgrade or EV charger install nearby, is a search a local business can rank for, because a national directory has nothing local to say and your site can. Filling the gaps above, a real site, an active profile, city and service pages, fresh reviews, is what moves you into the results homeowners actually see. None of it is a trick; it is just the basic groundwork a directory does at scale and most local electricians never get around to.</p>'}],
    "bridge_h2": "Fix the gaps and show up for your city",
    "bridge_text": 'Websites and SEO for electricians builds a site that ranks for electrician near me in your city, keeps the pages and profile that Google rewards, and puts click-to-call on every page so a visit turns into a call. It is how you stop losing searches to a directory and start showing up for the work near you.',
    "bridge_slug": "websites-seo-for-electricians",
    "bridge_label": "See websites and SEO for electricians",
    "faqs": [
        ("How long does it take to start showing up on Google?",
         'Local, specific searches like your city plus a service can start moving within weeks, while broader terms take longer and build over months. There is no honest overnight fix, but the local searches a homeowner near you actually types are usually the fastest to improve.'),
        ("Do I need a website, or is a Google Business Profile enough?",
         'You want both, and they help each other. The profile is what often shows in the map results, but a real website gives Google something to rank and gives homeowners somewhere to call or request a quote. A profile with no site behind it leaves easy visibility on the table.')],
},
# ==================== 9. After-hours emergency calls -> AI receptionist ====================
{
    "slug": "after-hours-emergency-calls",
    "trade_slug": "electricians", "trade_plural": "electricians",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "title": "How Do I Stop Losing After-Hours Emergency Calls? | Top Shelf Business Solutions",
    "h1": "How Do I Stop Losing After-Hours Emergency Calls?",
    "meta_desc": "After-hours no-power and safety calls go to whoever answers first. Here is how 24/7 triage captures those emergencies instead of losing them to voicemail.",
    "answer": "Homeowners with no power or a burning smell at night will not leave a voicemail, they call down the list until someone answers. Stop losing them with 24/7 answering that triages the call, sorts a real hazard from a can-wait, books routine work, and flags a true emergency to you, instead of forwarding every call to your cell.",
    "sections": [
        {"h2_html": "After-hours callers do not <em>wait for you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An electrical emergency does not keep business hours. Power drops across half the house at 11 p.m., an outlet sparks on a Saturday, something smells hot on a Sunday, and the homeowner is scared and wants someone now. They will not leave a voicemail and wait until Monday. They call down the list until a person answers, and the electrician who picks up gets the work, which is often a panel replacement or an emergency service call that is real money.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So the after-hours calls you miss are not the small ones. They are frequently the most urgent and most valuable jobs there are, going straight to whoever happened to answer at the exact moment the homeowner was most motivated to say yes. Every one of those that rolls to voicemail is a job you were in line for and simply were not awake to catch.</p>'},
        {"h2_html": "Forwarding every call to your cell is <em>not the answer</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most electricians try to solve this by sending every after-hours call to their personal phone, and it burns them out fast. You cannot answer at dinner, on a date, or asleep at two in the morning, and half the calls that do wake you are routine questions that could have waited for daylight. You need every call answered, but you do not need every call to be yours to personally answer.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">What actually works is answering that catches every after-hours call, sorts a true hazard from a call that can wait, books the routine work for your next opening, and only pulls you in when something is genuinely urgent. You stop losing the emergencies to the next electrician on the list, and you stop being woken up for the ones that were never emergencies at all.</p>'}],
    "bridge_h2": "Answer every after-hours call without living on your phone",
    "bridge_text": 'An AI receptionist for electricians answers 24/7, triages the burning-smell and no-power calls the way you would, books routine work onto your schedule, and flags a true emergency to you right away. You keep the urgent jobs that used to roll to voicemail, and you keep your evenings.',
    "bridge_slug": "ai-receptionist-for-electricians",
    "bridge_label": "See the AI receptionist",
    "faqs": [
        ("How does it know the difference between an emergency and a routine call?",
         'It asks the questions you would: is there a burning smell, is anything sparking or hot, is there any power at all, has the breaker been reset. A genuine hazard gets flagged to you right away, while a call that can wait gets booked for your next opening instead of waking you up at two in the morning.'),
        ("Will customers be annoyed talking to an automated receptionist at night?",
         'At 11 p.m. with no power, what a homeowner wants is for someone to actually respond and take the problem seriously, which beats a voicemail box every time. It answers naturally and is upfront about what it is, and it gets them a real answer and a time instead of silence until Monday.')],
},
]
