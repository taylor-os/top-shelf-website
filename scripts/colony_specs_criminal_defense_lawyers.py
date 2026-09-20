"""Colony page specs for CRIMINAL DEFENSE LAWYERS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a criminal defense firm owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, criminal-defense-specific substance (the generator owns
shell, schema, events, keyword placement). Same honesty rules as the money specs: no invented
stats, prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500
plans, $1,500 one-time site) ever appear; no em/en dashes anywhere; never "leak" as a metaphor.
Legal-ethics rules on top: never promise a case outcome, acquittal, or result; the AI receptionist
runs intake and booking, never legal advice; keep every claim attorney-advertising compliant.

Six questions, mixed cost / problem / how-to, spread across three money pages:
  1 criminal-defense-lawyer-website-cost              (cost)    -> websites-seo-for-criminal-defense-lawyers
  2 criminal-defense-answering-service-cost           (cost)    -> ai-receptionist-for-criminal-defense-lawyers
  3 is-a-crm-worth-it-criminal-defense                (cost)    -> crm-for-criminal-defense-lawyers
  4 why-criminal-defense-firms-miss-after-hours-calls (problem) -> ai-receptionist-for-criminal-defense-lawyers
  5 why-criminal-defense-leads-go-cold                (problem) -> crm-for-criminal-defense-lawyers
  6 how-do-criminal-defense-firms-get-more-clients    (how-to)  -> marketing-for-criminal-defense-lawyers
"""

