"""Colony page specs for PERSONAL INJURY LAWYERS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a personal injury firm owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict owns UNIQUE, hand-written, personal-injury-specific substance (the generator owns shell,
schema, events, keyword placement). Every page leads with the injury reality: an accident victim
who signs with whoever answers first, contingency work, one signed case that dwarfs the cost,
after-hours and Spanish-speaking callers, competing with big-ad-budget firms, so it never reads as
a generic legal or plumbing template. Same honesty rules as the money specs: no invented stats,
prices, or clients; only the real prices ($299/$899/$2,500 plans, $1,500 one-time site) ever
appear; no em or en dashes anywhere; leads "go cold" or "slip away", never "leak". Attorney-
advertising compliant: no promise of any case outcome, settlement, result, or ranking; the AI
receptionist does intake and booking, never legal advice; attorneys make every legal decision.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 personal-injury-lawyer-website-cost         (cost)    -> websites-seo-for-personal-injury-lawyers
  2 personal-injury-answering-service-cost       (cost)    -> ai-receptionist-for-personal-injury-lawyers
  3 is-intake-software-worth-it-personal-injury  (cost)    -> crm-for-personal-injury-lawyers
  4 why-personal-injury-firms-miss-intake-calls  (problem) -> ai-receptionist-for-personal-injury-lawyers
  5 why-personal-injury-leads-go-cold            (problem) -> crm-for-personal-injury-lawyers
  6 how-do-personal-injury-firms-get-more-cases  (how-to)  -> marketing-for-personal-injury-lawyers
"""

