"""Colony page specs for LOCKSMITHS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a locksmith-business owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, locksmith-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
percentages, or prices; hedge instead of overpromise; only the real prices ($299/$899/$2,500
plans, $1,500 one-time site) ever appear, and no locksmith service prices are invented; no
em/en dashes anywhere; never "leak" as a metaphor. Ethics: the AI does intake, triage,
scheduling, and an arrival window only, it never binds a price, and nothing here promises
security or safety, because no lock or locksmith can be guaranteed.

The locksmith reality drives every page: emergency lockouts (a person shut out of a car, a
house, or a business, often at night) where speed-to-answer is everything and the stranded
caller phones down the list until someone picks up, alongside planned work (rekeys, lock
installs, safes, commercial master-key systems) and the commercial and property-manager
accounts that are the real repeat-work engine. Trust matters because a customer is letting
someone defeat a lock and into their car, home, or business.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 locksmith-website-cost              (cost)     -> websites-seo-for-locksmiths
  2 locksmith-answering-service-cost    (cost)     -> ai-receptionist-for-locksmiths
  3 is-a-crm-worth-it-for-a-locksmith   (cost)     -> crm-for-locksmiths
  4 why-locksmiths-miss-calls           (problem)  -> ai-receptionist-for-locksmiths
  5 why-locksmith-leads-go-cold         (problem)  -> crm-for-locksmiths
  6 how-do-locksmiths-get-more-customers(how-to)   -> marketing-for-locksmiths
"""

