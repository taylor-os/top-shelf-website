"""Colony page specs for IMMIGRATION LAWYERS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question an immigration-firm owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, immigration-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear; no em/en dashes anywhere; never "leak" as a metaphor.

Immigration is its own animal, and every page leads with that reality: callers who are more
comfortable in Spanish or another language and hang up on a voicemail they cannot follow; hard
government deadlines (a request for evidence, an expiring status, a detained relative, a removal
hearing) where a few days matter; document-heavy cases; whole families involved; long USCIS waits;
and a practice that lives on trust, reachability, and community referrals. A bilingual, after-hours
front desk is a genuine edge. LEGAL ETHICS run through all of it: nothing promises an outcome, an
approval, a visa, or a green card; the AI does intake and booking only, never legal advice; every
legal decision stays with the attorneys; and the copy stays attorney-advertising compliant.

Six questions, mixed cost / problem / how-to, spread across three money pages:
  1 immigration-lawyer-website-cost              (cost)    -> websites-seo-for-immigration-lawyers
  2 immigration-law-firm-answering-service-cost  (cost)    -> ai-receptionist-for-immigration-lawyers
  3 is-a-crm-worth-it-immigration-law            (cost)    -> crm-for-immigration-lawyers
  4 why-immigration-firms-miss-calls             (problem) -> ai-receptionist-for-immigration-lawyers
  5 why-immigration-consultations-go-cold        (problem) -> crm-for-immigration-lawyers
  6 how-do-immigration-lawyers-get-more-clients  (how-to)  -> marketing-for-immigration-lawyers
"""

