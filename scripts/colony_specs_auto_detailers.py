"""Colony page specs for AUTO DETAILERS (plan section 5 "Problem/symptom" colony + section 6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question an auto-detailing owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Auto detailing is its own animal, not repair or body work. It is appointment-based COSMETIC
work booked ahead, wash, interior, paint correction, ceramic coating, headlight restoration.
The revenue base is packages plus recurring maintenance plans plus gift options, split across
mobile and shop. Discovery is image-driven and Instagram-fed (before-and-after proof). The
detailer is elbow-deep in a car with a machine running and cannot answer the phone, and the
retention engine is rebooking on a maintenance cadence, not a one-time repair. Every dict below
owns UNIQUE, hand-written, detailer-specific substance (the generator owns shell, schema,
events, keyword placement).

Same honesty rules as the money specs: no invented stats, percentages, prices, or clients;
hedge instead of overpromise; only the real Top Shelf prices ($299/$899/$2,500 plans, $1,500
one-time site) ever appear, and the detailer's OWN package pricing stays generic with no
numbers; the AI receptionist does scheduling and intake ONLY and hands judgment calls to the
owner; no em/en dashes anywhere; the word "leak" is never used as a money metaphor.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 auto-detailing-website-cost              (cost)    -> websites-seo-for-auto-detailers
  2 auto-detailing-answering-service-cost    (cost)    -> ai-receptionist-for-auto-detailers
  3 is-a-crm-worth-it-for-an-auto-detailer   (cost)    -> crm-for-auto-detailers
  4 why-auto-detailers-miss-calls            (problem) -> ai-receptionist-for-auto-detailers
  5 why-detailing-clients-dont-rebook        (problem) -> crm-for-auto-detailers
  6 how-do-auto-detailers-get-more-clients   (how-to)  -> marketing-for-auto-detailers
"""