TOPICS = [
# ==================== How Much Does a Locksmith Website Cost? (cost -> websites-seo) ====================
{
    "slug": "locksmith-website-cost",
    "h1": "How Much Does a Locksmith Website Cost?",
    "title": "How Much Does a Locksmith Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A locksmith website's real job is tap-to-call for a lockout and ranking for locksmith near me, not its price tag. Top Shelf builds yours for $1,500 one-time or free on a plan.",
    "answer": "A locksmith website can run from a couple hundred dollars for a template to several thousand for a custom build, but the price matters far less than whether it puts a tap-to-call button in front of someone locked out right now and ranks for locksmith near me. Top Shelf builds a custom site for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a locksmith website actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before you compare quotes, it helps to know what the site is for, because a locksmith website earns its keep in one specific moment. Someone is standing next to a car they cannot get into, or outside their own front door after dark, searching on a phone with one hand. The site that wins that customer is the one that loads fast and puts a way to reach you right in front of them, not the one with the prettiest homepage. What actually matters is a short list of things done well.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A tap-to-call button in front of the visitor before they scroll, because a stranded caller is not going to read, they are going to call.</li><li>Your service area and your services in plain sight: car lockouts, home lockouts, rekeys, lock installs, safes, and commercial work, so a caller knows in seconds you handle their problem.</li><li>Visible proof you are licensed, insured, and bonded, because a customer is about to let a stranger defeat a lock and needs a reason to trust yours.</li><li>Built to rank for the searches people actually make, like locksmith near me and 24 hour locksmith, so you show up when someone needs you now.</li></ul>'},
        {"h2_html": "What a locksmith should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Prices for a locksmith website swing from a couple hundred dollars for a template you fill in yourself to several thousand for a custom build, and the number on its own tells you very little. A do-it-yourself builder is cheap each month, but you do the work and it is rarely set up to rank or to convert a caller in a hurry. A one-time custom build is yours to keep, but a site alone does little if nobody is doing the ongoing work to get it found. The most expensive site of all is a beautiful one that never ranks and buries your number, because you paid for it and it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that answers the lockout",
    "bridge_text": "A locksmith website is only worth what it brings in. Ours is built to rank for the towns you cover and put tap-to-call in front of a stranded caller, then wired to follow up on every job it captures.",
    "bridge_slug": "websites-seo-for-locksmiths",
    "bridge_label": "Websites & SEO for locksmiths",
    "faqs": [
        ("Is a cheap template site good enough for a locksmith?",
         "It can get you online, but a template you fill in yourself is rarely built to rank for locksmith near me or to put tap-to-call in front of a stranded caller, and you do the work of maintaining it. If a site is not getting found or turning searches into calls, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "locksmiths", "trade_plural": "locksmiths",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ What Does a Locksmith Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "locksmith-answering-service-cost",
    "h1": "What Does a Locksmith Answering Service Cost?",
    "title": "What Does a Locksmith Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for locksmiths often bill per call or per minute, which climbs fast on a busy night. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for locksmiths usually bill per call, per minute, or on a retainer, so a busy night of lockouts gets expensive fast. Top Shelf takes a different route: an AI receptionist that answers every call 24/7 and books the job comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they handle, which sounds fair until a busy night turns into a big bill. A locksmith gets the most calls at the worst times for a live service: late nights, weekends, and the stretches when every stranded caller in town seems to phone at once, which is exactly when after-hours minutes tend to cost the most. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for every call answered, so a busy stretch or a run of price-shoppers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a rattled caller who needs calming, or a slow operator, costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when the lockouts are stacking up.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a person locked out of their car in a dark lot does not leave a voicemail, they call the next locksmith on the list. The real cost of no coverage is not a monthly fee, it is the after-hours lockout that went to the shop that picked up. But a generic call center reading a script cannot tell a car lockout from a commercial rekey, or a snapped key from a whole building that needs new locks, so you can pay for coverage and still get poor triage.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, triages the way you would, gives a realistic arrival window, and books the job or flags a true emergency to your phone. It handles the intake and the scheduling and leaves the pricing to you. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One late-night lockout you would have lost while your hands were full can be worth well more than the plan costs, and everything it catches after that is on top. It does not replace your judgment on a true emergency, it hands those straight to you.</p>'}],
    "bridge_h2": "Answer every lockout without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, tells a car lockout from a commercial rekey, and books it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-locksmiths",
    "bridge_label": "AI receptionist for locksmiths",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when the lockouts spike, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the after-hours lockout it books instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or holidays?",
         "No. It answers 24/7 as part of the plan, including the 2am car lockout and the holiday house lockout that are often your best-paying jobs, with no after-hours surcharge or overage.")],
    "trade_slug": "locksmiths", "trade_plural": "locksmiths",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============== Is a CRM Worth It for a Locksmith? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-locksmith",
    "h1": "Is a CRM Worth It for a Locksmith?",
    "title": "Is a CRM Worth It for a Locksmith? | Top Shelf Business Solutions",
    "meta_desc": "For most locksmiths a CRM pays for itself by rescuing one rekey quote or turning a one-time lockout into a standing account. It comes in Top Shelf's Signature plan at $899/mo, not a separate bill.",
    "answer": "For most locksmiths, yes, especially if you do repeat or commercial work. A CRM pays for itself the first time it wins back a rekey or install quote you would have let go cold, or turns a one-time lockout into a standing property-manager account. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a locksmith when you have more quotes and accounts than you can keep straight in your head, which is most shops that do any commercial or planned work on top of emergency lockouts. It is not worth it if you run purely one-off lockouts and never send a quote or serve the same customer twice, though that rarely stays true as you grow into rekeys, installs, and commercial accounts. The honest test is simple: how many rekey or install quotes have you sent in the last month that you never followed up on, and how many property managers or businesses did you help once and never contact again? Those are the jobs a CRM is built to bring back.</p>'},
        {"h2_html": "What it actually <em>earns a locksmith</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a locksmith is not the software, it is the repeat work that stops slipping away. A homeowner sitting on a bid to rekey the whole house, a property manager you let a tenant back in for once, a business that may want its locks changed after someone leaves: each one is a job you have already half-earned and are one follow-up away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open quote on a schedule, so a customer comparing locksmiths keeps hearing from you while the others go quiet.</li><li>It keeps every commercial account, building, and keyway in one place, so the turnover rekeys and lock changes come back to you instead of drifting to whoever was free.</li><li>It keeps your whole customer list and job history in one place instead of a truck full of paper and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: win back one standing account you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Turn one lockout into a standing account",
    "bridge_text": "The quotes and accounts you already have are the cheapest work you can get. A CRM follows up on every one for you, so the property manager you rekeyed once calls you next instead of the shop that stayed in touch.",
    "bridge_slug": "crm-for-locksmiths",
    "bridge_label": "CRM for locksmiths",
    "faqs": [
        ("Is a CRM overkill for a small locksmith business?",
         "Not usually. Even a one-person locksmith meets more property managers and sends more rekey and install quotes than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If quotes go cold and accounts forget your name, a CRM earns its keep."),
        ("How is a CRM different from keeping numbers in my phone?",
         "A phone full of contacts does not follow up on a quote, does not remember which building is due for a turnover rekey, and does not tell you which account has gone quiet. A CRM does all of that on a schedule, so the repeat work shows up instead of depending on you to remember.")],
    "trade_slug": "locksmiths", "trade_plural": "locksmiths",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do Locksmiths Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-locksmiths-miss-calls",
    "h1": "Why Do Locksmiths Miss So Many Calls?",
    "title": "Why Do Locksmiths Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Locksmiths miss calls because their hands are on a lock, a key cutter, or a fob, and a stranded caller does not leave a voicemail, they call the next locksmith on the list.",
    "answer": "You miss calls because they come when your hands are full, on a lock, a key cutter, or a fob programmer, or while you are driving to the last job, and a person locked out does not leave a voicemail. They hang up and call the next locksmith. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when your hands are <em>on a lock</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Locksmithing is a two-hands trade. When the phone rings you are often picking a lock, cutting a key, programming a fob, or working a safe, and none of those are things you can drop to take a call. The busier you are, the more calls you miss, which means your best days are also the ones where the most work slips away. It is not a discipline problem. One person cannot do the job in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a lockout it is not one. Someone stranded next to a car in a dark parking lot, or shut out of their home after dark, is not going to leave a message and wait. They move down the list until a real person answers, and by the time you check your phone, the job is already gone.</p>'},
        {"h2_html": "The calls you miss are your <em>best-paying calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A missed lockout, a car in a parking lot at night, a family shut out of the house, a shop owner stuck on the sidewalk before opening, is some of the highest-margin work you can get, and it comes when most other shops are closed too. Those after-hours calls are exactly the ones a customer will pay a premium for, and exactly the ones most likely to roll to voicemail. So the calls you are most likely to miss are also the ones worth the most.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can tell a real emergency from a call that can wait. A voicemail box cannot triage, and a generic call center does not know a car lockout from a mortise rekey. What actually works is something that answers on the first ring day or night, asks whether it is a car, a home, or a business, gets the location, gives a realistic arrival window, and either books the visit or flags a true emergency straight to your phone, so you decide whether to roll out without ever missing the call in the first place.</p>'}],
    "bridge_h2": "Stop losing lockouts to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, tells a car lockout from a routine rekey, and books it or flags it to you, so the lockout never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-locksmiths",
    "bridge_label": "AI receptionist for locksmiths",
    "faqs": [
        ("Would a stranded caller rather reach a real person?",
         "In a lockout, what a caller needs most is to know a real locksmith is on the way and roughly when, and a calm voice that captures the details and gives an arrival window beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, and hands true emergencies straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are picking a lock, working a safe, or already on another call. Something that always answers and triages is what catches the calls a forward would still miss.")],
    "trade_slug": "locksmiths", "trade_plural": "locksmiths",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do My Locksmith Leads Go Cold? (problem -> crm) ============
{
    "slug": "why-locksmith-leads-go-cold",
    "h1": "Why Do My Locksmith Leads Go Cold?",
    "title": "Why Do My Locksmith Leads Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most locksmith leads go cold not over price but because nobody followed up. The rekey bid or the account you served once went to whoever checked back in.",
    "answer": "Most locksmith leads go cold not because your price was wrong, but because nobody followed up. The homeowner sitting on a rekey bid, or the property manager you helped once, got busy, gathered other prices, or lost your number, and the job went to whoever checked back in. A quiet lead is usually a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "A cold lead is usually forgotten, not <em>lost on price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet quote as a no on price, so you drop it and move on. But most of the time the customer did not decide against you at all. They asked for a bid on rekeying the house, new locks for the business, or a master-key setup, meant to think it over, and then the next lockout call pulled you across town and yours slid down their pile. A week later they could not tell you the difference between the locksmiths who quoted them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The one who gets the job is usually not the cheapest. It is the one who stayed in front of them with a friendly check-in a few days later. The same is true of a commercial account: a property manager who used you once will keep calling whoever stays in touch, and drift to another locksmith the moment you go quiet. That second touch is what turns a maybe into booked work, and it is exactly the thing there is no time for between lockouts.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Locksmiths do not skip follow-up because they are lazy. They skip it because the day fills up. You finish a job, roll to the next, handle the lockout that jumped the line, and by evening the quote you sent that morning is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest quotes to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which quotes are still open and going cold.</li><li>The follow-up depends on you remembering, so it competes with the actual work and loses.</li><li>By the time you circle back, the customer has already booked whoever beat you to it.</li><li>The commercial account you served once quietly drifts to another locksmith because nobody stayed in touch.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open quote and every account gets a couple of timed check-ins automatically, written to sound like you, the customer comparing locksmiths keeps hearing from you while the others go silent, and the work you already earned stops slipping away.</p>'}],
    "bridge_h2": "Follow up on every quote and account, automatically",
    "bridge_text": "A CRM keeps every open quote and commercial account in front of you and sends timed check-ins for you, so a customer comparing locksmiths keeps hearing from you while the others go quiet.",
    "bridge_slug": "crm-for-locksmiths",
    "bridge_label": "CRM for locksmiths",
    "faqs": [
        ("How many times should I follow up on a locksmith quote?",
         "A couple of light touches over the first week or two catches most of the maybes without being pushy: a check-in a few days after the quote, then a short note answering common questions. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly check-in reads as attentive, not pushy, and most customers appreciate the nudge because they meant to get back to you and forgot. You can always jump in and message anyone directly.")],
    "trade_slug": "locksmiths", "trade_plural": "locksmiths",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Do Locksmiths Get More Customers? (how-to -> marketing) ========
{
    "slug": "how-do-locksmiths-get-more-customers",
    "h1": "How Do Locksmiths Get More Customers?",
    "title": "How Do Locksmiths Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Locksmiths get more customers by showing up for locksmith near me, which comes down to a complete Google profile and steady reviews, because it is a trust purchase.",
    "answer": "The fastest way is to show up the moment someone searches locksmith near me or 24 hour locksmith, which comes down to a complete, active Google Business Profile and a site built to rank. Reviews matter more for a locksmith than most trades, because a customer is choosing who to trust with their car, home, or business.",
    "sections": [
        {"h2_html": "Be the one they find when they are <em>locked out</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most locksmith customers do not go shopping in advance. They search in the moment, locked out of a car or a house, or a business owner who needs the locks changed today, and they pick from whatever comes up first. When someone searches for a locksmith near them, the first thing Google shows is the map pack: the little map with three local listings, star ratings, and a call button. Most people call one of those three without ever scrolling to the results below.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So getting more customers starts with being in those three, and that runs on your Google Business Profile more than your website: whether it is verified, complete, and active, how close you are to the searcher, and how many recent, genuine reviews you have. A great website with a neglected profile is a nice brochure almost nobody sees at the moment they are choosing who to call.</p>'},
        {"h2_html": "For a locksmith, trust does the <em>heavy lifting</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A locksmith is a trust purchase in a way most trades are not. A customer is about to let a stranger defeat a lock and get into their car, their home, or their business, so before they call they look hard for reasons to believe you are the right choice. That is why reviews and visible credentials do more for a locksmith than almost anything else you can do.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Ask every happy customer for an honest review at the moment the job is done, when the relief is highest, and make it a single tap.</li><li>Keep the profile active with real photos and posts, so it reads as a working business, not an abandoned listing.</li><li>Show that you are licensed, insured, and bonded, and name your service area plainly, so a nervous first-time caller has a reason to pick you.</li><li>Make sure both your emergency work and your planned work, car and home lockouts as well as rekeys, installs, and commercial jobs, show up in what you rank for.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this is a trick, and no honest company can promise you a specific spot on the map, because Google decides that. What moves it is doing these things steadily, so a neglected presence climbs over a few weeks and then compounds as the reviews build.</p>'}],
    "bridge_h2": "Get found the moment someone needs a locksmith",
    "bridge_text": "Most locksmith calls start with a search or the map pack. Keeping your Google profile verified, active, and full of recent reviews is how you show up there when someone is locked out nearby.",
    "bridge_slug": "marketing-for-locksmiths",
    "bridge_label": "Marketing for locksmiths",
    "faqs": [
        ("What is the fastest way for a locksmith to get more calls?",
         "Get into the map pack. When someone searches locksmith near me, Google shows three local listings first, and most callers pick from those. A verified, complete, active Google Business Profile with a steady stream of genuine reviews is the quickest way to show up there."),
        ("Do reviews really matter that much for a locksmith?",
         "Yes, more than for most trades, because it is a security purchase. A stranger is deciding who to trust with their car, home, or business, and recent, genuine reviews are often what tips that choice. Asking every happy customer at the right moment is how they build.")],
    "trade_slug": "locksmiths", "trade_plural": "locksmiths",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
