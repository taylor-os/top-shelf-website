"""Colony page specs for BANKRUPTCY ATTORNEYS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a bankruptcy-firm owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, bankruptcy-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear; no em/en dashes anywhere; never "leak" as a money metaphor.

Legal-ethics guardrails, strict for this trade: the pages never promise a debt will be discharged,
never promise a specific result, and never say a firm will wipe out anyone's debt. The AI
receptionist does intake and booking only; it never gives legal advice and never tells a caller
whether to file Chapter 7 or Chapter 13. Copy stays attorney-advertising compliant and meets a
caller in crisis with dignity, never shaming language. Every scenario is illustrative, never a
named client or a named competitor (debt-relief mills are described generically).

Six questions, mixed cost / problem / how-to, spread across the four legal money pages:
  1 bankruptcy-attorney-website-cost            (cost)    -> websites-seo-for-bankruptcy-attorneys
  2 bankruptcy-answering-service-cost           (cost)    -> ai-receptionist-for-bankruptcy-attorneys
  3 is-a-crm-worth-it-bankruptcy-law            (cost)    -> crm-for-bankruptcy-attorneys
  4 why-bankruptcy-firms-miss-calls             (problem) -> ai-receptionist-for-bankruptcy-attorneys
  5 why-bankruptcy-leads-go-cold                (problem) -> crm-for-bankruptcy-attorneys
  6 how-do-bankruptcy-attorneys-get-more-clients (how-to)  -> marketing-for-bankruptcy-attorneys
"""

