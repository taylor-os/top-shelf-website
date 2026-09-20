"""Colony page specs for GENERAL CONTRACTORS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a general-contracting owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, general-contractor-specific substance (the generator
owns shell, schema, events, keyword placement). Honesty rules match the money specs: no invented
stats, percentages, or clients; only the real prices ($299/$899/$2,500 plans, $1,500 one-time
site) ever appear, and no project prices are ever invented; hedge instead of overpromise; no
em/en dashes anywhere; never "leak" as a metaphor. Ethics: the AI does intake and scheduling
ONLY, it never quotes a price or binds a bid.

The general-contractor angle, kept DISTINCT from the specialty home-services trades (plumbers,
roofers, flooring, fence, foundation): a GC sells large PROJECTS (kitchen and bath remodels,
additions, whole-home renovations), not one specialty repair. The buyer gathers three or four
bids and takes weeks to decide on a large sum, so bid follow-up over that long cycle is decisive.
The work is won on a portfolio of finished projects, licensing and trust, referrals and repeat
clients, and being reachable while the owner is on a job site coordinating subs and schedules.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 general-contractor-website-cost            (cost)    -> websites-seo-for-general-contractors
  2 general-contractor-answering-service-cost  (cost)    -> ai-receptionist-for-general-contractors
  3 is-a-crm-worth-it-for-a-general-contractor (cost)    -> crm-for-general-contractors
  4 why-general-contractors-miss-calls         (problem) -> ai-receptionist-for-general-contractors
  5 why-contractor-bids-go-cold                (problem) -> crm-for-general-contractors
  6 how-do-general-contractors-get-more-clients(how-to)  -> marketing-for-general-contractors
"""

