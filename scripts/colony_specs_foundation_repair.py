"""Colony page specs for FOUNDATION REPAIR (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a foundation-repair-business owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Same contract and honesty rules as scripts/colony_specs_plumbers.py (this file matches its schema
key-for-key), and the same foundation-repair voice as scripts/specs_foundation_repair.py. Foundation
repair is a high-ticket, engineered sale that starts with a frightened homeowner: a stair-step crack
in the brick, a door that will not latch, a floor that has started to slope. The caller is anxious
and researching hard, the sale runs from free inspection to engineered estimate to a decision made
over weeks of second opinions and financing, a transferable warranty and credentials matter, and the
company that answered fast and felt calm and trustworthy wins. So the substance leans on calming an
anxious first-time caller, relentless follow-up on outstanding estimates over the weeks a homeowner
compares opinions, honest non-alarmist education (a real structural problem versus ordinary settling),
and a credible presence that converts a scared researcher. Never scare tactics, never a promised
repair price. The AI answers and books the free inspection only, it never diagnoses or quotes the
repair, and nothing here guarantees a structural outcome or a ranking.

No invented stats, percentages, prices, or clients; hedge instead of overpromise; only the real prices
(the $1,500 one-time site and the $299/$899/$2,500 monthly plans, CRM+AI in the $899 Signature) ever
appear; no invented foundation repair prices; no em/en dashes anywhere; "go cold"/"slip through",
never "leak" as a money metaphor (a literal foundation water leak would be fine).

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 foundation-repair-website-cost                        (cost)     -> websites-seo-for-foundation-repair
  2 foundation-repair-answering-service-cost              (cost)     -> ai-receptionist-for-foundation-repair
  3 is-a-crm-worth-it-for-a-foundation-repair-company     (cost)     -> crm-for-foundation-repair
  4 why-foundation-repair-companies-miss-calls            (problem)  -> ai-receptionist-for-foundation-repair
  5 why-foundation-repair-estimates-go-cold               (problem)  -> crm-for-foundation-repair
  6 how-do-foundation-repair-companies-get-more-customers (how-to)   -> marketing-for-foundation-repair
"""

