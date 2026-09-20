"""Per-page content specs for the SEO corpus (plan §5), property management batch. Same
contract as scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics
(shell, schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below
owns the UNIQUE, hand-written, property-management-specific substance that clears the uniqueness
gate. Never templated find-and-replace, never the plumber content reworded.

Real Estate hub. Four service angles are here in one file (the ai-receptionist dict carries
"demo": True). A property management company answers one phone for three different callers,
a prospective tenant who wants to lease a vacant unit, a current tenant with a maintenance
problem, and an owner shopping for a manager, so the copy leans on those three call types, on
owner acquisition as the growth engine (a new owner is recurring management fees for years),
and on the trust an owner needs before handing over an investment. Each example body ends with
the literal "Illustrative example, not a client." per the honesty rule; if the generator also
appends that line, dedupe there.
"""

SPECS = [
# ==================== AI Receptionist for Property Management ====================
{
    "slug": "ai-receptionist-for-property-management", "demo": True,
    "trade_slug": "property_management", "trade_plural": "property management companies",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "breadcrumb_leaf": "AI Receptionist for Property Management",
    "title": "AI Receptionist for Property Management | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Property Management",
    "meta_desc": "A property management answering service answers every leasing, maintenance, and owner call, triages after-hours emergencies, and books showings for you.",
    "service_schema_name": "AI Receptionist for Property Management",
    "eyebrow": "For Property Management",
    "h1_html": "AI Receptionist <em>for Property Management</em>",
    "answer_block": "A property management answering service answers every call the moment it rings, a prospect asking about a vacant unit, a tenant with an emergency, or an owner shopping for a manager, triages it, and books the showing or routes the crisis while your team is buried in turnovers. Every call, and the number it rings on, belongs to you.",
    "sections": [
        {"h2_html": "The leasing call you miss is a unit that <em>stays empty another month</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A prospective tenant scrolling listings on their phone calls three companies about a vacant unit, and they want to see it today, not next week. If yours rolls to voicemail, they tour a unit down the street that same afternoon and sign the lease there, and your owner\'s unit sits empty another month while the rent it should have earned never comes back. Leasing runs on that kind of speed, because a good renter looking this week has usually signed somewhere by next week, and every day a unit sits vacant is money the owner is watching disappear. But your team is out running a move-out inspection with no signal, walking a property with an owner, or already on the other line with a tenant whose air conditioning just quit, so the call that would have filled the unit quietly goes to whoever happened to pick up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An AI receptionist answers on the first ring, tells the prospect exactly what is available and where, answers the obvious questions about rent, deposit, lease length, and pet policy, and books the showing straight onto your calendar or your leasing agent\'s. The unit gets seen while interest is hot, instead of after the prospect has already toured and signed somewhere else, and your owner sees you filling their vacancy fast.</p>'},
        {"h2_html": "Built around the <em>three calls you actually field</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Property management is really three businesses answering one phone. A prospect wants to lease a vacant unit, a current tenant has a problem in theirs, and an owner is shopping for someone to manage their property, and all three call the same number expecting a completely different thing. A voicemail box cannot tell them apart, and a generic call center reading a script does not know a flooded unit from a slow drain, or a serious owner lead from a wrong number.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A prospect asking about a vacancy gets current availability, rent, and pet policy, and a showing booked on your calendar instead of a voicemail they will never leave.</li><li>A tenant reporting a problem is triaged the way your office would: an active water leak or no heat is treated as urgent, while a dripping faucet or a squeaky door is logged as routine.</li><li>An owner shopping for a manager, the call that actually grows the company, never hits voicemail; their details and their portfolio are captured and flagged to you at once.</li><li>It answers around the clock, so the 2am emergency in a unit and the Saturday owner inquiry are both handled while every other office is closed.</li></ul>'},
        {"h2_html": "The call that <em>grows your portfolio</em> cannot go to voicemail",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Winning a new owner is the growth engine of a property management company, and it is nothing like landing a one-time job. A new owner is not a single payday; it is a management fee every month for as long as you keep the property, often years, plus the leasing fee each time you fill a unit and the renewal fee each time a tenant stays. One signed owner with a few doors can be worth more over its life than dozens of ordinary transactions. An owner who just inherited a rental, or who is finally fed up with a manager who stopped returning calls, is usually phoning two or three companies in a single afternoon to compare, and they are judging each one by how it handles that very first call. The company that answers like a real, staffed business, instead of a voicemail box, earns the first meeting, and the first meeting is most of the battle.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Miss that call and you have not lost a service ticket. You have handed years of recurring revenue to the company down the street that happened to pick up the phone while you were busy running the doors you already manage.</p>'},
        {"h2_html": "You own the number, the calls, and the <em>owner list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing business number, or a new one registered in your name, not ours. Every caller, every unit, and every owner lead is yours and exportable any time, so the pipeline you build becomes an asset you keep instead of something you rent back month to month. There is no long contract holding your data hostage, and if you ever leave, the number and the history come with you. The AI receptionist is one piece of the Top Shelf platform, and it hands every call it captures to the same CRM that follows up automatically, so a warm owner lead, a prospect who asked for a showing, or a maintenance request logged after hours never slips through the cracks between one busy day and the next.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A Saturday owner call, captured while your team is <em>at a turnover</em>",
        "body_html": 'It is a Saturday and an owner with four rentals has quietly had enough of their current manager, so they start calling around while your crew is across town finishing a turnover. The first company they try goes to voicemail. Yours answers, learns they have four doors and what has been going wrong, captures their name, number, and portfolio, and books a call with you for Monday morning while flagging it as a new-owner lead. You walk in Monday to a warm prospect worth years of management fees already on your calendar, instead of finding out later that the owner signed with someone who simply answered faster. Illustrative example, not a client.'},
    "faqs": [
        ("Does it work with my current phone number?",
         "Yes. It can answer on your existing business number, or set up a new one registered in your name. Either way the number, and every leasing, maintenance, and owner call that comes through it, belongs to you and goes with you if you ever leave."),
        ("Can it handle leasing, maintenance, and owner calls differently?",
         "Yes, that is the whole point. It knows a prospect asking about a vacancy from a tenant reporting a problem from an owner shopping for a manager, and it responds to each the way your office would, booking the showing, triaging the repair, or capturing the owner lead and flagging it to you."),
        ("Can it tell a real maintenance emergency from a routine request?",
         "Yes. It asks the questions you would, is there an active water leak, is there heat, is anyone unsafe, and treats a true emergency as urgent while logging a dripping faucet or a squeaky door as routine. You set exactly what counts as a drop-everything call."),
        ("Will it actually book showings on my calendar?",
         "Yes. Showings and routine appointments land straight on your calendar based on the availability you set, and you get a text with the details right away. For an urgent maintenance call it can alert you at once so you decide how fast to respond."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your triage questions, your calendar, and your rules for leasing, maintenance, and owner calls, so it is answering in days, not weeks. Start with a free audit and we will show you what your current setup is missing.")],
    "related": [
        ("industry-real-estate.html", "Everything Top Shelf does for property management companies"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-property-management.html", "The CRM that nurtures every owner and tenant lead"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing owners and vacancies to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many leasing, maintenance, and owner calls your current setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ==================== CRM for Property Management ====================
{
    "slug": "crm-for-property-management",
    "trade_slug": "property_management", "trade_plural": "property management companies",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "breadcrumb_leaf": "CRM for Property Management",
    "title": "CRM for Property Management | Top Shelf Business Solutions",
    "og_title": "CRM for Property Management",
    "meta_desc": "A CRM for property management nurtures every owner lead and keeps your tenant and leasing pipeline moving, so new doors sign and units fill faster.",
    "service_schema_name": "CRM for Property Management",
    "eyebrow": "For Property Management",
    "h1_html": "CRM <em>for Property Management</em>",
    "answer_block": "A CRM for property management keeps every owner lead, prospective tenant, and current resident in one place and follows up for you, so the owner comparing managers signs with you and the prospect who toured a unit last week actually applies. Your pipeline stops living in your head and your inbox.",
    "sections": [
        {"h2_html": "The owner leads you already talked to are the doors you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most property managers do not have a lead problem. They have a follow-up problem. An owner calls to ask what you charge and how you handle maintenance, you have a good conversation, they say they want to think it over or compare a couple of companies, and then a turnover, a pair of maintenance fires, and a stack of month-end statements later, you never circle back. They sign with the company that followed up, which is rarely the cheapest and almost never the one that went quiet. That owner was never really lost. They just needed one more call or a short note a few days later, and that is exactly the thing there is no time for when you are running a portfolio and putting out fires all day.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every owner lead in front of you and follows up on a schedule you set, with messages that go out on time whether or not you remember. The owner weighing two or three companies keeps hearing from you while the others disappear, and the doors come to you.</p>'},
        {"h2_html": "Every owner you sign is revenue <em>for years</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A signed owner is the cheapest, most durable revenue a management company has. You went through the work of earning their trust once, and now every month that property is under management it pays you, and the next property they buy, and the referral they send another landlord, is yours too if you stay in front of them. But you cannot personally remember to nurture every owner lead and check in with every existing owner, so a lot of that growth quietly stalls in an inbox you meant to get back to.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every owner, property, unit, and conversation lives in one place, instead of scattered across your inbox, your texts, and your memory.</li><li>Owner leads get nurtured automatically until they decide, so a strong conversation in March is not forgotten by May when the owner is finally ready.</li><li>Renewal, inspection, and check-in reminders fire on schedule, so nothing about a property you already manage falls through.</li><li>You can see which owner has not heard from you in a while and reach out before they start quietly wondering what they are paying you for.</li></ul>'},
        {"h2_html": "The leasing pipeline that <em>fills units faster</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The tenant side has its own pipeline, and it slips away just as easily. A prospect who toured a unit and did not apply is not gone; they are deciding between yours and two others they saw the same day. An application that sits half-finished is not a rejection; it is someone who simply got busy. A quick, automatic follow-up, a note that the unit is still available, a friendly nudge to finish the application, keeps your vacancy moving while the other listings go silent. A vacant unit is lost rent every single day it sits, and the difference between filling it this week and filling it next month is often nothing more than staying in touch with the people who already walked through the door.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The CRM tracks each prospect through the leasing funnel, from first inquiry to booked showing to submitted application to signed lease, so you can see at a glance where every renter stalled and give them the one nudge that moves them forward. No interested renter is forgotten, and no unit sits open a day longer than it has to, which is exactly what your owners are quietly watching you for.</p>'},
        {"h2_html": "You <em>own the list</em>, and it works with the rest of the system",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every owner, every tenant, and every note is yours and exportable any time, not locked inside software you rent by the month. The CRM is one piece of the Top Shelf platform and connects to the AI receptionist, so an owner call or a leasing inquiry it answers lands in your database and starts getting followed up on automatically, and to online booking, so a scheduled showing or inspection is logged against the right property with its full history attached. It also means one clean record per owner and per unit, no duplicate contacts and no conflicting notes, so anyone on your team can pick up a conversation exactly where the last person left it. Nothing you have worked to earn, an owner who was close to signing or a prospect who loved the unit, goes cold because you got pulled onto something else. The owners and prospects you already earned stay warm on their own, so your pipeline compounds instead of resetting every time the week gets busy.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The four-door owner who <em>signs in April</em>",
        "body_html": 'An owner with four rentals calls in February to ask what you charge and how you handle maintenance and monthly statements. It is a good call, but they want to compare a couple of companies first, and normally that is the last you ever hear from them. Instead, the CRM sends a friendly check-in a few days later and a short, genuinely useful note the week after, both written to sound like you and not a form letter. The other companies never followed up, so when the owner is finally ready in April, yours is the only name still in front of them. They hand you all four doors without shopping any further, and you never once sat down to chase it. Illustrative example, not a client.'},
    "faqs": [
        ("Does it import my existing owners, tenants, and properties?",
         "Yes. Your current owners, tenants, leads, and property records come in and live in one place, and everything stays yours and exportable. The point is to make the pipeline and the portfolio you already have actually work for you instead of sitting in an inbox."),
        ("Will it really follow up on owner leads automatically?",
         "Yes, on the schedule you approve. An owner who asked about your services gets a check-in a few days later and another after that, all sent for you, so an owner comparing companies keeps hearing from you while the others go quiet. You can jump in and message anyone directly any time."),
        ("Can it manage the leasing pipeline too?",
         "Yes. It tracks each prospect from first inquiry through showing and application, and can nudge someone to finish an application or remind them a unit is still available, so vacancies fill faster and no interested renter is forgotten."),
        ("How is this different from a spreadsheet or my inbox?",
         "A spreadsheet does not follow up, does not remember which owner is due for a check-in, and does not tell you which lead is going cold. The CRM does all of that on a schedule, so the owner accounts and filled units actually show up instead of depending on you to remember between fires."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your owners, tenants, and properties, build your follow-up and reminder sequences, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will show you where leads are slipping through today.")],
    "related": [
        ("industry-real-estate.html", "Everything Top Shelf does for property management companies"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-property-management.html", "The AI receptionist that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting owner leads and prospects <em>go cold</em>",
    "cta_sub": "Get a free audit of how many of your owner leads and prospective tenants are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ==================== Marketing for Property Management ====================
{
    "slug": "marketing-for-property-management",
    "trade_slug": "property_management", "trade_plural": "property management companies",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "breadcrumb_leaf": "Marketing for Property Management",
    "title": "Marketing for Property Management | Top Shelf Business Solutions",
    "og_title": "Marketing for Property Management",
    "meta_desc": "Property management marketing keeps you visible to owners searching for a manager and tenants hunting a rental, so new doors and units both find you first.",
    "service_schema_name": "Marketing for Property Management",
    "eyebrow": "For Property Management",
    "h1_html": "Marketing <em>for Property Management</em>",
    "answer_block": "Property management marketing keeps you visible where your two audiences actually look, owners searching for a company to trust with their investment and tenants hunting for a rental, so when either one searches near you, your name is the active, well-reviewed one they call instead of the company that let its profile go stale.",
    "sections": [
        {"h2_html": "You are marketing to <em>two audiences at once</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most local businesses chase one kind of customer. A property manager has two, and they could not be more different. Owners are shopping for someone to trust with a serious investment, sometimes their largest one, and they research carefully and slowly before they hand over the keys. Prospective tenants are scrolling listings and want a unit they can walk through this week. Both start on a phone, both search locally, and being easy to find and easy to trust at the exact moment each one looks is the whole game. The owner search is the valuable one, because a single owner turns into years of management fees, but a steady flow of tenant demand is what fills the vacancies fast and keeps those owners happy enough to stay with you.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Marketing for a property manager is not about clever ads shown to people with no rental and no property. It is about being visible and credible in your area the moment an owner needs a manager or a renter needs a home, because that is when the decision actually gets made. Get found and trusted in that narrow window, and you win both the door and the tenant to fill it.</p>'},
        {"h2_html": "Your Google Business Profile is the <em>storefront owners judge you by</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When an owner searches for a property management company near them, the map pack, those three local listings with the star ratings, is the first thing they see, above the websites and above the ads. An owner about to trust you with a property worth far more than any single service call is going to study that listing hard, and one that sits untouched with a handful of old reviews looks like a risk next to one that is active, complete, and stacked with recent reviews from both owners and tenants. Current photos of properties you manage, accurate service areas, up-to-date contact details, and a steady flow of reviews turn your profile into a quiet, always-on advertisement running in the exact spot where an owner decides who is worth a call.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The same listing works on the tenant side too. A prospect searching for a rental in your area sees the same profile, the same rating, and the same photos, and decides in a glance whether your company looks like one worth renting from. A single well-kept profile quietly does double duty, pulling owners and tenants from the one place both of them look first.</p>'},
        {"h2_html": "Reviews from owners and tenants <em>decide who an owner trusts</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An owner handing over a property is really asking one quiet question: will these people protect my investment and not create headaches I will have to clean up. Reviews answer that faster and more believably than anything you can say about yourself. Reviews from other owners show that you communicate, send clear statements, and pay on time. Reviews from tenants show that you handle maintenance quickly and treat people fairly, which any experienced owner knows is exactly what keeps good tenants in place and rent flowing. A steady stream of both, kept fresh instead of frozen two years in the past, is often the difference between an owner picking up the phone and an owner scrolling right past you to the next listing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is the public, reputation-facing side of the business. The private follow-up to the owner leads and prospects already in your pipeline is the CRM, and the two work best together, one bringing new owners and renters to your door and the other making sure the ones who show interest actually sign.</p>'},
        {"h2_html": "Show up in the <em>neighborhoods you actually manage</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Marketing to a whole metro is expensive, forgettable, and mostly wasted for a property manager. It brings you owner calls for houses an hour outside your range and tenant inquiries for units you do not have in neighborhoods you do not serve. Focusing on the specific cities and neighborhoods where you actually manage doors, with a profile, photos, and content built around those areas, is what puts you in front of the owners and tenants you can genuinely take on. It is a tighter, cheaper, and far more honest target than a citywide spend, and it is the one that turns into signed owners and filled units instead of calls you have to turn away. As you add doors in a new area, the same focused approach extends to that market, so your visibility grows exactly where your business actually grows, not everywhere at once.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "An owner two suburbs over <em>finds you first</em>",
        "body_html": 'An owner with a single rental two suburbs over gets tired of chasing repairs and late rent on their own and searches for a property management company near them. Because your Google profile has been kept active all year, with recent reviews from both owners and tenants, current service areas, and real photos of properties like theirs, you sit at the top of the map pack for that area. The owner reads a tenant\'s review praising how fast a maintenance request got handled and an owner\'s review about clear, on-time monthly statements, and they call you before the two companies listed below you. The company that let its profile go quiet a year ago never even gets considered, and never knows the call happened. Illustrative example, not a client.'},
    "faqs": [
        ("Do you post to my Google Business Profile for me?",
         "Yes. We keep it active with photos, updates, and reviews from both owners and tenants on a regular schedule, and keep your service areas, services, and contact details accurate, so it looks current whenever an owner or a renter searches near them."),
        ("How do you market to owners and tenants at the same time?",
         "The same local presence works for both. Owner-focused content and reviews build the trust an owner needs before handing over a property, while your visibility in the areas you cover pulls in the renters who fill your vacancies. One well-kept profile does double duty."),
        ("How is this different from the CRM follow-up?",
         "The CRM follows up privately with owners and prospects already in your pipeline. Marketing is the public-facing side, your Google profile, reviews, and local visibility, aimed at owners and tenants who are not yours yet but need to find and trust you the moment they start looking."),
        ("What does focusing on my service area actually mean?",
         "It means building your profile and content around the specific cities and neighborhoods where you actually manage doors, instead of spreading a budget across a whole metro. That is what puts you in the map pack where the owner and tenant searches you can actually serve are happening."),
        ("How long before I see it working?",
         "A neglected profile can climb in the map pack within weeks once it is active and complete, and it compounds from there as reviews and content build. Setup is included, and a free audit will show you what your current presence looks like to an owner searching near you today.")],
    "related": [
        ("industry-real-estate.html", "Everything Top Shelf does for property management companies"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-property-management.html", "The website that captures the owners this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the manager owners <em>can already see</em>",
    "cta_sub": "Get a free audit of how visible you actually are to owners and tenants searching near you right now, whether you work with us or not. No credit card, never a call center.",
},
# ==================== Websites & SEO for Property Management ====================
{
    "slug": "websites-seo-for-property-management",
    "trade_slug": "property_management", "trade_plural": "property management companies",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "breadcrumb_leaf": "Websites & SEO for Property Management",
    "title": "Websites & SEO for Property Management | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Property Management",
    "meta_desc": "A property management website built for SEO ranks when an owner searches in your city, and captures that lead directly instead of a listing portal.",
    "service_schema_name": "Websites & SEO for Property Management",
    "eyebrow": "For Property Management",
    "h1_html": "Websites &amp; SEO <em>for Property Management</em>",
    "answer_block": "A property management website built for SEO ranks for what an owner types when they need a manager, property management company near me and your city's name, shows up in the map pack for the areas you cover, and captures that owner lead the moment they land, so a years-long account belongs to you, not a listing portal.",
    "sections": [
        {"h2_html": "The listing portals are <em>renting owners back to you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for a property manager in your city and the top of the page is often a national listing portal or a directory, not the local company that actually knows the market. Those sites publish thousands of pages and have years of authority behind them, so when an owner searches for a manager, they land there first, fill out a form, and that lead gets sold, sometimes to several companies at once, sometimes back to you for a fee out of your own margin. Your site not ranking is not a vanity problem. It is the reason a serious owner account, the kind worth years of management fees, gets handed to whoever pays the portal the most that month or happens to be next on the rotation.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The portals are not really competing with you on service. They are renting you back the owners who were already searching in your own city, and every dollar you send them buys a lead you never truly own, often shared with two or three of your direct competitors the moment it comes in.</p>'},
        {"h2_html": "Rank for what an owner types when they <em>need a manager</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national portal this year for the broadest term, and you do not need to. You can rank for your own company name, for the specific cities and neighborhoods where you manage doors, and for the exact searches an owner makes when they are ready to hand off a property: property management company near me, rental management in your city, HOA management, or someone to manage my rental. You can also rank for the questions owners ask before they ever call, how much property managers charge, what a manager actually does, and whether it is worth it, which is exactly where a careful owner begins. Pages built around the areas you truly serve and the services you truly offer are what search engines, and cautious owners, reward with the click, because they answer the real question instead of casting a wide, generic net.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The same pages pull tenant searches too, the renters looking for available units in the areas you cover, so one site built around your real market works both sides of your business at once, filling vacancies for the owners you have while pulling in the next owner who needs a manager.</p>'},
        {"h2_html": "Your site is what an owner <em>judges before trusting you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An owner is about to hand a stranger control of a property worth far more than any single transaction, so they research harder than any tenant ever will, and your website is where that research quietly lands. A professional, fast, clear site that explains how you handle maintenance, tenant screening, rent collection, monthly owner statements, and day-to-day communication, and that shows real reviews from both owners and tenants, is what turns a nervous searcher into a phone call. A thin, dated, or slow site does the opposite; it quietly tells a careful owner to keep looking, no matter how good you actually are once the work starts. Most of these visits happen on a phone, so the site has to load fast, make it obvious how to reach a real person, and answer the questions an owner is silently asking before they will trust you with the keys, what you charge, how you protect their property, and how quickly you respond when something goes wrong.</p>'},
        {"h2_html": "The owner accounts are <em>yours, permanently</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you put into a pay-per-lead portal disappears the day you stop paying, and the lead was never really yours to begin with. A website you own keeps ranking, keeps capturing owner and tenant leads, and keeps compounding in value for as long as it exists, and it is registered to you, not a platform that can drop you tomorrow or quietly sell you next to the company down the street. Over a few years, a site that steadily brings in even a handful of owner accounts pays for itself many times over, because each of those owners is recurring revenue rather than a one-time fee. That is the opposite of a lead you rented, which vanished the moment you stopped paying for it. The site plugs into the same CRM that nurtures every owner lead it captures and the AI receptionist that answers the calls it drives, so a serious owner who found you at midnight is followed up on instead of forgotten. Nothing the site earns you slips away in the gap between the first click and the signed management agreement.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A new landlord finds <em>you</em>, not a portal",
        "body_html": 'Someone inherits a house across town, decides they have no interest in being a landlord themselves, and searches for a property management company in that area on their phone. Instead of a national portal that would sell their information to three companies at once, they find your site ranking for that city, with a page that explains in plain language exactly how you handle maintenance, screening, and monthly owner statements, plus real reviews from current owners saying you did what you promised. They read enough to trust you, tap to call, and you answer on the first ring. The account is yours, worth years of management fees, and no portal ever touched it, sold it, or charged you a cent for the lead. Illustrative example, not a client.'},
    "faqs": [
        ("Will my site actually outrank the big portals?",
         "Not for the broadest terms overnight. It can realistically rank for your company name, your specific cities and neighborhoods, and the owner-intent searches a national portal has no reason to target well, which is exactly where a local property manager can win."),
        ("How is this different from paying a portal for leads?",
         "A pay-per-lead portal rents you a lead it also sells to your competitors, and it stops the day you stop paying. A website you own captures owner and tenant leads that are yours alone and keeps working long after it is built, without a per-lead fee coming out of every account."),
        ("Do I need to rank for every city I manage in?",
         "You rank for the ones that matter most first. We build pages for your core markets and the highest-intent owner searches, then expand, rather than spreading thin across a whole metro at once."),
        ("Owners research carefully. Does a website really matter that much?",
         "Especially then. An owner about to trust you with a property researches harder than any tenant, and your site is where that research lands. A clear, professional site that answers their questions and shows real reviews is often what turns a cautious searcher into a call."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks; broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-real-estate.html", "Everything Top Shelf does for property management companies"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-property-management.html", "Staying visible to owners and tenants beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results in <em>your own market</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the portals taking your owner leads, whether you work with us or not. No credit card, never a call center.",
},
]