TOPICS = [
# ============ How Much Does a General Contractor Website Cost? (cost -> websites-seo) ============
{
    "slug": "general-contractor-website-cost",
    "h1": "How Much Does a General Contractor Website Cost?",
    "title": "How Much Does a General Contractor Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A general contractor website ranges from cheap templates to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on a plan.",
    "answer": "A general contractor website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more than the price is whether it shows your finished projects, proves you are licensed and insured, and gets found locally. Top Shelf builds a custom site for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a general contractor website has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner about to hand a builder a large sum and the keys to their home for months does not skim a website the way they would for a quick repair. They are deciding whether to trust you, so the site has a bigger job to do than simply exist. Before you compare quotes, it helps to know what the site actually has to accomplish for a purchase this size.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Show a real portfolio of completed projects, kitchens, additions, whole-home renovations, because photos of finished work are the proof a nervous buyer needs before they call.</li><li>Make requesting a consultation or an estimate obvious on every page, so a ready homeowner can reach you in one tap instead of hunting for a number.</li><li>Prove you are licensed, insured, and established, the trust signals that matter most when someone is spending real money on their house.</li><li>Get found for the searches homeowners actually use, general contractor near me, home addition contractor, kitchen remodel near me, not just sit at a web address nobody types.</li></ul>'},
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number swings because a site you fill in yourself and a site built to win a homeowner over on a major project are different things with the same name. What raises the cost is the work that makes a contractor look established and get found: a portfolio laid out to sell, pages written to rank for the towns you build in, and the ongoing search work that keeps you visible after launch. A cheap template can get you online, but if it does not show your work or turn up in a search, its low price is not really a bargain, because it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that wins the project",
    "bridge_text": "A general contractor website earns its keep by turning a homeowner search into a booked consultation. Ours is built to show your finished work, prove you are established, rank for the towns you build in, and turn a visit into a call.",
    "bridge_slug": "websites-seo-for-general-contractors",
    "bridge_label": "Websites & SEO for general contractors",
    "faqs": [
        ("Is a cheap template site good enough for a general contractor?",
         "It can get you online, but a template you fill in yourself rarely shows your finished projects well or ranks for the searches homeowners use, and you do the upkeep. For a purchase as large as a remodel, a site that does not build trust or get found is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "general_contractors", "trade_plural": "general contractors",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== What Does a General Contractor Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "general-contractor-answering-service-cost",
    "h1": "What Does a General Contractor Answering Service Cost?",
    "title": "What Does a General Contractor Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for contractors often bill per call or per minute. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for general contractors usually bill per call, per minute, or a monthly retainer, so a busy stretch gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every project call, captures the scope, and books the consult comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy stretch turns into a big bill. A general contractor is a poor fit for that model in a particular way: you get a small number of very high-value project calls rather than a steady stream of small tickets, and a lot of them land in the evenings and on weekends when homeowners finally sit down to research a remodel. It is worth knowing the common models before you sign one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for every call answered, so a wave of early-stage tire-kickers costs the same as a serious buyer.</li><li>Per-minute pricing: you pay for talk time, so a homeowner who wants to talk through a whole renovation runs up the meter.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner planning a kitchen remodel or an addition lines up three or four contractors and leans toward the one who picks up and sounds organized. The real cost of no coverage is not a monthly fee, it is the whole project that went to the builder who answered first. But a generic call center reading a script cannot tell a full gut renovation from a small repair, or which caller is ready to book a consult and which is a year out, so you can pay for coverage and still get poor triage.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, asks what the homeowner wants built and captures the scope, and books the consult on your calendar or hands you a qualified lead. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. Because a contractor lives on a small number of large projects, one remodel you would have lost while your hands were full is usually worth far more than the plan costs for a long stretch. It does the intake and scheduling only, it never guesses at a price or commits you to a bid, so you always set the scope and the number yourself.</p>'}],
    "bridge_h2": "Answer every project call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, captures the scope a real consult needs, and books it, all on a flat monthly plan. It handles intake only and never binds a bid.",
    "bridge_slug": "ai-receptionist-for-general-contractors",
    "bridge_label": "AI receptionist for general contractors",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the one project call it captures instead of losing to voicemail, which for a contractor can be worth more than the plan costs for months."),
        ("Can it price a job or commit me to a bid?",
         "No, and that is on purpose. It captures what a consult needs, what they want built, roughly when, and whether they have plans or a budget, then books the appointment or hands you the lead. You still walk the project and set the scope and the price yourself, so nothing is quoted or promised in your name.")],
    "trade_slug": "general_contractors", "trade_plural": "general contractors",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Is a CRM Worth It for a General Contractor? (cost -> crm) ============
{
    "slug": "is-a-crm-worth-it-for-a-general-contractor",
    "h1": "Is a CRM Worth It for a General Contractor?",
    "title": "Is a CRM Worth It for a General Contractor? | Top Shelf Business Solutions",
    "meta_desc": "For most general contractors a CRM pays for itself by winning back one cold bid and reviving past clients. It comes in the Signature plan at $899/mo.",
    "answer": "For most general contractors, yes. A CRM pays for itself the first time it wins back a bid you would have let go cold, or brings a past client back for their next project. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a general contractor when you have more open bids, past clients, and referral sources than you can personally keep track of, which is most established builders. It is not worth it if you run one small job at a time and are genuinely calling everyone back, though that rarely stays true as you grow. The honest test is simple: how many bids have you put real time into over the last few months that you never followed up on, and how many past clients have not heard from you in a year or two? On a remodel or an addition the decision takes weeks, so a bid that goes quiet is usually still deciding, and a home you already built is the warmest lead you have for the next project. Those are exactly the jobs a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a contractor is not the software, it is the work that stops slipping away. A homeowner still weighing a bid over several weeks, a family whose kitchen you finished two years ago, a designer or an agent who could send you the next renovation: each one is a project you have half-earned and are one timely touch away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open bid on a schedule, so a homeowner comparing three contractors keeps hearing from you across the weeks they take to decide, while the others go quiet.</li><li>It keeps past clients and referral sources warm, the designers, architects, and agents who send you work, so the repeat projects and referrals come back without you tracking dates.</li><li>It keeps every client, bid, project photo, and note in one place instead of a truck console full of paper and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. Because a contractor lives on a small number of large projects, recovering a single one you would have lost pays for it for a long stretch, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your bids and past clients to work",
    "bridge_text": "The bids you already sent and the homes you already built are the cheapest projects you can win. A CRM follows up on every one for you, so the homeowner comparing contractors and the past client planning their next project both come back to you.",
    "bridge_slug": "crm-for-general-contractors",
    "bridge_label": "CRM for general contractors",
    "faqs": [
        ("Is a CRM overkill for a small general contracting business?",
         "Not usually. Even a one-crew builder puts out more bids and has built for more homes than anyone can track by memory, and each project is large. The point is not size, it is whether follow-up is falling through. If bids go cold and past clients forget your name, a CRM earns its keep."),
        ("How is a CRM different from keeping notes in my phone?",
         "A phone full of contacts does not follow up on a bid, does not remind you which past client is due for their next project, and does not keep your referral sources warm. A CRM does all of that on a schedule, so the repeat work and referrals show up instead of depending on you to remember.")],
    "trade_slug": "general_contractors", "trade_plural": "general contractors",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do General Contractors Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-general-contractors-miss-calls",
    "h1": "Why Do General Contractors Miss So Many Calls?",
    "title": "Why Do General Contractors Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "General contractors miss calls because they ring from a job site, and a homeowner shopping three or four builders does not leave a voicemail, they call the next one.",
    "answer": "You miss calls because they ring while you are on a job site, coordinating subs, meeting an inspector, or pricing the next job from the truck. A homeowner lining up three or four contractors does not leave a voicemail, they call the next name on the list. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">General contracting is a hands-full, on-site trade. When the phone rings you are usually walking a framing crew through a change, coordinating a sub who showed up late, meeting an inspector, or pricing the next job from the truck between stops, and none of those are moments you can stop and take a call. The busier you are running active projects, the more calls you miss, which means your best stretches are also when the most new work slips away. It is not a discipline problem. One person cannot run the jobs in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a homeowner planning a remodel it is not one. Someone about to spend a large sum lines up three or four contractors and leans toward the one who answers and sounds organized. They are not going to leave a message and wait, they move down the list until a real, professional voice picks up, and by the time you check your phone the project is already gone.</p>'},
        {"h2_html": "A missed call is a whole <em>project lost</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal, and for a contractor the stakes are higher than most trades. You do not lose a small service ticket you can shrug off, you lose a whole remodel or addition, the kind of project that can carry a slow month, to whoever happened to answer. Those inquiries also tend to come in the evenings and on weekends, when homeowners finally sit down to research who to hire, which is exactly when a call is most likely to roll to voicemail. So the calls you are most likely to miss are also the ones worth the most.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that always answers and can qualify a serious buyer, not just take a message. A voicemail box cannot ask what someone wants built, and a generic call center does not know a full renovation from a small repair. What actually works is something that answers on the first ring day or night, asks what the project is, roughly when, and where, and either books the consult on your calendar or hands you a qualified lead, so the homeowner reaches a real answer instead of a beep. It handles the intake and scheduling only, it never quotes a price or commits you to a bid, so you still set the scope yourself.</p>'}],
    "bridge_h2": "Stop losing projects to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, asks what the homeowner wants built, and books the consult or hands you the lead, so the project never rolls to voicemail. It does intake only and never binds a bid.",
    "bridge_slug": "ai-receptionist-for-general-contractors",
    "bridge_label": "AI receptionist for general contractors",
    "faqs": [
        ("Would a homeowner rather reach a real person?",
         "On a project this size, what a homeowner wants most is to know a real, organized company is handling it, and a calm voice that captures the scope beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the details, and books the consult or hands the lead straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are on a ladder, walking a site with an inspector, or already on another call. Something that always answers and qualifies the project is what catches the calls a forward would still miss.")],
    "trade_slug": "general_contractors", "trade_plural": "general contractors",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do My Contractor Bids Go Cold? (problem -> crm) ============
{
    "slug": "why-contractor-bids-go-cold",
    "h1": "Why Do My Contractor Bids Go Cold?",
    "title": "Why Do My Contractor Bids Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most contractor bids go cold not over price but because nobody followed up. A remodel is a slow, weeks-long decision, and it goes to the builder who stayed in touch.",
    "answer": "Most contractor bids go cold not because your price was wrong, but because nobody followed up. A remodel or an addition is a big decision, so the homeowner gathers other bids, talks it over, and lines up financing over several weeks. The project goes to whoever stayed in front of them, which is rarely the cheapest.",
    "sections": [
        {"h2_html": "Silence usually means still deciding, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet bid as a no on price, so you drop it and move on. But on a large project the homeowner almost never decided against you that fast. They asked for a bid on a kitchen or an addition, meant to think it over, and then the size of the decision slowed everything down. They are weighing two or three other numbers, talking it through with a spouse, and lining up financing, and a choice this big rarely lands in a week. A month later they could not tell you which of the contractors who came out quoted what.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The one who wins the project is usually not the cheapest. It is the one who stayed in front of them through the long decision, a friendly check-in a week later, a note answering the question they were stuck on, a nudge when the season they mentioned arrives. That steady presence is what turns a maybe into a signed contract, and being the organized one who never dropped the thread is exactly the reassurance a nervous buyer wants before handing over a large sum.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Contractors do not skip follow-up because they are lazy. They skip it because running the jobs you already have eats the day. You are coordinating subs, chasing a delivery that came up short, keeping three active sites on schedule, and handling the problem that jumped the line, and by evening the bid you sent two weeks ago is out of sight. Doing it from memory means it only happens when things are slow, which is exactly when you have the fewest bids to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which bids are still open and quietly going cold.</li><li>The follow-up depends on you remembering, so it competes with the work in front of you and loses.</li><li>By the time you circle back, the homeowner has already signed with the contractor who stayed in touch.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open bid gets timed check-ins automatically, written to sound like you and spaced across the weeks a homeowner actually takes to decide, the buyer comparing contractors keeps hearing from you while the others go silent, and the projects you already priced stop slipping away.</p>'}],
    "bridge_h2": "Follow up on every bid, automatically",
    "bridge_text": "A CRM keeps every open bid in front of you and sends timed check-ins for you across the weeks a homeowner takes to decide, so the buyer comparing contractors keeps hearing from you while the other builders go quiet.",
    "bridge_slug": "crm-for-general-contractors",
    "bridge_label": "CRM for general contractors",
    "faqs": [
        ("How many times should I follow up on a bid?",
         "A few light touches spread across the weeks a homeowner takes to decide catches most of the maybes without being pushy: a check-in a week after the bid, a note answering common questions, and a nudge when they said they would be ready. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly check-in reads as attentive and organized, which is exactly the reassurance a homeowner wants before a big project. You can always jump in and message anyone directly.")],
    "trade_slug": "general_contractors", "trade_plural": "general contractors",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Do General Contractors Get More Clients? (how-to -> marketing) ========
{
    "slug": "how-do-general-contractors-get-more-clients",
    "h1": "How Do General Contractors Get More Clients?",
    "title": "How Do General Contractors Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "General contractors get more clients from referrals and repeat work first, then from being easy to find and trust online when a homeowner searches for a builder.",
    "answer": "General contractors get more clients by working the warmest leads first, referrals and past clients, then making sure a homeowner searching for a builder can find you, trust you, and see your finished work. Word of mouth wins most remodels, but being visible and credible online is what turns a stranger search into a call.",
    "sections": [
        {"h2_html": "Start with the warmest leads you <em>already have</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The cheapest and most reliable clients a general contractor gets are the ones who already trust you or were sent by someone who does. Word of mouth wins most remodels, because a homeowner about to hand a builder a large sum and the keys to their home for months would far rather hire the contractor a friend, a designer, or an agent already vouched for. That trust arrives before you do. So the first place to find more clients is not an ad, it is the referral and repeat work you are probably leaving on the table.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Stay in touch with past clients, because the kitchen you finished this year is the bathroom or the addition you win next year.</li><li>Keep your referral sources warm, the designers, architects, and agents who can hand you a steady stream of projects.</li><li>Ask for the referral and the review while the work is still fresh, when a happy client is most glad to give one.</li></ul>'},
        {"h2_html": "Then be easy to <em>find and trust online</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The warm leads only go so far, and the rest of your growth comes from homeowners who do not know you yet and start on Google. When someone searches for a general contractor or a home remodel near them, the first thing that shows is the map pack, the three local listings with star ratings, so a verified, active Google Business Profile with a steady flow of genuine reviews is often what gets you in front of a new buyer at all. From there they are deciding whether to trust you with a big, expensive job, and that is where a website full of finished projects, kitchens, additions, whole-home renovations, does the convincing that a phone number alone cannot.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Put together, getting more clients is less about one clever tactic and more about doing all of it steadily: keep the referral engine warm, stay visible where homeowners search, collect real reviews, and show your work so a stranger can trust you the way a referral already does. What no honest company can promise is a specific ranking or a set number of leads, because no one controls Google, but these are the levers that actually move it, and a free audit can show you which one is costing you the most right now.</p>'}],
    "bridge_h2": "Turn your reputation into a steady stream of projects",
    "bridge_text": "Getting more clients means working your referrals and repeat clients while staying visible and credible where homeowners search. Marketing built for contractors keeps the warm leads warm and puts you in front of the new ones looking for a builder.",
    "bridge_slug": "marketing-for-general-contractors",
    "bridge_label": "Marketing for general contractors",
    "faqs": [
        ("What is the best source of new clients for a general contractor?",
         "Referrals and repeat clients, by a wide margin. On a purchase as large as a remodel, a homeowner trusts a recommendation far more than an ad, so the builders who grow fastest are usually the ones who stay in touch with past clients and referral sources. Online visibility then adds the new buyers who do not know you yet."),
        ("Do I need to run ads to get more remodels?",
         "Not necessarily. Many contractors grow on referrals, repeat work, and a strong, well-reviewed presence in local search before spending a dollar on ads. Ads can add reach once those basics are working, but a warm referral engine and being easy to find and trust online usually come first.")],
    "trade_slug": "general_contractors", "trade_plural": "general contractors",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
