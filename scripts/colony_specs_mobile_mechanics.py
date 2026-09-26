"""Colony page specs for MOBILE MECHANICS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a mobile-mechanic owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, mobile-mechanic-specific substance (the generator owns
shell, schema, events, keyword placement). The whole angle is the come-to-you reality that makes a
mobile mechanic different from a fixed shop: NO shop, so the Google Business Profile and the website
ARE the entire storefront (no walk-in traffic, no building to drive past); the pitch is convenience,
the repair done at the customer home or work with no tow needed, and the trust of a stranger letting
someone work on their car in their own driveway; the mechanic is literally under a car when the next
call comes, so missed calls are guaranteed without coverage; service radius and travel matter; and
repeat plus referral work is the moat.

Same honesty rules as the money specs: no invented stats, percentages, or clients; hedge instead of
overpromise; only the real prices ($299 and $899 monthly plans, $1,500 one-time site) ever appear;
no em/en dashes anywhere; never "leak" as a money metaphor (a literal oil leak is fine). ETHICS:
the AI receptionist does intake and scheduling ONLY, it never diagnoses the car or quotes the repair,
and nothing here guarantees a repair outcome.

Six questions, mixed cost / problem / how-to, spread across three money pages:
  1 mobile-mechanic-website-cost               (cost)    -> websites-seo-for-mobile-mechanics
  2 mobile-mechanic-answering-service-cost     (cost)    -> ai-receptionist-for-mobile-mechanics
  3 is-a-crm-worth-it-for-a-mobile-mechanic    (cost)    -> crm-for-mobile-mechanics
  4 why-mobile-mechanics-miss-calls            (problem) -> ai-receptionist-for-mobile-mechanics
  5 why-mobile-mechanic-leads-go-cold          (problem) -> crm-for-mobile-mechanics
  6 how-do-mobile-mechanics-get-more-customers (how-to)  -> marketing-for-mobile-mechanics
"""