TOPICS = [
# ============ How Much Does a Bankruptcy Attorney Website Cost? (cost -> websites-seo) ============
{
    "slug": "bankruptcy-attorney-website-cost",
    "h1": "How Much Does a Bankruptcy Attorney Website Cost?",
    "title": "How Much Does a Bankruptcy Attorney Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A bankruptcy attorney website ranges from cheap templates to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A bankruptcy attorney website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters most is whether it reaches someone quietly searching in a debt crisis and earns the free consultation. Top Shelf builds a custom five page site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number you see quoted for a bankruptcy attorney website swings wildly because you are not all buying the same thing. A cheap template you fill in yourself and a custom site built to rank in your area and earn consultations are different products with the same name. Before you compare quotes, it helps to know what you are actually paying for.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A do-it-yourself website builder is cheap monthly, but you do the work, and it is rarely built to rank or to reassure someone anxious enough to be searching quietly for help.</li><li>A one-time custom build costs more up front and is yours to keep, but a site alone does little if nobody is doing the ongoing SEO to get it found ahead of the debt-relief mills spending heavily on ads.</li><li>An agency retainer bundles the build with ongoing SEO and updates, which is where most of the long-term value lives, and also where the monthly cost lives.</li><li>Hidden costs to ask about before you sign: who owns the site, what a change costs, and whether you keep it if you leave.</li></ul>'},
        {"h2_html": "What a bankruptcy firm should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A bankruptcy attorney website earns its money one way: it turns someone quietly searching in a debt crisis into a booked free consultation. Most people look at your site late at night, on a break, or in private, half-expecting to be judged, long before they work up the nerve to call. That means it has to load fast, rank for the towns you serve and the questions people actually type, whether they would file Chapter 7 or Chapter 13, whether filing can stop a garnishment or a foreclosure, and meet a frightened visitor with calm, plain, judgment-free language and an easy way to book. A polished site that never ranks, or that reads cold and clinical to someone ashamed to be there, is the most expensive kind, because you paid for it and it brings you nothing while the debt-relief mills collect the calls.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that earns consultations",
    "bridge_text": "A bankruptcy firm website is only worth what it brings in. Ours is built to rank for the towns you serve, meet a frightened searcher with dignity, and turn a quiet late-night visit into a booked free consultation.",
    "bridge_slug": "websites-seo-for-bankruptcy-attorneys",
    "bridge_label": "Websites & SEO for bankruptcy attorneys",
    "faqs": [
        ("Is a cheap template site good enough to start with?",
         "It can get you online, but a template you fill in yourself is rarely built to rank or to reassure someone anxious enough to be searching quietly for a bankruptcy attorney, and you do the work of maintaining it. If a site is not getting found or turning private visits into booked consultations, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "bankruptcy_attorneys", "trade_plural": "bankruptcy attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ========= What Does a Bankruptcy Answering Service Cost? (cost -> ai-receptionist) =========
{
    "slug": "bankruptcy-answering-service-cost",
    "h1": "What Does a Bankruptcy Answering Service Cost?",
    "title": "What Does a Bankruptcy Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for bankruptcy firms often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 with dignity in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for bankruptcy firms usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call 24/7 with dignity, runs the intake, and books the free consultation comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. A bankruptcy firm also gets its calls at the hardest hours to staff live: nights, early mornings, weekends, and the quiet moments after work when someone can finally call without a spouse or coworker overhearing. Those after-hours minutes tend to cost the most. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of wrong numbers and debt-relief tire-kickers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a frightened caller who needs a minute to get the words out costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: someone ashamed and frightened about their debts does not leave a voicemail, they hang up and call the next firm, or a debt-relief mill that promises the world. The real cost of no coverage is not a monthly fee, it is the Chapter 7 or Chapter 13 matter that went to whoever picked up. But a generic call center reading a script cannot reassure a person in that state, cannot tell a true deadline from a caller still working up the courage to explain, and cannot capture the facts a bankruptcy file actually starts with.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, meets the caller with calm and dignity, runs the intake you design, and flags a true deadline, wages already being garnished, a foreclosure sale date, a repossession, a lawsuit, straight to your on-call attorney. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One consultation you would have lost on a weekend can be worth well more than the plan costs. And it stays in its lane: it never gives legal advice, never tells a caller whether to file Chapter 7 or Chapter 13, and never promises that any debt will be discharged, because those judgments belong to your attorneys alone.</p>'}],
    "bridge_h2": "Answer every anxious call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7 with dignity, runs the debt and means-test intake, and books the free consultation, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-bankruptcy-attorneys",
    "bridge_label": "AI receptionist for bankruptcy attorneys",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the after-hours consultation it books instead of losing to voicemail or a debt-relief mill."),
        ("Will it give the caller legal advice or promise their debt will be wiped out?",
         "No, and this matters. It answers, reassures, and captures the facts; it never advises on the case, never tells a caller whether to file Chapter 7 or Chapter 13, and never promises that any debt will be discharged. Every legal question and every decision about taking a matter stays with your attorneys.")],
    "trade_slug": "bankruptcy_attorneys", "trade_plural": "bankruptcy attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============== Is a CRM Worth It for a Bankruptcy Law Firm? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-bankruptcy-law",
    "h1": "Is a CRM Worth It for a Bankruptcy Law Firm?",
    "title": "Is a CRM Worth It for a Bankruptcy Law Firm? | Top Shelf Business Solutions",
    "meta_desc": "For most bankruptcy firms a CRM pays for itself by reviving one consultation that stalled out of shame and keeping signed clients moving through the paperwork. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most bankruptcy firms, yes. A CRM pays for itself the first time it revives a free consultation that stalled because fear and shame stopped someone from moving, or keeps a signed client on track through the means test and document gathering. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a bankruptcy firm when you have more free consultations, stalled files, and past clients than you can personally keep track of, which is most established practices. It is not worth it if you are a solo attorney handling a handful of matters and genuinely calling everyone back, though that rarely stays true as you grow. The honest test is simple: how many people sat down for a free consultation in the last month, agreed that filing made sense, and then went quiet without a single follow-up? How many signed clients are stuck halfway through gathering documents right now, one dreaded task away from stalling out? And how many past clients and referral sources have not heard a word from you in a year? Those are the matters a CRM is built to recover, and for most firms there are more of them than the day allows anyone to chase by hand.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a bankruptcy firm is not the software, it is the work that stops slipping through. Someone who froze after the free consultation because bankruptcy feels like failure, a signed client dreading the pile of pay stubs and statements, a past client who quietly refers the next person: each one is a matter you have already half-earned and are one respectful reminder away.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every consultation that has not turned into a filing, gently and on a schedule, so a person stalled by fear keeps hearing that you are ready whenever they are.</li><li>It nudges signed clients for the specific documents still missing and checks in ahead of a hearing or the meeting of creditors, so the file keeps moving instead of stalling in intake.</li><li>It keeps a light, respectful touch on past clients and the professionals who refer you, so that quiet network stays warm.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one matter you would have lost and it has paid for itself, and everything after that is margin. It organizes the follow-up and never promises a client anything about how their debts will be resolved; that stays with your attorneys.</p>'}],
    "bridge_h2": "Put your consultations and clients to work",
    "bridge_text": "The consultations you have already given and the clients you have already signed are the cheapest matters you can win. A CRM follows up on every one with care, so the person who froze files with you instead of letting it slide.",
    "bridge_slug": "crm-for-bankruptcy-attorneys",
    "bridge_label": "CRM for bankruptcy attorneys",
    "faqs": [
        ("Is a CRM overkill for a small bankruptcy practice?",
         "Not usually. Even a solo or two-attorney firm gives more free consultations and signs more clients than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If consultations go cold and signed clients stall in the paperwork, a CRM earns its keep."),
        ("How is a CRM different from keeping notes in my case software?",
         "Your bankruptcy case and petition software prepares the schedules, the means test, and the filing itself. A CRM runs everything around it: the consultations you have not signed, the clients stuck gathering documents, and the past clients and professionals who refer you. The two do different jobs.")],
    "trade_slug": "bankruptcy_attorneys", "trade_plural": "bankruptcy attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Why Do Bankruptcy Firms Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-bankruptcy-firms-miss-calls",
    "h1": "Why Do Bankruptcy Firms Miss So Many Calls?",
    "title": "Why Do Bankruptcy Firms Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Bankruptcy firms miss calls because they ring during court and after hours, and an ashamed caller in crisis will not leave a voicemail about their debts, they call the next firm.",
    "answer": "Bankruptcy firms miss calls because they come when an attorney cannot pick up, in court, at a hearing, with a client, and because the caller often phones quietly after hours. Someone ashamed of their debts will not leave a voicemail about them. They hang up and call the next firm or a debt-relief mill. The fix is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A bankruptcy practice is a hands-full practice. When the phone rings you are often in court, sitting through a meeting of creditors, in a consultation with someone across the desk, or driving between the two, and none of those are moments you can stop and take a call. The busier your calendar, the more calls you miss, which means your best stretches are also the ones where the most work slips away. It is not a discipline problem. One attorney cannot be in a hearing and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a bankruptcy caller it is not one. Many people call quietly, after work or once the house is asleep, already braced to be judged for letting things get this far. Asked to leave a message about their debts on a machine, most will not. The shame wins, they hang up, and by the time you check your phone the person has already moved down the list to whoever answered.</p>'},
        {"h2_html": "Missed calls are whole <em>retainers walking away</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal, and for a bankruptcy firm a missed call is rarely small. It is a full Chapter 7 or Chapter 13 matter, and it tends to come at exactly the private hours when other firms are closed too and someone finally has the nerve to reach out. Those are also the calls a debt-relief mill is standing by to answer around the clock, promising more than it can deliver. So the calls you are most likely to miss are the ones worth the most and the ones most at risk of going to the wrong place.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can meet a frightened caller with dignity. A voicemail box cannot reassure anyone, and a generic call center does not know a true deadline from a caller still gathering courage. What actually works is something that answers on the first ring day or night, stays calm and judgment-free, finds out whether a garnishment, a sale date, or a lawsuit is already running, and either books the consultation or flags a true emergency to your on-call attorney. It runs intake and booking only; it never gives legal advice, never tells a caller which chapter to file, and never promises that any debt will be discharged.</p>'}],
    "bridge_h2": "Stop losing retainers to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, meets an anxious caller with dignity, runs the intake, and books it or flags a real deadline to you, so the matter never rolls to voicemail or a debt-relief mill.",
    "bridge_slug": "ai-receptionist-for-bankruptcy-attorneys",
    "bridge_label": "AI receptionist for bankruptcy attorneys",
    "faqs": [
        ("Would a caller rather reach a real person?",
         "In a debt crisis, what a frightened caller needs most is to feel a real firm is handling it without judgment, and a calm voice that captures the details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, and hands true deadlines straight to your attorney."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are in court, at a hearing, or already with a client. Something that always answers, reassures, and runs the intake is what catches the calls a forward would still miss.")],
    "trade_slug": "bankruptcy_attorneys", "trade_plural": "bankruptcy attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Why Do My Bankruptcy Leads Go Cold? (problem -> crm) ============
{
    "slug": "why-bankruptcy-leads-go-cold",
    "h1": "Why Do My Bankruptcy Leads Go Cold?",
    "title": "Why Do My Bankruptcy Leads Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most bankruptcy leads go quiet not over price but because fear and shame stop people from moving. A creditor offers a payment plan, the paperwork feels impossible, and nobody followed up.",
    "answer": "Most bankruptcy leads go cold not because your fee was wrong, but because fear and shame stop people from moving, and nobody followed up. They had the free consultation, agreed filing made sense, then a creditor offered a payment plan or the paperwork felt impossible, and they froze. A lead that goes quiet is usually not a no, it is a maybe that never got a gentle second touch.",
    "sections": [
        {"h2_html": "Silence usually means frozen, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet lead as a no on your fee, so you drop it and move on. But most of the time the person did not decide against you at all. They sat down for the free consultation, understood that filing could give them a fresh start, and meant to go ahead. Then they left, and the fear came back. Bankruptcy can feel like an admission of failure, so the moment passes and the shame settles in. A creditor calls and promises to work something out. The stack of documents feels impossible to face. So they go quiet, and the matter that could have helped them sits untouched while the garnishment keeps taking.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The firm that gets the matter is usually not the cheapest. It is the one that stayed kindly in touch: a warm, no-pressure check-in a couple of weeks later that reminds the person you are ready whenever they are. That second touch is what turns a frozen maybe into a filing, and it is exactly the thing there is no time for between hearings and clients.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Attorneys do not skip follow-up because they are lazy. They skip it because the day fills up. You finish a hearing, meet the next client, handle the filing due Friday, and by evening the consultation from last week is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest matters to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which consultations are still open and quietly going cold.</li><li>The follow-up depends on you remembering, so it competes with the actual legal work and loses.</li><li>By the time you circle back, the person has given up, taken a creditor payment plan, or filed with whoever stayed in touch.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open consultation gets a few timed, gentle check-ins automatically, written to sound like your firm and never to shame anyone, the person who froze keeps hearing from you at the right moment, and the matters you already earned stop slipping away.</p>'}],
    "bridge_h2": "Follow up on every consultation, with care",
    "bridge_text": "A CRM keeps every stalled consultation in front of you and sends gentle, timed check-ins for you, so a person frozen by fear keeps hearing that you are ready, and files with your firm instead of letting it slide.",
    "bridge_slug": "crm-for-bankruptcy-attorneys",
    "bridge_label": "CRM for bankruptcy attorneys",
    "faqs": [
        ("How many times should I follow up on a bankruptcy consultation?",
         "A few light, respectful touches over the first several weeks catches most of the frozen maybes without any pressure: a warm check-in a couple of weeks after the consultation, then a short note later that you are ready whenever they are. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal or pushy?",
         "Not when it is written to sound like your firm, sent at a gentle pace, and never shames anyone. A short, kind check-in reads as care, not a sales chase, and most people appreciate knowing a firm is ready without judgment. You can always step in and reach anyone yourself.")],
    "trade_slug": "bankruptcy_attorneys", "trade_plural": "bankruptcy attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ======== How Do Bankruptcy Attorneys Get More Clients? (how-to -> marketing) ========
{
    "slug": "how-do-bankruptcy-attorneys-get-more-clients",
    "h1": "How Do Bankruptcy Attorneys Get More Clients?",
    "title": "How Do Bankruptcy Attorneys Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "Bankruptcy attorneys get more clients by being easy to find at the private moment someone searches, reassuring them with dignity, and making the free consultation simple to book.",
    "answer": "Bankruptcy attorneys get more clients by being easy to find at the quiet, private moment someone in debt crisis finally searches, by meeting them with reassurance instead of shame, and by making the free consultation simple to book. Most firms do good work but are hard to find and easy to overlook next to debt-relief mills. Getting seen and trusted is what steadily grows the caseload.",
    "sections": [
        {"h2_html": "People search for you <em>privately, in a hard moment</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most people do not go looking for a bankruptcy attorney until something forces their hand: a garnished paycheck, a foreclosure notice, a lawsuit in the mailbox. When they finally search, they do it quietly, often late at night and half-expecting to be judged. The first thing Google shows them is not a website at all. It is the map pack, the little map with three local firms, star ratings, and a call button, and most people choose from those three without scrolling further. So if your phone is quiet even though you do good work, the reason is usually that you are not in front of them at that moment, and the debt-relief mills paying for ads are.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting seen there is a different job from having a website. It runs on your Google Business Profile, whether it is verified, complete, and active, how close you are to the searcher, and how many genuine reviews you have, alongside a site that answers the questions people actually type. A great practice that is hard to find is a quiet phone, no matter how good the work is.</p>'},
        {"h2_html": "Get found, and get <em>trusted</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more clients is less about one clever trick and more about being findable and trustworthy at that private moment, consistently. Most of what moves it is fixable, and none of it requires overpromising.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Get your Google Business Profile verified, complete, and active, with the right service area, hours, and categories, so you show up in the map pack where the search starts.</li><li>Answer the questions people actually type, whether they would file Chapter 7 or Chapter 13, what the means test is, whether filing can stop a garnishment or a foreclosure, so you rank and reassure at the same time, without ever giving legal advice online.</li><li>Build a steady flow of genuine reviews by asking honestly, knowing many bankruptcy clients value their privacy and will not post, so you never fabricate, filter, or pay for reviews.</li><li>Lead with dignity and the free consultation, so a frightened person feels safe reaching out to you instead of a debt-relief mill.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Do these consistently and a neglected presence can climb over a few weeks, then compound. What no honest company can promise is a specific ranking or a set number of new clients, because no one controls Google, and attorney-advertising rules rightly forbid promising anyone a result. You compete with the mills on being found, trusted, and kind, not on hype. A free audit can show you where your presence stands today first.</p>'}],
    "bridge_h2": "Get found where people quietly search",
    "bridge_text": "Most bankruptcy clients begin with a private search in a hard moment. Getting your Google presence verified, active, and full of genuine reviews, and answering the questions people ask, is how you show up and earn the free consultation.",
    "bridge_slug": "marketing-for-bankruptcy-attorneys",
    "bridge_label": "Marketing for bankruptcy attorneys",
    "faqs": [
        ("Do I need a big ad budget to compete with debt-relief companies?",
         "Not to win the local search. The map pack runs on your Google Business Profile, not on ad spend, so a verified, active, well-reviewed profile and a site that answers real questions can put you in front of people at the moment they search, without outspending the mills. Ads can help, but they are not the only way in."),
        ("How long until I see more bankruptcy clients?",
         "A neglected Google presence that gets verified, completed, and active can start climbing within a few weeks, and it compounds as reviews and content build. Nobody controls Google, so no honest company promises a specific position or a set number of clients, but consistency is what moves it.")],
    "trade_slug": "bankruptcy_attorneys", "trade_plural": "bankruptcy attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
]
