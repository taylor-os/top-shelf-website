"""Per-page content specs for the SEO corpus (plan §5), Window Cleaning batch.
generate_corpus.py imports SPECS from a specs module; each dict is one page's UNIQUE,
hand-written, trade-specific content. The generator owns the mechanics (shell, schema,
events, interlinks, keyword placement); the spec owns the substance that clears the
uniqueness gate. Never templated find-and-replace, never the pressure-washing content
reworded.

Window cleaning runs on RECURRING WORK, not the one-off blast. Residential glass is a
quarterly or twice-a-year cadence, and commercial storefronts, offices, restaurants, and
property-manager routes are weekly or monthly contracts, which is the recurring-revenue
goldmine and the CRM's core lever. The crew is up a ladder or moving down a route with a
squeegee in hand and cannot answer, so the estimate and booking calls drop. The value is
landing standing accounts and dense routes, following up open quotes, converting one-time
cleans into plans, and reactivating past residential customers by season (spring, and the
weeks before the holidays). Marketing runs on streak-free reviews and the map pack rather
than a dramatic before-and-after, because clean glass does not photograph the way a
pressure-washed driveway does. A fast site with an instant quote and a recurring-plan
signup beats renting your own calls back from a lead-seller.

This batch is four pages (the ai-receptionist dict carries "demo": True). Each example
body ends with the literal "Illustrative example, not a client." per the honesty rule; if
the generator also appends that line, dedupe there.
"""