TOPICS = [
# ============ How Much Does an Immigration Lawyer Website Cost? (cost -> websites-seo) ============
{
    "slug": "immigration-lawyer-website-cost",
    "h1": "How Much Does an Immigration Lawyer Website Cost?",
    "title": "How Much Does an Immigration Lawyer Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "An immigration lawyer website ranges from cheap templates to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "An immigration lawyer website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more than the price is whether it ranks and turns an anxious searcher into a booked consultation. Top Shelf builds a custom site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number you see quoted for an immigration lawyer website swings widely because you are not all buying the same thing. A cheap template you fill in yourself and a custom site built to rank for the searches an anxious person makes, often in more than one language, are different products with the same name. Before you compare quotes, it helps to know what you are actually paying for.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A do-it-yourself website builder is cheap by the month, but you do the work, and it is rarely built to rank or to turn a nervous visitor into a booked consultation.</li><li>A one-time custom build costs more up front and is yours to keep, but a site alone does little if nobody is handling the ongoing SEO that gets it found.</li><li>An agency retainer bundles the build with ongoing SEO and updates, which is where most of the long-term value lives, and also where the monthly cost lives.</li><li>Hidden costs to ask about before you sign: who owns the site, what a change costs, whether it is built to work in more than one language, and whether you keep it if you leave.</li></ul>'},
        {"h2_html": "What an immigration firm should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An immigration lawyer website earns its money one way: it turns a person searching in a hurry, and often in Spanish, into a booked consultation on your calendar. That means it has to load fast, rank for the towns and the searches people use when they need help with their status, speak to the visitor in the language they searched in, and put a clear way to call or book in front of them before they scroll. A handsome site that never ranks and buries your number and your booking link is the most expensive kind, because you paid for it and it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest firm can promise is a specific ranking by a specific date, because no one controls Google, and nothing on the site should ever promise a visa, a green card, or any legal outcome. A free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that books consultations",
    "bridge_text": "An immigration lawyer website is only worth what it brings in. Ours is built to rank for the towns you cover, speak to visitors in the language they searched in, and turn searches into booked consultations.",
    "bridge_slug": "websites-seo-for-immigration-lawyers",
    "bridge_label": "Websites & SEO for immigration lawyers",
    "faqs": [
        ("Does the website need to work in Spanish too?",
         "For most immigration firms, yes. A large share of the people searching for help are more comfortable in Spanish or another language, and a site that speaks to them in the language they searched in earns more consultations. We can build it to serve more than one language so no visitor bounces because they could not read it."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep. On a monthly plan the site is built for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "immigration_lawyers", "trade_plural": "immigration lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ==== What Does an Immigration Law Firm Answering Service Cost? (cost -> ai-receptionist) ====
{
    "slug": "immigration-law-firm-answering-service-cost",
    "h1": "What Does an Immigration Law Firm Answering Service Cost?",
    "title": "What Does an Immigration Law Firm Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for immigration firms often bill per call or minute, and few take intake in Spanish. Top Shelf includes a bilingual AI receptionist in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for immigration firms usually bill per call, per minute, or a monthly retainer, and few can take intake in Spanish or flag a filing deadline. Top Shelf takes a different approach: an AI receptionist that answers 24/7 in English or Spanish, books the consultation, and flags urgent cases, in the Signature plan at $899 a month flat.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy month turns into a big bill. An immigration firm also gets calls at the hardest times to cover: evenings after a long work shift, weekends, and the moment a notice from the government arrives in the mail. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of wrong numbers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a frightened caller who needs a moment to explain their situation costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands, and, on most services, no way to run the intake in a language other than English.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: the consultation is the front door to your whole practice, and a person who has finally decided to deal with their status does not leave a voicemail, they call the next firm on the page. The real cost of no coverage is not a monthly fee, it is the client who booked with whoever picked up. But a generic call center reading a script cannot run intake in Spanish, cannot tell a routine question from a relative in custody or a deadline that is closing, so you can pay for coverage and still lose the call.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, in English or Spanish, gathers what a case actually starts with, and books the consultation or flags a truly urgent matter to your on-call attorney. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One consultation you would have lost after hours can be worth well more than the plan costs. Just as important, it does intake and booking only: it never gives legal advice and never promises an approval, a visa, or a green card, and every legal decision stays with your attorneys.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads an English-only script, an AI receptionist answers 24/7 in English or Spanish, books the consultation, and flags an urgent deadline to your attorney, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-immigration-lawyers",
    "bridge_label": "AI receptionist for immigration lawyers",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the after-hours consultation it books, in the caller's language, instead of losing it to voicemail."),
        ("Does it really take intake in Spanish?",
         "Yes, and for immigration work that is a real edge. It can greet the caller and run the whole intake in the language they are comfortable in, so a Spanish-first caller is helped and understood instead of hanging up on a voicemail they cannot follow. It captures the facts and books the consultation; it never gives legal advice or promises a result.")],
    "trade_slug": "immigration_lawyers", "trade_plural": "immigration lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Is a CRM Worth It for an Immigration Law Firm? (cost -> crm) ============
{
    "slug": "is-a-crm-worth-it-immigration-law",
    "h1": "Is a CRM Worth It for an Immigration Law Firm?",
    "title": "Is a CRM Worth It for an Immigration Law Firm? | Top Shelf Business Solutions",
    "meta_desc": "For most immigration firms a CRM pays for itself by rescuing one cold consultation and keeping clients from drifting during long waits. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most immigration firms, yes. A CRM pays for itself the first time it wins back a consultation that went quiet, or keeps a client from drifting away during a long government wait. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for an immigration firm when you have more consultations and open cases than you can personally keep track of, which is most established practices. It is not worth it if you are a solo attorney handling a handful of matters and genuinely calling everyone back, though that rarely stays true as word spreads through a community. The honest test is simple: how many consultations have you given in the last month that never turned into a signed case because no one followed up, and how many clients waiting out a long case have not heard a word from you in months? Those are the people a CRM is built to keep. It does not replace your immigration case-management software, which holds the legal file and the filing deadlines. It works the human side around it: the consultations you have not signed, and the clients who need reassurance through the quiet stretches.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for an immigration firm is not the software, it is the work that stops slipping through. A person sitting on a consultation about a green card, a family still gathering documents, a client three months into a silent wait who is starting to fear the worst: each one is a case you have already half-earned and are one steady touch away from keeping.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open consultation on a schedule, in the language the person reads, so someone still gathering documents keeps hearing from you while other firms go quiet.</li><li>It sends reassuring check-ins through the long waits, so a client hears from you before they panic, flood your front desk, or drift away discouraged.</li><li>It keeps a reminder on each next step, a biometrics appointment, an interview, a renewal window, so the human side of hitting a date does not fall through.</li><li>It keeps a light, steady hand on past clients and the families who refer you, which for an immigration practice is the engine that brings the next several cases.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. Recover one client you would have lost and it has paid for itself. It runs the relationship; your attorneys run the cases and make every legal decision, and nothing here ever promises a client an outcome.</p>'}],
    "bridge_h2": "Put your consultation list to work",
    "bridge_text": "The consultations and past clients you already have are the cheapest cases you can get. A CRM follows up on every one for you, in the language they read, so they stay with your firm instead of the one that kept in touch.",
    "bridge_slug": "crm-for-immigration-lawyers",
    "bridge_label": "CRM for immigration lawyers",
    "faqs": [
        ("Is a CRM overkill for a small immigration firm?",
         "Not usually. Even a small practice gives more consultations and carries more long-running cases than anyone can track by memory, especially once a community starts referring you. The point is not size, it is whether follow-up is falling through. If consultations go cold and clients drift away during the wait, a CRM earns its keep."),
        ("How is this different from my immigration case-management software?",
         "It sits alongside it. That software runs the legal file, the forms, and the filing deadlines. The CRM runs everything around it: the consultations you have not signed, the clients who need reassurance through a long case, and the families and community who refer you. The two do different jobs.")],
    "trade_slug": "immigration_lawyers", "trade_plural": "immigration lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Why Do Immigration Firms Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-immigration-firms-miss-calls",
    "h1": "Why Do Immigration Firms Miss So Many Calls?",
    "title": "Why Do Immigration Firms Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Immigration firms miss calls because they ring during hearings and after hours, and an anxious caller who reaches an English-only voicemail does not wait, they call the next firm.",
    "answer": "Immigration firms miss calls because they come while you are in a hearing, with a client, or gone for the day, and an anxious person who has finally decided to call does not leave a voicemail. They call the next firm. Many callers are also more comfortable in Spanish, so an English-only front desk loses them too.",
    "sections": [
        {"h2_html": "The call comes when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone who has finally decided to deal with their immigration status, to start a green card, file for a spouse or a parent, or answer a notice from the government, has usually been thinking about it for a long time before they pick up the phone. When they call, they are anxious and ready to talk to a lawyer today. But you are in a hearing, meeting another client, driving between them, or gone for the evening, and none of those are moments you can stop and take a call. The busier your firm is, the more calls slip away.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a person in this state it is not one. Someone frightened about their status does not leave a message and wait. They move down the list until a real person answers and books them in, and by the time you check your phone, the consultation is already booked with another firm.</p>'},
        {"h2_html": "The language gap makes the misses <em>more expensive</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call costs the same. A large share of the people who call an immigration firm are more comfortable in Spanish or another language, and a caller who reaches a voicemail they cannot follow simply hangs up and finds a firm where someone speaks their language. That call was yours to lose. The consultation is the front door to your whole practice, so a missed call is rarely a small thing: it is the case that books with whoever answered.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Worse still are the calls that cannot wait. A relative picked up and held, a request for evidence with a window closing, a status about to lapse: these are hard deadlines where a few days matter, and they roll to voicemail over a weekend just like everything else. Closing the gap takes coverage that never sleeps, answers in the language the caller speaks, and can tell an urgent matter from a routine question. What works is something that answers on the first ring day or night, runs the intake in their own language, books the consultation, and flags a truly urgent case to your on-call attorney, so nothing time-sensitive sits unseen and nobody is lost because the front desk could not understand them.</p>'}],
    "bridge_h2": "Stop losing consultations to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, in English or Spanish, books the consultation, and flags an urgent deadline to your attorney, so the case never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-immigration-lawyers",
    "bridge_label": "AI receptionist for immigration lawyers",
    "faqs": [
        ("Would a nervous caller rather reach a real person?",
         "What an anxious caller needs most is to know a real firm is handling it, and a calm voice in their own language that captures the details beats a voicemail box every time. The AI receptionist is upfront about what it is, runs the intake, and hands truly urgent matters straight to your on-call attorney. It never gives legal advice or promises a result."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free and you speak the caller's language. Forwarding still rolls to voicemail when you are in a hearing or with a client, and it does nothing for a Spanish-first caller if no one is there to answer in Spanish. Something that always answers and runs bilingual intake is what catches the calls a forward would still miss.")],
    "trade_slug": "immigration_lawyers", "trade_plural": "immigration lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Why Do My Immigration Consultations Go Cold? (problem -> crm) ============
{
    "slug": "why-immigration-consultations-go-cold",
    "h1": "Why Do My Immigration Consultations Go Cold?",
    "title": "Why Do My Immigration Consultations Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most immigration consultations go cold not over price but because the real barriers to starting stall the client and nobody followed up. The case that felt urgent slips down their list.",
    "answer": "Most immigration consultations go cold not because the person decided against you, but because the real barriers to starting, scattered documents, the fee to gather, a family member to consult, stall them, and nobody followed up. The case that felt urgent in your office quietly slips down their list.",
    "sections": [
        {"h2_html": "Silence usually means stalled, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet consultation as a no, so you let it go and move on. But most of the time the person did not decide against you at all. They sat down about a green card or a family petition, left ready to move forward, and then ran into the real reasons immigration cases stall: the documents are scattered across two countries, the fee is a lot of money to gather, a spouse or a parent needs to be talked to first. Weeks pass, life crowds in, and the case that felt urgent in your office slides down the list.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The firm that gets the case is usually not the cheapest. It is the one that stayed in front of them while they were still working up the nerve and the money, a warm check-in a few days later, a note in the language they read answering the question they were stuck on. That patient second touch is what turns a maybe into a signed case, and it is exactly the thing there is no time for between filings and hearings.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Immigration lawyers do not skip follow-up because they do not care. They skip it because the day fills up. You finish a filing, prepare for a hearing, take the walk-in whose status is about to lapse, and by evening the consultation you gave on Tuesday is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest consultations to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which consultations are still open and going cold.</li><li>The follow-up depends on you remembering, so it competes with active cases and loses.</li><li>By the time you circle back, the person has signed with a firm that reached out first, or given up on the process altogether.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not an effort problem, and it is the kind of thing you fix once and then it just runs. When every open consultation gets a couple of timed check-ins automatically, written to sound like your firm and, when it helps, in the language the person reads, someone still gathering documents keeps hearing from you while other firms go quiet. The work you already earned stops slipping away, and nothing in those messages ever promises an outcome.</p>'}],
    "bridge_h2": "Follow up on every consultation, automatically",
    "bridge_text": "A CRM keeps every open consultation in front of you and sends timed check-ins for you, in the language the person reads, so someone still gathering documents keeps hearing from your firm while others go quiet.",
    "bridge_slug": "crm-for-immigration-lawyers",
    "bridge_label": "CRM for immigration lawyers",
    "faqs": [
        ("How many times should I follow up on a consultation?",
         "A few light touches over the first weeks catches most of the people who stalled rather than declined: a check-in a few days after the consultation, then a short note answering common questions. The key is that it happens at all and on time, in the language they read, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like your firm, sent at a humane pace, and, when it helps, in the language the person is comfortable in. A short, warm check-in reads as attentive, not pushy, and most people appreciate the nudge because they meant to move forward and life got in the way. You can always step in and reach anyone directly.")],
    "trade_slug": "immigration_lawyers", "trade_plural": "immigration lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ How Do Immigration Lawyers Get More Clients? (how-to -> marketing) ============
{
    "slug": "how-do-immigration-lawyers-get-more-clients",
    "h1": "How Do Immigration Lawyers Get More Clients?",
    "title": "How Do Immigration Lawyers Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "Immigration lawyers get more clients by being easy to find and reach in the language people search in, and by turning satisfied clients and a trusting community into steady referrals.",
    "answer": "Immigration lawyers get more clients by being easy to find and easy to reach in the language people search in, and by turning every satisfied client into referrals. Show up in local search, keep genuine reviews coming, answer every call in the caller's language, and stay in touch with the community that already trusts you.",
    "sections": [
        {"h2_html": "Be easy to find, and easy to <em>reach</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most people looking for an immigration lawyer start the same way anyone looks for a local business: they search, and often they search in Spanish or another language. The first thing Google shows is the map pack, the little map with three local listings, star ratings, and a call button, and most people choose from those three without scrolling further. Getting into them runs on your Google Business Profile: whether it is verified, complete, and active, how close you are to the searcher, and how many recent, genuine reviews you have. A firm with a neglected profile is a nice brochure nobody sees at the moment someone is deciding who to call.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">But being found is only half of it. If the call rolls to voicemail, or reaches a front desk that cannot understand a Spanish-first caller, the search that found you still books with the next firm. For an immigration practice, being reachable in the language people speak is as much a part of getting clients as showing up in the first place.</p>'},
        {"h2_html": "Turn one client into the <em>next several</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Immigration work has a referral engine unlike almost any other practice. Help one person through a case and they can point a spouse, a parent, a sibling, and a whole circle at work and at church your way, because you are now the firm the family already trusts. That word of mouth is the lifeblood of an immigration practice, and it stays warm only if you stay in touch. A steady, respectful hand on past clients and the people who send you cases, a check-in after a case closes, a note when a renewal window is coming up, a thank-you to someone who referred a relative, keeps your firm the first name that comes up the next time someone in that community needs help.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this depends on gimmicks or invented promises. It works by doing a handful of plain things consistently: keep the profile active, ask every satisfied client for an honest review and make it one tap, answer every call in the language the caller speaks, and stay in touch with the community that trusts you. One rule keeps it clean and keeps you on the right side of attorney-advertising standards: everything you say is honest, you never buy reviews or filter out unhappy ones, and you never promise a visa, a green card, or any result. Good, reachable, trustworthy service is what compounds.</p>'}],
    "bridge_h2": "Get found, get reached, get referred",
    "bridge_text": "Marketing for an immigration firm is being easy to find in the language people search, easy to reach when they call, and worth referring after the case. We handle the search, the profile, and the reviews that make that happen.",
    "bridge_slug": "marketing-for-immigration-lawyers",
    "bridge_label": "Marketing for immigration lawyers",
    "faqs": [
        ("What is the fastest way to get more immigration clients?",
         "For most firms it is the local basics done well: a verified, active Google Business Profile, a steady flow of honest reviews, and a phone that is actually answered in the language people speak. Those move the needle faster than anything, because they meet people at the moment they are searching and deciding who to call."),
        ("Is it compliant to ask clients for reviews?",
         "Asking every client for an honest review is allowed and encouraged. What is not allowed is filtering out unhappy clients, offering incentives, or paying for reviews, and no marketing should ever promise a visa, a green card, or any outcome. Honest reviews and honest claims keep you on the right side of attorney-advertising standards.")],
    "trade_slug": "immigration_lawyers", "trade_plural": "immigration lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
]
