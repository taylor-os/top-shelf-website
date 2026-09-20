"""Per-page content specs for the SEO corpus (plan §5), immigration lawyers batch. Same
contract as scripts/corpus_specs.py: generate_corpus.py imports SPECS and owns the mechanics
(shell, schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict
below owns the UNIQUE, hand-written, immigration-firm-specific substance that clears the
uniqueness gate. Never templated find-and-replace, never the plumber, personal-injury, or
criminal-defense content reworded.

Legal hub, shared with the personal-injury and criminal-defense batches, so these dicts are
written immigration-distinct on purpose: a process that runs for months or years across many
steps (family petitions, visas, green cards, citizenship, asylum, removal defense), anxious
clients who often speak Spanish or another language first, USCIS deadlines and RFE response
windows as hard dates, the consultation as the front door, and long quiet stretches where a
client needs steady contact. Four service angles are here in one file (the ai-receptionist
dict carries "demo": True). Each example body ends with the literal "Illustrative example,
not a client." per the honesty rule; if the generator also appends that line, dedupe there.
Attorney advertising ethics: nothing here promises or implies an approval, a visa, a green
card, or any outcome, and the AI intake never gives legal advice.
"""

SPECS = [
# ==================== AI Receptionist for Immigration Lawyers ====================
{
    "slug": "ai-receptionist-for-immigration-lawyers", "demo": True,
    "trade_slug": "immigration_lawyers", "trade_plural": "immigration lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
    "breadcrumb_leaf": "AI Receptionist for Immigration Lawyers",
    "title": "AI Receptionist for Immigration Lawyers | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Immigration Lawyers",
    "meta_desc": "An immigration law answering service answers every call in English or Spanish, books the consultation, and flags urgent deadlines to your on-call attorney.",
    "service_schema_name": "AI Receptionist for Immigration Lawyers",
    "eyebrow": "For Immigration Lawyers",
    "h1_html": "AI Receptionist <em>for Immigration Lawyers</em>",
    "answer_block": "An immigration law answering service answers every call the moment it rings, in English or Spanish, books the consultation that is the front door to your firm, and flags an RFE deadline, a detained relative, or an expiring visa to your on-call attorney. The number stays registered to you, and the callers it brings in are yours.",
    "sections": [
        {"h2_html": "The call you miss is the consultation that <em>books with the next firm</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone who has finally decided to deal with their immigration status, to start a green card, file for a spouse or a parent, or answer a notice from the government, has usually been thinking about it for a long time before they pick up the phone. When they call, they are anxious and they are ready to talk to a lawyer today. If your line rolls to voicemail, they do not sit and wait. They call the next immigration firm on the page, and the one after that, until a real person answers and books them in. The consultation is the front door to your whole practice, and the firm that answers is usually the firm that gets to hold that first meeting.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">But you are in a hearing, meeting another client, or gone for the day, so the call you would have wanted goes to voicemail and the consultation goes to whoever answered. An AI receptionist answers on the first ring, stays calm with a nervous caller, finds out what they need and whether anything is on a deadline, and books the consultation on your calendar instead of letting it walk down the street. You come out of the hearing to the meeting already set, with the caller\'s name, language, and situation attached.</p>'},
        {"h2_html": "Built for callers whose <em>first language may not be English</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A large share of the people who call an immigration firm are more comfortable in Spanish or another language than in English, and a caller who reaches a voicemail in a language they do not speak, or a receptionist who cannot understand them, simply hangs up and finds a firm where someone speaks their language. That call was yours to lose. An AI receptionist can greet the caller and run the whole intake in the language they are comfortable in, so the conversation never stalls and the person feels understood from the very first word.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers and runs intake in the caller\'s own language, so a Spanish-first caller, or one who speaks another language, is helped instead of sent to voicemail.</li><li>Gathers what a case actually starts with: who the case is for, their current status, what they are trying to do, whether it is family based, employment based, citizenship, asylum, or removal defense, and whether they have received any notice or deadline.</li><li>Answers day and night, so the person who can only call after a long work shift still reaches a real conversation instead of a machine.</li><li>Treats a returning client or a referral from the community differently from a first-time caller, so the people who already trust you never hit a voicemail.</li></ul>'},
        {"h2_html": "Some immigration calls <em>cannot wait until Monday</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most immigration calls are not a middle-of-the-night emergency the way an arrest or a wreck is, and that is exactly why the urgent ones get missed. A relative picked up and held by immigration, a notice to appear with a date on it, a request for evidence with a response window that is already closing, a work permit or a status about to lapse, these are hard deadlines where a few days matter and a message left until Monday can cost someone dearly. An AI receptionist can tell those apart from a routine question about starting a petition.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">You decide what counts as urgent, and when a caller describes one of those situations the receptionist flags it to your on-call attorney at once so a real person can call back fast, while the routine consultations simply land on your calendar. Nothing time-sensitive sits unseen in a voicemail box over a weekend, and because the caller was understood in their own language from the first ring, the urgency is captured correctly instead of lost in a call the front desk could not follow.</p>'},
        {"h2_html": "You <em>own</em> the number, the intake, and the client list",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It answers on the number your firm already uses, or a fresh one put in your name, never in ours. Every caller, every intake, and every detail is yours and exportable any time, so the people you work hard to reach are an asset your firm keeps instead of something you rent back month to month. No long contract locks your data away. The AI receptionist is one piece of the Top Shelf platform, and it hands every consultation it books to the same CRM that follows up, so a person who has not signed yet never quietly goes cold. Just as important, it answers, reassures, and records the facts in the caller\'s language, and it never gives legal advice and never promises an approval, a visa, or a green card. Your attorneys make every legal decision and every call about whether to take a matter.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "An after-hours call in Spanish, <em>captured while you sleep</em>",
        "body_html": 'It is after seven in the evening when a woman gets home from work and finally calls about bringing her husband over on a family petition. Two firms she tries have closed for the day and send her to an English-only voicemail. Yours answers in Spanish, stays warm and calm, learns who the petition is for and that she has not received any notice yet, and books her a consultation for Thursday morning. It also notes that another caller that same evening mentioned a request for evidence due in a week, and flags that one to your on-call attorney right away. You arrive in the morning to both already handled, instead of hearing she hired someone else. Illustrative example, not a client.'},
    "faqs": [
        ("Does it work with my current firm phone number?",
         'Yes. It can answer on your existing number, or set up a new one registered in your name. Either way the number and every intake that comes through it belong to your firm and go with you if you ever leave.'),
        ("Can it actually take intake in Spanish or another language?",
         'Yes, and for immigration work that is a real edge. It can greet the caller and run the full intake in the language they are comfortable in, so a Spanish-first caller, or one who speaks another language, is helped and understood instead of hanging up on a voicemail they cannot follow. You decide which languages it handles.'),
        ("Will it flag an urgent case, like a detention or a filing deadline, to my attorney?",
         'It flags the calls you tell it to treat as urgent, a relative in custody, a notice with a date on it, a request for evidence whose window is closing, a status about to expire, and alerts your on-call attorney right away so a real person can call back fast. You set what counts as drop-everything.'),
        ("Is it going to give the caller legal advice or promise a result?",
         'No, and this matters. It answers, reassures, and captures the facts; it never advises on a case, never gives an opinion on someone\'s odds, and never promises an approval, a visa, or a green card. Every legal question and every decision about taking a matter stays with your attorneys. A nervous caller mostly needs to know a real firm is handling it, and a calm voice that gets the details beats a voicemail box.'),
        ("How fast can it be running?",
         'Setup is included with no separate onboarding fee. We build your intake questions, the languages it answers in, your booking, and your urgent-case rules for you, so it is answering in days, not weeks. Start with a free audit and we will show you what your current phone setup is missing.')],
    "related": [
        ("industry-legal.html", "Everything Top Shelf does for immigration lawyers"),
        ("solution-ai-phone.html", "How the AI phone and intake system works"),
        ("crm-for-immigration-lawyers.html", "The CRM that follows up on every consultation you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing consultations to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many calls and after-hours consultations your current setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ========================= CRM for Immigration Lawyers =========================
{
    "slug": "crm-for-immigration-lawyers",
    "trade_slug": "immigration_lawyers", "trade_plural": "immigration lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
    "breadcrumb_leaf": "CRM for Immigration Lawyers",
    "title": "CRM for Immigration Lawyers | Top Shelf Business Solutions",
    "og_title": "CRM for Immigration Lawyers",
    "meta_desc": "A CRM for immigration lawyers follows up on every consultation and keeps clients steady through the long waits, so they stay with you instead of drifting away.",
    "service_schema_name": "CRM for Immigration Lawyers",
    "eyebrow": "For Immigration Lawyers",
    "h1_html": "CRM <em>for Immigration Lawyers</em>",
    "answer_block": "A CRM for immigration lawyers keeps every consultation, client, and open case in one place and follows up for you, so the person still gathering documents and the family waiting out a long case both stay with your firm instead of the one that kept in touch. Your consultation list quietly becomes your caseload.",
    "sections": [
        {"h2_html": "The consultation you gave is the case that <em>drifts away</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most immigration firms do not have a caller problem. They have a follow-through problem. Someone sits down for a consultation about a green card or a family petition, leaves ready to move forward, and then runs into the real reasons immigration cases stall: the documents are scattered across two countries, the fee is a lot of money to gather, a spouse or a parent needs to be talked to first. Weeks pass, life crowds in, and the case that felt urgent in your office quietly slips down their list. They were never a bad lead. They just needed a nudge while they were still deciding, and that is the call there is never time to make between filings and hearings.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every consultation that has not turned into a signed case in front of you and follows up for you, on a schedule you set, with messages that sound like your firm and, when it helps, land in the client\'s own language. The person still working up the nerve and the money hears from you again instead of drifting to the firm that stayed in touch. It is not pressure, it is a patient reminder that you are still there and still ready when they are, which for a hesitant client is often all it takes.</p>'},
        {"h2_html": "A case that runs for years needs a client who <em>does not give up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Signing the client is the start of a road that can run for months or years. A petition is filed and then everyone waits, sometimes a very long time, for the government to act, and in that silence a client starts to worry. They wonder whether anything is happening, whether their case was forgotten, whether they did something wrong, and a frightened client with no news is the one who calls your office again and again, posts a bad review, or drifts off and misses an appointment. The quiet stretches are exactly when a client needs to hear from you, and exactly when a busy firm goes silent.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every client, case, note, and stage sits in one place, so you can see where each person is on the long road from petition to interview to decision.</li><li>Steady check-ins go out through the waiting, so a client hears a reassuring word before they start to worry, not after they have already panicked.</li><li>Reminders reach the client before each concrete step, a biometrics appointment, an interview, a renewal window, so the date does not slip because everyone assumed someone else was watching it.</li><li>You can see at a glance who has gone quiet on your calendar and reach the anxious client before they reach for another firm\'s number.</li></ul>'},
        {"h2_html": "One family you help becomes the <em>next several</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Immigration work has a referral engine unlike any other practice. Help one person become a citizen and they can petition for a spouse, a parent, a sibling, and each of those is a new case that comes to the firm the family already trusts. A client who was treated with patience and respect becomes the name passed around a tight community, at church, at work, among relatives, whenever someone else needs help with their papers. That word of mouth is the lifeblood of an immigration practice, and it stays warm only if you stay in touch. A CRM keeps a light, steady hand on past clients and the people who send you cases, a check-in after a case closes, a note when a work permit is coming up for renewal, a thank-you to someone who referred a relative, so your firm is the first name that comes up the next time a family in that community needs a lawyer.</p>'},
        {"h2_html": "One list, wired to your calls and every <em>stage of a case</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every client and every note is yours and exportable any time, never trapped inside a tool you rent by the month. The CRM is one piece of the Top Shelf platform: it takes the consultations the AI receptionist books and starts the follow-up on its own, and it hangs each meeting and next step on the right person so nothing is tracked in two places or forgotten in one. Your immigration case-management software holds the official file, the forms, and the legal deadlines; the CRM works the human side of a long case, the follow-up on people who have not signed, the reassurance through the quiet stretches, the steady touch on the families and community who refer you. It runs the relationship while your attorneys run the cases and make every legal decision. Nothing your firm has earned goes cold, and nothing here ever promises a client an outcome.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The long wait that <em>keeps its client</em>",
        "body_html": 'A family files a green card petition through your firm and then the long wait begins, the kind where months pass with no word from the government. Normally that silence is where a client starts to fear the worst and either floods your front desk with calls or drifts away discouraged. Instead the CRM sends a calm check-in every so often, in the language they read, and a reminder when their biometrics appointment comes up, so they always know their case is moving and in steady hands. When the mother\'s sister needs help with her own paperwork the next year, there is no question who the family calls. Nobody on your team had to keep a mental list. Illustrative example, not a client.'},
    "faqs": [
        ("Does it import my existing clients and consultations?",
         'Yes. Your current clients, past consultations, and case notes come in and live in one place, all of it yours and exportable. The point is to put the contacts your firm has already earned to work instead of letting them sit in a phone and an inbox.'),
        ("Will it follow up on people who came in for a consultation but have not started?",
         'Yes, on the schedule you approve. An open consultation gets a check-in a few days later and another after that, sent for you and, when it helps, in the client\'s own language, so a person still gathering documents keeps hearing from you while other firms go quiet. You can step in and reach anyone directly any time.'),
        ("Can it keep a client calm during the long waits at USCIS?",
         'Yes, and that is often the biggest win. You set the rhythm, and it sends reassuring check-ins through the quiet stretches so a client hears from your firm before they start to fear the worst, instead of stewing, flooding your front desk, or drifting away discouraged.'),
        ("Can it remind clients about a biometrics appointment, an interview, or a renewal?",
         'Yes. It keeps a reminder on each client\'s next step and nudges them before the date, so they arrive prepared and a renewal window does not lapse unnoticed. Your case-management software still holds the official file and the legal deadlines; the CRM works the human side of hitting them.'),
        ("How is this different from my immigration case-management software?",
         'It sits alongside it. That software runs the legal file, the forms, and the filing deadlines. This runs everything around it: the consultations you have not signed, the clients who need reassurance through a long case, and the families and community who refer you. The two do different jobs.')],
    "related": [
        ("industry-legal.html", "Everything Top Shelf does for immigration lawyers"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-immigration-lawyers.html", "The AI receptionist that feeds it every consultation"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting consultations and clients <em>drift away</em>",
    "cta_sub": "Get a free audit of how many of your consultations and open cases are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ====================== Marketing for Immigration Lawyers ======================
{
    "slug": "marketing-for-immigration-lawyers",
    "trade_slug": "immigration_lawyers", "trade_plural": "immigration lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
    "breadcrumb_leaf": "Marketing for Immigration Lawyers",
    "title": "Marketing for Immigration Lawyers | Top Shelf Business Solutions",
    "og_title": "Marketing for Immigration Lawyers",
    "meta_desc": "Immigration lawyer marketing keeps your Google Business Profile active and reviews strong, so a wary client searching nearby trusts your firm enough to call.",
    "service_schema_name": "Marketing for Immigration Lawyers",
    "eyebrow": "For Immigration Lawyers",
    "h1_html": "Marketing <em>for Immigration Lawyers</em>",
    "answer_block": "Immigration lawyer marketing keeps your firm visible and trustworthy where clients actually look, your Google Business Profile, your reviews, and your standing in the community, so when someone anxious searches for an immigration lawyer nearby, in English or in their own language, your name is the one that looks real, respected, and safe enough to call.",
    "sections": [
        {"h2_html": "Choosing an immigration lawyer is a <em>careful, high-trust decision</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody hires an immigration lawyer on impulse. This is a decision about a family\'s future, a case that can run for years, and a real amount of money, so people take their time. They search, they read reviews, they ask relatives and friends who have been through it, and they compare a few firms before they ever pick up the phone. That patience changes what your marketing has to do. You are not catching someone in one frantic moment the way an accident or an arrest does; you are staying visible and looking trustworthy across the whole stretch of time a person spends deciding, so that when they are finally ready, yours is a name they have already seen more than once and started to trust.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Get found and look credible through that window and the consultation is usually yours. A firm that shows up thin, stale, and barely reviewed loses to the one that looks active and established, no matter how good the lawyering behind the quiet profile actually is. Marketing is simply making sure yours is the profile that keeps earning that trust, in the places your clients look.</p>'},
        {"h2_html": "The community is wary of scams, so <em>trust is the whole game</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">People looking for immigration help are often carrying real fear, about their status, about their family, and about being taken advantage of. Many have been warned about scams and about people who pose as lawyers and take money for paperwork they are not allowed to touch, so a newcomer to your profile arrives already guarded. That wariness is the single biggest thing your marketing has to answer, and it answers very differently than it would for most trades. A loud, boastful listing reads as exactly the kind of thing they were told to avoid. What reassures a cautious person is a profile that looks like a real, licensed law firm run by real people: clear and honest information, a genuine address and set hours, current photos, and reviews from people who describe being treated with respect and never talked down to. Looking legitimate and human is not a nicety in this field, it is the deciding factor in whether a frightened person trusts you enough to reach out at all, or quietly keeps scrolling.</p>'},
        {"h2_html": "Be found in the <em>language your clients think in</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A great many of your clients search, read, and feel most at ease in Spanish or another language, and they search for the exact thing weighing on them, not a generic banner. Being present in their language, and known for the specific help they need, is what puts your firm in front of the right person at the right moment. Reaching them in the language they think in is not a translation afterthought either; it signals that this is a firm where they will be understood, which for a nervous newcomer is half the reason they choose one lawyer over another.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A profile and content that meet clients in the language they actually use, so a Spanish-first searcher finds a firm that clearly speaks to them.</li><li>Known for the services you truly handle, green cards, family petitions, work visas, citizenship, asylum, or removal defense, instead of one vague immigration label lost among the rest.</li><li>Anchored to the city and community you serve, so the people close enough to sit down with you are the ones who find you.</li><li>The questions a nervous first-timer asks, what a consultation costs, what the process looks like, answered plainly right where they will see them.</li></ul>'},
        {"h2_html": "Reviews from your community, earned <em>within the rules</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Reviews carry enormous weight with someone choosing an immigration lawyer, because word of mouth is how trust travels through an immigrant community, and a review works even harder when it is written in the language the next reader speaks. The reviews you gather need to be genuine, collected only from clients who are willing to give them, and never pressured or paid for. When a review speaks to being treated with dignity, kept informed through a long and stressful case, and helped honestly, it reassures the next anxious caller far more than any claim you could make about yourself. All of it stays inside the rules for attorney advertising: no promising or implying an approval, a visa, or a green card, no fake or incentivized reviews, no misleading claims. A steady stream of genuine reviews and current activity also keeps you rising in the local results over time, so each honest review does double duty, reassuring the reader and lifting you in front of the next one. This is the public face of your firm, aimed at people who are not your clients yet; the private follow-up to the people already in your database is the CRM.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A weeks-long search that ends <em>at your firm</em>",
        "body_html": 'A woman looking for help to bring her mother over spends two weeks reading and asking around before she trusts anyone with it. Every time she looks, your firm\'s profile is active, with recent reviews in the language she reads that describe people being treated with respect and kept informed. The firm one listing down looks abandoned, old reviews, missing hours, no sign anyone is home. She books a consultation with you, because yours is the only one that looks both real and safe to call. Illustrative example, not a client.'},
    "faqs": [
        ("Do you post to my Google Business Profile for me?",
         'Yes. We keep it active with updates, real replies to reviews, and local content on a regular schedule, and keep your practice areas, hours, and service area accurate, so it looks current whenever someone searches for an immigration lawyer near them.'),
        ("Can you help me reach clients who search in Spanish or another language?",
         'Yes, and in this field it matters more than almost anywhere. We can build your profile and content to meet clients in the language they actually use, so a Spanish-first searcher finds a firm that clearly speaks to them instead of scrolling past to one that does.'),
        ("My community has been burned by scams. How does marketing build trust?",
         'By making you look unmistakably like a real, licensed firm run by real people, with honest information, a genuine presence, and reviews that describe respectful, honest treatment. In a field crowded with people posing as lawyers, looking legitimate and human is exactly what reassures a wary person enough to reach out.'),
        ("Is this allowed under attorney advertising rules?",
         'Yes, and staying inside those rules is the whole approach. No promising or implying an approval, a visa, or a green card, no fake or paid reviews, no misleading claims. We keep your real profile active and your genuine reviews visible, which is both permitted and what actually earns trust.'),
        ("How is this different from the CRM follow-up?",
         'The CRM works privately with the people already in your database, consultations you have not signed, current clients, past clients, and referral sources. Marketing is the public side: being visible, current, and trustworthy to the anxious stranger who has never heard of you and needs an immigration lawyer now.')],
    "related": [
        ("industry-legal.html", "Everything Top Shelf does for immigration lawyers"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-immigration-lawyers.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the firm they <em>trust enough to call</em>",
    "cta_sub": "Get a free audit of how visible and trustworthy your firm looks to someone searching for an immigration lawyer in your community right now, whether you work with us or not. No credit card, never a call center.",
},
# =================== Websites & SEO for Immigration Lawyers ===================
{
    "slug": "websites-seo-for-immigration-lawyers",
    "trade_slug": "immigration_lawyers", "trade_plural": "immigration lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
    "breadcrumb_leaf": "Websites & SEO for Immigration Lawyers",
    "title": "Websites & SEO for Immigration Lawyers | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Immigration Lawyers",
    "meta_desc": "An immigration lawyer website built for SEO ranks for green card and citizenship searches in your city and captures the consultation, in your clients' language.",
    "service_schema_name": "Websites & SEO for Immigration Lawyers",
    "eyebrow": "For Immigration Lawyers",
    "h1_html": "Websites &amp; SEO <em>for Immigration Lawyers</em>",
    "answer_block": "An immigration lawyer website built for SEO ranks for the exact help someone is searching for, a green card lawyer, a citizenship attorney, help with a family petition, in your city and in the language your clients read, and turns a careful, wary researcher into a booked consultation that belongs to your firm, not a directory.",
    "sections": [
        {"h2_html": "In this field, your site is the first proof you are <em>real and licensed</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone weighing an immigration case is not landing on your site in a panic, they are researching, carefully, because it is their family and their future and a lot of money over a long engagement. And they arrive guarded, because this is a field crowded with scams and people who pose as lawyers, so in the first few seconds they are asking one quiet question: is this a real, licensed firm I can trust, or something to click away from. A site that opens cleanly, explains the process in plain language, names the help you actually offer, and shows real people and honest reviews answers that question with a yes. A cheap, generic template answers it with a no, no matter how good the firm behind it is.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">For immigration work the website is not a brochure, it is the first proof that you are legitimate and safe to hand a family\'s future to. That proof is exactly what carries a cautious visitor from reading to requesting a consultation instead of closing the tab and asking a cousin who they used.</p>'},
        {"h2_html": "Rank for the <em>status someone is trying to get</em>, not a slogan",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national legal directory this year for a broad term like immigration lawyer, and you do not need to. People do not search in the abstract; they search for the exact status they are chasing and the place they live. A green card lawyer in your city, a citizenship or naturalization attorney nearby, help with a family petition, a work visa, asylum, or deportation and removal defense, these are the searches that actually turn into consultations, and they are exactly where a national directory is weak and a real local firm can win. Pages built around the services you genuinely offer and the community you actually serve are what a search engine can rank and what an anxious searcher clicks. A single page that only says immigration law competes with everyone and stands out to no one, while a firm that speaks to the specific case someone is facing feels like it was built for them. And the more of these specific pages you build, the more of your own city\'s immigration searches you quietly own, one status and one neighborhood at a time, in a way a broad national directory never bothers to.</p>'},
        {"h2_html": "In their language, with an easy way to <em>reach you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A visitor who is more comfortable in Spanish or another language will not stay on a site they cannot read, and a nervous person is not going to fill out a demanding form or wade through pages of legal history before they feel safe. The site has to meet them where they are and make the first step easy and low-pressure, whatever the hour they found you. Every extra click, every field they do not understand, every paragraph of dense legal English is a reason for an already-anxious person to give up and close the tab.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Available in the language your clients read, so the people you serve are not turned away at the door by a wall of English.</li><li>Plain, honest explanations of a confusing process, with no jargon and no claims about how a case will end.</li><li>A simple way to request a consultation for the person who would rather write than call, and a clear phone option for the person who wants to talk now.</li><li>Fast and easy to use on a phone, because that is where most of your visitors are reading.</li></ul>'},
        {"h2_html": "The consultations are <em>yours</em>, not a directory's",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search your own city for an immigration lawyer and the top results are often not local firms at all, they are directories and pay-per-lead services that outrank everyone and then sell the contact, sometimes to several firms at once, sometimes back to you for a slice of the fee. Every month you have no real site of your own, that traffic, and the families behind it, belongs to a middleman instead of you. A site your firm owns and ranks flips it: the person reaches you and only you, there is no per-lead charge skimming a fee a family is already stretching to afford, and the page keeps working and compounding for as long as it stands. The work you put into it this year keeps paying off the next, which is the opposite of a lead you buy once and never see again. It is registered to your firm, not a platform that can drop you or raise the rate, and it feeds the same CRM and answering service that catch and follow up on every consultation it earns. It works to bring people in; it never promises any of them an outcome.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A green card search that finds <em>your firm, not a middleman</em>",
        "body_html": 'A man wants to help his wife get her green card and spends a couple of weeks reading before he trusts anyone with it. He searches for a green card lawyer in his city, and instead of a directory that would take his information and sell it to three firms, he finds your site ranking for exactly that, readable in the language he thinks in, clearly a real and licensed firm, with reviews from people like him. He requests a consultation right there, and it comes straight to you with no middleman in between. Illustrative example, not a client.'},
    "faqs": [
        ("What immigration terms can my site realistically rank for?",
         'The specific and local ones: your firm name, and the help you offer paired with your city, a green card lawyer, a citizenship attorney, a family petition, a work visa, asylum, or removal defense near you. That is where a local firm can win, not the broadest national terms a directory has spent years dominating.'),
        ("Can my site work in Spanish or another language?",
         'Yes, and for most immigration firms it should. A visitor who is more comfortable in another language will not stay on a site they cannot read, so meeting them in their language keeps the people you serve from bouncing straight to a competitor.'),
        ("How is this different from paying for leads or a directory?",
         'A pay-per-lead service or directory rents you a contact it also sells to other firms, and it stops the day you stop paying. A website your firm owns captures the consultation for you alone and keeps working long after it is built, with no fee coming out of every case.'),
        ("My clients are careful and wary of scams. Can a website really build that trust?",
         'Yes, and it is one of the main jobs of the site. A clean, honest page that explains the process plainly, shows real people and real reviews, and makes no claims about outcomes tells a cautious person you are legitimate and safe to contact. That is often what decides whether they reach out at all.'),
        ("How long until it starts ranking?",
         'Local, specific searches can start moving within weeks; the broader, more competitive terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.')],
    "related": [
        ("industry-legal.html", "Everything Top Shelf does for immigration lawyers"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-immigration-lawyers.html", "Staying visible in your community beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the searches for <em>your own community</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and lead-sellers taking your consultations, whether you work with us or not. No credit card, never a call center.",
},
]