TOPICS = [
# ========== How Much Does a Criminal Defense Lawyer Website Cost? (cost -> websites-seo) ==========
{
    "slug": "criminal-defense-lawyer-website-cost",
    "h1": "How Much Does a Criminal Defense Lawyer Website Cost?",
    "title": "How Much Does a Criminal Defense Lawyer Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A criminal defense lawyer website ranges from cheap templates to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A criminal defense lawyer website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more than the price is whether it ranks and turns a frightened searcher into a call. Top Shelf builds a custom five page site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number you see quoted for a criminal defense website swings widely because you are not all buying the same thing. A cheap template you fill in yourself and a custom site built to rank in your county and convert a frightened caller are different products with the same name. Before you weigh quotes, it helps to know what you are actually paying for.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A do-it-yourself website builder is cheap by the month, but you do the work, and it is rarely built to rank or to convince someone in a panic that your firm is the one to call.</li><li>A one-time custom build costs more up front and is yours to keep, but a site alone does little if nobody is doing the ongoing SEO to get it found when a person searches for a lawyer at midnight.</li><li>An agency retainer bundles the build with ongoing SEO and updates, which is where most of the long-term value lives, and also where the monthly cost lives.</li><li>Hidden costs to ask about before you sign: who owns the site, what a change costs, and whether you keep it if you leave.</li></ul>'},
        {"h2_html": "What a defense firm should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A criminal defense website earns its money one way: it turns a person who just searched for a lawyer, often frightened and often in the middle of the night, into a call on your phone. That means it has to load fast, rank for the county you practice in and the charges people search when they are in trouble, and put a tap-to-call button in front of a visitor before they scroll. A handsome site that never ranks and buries your number is the most expensive kind, because you paid for it and it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, and no site can promise a case result. A free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that earns its keep",
    "bridge_text": "A criminal defense website is only worth what it brings in. Ours is built to rank for the county you cover and turn a frightened search into a call, then wired to follow up on every one before the court date.",
    "bridge_slug": "websites-seo-for-criminal-defense-lawyers",
    "bridge_label": "Websites & SEO for criminal defense lawyers",
    "faqs": [
        ("Is a cheap template site good enough to start with?",
         "It can get you online, but a template you fill in yourself is rarely built to rank or to convince a frightened caller that your firm is the one to trust, and you do the upkeep. If a site is not getting found or turning searches into calls, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "criminal_defense_lawyers", "trade_plural": "criminal defense lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ======= What Does a Criminal Defense Answering Service Cost? (cost -> ai-receptionist) =======
{
    "slug": "criminal-defense-answering-service-cost",
    "h1": "What Does a Criminal Defense Answering Service Cost?",
    "title": "What Does a Criminal Defense Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for criminal defense firms often bill per call or minute, which adds up fast. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for criminal defense firms usually bill per call, per minute, or a monthly retainer, so a busy stretch gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call 24/7, stays calm with a frightened caller, and runs intake comes in the Signature plan at $899 flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy week turns into a big bill. A defense firm also gets its calls at the worst times for a live service: nights, weekends, and holidays, right after the arrests happen, when after-hours minutes tend to cost the most. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a run of calls after a busy weekend of arrests, wrong numbers and all, runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a frightened family member who needs a few minutes to calm down costs you more than a quick caller.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when the arrests are stacking up.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a person calling from a jail parking lot, or a spouse who just got the call, does not leave a voicemail. They dial the next firm on the list until someone picks up. The real cost of no coverage is not a monthly fee, it is the retained case that went to the firm that answered. But a generic call center reading a script cannot stay steady with a panicked caller or ask the questions a defense file needs, so you can pay for coverage and still get an intake that tells you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, stays calm, captures the charge, the county, and the custody and bond status, and either books the consultation or flags a true emergency to your on-call attorney. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One serious case you would have lost over a weekend can be worth well more than the plan costs, and everything it captures after that is on top. It never gives legal advice or discusses the charge, it answers, reassures, and hands the case to you.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, stays calm with a frightened family, runs your intake, and books the consultation, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-criminal-defense-lawyers",
    "bridge_label": "AI receptionist for criminal defense lawyers",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when the arrests stack up, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the after-hours case it captures instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or holidays?",
         "No. It answers 24/7 as part of the plan, including the late-night DWI and the weekend booking that are often your best cases, with no after-hours surcharge or overage.")],
    "trade_slug": "criminal_defense_lawyers", "trade_plural": "criminal defense lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Is a CRM Worth It for a Criminal Defense Firm? (cost -> crm) ============
{
    "slug": "is-a-crm-worth-it-criminal-defense",
    "h1": "Is a CRM Worth It for a Criminal Defense Firm?",
    "title": "Is a CRM Worth It for a Criminal Defense Firm? | Top Shelf Business Solutions",
    "meta_desc": "For most criminal defense firms a CRM pays for itself by rescuing one caller before their court date and keeping bondsmen warm. It comes in Top Shelf's Signature plan at $899/mo, not a separate bill.",
    "answer": "For most criminal defense firms, yes. A CRM pays for itself the first time it wins back a caller who would have retained someone else before their court date, or brings a past client back. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a criminal defense firm when you have more callers, clients, and referral sources than you can personally keep track of, which is most firms past the true solo stage. It is not worth it if you are a one-person shop taking a handful of matters and genuinely calling every caller and every bondsman back, though that rarely stays true as the calls grow. The honest test is simple: how many callers reached you, did not retain that day, and never heard from you again before their court date? And how many past clients and referring bondsmen have not heard from you in a year? Those are the cases a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a defense firm is not the software, it is the work that stops slipping away. A family sitting on a decision until they scrape together a retainer, a bondsman who sent you someone last spring, a past client who came out the other side grateful: each one is a case, or the source of one, that you have already half-earned and are one timely touch away from keeping.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every caller who has not retained on a clock tied to how close their court date is, so a family comparing firms keeps hearing from you while the others go quiet.</li><li>It keeps signed clients steady with an update before each setting, so a frightened client hears from you first instead of stewing and shopping around mid-case.</li><li>It keeps a light, scheduled touch on the bondsmen, past clients, and referring attorneys who send you work, so your name is first in mind the next time trouble finds someone they know.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one case you would have lost and it has paid for itself, and everything after that is margin. It runs the relationships around the file; your attorneys run the defense and make every call about the case.</p>'}],
    "bridge_h2": "Put your callers and sources to work",
    "bridge_text": "The callers who have not retained yet and the bondsmen who already send you work are the cheapest cases you can get. A CRM follows up on every one for you, so they come to your firm instead of the office that stayed in touch.",
    "bridge_slug": "crm-for-criminal-defense-lawyers",
    "bridge_label": "CRM for criminal defense lawyers",
    "faqs": [
        ("Is a CRM overkill for a small criminal defense firm?",
         "Not usually. Even a solo attorney fields more callers, clients, and referral sources than anyone can track by memory. The point is not size, it is whether follow-up is slipping. If callers retain elsewhere before their court date and bondsmen forget your name, a CRM earns its keep."),
        ("How is a CRM different from my case-management software?",
         "Your case-management software runs the legal file, the deadlines, and the discovery. A CRM works the people around it: the callers who have not retained, the clients who need reassurance between hearings, and the sources who refer you. The two sit side by side and do different jobs.")],
    "trade_slug": "criminal_defense_lawyers", "trade_plural": "criminal defense lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ====== Why Do Criminal Defense Firms Miss After-Hours Calls? (problem -> ai-receptionist) ======
{
    "slug": "why-criminal-defense-firms-miss-after-hours-calls",
    "h1": "Why Do Criminal Defense Firms Miss After-Hours Calls?",
    "title": "Why Do Criminal Defense Firms Miss After-Hours Calls? | Top Shelf Business Solutions",
    "meta_desc": "You miss after-hours calls because arrests happen at night while you are in trial or asleep, and a frightened family with someone in jail does not leave a voicemail, they call the next firm.",
    "answer": "Criminal defense firms miss after-hours calls because arrests happen at night and on weekends, when you are in trial, asleep, or with another client, and a frightened family member with someone in a jail cell does not leave a voicemail. They call the next firm. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Criminal work does not keep office hours. Arrests spike at night, over the weekend, and on holidays, and that is exactly when you are least able to answer, in trial prep, at a family dinner, at a jail meeting with another client, or asleep. The busier your practice, the more of these calls you miss, which means your strongest stretches are also when the most work slips past. It is not a discipline problem. One attorney cannot run a full docket and answer every call that comes in at 2am.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for someone whose husband was just booked it is not one. A person calling from a jail parking lot is not going to leave a message and wait until morning. They are frightened, they want a real voice now, and they keep dialing down the list until a person picks up. By the time you check your phone in the morning, the case is already gone, and you will never know it rang.</p>'},
        {"h2_html": "Missed after-hours calls are your most <em>expensive misses</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. The after-hours arrest call, a DWI, a domestic, a felony booking, is often the case that can carry your firm for months, and it comes when every other office is closed too. Those late-night calls are exactly the ones a frightened family will retain on the spot, and exactly the ones most likely to roll to voicemail. So the calls you are most likely to miss are also the ones worth the most. Miss enough of them and it is not a slow month you notice, it is the sense that the good cases always seem to land with the firm down the street.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can tell a case that cannot wait from a call that can. A voicemail box cannot run intake, and a generic call center does not know to ask which county is holding someone or whether bond has been set. What actually works is something that answers on the first ring day or night, stays calm, captures who was arrested, the charge, and the custody status, and either books the consultation or flags a true emergency straight to your on-call attorney, so you decide whether to act without ever missing the call in the first place.</p>'}],
    "bridge_h2": "Stop losing cases to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, stays calm with a frightened family, captures the intake, and books it or flags it to your on-call attorney, so the after-hours arrest never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-criminal-defense-lawyers",
    "bridge_label": "AI receptionist for criminal defense lawyers",
    "faqs": [
        ("Would a frightened caller rather reach a real person?",
         "In a crisis, what a family needs most is to know a real firm is handling it, and a calm voice that captures the details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, gives no legal advice, and hands true emergencies straight to your on-call attorney."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when you can pick up. Forwarding still rolls to voicemail when you are in trial, asleep, or already on another call. Something that always answers and runs intake is what catches the cases a forward would still miss.")],
    "trade_slug": "criminal_defense_lawyers", "trade_plural": "criminal defense lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Why Do Criminal Defense Leads Go Cold? (problem -> crm) ============
{
    "slug": "why-criminal-defense-leads-go-cold",
    "h1": "Why Do Criminal Defense Leads Go Cold?",
    "title": "Why Do Criminal Defense Leads Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most criminal defense leads go cold not over your fee but because nobody followed up before the court date. The caller retained whoever circled back in time.",
    "answer": "Most criminal defense leads go cold not because your fee was wrong, but because nobody followed up before the court date. The caller was gathering a retainer or calling other firms, and retained whoever circled back in time. A lead that goes quiet is usually not a no, it is a decision that has not been made yet.",
    "sections": [
        {"h2_html": "Silence usually means still deciding, not <em>gone</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet caller as a no on your fee, so you drop it and move on. But most of the time the person did not decide against you at all. They called after an arrest, meant to retain once they had the money together or had heard from a bondsman, and then the days slid by. They are juggling two other firms they called that night, a court date bearing down, and more fear than they can think straight through, and your call slid down the pile. A few days later they could not tell you apart from the other lawyers they spoke to.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The firm that gets retained is usually not the cheapest. It is the one that stayed in front of them: a calm check-in a day or two later, a short note before the arraignment. That second touch is what turns a maybe into a signed retainer, and it is exactly the thing there is no time for when your own week is full of hearings for other clients.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Defense attorneys do not skip follow-up because they are careless. They skip it because the day fills up. You are in court all morning, meeting a client at the jail in the afternoon, and by evening the family who called Monday is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when the fewest new callers are coming in.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system flagging which callers have not retained and how close their court date is.</li><li>The follow-up depends on you remembering, so it competes with active cases and loses.</li><li>By the time you circle back, the caller has already retained a firm that reached them first.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every caller who has not retained gets a couple of timed check-ins tied to their court date, written to sound like your firm, the family comparing firms keeps hearing from you while the others go silent, and the cases you already earned the call on stop slipping away.</p>'}],
    "bridge_h2": "Follow up before the court date, automatically",
    "bridge_text": "A CRM keeps every caller who has not retained in front of you and sends timed check-ins tied to their court date, so a family comparing firms keeps hearing from you while the other lawyers go quiet.",
    "bridge_slug": "crm-for-criminal-defense-lawyers",
    "bridge_label": "CRM for criminal defense lawyers",
    "faqs": [
        ("How many times should I follow up with a caller who has not retained?",
         "A couple of light touches in the days before their court date catches most of the maybes without being pushy: a check-in a day or two after the call, then a short note as the setting approaches. The key is that it happens at all and in time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like your firm and sent at a sensible pace. A short, steady check-in reads as attentive, not pushy, and a frightened family usually welcomes hearing that a real firm is still there. You can always step in and message anyone directly.")],
    "trade_slug": "criminal_defense_lawyers", "trade_plural": "criminal defense lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ========== How Do Criminal Defense Firms Get More Clients? (how-to -> marketing) ==========
{
    "slug": "how-do-criminal-defense-firms-get-more-clients",
    "h1": "How Do Criminal Defense Firms Get More Clients?",
    "title": "How Do Criminal Defense Firms Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "Criminal defense firms get more clients by being easy to find and trust the moment someone is arrested, when a frightened person searches for a lawyer and retains whoever shows up first.",
    "answer": "Criminal defense firms get more clients by being easy to find and easy to trust the moment someone is arrested. Most clients are not shopping ahead, they search for a lawyer in a panic and retain one of the first firms that shows up and looks credible. Getting more clients starts with being visible and trusted exactly then.",
    "sections": [
        {"h2_html": "Clients find you at the <em>worst moment of their life</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A criminal defense client is almost never planning ahead. Nobody keeps a lawyer on hand in case they are arrested. The search happens the instant it goes wrong, from a phone, often late at night, run by the person in custody or by a spouse or parent who just got the call and does not know what a bond hearing even is. They are frightened, ashamed, and in a hurry, and they choose from the firms that show up first and look like they can be trusted with the worst night of their life.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That changes what getting more clients means. You are not building a brand people admire over years. You are making sure that at the exact moment a frightened person types criminal defense lawyer into their phone, your firm is one of the few they see, and that what they see makes them feel they can pick up and call you. Speed and trust are what get a firm hired here, not the lowest price.</p>'},
        {"h2_html": "The channels that actually <em>bring in cases</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting found and getting chosen come down to a handful of things done consistently, not one clever trick. Each one puts your firm in front of the frightened searcher and gives them a reason to trust you over the office next to you on the results page.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Show up on Google for your area and the charges you defend, both in the map pack at the top and in the results below it, because that is where the panicked search starts.</li><li>Build a steady stream of genuine reviews, since trust is the whole decision for someone handing their freedom to a stranger, and reply to every one.</li><li>Keep a fast, credible website that loads on a phone and makes it easy to call, so the visibility you earn turns into calls instead of bounces.</li><li>Stay in front of the bondsmen, past clients, and other attorneys who send you cases, so referrals keep coming while the search traffic builds.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this promises a specific ranking or a specific number of new clients, because no one controls Google and no honest firm guarantees an outcome. What it does is make you findable and credible at the moment people decide, done steadily so it compounds. A free audit can show you where your firm stands on each of these before you change anything.</p>'}],
    "bridge_h2": "Get found where the cases start",
    "bridge_text": "Most criminal defense clients start with a panicked search after an arrest. Marketing that keeps you visible on Google, full of genuine reviews, and in front of your referral sources is how you get chosen at that moment.",
    "bridge_slug": "marketing-for-criminal-defense-lawyers",
    "bridge_label": "Marketing for criminal defense lawyers",
    "faqs": [
        ("What is the fastest way to get more criminal defense clients?",
         "Being visible and credible at the moment of the search. That usually means getting into the Google map pack for your area, keeping a steady flow of genuine reviews, and having a site that earns trust fast. No one controls Google, so no honest company promises a specific rank or a set number of clients."),
        ("Do reviews really matter for a criminal defense firm?",
         "They carry a lot of weight. Someone deciding who to trust with their freedom reads reviews closely, and a steady stream of genuine ones reassures the next frightened caller more than anything you can say about yourself. Ask every client you can honestly ask, and never buy or filter reviews.")],
    "trade_slug": "criminal_defense_lawyers", "trade_plural": "criminal defense lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
]