TOPICS = [
# ============ How Much Does a Mobile Mechanic Website Cost? (cost -> websites-seo) ============
{
    "slug": "mobile-mechanic-website-cost",
    "h1": "How Much Does a Mobile Mechanic Website Cost?",
    "title": "How Much Does a Mobile Mechanic Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A mobile mechanic has no shop, so the website and Google profile are the whole storefront. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A mobile mechanic website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. But because you have no shop, the site and your Google profile are your entire storefront, so what matters is whether it wins the job. Top Shelf builds one for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "Your website is your only <em>storefront</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A fixed shop has a building, a sign on the road, and people walking in or driving past it every day. A mobile mechanic has none of that. There is no storefront to find, no window to notice, and no lot to pull into. That means your website and your Google Business Profile are the entire storefront, and almost every customer you get meets your business there first. So the site has to do the job a building does for a shop. It has to show the area you cover, so a driver knows you will actually come to them. It has to say plainly what you fix on-site, in a driveway, a parking lot, or at their place of work, so they know a mobile visit is even possible for their problem. It has to let them book a visit without a phone call. And it has to carry the reviews that make a stranger comfortable letting you work on their car at their home. Get those right and the price of the site stops being the real question. A cheap site that does none of them is the expensive one, because it is the only storefront you have and it is quietly turning people away.</p>'},
        {"h2_html": "What a mobile mechanic should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number you see quoted for a mobile mechanic website swings widely, because a template you fill in yourself and a custom site built to get found are different products with the same name. But for a come-to-you business the real test is narrow. Does it show up when someone nearby searches for a mobile mechanic, and does it turn that visitor into a booked visit before they call the next name on the list. A site that looks fine but never ranks and hides your number is the costly one, because you paid for it and it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps the pricing simple. A custom five page site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing work of getting it ranked is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site and profile stand first.</p>'}],
    "bridge_h2": "Make the only storefront you have earn its keep",
    "bridge_text": "With no shop, your website and profile are the whole storefront. Ours is built to get found for the area you cover and turn a search into a booked visit, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-mobile-mechanics",
    "bridge_label": "Websites & SEO for mobile mechanics",
    "faqs": [
        ("Do I even need a website if I have a Google Business Profile?",
         "Yes. The profile is what gets you into the map when someone searches, but a driver deciding whether to let you work on their car in their driveway wants to see the area you cover, what you fix on-site, and real reviews, and that is what the website carries. The two work together, and with no shop they are the whole storefront."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep. On a monthly plan the site is built for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "mobile_mechanics", "trade_plural": "mobile mechanics",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ======= What Does a Mobile Mechanic Answering Service Cost? (cost -> ai-receptionist) =======
{
    "slug": "mobile-mechanic-answering-service-cost",
    "h1": "What Does a Mobile Mechanic Answering Service Cost?",
    "title": "What Does a Mobile Mechanic Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 and books the visit in the Signature plan at $899/mo.",
    "answer": "Traditional answering services usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call while you are under a car, takes the details, and books the visit comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. A mobile mechanic gets the most calls at the worst possible moment for answering one, flat on your back under a car in a driveway, with no helper and no free hand. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a run of tire-kickers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty caller or a slow operator costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple. A driver whose car will not start does not leave a voicemail. They call the next mobile mechanic, and the one after that, or they give up and call a tow truck to haul the car to a shop, the exact trip they called you to avoid. The real cost of no coverage is not a monthly fee, it is the job that went to whoever picked up. But a generic call center reading a script cannot take the details a mobile job actually needs, so you can pay for coverage and still get a useless message.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, asks the questions you set, whether the car will start or move, whether it is safe where it sits, and where it is, then captures the address and the symptom, checks it against the area you cover, and books the visit or flags a true roadside emergency to your phone. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. It handles the intake and the scheduling only. It does not diagnose the car or price the repair, and it makes no promises about the fix, so those calls stay with you. One job you would have lost to voicemail can be worth more than the plan costs for months, and everything it books after that is on top.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7 even while you are under a car, takes the address and symptom, and books the visit, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-mobile-mechanics",
    "bridge_label": "AI receptionist for mobile mechanics",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the stranded driver it books instead of losing to voicemail while your hands are under a car."),
        ("Does it diagnose the car or quote the repair?",
         "No. It handles the intake and the booking only. It answers the call, reassures the driver, asks the questions you set, captures the address and the symptom, and gets the visit on your calendar. It does not diagnose the problem or price the work, and it makes no promises about the fix. Those stay with you.")],
    "trade_slug": "mobile_mechanics", "trade_plural": "mobile mechanics",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============== Is a CRM Worth It for a Mobile Mechanic? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-mobile-mechanic",
    "h1": "Is a CRM Worth It for a Mobile Mechanic?",
    "title": "Is a CRM Worth It for a Mobile Mechanic? | Top Shelf Business Solutions",
    "meta_desc": "For most mobile mechanics a CRM pays for itself by reviving one quote given in a driveway and bringing past customers back. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most mobile mechanics, yes. A CRM pays for itself the first time it wins back a repair you quoted in a driveway, or brings a past customer back for the next job. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a mobile mechanic when you have more open quotes and past customers than you can keep track of from the road, which is most operators past their first year. It is not worth it if you are doing a handful of jobs a week and genuinely calling everyone back, though that rarely stays true as word gets around and the repeat work builds. The honest test is simple. How many repairs have you quoted in a driveway in the last month that you never circled back on, and how many past customers have not heard from you in a year. Those are the jobs a CRM is built to bring back, and for a come-to-you business there are usually more of them than you would guess, because the follow-up either happens from a truck between stops or it does not happen at all.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a mobile mechanic is not the software, it is the work that stops slipping away. A driver sitting on a brake quote, a family whose alternator you replaced two years ago, a car that is due for an oil change, each one is a job you have already half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open quote on a schedule, so a driver comparing a couple of mechanics keeps hearing from you while the others go quiet.</li><li>It fires service reminders, an oil change by months or mileage, a brake check, a state inspection before it lapses, so recurring work comes back without you tracking a single date from the road.</li><li>It keeps your whole customer list, their addresses, and their vehicles in one place instead of a truck full of texts, receipts, and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The come-to-you convenience is the strongest repeat hook in the trade, and it only pays off if you stay in touch. A driver who learned they can get the car fixed in their own driveway rarely goes back to a shop, so that first job can turn into years of work. At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. Recover one job you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your customer list to work",
    "bridge_text": "The drivers you already fixed are the cheapest jobs you can get. A CRM follows up on every quote and reminds them when a car is due, so they call you next instead of the mechanic who stayed in touch.",
    "bridge_slug": "crm-for-mobile-mechanics",
    "bridge_label": "CRM for mobile mechanics",
    "faqs": [
        ("Is a CRM overkill for a one-person mobile operation?",
         "Not usually. Even a solo mobile mechanic services more cars and quotes more repairs than anyone can track by memory from the road. The point is not the size of the operation, it is whether follow-up is falling through. If quotes go cold and past customers forget your name, a CRM earns its keep."),
        ("How is a CRM different from keeping numbers in my phone?",
         "A phone full of contacts does not follow up on a quote, does not remember whose car is due for service, and does not tell you which job is going cold. A CRM does all of that on a schedule, so the repeat and deferred work shows up instead of depending on you to remember it between stops.")],
    "trade_slug": "mobile_mechanics", "trade_plural": "mobile mechanics",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Why Do Mobile Mechanics Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-mobile-mechanics-miss-calls",
    "h1": "Why Do Mobile Mechanics Miss So Many Calls?",
    "title": "Why Do Mobile Mechanics Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Mobile mechanics miss calls because they ring while you are under a car at a customer's house, and a stranded driver does not leave a voicemail, they call the next mechanic.",
    "answer": "Mobile mechanics miss calls because they come while your hands are full under a car in someone's driveway, with no helper and no free hand. A stranded driver does not leave a voicemail; they call the next mechanic or give up and call a tow. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes while you are <em>under a car</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A mobile mechanic is a one-person, hands-full job. When the phone rings you are flat on your back under a car in a driveway, greasy to the elbows, or crouched next to a no-start in a parking lot. There is no counter, no helper, and no free hand, so the call goes to voicemail. The busier you are, the more calls you miss, which means your best days are also the ones where the most work slips away. It is not a discipline problem. One person cannot do the job in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a driver stuck with a car that will not start it is not one. They are not going to leave a message and wait to hear back. They move down the list until someone answers, and by the time you slide out from under the car and check your phone, the job is already gone.</p>'},
        {"h2_html": "A stranded driver just calls the <em>next mechanic</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When you do not pick up, the driver does not wait around. They call the next mobile mechanic on the list, then the one after that, until someone answers, or they give up and call a tow truck to take the car to a shop, which is the exact trip they were trying to avoid by calling you. So the call you miss is not a lost message. It is a booked job that went to whoever happened to be free to talk while your hands were on a car.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can take the details a mobile job needs. A voicemail box cannot reassure a stranded driver or write down an address, and a generic call center does not know what to ask. What actually works is something that answers on the first ring, day or night, asks whether the car will start or move at all, gets the address and the symptom, checks it against the area you cover, and either books the visit or flags a true roadside emergency to your phone. It handles the intake and the booking only. It does not diagnose the car or quote the repair, so those decisions stay with you, and you never miss the call in the first place.</p>'}],
    "bridge_h2": "Stop losing jobs to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, even while you are under a car, takes the address and symptom, and books the visit or flags it to you, so the job never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-mobile-mechanics",
    "bridge_label": "AI receptionist for mobile mechanics",
    "faqs": [
        ("Would a customer rather reach a real person?",
         "When a car will not start, what a driver needs most is to know a real mechanic is coming, and a calm voice that captures the address and the problem beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the details, and hands the real decisions straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are under a car, on a ladder, or already on another job. Something that always answers and takes the details is what catches the calls a forward would still miss.")],
    "trade_slug": "mobile_mechanics", "trade_plural": "mobile mechanics",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Why Do My Mobile Mechanic Leads Go Cold? (problem -> crm) ============
{
    "slug": "why-mobile-mechanic-leads-go-cold",
    "h1": "Why Do My Mobile Mechanic Leads Go Cold?",
    "title": "Why Do My Mobile Mechanic Leads Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most mobile mechanic leads go cold not over price but because nobody followed up. The driver meant to think it over, and the repair went to whoever checked back in.",
    "answer": "Most mobile mechanic leads go cold not because your price was wrong, but because nobody followed up. You quoted the repair on the spot, the driver wanted to wait for payday or check a shop, and then you drove to the next job. A lead that goes quiet is usually a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "Quiet usually means forgotten, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet quote as a no on price, so you drop it and move on. But most of the time the driver did not decide against you at all. You got to the car, found the fault, and gave a price for the alternator or the brakes on the spot, and because it was more than they hoped, they said they wanted to think about it, wait for payday, or check what a shop would charge. Then you were off to the next job across town. A week later they could not tell you apart from the other mechanic who came out.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The one who gets the job is usually not the cheapest. It is the one who stayed in front of them, a friendly check-in a few days later, a quick note answering the question they were stuck on. That second touch is what turns a maybe into a booked repair, and it is exactly the thing there is no time for from the road between stops.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Mobile mechanics do not skip follow-up because they are lazy. They skip it because the day fills up. You finish a job in one driveway, drive across town to the next, handle the no-start that jumped the line, and by evening the brake quote you gave on Tuesday is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest quotes to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which quotes are still open and quietly going cold.</li><li>The follow-up depends on you remembering, so it competes with the actual work and loses.</li><li>By the time you circle back, the driver has already booked whoever beat you to it.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open quote gets a couple of timed check-ins automatically, written to sound like you, the driver comparing mechanics keeps hearing from you while the others go silent, and the repairs you already quoted stop slipping away to a shop.</p>'}],
    "bridge_h2": "Follow up on every quote, automatically",
    "bridge_text": "A CRM keeps every driveway quote in front of you and sends timed check-ins for you, so a driver weighing a repair keeps hearing from you while the other mechanics go quiet.",
    "bridge_slug": "crm-for-mobile-mechanics",
    "bridge_label": "CRM for mobile mechanics",
    "faqs": [
        ("How many times should I follow up on a repair quote?",
         "A couple of light touches over the first week or two catches most of the maybes without being pushy, a check-in a few days after the quote, then a short note a bit later. The key is that it happens at all and on time, which is what a CRM handles for you while you are on a job."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly check-in reads as attentive, not pushy, and most drivers appreciate the nudge because they meant to get back to you and forgot. You can always jump in and message anyone directly.")],
    "trade_slug": "mobile_mechanics", "trade_plural": "mobile mechanics",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ======== How Do Mobile Mechanics Get More Customers? (how-to -> marketing) ========
{
    "slug": "how-do-mobile-mechanics-get-more-customers",
    "h1": "How Do Mobile Mechanics Get More Customers?",
    "title": "How Do Mobile Mechanics Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Mobile mechanics get more customers by being found where drivers search and turning every driveway job into repeat and referral work. With no shop, your profile and reviews carry it.",
    "answer": "Mobile mechanics get more customers two ways: by being easy to find when a driver searches for one nearby, and by turning every driveway job into repeat and referral work. With no shop and no walk-in traffic, your Google Business Profile, website, and reviews do the job a storefront would, and staying in touch keeps past customers coming back.",
    "sections": [
        {"h2_html": "With no shop, you get found on <em>Google or not at all</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A fixed shop pulls in people who walk by, drive past the sign, or have known the place for years. A mobile mechanic has none of that. There is no building, no foot traffic, and no window on a busy road. So almost every new customer finds you the same way, by searching for a mobile mechanic near them, and the first thing Google shows is the map pack, the little map with three local listings, star ratings, and a call button. Most people choose from those three without scrolling further. If your Google Business Profile is incomplete, unverified, or short on recent reviews, you sit below the mechanics who keep theirs active, no matter how good your work is. Getting into that map pack runs on the profile, whether it is verified and complete, how close you are to the searcher, and how many genuine, recent reviews you have. Those reviews do double duty for a come-to-you business, because a stranger deciding whether to let you work on their car in their own driveway leans on them harder than a shop walk-in ever would.</p>'},
        {"h2_html": "Turn one driveway job into <em>years of work</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting found is only half of it. The cheapest customer is the one you already have, and a mobile mechanic has the strongest repeat hook in the trade. A driver who found out they can get the car fixed in their own driveway rarely wants to go back to arranging a ride and sitting in a waiting room. The next oil change, the next brake job, the next no-start is yours if you stay in front of them.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Ask every happy customer for a review the moment the car is running again, and make it one tap, so the profile that gets you found keeps growing.</li><li>Stay in touch with past customers on a schedule, a service reminder or a seasonal note, so they do not lose your number and call whoever they stumble onto next.</li><li>Make it easy for them to refer you, because a driver who loved the convenience will mention you to the other multi-car households on the street.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this promises a spot on the map, because no one controls Google. But being easy to find, well reviewed, and in steady touch with the customers you already earned is what actually grows a come-to-you business over time. A free audit can show you where you stand today and which of these is costing you the most work.</p>'}],
    "bridge_h2": "Get found, and stay found",
    "bridge_text": "Most mobile mechanic customers start on Google and come back if you stay in touch. Keeping your profile active and full of reviews, then following up with past customers, is how a come-to-you business grows.",
    "bridge_slug": "marketing-for-mobile-mechanics",
    "bridge_label": "Marketing for mobile mechanics",
    "faqs": [
        ("Do I need a shop or a street address to get more customers?",
         "No, but you do need to be findable. With no walk-in traffic, your Google Business Profile and your reviews are your storefront, and a verified, active, well-reviewed profile is what puts you in front of drivers searching nearby. A service-area business can show the area it covers without publishing a storefront address."),
        ("How long until I see more customers?",
         "A neglected profile that gets verified, completed, and active can start climbing within a few weeks, and it compounds as reviews and steady contact build. Nobody controls Google, so no honest company promises a specific position or a number of new customers, but consistency is what moves it.")],
    "trade_slug": "mobile_mechanics", "trade_plural": "mobile mechanics",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
]
