"""Colony page specs for FENCE COMPANIES (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a fence-company owner would search, answered directly up top (the
40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the page's
authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, fence-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear, and never an invented fence price; no em/en dashes anywhere;
never "leak" as a metaphor. The AI receptionist does scheduling and intake ONLY, it never sets a
price or binds an estimate, the owner always walks the yard and quotes it.

The fence reality every page leads with: a homeowner planning a fence (privacy, a new dog, a
pool-code enclosure, a new-build lot) calls three or four companies for estimates and hires
whoever answers and comes out to measure soonest. Choices are wood, vinyl, aluminum, chain-link.
The season is spring, summer, and new construction. HOA approvals and property-line questions
stretch the decision over weeks. The crew is out setting posts and misses the estimate call, and
capturing and following up quotes over the deciding weeks is the CRM win. This is a fence
specialty, NOT a whole-project general contractor.

Six questions, mixed cost / problem, spread across the four fence money pages:
  1 fence-company-website-cost              (cost)    -> websites-seo-for-fence-companies
  2 fence-company-answering-service-cost    (cost)    -> ai-receptionist-for-fence-companies
  3 is-a-crm-worth-it-for-a-fence-company   (cost)    -> crm-for-fence-companies
  4 why-fence-companies-miss-calls          (problem) -> ai-receptionist-for-fence-companies
  5 why-fence-estimates-go-cold             (problem) -> crm-for-fence-companies
  6 how-do-fence-companies-get-more-customers (problem) -> marketing-for-fence-companies
"""

