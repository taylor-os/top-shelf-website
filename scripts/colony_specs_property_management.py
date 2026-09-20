"""Colony page specs for PROPERTY MANAGEMENT companies (plan §5 "Problem/symptom" colony +
§6 link-sculpting). generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS
from each. A colony page is ONE real question a property-management owner would search, answered
directly up top (the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that
funnels the page's authority into the ONE money page the question implies. Lighter than a money
page (the generator owns shell, schema, events, keyword placement).

Property management is NOT a single-agent realtor business and NOT the plumber template, so this
colony leads with the property-management reality instead of converging with either:
  - TWO audiences call the same phone at once. Property OWNERS (the B2B growth engine: signing
    more doors/units under management, each door recurring monthly revenue for years) and TENANTS
    (leasing inquiries, maintenance requests, rent questions), so the calls never stop.
  - The growth lever is winning OWNER accounts, not one-off transactions. Leasing speed fills
    vacancies; maintenance coordination keeps owners happy; owner acquisition compounds.
  - The website question leads with what a PM site must DO (an owners "what we manage / get a
    proposal" path AND a tenants "available rentals / apply / maintenance" path, credibility, and
    "property management company near me"), NOT a template-vs-custom-vs-agency price ladder.

Same honesty rules as the money specs: no invented stats, prices, or clients; hedge instead of
overpromise; only the real Top Shelf prices ($299/$899/$2,500 plans, $1,500 one-time site) ever
appear; NO invented management fees or percentages; no em/en dashes anywhere; never "leak" as a
money metaphor (a literal maintenance leak in a unit is fine); illustrative scenarios, no named
clients or competitors. Ethics: the AI does scheduling and intake ONLY, routing owner leads and
tenant requests, and never quotes a management fee.

Six questions, mixed cost / problem / how-to, spread across four Real Estate money pages:
  1 property-management-website-cost            (cost)    -> websites-seo-for-property-management
  2 property-management-answering-service-cost  (cost)    -> ai-receptionist-for-property-management
  3 is-a-crm-worth-it-for-property-management   (cost)    -> crm-for-property-management
  4 why-property-managers-miss-calls            (problem) -> ai-receptionist-for-property-management
  5 why-property-management-leads-go-cold       (problem) -> crm-for-property-management
  6 how-do-property-managers-get-more-doors     (how-to)  -> marketing-for-property-management
"""