TOPICS = [
# ============ How Much Does an Auto Detailing Website Cost? (cost -> websites-seo) ============
{
    "slug": "auto-detailing-website-cost",
    "h1": "How Much Does an Auto Detailing Website Cost?",
    "title": "How Much Does an Auto Detailing Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "An auto detailing website runs from cheap DIY templates to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "An auto detailing website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more than the price is whether it shows your work, ranks for detailing near you, and lets people book. Top Shelf builds a custom five page site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What a detailing website actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A detailing website is not a brochure, it is a showroom. People choose a detailer with their eyes, so before anyone reads a word they want to see the work: a gloss black hood after a correction, a trashed interior brought back to new, a coated car catching the light. The site has to load fast on a phone, put that finished work up front, and make it obvious how to book, because most of your visitors found you by searching for something specific and are ready to act.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Show the transformation, a gallery of before and after cars, so a visitor sees proof instead of promises.</li><li>Rank for how people actually search, mobile detailing near me, ceramic coating near me, interior detailing in your town, so you are found the moment someone wants it.</li><li>Make booking close to one tap, a clear path to request a slot or a package, not a phone number buried at the bottom.</li><li>Lay out your packages and any gift options plainly, so a visitor can see what you offer and choose without a back and forth.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A site that does those things turns a search into a booked car. A pretty page that never ranks and hides your work and your booking button is the expensive kind, because you paid for it and it sends you nothing.</p>'},
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Once you know what the site has to do, the price differences make more sense. You are not all buying the same thing, and the cheap number and the high one are often different products with the same name. Before you compare quotes, it helps to know what you are actually paying for.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A do-it-yourself builder is cheap each month, but you build and maintain it, and it is rarely set up to rank or to turn a scroller into a booking.</li><li>A one-time custom build costs more up front and is yours to keep, though a site alone does little if no one is doing the ongoing SEO that gets it found.</li><li>An agency retainer bundles the build with ongoing SEO and updates, which is where most of the long-term value sits, and also where the monthly cost sits.</li><li>Questions to ask before you sign: who owns the site, what a change costs, and whether you keep it if you leave.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that gets it ranking is handled for you. There is no setup fee either way. No honest company can promise a specific ranking by a specific date, because no one controls Google, but a free audit can show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a detailing site that books cars",
    "bridge_text": "A detailing website earns its keep by turning a search into a booked car. Ours is built to show your finished work, rank for the detailing people search near you, and make booking close to one tap, then wired to follow up on every lead.",
    "bridge_slug": "websites-seo-for-auto-detailers",
    "bridge_label": "Websites & SEO for auto detailers",
    "faqs": [
        ("Do I still need a website if I have an Instagram full of my work?",
         "Instagram is great for showing details and building trust, but you do not own it, it does not rank on Google when someone searches for a detailer near them, and it is hard to book from. A website is the home base people find when they search and the place they actually schedule, with your Instagram feeding it."),
        ("What is the most affordable way to get a good detailing site?",
         "On any monthly plan starting at $299 the site is included, with the ongoing SEO handled for you. If you would rather own it outright, the one-time custom build is $1,500 with no setup fee. A cheap DIY template can get you online, but it rarely ranks or turns visitors into booked cars.")],
    "trade_slug": "auto_detailers", "trade_plural": "auto detailers",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ======== What Does an Auto Detailing Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "auto-detailing-answering-service-cost",
    "h1": "What Does an Auto Detailing Answering Service Cost?",
    "title": "What Does an Auto Detailing Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for auto detailers often bill per call or minute. Top Shelf includes an AI receptionist that books every call in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for auto detailers usually bill per call, per minute, or a monthly retainer, so a busy stretch runs up the bill, and a generic call center cannot tell a maintenance wash from a paint correction. Top Shelf takes a different approach: an AI receptionist that answers and books the job comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they handle, which sounds fair until a good week turns into a big bill. A detailer gets these calls in the middle of a job, hands full and a machine running, and the people calling are comparing two or three detailers to book, so the busier you are the more you miss and the more a metered service costs at the same time. It helps to know the common models before you sign one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per call pricing: you pay for each call answered, so a busy week or a run of price shoppers runs up the cost.</li><li>Per minute pricing: you pay for talk time, so a chatty caller or a slow operator costs more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of calls or minutes, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a customer pricing a full detail or a coating is calling down a list, and if you do not pick up they book the detailer who did. The real cost of no coverage is not a monthly fee, it is the booked car that went to someone else. But a generic call center reading a script cannot do a detailer intake. It does not know a maintenance wash from a multi stage correction, whether the customer wants mobile or drop off, or what the vehicle needs, so you can pay for coverage and still get a useless message.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, asks what your intake would, and books the appointment on your calendar, or for work that needs eyes on the car first captures the vehicle and its condition and books a consultation. It comes in the Signature plan, flat, at $899 a month, with no per call or per minute meter running. One ceramic coating booked, or one customer who signs onto a recurring maintenance plan, is often worth more than the plan costs for months, and everything after that is on top. It handles the scheduling and the intake, and it hands the judgment calls, like pricing a heavy correction, straight to you.</p>'}],
    "bridge_h2": "Answer every booking call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers every booking call, does a real detailing intake, and schedules it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-auto-detailers",
    "bridge_label": "AI receptionist for auto detailers",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the booking it captures instead of losing to voicemail while your hands are on a car."),
        ("Does it cost extra for evenings or weekends?",
         "No. It answers as part of the plan whenever the phone rings, including the lunch break and the evening when people actually call to compare detailers, with no surcharge or overage. It does the scheduling and intake and flags anything that needs your judgment to you.")],
    "trade_slug": "auto_detailers", "trade_plural": "auto detailers",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Is a CRM Worth It for an Auto Detailer? (cost -> crm) ============
{
    "slug": "is-a-crm-worth-it-for-an-auto-detailer",
    "h1": "Is a CRM Worth It for an Auto Detailer?",
    "title": "Is a CRM Worth It for an Auto Detailer? | Top Shelf Business Solutions",
    "meta_desc": "For most auto detailers a CRM pays for itself by reviving one cold coating quote and rebooking past customers. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most auto detailers, yes. A CRM pays for itself the first time it revives a coating quote you would have let go cold, or brings a past customer back for a maintenance wash. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a detailer when you have more quotes and past cars than you can personally keep track of, which is most shops past their first year. It is not worth it if you are a brand new one person operation doing a couple of cars a week and genuinely reaching out to everyone, though that rarely stays true as you grow. The honest test is simple: how many coating or correction quotes have you given in the last month that you never followed up on, and how many cars you detailed a year ago have not heard from you since? Those are the jobs a CRM is built to bring back.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a detailer is not the software, it is the work that stops slipping away. A customer sitting on a coating quote, a car you detailed last season that is due for a refresh, a coating that needs its maintenance wash to keep the warranty: each one is a booking you have half earned and are one reminder away from filling.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open quote on a schedule, so a customer comparing detailers keeps hearing from you while the others go quiet.</li><li>It fires maintenance and coating care reminders, so the recurring wash and the annual interior come back around without you tracking a single date.</li><li>It sends seasonal nudges at the right time, a cleanup after winter grime, a fresh detail before summer trips, a protective coat before the salt and cold.</li><li>It keeps your whole customer list and every vehicle history in one place instead of a phone full of texts and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow up that feed it. The math is the same as the answering service: bring back one job you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your customer list to work",
    "bridge_text": "The quotes and past cars you already have are the cheapest bookings you can get. A CRM follows up on every one for you, so they book you next instead of the detailer who stayed in touch.",
    "bridge_slug": "crm-for-auto-detailers",
    "bridge_label": "CRM for auto detailers",
    "faqs": [
        ("Is a CRM overkill for a small detailing business?",
         "Not usually. Even a one van operation details more cars and gives more quotes than anyone can track by memory. The point is not size, it is whether follow up is falling through. If coating quotes go cold and past customers forget to rebook, a CRM earns its keep."),
        ("How is a CRM different from keeping customers in my phone?",
         "A phone full of contacts does not follow up on a quote, does not know whose coating is due for its maintenance wash, and does not tell you which car is overdue for a refresh. A CRM does all of that on a schedule, so the repeat work shows up instead of depending on you to remember.")],
    "trade_slug": "auto_detailers", "trade_plural": "auto detailers",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Why Do I Miss So Many Booking Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-auto-detailers-miss-calls",
    "h1": "Why Do I Miss So Many Booking Calls?",
    "title": "Why Do I Miss So Many Booking Calls? | Top Shelf Business Solutions",
    "meta_desc": "Auto detailers miss calls because they ring while your hands are on a car, and a customer booking a detail will not leave a voicemail, they book whoever answered.",
    "answer": "You miss calls because they come while your hands are on a car, gloves on, a polisher or extractor running, or you are mobile in a driveway across town. A customer calling to book a detail will not leave a voicemail, they book the next detailer who answers. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes while your <em>hands are on the car</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Detailing is a hands full trade. When the phone rings you are often leaned into a back seat with an extractor, running a polisher across a hood, or parked in a driveway two towns over with a foam cannon in hand, and none of those are moments you can stop and take a call. The busier you are, the more calls you miss, which means your best weeks are the ones where the most work slips by. It is not a discipline problem. One person cannot detail the car in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a booking call it is not one. Someone pricing a detail is calling two or three shops in a row, and they are not going to leave a message and wait. They book whoever picks up, and by the time you peel off your gloves and check your phone, the car is already scheduled somewhere else.</p>'},
        {"h2_html": "The calls you miss are the ones worth <em>the most</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. The higher ticket cosmetic work, a full paint correction, a ceramic coating, a customer signing onto a recurring maintenance plan, is exactly the kind of call that comes in while you are heads down on another car with a machine running. So the calls you are most likely to miss are also the ones worth the most, and they go to the detailer who happened to be free to talk.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that answers on the first ring and can do a real detailer intake, not a voicemail box and not a call center reading a script. What actually works is something that picks up while your hands stay on the car, asks what the vehicle needs and whether they want it mobile or at your shop, gathers the vehicle and the address, and either books it on your calendar or captures the details and books a consultation, flagging it to your phone. It handles the scheduling and intake so the booking never rolls to voicemail in the first place, and leaves the judgment calls to you.</p>'}],
    "bridge_h2": "Stop sending bookings to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring while your hands stay on the car, does a real detailing intake, and books it or flags it to you, so the booking never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-auto-detailers",
    "bridge_label": "AI receptionist for auto detailers",
    "faqs": [
        ("Would a customer rather reach a real person?",
         "On a booking call, what a customer wants most is to get their car scheduled, and a natural voice that captures the vehicle and the details beats a voicemail box every time. The AI receptionist is upfront about what it is, does the intake, and hands anything that needs your judgment straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are mid polish, elbow deep in an interior, or on a mobile job. Something that always answers and does the intake is what catches the calls a forward would still miss.")],
    "trade_slug": "auto_detailers", "trade_plural": "auto detailers",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Why Don't My Detailing Customers Come Back? (problem -> crm) ============
{
    "slug": "why-detailing-clients-dont-rebook",
    "h1": "Why Don't My Detailing Customers Come Back?",
    "title": "Why Don't My Detailing Customers Come Back? | Top Shelf Business Solutions",
    "meta_desc": "Detailing customers stop coming back not because they were unhappy, but because nothing reminded them the coating, interior, or seasonal detail was due again.",
    "answer": "Usually not because they were unhappy, but because nothing reminded them. A detailed car looks great for months, so the customer never thinks about the next wash or seasonal detail, and with no nudge they drift until they stumble onto whoever is easiest. Rebooking runs on a reminder, not on the quality of the work.",
    "sections": [
        {"h2_html": "A clean car is the reason they <em>forget to come back</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Here is the quiet irony of good detailing: you do such careful work that the car stays looking new for months, so nothing forces the next visit the way a broken thing does in other trades. The coating you applied quietly needs its maintenance wash on a schedule to hold its warranty. The interior you restored slowly gets lived in again. Road grime and salt build up over a season without any single moment that says it is time. The customer is not being disloyal, they simply are not thinking about their car right now, and no one has told them the next detail is due.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So the booking does not go to a competitor who out sold you. It goes to whoever the customer happens to find when the car finally bothers them enough to look, which might be you and might not. The work was never the problem. The silence after it was.</p>'},
        {"h2_html": "Rebooking runs on a <em>cadence, not memory</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You cannot personally remember when a few hundred past cars are each due for their next visit, and trying to do it by memory means it only happens when you are slow, which is exactly when you have the fewest customers to reach. A steady, light touch at the right moment is what keeps you the name they book, and it is the kind of thing you set up once and then it just runs.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A reminder that a coating is due for its maintenance wash, so the warranty stays intact and the car comes back to you.</li><li>A nudge that it has been several months since the last full detail, timed to how often that customer tends to come in.</li><li>Seasonal timing, a cleanup after winter grime, a refresh before summer road trips, a protective coat before the salt and cold.</li><li>A reason to reach out at the right moment, a car about to be sold, a lease coming back, a big trip ahead.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of it depends on you remembering between jobs, and all of it is written to sound like you, sent at a sensible pace. The repeat work that used to drift away comes back on a cadence instead, from the customer list you already have.</p>'}],
    "bridge_h2": "Turn every detail into the next one",
    "bridge_text": "The cars you have already detailed are the cheapest bookings you can get. A CRM reminds each customer when their coating, interior, or seasonal detail is due, written to sound like you, so they come back to you instead of drifting off.",
    "bridge_slug": "crm-for-auto-detailers",
    "bridge_label": "CRM for auto detailers",
    "faqs": [
        ("How often should I reach out to past detailing customers?",
         "Tie it to the service rather than a fixed calendar: a coating on its maintenance wash interval, a full detail every several months, a seasonal check in. The exact timing matters less than that it happens on time and every time, which is what a CRM handles for you."),
        ("Will reminders annoy my customers?",
         "Not when they are spaced sensibly and written to sound like you. Most customers appreciate the nudge, because they meant to book their next detail and simply forgot the car was due. You can always jump in and message anyone directly.")],
    "trade_slug": "auto_detailers", "trade_plural": "auto detailers",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ How Do I Get More Detailing Customers? (how-to -> marketing) ============
{
    "slug": "how-do-auto-detailers-get-more-clients",
    "h1": "How Do I Get More Detailing Customers?",
    "title": "How Do I Get More Detailing Customers? | Top Shelf Business Solutions",
    "meta_desc": "Auto detailers get more customers by being findable when people search detailing near them and letting before-and-after photos of finished cars do the selling.",
    "answer": "Two things together: be findable the moment someone searches for detailing near them, with a verified Google Business Profile and a site that ranks, and make your finished work visible where people scroll, with before and after photos and real reviews. Detailing is sold with images and proof, so being seen and being searchable is most of the battle.",
    "sections": [
        {"h2_html": "Be findable the moment someone <em>wants a detail</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone decides they want their car detailed, they search, and the first thing Google shows is not a website, it is the map pack, the little map with three local listings, star ratings, and a call button. Most people pick from those three. So if the phone is quiet even though you do great work, the usual reason is that you are not in those three, and almost no one scrolls past them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting there runs on your Google Business Profile: whether it is verified, complete, and active, how close you are to the searcher, and how many recent, genuine reviews you have. Reviews matter more for a detailer than for most trades, because a customer is handing over a car they care about, and for a mobile job, letting you into their driveway. A steady stream of real reviews is often what tips a first time caller. No one controls Google, so no honest company promises a specific spot, but a verified, active, well reviewed profile is the lever that moves it.</p>'},
        {"h2_html": "Let your <em>finished work</em> do the selling",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Detailing is a visual trade, and discovery is visual too. People decide with their eyes, so the single best thing you can show a stranger is the transformation: a swirl free hood after a correction, a trashed interior brought back to new, water beading on a fresh coat. Proof like that turns a scroller into a caller in a way that words cannot.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Post a steady stream of before and after photos where people already scroll, so your work keeps showing up.</li><li>Keep your Google profile full of recent photos and reviews, not set up once and forgotten.</li><li>Give your website a gallery that ranks and shows the range of what you do, from a maintenance wash to a multi stage correction.</li><li>Make your packages and any gift options easy to see and easy to book, so an interested visitor does not have to ask.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Being seen brings new customers in, and staying in touch keeps them, so the work compounds instead of starting from zero every month. The honest part: none of this is an overnight switch and no one can promise a ranking, but showing up where people search and letting your finished cars do the talking is what steadily fills a detailing calendar.</p>'}],
    "bridge_h2": "Get seen where the bookings start",
    "bridge_text": "Most detailing customers begin with a search or a scroll. Keeping your Google profile active and full of reviews, and your finished work in front of people, is how you show up when someone nearby wants their car detailed.",
    "bridge_slug": "marketing-for-auto-detailers",
    "bridge_label": "Marketing for auto detailers",
    "faqs": [
        ("Is Instagram or Google more important for getting detailing customers?",
         "They do different jobs. Social shows your work and builds trust with people who come across you, while Google, your profile and your site, catches people actively searching to book a detailer right now. You want both, but the search side is where the ready to book customers are."),
        ("Do reviews really matter for a detailer?",
         "A lot. Handing over a car they care about, and for mobile work their driveway, is a trust decision, and a steady stream of recent, genuine reviews on your Google profile is often what tips a first time caller to you. Ask every happy customer honestly, and never filter out unhappy ones or pay for reviews.")],
    "trade_slug": "auto_detailers", "trade_plural": "auto detailers",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
]