SPECS = [
# ==================== AI Receptionist for Window Cleaning ====================
{
    "slug": "ai-receptionist-for-window-cleaning", "demo": True,
    "trade_slug": "window_cleaning", "trade_plural": "window cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "AI Receptionist for Window Cleaning",
    "title": "AI Receptionist for Window Cleaning | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Window Cleaning",
    "meta_desc": "A window cleaning answering service answers every quote call while your crew is up a ladder or on a route, then books the estimate on your calendar.",
    "service_schema_name": "AI Receptionist for Window Cleaning",
    "eyebrow": "For Window Cleaning",
    "h1_html": "AI Receptionist <em>for Window Cleaning</em>",
    "answer_block": "A window cleaning answering service answers every quote call the moment it rings, even while your crew is up a ladder or working down a route with a squeegee in hand, finds out whether it is a home or a storefront and how often they want it done, and books the estimate straight onto your calendar.",
    "sections": [
        {"h2_html": "The quote call you miss is the recurring account that <em>signs with someone else</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner who wants a regular clean, or a shop manager who wants the storefront glass done every couple of weeks, is not loyal to anyone yet. They found a few window cleaners on Google, they are calling down the list, and they book the first one that answers and can come give a price. Whoever picks up usually wins, and the real prize is not one clean, it is a standing account that renews on its own for years. But you are up a ladder with both hands on a pole, or three stops into a route with a squeegee going, and you cannot come off the glass to answer. The call rolls to voicemail, a caller shopping around does not leave one, and that recurring account goes to whoever picked up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An AI receptionist answers on the first ring even while you are mid-wash on a second story, sounds like someone who knows the trade, finds out whether it is a house or a commercial storefront, how many windows and stories, inside and out or just outside, and how often they want it done, then books the estimate or the recurring visit straight onto your calendar. The account gets captured instead of lost to the company that happened to be free to answer.</p>'},
        {"h2_html": "Built around how a <em>window cleaning crew actually works</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your phone rings hardest at the worst possible moment to answer it. You are steadying a ladder against a second-story window, running a squeegee down a storefront pane, or driving between the stops on the day route, and that is exactly when the estimate and scheduling calls come in. A voicemail box cannot qualify a job, and a generic call center reading a script does not know an inside-and-out house clean from a monthly storefront route, or why a three-story home with hard-to-reach glass is a different quote than a single-story ranch.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers every call while your crew is up a ladder, mid-squeegee, or driving between stops, so no estimate rolls to voicemail.</li><li>Knows the work: an inside-and-out residential clean, a recurring quarterly, a storefront on a weekly or monthly route, screens and tracks, hard water spots, and post-construction glass.</li><li>Gets the address, the number of windows and stories, and how often they want it, then books the estimate or the recurring visit and texts you the details on the spot.</li><li>Tells a one-time caller apart from someone who wants a standing plan, so the recurring accounts worth the most never land in a voicemail box.</li></ul>'},
        {"h2_html": "The math is <em>one account that renews on its own</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not need it to catch many calls to come out ahead. One storefront that signs a monthly route, or one household that puts a quarterly clean on autopilot, is worth far more over a year than a single clean. Everything it books after that first save is extra. The point is simple: stop handing standing accounts, the steadiest money in this trade, to whichever company happened to be next to a quiet phone.</p>'},
        {"h2_html": "You own the number, the calls, and the <em>customer list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing business number, or a new one registered in your name, not ours. Every caller, every address, and every job detail is yours and exportable any time, so the recurring customer list you build is an asset you keep instead of something you rent back month to month. There is no long contract holding your data. The answering service is one piece of the Top Shelf platform, and it hands every call it captures to the same CRM that follows up on the quote and keeps each recurring account on schedule, so a clean you booked never quietly falls off the route.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A storefront route, signed while your <em>crew is on a ladder</em>",
        "body_html": "A shop manager on a busy street is tired of fingerprints and grime on the front glass and wants it cleaned every couple of weeks. She calls three window cleaners on her lunch break. Two go to voicemail, and a manager who wants it handled does not leave one, she keeps dialing. Yours answers, asks how many panes and how often, and books an estimate for the next morning while a note pings your phone. Your crew never came off the ladder. You turn a lunch-hour call into a standing account that cleans itself onto the schedule every two weeks. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current phone number?",
         "Yes. It can answer on your existing business number, or set up a new one registered in your name. Either way the number and every call that comes through it belong to you and go with you if you ever leave."),
        ("Can it actually quote a job over the phone?",
         "It does not throw out a firm price sight unseen, and you would not want it to. It gathers exactly what you need to quote, whether it is a home or a storefront, how many windows and stories, inside and out or just outside, screens and tracks, and how often they want it, then books the estimate or the recurring visit on your calendar so you can price it right."),
        ("Can it handle a caller who wants regular service?",
         "Yes, and that is where it earns its keep in this trade. When a storefront or a household asks about a weekly, monthly, or quarterly clean, it captures how often and what they want and books the first visit, so the standing accounts that are the steadiest money in window cleaning get caught instead of going to voicemail."),
        ("Is it going to sound like a robot?",
         "It answers naturally and is upfront rather than pretending to be a person. A homeowner or a shop manager who just wants their glass cleaned mostly needs to know a real company is handling it and someone will come give a price, and a steady voice that captures the details beats a voicemail box every time. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your services, your questions, and your calendar for you, so it is answering in days, not weeks. Start with a free audit and we will show you what your current setup is missing.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for window cleaning companies"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-window-cleaning.html", "The CRM that follows up on every call you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing recurring accounts to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many estimate calls and standing accounts your current setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ========================= CRM for Window Cleaning =========================
{
    "slug": "crm-for-window-cleaning",
    "trade_slug": "window_cleaning", "trade_plural": "window cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "CRM for Window Cleaning",
    "title": "CRM for Window Cleaning | Top Shelf Business Solutions",
    "og_title": "CRM for Window Cleaning",
    "meta_desc": "A CRM for window cleaning companies follows up on every quote and keeps each recurring account on schedule, so one-time cleans turn into standing plans.",
    "service_schema_name": "CRM for Window Cleaning",
    "eyebrow": "For Window Cleaning",
    "h1_html": "CRM <em>for Window Cleaning</em>",
    "answer_block": "A CRM for window cleaning companies keeps every lead, past customer, and recurring account in one place and follows up for you, so the quote a homeowner is sitting on turns into a standing plan and the storefront you cleaned once stays on a route that renews on its own. Your customer list quietly becomes recurring revenue.",
    "sections": [
        {"h2_html": "The quotes you sent are jobs you are losing, and the <em>one-time cleans are plans you never offered</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most window cleaning companies do not have a lead problem, they have a follow-up problem, and a plan problem. You quote a house or a storefront, they say they want to think about it, and then you get busy on the route and never circle back. They booked whoever followed up, and often that was not you. And the ones who did book usually booked a single clean, when a quick nudge could have turned it into a quarterly plan that runs on its own. Both the open quote and the one-time clean were money left sitting on the table.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every open quote in front of you and follows up on a schedule you set, and it prompts you to offer a recurring plan to the customer who just booked a one-off, all with texts and emails that go out on time whether or not you remember. The quote comes back around, and the single clean turns into an account that renews.</p>'},
        {"h2_html": "Windows get dirty again on a <em>schedule you can set your watch by</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This is what makes a CRM worth more in window cleaning than almost anywhere. Glass does not stay clean. Rain spots it, dust films it, sprinklers streak it, and pollen and fingerprints are back within weeks, so a house you did in spring genuinely needs it again by late summer, and a busy storefront needs it far sooner than that. That is not a problem, it is a standing appointment nobody has booked yet. The customer who loved their spotless windows would happily have it done on a regular cadence, but they forget, and they forget your name, and next time they search and hire whoever turns up first.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every customer, address, service history, and note lives in one place instead of a truck full of scribbled quotes and your memory.</li><li>Recurring visits fire on their own cadence, a quarterly or twice-a-year residential clean, a weekly or monthly storefront route, so the next visit is booked before the glass is dirty again.</li><li>Seasonal reminders go out at the moments people actually notice the glass, spring cleaning and the weeks before the holidays when guests are coming, so past customers rebook without you chasing them.</li></ul>'},
        {"h2_html": "Commercial routes are the <em>recurring revenue this trade is built on</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner is worth coming back to a few times a year. A storefront that wants spotless glass for every customer who walks up, an office, a restaurant, a medical suite, or a property manager with a row of units is worth coming back every week or every month, on a contract. That recurring commercial work is the steadiest, most predictable money in window cleaning, and it lives or dies on staying organized: knowing which route runs which day, when each account is due, and who to invoice. A CRM holds every account and its cadence, and because you can see them by area, you can build dense routes where a day is full of nearby stops instead of windshield time. The recurring revenue keeps rolling instead of slipping because you lost track of a rotation.</p>'},
        {"h2_html": "You own the list, and it <em>works with everything else</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every customer and every note is yours and exportable any time, not locked inside software you rent. The CRM is one piece of the Top Shelf platform and connects to the answering service, so a call it answers lands in your database and gets followed up on automatically, and to online booking and review requests, so a finished clean logs against the right account with its full history and cadence attached and quietly asks a happy customer for a review. Nothing you have earned falls off the route.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The house that becomes a <em>standing quarterly</em>",
        "body_html": "You clean a family home inside and out in the spring, and they pay for the single job and thank you. Normally that is the last you hear from them until they happen to remember you, if they ever do. Instead the CRM has you offer a quarterly plan on the spot, and when they are not ready, it sends a friendly reminder as the summer haze and sprinkler spots build back up. They rebook, and this time they say yes to the standing plan. A row of storefronts two blocks over signs a monthly after a check-in, and now that whole street is one dense afternoon on your route every month. You never sat down to chase any of it. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing customers and past jobs?",
         "Yes. Your current customers, leads, and job history come in and live in one place, and everything stays yours and exportable. The point is to make the customer list you already have actually work for you."),
        ("Will it really follow up on quotes automatically?",
         "Yes, on the schedule you approve. An open quote gets a check-in a few days later and another after that, all sent for you, so a homeowner or a manager comparing prices keeps hearing from you while the other companies go quiet. You can jump in and message anyone directly any time."),
        ("Can it turn one-time cleans into recurring plans?",
         "Yes, and this is where it pays off most in window cleaning. It prompts you to offer a plan when someone books a single clean, and it sends the residential and seasonal reminders, a quarterly, a twice-a-year, a touch-up before the holidays, so the cleans that always come due again turn into bookings that come with them."),
        ("Can it handle my commercial and storefront routes?",
         "Yes. Recurring accounts, which day each route runs, and what is due all live in the CRM, and you can see them by area to keep routes dense, so a weekly storefront or a monthly office stays on schedule and gets invoiced instead of slipping because you lost track of when you were last there."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your customers, build your follow-up and reminder sequences, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will show you where jobs are slipping through today.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for window cleaning companies"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-window-cleaning.html", "The answering service that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting quotes and accounts <em>go cold</em>",
    "cta_sub": "Get a free audit of how many of your quotes and past customers are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ======================= Marketing for Window Cleaning =======================
# ===================== Websites & SEO for Window Cleaning =====================
{
    "slug": "websites-seo-for-window-cleaning",
    "trade_slug": "window_cleaning", "trade_plural": "window cleaning companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "Websites & SEO for Window Cleaning",
    "title": "Websites & SEO for Window Cleaning | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Window Cleaning",
    "meta_desc": "A window cleaning website built for SEO ranks for window cleaning near me and captures the quote or recurring-plan signup directly, not a lead-seller.",
    "service_schema_name": "Websites & SEO for Window Cleaning",
    "eyebrow": "For Window Cleaning",
    "h1_html": "Websites &amp; SEO <em>for Window Cleaning</em>",
    "answer_block": "A window cleaning website built for SEO ranks for the searches people make when the glass looks spotted, window cleaning near me, residential and commercial window washing in your city, and captures the quote or the recurring-plan signup directly, so the account is yours instead of a lead-seller renting it back to you.",
    "sections": [
        {"h2_html": "The lead-sellers are not competing with you, they are <em>renting you back your own calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for window cleaning in your town and the top of the page is often a directory, a national booking middleman, or a pay-per-lead service, not the local company doing the actual work. Those sites publish thousands of pages and carry years of authority, so a homeowner or a business searching lands there first, fills out a form, and that lead gets sold, sometimes to three companies at once, sometimes back to you for a fee out of your own margin. It stings more in this trade, because the lead they sold you as a single job could have been a recurring account worth many cleans a year. Your site not ranking is not a vanity problem. It is the reason a call you should have gotten for free gets sold back to you.</p>'},
        {"h2_html": "Rank for what people type when the <em>glass looks spotted</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national directory this year for the broadest term, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you cover, and for the exact searches people make when they are finally fed up with the spots: window cleaning near me, residential window washing in your city, commercial and storefront window cleaning, screen and track cleaning, hard water stain removal, post-construction window cleaning. Pages built around the services you actually offer and the areas you actually serve are what search engines, and people ready to book, reward with the click. The commercial and specialty searches especially are ones a national directory never bothers to answer well, and every one of them is a page you can own outright, and a doorway to a recurring account rather than a single clean.</p>'},
        {"h2_html": "Make the quote, and the <em>recurring plan, one tap away</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most of these searches happen on a phone, so the site has to be fast and it has to be easy. A quick, obvious way to request a quote, describe the home or the storefront, say how many windows and stories, and enter the address, turns a visitor into a lead right there. But window cleaning has an advantage most trades do not: the best customers do not want a one-time job, they want it handled on a schedule. A site that lets someone sign up for a quarterly residential clean, or ask about a storefront route, right on the page, captures the recurring account at the exact moment they are motivated, instead of hoping they call back later. A pretty site that buries the quote button, or only ever sells a single clean, is a wasted opportunity.</p>'},
        {"h2_html": "The calls and accounts are <em>yours</em>, permanently",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you put into a pay-per-lead service disappears the day you stop paying, and the lead was never really yours anyway. A website you own keeps ranking, keeps capturing quote requests and plan signups, and keeps compounding in value for as long as it exists, and it is registered to you, not a platform that can drop you or sell the same lead to your competition. The site plugs into the same CRM that follows up on every quote it captures and keeps each recurring account on schedule, and the answering service that picks up the calls it drives, so nothing it earns you falls off the route.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A spotted-glass search finds <em>you</em>, not a directory",
        "body_html": "A homeowner two neighborhoods over finally gets tired of looking through windows spotted with rain and sprinkler marks and searches window cleaning near me on a phone. Instead of a national directory that would sell the lead to three companies, they find your site ranking for that area, with a page about residential window cleaning, real reviews about streak-free results, and a quote request right at the top. They enter how many windows and their address, and because the page offers it, they choose a quarterly plan instead of a single clean. It lands in your system as a recurring account that is yours alone. You paid nothing per lead, and no middleman ever touched it. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the residential, commercial, and specialty searches a national directory has no reason to target well, storefront window cleaning, hard water removal, post-construction cleanup in your city, which is exactly where a local company can win."),
        ("How is this different from paying for leads?",
         "A pay-per-lead service rents you a call that it also sells to your competitors, and it stops the day you stop paying. A website you own captures quotes and recurring-plan signups that are yours alone and keeps working long after it is built, without a per-lead fee coming out of every job, which stings even more when that lead could have been a standing account."),
        ("Can visitors sign up for regular service right from the site?",
         "Yes, and in window cleaning that is the whole point. The site is built so a visitor can request a quote in a tap and, when they are ready, sign up for a recurring residential plan or ask about a storefront route, so you capture a standing account at the moment they are motivated instead of hoping they call back. It lands straight in your CRM."),
        ("I do a lot of commercial and storefront work. Does a website help with that?",
         "Yes. Business owners and property managers search too, and they read your site to decide whether you look reliable enough to put on a standing contract. Pages built around commercial and storefront window cleaning, with real reviews and an easy way to ask about a route, are what win that recurring work."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks; broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for window cleaning companies"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and lead-sellers taking your calls, whether you work with us or not. No credit card, never a call center.",
},
]
