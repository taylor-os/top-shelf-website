"""Colony page specs for PLUMBERS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a plumbing-business owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, plumber-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear; no em/en dashes anywhere; "find the gap", never "leak" as a
money metaphor (literal plumbing leaks like a burst pipe are fine).

Nine questions, mixed problem / how-to / cost, spread across all seven money pages:
  1 plumber-website-cost           (cost)     -> websites-seo-for-plumbers
  2 plumber-answering-service-cost (cost)     -> ai-receptionist-for-plumbers
  3 is-a-crm-worth-it              (cost)     -> crm-for-plumbers
  4 why-do-i-miss-emergency-calls  (problem)  -> ai-receptionist-for-plumbers
  5 why-do-my-quotes-go-unanswered (problem)  -> crm-for-plumbers
  6 why-am-i-not-on-google         (problem)  -> marketing-for-plumbers
  7 how-do-i-get-more-reviews      (how-to)   -> review-software-for-plumbers
  8 how-do-i-stop-phone-tag        (how-to)   -> online-booking-for-plumbers
  9 how-do-i-stop-no-shows         (how-to)   -> automation-for-plumbers
"""

TOPICS = [
# ==================== How Much Does a Plumber Website Cost? (cost -> websites-seo) ====================
{
    "slug": "plumber-website-cost",
    "h1": "How Much Does a Plumber Website Cost?",
    "title": "How Much Does a Plumber Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A plumber website ranges from cheap templates to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A plumber website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more than the price is whether it ranks and captures calls. Top Shelf builds a custom five page site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number you see quoted for a plumber website swings wildly because you are not all buying the same thing. A cheap template you fill in yourself and a custom site built to rank in your service area are different products with the same name. Before you compare quotes, it helps to know what you are actually paying for.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A do-it-yourself website builder is cheap monthly, but you do the work, and it is rarely built to rank or to convert a homeowner searching in a hurry.</li><li>A one-time custom build costs more up front and is yours to keep, but a site alone does little if nobody is doing the ongoing SEO to get it found.</li><li>An agency retainer bundles the build with ongoing SEO and updates, which is where most of the long-term value lives, and also where the monthly cost lives.</li><li>Hidden costs to ask about before you sign: who owns the site, what a change costs, and whether you keep it if you leave.</li></ul>'},
        {"h2_html": "What a plumber should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A plumber website earns its money one way: it turns a homeowner searching in a hurry into a call on your phone. That means it has to load fast, rank for the towns you cover and the searches people make when something breaks, and put a tap-to-call button in front of a visitor before they scroll. A beautiful site that never ranks and buries your number is the most expensive kind, because you paid for it and it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that pays for itself",
    "bridge_text": "A plumber website is only worth what it brings in. Ours is built to rank for the towns you cover and turn searches into calls, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-plumbers",
    "bridge_label": "Websites & SEO for plumbers",
    "faqs": [
        ("Is a cheap template site good enough to start with?",
         "It can get you online, but a template you fill in yourself is rarely built to rank or to convert a homeowner in a hurry, and you do the work of maintaining it. If a site is not getting found or turning visitors into calls, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "plumbers", "trade_plural": "plumbers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ What Does a Plumber Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "plumber-answering-service-cost",
    "h1": "What Does a Plumber Answering Service Cost?",
    "title": "What Does a Plumber Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for plumbers often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for plumbers usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call 24/7 and books the job comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. A plumber also gets the most calls at the worst times for a live service: nights, weekends, and the first hard freeze, when after-hours minutes tend to cost the most. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of tire-kickers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty caller or a slow operator costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner with water spreading across the floor does not leave a voicemail, they call the next plumber. The real cost of no coverage is not a monthly fee, it is the emergency job that went to the shop that picked up. But a generic call center reading a script cannot tell a slab leak from a running toilet, so you can pay for coverage and still get bad triage.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, triages like you would, and books the job or flags a true emergency to your phone. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One emergency job you would have lost on a weekend can be worth well more than the plan costs, and everything it catches after that is on top. We will not pretend it replaces your judgment on a real emergency, it hands those straight to you.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, tells a burst pipe from a drip, and books it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-plumbers",
    "bridge_label": "AI receptionist for plumbers",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the after-hours emergency it books instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or holidays?",
         "No. It answers 24/7 as part of the plan, including the 2am burst pipe and the holiday sewage backup that are often your best-paying jobs, with no after-hours surcharge or overage.")],
    "trade_slug": "plumbers", "trade_plural": "plumbers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============== Is a CRM Worth It for a Plumbing Company? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it",
    "h1": "Is a CRM Worth It for a Plumbing Company?",
    "title": "Is a CRM Worth It for a Plumbing Company? | Top Shelf Business Solutions",
    "meta_desc": "For most plumbers a CRM pays for itself by rescuing one cold quote and reviving past customers. It comes in Top Shelf's Signature plan at $899/mo, not a separate bill.",
    "answer": "For most plumbing companies, yes. A CRM pays for itself the first time it wins back a quote you would have let go cold, or brings a past customer back for a water heater. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a plumbing company when you have more quotes and past customers than you can personally keep track of, which is most established shops. It is not worth it if you are a one-person operation doing a handful of jobs a week and genuinely calling everyone back, though that rarely stays true as you grow. The honest test is simple: how many quotes have you sent in the last month that you never followed up on, and how many past customers have not heard from you in a year? Those are the jobs a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a plumber is not the software, it is the work that stops slipping through. A homeowner sitting on a water heater bid, a family whose faucet you fixed two years ago, a maintenance visit that is overdue: each one is a job you have already half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open quote on a schedule, so a homeowner comparing three bids keeps hearing from you while the other two go quiet.</li><li>It fires maintenance reminders, a water heater flush, a drain cleaning, a sump pump check, so recurring work comes back without you tracking dates.</li><li>It keeps your whole customer list and job history in one place instead of a truck full of paper and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one job you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your customer list to work",
    "bridge_text": "The quotes and past customers you already have are the cheapest jobs you can get. A CRM follows up on every one for you, so they call you next instead of the shop that stayed in touch.",
    "bridge_slug": "crm-for-plumbers",
    "bridge_label": "CRM for plumbers",
    "faqs": [
        ("Is a CRM overkill for a small plumbing business?",
         "Not usually. Even a one or two truck shop sends more quotes and services more homes than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If quotes go cold and past customers forget your name, a CRM earns its keep."),
        ("How is a CRM different from keeping numbers in my phone?",
         "A phone full of contacts does not follow up on a quote, does not remember who is due for maintenance, and does not tell you which job is going cold. A CRM does all of that on a schedule, so the repeat work shows up instead of depending on you to remember.")],
    "trade_slug": "plumbers", "trade_plural": "plumbers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do I Miss So Many Emergency Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-do-i-miss-emergency-calls",
    "h1": "Why Do I Miss So Many Emergency Calls?",
    "title": "Why Do I Miss So Many Emergency Calls? | Top Shelf Business Solutions",
    "meta_desc": "You miss emergency calls because they ring while your hands are full, and a homeowner with water spreading does not leave a voicemail, they call the next plumber.",
    "answer": "You miss emergency calls because they come when your hands are full, under a sink, in a crawlspace, or driving to the last job, and a homeowner with water spreading does not leave a voicemail. They hang up and call the next plumber. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Plumbing is a hands-full trade. When the phone rings you are often under a sink with a wrench, in a crawlspace with no signal, on a ladder, or driving between jobs, and none of those are moments you can stop and take a call. The busier you are, the more calls you miss, which means your best weeks are also the ones where the most work slips away. It is not a discipline problem. One person cannot do the job in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for an emergency it is not one. A homeowner watching water come through the ceiling is not going to leave a message and wait. They move down the list until someone answers, and by the time you check your phone, the job is already gone.</p>'},
        {"h2_html": "Missed emergencies are your most <em>expensive misses</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A missed emergency, a burst pipe, a sewage backup, no water at all, is the highest-margin work you can get, and it comes when every other shop is closed too. Those after-hours calls are exactly the ones a homeowner will pay a premium for, and exactly the ones most likely to roll to voicemail. So the calls you are most likely to miss are also the ones worth the most.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can tell an emergency apart from a call that can wait. A voicemail box cannot triage, and a generic call center does not know a slab leak from a running toilet. What actually works is something that answers on the first ring day or night, asks whether the water is shut off, gets the address, and either books the visit or flags a true emergency straight to your phone, so you decide whether to roll a truck without ever missing the call in the first place.</p>'}],
    "bridge_h2": "Stop losing emergencies to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, tells a burst pipe from a drip, and books it or flags it to you, so the emergency never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-plumbers",
    "bridge_label": "AI receptionist for plumbers",
    "faqs": [
        ("Would a customer rather reach a real person?",
         "In an emergency, what a homeowner needs most is to know a real plumber is handling it, and a calm voice that captures the details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, and hands true emergencies straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are under a sink, on a ladder, or already on another call. Something that always answers and triages is what catches the calls a forward would still miss.")],
    "trade_slug": "plumbers", "trade_plural": "plumbers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do My Plumbing Quotes Go Unanswered? (problem -> crm) ============
{
    "slug": "why-do-my-quotes-go-unanswered",
    "h1": "Why Do My Plumbing Quotes Go Unanswered?",
    "title": "Why Do My Plumbing Quotes Go Unanswered? | Top Shelf Business Solutions",
    "meta_desc": "Most plumbing quotes go quiet not over price but because nobody followed up. The homeowner got busy or took other bids, and the job went to whoever checked back in.",
    "answer": "Most plumbing quotes go unanswered not because your price was wrong, but because nobody followed up. The homeowner got busy, gathered other bids, or simply forgot, and the job went to whoever checked back in. A quote that goes quiet is usually not a no, it is a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "Silence usually means forgotten, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet quote as a no on price, so you drop it and move on. But most of the time the homeowner did not decide against you at all. They asked for a bid on a water heater or a repipe, meant to think it over, and then life got in the way. They are juggling two other quotes, a work schedule, and a dozen other decisions, and yours slid down the pile. A week later they could not tell you the difference between the three plumbers who came out.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The one who gets the job is usually not the cheapest. It is the one who stayed in front of them: a friendly check-in a couple of days later, a quick note answering the question they were stuck on. That second touch is what turns a maybe into a booked job, and it is exactly the thing there is no time for between service calls.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Plumbers do not skip follow-up because they are lazy. They skip it because the day fills up. You finish a job, roll to the next, handle the emergency that jumped the line, and by evening the quote you sent Tuesday is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest quotes to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which quotes are still open and going cold.</li><li>The follow-up depends on you remembering, so it competes with the actual work and loses.</li><li>By the time you circle back, the homeowner has already booked someone who beat you to it.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open quote gets a couple of timed check-ins automatically, written to sound like you, the homeowner comparing bids keeps hearing from you while the others go silent, and the work you already quoted stops slipping away.</p>'}],
    "bridge_h2": "Follow up on every quote, automatically",
    "bridge_text": "A CRM keeps every open quote in front of you and sends timed check-ins for you, so a homeowner comparing bids keeps hearing from you while the other plumbers go quiet.",
    "bridge_slug": "crm-for-plumbers",
    "bridge_label": "CRM for plumbers",
    "faqs": [
        ("How many times should I follow up on a plumbing quote?",
         "A couple of light touches over the first week or two catches most of the maybes without being pushy: a check-in a few days after the quote, then a short note answering common questions. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly check-in reads as attentive, not spammy, and most homeowners appreciate the nudge because they meant to get back to you and forgot. You can always jump in and message anyone directly.")],
    "trade_slug": "plumbers", "trade_plural": "plumbers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== Why Isn't My Plumbing Business Showing Up on Google? (problem -> marketing) ========
{
    "slug": "why-am-i-not-on-google",
    "h1": "Why Isn't My Plumbing Business Showing Up on Google?",
    "title": "Why Isn't My Plumbing Business Showing Up on Google? | Top Shelf Business Solutions",
    "meta_desc": "Hard to find on Google? Usually it is your Google Business Profile, not your website. The map pack is where local plumbing calls actually start.",
    "answer": "Usually it is your Google Business Profile, not your website. When someone searches for a plumber near them, Google shows the map pack first, those three local listings with star ratings. If your profile is incomplete, unverified, or has few recent reviews, you sit below shops that keep theirs active, no matter how good your work is.",
    "sections": [
        {"h2_html": "The map pack is the real <em>front door</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a homeowner searches for a plumber near them, the first thing Google shows is not a website at all. It is the map pack, the little map with three local listings, star ratings, and a call button. Most people pick from those three without ever scrolling to the regular results below. So if you are wondering why the phone is quiet even though you have a website, the answer is usually that you are not in those three, and almost nobody is looking past them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting into the map pack is a different job from having a website. It runs on your Google Business Profile: whether it is verified, complete, and active, how close you are to the searcher, and how many recent, genuine reviews you have. A great website with a neglected profile is a nice brochure nobody sees at the moment they are choosing who to call.</p>'},
        {"h2_html": "What keeps a plumber <em>off the map</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">If you are not showing up, it is usually one of a handful of fixable things, not a mystery. Google tends to trust profiles that look active and legitimate, and quietly buries the ones that look abandoned or incomplete.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>The profile is unverified, missing, or has the wrong service area, hours, or categories.</li><li>Few reviews, or none in months, so you look inactive next to a shop collecting them steadily.</li><li>No recent posts or photos, so the profile reads as stale.</li><li>Inconsistent name, address, and phone number across the web, which makes Google unsure you are one real business.</li><li>You are simply farther from the searcher than competitors, which matters more the bigger your area is.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of these require a new website. They require getting the profile verified and complete, keeping it active, and building a steady flow of real reviews. Do that consistently and a neglected profile can climb over a few weeks, then compound. What no one can honestly promise is a specific spot on the map, because Google decides that, but the levers above are the ones that move it.</p>'}],
    "bridge_h2": "Get seen where the calls start",
    "bridge_text": "Most local plumbing calls begin in the map pack. Keeping your Google profile verified, active, and full of recent reviews is how you show up there when a pipe breaks nearby.",
    "bridge_slug": "marketing-for-plumbers",
    "bridge_label": "Marketing for plumbers",
    "faqs": [
        ("Do I need a website to show up on Google Maps?",
         "Not to appear in the map pack, which runs on your Google Business Profile. A website helps you rank in the results below the map and gives the profile something to link to, but the fastest way onto the map itself is a verified, active, well-reviewed profile."),
        ("How long until my plumbing business shows up?",
         "A neglected profile that gets verified, completed, and active can start climbing within a few weeks, and it compounds as reviews and posts build. Nobody controls Google, so no honest company promises a specific position, but consistency on the profile is what moves it.")],
    "trade_slug": "plumbers", "trade_plural": "plumbers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==== How Do I Get More Google Reviews for My Plumbing Business? (how-to -> review-software) ====
{
    "slug": "how-do-i-get-more-reviews",
    "h1": "How Do I Get More Google Reviews for My Plumbing Business?",
    "title": "How Do I Get More Google Reviews for My Plumbing Business? | Top Shelf Business Solutions",
    "meta_desc": "Get more Google reviews by asking every happy customer the moment the job is done and making it one tap. The relief right after a fix is when they are most willing.",
    "answer": "Ask every happy customer right when the job is done and the water is running again, and make leaving a review a single tap. Most plumbers do good work but forget to ask, or ask too late. Sending the request automatically at that moment of relief, with a direct link, is what steadily grows your reviews.",
    "sections": [
        {"h2_html": "The problem is timing and asking, not your <em>work</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most plumbers have plenty of happy customers and not many reviews, and the gap is not the quality of the work. It is that asking gets forgotten, feels awkward at the door, or happens too late. The best moment to ask is the one most plumbers miss: right after the water is running again and the customer is standing there relieved the crisis is over. Wait until you are packing the truck and it slips your mind. Ask three weeks later and the relief, along with the motivation, is gone.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The second problem is friction. Even a willing customer will not hunt down your profile, log in, and figure out where to click. Every extra step loses a share of the people who meant to leave a review. If leaving one is not close to a single tap, most of the goodwill you earned never makes it online.</p>'},
        {"h2_html": "How to actually get more, <em>consistently</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more reviews is less about a clever trick and more about doing the same simple thing after every single job, which is exactly what tends to fall apart when you are busy. A repeatable process beats good intentions.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Ask every happy customer, every time, not just the ones you remember, so it is never left to chance.</li><li>Ask at the right moment, right after the job is done, when relief is highest.</li><li>Make it one tap with a direct link straight to your Google profile, by text and email.</li><li>Reply to every review, good or bad, which reassures the next reader and helps your local ranking.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Doing all that by hand after each job is what slips first on a busy week. Software fixes it by sending the ask automatically the moment a job is marked done, so the request goes out every time without you thinking about it. One rule keeps you on the right side of Google: ask every customer honestly, and never filter out unhappy ones or pay for reviews.</p>'}],
    "bridge_h2": "Turn every finished job into a review",
    "bridge_text": "Review software asks every happy customer the moment the job is done and makes it one tap, so the reviews build on their own and the next searcher calls you first.",
    "bridge_slug": "review-software-for-plumbers",
    "bridge_label": "Review software for plumbers",
    "faqs": [
        ("Is asking customers for reviews against Google policy?",
         "Asking every customer for an honest review is allowed and encouraged. What is not allowed is filtering out unhappy customers, offering incentives, or paying for reviews. Asking everyone at the right moment and making it easy is squarely within the rules."),
        ("What should I do about a bad review?",
         "Reply calmly and professionally rather than ignoring it. One measured response sitting under a wall of genuine positive reviews often reassures the next reader more than a spotless record would. The faster you know about it the better, which is why being alerted the moment one lands helps.")],
    "trade_slug": "plumbers", "trade_plural": "plumbers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ How Do I Stop Playing Phone Tag With Customers? (how-to -> online-booking) ============
{
    "slug": "how-do-i-stop-phone-tag",
    "h1": "How Do I Stop Playing Phone Tag With Customers?",
    "title": "How Do I Stop Playing Phone Tag With Customers? | Top Shelf Business Solutions",
    "meta_desc": "Stop phone tag by letting customers book non-emergency plumbing work themselves online, on your real availability, so routine jobs get scheduled without a callback.",
    "answer": "Stop phone tag by letting customers schedule non-emergency work themselves. A lot of plumbing, quotes, drain cleanings, faucet installs, inspections, is not urgent, and those callers would happily book online if you let them. A booking link on your real availability turns the back-and-forth into an appointment that lands on your calendar while you work.",
    "sections": [
        {"h2_html": "Phone tag is quietly costing you <em>routine jobs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every plumbing job is a 2am emergency. A homeowner wants a quote on a water heater, a drain snaked, or a faucet swapped, and none of it needs a phone call this minute. But the way most shops handle it forces one anyway: the customer calls during the day, you are on a job, you call back at five, they are at dinner, and two days of voicemail tag later they booked the plumber who made it easier. The job was never the problem. The back-and-forth was.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Every one of those handoffs is a place the customer can drop out. When someone is motivated enough to reach out, making them wait for a callback is the surest way to lose a routine job you should have had, especially to a competitor whose site let them just pick a time.</p>'},
        {"h2_html": "Let the routine work <em>book itself</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The fix is to let customers schedule the non-urgent work themselves, on your real availability, without ever reaching you first. A booking link lets a homeowner grab an open slot the moment they think of it, at night or on a lunch break, and you wake up to the appointment already set with the details attached. That does not mean handing your calendar to a flooding kitchen. A good booking flow asks what is going on first and points a true emergency, active leak, sewage, no water, straight to your phone to call now, while only genuinely routine work self-schedules.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">You stay in control of it. You set which jobs are bookable online, how long each takes, how much notice you need, and how much drive-time buffer to leave, so you are never booked with no way to get there. It syncs to the calendar you already use so it cannot double-book a tech, and it sends a confirmation and reminder that cut down no-shows. The phone tag disappears and the routine jobs stop slipping to whoever was easier to book.</p>'}],
    "bridge_h2": "Let customers book without the callback",
    "bridge_text": "Online booking lets routine plumbing jobs schedule themselves on your real availability, while true emergencies still get pointed to your phone, so you stop trading voicemails.",
    "bridge_slug": "online-booking-for-plumbers",
    "bridge_label": "Online booking for plumbers",
    "faqs": [
        ("Will online booking send emergencies to a slot three days out?",
         "Not if it is set up right. The booking form asks what is going on first, and a true emergency like an active leak, sewage, or no water is pointed straight to your emergency line to call now. Only the work you mark as routine can self-schedule."),
        ("Can I control which jobs customers can book?",
         "Yes. You decide which job types are bookable online, how long each runs, how much notice you need, and how much buffer to leave for drive time. Everything else still comes through a call, so you keep control of your day.")],
    "trade_slug": "plumbers", "trade_plural": "plumbers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ How Do I Stop No-Shows and Wasted Trips? (how-to -> automation) ============
{
    "slug": "how-do-i-stop-no-shows",
    "h1": "How Do I Stop No-Shows and Wasted Trips?",
    "title": "How Do I Stop No-Shows and Wasted Trips? | Top Shelf Business Solutions",
    "meta_desc": "Cut no-shows with automatic confirmations and reminders before every visit, plus on-my-way texts, so customers are home and trucks stop rolling to empty houses.",
    "answer": "Send automatic confirmations and reminders by text before every visit, and an on-my-way message when your tech heads out. Most no-shows happen because a customer forgot or did not know when to expect you, not because they meant to waste your time. A quick, timed reminder is the single biggest lever on empty-house trips.",
    "sections": [
        {"h2_html": "Most no-shows are forgotten, not <em>deliberate</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A plumber driving to an empty house is an hour and a tank of gas you never get back, plus a slot a paying job could have filled. It is tempting to blame flaky customers, but most no-shows are not deliberate. The appointment was made days ago, nobody reminded them, and it fell off their calendar the same way a quote falls off yours. Others are not sure when in a wide window you will actually arrive, so they run an errand and miss you.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That means most wasted trips are preventable with information, not enforcement. A customer who gets a clear confirmation, a reminder the day before, and a heads-up when you are on the way is far more likely to be standing there when you pull up. The gap is not the customer, it is that nobody told them what to expect.</p>'},
        {"h2_html": "The reminders that actually keep <em>trucks moving</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason these reminders do not happen is the same reason follow-up does not: you are busy doing the work, and stopping to text every customer to confirm tomorrow is exactly what slips on a full day. So it either does not happen, or it eats time you do not have. Automating it means it happens every time without anyone working the phones.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A confirmation when the appointment is booked, so it lands on their calendar.</li><li>A reminder the day before, with an easy way to reschedule instead of just not being home.</li><li>An on-my-way text with a realistic arrival window when the tech leaves, so they know when to expect you.</li><li>A quick note if the schedule slips, so a running-late job does not turn into a missed one.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">For an owner running a couple of trucks, that is a fuller, tighter schedule without anyone stopping to make confirmation calls. The same automation can carry the follow-up after the job, a review request and a maintenance reminder, so the visit keeps paying off long after the truck pulls away.</p>'}],
    "bridge_h2": "Keep your trucks moving, not idling",
    "bridge_text": "Automation sends confirmations, reminders, and on-my-way texts for you, so customers are home when you arrive and your techs stop driving to empty houses.",
    "bridge_slug": "automation-for-plumbers",
    "bridge_label": "Automation for plumbers",
    "faqs": [
        ("Do reminder texts really cut no-shows?",
         "They are the single biggest lever on it. Automatic confirmations and reminders before a visit, plus an on-my-way text, keep the appointment top of mind and give the customer an easy way to reschedule instead of simply not being home. Fewer empty-house trips is usually the first thing owners notice."),
        ("Will setting all this up take more time than it saves?",
         "The setup is done once and then it runs on its own. The sequences are built around how you already schedule your day, so after that the confirmations, reminders, and on-my-way texts send automatically without you or a dispatcher working the phones for each stop.")],
    "trade_slug": "plumbers", "trade_plural": "plumbers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