TOPICS = [
# ============ How Much Does a Personal Injury Lawyer Website Cost? (cost -> websites-seo) ============
{
    "slug": "personal-injury-lawyer-website-cost",
    "h1": "How Much Does a Personal Injury Lawyer Website Cost?",
    "title": "How Much Does a Personal Injury Lawyer Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A personal injury lawyer website ranges from cheap templates to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A personal injury lawyer website can run from a few hundred dollars for a template to several thousand for a custom build. What matters more is whether it ranks and captures the call from someone who just had a wreck, since they sign with whoever answers first. Top Shelf builds one for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The price you see quoted for a personal injury law firm website swings widely because firms are not all buying the same thing. A template you fill in yourself and a custom site built to rank against the firms with big advertising budgets are different products with the same name. An accident victim rarely scrolls past the first few results, so before you compare quotes it helps to know what you are actually paying for.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A do-it-yourself builder is cheap each month, but you do the work, and it is rarely built to rank or to convert someone searching in a panic right after a crash.</li><li>A one-time custom build costs more up front and is yours to keep, but a site alone does little if nobody handles the ongoing SEO that gets it found.</li><li>An agency retainer bundles the build with ongoing SEO and updates, which is where most of the long-term value lives, and also where the monthly cost lives.</li><li>Questions to ask before you sign: who owns the site, what a change costs, and whether you keep it if you leave.</li></ul>'},
        {"h2_html": "What a personal injury firm should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A personal injury website earns its money one way: it turns someone searching after an accident into a call or an intake your firm actually receives. That means it has to load fast, rank for the injuries and areas you handle, and put a tap-to-call button in front of a shaken visitor before they scroll on to the next firm. Because injury work runs on contingency, the firm carries the cost of getting found, so a site that looks impressive but never ranks is the most expensive kind. One signed case can be worth far more to your firm than the site ever cost.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking, a case, or a result, because no one controls Google or the outcome of a matter, but a free audit can show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that pays for itself",
    "bridge_text": "A personal injury website is only worth the cases it brings in. Ours is built to rank for the injuries and areas you handle and turn a search after a wreck into an intake, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-personal-injury-lawyers",
    "bridge_label": "Websites & SEO for personal injury lawyers",
    "faqs": [
        ("Is a cheap template site good enough for a personal injury firm?",
         "It can get you online, but a template you fill in yourself is rarely built to rank against firms with real ad budgets or to convert someone searching in a panic after a crash. If a site is not getting found or turning visitors into intakes, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "personal_injury_lawyers", "trade_plural": "personal injury lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ========= What Does a Personal Injury Answering Service Cost? (cost -> ai-receptionist) =========
{
    "slug": "personal-injury-answering-service-cost",
    "h1": "What Does a Personal Injury Answering Service Cost?",
    "title": "What Does a Personal Injury Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for personal injury firms often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "A personal injury answering service usually bills per call, per minute, or on a monthly retainer, so the busy nights add up fast. Top Shelf takes a different route: an AI receptionist that answers every accident call 24/7 and runs intake comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy stretch turns into a big bill. A personal injury firm gets its calls at the worst times for a live service: nights, weekends, and the hours right after a wreck, when after-hours minutes tend to cost the most. A real share of those callers are more comfortable in Spanish, and a voicemail box does nothing for them. It helps to know the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for every call answered, so a busy week or a wave of calls that are not real cases runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a long, emotional call after an accident costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when the calls are coming in.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: someone who was just in a wreck does not leave a voicemail, they call the next firm on the list until a real person picks up. The true cost of no coverage is not a monthly fee, it is the case that signed with whoever answered first. But a generic call center reading a script cannot run a real intake, so you can pay for coverage and still lose the case on a weak first call.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, gathers the facts a case actually needs, and books the consultation or flags a true emergency to your on-call attorney. It can be set to answer in Spanish as well as English. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. Because injury work runs on contingency and one signed case can be worth far more than the plan, a single intake it saves on a weekend can cover the cost many times over. It captures the facts and books the call; it never gives legal advice, and your attorneys decide every case.</p>'}],
    "bridge_h2": "Answer every accident call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, runs the intake a case needs, and books it or routes a true emergency to your on-call attorney, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-personal-injury-lawyers",
    "bridge_label": "AI receptionist for personal injury lawyers",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when the accident calls come in, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the after-hours case it runs intake on instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or holidays?",
         "No. It answers 24/7 as part of the plan, including the late-night call after a wreck and the holiday accident that other firms send straight to voicemail, with no after-hours surcharge or overage.")],
    "trade_slug": "personal_injury_lawyers", "trade_plural": "personal injury lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Is Intake Software Worth It for a Personal Injury Firm? (cost -> crm) ============
{
    "slug": "is-intake-software-worth-it-personal-injury",
    "h1": "Is Intake Software Worth It for a Personal Injury Firm?",
    "title": "Is Intake Software Worth It for a Personal Injury Firm? | Top Shelf Business Solutions",
    "meta_desc": "For most personal injury firms, intake software pays for itself by rescuing one lead that would have gone cold. It comes in Top Shelf's Signature plan at $899/mo, not a separate bill.",
    "answer": "For most personal injury firms, yes. Intake software pays for itself when it wins back a lead that would have gone cold while you were in court, or keeps a signed client from feeling ignored. It stops being worth it only if you chase every intake anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When intake software is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Intake software is worth it for a personal injury firm when you take more calls and intakes than anyone can personally keep track of, which is most firms doing any real advertising. It is not worth it if you are a solo attorney handling a handful of matters and genuinely calling every lead back, though that rarely holds as you grow. The honest test is simple: how many intakes did you run last month that nobody followed up on, and how many people said they wanted to think it over and were never heard from again? Those are the cases this is built to bring back, and in injury work a single one of them can be worth far more than a year of the software.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of intake software for a personal injury firm is not the app, it is the work that stops slipping away. A person weighing two or three firms after a wreck, a signed client sitting in the quiet middle of a case, a past client who just had a second accident: each one is a case you have already half-earned and are one timely message away from keeping.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every unsigned intake on a schedule, so the person comparing firms keeps hearing from you while the others go quiet.</li><li>It sends check-ins through the slow stretches of a signed case, so a client hears from your firm before they start to worry and leave a bad review.</li><li>It keeps every lead, client, and intake in one place instead of scattered across voicemails, notes, and memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf this is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: bring back one case you would have lost and it has paid for itself. It tracks the follow-up and the facts; your attorneys make every decision about the case.</p>'}],
    "bridge_h2": "Put your intake list to work",
    "bridge_text": "The intakes you already ran are the cheapest cases you can get. Intake and follow-up software works every one for you, so the person still deciding calls you back instead of the firm that stayed in touch.",
    "bridge_slug": "crm-for-personal-injury-lawyers",
    "bridge_label": "CRM for personal injury lawyers",
    "faqs": [
        ("Is intake software overkill for a small personal injury firm?",
         "Not usually. Even a one or two attorney firm runs more intakes and takes more calls than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If leads go cold and signed clients feel forgotten, intake software earns its keep."),
        ("How is this different from the case-management software I already use?",
         "It sits alongside it. Case management runs the legal file; this runs the relationship, the follow-up on leads you have not signed, the check-ins with clients, and the touchpoints with referral sources, which is the part that tends to fall through when everyone is busy.")],
    "trade_slug": "personal_injury_lawyers", "trade_plural": "personal injury lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ========= Why Do Personal Injury Firms Miss Intake Calls? (problem -> ai-receptionist) =========
{
    "slug": "why-personal-injury-firms-miss-intake-calls",
    "h1": "Why Do Personal Injury Firms Miss Intake Calls?",
    "title": "Why Do Personal Injury Firms Miss Intake Calls? | Top Shelf Business Solutions",
    "meta_desc": "Personal injury firms miss intake calls because they ring during court, depositions, and the night, and an accident victim does not leave a voicemail, they call the next firm.",
    "answer": "Personal injury firms miss intake calls because they come when an attorney is in court, in a deposition, with another client, or asleep, and someone who was just in a wreck does not leave a voicemail. They call the next firm until one answers. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Trial work does not keep phone hours. When an accident call comes in you are often standing in front of a judge, sitting in a deposition, meeting another client, or asleep at one in the morning, and none of those are moments you can stop and take it. The more cases you are actively working, the more new calls you miss, which means your busiest stretches are also the ones where the most new work slips away. It is not a discipline problem. One attorney cannot try a case and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for someone who was just hurt it is not one. A person calling from a hospital bed or a body shop, still shaken, is not going to leave a message and wait for a callback. They move down the list until a real person answers, and by the time you check your phone, the case has already signed somewhere else.</p>'},
        {"h2_html": "The intake you miss is your most <em>expensive miss</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. The call after a serious wreck, the one with real injuries and another driver who was clearly at fault, is the case that matters most, and it comes in at night and on weekends when every other firm is closed too. Those after-hours calls are exactly the ones a person makes to three or four firms in a row, and exactly the ones most likely to roll to voicemail. So the calls you are most likely to miss are also the ones worth the most to your firm.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can actually run an intake, not just take a message. A voicemail box cannot ask what happened, and a generic call center does not know which questions a case needs or which call cannot wait until Monday. What works is something that answers on the first ring day or night, gathers the facts, books the consultation, and flags a true emergency straight to your on-call attorney, so you never lose the case just because you could not pick up. It records the facts; your attorneys make every legal decision.</p>'}],
    "bridge_h2": "Stop losing intakes to voicemail",
    "bridge_text": "An AI receptionist answers every accident call on the first ring, day or night, runs the intake a case needs, and books it or routes a true emergency to your on-call attorney, so the case never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-personal-injury-lawyers",
    "bridge_label": "AI receptionist for personal injury lawyers",
    "faqs": [
        ("Would an accident victim rather reach a real person?",
         "What someone needs most after a wreck is to know a real firm is handling it, and a calm voice that captures the details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, and hands a true emergency straight to your on-call attorney."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your phone is free. Forwarding still rolls to voicemail when you are in court, in a deposition, or already on another call. Something that always answers and runs the intake is what catches the calls a forward would still miss.")],
    "trade_slug": "personal_injury_lawyers", "trade_plural": "personal injury lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ================ Why Do Personal Injury Leads Go Cold? (problem -> crm) ================
{
    "slug": "why-personal-injury-leads-go-cold",
    "h1": "Why Do Personal Injury Leads Go Cold?",
    "title": "Why Do Personal Injury Leads Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most personal injury leads go cold not over price but because nobody followed up. The person wanted to wait on the insurance offer, and signed with whoever checked back in.",
    "answer": "Most personal injury leads go cold not because the person picked another firm on the spot, but because nobody followed up. They wanted to think it over, talk to a spouse, or wait on the insurance offer, and the case went to whoever checked back in. A quiet lead is usually a maybe that never got a second call.",
    "sections": [
        {"h2_html": "Silence usually means waiting, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet lead as a no, so you drop it and move on. But most of the time the person did not decide against you at all. They called after an accident, ran through the intake, and meant to move forward, then got pulled into their own life: work, doctor visits, the insurance adjuster, and a dozen other decisions. Yours slid down the pile. A week later they could not tell you apart from the two other firms they called that day.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The firm that signs the case is usually not the one they called first. It is the one that stayed in front of them: a friendly check-in a couple of days later, a short note answering the question they were stuck on. That second touch is what turns a maybe into a signed client, and it is exactly the thing there is no time for between hearings and active files.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Attorneys do not skip follow-up because they do not care. They skip it because the day fills up. You finish a hearing, roll into a client meeting, handle the case that jumped the line, and by evening the intake you ran on Tuesday is out of sight. Doing it from memory means it only happens when things are slow, which is exactly when you have the fewest new leads to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which intakes are still open and going cold.</li><li>The follow-up depends on you remembering, so it competes with active cases and loses.</li><li>By the time you circle back, the person has already signed with a firm that beat you to it.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and it just runs. When every open intake gets a couple of timed check-ins automatically, written to sound like your firm, the person comparing firms keeps hearing from you while the others go quiet, and the cases you already worked to earn stop slipping away.</p>'}],
    "bridge_h2": "Follow up on every lead, automatically",
    "bridge_text": "A CRM keeps every open intake in front of you and sends timed check-ins for you, so a person comparing firms keeps hearing from you while the others go quiet, and the case comes back.",
    "bridge_slug": "crm-for-personal-injury-lawyers",
    "bridge_label": "CRM for personal injury lawyers",
    "faqs": [
        ("How many times should I follow up on an unsigned lead?",
         "A couple of light touches over the first week or two catches most of the maybes without being pushy: a check-in a few days after the intake, then a short note answering common questions. What matters is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like your firm and sent at a sensible pace. A short, steady check-in reads as attentive, not pushy, and most people appreciate it because they meant to get back to you and forgot. You can always step in and message anyone directly.")],
    "trade_slug": "personal_injury_lawyers", "trade_plural": "personal injury lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ How Do Personal Injury Firms Get More Cases? (how-to -> marketing) ============
{
    "slug": "how-do-personal-injury-firms-get-more-cases",
    "h1": "How Do Personal Injury Firms Get More Cases?",
    "title": "How Do Personal Injury Firms Get More Cases? | Top Shelf Business Solutions",
    "meta_desc": "Personal injury firms get more cases by being the firm an accident victim finds and reaches first: the Google map pack, real reviews, and answering every call, not by outspending the big firms.",
    "answer": "Personal injury firms get more cases by being the firm an accident victim finds and reaches first. That means showing up in Google's map pack and search, a steady stream of real reviews, a site that converts, and answering every call. You do not have to outspend the firms buying billboards and TV to win the local search.",
    "sections": [
        {"h2_html": "You do not have to outspend the <em>billboard firms</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to look at the firms with billboards on the highway and television spots during the news and assume that is the price of getting cases. It is one way, and an expensive one. But most people who were just in an accident do not dial the number off a billboard from memory. They pick up their phone and search for an injury lawyer near them, then choose from what they see. That search is a game a smaller firm can win, because it does not go to whoever spent the most, it goes to whoever shows up and looks trustworthy at that moment.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The first thing Google shows for that search is not a website. It is the map pack, the little map with three local firms, star ratings, and a call button. Most people choose from those three without scrolling further, so if you are not there, the ad budget the big firms spend barely matters to the person searching right now.</p>'},
        {"h2_html": "What actually brings in <em>more cases</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more cases is less about one clever move and more about doing the unglamorous things consistently, which is what tends to fall apart when a firm is busy running its cases. A handful of levers do most of the work.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Get your Google Business Profile verified, complete, and active, since the map pack is where most local injury searches start.</li><li>Build a steady flow of real reviews from past clients, because the firm with recent, genuine reviews earns the click over the one with none.</li><li>Have a site that loads fast, ranks for the injuries and areas you handle, and makes it one tap to call.</li><li>Answer every call and follow up on every intake, so the demand you already create does not slip away to the firm that picked up.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this promises a case or a result, because no one controls Google or how a matter turns out. But being consistently findable, well reviewed, and quick to answer is how a local firm competes for cases without matching a national advertising budget. A free audit can show you where your firm stands on each of these today.</p>'}],
    "bridge_h2": "Get found where the cases start",
    "bridge_text": "Most injury cases begin with a search, not a billboard. Keeping your Google profile active, your reviews growing, and your site ranking is how you get in front of an accident victim right when they are choosing who to call.",
    "bridge_slug": "marketing-for-personal-injury-lawyers",
    "bridge_label": "Marketing for personal injury lawyers",
    "faqs": [
        ("Do I need a big advertising budget to get personal injury cases?",
         "Not to win the local search. Billboards and television are one route, but most people search for an injury lawyer after a wreck and choose from the map pack and reviews. A verified, active profile, real reviews, and a site that ranks put you in that moment without a national budget."),
        ("How long until my firm shows up on Google?",
         "A neglected profile that gets verified, completed, and active can start climbing within a few weeks, and it compounds as reviews and content build. Nobody controls Google, so no honest company promises a specific position or a case, but consistency on the profile is what moves it.")],
    "trade_slug": "personal_injury_lawyers", "trade_plural": "personal injury lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
]
