"""Per-page content specs for the SEO corpus (plan §5), auto detailing batch. Same contract
as scripts/corpus_specs.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, auto-detailing-specific substance that clears the uniqueness gate.
Never templated find-and-replace, never the plumber, auto-repair, or auto-body content reworded.

Auto hub, detailing angle. This is deliberately distinct from the general auto-repair batch
(mechanical service, drop-offs, warning lights) and the auto-body batch (collision, insurance
claims): detailing is appointment-based cosmetic care, interior and exterior details, paint
correction, ceramic coating, headlight restoration, often mobile and booked ahead rather than a
walk-in. The engine is the before-and-after photo and short video, and the goldmine is recurring
maintenance-wash plans and reactivated past customers. Four service angles are here in one file
(the ai-receptionist dict carries "demo": True). Each example body ends with the literal
"Illustrative example, not a client." per the honesty rule; if the generator also appends that
line, dedupe there.
"""

SPECS = [
# ==================== AI Receptionist for Auto Detailers ====================
{
    "slug": "ai-receptionist-for-auto-detailers", "demo": True,
    "trade_slug": "auto_detailing", "trade_plural": "auto detailers",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "AI Receptionist for Auto Detailers",
    "title": "AI Receptionist for Auto Detailers | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Auto Detailers",
    "meta_desc": "An auto detailing answering service answers every booking call while you are elbow-deep in a car with the buffer running, then books the appointment for you.",
    "service_schema_name": "AI Receptionist for Auto Detailers",
    "eyebrow": "For Auto Detailers",
    "h1_html": "AI Receptionist <em>for Auto Detailers</em>",
    "answer_block": "An auto detailing answering service answers every call the moment it rings, even when you are elbow-deep in an interior or running a buffer. It captures what the car needs and where, books it on your calendar, and keeps your own number yours, so the booking belongs to you, not the shop that picked up.",
    "sections": [
        {"h2_html": "The call you cannot take while the buffer is running is the detail that <em>books someone else</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A detail is booked ahead, not walked in, so the person calling you is calling to schedule and price a job, and they are calling two or three detailers in a row to do it. The trouble is that you are the one doing the work. You are leaned into a back seat with an extractor, running a polisher across a hood, or parked in a driveway two towns over with a foam cannon in hand, and you cannot stop mid-panel to grab the phone. So the call rolls to voicemail, and a customer who wants their car booked this week does not leave one. They simply book the detailer who answered.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An auto detailing answering service answers on the first ring while your hands stay on the car. It finds out what the vehicle needs, an interior clean-up, a full detail, paint correction, a ceramic coating, and either books it on your calendar or flags the details to you. The job is scheduled instead of handed to whoever happened to be free to talk.</p>'},
        {"h2_html": "Built around how a <em>detailer actually gets calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A detailing phone does not ring with emergencies. It rings with people who want a price and a slot: what does a full interior and exterior run, can you fit a ceramic coating in this month, do you come to the house, how long will the car be tied up. Those calls land in the middle of a job, when your hands are wet and a machine is running, and every one you miss is a booking that goes to the next name on the search. A voicemail box cannot quote a job, and a generic call center reading a script does not know a maintenance wash from a multi-stage paint correction, or what a headlight restoration even is.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers while you work, so a customer pricing a detail reaches a real answer instead of a voicemail and books with you.</li><li>Asks what your intake would: the vehicle, its condition, which service they are after, and whether they want it mobile at their place or dropped to you.</li><li>Gathers the vehicle, the service, and the address, books the appointment on your calendar, and texts you the details so the day is already planned.</li><li>Treats a repeat client or a maintenance-plan member differently from a first-time caller, so the customers who keep your calendar full never hit a voicemail.</li></ul>'},
        {"h2_html": "The math is <em>one coating or one plan</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not need to catch many calls for this to pay for itself. A single ceramic coating or paint-correction booking, or one customer who signs onto a recurring maintenance-wash plan, is often worth more than the system costs for months, and the higher-ticket cosmetic work is exactly the kind of call that comes in while you are busy on another car. Everything it books after that first save is on top. The point is to stop handing your best jobs to the detailer who simply answered faster while your hands were full.</p>'},
        {"h2_html": "You own the number, the calls, and the <em>customer list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It runs on the business number you already hand out, or a fresh one put in your name, never ours. Every caller, every vehicle, and every note stays yours and exports whenever you want, so the customer list you build is something you own outright, not something a vendor rents back to you by the month, and no contract locks your data away. The AI receptionist is one piece of the Top Shelf platform, and paired with the CRM on the Signature plan it drops every call it captures into the same system that chases the quote, so a booking or a maintenance reminder never quietly slips.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A ceramic coating, booked while you were <em>heads-down on a polisher</em>",
        "body_html": "A customer decides they finally want their new truck ceramic coated and calls three detailers on their lunch break to compare. You are in the middle of a two-stage polish with gloves on and the machine running, so on any other day the call goes to voicemail and they book whoever picks up. Instead the receptionist answers, asks about the vehicle and whether they want the coating at your shop or their home, and books a consultation for Thursday while flagging it to your phone. You finish the panel to find the job already on your calendar, with the vehicle, the service, and the address attached. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current business number?",
         "Yes. It can answer on the number you already use, or set up a new one registered in your name. Either way the number and every call that comes through it belong to you and go with you if you ever leave."),
        ("Can it handle mobile jobs and get an address to travel to?",
         "Yes. It asks whether the customer wants the detail done at your shop or at their home or office, gathers the address and the vehicle, and books it against your calendar with drive time in mind, so a mobile day is planned instead of scattered."),
        ("Will it actually book the job, or just take a message?",
         "It books. A wash or a standard detail lands straight on your calendar, and for work that needs eyes on the car first, like paint correction or a coating, it captures the vehicle and its condition, books a consultation, and texts you everything so the day is set."),
        ("Is it going to sound like a robot to my customers?",
         "It answers naturally and is upfront instead of pretending to be a person. A customer who just wants to know a real detailer can get to their car cares that the call was answered and the details were caught, not that a receptionist picked up. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your services, your calendar, and your booking rules for you, so it is answering in days, not weeks. Start with a free audit and we will show you what your current phone setup is missing.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for auto detailers"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-auto-detailers.html", "The CRM that follows up on every call you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop sending bookings to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many booking and quote calls your current phone setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ========================= CRM for Auto Detailers =========================
{
    "slug": "crm-for-auto-detailers",
    "trade_slug": "auto_detailing", "trade_plural": "auto detailers",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "CRM for Auto Detailers",
    "title": "CRM for Auto Detailers | Top Shelf Business Solutions",
    "og_title": "CRM for Auto Detailers",
    "meta_desc": "A CRM for auto detailing follows up on every quote and past customer for you, so a car you detail once keeps booking maintenance washes and seasonal details.",
    "service_schema_name": "CRM for Auto Detailers",
    "eyebrow": "For Auto Detailers",
    "h1_html": "CRM <em>for Auto Detailers</em>",
    "answer_block": "A CRM for auto detailing keeps every customer, vehicle, and open quote in one place and follows up for you, so the ceramic coating a customer is deciding on and the client whose car you detailed six months ago both book you again instead of the detailer who stayed in touch. Your customer list becomes your calendar.",
    "sections": [
        {"h2_html": "The quotes you already gave are the details you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A detailer with steady work does not usually have a lead problem. They have a follow-up problem. Someone asks what a ceramic coating or a full paint correction will run, you give them a number, they say they want to think about it or wait for payday, and then you are heads-down on the next car and never circle back. They price it with two other detailers, and the job goes to whoever followed up, not always the lowest number. The quote was never dead. It just needed one more text a few days later, and that is the thing there is never time for between jobs.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every open quote in front of you and follows up on a schedule you set, by text and email, whether or not you remember. The customer weighing a coating or a correction hears from you again while the other detailers go quiet, and the booking comes back to you.</p>'},
        {"h2_html": "Every car you detail is a customer <em>on a cycle</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Detailing is not a one-time job the way people assume. A car that got a full detail is due for a maintenance wash in a few weeks, the ceramic coating you applied wants a proper decontamination wash on a schedule to keep its warranty, and the interior you restored will need it again next season. Past customers are the cheapest work a detailer can get, because they already trust you with a car they care about and with their driveway. But you cannot personally remember when a few hundred past customers are each due, so most of that repeat work slips to whoever they stumble onto when they finally think about it.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every customer, vehicle, service history, and note lives in one place instead of a phone full of texts and your memory.</li><li>Maintenance and coating-care reminders go out on schedule, so the recurring wash and the annual detail come back around without you tracking a single date.</li><li>Seasonal nudges land at the right time, a spring cleanup after winter grime, a fresh detail before summer road trips, a protective coat before the salt and cold.</li><li>You can see who has not been in for a while and reach the right customer with the right reminder at the right time.</li></ul>'},
        {"h2_html": "The customers due for a wash are a <em>goldmine sitting idle</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A customer whose car is overdue for a wash or a refresh is not being disloyal, they simply have not thought about it, and nothing forces the issue the way a real problem does in other trades. A steady, light touch, a note that their coating is due for its maintenance wash, a nudge that it has been six months since their last full detail, keeps you the name they book before the car bothers them enough to look elsewhere. Reactivating customers who are already due, and catching the ones with a specific reason to detail, a car about to be sold, a lease coming back, a big trip ahead, is some of the easiest work you will book all month, and it is sitting in the customer list you already have, waiting for a reason to reach out.</p>'},
        {"h2_html": "You own the list, and it works with the <em>rest of the system</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every customer and every vehicle record belongs to you and exports any time, never trapped inside software you rent. Because the CRM is part of the Top Shelf platform, a call the AI receptionist answers drops straight into your database and gets worked automatically, and it ties into online booking, so a scheduled detail is logged against the right customer with their whole history already attached. The CRM and the AI receptionist come together on the Signature plan, so nothing you have earned goes cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The coating quote that <em>closes itself</em>",
        "body_html": "A customer asks what it would cost to ceramic coat their new car, and you give them a price on the spot. They want to wait until after the holidays, so normally that is the last you hear of it. Instead the CRM sends a friendly check-in the following week and a short reminder a couple of weeks after that, both written to sound like you. The other two detailers they called never followed up, so when the customer is finally ready, yours is the only name still in front of them, and they book without shopping around again. You never sat down to chase it. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing customers and past jobs?",
         "Yes. Your current customers, vehicles, and service history come in and live in one place, and everything stays yours and exportable. The point is to make the customer list you already have actually work for you."),
        ("Will it really follow up on quotes automatically?",
         "Yes, on the schedule you approve. An open quote for a coating or a correction gets a check-in a few days later and another after that, all sent for you, so a customer comparing detailers keeps hearing from you while the others go quiet. You can jump in and message anyone directly any time."),
        ("Can it send maintenance-wash and seasonal reminders?",
         "Yes. You set the cadence, a maintenance wash on a coating, an annual interior detail, a seasonal cleanup before summer or winter, and the reminders go out automatically so recurring work comes back around without you tracking every date."),
        ("How is this different from just having customers in my phone?",
         "A phone full of contacts does not follow up, does not know whose coating is due for its wash, and does not tell you which quote is going cold. The CRM does all of that on a schedule, so the repeat and deferred work actually shows up instead of depending on you to remember."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your customers and vehicles, build your follow-up and reminder sequences, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will show you where jobs are slipping through today.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for auto detailers"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-auto-detailers.html", "The AI receptionist that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting quotes and customers <em>go cold</em>",
    "cta_sub": "Get a free audit of how many of your quotes and past customers are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ======================= Marketing for Auto Detailers =======================
{
    "slug": "marketing-for-auto-detailers",
    "trade_slug": "auto_detailing", "trade_plural": "auto detailers",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "Marketing for Auto Detailers",
    "title": "Marketing for Auto Detailers | Top Shelf Business Solutions",
    "og_title": "Marketing for Auto Detailers",
    "meta_desc": "Auto detailing marketing turns your before-and-after photos and short videos into bookings and keeps you visible on Google when someone nearby searches.",
    "service_schema_name": "Marketing for Auto Detailers",
    "eyebrow": "For Auto Detailers",
    "h1_html": "Marketing <em>for Auto Detailers</em>",
    "answer_block": "Auto detailing marketing puts your best work where people actually decide, your before-and-after photos and short videos on social, your reviews and Google Business Profile in local search, so the transformation you just pulled off becomes the reason a nearby car owner books you instead of the detailer who never shows their work.",
    "sections": [
        {"h2_html": "Detailing sells the <em>before and after</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">No other trade markets itself the way detailing does, because the work is the ad. A filthy interior brought back to new, swirl marks buffed out of a black hood until it reflects like glass, water beading across a fresh coat of ceramic, these are images that stop a thumb mid-scroll, and they sell the job better than any words you could write. A car owner does not want to read about your process. They want to see the result and picture their own car looking like that. If you are not capturing and showing that transformation, you are doing the hardest part of the marketing every single day and throwing the proof away.</p>'},
        {"h2_html": "Short video is where a detail <em>spreads on its own</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A single satisfying clip of a spotless extraction, a foam bath sheeting off a hood, or a paint correction turning haze into a mirror can reach far more people than a paid ad, because the platforms push it and viewers share it. Detailing is one of the few local trades where the work is genuinely fun to watch, and that is an advantage most detailers waste by never filming. The point is not to become a full-time creator. It is to turn the work you are already doing into a steady feed of short before-and-after videos and posts that keep your name in front of your area, so when someone finally decides their car needs help, yours is the detailer they already follow.</p>'},
        {"h2_html": "Be the detailer they can <em>find and trust nearby</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone searches for detailing near me, mobile detailing, or ceramic coating in their town, the map pack, those three local listings with the star ratings, is the first thing they see. A profile that sits untouched looks abandoned next to one with recent photos of real work, current services, and a steady stream of reviews. It matters even more for detailing than most trades, because a customer is either handing over the keys to a car they care about or inviting you into their driveway, and the reviews and the photos are how a stranger decides you are safe to trust with either. Keeping your Google Business Profile active and full of your best work is a standing advertisement in the exact spot people look.</p>'},
        {"h2_html": "Stay in front for the season, and for <em>past customers</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Detailing demand moves with the calendar, a deep clean when spring pollen and winter salt come off, protection before summer sun and road trips, gift certificates and pre-sale details around the holidays, and being visible right before each wave beats scrambling once it lands. A steady local presence, fresh before-and-after posts, the occasional tip on keeping a finish looking new, keeps you top of mind for the next detail and reminds past customers you are still the one to call. This is the public-facing side of the business, aimed at people who are not your customer yet; the private follow-up to the people already in your list is the CRM.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "One black hood, and the <em>whole town scrolls past it</em>",
        "body_html": "You spend a Saturday correcting the paint on a black sedan, and before you hand back the keys you film thirty seconds of the hood going from hazy and swirled to a clean mirror finish. It goes up that night. Over the next few days it works its way around your area, a few people share it, and two of them message you about their own cars, one asking about a coating and one about a full detail. You did not buy an ad. You showed the work you were already doing, and it went and found your next customers on its own. Illustrative example, not a client."},
    "faqs": [
        ("Do you post to my social media and Google profile for me?",
         "Yes. We help you turn the before-and-after photos and clips you capture on the job into a steady schedule of posts and Google updates, and keep your hours, services, and service area accurate, so your best work is always in front of your area."),
        ("I am not a videographer. Do I have to be good on camera?",
         "No. The work is the content, not you. A short clip of a transformation, filmed on your phone as you go, is what people want to see. We help you make capturing it a habit and turn what you shoot into posts, so you are never expected to perform on camera."),
        ("How is this different from the CRM follow-up?",
         "The CRM follows up privately with people already in your list. Marketing is the public-facing side, your social feed, your reviews, and your Google profile, aimed at car owners who are not your customer yet but need to find you and trust you before they book."),
        ("Does this work for a mobile detailer with no shop?",
         "Especially well. A mobile detailer has no storefront to be found by, so the photos, the videos, and a well-kept Google profile built around your service area are your storefront, and they are what let a nearby customer discover you and book you to their driveway."),
        ("How long before I see it working?",
         "A neglected profile can climb in the map pack within weeks once it is active and complete, and social builds as you post consistently. Setup is included, and a free audit will show you what your current online presence looks like to someone searching for a detailer near them today.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for auto detailers"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-auto-detailers.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Turn your best work into <em>your next booking</em>",
    "cta_sub": "Get a free audit of how visible you actually are on social and Google in your service area right now, whether you work with us or not. No credit card, never a call center.",
},
# ==================== Websites & SEO for Auto Detailers ====================
{
    "slug": "websites-seo-for-auto-detailers",
    "trade_slug": "auto_detailing", "trade_plural": "auto detailers",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "Websites & SEO for Auto Detailers",
    "title": "Websites & SEO for Auto Detailers | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Auto Detailers",
    "meta_desc": "An auto detailing website built for SEO ranks for detailing near me and ceramic coating, and books the job directly instead of a lead-seller.",
    "service_schema_name": "Websites & SEO for Auto Detailers",
    "eyebrow": "For Auto Detailers",
    "h1_html": "Websites &amp; SEO <em>for Auto Detailers</em>",
    "answer_block": "An auto detailing website built for SEO ranks for what a car owner searches when they want their car detailed, detailing near me, mobile detailing, ceramic coating in your city, shows the before-and-after work that convinces them, and lets them book in a couple of taps instead of a directory renting your bookings back to you.",
    "sections": [
        {"h2_html": "The lead-sellers are not competing with you, they are <em>renting you back your own bookings</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for a detailer in your area and the names at the very top are often not detailers at all. They are directories, national booking apps, and pay-per-lead services that have spent years stacking up pages and authority, so a car owner searching for a detail lands on them first. They fill out a form, and that request gets sold, sometimes to several detailers at once, sometimes rented straight back to you for a fee that comes out of the job. When your own site does not show up, that is not a bruised ego. It is the reason a booking you should have earned for free arrives with a middleman attached, or goes to whoever paid the most that week.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A site of your own turns that same search into a booking that lands with you and nobody else, with the customer, the vehicle, and the job in your hands from the first click, and nobody skimming a cut of work you did yourself.</p>'},
        {"h2_html": "Rank for what a car owner types when they <em>want their car detailed</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You are not going to top a national directory this year on the widest, most generic term, and you do not have to. You can rank for your own name, for the specific towns and neighborhoods you cover, and for the exact searches a car owner makes when they want their car handled: detailing near me, mobile detailing, ceramic coating in your city, interior detailing, paint correction, headlight restoration. Pages built around the services you actually offer, and around whether you travel to the customer or they come to you, are what earn the click from both the search engine and the car owner who is ready to book.</p>'},
        {"h2_html": "Your site is your <em>portfolio, and it should book while you sleep</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A detail is a discretionary purchase, so a car owner deciding to spend on one wants two things before they commit: proof you do beautiful work, and an easy way to book without a phone call. The site has to load fast, lead with a gallery of your real before-and-after work, make your service area and whether you travel obvious, and put an instant quote or booking a couple of taps away. Detailing is planned, not urgent, so people are more willing to book online here than in almost any trade, and the detailer whose site lets them pick a slot at ten at night wins the job over the one who makes them wait for a callback.</p>'},
        {"h2_html": "The bookings are <em>yours</em>, permanently",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Money spent on a pay-per-lead service is gone the moment you stop feeding it, and the booking it rented you was never truly yours. A website you own keeps ranking, keeps showing your work, and keeps taking bookings for as long as it exists, and it is registered to you, not a platform that can drop you. The site plugs into the same CRM that follows up on every request it captures and the AI receptionist that answers the calls it drives, so nothing it earns you slips away.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A ceramic coating search finds <em>you</em>, not a directory",
        "body_html": "A car owner in the next town over decides their new car deserves a ceramic coating and searches ceramic coating near me on their phone. Instead of a national directory that would sell the request to three detailers, they find your site ranking for that town, with a gallery of coated cars beading water right at the top, your service area clear, and a booking form a couple of taps down the page. They book a consultation with you directly, with no per-lead fee and no middleman anywhere in the chain. You wake up to the job on your calendar. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the detailing and coating searches a national directory has no reason to target well, which is exactly where a local detailer can win."),
        ("How is this different from paying for leads?",
         "A pay-per-lead service rents you a request that it also sells to other detailers, and it stops the day you stop paying. A website you own captures bookings that are yours alone and keeps working long after it is built, without a per-lead fee coming out of every job."),
        ("Do people really book a detail online?",
         "More than in most trades, because a detail is planned rather than urgent. When someone can see your work and pick a slot at ten at night without a phone call, plenty will, and the ones who would rather talk still get a way to reach you in one tap."),
        ("I am a mobile detailer. Does a website still help?",
         "Even more. Without a storefront, your site and your Google presence are how customers find you at all, and a fast site that shows your work, makes your service area obvious, and lets someone book you to their driveway is what turns a search into a job on your route."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks; broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for auto detailers"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-auto-detailers.html", "Staying visible in your service area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and lead-sellers taking your bookings, whether you work with us or not. No credit card, never a call center.",
},
]