TOPICS = [
# ============ How Much Does a Foundation Repair Website Cost? (cost -> websites-seo) ============
{
    "slug": "foundation-repair-website-cost",
    "h1": "How Much Does a Foundation Repair Website Cost?",
    "title": "How Much Does a Foundation Repair Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A foundation repair website runs from a cheap template to a few thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A foundation repair website can run from a couple hundred dollars for a template to several thousand for a custom build, but the price matters far less than whether it books inspections. It has to make a frightened homeowner trust you enough to request a free inspection. Top Shelf builds one for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a foundation repair website has to <em>actually do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before you compare prices, it helps to know what you are really buying, because a foundation repair website is not a brochure. It is the thing a frightened homeowner reads late at night, after they spotted a stair-step crack in the brick or a door that will not latch, while they decide whether you are a real, credentialed company or someone who will scare them and vanish. A site that does that job well is worth far more than a cheap one that does not, and it is a different product from the template a hobby business fills in.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Puts requesting a free inspection front and center, so a worried homeowner can book one in a tap instead of hunting for a buried form or a number nobody answers.</li><li>Builds credibility fast, with your credentials, your process from free inspection to engineered estimate, and your transferable warranty stated plainly, because someone about to spend a large sum reads all of it before they call.</li><li>Shows before-and-after photos of real jobs and answers the fear a homeowner actually carries, is this serious, can it wait, will you oversell me, without a scare tactic or a promised number.</li><li>Ranks for what a scared homeowner types, foundation repair near me and your city, so they find you instead of a directory that sells their details to three companies at once.</li></ul>'},
        {"h2_html": "What that <em>costs</em>, and what drives the number",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number you see quoted swings widely because those are not all the same product. A do-it-yourself builder is cheap monthly, but you do the work and it is rarely built to rank or to reassure a nervous buyer. A one-time custom build costs more up front and is yours to keep, but a site alone does little if nobody is doing the ongoing SEO that gets it found on foundation repair near me. An agency retainer bundles the build with that ongoing work, which is where most of the long-term value lives and also where the monthly cost lives. Before you sign anything, ask who owns the site, what a change costs, and whether you keep it if you leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that books inspections",
    "bridge_text": "A foundation repair website earns its money by turning a scared midnight searcher into a booked inspection. Ours is built to rank for the towns you serve, prove you are credible, and make requesting a free inspection effortless.",
    "bridge_slug": "websites-seo-for-foundation-repair",
    "bridge_label": "Websites & SEO for foundation repair",
    "faqs": [
        ("Is a cheap template site good enough for a foundation company?",
         "It can put you online, but a template you fill in yourself is rarely built to rank or to reassure a homeowner about to spend a large sum. For a repair this size, a site that looks thin or loads slowly quietly costs you the inspection to a company that looks more established, so its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "foundation_repair", "trade_plural": "foundation repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ====== What Does a Foundation Repair Answering Service Cost? (cost -> ai-receptionist) ======
{
    "slug": "foundation-repair-answering-service-cost",
    "h1": "What Does a Foundation Repair Answering Service Cost?",
    "title": "What Does a Foundation Repair Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for foundation repair often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for foundation repair usually bill per call, per minute, or a monthly retainer plus overage, so a busy stretch gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call, calms the homeowner, and books the free inspection comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month becomes a big bill. Foundation calls also tend to land at the worst times for a live service, in the evening or on a weekend, once a homeowner finally sits down, really looks at the crack they have walked past for months, and starts searching photos that scare them worse. Those after-hours minutes are often the ones that cost the most. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of nervous tire-kickers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, and a frightened homeowner with a lot of questions is exactly the caller who runs long.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner who just spotted a crack does not call one company, they call three or four in a row and lean hard toward the first that picks up and sounds calm. A voicemail box cannot reassure a frightened person, and a generic call center reading a script cannot steady a nervous caller or gather the right signs. So you can pay for coverage and still lose the job to whoever sounded like a real foundation company.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, stays calm instead of alarmist, gathers what the homeowner is seeing and where, and books the free inspection on your calendar. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. Because a foundation company lives on a small number of large, engineered jobs, one inspection you would have lost on a weekend can be worth well more than the plan costs, and everything after that is on top. It handles scheduling and intake only, it never diagnoses the problem or quotes the repair, that stays with your estimator.</p>'}],
    "bridge_h2": "Answer every anxious call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, calms a frightened homeowner, and books the free inspection, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-foundation-repair",
    "bridge_label": "AI receptionist for foundation repair",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the inspection it books instead of losing an anxious caller to voicemail."),
        ("Does it diagnose the problem or quote the repair over the phone?",
         "No, and it should not. It handles the call and the calendar only. It calms the homeowner, gathers what they are seeing, and books the free inspection. Diagnosing a foundation and pricing an engineered repair stays with your estimator on site, where it belongs.")],
    "trade_slug": "foundation_repair", "trade_plural": "foundation repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ====== Is a CRM Worth It for a Foundation Repair Company? (cost -> crm) ======
{
    "slug": "is-a-crm-worth-it-for-a-foundation-repair-company",
    "h1": "Is a CRM Worth It for a Foundation Repair Company?",
    "title": "Is a CRM Worth It for a Foundation Repair Company? | Top Shelf Business Solutions",
    "meta_desc": "For most foundation repair companies a CRM pays for itself following up on engineered estimates over the weeks a homeowner decides. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most foundation repair companies, yes. The decision on a big repair is made over weeks of second opinions and financing, and a CRM pays for itself the first time it follows up on an engineered estimate you would have let go quiet, or revives an old inspection. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a foundation repair company when you are delivering more estimates and sitting on more past inspections than you can personally keep track of, which is nearly every established shop. It is not worth it if you close every job at the kitchen table and never send an estimate a homeowner takes time to think about, which almost never describes this trade, because a repair this size is decided over weeks, not on the spot. The honest test is simple: how many engineered estimates have you delivered in the last few months that went quiet, and how many old inspections are sitting untouched from homeowners who said they wanted to watch it. Those are the jobs a CRM is built to bring back.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a foundation company is not the software, it is the work that stops slipping away in the long gap between the inspection and the signature. A family sitting on a pier estimate while they get a second opinion, a homeowner waiting on financing, an inspection you ran a year ago for someone who decided to wait: each one is a job you have already half-earned and are one honest check-in away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open estimate on the cadence you set, so a homeowner comparing three companies keeps hearing from you while the other two go silent.</li><li>It keeps a gentle, honest touch with the not-yet buyers, so when a crack widens, a door stops latching, or they go to sell, your name is the one already in front of them.</li><li>It keeps every lead, inspection, and engineered estimate in one place instead of a truck console and whatever anyone can still remember a month later.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one engineered job you would have lost to silence and it has paid for itself many times over, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your estimates and old inspections to work",
    "bridge_text": "The estimates you already delivered and the inspections you already ran are the cheapest jobs you can get. A CRM follows up on every one over the weeks a homeowner decides, so they sign with you instead of whoever stayed in touch.",
    "bridge_slug": "crm-for-foundation-repair",
    "bridge_label": "CRM for foundation repair",
    "faqs": [
        ("Is a CRM overkill for a small foundation repair company?",
         "Not usually. Even a one-crew shop delivers more engineered estimates and carries more past inspections than anyone can track by memory, and each one is a large job. The point is not size, it is whether follow-up over a weeks-long decision is falling through. If estimates go quiet and old inspections are forgotten, a CRM earns its keep."),
        ("How is a CRM different from keeping notes in a spreadsheet?",
         "A spreadsheet does not follow up on an estimate, does not remind you which one is going cold, and does not tell you which homeowner who decided to wait is ready now. A CRM does all of that on a schedule, so the estimates you delivered and the inspections you ran actually turn into signed jobs.")],
    "trade_slug": "foundation_repair", "trade_plural": "foundation repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ====== Why Do Foundation Repair Companies Miss Calls? (problem -> ai-receptionist) ======
{
    "slug": "why-foundation-repair-companies-miss-calls",
    "h1": "Why Do Foundation Repair Companies Miss Calls?",
    "title": "Why Do Foundation Repair Companies Miss Calls? | Top Shelf Business Solutions",
    "meta_desc": "Foundation repair companies miss calls because they ring while a crew is under a house, and a frightened homeowner does not leave a voicemail, they call the next company.",
    "answer": "Foundation repair companies miss calls because they come in while your hands are full, under a house, setting piers, or driving between inspections, and often in the evening once a homeowner finally panics about a crack. A scared homeowner does not leave a voicemail, they call the next company. The fix is making sure every call gets a calm answer.",
    "sections": [
        {"h2_html": "The call comes exactly when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Foundation repair is a hands-full trade. When the phone rings you are often under a house, watching a crew set piers, down in a crawl space with no signal, or driving between inspections, and none of those are moments you can stop and take a call. Worse, the calls cluster in the evenings and on weekends, because that is when a homeowner finally sits down, really looks at the crack they have been walking past, searches photos that scare them, and works up the nerve to call. Those are exactly the hours you are least likely to be by the phone. It is not a discipline problem. One person cannot be under a house and answering every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a frightened homeowner it is not one. Someone half-convinced their house is coming apart is not going to leave a message and wait. They move down the list until a real person answers and sounds calm, and by the time you check your phone, the inspection is already booked with someone else.</p>'},
        {"h2_html": "A missed foundation call is your most <em>expensive miss</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A foundation company lives on a small number of large, engineered jobs, so the call you let ring out is not a small service ticket, it is a whole pier job or slab repair, the kind that can carry a slow month. Handing that to whoever answered faster is the most expensive thing a full day quietly costs you. And because a frightened caller is looking for someone to trust before they are looking for a price, the company that picks up calm and first is usually the one that wins the job.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can steady a nervous homeowner instead of reading a script. A voicemail box cannot reassure anyone, and a generic call center cannot sound like a company that actually goes under houses. What works is something that answers on the first ring day or night, stays calm, asks what they are seeing and where, gets the address, and books the free inspection or flags a hot lead to your phone, so the anxious call never rolls to voicemail in the first place. It handles the intake and the calendar only, it does not diagnose or quote, that stays with your estimator.</p>'}],
    "bridge_h2": "Stop losing inspections to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, calms a frightened homeowner, and books the free inspection or flags it to you, so the anxious call never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-foundation-repair",
    "bridge_label": "AI receptionist for foundation repair",
    "faqs": [
        ("Would a worried homeowner rather reach a real person?",
         "What a frightened homeowner needs most is to know a real, steady company is going to come look, and a calm voice that captures the details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the signs, and books the free inspection, and it hands a hot lead straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are under a house, setting piers, or already on another call, which is most of the day. Something that always answers and stays calm is what catches the calls a forward would still miss.")],
    "trade_slug": "foundation_repair", "trade_plural": "foundation repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ====== Why Do Foundation Repair Estimates Go Cold? (problem -> crm) ======
{
    "slug": "why-foundation-repair-estimates-go-cold",
    "h1": "Why Do Foundation Repair Estimates Go Cold?",
    "title": "Why Do Foundation Repair Estimates Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most foundation repair estimates go cold not over price but because nobody followed up over the weeks a homeowner spends on second opinions and financing.",
    "answer": "Most foundation repair estimates go cold not because your price was wrong, but because nobody followed up. A repair this size is decided over weeks while the homeowner gets second opinions, lines up financing, and wonders whether it is urgent yet. The job goes to whoever stayed in touch, and a quiet estimate is usually a maybe, not a no.",
    "sections": [
        {"h2_html": "Silence usually means still deciding, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet estimate as a no on price, so you drop it and move on. But most of the time the homeowner did not decide against you at all. They got an engineered estimate on a pier job or a slab repair, a large and frightening number, and they did what anyone does with a decision that big: they went to think. They are getting a second and third opinion, talking it over with a spouse, waiting to hear about financing, and quietly wrestling with whether the problem is urgent enough to act on now. A week later they could not tell you which of the three companies said what.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The company that wins is usually not the cheapest. It is the one that stayed calm and in front of them, a friendly check-in a few days later, an honest answer to the is-it-urgent question they are stuck on, a nudge when financing is the thing holding them up. That steady second touch is what turns a maybe into a signed job, and it is exactly the thing there is no time for between inspections.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Foundation companies do not skip follow-up because they are lazy. They skip it because the day fills up. You run an inspection, deliver the estimate, roll to the next job, manage the crew, and by the time a homeowner is ready to talk weeks later, the estimate you delivered in March is long out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest estimates to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system telling you which engineered estimates are still open and which are quietly going cold.</li><li>The follow-up depends on you remembering across a decision window that runs weeks or months, so it competes with the actual work and loses.</li><li>By the time you circle back, the homeowner has signed with whichever company happened to check in at the right moment.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open estimate gets timed, honest check-ins automatically, written to sound like you, the homeowner comparing companies keeps hearing from you across the whole decision while the others go silent, and the engineered jobs you already quoted stop slipping away.</p>'}],
    "bridge_h2": "Follow up on every estimate, automatically",
    "bridge_text": "A CRM keeps every open estimate in front of you and sends timed, honest check-ins for you across the weeks a homeowner decides, so the family weighing a big repair keeps hearing from you while the other companies go quiet.",
    "bridge_slug": "crm-for-foundation-repair",
    "bridge_label": "CRM for foundation repair",
    "faqs": [
        ("How many times should I follow up on a foundation estimate?",
         "A handful of light, honest touches spread across the decision window catches most of the maybes without being pushy: a check-in a few days after the estimate, a calm answer to the is-it-urgent question, and a nudge when financing comes up. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal on a big repair?",
         "Not when it is written to sound like you and paced sensibly. A short, honest check-in reads as steady and attentive, which is exactly the reassurance a nervous buyer on a large repair wants. Most homeowners appreciate the nudge because they meant to get back to you, and you can jump in and message anyone directly any time.")],
    "trade_slug": "foundation_repair", "trade_plural": "foundation repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ====== How Do Foundation Repair Companies Get More Customers? (how-to -> marketing) ======
{
    "slug": "how-do-foundation-repair-companies-get-more-customers",
    "h1": "How Do Foundation Repair Companies Get More Customers?",
    "title": "How Do Foundation Repair Companies Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Foundation repair companies get more customers by earning trust, steady reviews, honest education, and local visibility, so a wary homeowner calls them first.",
    "answer": "Foundation repair companies get more customers less by chasing demand and more by earning trust. A homeowner who spots a crack researches hard and rules out anyone who looks thin or pushy before they call. Steady genuine reviews, honest education, and strong local visibility make you the credible, non-alarmist name they call first when fear sends them looking.",
    "sections": [
        {"h2_html": "A foundation customer is won on trust, not <em>reach</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody hires the first foundation company they stumble on the way they grab the nearest coffee. A homeowner who spots a crack is frightened on two fronts at once, scared the house is failing and just as scared of being talked into a huge repair they may not need. That second fear runs deep in this trade, because everyone has heard the story of the company that scared someone into a fortune of work. So they research. They read reviews, compare companies, ask a neighbor who had it done, and quietly rule out anyone who looks thin, pushy, or hard to trust before they ever make contact.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting more customers, then, is less about shouting the loudest at people with no problem yet and more about being easy to find and easy to believe the moment fear sends someone looking. The work you do is good. The job of your marketing is making a wary homeowner know that before they ever let you in the door.</p>'},
        {"h2_html": "How you become the name they <em>call first</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not do it with one clever trick. You do it by being visible and credible in the exact spots a scared homeowner looks, and by doing it consistently.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep your Google Business Profile active and complete, because the map pack is the first thing a homeowner sees and their first read on whether you are worth a call at all.</li><li>Build a steady flow of genuine reviews and reply to them calmly, because a buyer braced to be oversold leans on reviews harder here than in almost any trade, and reviews also lift you in local search.</li><li>Publish honest education, plain answers to what causes foundation movement, which signs matter, and how to tell a real problem from ordinary settling, so you read as the straight shooter instead of another company trying to frighten them.</li><li>Focus on the specific towns you serve, because foundation problems are local to the soil, and a homeowner searching foundation repair near me wants a company that clearly works their area.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Do that consistently and you are on the short list before the first call, and you stay in front of past customers, who send you the neighbor with the same worry and whose transferable warranty comes up again when they sell. None of it promises a number or scares anyone into a sale, and none of it can honestly guarantee a ranking, because no one controls Google, but it is what steadily turns frightened searchers into homeowners who call you first.</p>'}],
    "bridge_h2": "Be the foundation name they already trust",
    "bridge_text": "Most foundation calls begin with a scared homeowner researching who to trust. Keeping your Google profile active, your reviews steady, and your answers honest is how you become the credible name they call when a crack appears nearby.",
    "bridge_slug": "marketing-for-foundation-repair",
    "bridge_label": "Marketing for foundation repair",
    "faqs": [
        ("What is the fastest way to get more foundation customers?",
         "There is no overnight switch, but the fastest durable lever is trust where people already look: a complete, active Google Business Profile and a steady stream of genuine reviews. Those often earn a wary homeowner their first call and lift you in local search at the same time, so more nearby searchers find you."),
        ("Do I need to run ads to get foundation customers?",
         "Not necessarily. Much of this trade is won on trust and local visibility that you own, your profile, reviews, honest education, and pages tied to the towns you serve, which keep working without a per-click or per-lead fee. Ads can add reach on top, but the credible, findable presence is what a frightened homeowner is actually looking for.")],
    "trade_slug": "foundation_repair", "trade_plural": "foundation repair companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
