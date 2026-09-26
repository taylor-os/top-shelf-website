"""Colony page specs for FAMILY LAW ATTORNEYS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a family law firm owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, family-law-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear; no em/en dashes anywhere; never "leak" as a metaphor.

Legal-ethics rules this trade adds on top: never promise an outcome, a custody result, or how any
matter will resolve; the AI receptionist runs intake and booking only, never legal advice; keep it
attorney-advertising compliant; and stay sensitive about divorce and children, never exploitative.

Six questions, mixed cost / problem / how-to, funneling into four money pages:
  1 family-law-attorney-website-cost            (cost)    -> websites-seo-for-family-law-attorneys
  2 family-law-answering-service-cost           (cost)    -> ai-receptionist-for-family-law-attorneys
  3 is-a-crm-worth-it-family-law                (cost)    -> crm-for-family-law-attorneys
  4 why-family-law-firms-miss-calls             (problem) -> ai-receptionist-for-family-law-attorneys
  5 why-family-law-consultations-go-cold        (problem) -> crm-for-family-law-attorneys
  6 how-do-family-law-attorneys-get-more-clients (how-to) -> marketing-for-family-law-attorneys
"""

TOPICS = [
# ============ How Much Does a Family Law Attorney Website Cost? (cost -> websites-seo) ============
{
    "slug": "family-law-attorney-website-cost",
    "h1": "How Much Does a Family Law Attorney Website Cost?",
    "title": "How Much Does a Family Law Attorney Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A family law attorney website ranges from a cheap template to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A family law attorney website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more than the price is whether it earns the trust of someone quietly researching a divorce and turns that visit into a consultation. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number you see quoted for a family law website swings wildly because you are not all buying the same thing. A cheap template you fill in yourself and a custom site built to rank in your area and reassure an anxious visitor are different products with the same name. Before you compare quotes, it helps to know what you are actually paying for.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A do-it-yourself website builder is cheap monthly, but you do the work, and it is rarely built to rank or to earn the trust of someone quietly researching a divorce or a custody change.</li><li>A one-time custom build costs more up front and is yours to keep, but a site alone does little if nobody is doing the ongoing SEO to get it found.</li><li>An agency retainer bundles the build with ongoing SEO and updates, which is where most of the long-term value lives, and also where the monthly cost lives.</li><li>Hidden costs to ask about before you sign: who owns the site, what a change costs, and whether you keep it if you leave.</li></ul>'},
        {"h2_html": "What a family law firm should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A family law website earns its money one way: it turns a person quietly researching a divorce or a custody change into a booked consultation. That means it has to load fast, rank for the searches people make in your area when a family is coming apart, and feel discreet and human enough that a frightened visitor trusts you enough to reach out. A beautiful site that never ranks and reads cold is the most expensive kind, because you paid for it and it brings you nothing. The point is not how the site looks to you, it is whether it reaches the person searching at midnight and gives them a reason to call in the morning.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest firm can promise is a specific ranking by a specific date, because no one controls Google, or anything about how a matter will resolve, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that earns the consultation",
    "bridge_text": "A family law website is only worth the consultations it brings in. Ours is built to rank for the divorce and custody searches in your area and give an anxious visitor a reason to trust you, then reach out.",
    "bridge_slug": "websites-seo-for-family-law-attorneys",
    "bridge_label": "Websites & SEO for family law attorneys",
    "faqs": [
        ("Is a cheap template site good enough for a family law firm?",
         "It can get you online, but a template you fill in yourself is rarely built to rank or to reassure someone in the middle of an emotional decision, and you do the work of maintaining it. If a site is not getting found or turning a private visit into a consultation, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep. On a monthly plan the site is built for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "family_law_attorneys", "trade_plural": "family law attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ========= What Does a Family Law Answering Service Cost? (cost -> ai-receptionist) =========
{
    "slug": "family-law-answering-service-cost",
    "h1": "What Does a Family Law Answering Service Cost?",
    "title": "What Does a Family Law Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for family law firms often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for family law firms usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call 24/7, runs the intake, and books the consultation comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. A family law firm also gets its calls at the hardest hours for a live service: after the kids are asleep, from a parked car, on a weekend when someone has finally decided they cannot wait, when after-hours minutes tend to cost the most. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of early inquiries runs up the cost.</li><li>Per-minute pricing: you pay for talk time, and a family law caller who is upset and needs a patient ear is exactly the kind of call that costs you more.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a person who spent weeks working up the nerve to call a divorce attorney does not leave a voicemail, they call the next firm on the list until someone answers warmly. The real cost of no coverage is not a monthly fee, it is the client you would have retained who went to whoever picked up. But a generic call center reading a script cannot meet a caller who is in tears, and cannot tell a safety emergency from someone who is only beginning to think about their options, so you can pay for coverage and still get cold, wrong triage.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, stays calm and unhurried with an emotional caller, runs the intake you design, and books the consultation or flags a true emergency, a safety fear, a child kept against an order, papers just served with a fast deadline, to your on-call attorney. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One matter you would have lost to a voicemail on a weekend is usually worth far more than the plan costs, and everything it catches after that is on top. It never gives legal advice and never predicts how a case will go; those calls stay with your attorneys.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7 with a calm, private voice, runs the intake, and books the consultation, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-family-law-attorneys",
    "bridge_label": "AI receptionist for family law attorneys",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the after-hours consultation it books, with a caller who might otherwise have hung up, instead of losing it to voicemail."),
        ("Does it cost extra for nights, weekends, or holidays?",
         "No. It answers 24/7 as part of the plan, including the late call from a parent who can only talk once the house is asleep and the weekend call from someone who has finally decided, with no after-hours surcharge or overage.")],
    "trade_slug": "family_law_attorneys", "trade_plural": "family law attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============== Is a CRM Worth It for a Family Law Firm? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-family-law",
    "h1": "Is a CRM Worth It for a Family Law Firm?",
    "title": "Is a CRM Worth It for a Family Law Firm? | Top Shelf Business Solutions",
    "meta_desc": "For most family law firms a CRM pays for itself by reviving one consultation that got cold feet. It comes in Top Shelf's Signature plan at $899/mo, not a separate bill.",
    "answer": "For most family law firms, yes. A CRM pays for itself the first time it wins back a consultation someone canceled while deciding whether to file, or keeps an anxious client from drifting away mid-case. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a family law firm when you have more consultations, unsigned prospects, and past clients than you can personally keep track of, which is most established practices. It is not worth it if you are a solo attorney handling a handful of matters and genuinely staying in touch with everyone yourself, though that rarely stays true as you grow. The honest test is simple: how many consultations canceled or no-showed in the last month that you never followed up on, and how many past clients have not heard from you in a year? Those are the matters a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a family law firm is not the software, it is the work that stops slipping through. A person who booked a consultation and then lost their nerve, a signed client going quiet during a long, frightening case, a past client whose coworker now needs the same help: each one is a relationship you have already half-earned and are one careful touch away from keeping.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every consultation that never converted, on a schedule you set, with gentle, no-pressure check-ins, so someone who is still deciding keeps hearing that you are there.</li><li>It keeps signed clients steady, sending reminders before each hearing or mediation and a steadying word through the long quiet stretches, so a scared client hears from you before they start to spiral.</li><li>It keeps a light, respectful touch on past clients and referral sources, the therapists, financial advisors, and past clients who send families your way when it is their turn.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: keep one matter you would have lost and it has paid for itself, and everything after that is margin. It carries the relationship while your attorneys carry the case, and it never promises a client anything about how their matter will end.</p>'}],
    "bridge_h2": "Put your consultations and clients to work",
    "bridge_text": "The consultations you have already booked and the clients you have already helped are the least expensive matters you can win. A CRM follows up on every one with care, so they choose you when they are ready.",
    "bridge_slug": "crm-for-family-law-attorneys",
    "bridge_label": "CRM for family law attorneys",
    "faqs": [
        ("Is a CRM overkill for a small family law firm?",
         "Not usually. Even a solo or two-attorney firm takes more consultations and helps more families than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If consultations go cold and past clients forget your name, a CRM earns its keep."),
        ("How is a CRM different from my case-management software?",
         "It sits alongside it and does a different job. Your case-management software runs the legal file, the pleadings, and the filing deadlines. The CRM runs everything around it: the consultations you have not signed, the clients who need reassurance through a long case, and the past clients and professionals who refer you.")],
    "trade_slug": "family_law_attorneys", "trade_plural": "family law attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Why Do Family Law Firms Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-family-law-firms-miss-calls",
    "h1": "Why Do Family Law Firms Miss So Many Calls?",
    "title": "Why Do Family Law Firms Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Family law firms miss calls because they ring during hearings and mediations, and a caller who finally worked up the nerve will not leave a voicemail, they call the next firm.",
    "answer": "You miss calls because they come while you are in a hearing, in a mediation, or across the desk from another client, and a person who finally worked up the nerve to call a divorce attorney will not leave a voicemail. They call the next firm until someone answers. The fix is making sure every call is answered with care.",
    "sections": [
        {"h2_html": "The call comes exactly when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Family law is a courtroom-and-conference trade. When the phone rings you are often in a hearing with your phone off, in a mediation you cannot step out of, or across the desk from a client whose own life is coming apart, and none of those are moments you can stop and take a call. The busier your docket, the more calls you miss, which means your best weeks are also the ones where the most work slips away. It is not a discipline problem. One attorney cannot be present for the client in front of them and answer every new call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for this kind of first call it is not one. Someone who spent weeks deciding whether to even speak to a divorce lawyer, and who may be calling from the one room with a door that locks, is not going to leave a message and wait. The nerve it took drains away, or they simply move down the list until a real person answers gently, and by the time you check your phone the person is gone.</p>'},
        {"h2_html": "The calls you miss are the clients you would have <em>retained</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">In this practice the caller is not shopping on price. They are deciding who feels safe enough to trust with their family at the worst moment of it, and they very often retain the firm that answered warmly while they were most raw. So a missed call is not just a lost lead, it is the client who called three firms and stayed with the one that picked up. The calls most likely to roll to voicemail, the late ones, the weekend ones, are frequently the ones a person is most ready to act on.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps, meets an emotional caller with patience, and can tell a true emergency apart from a first inquiry. A voicemail box cannot reassure anyone, and a generic call center does not know that a child kept against an order is nothing like a general question about the process. What actually works is something that answers on the first ring day or night, stays calm and private, gathers what a matter starts with, and either books the consultation or flags a genuine emergency straight to your phone, so you decide how to respond without ever missing the call in the first place. It stays in its lane and never offers legal advice.</p>'}],
    "bridge_h2": "Stop losing your hardest callers to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, meets an emotional caller with a calm voice, runs the intake, and books the consultation or flags a true emergency to you.",
    "bridge_slug": "ai-receptionist-for-family-law-attorneys",
    "bridge_label": "AI receptionist for family law attorneys",
    "faqs": [
        ("Would a distressed caller rather reach a real person?",
         "In a painful moment what a caller needs most is to feel heard and to know a real firm is handling it, and a calm voice that captures the details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts gently, and hands true emergencies straight to your attorney."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail while you are in a hearing, in a mediation, or with another client. Something that always answers and triages is what catches the calls a forward would still miss.")],
    "trade_slug": "family_law_attorneys", "trade_plural": "family law attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Why Do My Family Law Consultations Go Cold? (problem -> crm) ============
{
    "slug": "why-family-law-consultations-go-cold",
    "h1": "Why Do My Family Law Consultations Go Cold?",
    "title": "Why Do My Family Law Consultations Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most family law consultations go cold not over your fee but ambivalence: the person got cold feet about filing, and the matter went to the firm that gently stayed in touch.",
    "answer": "Most family law consultations go cold not because your fee was wrong, but because the person got cold feet about ending a marriage or changing custody. They canceled, no-showed, or went quiet while still deciding. A consultation that goes silent is usually not a no, it is a maybe that never got a gentle second touch.",
    "sections": [
        {"h2_html": "Silence usually means ambivalent, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet consultation as a no on your fee, so you drop it and move on. But most of the time the person did not decide against you at all. They booked while still deciding whether to go through with anything, and then the fear settled in, or a spouse promised to change, or the thought of what it would do to the children stopped them cold. They were not a bad lead. They were an ambivalent one, and ambivalence is the normal state of a person standing at the edge of ending a marriage or a custody arrangement.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The firm they eventually retain is usually not the cheapest. It is the one that stayed gently in touch: a patient, no-pressure check-in a couple of weeks later that says you are there when they are ready. That second touch is what turns a maybe into a signed client, and it is exactly the thing there is no time for between hearings.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Family law attorneys do not skip follow-up because they do not care. They skip it because the day fills up. You finish a hearing, roll into a mediation, handle the client crisis that jumped the line, and by evening the consultation that canceled Tuesday morning is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest consultations to revive.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which consultations never converted and are quietly going cold.</li><li>The follow-up depends on you remembering, so it competes with a full docket and loses.</li><li>By the time you circle back, the person has either moved on or buried the whole decision for another year.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every consultation that did not convert gets a couple of gentle, timed check-ins automatically, written to sound like your firm and never to pressure, the person who got cold feet keeps hearing that you are there, and the matter you already met with stops slipping away.</p>'}],
    "bridge_h2": "Follow up on every consultation, with care",
    "bridge_text": "A CRM keeps every consultation that never converted in front of you and sends gentle, no-pressure check-ins for you, so the person who got cold feet returns to you instead of drifting to another firm.",
    "bridge_slug": "crm-for-family-law-attorneys",
    "bridge_label": "CRM for family law attorneys",
    "faqs": [
        ("How many times should I follow up on a family law consultation?",
         "A couple of light, respectful touches over the following weeks catches most of the ambivalent ones without pressure: a check-in a couple of weeks after the consultation, then a short note later. The key is that it happens at all and gently, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like your firm and sent at a sensitive pace. A short, caring check-in reads as attentive, not pushy, and someone weighing a decision this hard often appreciates knowing you are still there. You can always step in and reach anyone yourself.")],
    "trade_slug": "family_law_attorneys", "trade_plural": "family law attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ======== How Do Family Law Attorneys Get More Clients? (how-to -> marketing) ========
{
    "slug": "how-do-family-law-attorneys-get-more-clients",
    "h1": "How Do Family Law Attorneys Get More Clients?",
    "title": "How Do Family Law Attorneys Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "Family law attorneys get more clients by being easy to find the moment someone privately searches, and by handling reviews and referrals with care. No promised outcomes.",
    "answer": "Family law attorneys get more clients by being easy to find the moment someone privately searches for help, and by earning trust once found. That means an active Google presence, genuine reviews handled with care, and steady word-of-mouth from past clients and referral sources, not any promise about how a case will turn out.",
    "sections": [
        {"h2_html": "Most clients start with a private <em>search</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone deciding to talk to a divorce or custody lawyer usually searches quietly, late, from a phone, before telling a soul. When they search for a family law attorney near them, the first thing Google shows is not a website at all. It is the map pack, the little map with three local listings, star ratings, and a call button. Most people choose from those three without ever scrolling to the regular results below. So if the phone is quiet even though you have a website, the answer is usually that you are not in those three, and almost nobody is looking past them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting into the map pack is a different job from having a website. It runs on your Google Business Profile: whether it is verified, complete, and active, how close you are to the searcher, and how many recent, genuine reviews you have. A great website with a neglected profile is a nice brochure nobody sees at the moment a person is deciding, alone at midnight, who to call.</p>'},
        {"h2_html": "What actually moves it for a <em>family law firm</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting found is only half of it. A family law client is not comparing prices, they are choosing who feels safe to trust with the most private chapter of their life, so what you do once they find you matters as much as being on the map. A handful of fixable things move both.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Get the Google Business Profile verified, complete, and active, with the right service area, hours, and categories, so you appear the moment someone searches.</li><li>Build a steady flow of genuine reviews, asked for with care. Reviews are delicate in family law because clients are private about a divorce, so ask gently, let people share only what they are comfortable with, and never filter unhappy clients or pay for reviews.</li><li>Keep your name, address, and phone number consistent everywhere, so Google is sure you are one real firm.</li><li>Answer the frightened researcher\'s real questions on your site, so you are the firm that felt human before they ever called.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this happens overnight, and no one can honestly promise a specific spot on the map, because Google decides that, or anything about how a matter will resolve. What compounds it all is the quiet referral web this practice runs on: past clients who felt guided with patience, and the therapists and financial advisors who meet families at the breaking point, all pointing the next person to the firm they trust.</p>'}],
    "bridge_h2": "Be the firm they find, and trust",
    "bridge_text": "Most family law clients start with a quiet search and choose the firm that feels safe. Keeping your Google presence active and your reviews genuine is how you show up, and get chosen, when someone nearby needs help.",
    "bridge_slug": "marketing-for-family-law-attorneys",
    "bridge_label": "Marketing for family law attorneys",
    "faqs": [
        ("Do I need a website to show up on Google Maps?",
         "Not to appear in the map pack, which runs on your Google Business Profile. A website helps you rank in the results below the map and gives the profile something to link to, but the fastest way onto the map itself is a verified, active, well-reviewed profile."),
        ("Is it okay to ask family law clients for reviews?",
         "Asking every client for an honest review is allowed and encouraged, but be sensitive: clients are private about a divorce, so ask gently, let them share only what they are comfortable with, and reply to reviews with care. What is not allowed is filtering out unhappy clients, offering incentives, or paying for reviews.")],
    "trade_slug": "family_law_attorneys", "trade_plural": "family law attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
]
