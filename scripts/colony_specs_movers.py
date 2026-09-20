"""Colony page specs for MOVERS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a moving-company owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, mover-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real Top Shelf prices ($299/$899/$2,500
plans, $1,500 one-time site) ever appear, and NEVER an invented moving price; no em/en dashes
anywhere; never "leak" as a money metaphor. The AI does scheduling and intake only, it never
binds a moving quote.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 mover-website-cost                      (cost)     -> websites-seo-for-movers
  2 moving-company-answering-service-cost   (cost)     -> ai-receptionist-for-movers
  3 is-a-crm-worth-it-for-a-moving-company  (cost)     -> crm-for-movers
  4 why-movers-miss-calls                   (problem)  -> ai-receptionist-for-movers
  5 why-moving-estimates-go-cold            (problem)  -> crm-for-movers
  6 how-do-movers-get-more-customers        (how-to)   -> marketing-for-movers
"""

TOPICS = [
# ==================== How Much Does a Moving Company Website Cost? (cost -> websites-seo) ====================
{
    "slug": "mover-website-cost",
    "h1": "How Much Does a Moving Company Website Cost?",
    "title": "How Much Does a Moving Company Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A moving company website ranges from a cheap template to a custom build. What matters is whether it wins the estimate. Top Shelf builds yours for $1,500, or free on any monthly plan.",
    "answer": "A moving company website can run from a couple hundred dollars for a template to several thousand for a custom build. What matters more than the sticker price is whether it wins the estimate request over the movers a family is calling. Top Shelf builds a custom site for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a moving website actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone planning a move is on your site for one reason: to decide whether to trust your crew with everything they own, and then to ask for a price. A moving website earns its money by making that easy in the first few seconds, not by looking pretty. Before you compare quotes for a build, it helps to know what the site actually has to accomplish.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Put a request for an in-home or virtual estimate front and center, so a ready customer never has to hunt for how to reach you.</li><li>Earn trust fast: licensed and insured, years in business, and real photos of your crew and trucks, because a stranger is deciding who to let into their home.</li><li>Show up when someone searches for a mover near them and for the towns you cover, since a site nobody finds brings you nothing.</li><li>Lead with reviews, the one thing a nervous customer checks before handing over their belongings.</li><li>Load fast on a phone, where most of these searches happen, often at the last minute before a move.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A beautiful site that never ranks, hides the estimate request, and buries your reviews is the most expensive kind, because you paid for it and it still sends the move to the company whose site made booking easy.</p>'},
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number you get quoted swings widely because a website can mean very different things. A cheap builder you fill in yourself is inexpensive month to month, but you do the work, and it is rarely built to rank or to turn a nervous shopper into a booked estimate. A build made to get found in your area, put the estimate request first, and keep collecting reviews costs more, and the ongoing SEO that keeps it ranking is where much of the long-term value lives. Before you sign anything, ask who owns the site, what a change costs, and whether you keep it if you leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it found is handled for you. There is no setup fee either way. No honest company can promise a specific ranking by a specific date, because nobody controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that wins the estimate",
    "bridge_text": "A moving website is only worth the moves it books. Ours is built to rank for the towns you cover, put the estimate request first, and turn a nervous shopper into a booked move.",
    "bridge_slug": "websites-seo-for-movers",
    "bridge_label": "Websites & SEO for movers",
    "faqs": [
        ("Is a cheap template site good enough for a moving company?",
         "It can get you online, but a template you fill in yourself is rarely built to rank when someone searches for a mover near them, or to turn a nervous shopper into a booked estimate, and you do the upkeep. If a site is not getting found or winning the estimate request, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "movers", "trade_plural": "movers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ What Does a Moving Company Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "moving-company-answering-service-cost",
    "h1": "What Does a Moving Company Answering Service Cost?",
    "title": "What Does a Moving Company Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for movers often bill per call or per minute, which climbs in your busy season. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for movers usually bill per call, per minute, or on a monthly retainer, so your busiest season runs up the biggest bill. Top Shelf takes a different approach: an AI receptionist that answers every quote call 24/7 and books the estimate comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until your busy season turns into a big bill. A mover also gets slammed with calls at the worst times to answer them: the end-of-month crunch, the summer stretch, and the packed Saturdays when every crew you have is already on a truck. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy month or a wave of price-shoppers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, and a move has a lot to go over, where from, where to, size, stairs, packing, and dates, so those calls are rarely short.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right in peak season.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a family with a lease ending Monday does not leave a voicemail, they call the next mover on their list, and the deposit that would have held their date goes with them. The real cost of no coverage is not a monthly fee, it is the booked weekend that went to the company that picked up. But a generic call center reading a script cannot tell a studio apartment from a four-bedroom house, or a quick local move from a long-distance haul, so you can pay for coverage and still get useless notes.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, asks what you would ask, where from, where to, how big, stairs or an elevator, packing, and the date, and books the in-home or virtual estimate on your calendar. It never guesses at a price or binds a quote, it captures the move and leaves the number to you. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One full-house move you would have lost on a Saturday can be worth well more than the plan costs, and everything it catches after that is on top.</p>'}],
    "bridge_h2": "Answer every quote call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, gathers the whole move, and books the estimate, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-movers",
    "bridge_label": "AI receptionist for movers",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when your season peaks, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the booked move it captures instead of losing to voicemail."),
        ("Does it cost extra for the summer rush, weekends, or after hours?",
         "No. It answers 24/7 as part of the plan, including the packed Saturdays and the end-of-month crunch that are often your best-booking days, with no after-hours surcharge or overage.")],
    "trade_slug": "movers", "trade_plural": "movers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============== Is a CRM Worth It for a Moving Company? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-moving-company",
    "h1": "Is a CRM Worth It for a Moving Company?",
    "title": "Is a CRM Worth It for a Moving Company? | Top Shelf Business Solutions",
    "meta_desc": "For most movers a CRM pays for itself by rescuing an estimate that went cold and bringing past customers back for the next move. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most moving companies, yes. A CRM pays for itself the first time it wins back an estimate you would have let go cold, or brings a past customer back for their next move. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a moving company when you are giving more estimates and have moved more families than you can personally keep track of, which is most established outfits. It is not worth it if you are one truck doing a couple of jobs a week and genuinely calling everyone back, though that rarely stays true as you grow. The honest test is simple: how many estimates did you give last month that never got a second touch, and how many families you have moved have not heard from you since the truck pulled away? Those are the moves a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a mover is not the software, it is the work that stops slipping through. A family sitting on your estimate while they gather two more, a customer you moved two years ago who is ready for a bigger place, a happy customer who would gladly refer you: each one is a move you have half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open estimate on a schedule, so a family comparing three movers keeps hearing from you while the other two go quiet.</li><li>It flags past customers who moved a year or two back and are due to move again, so repeat work comes back without you tracking dates.</li><li>It sends thank-you and referral asks after a move while the good experience is still fresh, and keeps your whole customer list and move history in one place instead of a stack of paper estimates.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one move you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your customer list to work",
    "bridge_text": "The estimates and past customers you already have are the cheapest moves you can book. A CRM follows up on every one for you, so they call you next instead of the company that stayed in touch.",
    "bridge_slug": "crm-for-movers",
    "bridge_label": "CRM for movers",
    "faqs": [
        ("Is a CRM overkill for a small moving company?",
         "Not usually. Even a one or two truck outfit gives more estimates and moves more families than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If estimates go cold and past customers forget your name, a CRM earns its keep."),
        ("How is a CRM different from keeping numbers in my phone?",
         "A phone full of contacts does not follow up on an estimate, does not remember who is due to move again, and does not tell you which move is going cold. A CRM does all of that on a schedule, so the repeat work shows up instead of depending on you to remember.")],
    "trade_slug": "movers", "trade_plural": "movers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do Movers Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-movers-miss-calls",
    "h1": "Why Do Movers Miss So Many Calls?",
    "title": "Why Do Movers Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Movers miss calls because the whole crew is on a truck when the phone rings, and a family with a move-out date does not leave a voicemail, they book the mover who answered.",
    "answer": "Movers miss calls because the calls come when the whole crew is on a truck, wrapping furniture or driving to the next job, and a family with a hard move-out date does not leave a voicemail. They call the next mover on the list. The fix is not working harder, it is making sure every quote call gets answered.",
    "sections": [
        {"h2_html": "The call comes when your whole crew is <em>on a truck</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Moving is a hands-full trade from the first load to the last. When the phone rings, your crew is carrying a couch down three flights, wrapping a dresser, or driving to the next stop, and none of those are moments anyone can stop and take a quote call. The busier you are, the more calls you miss, which means your best weeks, the packed Saturdays and the summer stretch, are also the ones where the most work slips away. It is not a discipline problem. A crew cannot move a house and answer the phone at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a move it is not one. A family whose lease ends Monday is calling three or four companies and booking the first one that answers and can hold the date. They are not going to leave a message and wait, and by the time you check your phone that evening, the move is already booked with someone else.</p>'},
        {"h2_html": "The calls you miss are the ones worth the <em>most</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. The calls that come in during your busy season, when every crew is already out, are often the full-house moves and long-distance hauls worth the most, and they bunch up exactly when nobody can pick up. So the calls you are most likely to miss are also the ones worth the most, and each one you lose is a booked week that went to whoever answered.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can tell a real move from a tire-kicker. A voicemail box cannot gather a quote, and a generic call center does not know a studio from a four-bedroom or a local move from a long-distance haul. What actually works is something that answers on the first ring day or night, asks where they are moving from and to, how big, and what day, and books the in-home or virtual estimate or flags a big move straight to your phone. It captures the move and leaves the price to you, so the quote call never rings out in the first place.</p>'}],
    "bridge_h2": "Stop losing booked moves to voicemail",
    "bridge_text": "An AI receptionist answers every quote call on the first ring, day or night, gathers the whole move, and books the estimate or flags it to you, so the call never rolls to voicemail while your crew is on a truck.",
    "bridge_slug": "ai-receptionist-for-movers",
    "bridge_label": "AI receptionist for movers",
    "faqs": [
        ("Would a customer rather reach a real person?",
         "When someone is about to trust a crew with everything they own, what they need most is to know a real company is handling it, and a steady voice that captures the move beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the details, and hands a big move straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when your crew is carrying furniture, on the road, or already on another call. Something that always answers and gathers the move is what catches the calls a forward would still miss.")],
    "trade_slug": "movers", "trade_plural": "movers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do My Moving Estimates Go Cold? (problem -> crm) ============
{
    "slug": "why-moving-estimates-go-cold",
    "h1": "Why Do My Moving Estimates Go Cold?",
    "title": "Why Do My Moving Estimates Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most moving estimates go quiet not over price but because nobody followed up. The family got busy or gathered other quotes, and the move went to whoever checked back in.",
    "answer": "Most moving estimates go cold not because your price was wrong, but because nobody followed up. The family got busy, gathered two or three other quotes, or simply forgot, and the move went to whoever checked back in. An estimate that goes quiet is usually not a no, it is a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "Silence usually means forgotten, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet estimate as a no on price, so you drop it and move on. But most of the time the family did not decide against you at all. They asked three or four movers for a quote, meant to compare them, and then the move itself swallowed them: packing, a closing that kept slipping, work, and kids. Your estimate slid down the pile with everything else. A week later they could not tell you the difference between the movers who quoted them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The one who gets the move is usually not the cheapest. It is the one who stayed in front of them: a friendly check-in a couple of days later, a quick note answering the question they were stuck on. That second touch is what turns a maybe into a booked date, and it is exactly the thing there is no time for when your crews are out and the next call is already ringing.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Movers do not skip follow-up because they are lazy. They skip it because the day fills up, and in peak season it overflows. You finish a move, roll to the next, handle the Saturday that booked three deep, and by evening the estimate you gave on Tuesday is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest estimates to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which estimates are still open and going cold.</li><li>The follow-up depends on you remembering, so it competes with the actual moves and loses.</li><li>By the time you circle back, the family has already booked the mover who beat you to it.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open estimate gets a couple of timed check-ins automatically, written to sound like you, the family comparing quotes keeps hearing from you while the others go silent, and the moves you already quoted stop slipping away.</p>'}],
    "bridge_h2": "Follow up on every estimate, automatically",
    "bridge_text": "A CRM keeps every open estimate in front of you and sends timed check-ins for you, so a family comparing movers keeps hearing from you while the other companies go quiet.",
    "bridge_slug": "crm-for-movers",
    "bridge_label": "CRM for movers",
    "faqs": [
        ("How many times should I follow up on a moving estimate?",
         "A couple of light touches over the first week or two catches most of the maybes without being pushy: a check-in a few days after the estimate, then a short note answering common questions. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly check-in reads as attentive, not spammy, and most families appreciate the nudge because they meant to get back to you and forgot. You can always jump in and message anyone directly.")],
    "trade_slug": "movers", "trade_plural": "movers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ How Do Movers Get More Customers? (how-to -> marketing) ============
{
    "slug": "how-do-movers-get-more-customers",
    "h1": "How Do Movers Get More Customers?",
    "title": "How Do Movers Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Movers get more customers by being easy to find when someone searches for a mover near them, winning the trust click with reviews, and turning past moves into referrals and repeat work.",
    "answer": "Movers get more customers by being easy to find the moment someone searches for a mover, winning the trust click with strong reviews, and turning every move into repeat work and referrals. Most companies do good work but are hard to find, thin on reviews, or never follow up, so the moves go to whoever showed up and looked trustworthy.",
    "sections": [
        {"h2_html": "Get found where the search <em>starts</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone needs a mover, they do not open a phone book, they search for a mover near them, and the first thing Google shows is the map pack, the little map with three local listings, star ratings, and a call button. Most people pick from those three without scrolling to the results below. So if the phone is quiet even though you do good work, the usual reason is that you are not in those three, and almost nobody is looking past them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting found runs on two things: a Google Business Profile that is verified, complete, active, and stacked with recent reviews, and a website that ranks for the towns you actually cover. Reviews carry more weight for a mover than for almost any trade, because a customer is deciding whether to trust strangers with everything they own, and they read the reviews before they ever call.</p>'},
        {"h2_html": "Win the click, then keep the <em>customer</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Showing up is half the job. The other half is turning searchers into booked moves and turning one move into the next. A few levers move it more than anything else, and none of them require gimmicks.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Collect reviews steadily, asking every happy customer right after the truck pulls away, so the next nervous shopper sees a wall of recent, genuine ones.</li><li>Make the trust obvious: licensed and insured, years in business, and real photos of your crew, so a stranger feels safe letting you into their home.</li><li>Reply to every review, good or bad, which reassures the next reader and helps your local ranking.</li><li>Put an estimate request first on a site that loads fast on a phone, so a ready customer books instead of bouncing.</li><li>Work your past customers and referral sources, the family you moved two years ago, the apartment complex that hands out your card, the realtor who recommends a crew at closing.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The cheapest customers are the ones you have already earned, so the companies that grow are the ones that stay in front of past movers and keep asking happy ones to spread the word. What no one can honestly promise is a specific spot on the map or a set number of leads, because Google and word of mouth are not something anyone controls, but the levers above are the ones that move them. A free audit can show you which ones you are leaving on the table.</p>'}],
    "bridge_h2": "Get found, get chosen, get referred",
    "bridge_text": "More customers come from being easy to find, easy to trust, and hard to forget. Marketing that keeps your profile ranking, your reviews growing, and your past movers coming back is how you get there.",
    "bridge_slug": "marketing-for-movers",
    "bridge_label": "Marketing for movers",
    "faqs": [
        ("What is the fastest way for a moving company to get more customers?",
         "Usually the quickest win is the Google Business Profile and reviews, because that is where a search for a mover near them lands. A verified, active profile with a steady stream of recent reviews can climb over a few weeks, and it puts you in front of people at the moment they are choosing who to call."),
        ("Do reviews really matter that much for movers?",
         "More than for almost any trade. A customer is handing strangers everything they own, so they read the reviews before they call, and Google leans on recent, genuine ones to decide who to show in the map pack. Asking every happy customer right after the move is the single biggest lever.")],
    "trade_slug": "movers", "trade_plural": "movers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
