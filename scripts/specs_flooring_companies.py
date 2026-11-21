"""Per-page content specs for the SEO corpus (plan §5), flooring companies batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell, schema,
events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns the UNIQUE,
hand-written, flooring-specific substance that clears the uniqueness gate. Never templated
find-and-replace, never the plumber, general-contractor, foundation, or fence content reworded.

Flooring is a mid-ticket, visual, considered purchase. A homeowner choosing hardwood, luxury vinyl
plank, tile, or carpet wants to see samples and finished rooms and then get an in-home measure and
quote, so the business blends a showroom with in-home estimates. Buyers shop a few flooring
companies and go with the one that responds and books the measure, while the installer or estimator
is on a job laying floor and misses the call. So the substance leans on capturing every sample and
measure request, following up the still-choosing quotes over the weeks a homeowner compares samples
and companies, and reactivating past customers for the next room plus the referrals a visible new
floor earns. Product-and-project photo galleries, reviews, and a fast site that showcases the
materials and books an in-home consult are what win. Distinct from general contractors (whole
remodels) and from foundation and fence.

Home Services hub. Four service angles here in one file (the ai-receptionist dict carries
"demo": True). Each example body ends with the literal "Illustrative example, not a client." per
the honesty rule; if the generator also appends that line, dedupe there.
"""

