"""Per-page content specs for the SEO corpus (plan §5), foundation repair batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell, schema,
events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns the UNIQUE,
hand-written, foundation-repair-specific substance that clears the uniqueness gate. Never templated
find-and-replace, never the plumber, general-contractor, solar, or roofer content reworded.

Foundation repair is a high-ticket, engineered sale that starts with a frightened homeowner: cracks
in the wall, sticking doors, a sloping floor, and a caller who is scared it is catastrophic and
expensive. The inbound call is anxious and high-intent, the sale runs from free inspection to
engineered estimate to decision over weeks, financing and a transferable warranty are part of it,
and the homeowner picks the company that answered fast and felt trustworthy and non-alarmist. So the
substance leans on calming an anxious first-time caller, relentless follow-up on outstanding
estimates over the weeks a homeowner compares opinions and lines up financing, trust and education
that tells a real structural problem from ordinary cosmetic settling, and a credible, proof-heavy
presence that converts a frightened researcher. Never scare tactics, never a promised repair price.

Home Services hub. Four service angles here in one file (the ai-receptionist dict carries
"demo": True). Each example body ends with the literal "Illustrative example, not a client." per
the honesty rule; if the generator also appends that line, dedupe there.
"""

SPECS = [
# ==================== AI Receptionist for Foundation Repair ====================
{
    "slug": "ai-receptionist-for-foundation-repair", "demo": True,
    "trade_slug": "foundation_repair", "trade_plural": "foundation repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "AI Receptionist for Foundation Repair",
    "title": "AI Receptionist for Foundation Repair | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Foundation Repair",
    "meta_desc": "A foundation repair answering service answers every anxious call, calms the homeowner, gathers the warning signs, and books the free inspection for you.",
    "service_schema_name": "AI Receptionist for Foundation Repair",
    "eyebrow": "For Foundation Repair",
    "h1_html": "AI Receptionist <em>for Foundation Repair</em>",
    "answer_block": "A foundation repair answering service answers every call the moment it rings, day or night, calms a homeowner who just spotted cracks or a sticking door, gathers the signs and the address without alarming them, and books the free inspection straight onto your calendar, so the job belongs to you instead of the company that answered first.",
    "sections": [
        {"h2_html": "The frightened call you miss is the inspection your <em>competitor books</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner who just noticed a stair-step crack climbing the brick, a door that suddenly will not latch, or a floor that has started to slope is scared, and a scared homeowner does not call one company. They call three or four in a row, half-convinced the house is coming apart and the fix will cost a fortune, and they lean hard toward the first company that picks up, sounds calm, and offers to come look. Foundation work turns on that first contact more than almost any trade, because the caller is frightened and looking for someone to trust before they are looking for a price. But you are on a job site watching a crew set piers, down in a crawl space, or driving between inspections, so the call rings out, and the homeowner, along with a job worth far more than a quick service call, goes to whoever happened to answer.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A foundation repair answering service picks up on the first ring, stays calm and reassuring instead of alarmist, asks what they are seeing and where, gets the address, and books the free inspection or hands you a qualified lead with the details already captured. The frightened homeowner reaches a real, steady answer at the moment they most need one, and the inspection is sitting on your calendar instead of lost to the company down the road.</p>'},
        {"h2_html": "Built around how <em>foundation repair calls actually come in</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your calls do not come in while you are at a desk. They come in after a homeowner finally notices the crack they have been walking past for months, often in the evening or on a weekend once they sit down and start searching photos that scare them worse. A voicemail box cannot reassure a frightened person, and a generic call center reading a script cannot tell a genuine structural concern from ordinary cosmetic settling, gather the right signs, or sound like it belongs to a company that actually goes under houses.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers day and night, including the evening and weekend calls that come right after a homeowner finds something and panics.</li><li>Asks what you would ask: what they are seeing and where, cracks in brick or drywall, doors or windows sticking, floors that slope, gaps opening at the trim, and how long it has been happening.</li><li>Stays calm and never alarmist, so a worried homeowner feels steadied rather than sold, which is exactly what earns a nervous first-time caller.</li><li>Gets the address, books the free inspection on your calendar, and texts you the details, so an estimator walks in already knowing what the homeowner is worried about.</li><li>Treats a referral or a past customer differently from a cold caller, so the people most likely to sign never hit a voicemail.</li></ul>'},
        {"h2_html": "The math is <em>one signed foundation job</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not need to catch many calls for this to pay for itself. A foundation repair company lives on a small number of large, engineered jobs, so one repair you would have lost while your hands were full under a house is often worth more than the service costs for a long stretch. Missing that call is not a small ticket you shrug off. It is a whole pier job or slab repair, the kind that can carry a slow month, handed to whoever answered faster. Everything it captures after that first save is on top. You are not paying for someone to sit and wait for the phone to ring. You are making sure the frightened homeowner who finally worked up the nerve to call reached a calm, organized company that answered, steadied them, and put a free inspection on the calendar, instead of a voicemail box they never called back. For an anxious first-time caller weighing a repair this size, that first real, reassuring answer is often what decides which company they trust, and it protects the reputation you have built, because a homeowner who cannot reach you does not assume you are busy, they assume you are hard to pin down.</p>'},
        {"h2_html": "You own the number, the calls, and the <em>customer list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing business number, or a new one registered in your name, not ours. Every caller, every address, and every note about what they are seeing is yours and exportable any time, so the customer list you are building stays an asset you own instead of something you rent back month to month. There is no long contract holding your data hostage. The answering service is one piece of the Top Shelf platform, and it hands every lead it captures to the same CRM that keeps following up over the weeks a homeowner takes to decide on a repair this size, so an inspection request never quietly slips through the gap. A homeowner who would rather book the inspection themselves can, while the ones who need to talk to a calm voice reach a real answer instead of a recording.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "An evening crack-in-the-wall call, <em>booked before morning</em>",
        "body_html": 'It is 7pm and a homeowner who has spent the evening staring at a stair-step crack in the brick and a front door that no longer latches finally calls the three foundation companies they found online. The first two ring out to voicemail. Yours answers, sounds calm and unhurried, asks what they are seeing and how long it has been happening, gets the address, and books a free inspection for Thursday while a note pings your phone. You wake up to a booked inspection with the signs, the address, and the homeowner\'s number already attached, instead of hearing weeks later that they hired the company that picked up. Illustrative example, not a client.'},
    "faqs": [
        ("Does it work with my current phone number?",
         "Yes. It can answer on your existing business number, or set up a new one registered in your name. Either way the number and every lead that comes through it belong to you and go with you if you ever leave."),
        ("Can it calm a worried homeowner and gather the right details?",
         "Yes, that is the point. It stays calm and reassuring instead of alarmist, asks what they are seeing and where, cracks, sticking doors, sloping floors, how long it has gone on, and captures it all for your estimator. It does not diagnose or quote over the phone, it steadies the caller and books the free inspection."),
        ("What happens to calls when I am on a job site or under a house?",
         "That is exactly when it earns its keep. It answers every call the moment it comes in, no matter how buried your crew is, so the hours you cannot reach the phone stop being the hours you lose the most work."),
        ("Is it going to sound like a robot to a frightened homeowner?",
         "It answers naturally and calmly, and it is upfront instead of pretending to be a person. Someone worried their house is failing mostly needs to know a real, steady company is going to come look, and a calm voice that takes down the details beats a voicemail box every time. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your questions, your calendar, and your lead rules for you, so it is answering in days, not weeks.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for foundation repair companies"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-foundation-repair.html", "The CRM that follows up on every lead you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing foundation jobs to <em>voicemail</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
},
# ========================= CRM for Foundation Repair =========================
{
    "slug": "crm-for-foundation-repair",
    "trade_slug": "foundation_repair", "trade_plural": "foundation repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "CRM for Foundation Repair",
    "title": "CRM for Foundation Repair | Top Shelf Business Solutions",
    "og_title": "CRM for Foundation Repair",
    "meta_desc": "A CRM for foundation repair follows up on every inspection and estimate over the weeks a homeowner takes to decide, so the big repair comes back to you.",
    "service_schema_name": "CRM for Foundation Repair",
    "eyebrow": "For Foundation Repair",
    "h1_html": "CRM <em>for Foundation Repair</em>",
    "answer_block": "A CRM for foundation repair keeps every lead, inspection, and engineered estimate in one place and follows up for you over the weeks a homeowner spends getting opinions and lining up financing, so the family still weighing a big repair comes back to you instead of the company that stayed in touch and felt trustworthy.",
    "sections": [
        {"h2_html": "The estimates you already delivered are the jobs you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most foundation repair companies do not have a lead problem. They have a follow-up problem. You send an estimator out, deliver an engineered estimate on a pier job or a slab repair, and then the homeowner goes quiet. They are getting a second and third opinion, talking it over with a spouse, waiting on financing, and quietly wrestling with whether a repair this expensive is really necessary yet. A decision this big almost never lands in a day, and while it sits, you get pulled onto the jobs you already have and never circle back. Weeks later they sign with another company, and it is usually not the cheapest one. It is the one that kept in touch and felt the most steady and trustworthy the whole way through.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every open estimate in front of you and follows up on a schedule you set, with texts and emails that go out on time whether or not the week got away from you. The homeowner comparing three companies keeps hearing from you while the others go silent, and being the calm, organized one that never drops the thread is exactly the signal that wins a nervous buyer on a repair this size. None of it takes your crew off the job, because the follow-up runs in the background while you work, and you step in only when a homeowner actually replies.</p>'},
        {"h2_html": "A foundation decision is made over weeks, <em>not at the inspection</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The inspection is the start of the sale, not the end of it. Between the estimate and the signature sits a stretch of comparing, financing, and second-guessing whether the problem is urgent enough to act on now, and it can run weeks or months. This is where most companies quietly lose jobs they had all but won at the kitchen table, not to a better price but to silence. The homeowner did not say no. They said they needed to think, and then nobody gave them a reason to move, so the job drifted to whichever company happened to check in at the right moment.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every lead, inspection, engineered estimate, and note lives in one place instead of a truck console and whatever anyone can still remember a month later.</li><li>Follow-up goes out on the cadence you set across the whole decision window, a check-in after the inspection, a calm answer to the is-it-urgent question, a nudge when financing is the thing holding them up.</li><li>You can see exactly which estimates are still open and which homeowners have gone quiet, and reach the right one with the right message before a competitor closes them first.</li></ul>'},
        {"h2_html": "The homeowner who decided to <em>watch it</em> is still yours",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner who got an inspection a year ago and decided to keep an eye on the crack has not gone anywhere. People sit on foundation work all the time, the money was not there yet, the crack had not moved enough to truly frighten them, or a spouse was not convinced it could not wait. Then something shifts. A dry summer opens the crack wider, a door stops latching, the slope in the floor gets hard to ignore, or they decide to sell and a buyer wants the repair done and warrantied before closing. The company that kept a light, honest touch the whole time is the one they call, and the company that wrote them off after a single soft no never crosses their mind. Most companies leave those old inspections to rot in a spreadsheet, which means paying for a brand new lead while a warmer one waits a few rows down. A CRM keeps that entire list of not-yet buyers on a gentle, genuine touch, a seasonal note, an honest check that nothing has worsened, so the moment their situation tips, yours is the name already in front of them. Reviving inspections you already ran, worked patiently instead of abandoned, is often the cheapest pipeline a foundation company has.</p>'},
        {"h2_html": "You own the list, and it <em>works with the rest of the system</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every lead, estimate, and note is yours and exportable any time, not locked inside software you rent. The CRM is one piece of the Top Shelf platform and connects to the answering service, so a call it captures lands in your database and gets followed up on automatically, and to your booking, so a scheduled inspection is logged against the right homeowner with their full history already attached. The result is one place where every inspection you have run, every estimate you have delivered, and every job you have warrantied sits together, and nothing you spent money to earn goes cold in the long gap between the first call and the signed contract. You still message anyone directly whenever a job needs a real conversation, the system just makes sure the quiet ones are never forgotten. Over a few years that database, a record of every homeowner who ever worried about their foundation and every repair still waiting to happen, becomes one of the most valuable things the business owns, and it stays yours no matter what.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The estimate that <em>closes itself</em> weeks later",
        "body_html": 'You inspect a home in March, deliver an engineered estimate for a row of piers, and the homeowner tells you they want another opinion and need to look at financing. Normally that is the last you hear of it. Instead the CRM sends a calm check-in the next week, a short note answering the question everyone asks about whether it can wait, and a nudge when financing options come up, all written to sound like you. The other two companies never followed up, so when the homeowner is finally ready in May, yours is the only name still in front of them and the only one that felt steady the whole time. They sign with you without shopping it again. Illustrative example, not a client.'},
    "faqs": [
        ("Does it import my existing leads and past inspections?",
         "Yes. Your current leads, open estimates, and past inspections come in and live in one place, and everything stays yours and exportable. The point is to make the pipeline you have already built actually turn into signed jobs."),
        ("Will it really follow up on outstanding estimates automatically?",
         "Yes, on the schedule you approve. An open estimate gets a check-in days later and more touches over the following weeks, all sent for you, so a homeowner weighing three companies keeps hearing from you while the others go quiet. You can jump in and message anyone directly any time."),
        ("Can it bring back homeowners who decided to wait?",
         "Yes. It keeps a gentle, honest touch going with homeowners who got an inspection but were not ready, so when the crack widens, the door stops closing, or they go to sell, your name is already in front of them instead of a brand new lead you have to pay for all over again."),
        ("How is this different from just keeping notes in a spreadsheet?",
         "A spreadsheet does not follow up, does not remind you which estimate is going cold, and does not tell you who has gone quiet. The CRM does all of that on a schedule, so the estimates you already delivered and the inspections you already ran actually turn into jobs."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your leads, build your follow-up and revival sequences, and connect it to your calls and calendar, so it is working in days.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for foundation repair companies"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-foundation-repair.html", "The answering service that feeds it every lead"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting estimates and homeowners <em>go cold</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
},
# ======================= Marketing for Foundation Repair =======================
# ==================== Websites for Foundation Repair ====================
{
    "slug": "websites-seo-for-foundation-repair",
    "trade_slug": "foundation_repair", "trade_plural": "foundation repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "Websites for Foundation Repair",
    "title": "Websites for Foundation Repair | Top Shelf Business Solutions",
    "og_title": "Websites for Foundation Repair",
    "meta_desc": "A foundation repair website built for SEO ranks for foundation repair near me and your city, and reassures a frightened homeowner enough to book the inspection.",
    "service_schema_name": "Websites for Foundation Repair",
    "eyebrow": "For Foundation Repair",
    "h1_html": "Websites <em>for Foundation Repair</em>",
    "answer_block": "A foundation repair website built for SEO ranks for the searches a worried homeowner makes, foundation repair near me, foundation inspection, cracks in the brick, in your city, and earns the trust that turns a big, frightening repair into a booked inspection, so the lead comes straight to you instead of a lead-seller.",
    "sections": [
        {"h2_html": "The lead-sellers are not competing with you, they are <em>renting you back your own calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for a foundation company in your town and the top of the page is often a directory or a pay-per-lead marketplace, not a local company. Those sites publish thousands of pages and carry years of authority, so a frightened homeowner lands there first, fills out a form, and that inquiry gets sold, sometimes to several companies at once, sometimes back to you for a fee out of your own margin. You do the work of being a real, credentialed local company, and a middleman collects the rent on your own market. For foundation repair that sting is bigger than for most trades, because the lead being auctioned is not a small service call, it is a whole engineered repair. Your site not ranking is not a vanity problem. It is the reason a homeowner you should have reached for free gets sold to you, or handed to three competitors right alongside you, while the honest local company they were hoping to find sits invisible a click away. Ranking your own site is how you step out from behind that middleman and meet the homeowner directly, on the search they were already making, with no toll booth in between.</p>'},
        {"h2_html": "Rank for what a <em>frightened homeowner types</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national directory this year for the broadest term, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you serve, and for the exact things people search the moment they get scared, foundation repair near me, foundation inspection, cracks in a brick wall, sloping floors, a bowing basement wall, foundation repair in your city. Pages built around the work you actually do and the ground you actually serve are what search engines, and a homeowner deep in a worried search, reward with the click.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This kind of search is slow and considered, and that works in your favor. A homeowner researching a foundation problem over days reads more, clicks deeper, and remembers the company whose pages answered their questions straight instead of trapping them behind a form. It is also where the specific, high-intent searches live, a particular sign, a particular method, whether a certain crack is serious, questions a national marketplace never bothers to answer well, and every one of them is a page you can own outright while the directories chase the generic term. A single page that calmly answers the right question for the right town can bring in a homeowner who reads it, trusts it, and books an inspection, and then keep doing that for years.</p>'},
        {"h2_html": "A homeowner spending this much reads your site <em>before they ever call</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Foundation repair is not a low-trust purchase. The homeowner is frightened, about to spend a large sum, and likely to sign a financing agreement, so before they ever reach out they are on your site deciding whether you look like a real, established, credentialed company or an outfit that will scare them and vanish. That is why the site itself matters as much as the ranking. Before-and-after photos of real jobs, a clear explanation of your process from free inspection to engineered estimate, your credentials and the transferable warranty stated plainly, and honest answers to the fear a homeowner actually carries, is this catastrophic, can it wait, will you oversell me, are what turn a scared visitor into a booked inspection.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A lot of that deciding happens late at night, when a homeowner finally sits down after the kids are asleep to figure out how worried they should be, which is exactly when a site that loads fast, looks right on a phone, answers the real questions, and makes booking a free inspection effortless captures the lead, instead of a voicemail box nobody is checking or a form buried three clicks deep. The site does not need to be flashy. It needs to be calm, honest, fast, and built to reassure someone who is a little scared, with the proof and the inspection booking sitting right where a worried researcher can find them at a glance.</p>'},
        {"h2_html": "The leads are <em>yours</em>, permanently",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you pour into a pay-per-lead service disappears the day you stop paying, and the lead was never really yours anyway, it was sold to your competitors in the same breath and priced to take a bite out of the job. A website you own keeps ranking, keeps capturing inquiries, and keeps compounding in value for as long as it exists, and it is registered to you, not a platform that can drop you tomorrow or raise your per-lead price whenever it likes. The site plugs into the same CRM that follows up on every inquiry over the weeks a homeowner takes to decide, and the answering service that picks up the calls it drives, so a lead never lands in one place while the follow-up lives in another. The result is one site that ranks, earns trust, and hands every homeowner straight into the system that closes them, instead of a pretty page that looks nice and loses the lead in the gap between the first click and the signed contract. You are building an asset, not renting attention, and every month it keeps ranking is a month of homeowners a lead-seller would have charged you for one expensive name at a time.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A foundation search that finds <em>you, not a directory</em>",
        "body_html": 'A homeowner a couple of towns over notices a floor that has started to slope and searches for a foundation company near them. Instead of a national directory that would sell their details to three companies at once, they find your site ranking for that town, with a page that calmly explains what a sloping floor can mean and walks through your free inspection and engineered estimate. They read a few honest reviews, see that you are credentialed and that your work is warrantied, and book a free inspection right there. The inquiry comes straight to you, you paid nothing per lead, and no middleman ever touched it. Illustrative example, not a client.'},
    "faqs": [
        ("Will my site actually outrank the big directories?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the local and sign-specific searches a national directory has no reason to target well, which is exactly where a local foundation company can win."),
        ("How is this different from buying foundation leads?",
         "A lead marketplace rents you an inquiry it also sells to your competitors, and it stops the day you stop paying. A website you own captures inquiries that are yours alone and keeps working long after it is built, without an expensive per-lead fee coming out of every job."),
        ("Why does the site itself matter so much for foundation repair?",
         "Because a frightened homeowner is about to spend a large sum on their home. Before they call, they read your site to see whether you look established, credentialed, and honest, or like someone trying to scare them. A calm site with before-and-after proof, a clear process, your warranty, and straight answers is often what decides between you and the next company on the list."),
        ("Do I need to rank for every town I serve?",
         "You rank for the ones that matter most first."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks, and broader terms take longer and compound over months. Setup is included with no separate fee.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for foundation repair companies"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
},
]