TOPICS = [
# ============ How Much Does a Property Management Website Cost? (cost -> websites-seo) ============
{
    "slug": "property-management-website-cost",
    "h1": "How Much Does a Property Management Website Cost?",
    "title": "How Much Does a Property Management Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A property management website must win owners and serve tenants, not just look nice. Top Shelf builds a custom one for $1,500 one-time, or free on any monthly plan.",
    "answer": "A property management website can run from a few hundred dollars for a template to several thousand for a custom build. What matters more than the price is whether it wins owners handing over doors and serves tenants who want to apply, tour, or report a problem. Top Shelf builds yours for $1,500 one time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a property management website actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A property management website is not one website, it is two doorways sharing an address. An owner deciding who should manage their rental needs a clear path to what you manage and how to request a proposal, and they are handing over a major asset, so the site has to look like a real, established company before they will ever call. A tenant needs the opposite: available rentals they can browse, an application they can start, and an easy way to report a maintenance problem or ask a question about rent. A site that serves one audience and forgets the other quietly turns away half the people who land on it.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">On top of both, it has to be found. When an owner or a renter searches property management company near me, the site has to show up and load fast on a phone, because the company that is easy to find and easy to trust is the one that gets the call. That is the real job: an owners path that signals credibility and captures a proposal request, a tenants path that fills units and handles requests, and enough local visibility to be found the moment someone goes looking.</p>'},
        {"h2_html": "What is worth <em>paying for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A property management website earns its cost in two places: the owner accounts it helps you win and the units it helps you fill. Winning one owner is recurring revenue for years, and filling a vacancy a week faster is rent your owner actually collects, so a site that ranks locally, loads fast, and gives owners and tenants a clear next step pays for itself in a way a pretty brochure never will. A beautiful site that ranks for nothing and gives an owner nowhere to inquire is the most expensive kind, because you paid for it and it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that wins owners and fills units",
    "bridge_text": "A property management website is only worth what it brings in. Ours is built to rank for the towns you cover, give owners a clear path to a proposal and tenants a path to apply and report problems, then wired to follow up on every lead it captures.",
    "bridge_slug": "websites-seo-for-property-management",
    "bridge_label": "Websites & SEO for property management",
    "faqs": [
        ("Does a property management website really need tenant tools too?",
         "Yes. Owners are judging whether to trust you with their property, and tenants need to browse rentals, start an application, and report maintenance. A site that only speaks to one of them turns away the other. The strongest property management sites give each audience its own clear path from the first screen."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "property_management", "trade_plural": "property management companies",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ==== What Does a Property Management Answering Service Cost? (cost -> ai-receptionist) ====
{
    "slug": "property-management-answering-service-cost",
    "h1": "What Does a Property Management Answering Service Cost?",
    "title": "What Does a Property Management Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Property management answering services often bill per call or minute, which adds up fast. Top Shelf includes an AI receptionist that answers 24/7 at $899/mo.",
    "answer": "Traditional answering services for property managers bill per call, per minute, or a monthly retainer, so a portfolio of constant tenant and owner calls gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers around the clock, flat, in the Signature plan at $899 a month, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until you remember a property manager is fielding calls all day from two directions at once. Tenants call about a broken appliance, a lockout, a rent question, no hot water, and owners call to check on a property or shop for a new manager, and every one of those is a metered call. The more doors you manage, the more the meter runs, so growing your portfolio quietly grows your phone bill. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy portfolio or a wave of routine tenant questions runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty tenant or a slow operator costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when turnover season has your phones busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: the calls that matter most come when you are least able to take them. A prospect asking about a vacant unit tours somewhere else if you do not pick up, so the unit sits empty another month. An owner shopping for a manager on a Saturday signs with whoever answered, so years of recurring revenue go to the company down the street. A generic call center reading a script cannot tell a flooded unit from a slow drain, or a serious owner lead from a wrong number, so you can pay for coverage and still get bad triage.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, tells a leasing prospect from a tenant emergency from an owner lead, and books the showing, logs the maintenance request, or flags the owner lead straight to you. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. It handles scheduling and intake only, so it routes an owner lead to you but never quotes a management fee, because what you charge to manage a property is your conversation to have. One vacant unit filled a week sooner, or one owner account it saves on a weekend, can be worth well more than the plan costs.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers around the clock, tells a leasing prospect from a maintenance emergency from an owner lead, and books or routes each one, all on a flat monthly plan. It does the scheduling and intake, and hands the owner lead to you.",
    "bridge_slug": "ai-receptionist-for-property-management",
    "bridge_label": "AI receptionist for property management",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly as your portfolio grows and your phones get busier, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the vacancy it fills sooner and the owner lead it books instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or holidays?",
         "No. It answers around the clock as part of the plan, including the 2am maintenance emergency in a unit and the Saturday owner inquiry that are often the calls worth the most, with no after-hours surcharge or overage.")],
    "trade_slug": "property_management", "trade_plural": "property management companies",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ======== Is a CRM Worth It for a Property Management Company? (cost -> crm) ========
{
    "slug": "is-a-crm-worth-it-for-property-management",
    "h1": "Is a CRM Worth It for a Property Management Company?",
    "title": "Is a CRM Worth It for a Property Management Company? | Top Shelf Business Solutions",
    "meta_desc": "For most property managers a CRM pays for itself by winning back one owner lead and filling units faster. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most property management companies, yes. A CRM pays for itself the first time it wins back an owner lead you would have let go cold, since one signed owner is recurring revenue for years. It only stops being worth it if you already follow up with everyone. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a property management company when you have more owner leads, prospective tenants, and existing owners than you can personally keep track of, which is most companies past a handful of doors. It is not worth it if you manage a few units yourself and genuinely call every owner lead and prospect back, though that rarely stays true as you add doors. The honest test is simple: how many owner conversations have you had in the last few months that you never circled back on, how many prospects toured a unit and were never nudged to apply, and how many current owners have not heard from you since the last statement? Those are the doors and the units a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a property manager is not the software, it is the growth that stops slipping away. An owner who called to compare a couple of companies, a prospect who loved a unit but got busy, an existing owner quietly wondering what they pay you for: each one is revenue you have already half-earned and are one timely touch away from keeping.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every owner lead on a schedule, so an owner comparing managers keeps hearing from you while the other companies go quiet, and the doors come to you.</li><li>It works the leasing pipeline, nudging a prospect to finish an application or reminding them a unit is still available, so vacancies fill faster.</li><li>It keeps every owner, tenant, property, and conversation in one place instead of scattered across your inbox, your texts, and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is simple: win back one owner account you would have lost and it has paid for itself many times over, because that owner keeps paying every month you manage their doors, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your owner leads and pipeline to work",
    "bridge_text": "The owner leads you already talked to and the prospects who already toured are the cheapest doors you can win. A CRM follows up on every one for you, so the owner comparing managers signs with you and the prospect actually applies, instead of both going to the company that stayed in touch.",
    "bridge_slug": "crm-for-property-management",
    "bridge_label": "CRM for property management",
    "faqs": [
        ("Is a CRM overkill for a small property management company?",
         "Not usually. Even a company managing a few dozen doors juggles more owner leads, prospects, and existing owners than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If owner conversations go cold and prospects tour without applying, a CRM earns its keep quickly."),
        ("How is a CRM different from a spreadsheet or my inbox?",
         "A spreadsheet does not follow up, does not remember which owner is due for a check-in, and does not tell you which lead is going cold. A CRM does all of that on a schedule, so the owner accounts and filled units show up instead of depending on you to remember between fires.")],
    "trade_slug": "property_management", "trade_plural": "property management companies",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ============ Why Do Property Managers Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-property-managers-miss-calls",
    "h1": "Why Do Property Managers Miss So Many Calls?",
    "title": "Why Do Property Managers Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Property managers miss calls because the team is buried running doors while owners and tenants call the same phone at once. The calls worth the most roll to voicemail.",
    "answer": "You miss calls because your team is buried running the doors you already manage, turnovers, move-out inspections, walking a property with an owner, on the line with a tenant whose air conditioning quit, while owners and tenants both call the same phone that never stops. A prospect or owner who reaches voicemail just calls the next company.",
    "sections": [
        {"h2_html": "The calls come from two directions while your hands are <em>full</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Property management is really several businesses answering one phone. A prospect wants to see a vacant unit today, a current tenant has a problem in theirs, and an owner is shopping for someone to manage their property, and all three call the same number expecting a completely different thing. Meanwhile your team is out running a turnover, walking a unit on a move-out inspection with no signal, or already on the other line with a tenant whose water heater just quit. The busier your portfolio keeps you, the more calls stack up unanswered, which means your busiest stretches are also when the most opportunity slips away.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but it is not one. A renter scrolling listings is not going to leave a message and wait; they book a tour with whoever picks up. An owner comparing managers is not going to leave a voicemail either; they move down the list until a real, staffed company answers. By the time you check your phone between properties, the showing is booked elsewhere and the owner has already started building a relationship with someone else.</p>'},
        {"h2_html": "Your most expensive misses are the <em>calls worth the most</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A missed leasing call is a unit that sits empty another month, and that is rent your owner watches disappear while wondering why you have not filled it. A missed owner call is worse: winning a new owner is not a single payday, it is a management fee every month for as long as you keep the property, plus the leasing fee each time you fill a unit and the renewal fee each time a tenant stays. One owner with a few doors can be worth more over its life than dozens of ordinary calls, and that call is the one most likely to come on a Saturday when no one is at the desk.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can tell these calls apart. A voicemail box cannot triage, and a generic call center does not know a flooded unit from a slow drain, or a serious owner lead from a wrong number. What actually works is something that answers on the first ring day or night, gives a prospect the details and books the showing, treats a real maintenance emergency as urgent while logging the routine, and captures an owner lead and flags it straight to you, so the calls that grow the company never roll to voicemail in the first place.</p>'}],
    "bridge_h2": "Stop losing owners and vacancies to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, tells a leasing prospect from a tenant emergency from an owner lead, and books the showing, routes the maintenance request, or flags the owner lead to you, so the call that grows your portfolio never rolls to voicemail while your team is at a turnover.",
    "bridge_slug": "ai-receptionist-for-property-management",
    "bridge_label": "AI receptionist for property management",
    "faqs": [
        ("Would an owner or tenant rather reach a real person?",
         "What a caller needs most is to be handled, not parked in voicemail. A renter wants to know the unit is available and book a tour, and an owner wants to feel like they reached a real, staffed company. The AI receptionist is upfront about what it is, captures the details, and hands owner leads and true emergencies straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are at a turnover, walking a property, or already on another call, which is most of the day. Something that always answers and can triage is what catches the calls a forward would still miss.")],
    "trade_slug": "property_management", "trade_plural": "property management companies",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ============ Why Do My Property Management Leads Go Cold? (problem -> crm) ============
{
    "slug": "why-property-management-leads-go-cold",
    "h1": "Why Do My Property Management Leads Go Cold?",
    "title": "Why Do My Property Management Leads Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Property management leads go cold not over price but because nobody followed up. The owner compared managers and the door went to whoever stayed in touch.",
    "answer": "Most property management leads go cold not because your price was wrong, but because nobody followed up. The owner said they wanted to compare a couple of companies, the prospect who toured a unit got busy, and a turnover and a stack of month-end statements later, you never circled back. A lead that goes quiet is usually a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "Silence usually means forgotten, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet owner lead as a no on price, so you drop it and move on. But most of the time the owner did not decide against you at all. They called to ask what you charge and how you handle maintenance, had a good conversation, and meant to compare a couple of companies before deciding. Then a turnover, a pair of maintenance fires, and month-end statements buried the follow-up, and you never circled back. They sign with the company that stayed in front of them, which is rarely the cheapest and almost never the one that went quiet.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The leasing side goes cold the same way. A prospect who toured a unit and did not apply is not gone; they are deciding between yours and two others they saw the same day. An application that sits half-finished is not a rejection; it is someone who simply got busy. One friendly check-in a few days later is what turns that maybe into a signed lease, and it is exactly the thing there is no time for when you are running a portfolio all day.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Property managers do not skip follow-up because they are lazy. They skip it because the day fills up. You handle a turnover, take the emergency maintenance call that jumped the line, walk a property with an owner, close out month-end, and by evening the owner you spoke with on Tuesday is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest leads to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which owner leads are still open and going cold.</li><li>The follow-up depends on you remembering, so it competes with turnovers and maintenance fires and loses.</li><li>By the time you circle back, the owner signed with someone who stayed in touch and the prospect leased a unit down the street.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open owner lead gets a couple of timed check-ins automatically, written to sound like you, and every prospect gets a nudge to finish their application, the owner comparing companies keeps hearing from you while the others go silent, and the doors and filled units you already earned stop slipping away.</p>'}],
    "bridge_h2": "Follow up on every owner and prospect, automatically",
    "bridge_text": "A CRM keeps every owner lead and prospective tenant in front of you and sends timed check-ins for you, so the owner comparing managers keeps hearing from you while the other companies go quiet, and the prospect who toured actually applies. Your pipeline stops living in your head and your inbox.",
    "bridge_slug": "crm-for-property-management",
    "bridge_label": "CRM for property management",
    "faqs": [
        ("How many times should I follow up on an owner lead?",
         "A couple of light touches over the first week or two catches most of the maybes without being pushy: a check-in a few days after the first conversation, then a short, genuinely useful note after that. The key is that it happens at all and on time, which is what a CRM handles for you while you run the doors."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly check-in reads as attentive, not spammy, and most owners appreciate the nudge because they meant to get back to you and forgot. You can always jump in and message anyone directly.")],
    "trade_slug": "property_management", "trade_plural": "property management companies",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ============ How Do Property Managers Get More Doors? (how-to -> marketing) ============
{
    "slug": "how-do-property-managers-get-more-doors",
    "h1": "How Do Property Managers Get More Doors?",
    "title": "How Do Property Managers Get More Doors? | Top Shelf Business Solutions",
    "meta_desc": "Property managers get more doors by being the company owners find and trust when they search for a manager nearby. Each owner account is recurring revenue for years.",
    "answer": "Get more doors by becoming the property management company owners find and trust when they go looking, which usually starts with a search like property management company near me. Winning an owner account is recurring revenue for years, so showing up in the local results and looking credible when owners compare is what turns into signed doors.",
    "sections": [
        {"h2_html": "Every door you sign is revenue <em>for years</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more doors is really about winning more owner accounts, and an owner account is nothing like a one-time job. Every month a property is under your management it pays you, plus a leasing fee each time you fill a unit and a renewal fee each time a tenant stays, so one owner with a few doors can be worth more over its life than a pile of ordinary transactions. That is why owner acquisition, not any single campaign, is the growth engine of a property management company, and it is worth investing in the way you would invest in something that pays you back every month for years.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Owners find a manager two ways: a referral from someone they trust, and a search when they are fed up or have just bought a rental. When they search property management company near me, the map of local companies with star ratings shows up first, and most owners call from those without scrolling far. So if your phone is quiet even though you do good work, the reason is often that you are not showing up there, and almost no one is looking past the companies that are.</p>'},
        {"h2_html": "What actually wins <em>owner accounts</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An owner handing over a major asset checks you harder than a homeowner booking a repair, so being found is only half of it; you also have to look like a company worth trusting with a building. A handful of fixable things move both.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A Google Business Profile that is verified, complete, and active, with recent reviews from owners and tenants, so you look like an established company instead of an abandoned listing.</li><li>A consistent local presence, so your name is the one an owner already recognizes when they finally decide to switch managers.</li><li>Staying in front of the owner leads and landlords already in your orbit, because a referral and a familiar name close far more owner accounts than a cold ad.</li><li>A site and profile that make it obvious what you manage and how to ask for a proposal.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this is a trick, and none of it is instant. What no one can honestly promise is a specific spot on the map, because Google decides that, and there is no shortcut to the trust an owner needs before handing you their property. But a verified, active, well-reviewed presence compounds, and a free audit can show you exactly what an owner searching for a manager near you sees today.</p>'}],
    "bridge_h2": "Become the manager owners find first",
    "bridge_text": "Most new owner accounts start with a referral or a local search. Marketing for property management keeps your Google profile verified, active, and full of recent reviews, and keeps your name in front of the owners and landlords already in your orbit, so when someone nearby is finally fed up with their manager, yours is the company they call.",
    "bridge_slug": "marketing-for-property-management",
    "bridge_label": "Marketing for property management",
    "faqs": [
        ("What is the fastest way to get in front of owners searching for a manager?",
         "Your Google Business Profile. When an owner searches for a property management company near them, the local map results show first, and a verified, complete, well-reviewed profile is what gets you into them. It does not require a new website, just getting the profile right and keeping it active with real reviews."),
        ("How long until this brings in new doors?",
         "Owner trust builds over months, not days, which is why most companies give up before it pays off. A neglected profile that gets verified, completed, and active can start climbing within a few weeks and compounds as reviews build. No one controls Google, so no honest company promises a specific position, but consistency is what moves it.")],
    "trade_slug": "property_management", "trade_plural": "property management companies",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
]