SPECS = [
# ==================== AI Receptionist for Flooring Companies ====================
{
    "slug": "ai-receptionist-for-flooring-companies", "demo": True,
    "trade_slug": "flooring_companies", "trade_plural": "flooring companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "AI Receptionist for Flooring Companies",
    "title": "AI Receptionist for Flooring Companies | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Flooring Companies",
    "meta_desc": "A flooring company answering service answers every call while you are laying floor, captures the rooms and material, and books the measure for you.",
    "service_schema_name": "AI Receptionist for Flooring Companies",
    "eyebrow": "For Flooring Companies",
    "h1_html": "AI Receptionist <em>for Flooring Companies</em>",
    "answer_block": "A flooring company answering service answers every call the moment it rings, even when your crew is on its knees laying floor and cannot reach the phone, finds out which rooms and what material a homeowner is weighing, and books the in-home measure or showroom visit, so the job belongs to you instead of the flooring company that answered first.",
    "sections": [
        {"h2_html": "The call you miss is the floor <em>someone else measures</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner planning new floors is not calling one company. They line up a few, browse photos online, maybe stop by a showroom, and lean toward the one that answers, sounds like a real flooring company, and can get out to measure soon. Flooring turns on that responsiveness, because the homeowner is choosing both a product they will look at every day and the crew that will tear out the old floor and work in their house for a few days, so they are quietly sizing you up from the first call. But your estimator is on his knees with a trowel, your installer is mid-room with a nailer, and nobody is near the phone, so the call rings out and the job, which could be a whole main level, goes to whoever picked up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A flooring company answering service picks up on the first ring, sounds calm and professional, asks which rooms they want done and what they are leaning toward, hardwood, luxury vinyl plank, tile, or carpet, gets the address, and either books the in-home measure or invites them in to see samples. The measure is sitting on your calendar instead of lost to the flooring company down the road that happened to be near a phone.</p>'},
        {"h2_html": "Built around how <em>flooring calls actually come in</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your calls do not come in while you are sitting at a desk. They come in while you are laying floor, loading the trailer, or walking a job with a customer, and a lot of them come in the evenings and weekends when homeowners finally sit down to research floors after staring at a room they cannot stand anymore. A voicemail box cannot hold a serious buyer who is working down a list, and a generic call center reading a script does not know engineered hardwood from a floating vinyl install, or which caller wants a whole-house quote and which just wants a price on a set of stairs.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers every call and web inquiry, including the nights and weekends when homeowners actually shop for floors.</li><li>Asks what you would ask: which rooms, roughly how much square footage, what material they are considering, and whether they want to see samples or book a measure.</li><li>Books the in-home measure straight onto your calendar or sets up a showroom visit, and texts you the details so you show up already knowing the job.</li><li>Treats a referral or a repeat customer coming back for the next room differently from a cold web lead, so the warmest buyers never land in a voicemail box.</li></ul>'},
        {"h2_html": "The math is <em>one whole-house floor</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not need to catch many calls for this to pay for itself. A flooring job is rarely a small ticket, a single room is real money and a whole main level or a whole house is a large one, so one measure you would have lost while your hands were full on a job is often worth more than the service costs for a long stretch. Missing that call is not a quick service visit you shrug off, it is a full room or a whole floor handed to whoever answered faster. Everything it captures after that first save is on top. You are not paying for a receptionist to sit and wait for the phone to ring. You are making sure the one homeowner who was finally ready to replace their floors reached a real, organized company that answered, took down the rooms and the material, and put a measure on the calendar, instead of a voicemail box they never called back. For a buyer choosing between a few flooring companies, that first real answer is often what decides who gets to come out and quote, and it protects the reputation you have built, because a homeowner who cannot reach you does not assume you are busy with good work, they assume you are hard to pin down.</p>'},
        {"h2_html": "You own the number, the calls, and the <em>customer list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing business number, or a new one registered in your name, not ours. Every caller, every address, and every note about the rooms and material they want is yours and exportable any time, so the customer list you are building stays an asset you own instead of something you rent back month to month. There is no long contract holding your data hostage. The answering service is one piece of the Top Shelf platform, and it hands every lead it captures to the same CRM that keeps following up over the weeks a homeowner takes to settle on a material and a company, so a measure request or a quote never quietly slips through the gap. A homeowner who would rather book the measure themselves can, while the ones who want to talk through their options reach a real, professional answer instead of a recording.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "An after-hours flooring call, <em>booked before morning</em>",
        "body_html": 'It is 8pm and a homeowner who has finally had enough of the worn carpet in their living room and hallway sits down and calls the three flooring companies they found online. The first two ring out to voicemail. Yours answers, sounds calm and professional, asks which rooms they want done and whether they are leaning toward hardwood, luxury vinyl plank, or carpet, gets the address, and books an in-home measure for Thursday while a note pings your phone. You wake up to a booked measure with the rooms, the rough square footage, and the homeowner\'s number already attached, instead of hearing later that they went with the company that picked up. Illustrative example, not a client.'},
    "faqs": [
        ("Does it work with my current phone number?",
         "Yes. It can answer on your existing business number, or set up a new one registered in your name. Either way the number and every lead that comes through it belong to you and go with you if you ever leave."),
        ("Can it handle a real flooring inquiry, or just take a message?",
         "It does not guess at a price. It gathers what a real measure needs, which rooms, roughly how much square footage, what material they are considering, and whether they want samples or an in-home visit, then books the measure on your calendar or hands you a qualified lead. You still walk the job and set the quote, but the lead is captured instead of lost."),
        ("What happens to calls when my crew is on a job?",
         "That is exactly when it earns its keep. It answers every call and web inquiry the moment it comes in, no matter how buried your crew is in a room, so the hours you cannot reach the phone stop being the hours you lose the most work."),
        ("Is it going to sound like a robot to a homeowner?",
         "It answers naturally and is upfront instead of pretending to be a person. Someone about to pick out floors and let a crew into their home mostly wants to know a real, organized company is handling it, and a steady voice that takes down the rooms and the material beats a voicemail box every time. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your questions, your calendar, and your lead rules for you, so it is answering in days, not weeks. Start with a free audit and we will show you what your current setup is missing.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for flooring companies"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-flooring-companies.html", "The CRM that follows up on every lead you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing floors to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many measure requests and showroom calls your current setup is letting slip through the gap, whether you work with us or not. No credit card, never a call center.",
},
# ========================= CRM for Flooring Companies =========================
{
    "slug": "crm-for-flooring-companies",
    "trade_slug": "flooring_companies", "trade_plural": "flooring companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "CRM for Flooring Companies",
    "title": "CRM for Flooring Companies | Top Shelf Business Solutions",
    "og_title": "CRM for Flooring Companies",
    "meta_desc": "A CRM for flooring companies follows up on every measure and quote while a homeowner is still choosing, and brings past customers back for the next room.",
    "service_schema_name": "CRM for Flooring Companies",
    "eyebrow": "For Flooring Companies",
    "h1_html": "CRM <em>for Flooring Companies</em>",
    "answer_block": "A CRM for flooring companies keeps every lead, measure, and open quote in one place and follows up for you over the weeks a homeowner takes to settle on a material, so the family still comparing samples and the customer whose living room you did last year both come back to you instead of the company that stayed in touch.",
    "sections": [
        {"h2_html": "The quotes you already measured are the floors you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most flooring companies do not have a lead problem. They have a follow-up problem. You send someone out to measure, put together a quote for hardwood or luxury vinyl across a few rooms, and then the homeowner goes quiet. They are gathering another price or two, taking sample boards home to see them in their own light, and talking it over with a spouse about style and budget, and a decision about floors they will walk on every day rarely lands in an afternoon. Meanwhile you get pulled back onto the jobs you already have, and you never circle back. Weeks later they book with another company, and it is usually not the cheapest one. It is the one that kept in touch and made choosing feel easy.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every open quote in front of you and follows up on a schedule you set, with texts and emails that go out on time whether or not the week got away from you. The homeowner comparing samples and companies keeps hearing from you while the others go silent, and being the one who stayed helpful through the deciding is exactly what wins the job. None of it takes your crew off the floor, because the follow-up runs in the background while you install, and you step in only when a homeowner actually replies.</p>'},
        {"h2_html": "Choosing a floor happens at the kitchen table, <em>not at the measure</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The measure is the start of the sale, not the end of it. Between the quote and the deposit sits a stretch of comparing samples, pricing a couple of companies, and going back and forth on whether to spend up for hardwood or go with luxury vinyl, and it can run weeks. This is where most companies quietly lose jobs they had all but won in the living room, not to a better price but to silence. The homeowner did not say no, they said they needed to think, and then nobody gave them a reason to move, so the job drifted to whichever company happened to check in at the right moment.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every lead, measure, sample request, quote, and note lives in one place instead of a truck console full of scribbled measurements and whatever you can remember.</li><li>Follow-up goes out on the cadence you set across the whole deciding window, a check-in after the measure, an answer to the material-versus-material question, a nudge when a sample has been out for a week.</li><li>You can see exactly which quotes are still open and which homeowners have gone quiet, and reach the right one before a competitor books the measure you already ran.</li></ul>'},
        {"h2_html": "The next room, and the neighbor who <em>saw the floor</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A customer whose living room you floored last year has not gone anywhere, and they are the cheapest work a flooring company can get. You have already been in the house, they have seen how your crew works and how the floor held up, and the next room, the bedrooms, the stairs, the basement they always meant to finish, is yours if you stay in touch. New floors are also the most visible upgrade a house can get, so a happy customer\'s guests and neighbors notice and ask who did it, which makes a past customer a repeat buyer and a referral source at the same time. But you cannot personally remember to reach back out to everyone you have ever installed for, so most of that repeat work and word of mouth drifts to whoever turns up when they finally search, long after they lost your card. A CRM keeps that whole list on a light, genuine touch, a thank-you and a request for the review and the referral while the floor is still new, a seasonal note, a check that everything is holding, so the next room and the neighbor both come back to you instead of a stranger they found online.</p>'},
        {"h2_html": "You own the list, and it <em>works with the rest of the system</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every customer, quote, and note is yours and exportable any time, not locked inside software you rent. The CRM is one piece of the Top Shelf platform and connects to the answering service, so a call it captures lands in your database and gets followed up on automatically, and to your booking, so a scheduled measure is logged against the right customer with their full history already attached. The result is one place where every room you have quoted, floored, or been referred is tracked, and nothing you have earned goes cold in the gap between the measure and the deposit. You still message anyone directly whenever a job needs a real conversation, the system just makes sure the quiet ones never get forgotten. Over a few years that database, a record of every home you have floored and every room still waiting, becomes one of the most valuable things the business owns, and it stays yours no matter what.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The quote that <em>closes itself</em> weeks later",
        "body_html": 'You measure a home in March for hardwood in the living room and hallway, and the homeowner tells you they want to take the samples home and get one more price. Normally that is the last you hear of it. Instead the CRM sends a friendly check-in the next week, a short note comparing the two materials they were weighing a few days after that, and a nudge when the date they wanted it done by gets close, all written to sound like you. The other two companies never followed up, so when the homeowner is finally ready in April, yours is the only name still in front of them. They book with you without shopping it again. Illustrative example, not a client.'},
    "faqs": [
        ("Does it import my existing customers and past jobs?",
         "Yes. Your current customers, leads, and job history come in and live in one place, and everything stays yours and exportable. The point is to make the homes you have already floored actually book you the next room."),
        ("Will it really follow up on open quotes automatically?",
         "Yes, on the schedule you approve. A quote gets a check-in days later and more touches over the following weeks, all sent for you, so a homeowner comparing samples and companies keeps hearing from you while the others go quiet. You can jump in and message anyone directly any time."),
        ("Can it bring past customers back for the next room?",
         "Yes. It keeps a light, genuine touch going with customers you have already floored, so when they are ready to do the bedrooms, the stairs, or the basement, your name is already in front of them, and it asks for the review and the referral while the floor is still new."),
        ("How is this different from just keeping notes in my phone?",
         "A phone full of contacts does not follow up, does not remind you which quote is going cold, and does not tell you who has gone quiet. The CRM does all of that on a schedule, so the quotes you already measured and the rooms you have not done yet actually turn into jobs."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your customers, build your follow-up and reactivation sequences, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will find the gap where jobs are going cold today.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for flooring companies"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-flooring-companies.html", "The answering service that feeds it every lead"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting quotes and customers <em>go cold</em>",
    "cta_sub": "Get a free audit of how many of your measures and past customers are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ======================= Marketing for Flooring Companies =======================
# ==================== Websites & SEO for Flooring Companies ====================
{
    "slug": "websites-seo-for-flooring-companies",
    "trade_slug": "flooring_companies", "trade_plural": "flooring companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "Websites & SEO for Flooring Companies",
    "title": "Websites & SEO for Flooring Companies | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Flooring Companies",
    "meta_desc": "A flooring company website built for SEO ranks for flooring near me and your city, shows the galleries that sell floors, and books the in-home measure.",
    "service_schema_name": "Websites & SEO for Flooring Companies",
    "eyebrow": "For Flooring Companies",
    "h1_html": "Websites &amp; SEO <em>for Flooring Companies</em>",
    "answer_block": "A flooring company website built for SEO ranks for the searches a homeowner makes when picking new floors, flooring near me, hardwood floor installation, luxury vinyl plank, carpet and tile in your city, and shows the galleries, materials, and reviews that turn a browse into a booked measure, so the lead comes straight to you instead of a directory.",
    "sections": [
        {"h2_html": "The lead-sellers are not competing with you, they are <em>renting you back your own leads</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for a flooring company in your town and the top of the page is often a directory or a pay-per-lead marketplace, not a local installer. Those sites publish thousands of pages and carry years of authority, so a homeowner lands there first, fills out a form, and that inquiry gets sold, sometimes to several companies at once, sometimes back to you for a fee out of your own margin. You do the work of running a real showroom and a real crew, and a middleman collects the rent on your own market. For a flooring company the sting is real, because the lead being auctioned is not a small service trickle, it is a room or a whole floor. Your site not ranking is not a vanity problem. It is the reason a homeowner you should have reached for free gets sold to you, or handed to three competitors right alongside you, while the local company they were hoping to find sits invisible a click away.</p>'},
        {"h2_html": "Rank for the floors and towns homeowners <em>actually search</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national directory this year for the broadest term, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you serve, and for the exact things people search when new floors are on their mind, flooring near me, hardwood floor installation, luxury vinyl plank, carpet installer, tile flooring, and floor replacement in your city. Pages built around the materials you actually carry and the areas you actually serve are what search engines, and homeowners deep in choosing a floor, reward with the click.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This kind of search is slower and more considered than an emergency, and that works in your favor. A homeowner planning new floors over days reads more, clicks deeper, and remembers the company whose pages showed the material they were picturing and named the town they live in. It is also where the higher-value jobs live, the whole main level, the whole house, the stairs and the great room, and a page built around a specific material in a specific town is one a national directory never bothers to write well, so every one of them is a page you can own outright. A single page that ranks for the right floor in the right town can pay for the site with one job and keep paying for years.</p>'},
        {"h2_html": "A homeowner picking floors wants to <em>see them first</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Flooring is a visual, high-consideration purchase. Before a homeowner invites anyone out to measure, they are on your site deciding whether you look like a real, established company with work worth seeing, or just a truck and a phone number. That is why galleries matter more for a flooring company than for almost any trade. Real photos of finished floors, organized by material and room, a clear sense of what you carry, honest reviews, and your service area stated plainly are what turn a browsing visitor into a booked measure.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A lot of that browsing happens late at night, when a homeowner finally sits down after the kids are asleep to picture their rooms with new floors, which is exactly when a site that loads fast, looks right on a phone, shows the work, and makes requesting an in-home measure effortless captures the job, instead of a voicemail box nobody is checking or a form buried three clicks deep. The site does not need to be flashy, it needs to show the floors clearly, load fast, prove you are real, and put the gallery and the measure request where a homeowner can find them at a glance.</p>'},
        {"h2_html": "The leads are <em>yours</em>, permanently",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you pour into a pay-per-lead service disappears the day you stop paying, and the lead was never really yours anyway, it was sold to your competitors in the same breath. A website you own keeps ranking, keeps capturing inquiries, and keeps compounding in value for as long as it exists, and it is registered to you, not a platform that can drop you tomorrow. The site plugs into the same CRM that follows up on every inquiry over the weeks a homeowner takes to choose, and the answering service that picks up the calls it drives, so a lead never lands in one place while the follow-up lives in another. The result is one site that ranks, shows the work, and hands every homeowner straight into the system that closes them, instead of a pretty page that looks nice and loses the lead in the gap between the first click and the booked measure. You are building an asset, not renting attention, and every month it keeps ranking is a month of jobs a lead service would have charged you for one at a time.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A flooring search that finds <em>you, not a directory</em>",
        "body_html": 'A homeowner a couple of towns over decides it is finally time to replace the carpet in the whole house with luxury vinyl and searches for flooring installation in their town. Instead of a national directory that would sell their details to three companies at once, they find your site ranking for that town, with a page about luxury vinyl and a gallery of finished floors you actually installed. They browse a few rooms like theirs, read a couple of reviews, see that you are local, and request an in-home measure right there. The inquiry comes straight to you, you paid nothing per lead, and no middleman ever touched it. Illustrative example, not a client.'},
    "faqs": [
        ("Will my site actually outrank the big directories?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the material and installation searches a national directory has no reason to target well, which is exactly where a local flooring company can win."),
        ("How is this different from paying for leads?",
         "A pay-per-lead service rents you an inquiry it also sells to your competitors, and it stops the day you stop paying. A website you own captures inquiries that are yours alone and keeps working long after it is built, without a fee coming out of every job."),
        ("Do I really need a gallery on the site?",
         "For a flooring company, yes. Homeowners buy floors with their eyes, so photos of your finished work, organized by material and room and paired with reviews, are often what turn a browsing visitor into a booked measure. The gallery is doing the same job your showroom does."),
        ("Do I need to rank for every town I serve?",
         "You rank for the ones that matter most first. We build pages for your core service areas and the highest-value material and installation searches, then expand, rather than spreading thin across a whole metro at once."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks, and broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for flooring companies"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and lead-sellers taking your inquiries, whether you work with us or not. No credit card, never a call center.",
},
]