TOPICS = [
# ============ How Much Does a Fence Company Website Cost? (cost -> websites-seo) ============
{
    "slug": "fence-company-website-cost",
    "h1": "How Much Does a Fence Company Website Cost?",
    "title": "How Much Does a Fence Company Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A fence company website ranges from cheap templates to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A fence company website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more than the price is whether it shows your fence styles, ranks for fence installation near me, and turns a browsing homeowner into an estimate request. Top Shelf builds a custom site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What a fence company website actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner planning a fence is shopping with their eyes. They want to see a privacy run, a picket line, an ornamental aluminum panel, or a chain-link fence before they call anyone, and they are typing "fence company near me" or "fence installation near me" while they do it. So a fence company website earns its money on a few concrete things, not on looking pretty.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A gallery of real fence styles and materials, wood, vinyl, aluminum, and chain-link, so a homeowner can see the look they are picturing and know you build it.</li><li>An instant estimate request, a short form that captures what they want fenced, the material they like, and roughly how much yard, so a browsing visitor becomes a lead instead of a closed tab.</li><li>A clear service area and material list, so the searcher knows you cover their town and build the fence they want.</li><li>A tap-to-call button and a fast, mobile-first layout, because most of these searches happen on a phone out in the backyard.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is a different job from a brochure. A good-looking site that never ranks for the searches homeowners actually make, and buries the estimate request three scrolls down, is the most expensive kind, because you paid for it and it brings you nothing.</p>'},
        {"h2_html": "What a fence company should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number you get quoted swings wildly because you are not all buying the same thing. A do-it-yourself builder is cheap monthly, but you do the work, and it is rarely built to rank or to convert. A one-time custom build is yours to keep, but a site alone does little if nobody is doing the ongoing SEO to get it found for fence installation near me. An agency retainer bundles the build with ongoing SEO, which is where most of the long-term value lives, and also where the monthly cost lives. Before you sign, ask who owns the site, what a change costs, and whether you keep it if you leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a fence site that books measures",
    "bridge_text": "A fence company website is only worth the estimates it brings in. Ours shows your styles, ranks for the fence searches homeowners make, and turns a browsing visitor into a measure on your calendar.",
    "bridge_slug": "websites-seo-for-fence-companies",
    "bridge_label": "Websites & SEO for fence companies",
    "faqs": [
        ("Is a cheap template site good enough for a fence company to start with?",
         "It can get you online, but a template you fill in yourself rarely ranks for fence installation near me, rarely shows your styles well, and rarely turns a visitor into an estimate request, and you do the upkeep. If a site is not getting found or booking measures, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep. On a monthly plan the site is built for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "fence_companies", "trade_plural": "fence companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== What Does a Fence Company Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "fence-company-answering-service-cost",
    "h1": "What Does a Fence Company Answering Service Cost?",
    "title": "What Does a Fence Company Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for fence companies often bill per call or per minute, which adds up in spring. Top Shelf includes an AI receptionist that answers every estimate call in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for fence companies usually bill per call, per minute, or a monthly retainer, so a busy spring gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every estimate call, captures the fence details, and books the measure comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until spring hits and a good month turns into a big bill. A fence company gets its calls in bunches, in the evenings, on weekends, and across the first warm stretch when every homeowner decides at once that this is the year for a fence, which is exactly when the meter runs hottest. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy spring or a wave of price-shoppers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a homeowner walking through HOA rules and materials costs you more than a quick caller.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right in your busy season.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner who has decided to fence the yard calls three or four companies and hires whoever picks up and comes out to measure soonest. The real cost of no coverage is not a monthly fee, it is the estimate that went to the company that answered while your crew was setting posts. But a generic call center reading a script cannot tell a six-foot cedar privacy fence from an aluminum pool enclosure, or which caller is ready to book a measure, so you can pay for coverage and still get bad intake.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day, evening, or weekend, asks what a real measure needs, what they want fenced and why, the material, roughly how much yard, and where the property is, then books the measure or hands you a qualified lead. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One fence job you would have lost while the crew was on an install is often worth more than the plan costs for months, and everything it catches after that is on top. It does not guess at a price or bind an estimate, you still walk the yard and set the number at the measure.</p>'}],
    "bridge_h2": "Answer every estimate call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers day and night, captures the fence details, and books the measure, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-fence-companies",
    "bridge_label": "AI receptionist for fence companies",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly in spring when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the estimate it books instead of losing to voicemail while your crew is setting posts."),
        ("Does it set the fence price or promise a quote?",
         "No. It handles scheduling and intake only. It gathers what the homeowner wants, the material, and roughly how much yard, then books the measure or hands you the lead. You still walk the yard, set the scope, and give the price. It never binds an estimate on your behalf.")],
    "trade_slug": "fence_companies", "trade_plural": "fence companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Is a CRM Worth It for a Fence Company? (cost -> crm) ============
{
    "slug": "is-a-crm-worth-it-for-a-fence-company",
    "h1": "Is a CRM Worth It for a Fence Company?",
    "title": "Is a CRM Worth It for a Fence Company? | Top Shelf Business Solutions",
    "meta_desc": "For most fence companies a CRM pays for itself by rescuing one quote that went cold during the deciding weeks and bringing past yards back for gates and repairs. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most fence companies, yes. A CRM pays for itself the first time it wins back a quote that went quiet while a homeowner compared bids and waited on the HOA, or brings a past yard back for a gate or a repair. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a fence company when you send more quotes and build for more yards than you can personally keep track of, which is most established outfits. It is not worth it if you are a one-crew operation doing a handful of jobs a week and genuinely calling every quote back, though that rarely lasts through a busy spring. The honest test is simple: how many quotes have you sent in the last month that you never followed up on, and how many yards you fenced a few years back have not heard from you since? A fence is rarely a same-day decision, homeowners compare three companies and wait on HOA approval, so a quote that goes quiet is usually not a no. Those are the jobs a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a fence company is not the software, it is the work that stops slipping through. A homeowner sitting on a privacy-fence quote, a family whose backyard you fenced two years ago, a gate that is finally due to be replaced: each one is a job you have already half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open quote on a schedule, so a homeowner comparing three fence companies keeps hearing from you while the other two go quiet.</li><li>It flags the yards you built a few years back that may be due for a repair, a stain, a gate, or an extension, so recurring work comes back without you tracking dates.</li><li>It keeps your whole customer list, the style and material you installed, and job history in one place instead of a truck full of paper quotes and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one job you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your quotes and yards to work",
    "bridge_text": "The quotes you already sent and the yards you already fenced are the cheapest jobs you can get. A CRM follows up on every one for you, so they book you next instead of the company that stayed in touch.",
    "bridge_slug": "crm-for-fence-companies",
    "bridge_label": "CRM for fence companies",
    "faqs": [
        ("Is a CRM overkill for a small fence company?",
         "Not usually. Even a one or two crew outfit sends more quotes and fences more yards than anyone can track by memory, and a fence quote can sit for weeks while a homeowner compares bids and waits on the HOA. The point is not size, it is whether follow-up is falling through. If quotes go cold and past customers forget your name, a CRM earns its keep."),
        ("How is a CRM different from keeping numbers in my phone?",
         "A phone full of contacts does not follow up on a quote, does not remember which yard is due for a gate or a repair, and does not tell you which job is going cold. A CRM does all of that on a schedule, so the repeat work and the quotes you already sent show up instead of depending on you to remember.")],
    "trade_slug": "fence_companies", "trade_plural": "fence companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do Fence Companies Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-fence-companies-miss-calls",
    "h1": "Why Do Fence Companies Miss So Many Calls?",
    "title": "Why Do Fence Companies Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Fence companies miss calls because the estimate rings while the crew is out setting posts, and a homeowner shopping three companies hires whoever answers, not whoever calls back.",
    "answer": "Fence companies miss calls because they ring while the whole crew is out setting posts, digging, and hanging panels, with no free hand and often no signal in a backyard. A homeowner who has decided to fence the yard is calling three or four companies and hires whoever answers first, so a call that rolls to voicemail is usually a job gone, not a message waiting.",
    "sections": [
        {"h2_html": "The call comes exactly when your crew <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Fencing is a hands-full trade. When the phone rings your crew is setting posts in concrete, digging post holes, hanging panels, or stretching chain-link, and none of those are moments anyone can stop and take a call. Backyards swallow cell signal, and the busier you are, the more estimate calls you miss, which means your best weeks in spring are also the ones where the most work slips away. It is not a discipline problem. A crew cannot build the fence in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a fence estimate it is not one. A homeowner who has decided this is the year is not going to leave a message and wait. They work down their list of three or four companies until someone answers, and by the time you check your phone at the end of the day, the measure is already booked with whoever picked up.</p>'},
        {"h2_html": "Fencing runs on responsiveness more than <em>almost any trade</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A fence is a want the homeowner is excited about, not an emergency they are stuck with, so the company that answers, sounds like a real outfit, and comes out to walk the yard soonest usually walks away with the job. That makes the missed call especially costly: a full yard of privacy fence or a run of ornamental aluminum is a real ticket, worth far more than the afternoon you spent unable to reach the phone. And the calls bunch up in spring, summer, and around new construction, exactly when every crew you have is already on an install, so the season that could earn the most is the one handing the most estimates to voicemail.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can actually handle a fence inquiry, not just take a message. A voicemail box cannot ask what they want built, and a generic call center does not know a privacy fence from a pool enclosure. What works is something that answers on the first ring, evenings and weekends included, asks what they want fenced and roughly how much yard, gets the address, and books the measure or flags a hot lead to your phone. It handles scheduling and intake only and never sets a price, you still walk the yard and quote it, but the job is captured instead of lost.</p>'}],
    "bridge_h2": "Stop losing estimates to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, evenings and weekends included, captures the fence details, and books the measure or flags it to you, so the estimate never rolls to voicemail while your crew is on the truck.",
    "bridge_slug": "ai-receptionist-for-fence-companies",
    "bridge_label": "AI receptionist for fence companies",
    "faqs": [
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are setting posts, in a backyard with no signal, or already walking another yard. Something that always answers and captures the fence details is what catches the calls a forward would still miss."),
        ("Would a homeowner rather reach a real person?",
         "What a homeowner shopping for a fence wants most is a quick, professional answer and a measure on the calendar, and a calm voice that captures the details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, books the measure, and hands hot leads straight to you.")],
    "trade_slug": "fence_companies", "trade_plural": "fence companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do My Fence Estimates Go Cold? (problem -> crm) ============
{
    "slug": "why-fence-estimates-go-cold",
    "h1": "Why Do My Fence Estimates Go Cold?",
    "title": "Why Do My Fence Estimates Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most fence estimates go cold not over price but because nobody followed up while the homeowner compared bids and waited on the HOA. The job goes to whoever checked back in.",
    "answer": "Most fence estimates go cold not because your price was wrong, but because nobody followed up. A fence is rarely a same-day decision, so the homeowner is gathering other bids, talking it over with a spouse, and waiting on the HOA, and the job goes to whoever stayed in touch. A quote that goes quiet is usually a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "Silence usually means still deciding, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet fence quote as a no on price, so you drop it and move on. But most of the time the homeowner did not decide against you at all. They asked for a number on a privacy run or a new gate, meant to think it over, and then life and the process got in the way. They are juggling two other quotes, a spouse who wants a say, and an HOA that has to approve the style before anything can happen, and a fence simply is not a same-day buy. Weeks later they could not tell you apart from the other companies who came out.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The one who gets the job is usually not the cheapest. It is the one who stayed in front of them: a friendly check-in a few days later, a short note that lands right as the HOA approval comes through. That second touch is what turns a maybe into a booked measure, and it is exactly the thing there is no time for in the middle of the season.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Fence companies do not skip follow-up because they are lazy. They skip it because the season fills the day. You walk a yard, send a quote, and then the installs you already have booked pull the whole crew onto the tools, and by evening the quote you sent Tuesday is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest quotes to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which quotes are still open and going cold.</li><li>The follow-up depends on you remembering, so it competes with the install schedule and loses.</li><li>By the time you circle back, the homeowner has already booked whoever kept in touch while the HOA was deciding.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open quote gets a couple of timed check-ins automatically, written to sound like you, the homeowner comparing bids keeps hearing from you while the others go silent, and the work you already quoted stops slipping away over the deciding weeks.</p>'}],
    "bridge_h2": "Follow up on every quote, automatically",
    "bridge_text": "A CRM keeps every open fence quote in front of you and sends timed check-ins for you, so a homeowner comparing bids and waiting on the HOA keeps hearing from you while the other companies go quiet.",
    "bridge_slug": "crm-for-fence-companies",
    "bridge_label": "CRM for fence companies",
    "faqs": [
        ("How many times should I follow up on a fence quote?",
         "A couple of light touches over the first few weeks catches most of the maybes without being pushy: a check-in a few days after the quote, then a short note while the HOA approval is still pending. Because a fence decision stretches over weeks, the timing matters, and that is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly check-in reads as attentive, not spammy, and most homeowners appreciate the nudge because they meant to get back to you and got busy. You can always jump in and message anyone directly.")],
    "trade_slug": "fence_companies", "trade_plural": "fence companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Do Fence Companies Get More Customers? (problem -> marketing) ========
{
    "slug": "how-do-fence-companies-get-more-customers",
    "h1": "How Do Fence Companies Get More Customers?",
    "title": "How Do Fence Companies Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Fence companies get more customers by showing up on Google when homeowners search fence company near me, collecting reviews, and turning every visible fence into a neighbor referral.",
    "answer": "Fence companies get more customers by being easy to find and easy to trust the moment a homeowner decides to fence the yard. That means showing up in the Google map pack for fence company near me, having recent reviews that make you the obvious call, and turning the fence itself, the most visible work you do, into a steady stream of neighbor referrals.",
    "sections": [
        {"h2_html": "Most fence customers start on <em>Google</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a homeowner decides to fence the yard, for a new puppy, for privacy from a neighbor, to meet code before a pool goes in, or on a fresh new-build lot, the first thing most of them do is search for a fence company in their town. Google answers that with the map pack, the little map with three local listings, star ratings, and a call button, and most people pick from those three without scrolling further. So if the phone is quiet even though you do good work, the usual reason is that you are not in those three at the moment homeowners are choosing who to call.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting there runs on your Google Business Profile: whether it is verified, complete, and active, how close you are to the searcher, and how many recent, genuine reviews you have. A steady flow of reviews from happy customers does double duty, it lifts you in the map pack and it makes you the obvious pick for the next homeowner comparing three companies. What no one can honestly promise is a specific spot on the map, because Google decides that, but those are the levers that move it.</p>'},
        {"h2_html": "The fence itself is your best <em>salesperson</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A fence is the most visible work you do. It sits on the property line where every neighbor and everyone who walks the street sees it, and a clean, straight run quietly asks who built it. People planning a fence almost always ask the neighbor who just got one, so a crew that leaves good work is the easiest recommendation a customer ever makes, and it costs you nothing but the ask.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Ask every happy customer for a review the moment the fence is done and they are standing there admiring it, and make it one tap, so the reviews that feed your ranking keep building.</li><li>Stay in touch with past yards so a repair, a gate, or an extension comes back to you instead of drifting to whoever turns up in search.</li><li>Build the referral partners a fence company lives on: the home builder who fences every new house, the pool company that needs a code-compliant enclosure on every install, and the property manager who calls for every rental.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting found on Google brings in the homeowner who does not know you yet. The reviews and the referral flywheel turn every fence you build into the next two. Together they are a steadier pipeline than any single ad, and they compound over a season instead of stopping the day you stop paying.</p>'}],
    "bridge_h2": "Get found, get reviewed, get referred",
    "bridge_text": "More fence customers come from showing up on Google when homeowners search, collecting reviews that make you the obvious call, and turning every visible fence into a neighbor referral. That is what fence marketing is built to do.",
    "bridge_slug": "marketing-for-fence-companies",
    "bridge_label": "Marketing for fence companies",
    "faqs": [
        ("Do I need a website to get more fence customers?",
         "Not to appear in the map pack, which runs on your Google Business Profile, so getting that verified, complete, and well-reviewed is the fastest start. A website helps you rank in the results below the map, show your fence styles, and give a browsing homeowner a place to request an estimate, so the two work best together."),
        ("What is the cheapest way to get more fence jobs?",
         "The work you have already done. A review from every happy customer lifts you in local search, and staying in touch with past yards and referral partners like builders, pool companies, and property managers brings back repairs, gates, and new referrals without paying per lead. Getting found on Google adds the homeowners who do not know you yet.")],
    "trade_slug": "fence_companies", "trade_plural": "fence companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
