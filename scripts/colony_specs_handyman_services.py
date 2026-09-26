"""Colony page specs for HANDYMAN SERVICES (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a handyman would search, answered directly up top (the 40-60 word AEO
answer), then two body sections, then a "the fix" bridge that funnels the page's authority into
the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, handyman-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear; no em/en dashes anywhere; "find the gap", never "leak" as a
money metaphor.

Nine questions, mixed how-to / cost / problem, spread across all seven money pages:
  1 how-handymen-get-clients               (how-to)  -> marketing-for-handyman-services
  2 best-crm-for-handyman                  (how-to)  -> crm-for-handyman-services
  3 handyman-website-cost                  (cost)    -> websites-seo-for-handyman-services
  4 answering-service-for-handyman-cost    (cost)    -> ai-receptionist-for-handyman-services
  5 get-more-handyman-reviews              (how-to)  -> review-software-for-handyman-services
  6 why-handyman-quotes-go-unanswered      (problem) -> automation-for-handyman-services
  7 stop-phone-tag-handyman                (problem) -> ai-receptionist-for-handyman-services
  8 should-a-handyman-offer-online-booking (how-to)  -> online-booking-for-handyman-services
  9 keep-handyman-schedule-full            (problem) -> crm-for-handyman-services
"""

TOPICS = [
# ==================== How Do Handymen Get More Clients? (how-to -> marketing) ====================
{
    "slug": "how-handymen-get-clients",
    "h1": "How Do Handymen Get More Clients?",
    "title": "How Do Handymen Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "Handymen get more clients by being the name people already recognize, with an active Google profile, real reviews, and neighborhood visibility, so they call you first.",
    "answer": "Handymen get more clients less by chasing new leads and more by being the name a neighborhood already recognizes. Keep your Google Business Profile active and full of recent reviews, stay visible in the areas you cover, and follow up with past customers, so when a list finally gets long enough, yours is the name they call.",
    "sections": [
        {"h2_html": "Most handyman work comes from being <em>known, not found</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most homeowners do not shop hard for a handyman. When the list finally gets long enough to act on, they call the name they already recognize: the person a neighbor mentioned, the truck they have seen around, the handyman who did good work last year. Letting a stranger into the house for a day of odd jobs is a trust decision, so people default to a familiar name over a cold search. That means getting more clients is less about chasing brand-new leads and more about being the recognized, trusted name before anyone even has a list.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">You cannot buy that recognition with a single ad, and you do not need to. It comes from a handful of steady, cheap habits that keep your name in front of the neighborhoods you cover, so when someone finally sets aside a Saturday for their list, you are the first person they think of instead of a name they have to go find.</p>'},
        {"h2_html": "Where new handyman clients actually <em>come from</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">New handyman clients rarely come from one big splash. They come from being easy to find and easy to trust at the moment someone is ready, which is a mix of a few things done consistently.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>An active, complete Google Business Profile, so you show up in the map pack when someone searches for a handyman near them.</li><li>A steady stream of recent, genuine reviews, which is what a nervous homeowner reads before letting anyone into the house.</li><li>Visibility in the neighborhoods you actually cover, on the local channels people ask on, instead of a thin budget spread across a whole metro.</li><li>Past customers you stay in touch with, since a home you have helped once has a list that keeps growing.</li><li>A simple website that lists the work you do and lets someone reach you in one tap.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of these is a gimmick, and none of them works overnight. Done together and kept up, they turn you into the handyman a neighborhood already knows, which is the cheapest and most durable source of work there is.</p>'}],
    "bridge_h2": "Be the handyman they already know",
    "bridge_text": "Getting more clients is about being visible and trusted where local demand shows up. Marketing keeps your Google profile active, your reviews fresh, and your name first in the neighborhoods you cover.",
    "bridge_slug": "marketing-for-handyman-services",
    "bridge_label": "Marketing for handyman services",
    "faqs": [
        ("What is the fastest way for a handyman to get more clients?",
         "The fastest lever is usually your Google Business Profile. Getting it verified, complete, and collecting recent reviews can lift you in the map pack within weeks, which is exactly where local searches turn into calls. Nobody controls Google, so no honest company promises a specific spot, but an active profile is what moves it."),
        ("Do I need to pay for ads to get handyman work?",
         "Not to start. Most handyman work comes from recognition and search, an active profile, real reviews, and staying in touch with past customers, which cost little beyond consistency. Paid ads can add reach later, but the free groundwork is usually what fills the calendar first.")],
    "trade_slug": "handyman-services", "trade_plural": "handyman businesses",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ What's the Best App and CRM for a Handyman Business? (how-to -> crm) ============
{
    "slug": "best-crm-for-handyman",
    "h1": "What's the Best App and CRM for a Handyman Business?",
    "title": "What's the Best App and CRM for a Handyman Business? | Top Shelf Business Solutions",
    "meta_desc": "The best app for a handyman business is a CRM that keeps every customer and unfinished list in one place and follows up for you, so repeat work comes back on its own.",
    "answer": "The best app for a handyman business is not a fancier calendar, it is a CRM that keeps every customer, lead, and unfinished list in one place and follows up for you. For a solo handyman the right one books jobs, chases quotes, and brings past customers back, so repeat work returns without you tracking it by memory.",
    "sections": [
        {"h2_html": "The best handyman app is the one that <em>stops work slipping</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most handymen go looking for a better calendar or a slicker invoice app, but the tool that actually moves the needle is a CRM, the one place that holds every customer, lead, and unfinished list and reaches back out on its own. A prettier schedule does not win you the next job. The next job comes from the customer whose two leftover to-dos got a nudge, and the family who forgot your number until a seasonal reminder landed.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So the best app for a handyman business is not the one with the most buttons. It is the one that quietly does the follow-up you never have time for between jobs, and keeps your whole customer history in your pocket instead of a truck full of receipts.</p>'},
        {"h2_html": "What the right CRM does for a <em>solo handyman</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A handyman working alone does not need enterprise software. You need a short list of things handled without you thinking about them:</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keeps every customer, address, past job, and note in one place you can pull up on your phone.</li><li>Follows up on open quotes and leftover list items on a schedule, so work you half-earned does not go cold.</li><li>Sends seasonal nudges to past customers, a spring to-do list, a round of fixes before the holidays, so repeat work comes back on its own.</li><li>Feeds off the calls your phone and booking link capture, so a new lead lands in one system instead of a sticky note.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The point is not the label on the software. It is that the repeat and leftover work actually shows up, instead of depending on you to remember hundreds of homes. Recover one job you would have let slip and it has paid for itself.</p>'}],
    "bridge_h2": "Put your customer list to work",
    "bridge_text": "The customers and leftover lists you already have are the cheapest work you can get. A CRM keeps them in one place and follows up for you, so they call you next instead of whoever they happen to find.",
    "bridge_slug": "crm-for-handyman-services",
    "bridge_label": "CRM for handyman services",
    "faqs": [
        ("What is the best CRM for a small handyman business?",
         "The best one is whichever actually gets used and does the follow-up for you, not the one with the longest feature list. For a solo handyman that means simple enough to run from your phone, and connected to your calls and calendar so nothing has to be entered twice. Top Shelf includes one built for exactly that, in the Signature plan at $899 a month."),
        ("Is a CRM overkill if it is just me?",
         "Usually not. Even a one-person handyman shop serves more homes and sends more small quotes than anyone can track by memory. The question is not headcount, it is whether follow-up is falling through. If leftover to-dos and past customers keep slipping, a CRM earns its keep.")],
    "trade_slug": "handyman-services", "trade_plural": "handyman businesses",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============== How Much Should a Handyman Website Cost? (cost -> websites-seo) ==============
{
    "slug": "handyman-website-cost",
    "h1": "How Much Should a Handyman Website Cost?",
    "title": "How Much Should a Handyman Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "What a handyman website should cost depends on what it must do first: show your exact jobs, name your service area, and make a quote one tap. Top Shelf builds it for $1,500, or free on a plan from $299/mo.",
    "answer": "Before you ask what a handyman website costs, ask what it has to do: show a homeowner that you handle their exact small job, name the neighborhoods you cover, and make requesting a quote one tap. A site that does that is worth building. Top Shelf builds one for $1,500 one time, or free on any monthly plan from $299.",
    "sections": [
        {"h2_html": "What a handyman website has to <em>do first</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For a handyman, the website has a harder job than for most trades, because your visitor does not arrive with one clear problem. They have a random small thing, a light that flickers, a door off its hinges, a crib to assemble before the baby arrives, and they need to see in a few seconds that you are the person who handles exactly that. So before price ever comes up, a handyman site has to earn the click three ways.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>List the dozens of small jobs you really do, mounting, assembly, drywall patching, gutter cleaning, odd repairs, so a visitor spots their own to-do item and knows they are in the right place.</li><li>Name the towns and neighborhoods you serve, so a nearby homeowner trusts you can reach them and Google can rank you for those places.</li><li>Make asking for help effortless, a tap-to-call button and a simple way to send over a photo or a list, since most visitors are deciding on a phone in under a minute.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Get those three right and the site pays you back. Miss them and it does not matter how cheap or expensive it was, because a page that hides what you do and buries your number brings in nothing.</p>'},
        {"h2_html": "Then the honest question of <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Once the site does its job, the money question gets simpler. Prices run from a cheap template you build and maintain yourself, which almost never ranks, up to a custom build with real SEO behind it, which is what actually gets a handyman found. That difference matters far more than the figure on the invoice, so ask any company who owns the finished site and what a later change will cost you.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps the numbers plain. A custom five page site by itself runs $1,500 one time, built for you and yours to keep. Or you take it built at no extra charge on any monthly plan, which starts at $299 and includes the ongoing SEO that keeps it climbing. Setup is included with no separate fee, whichever path you pick. Nobody can honestly promise an exact spot on Google, but a free audit will show where you stand today.</p>'}],
    "bridge_h2": "A site built to bring in the small jobs",
    "bridge_text": "The right handyman website earns back its price by turning searches for your exact jobs into calls you own. We build it to rank in your service area and capture every visitor, then hand each lead off to follow-up.",
    "bridge_slug": "websites-seo-for-handyman-services",
    "bridge_label": "Websites & SEO for handyman services",
    "faqs": [
        ("Is $1,500 a fair price for a handyman website?",
         "For a custom site you own outright and that is built to rank and bring in calls, it is a reasonable one-time number, with no monthly lock-in. What decides whether any price is fair is not how low it is, but whether the site gets found and turns a visitor into a booked job."),
        ("What should a good handyman website actually include?",
         "A clear list of the small jobs you take on so visitors find their own task, the towns you cover, real photos of finished work, honest reviews, and a one-tap way to call or send a list. Anything that hides what you do or makes reaching you a chore is quietly costing you jobs.")],
    "trade_slug": "handyman-services", "trade_plural": "handyman businesses",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Much Does an Answering Service for a Handyman Cost? (cost -> ai-receptionist) ========
{
    "slug": "answering-service-for-handyman-cost",
    "h1": "How Much Does an Answering Service for a Handyman Cost?",
    "title": "How Much Does an Answering Service for a Handyman Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for a handyman often bill per call or minute, which adds up fast. Top Shelf includes an AI receptionist that answers around the clock, in the Signature plan from $899/mo.",
    "answer": "Answering services for a handyman usually bill per call, per minute, or a monthly retainer, so a busy week runs up the tab fast. Top Shelf takes a different approach: an AI receptionist that answers every call around the clock and books the job is included in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good week turns into a big bill. A handyman also fields a steady stream of small calls all day while your hands are full, so the meter runs whether or not the call turns into real work. It helps to know the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for every call answered, so a busy stretch or a wave of tire-kickers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty caller or a slow operator costs more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a person with a small job does not leave a voicemail and wait, they call the next handyman on the list. The real cost of no coverage is not a monthly fee, it is the afternoon of easy work that went to whoever picked up. But a generic call center reading a script cannot capture a six-item honey-do list or tell a ten-minute job from a half-day, so you can pay for coverage and still get useless messages.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, takes down the whole list, roughs out the time, and books it on your calendar. It is included in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. The extra jobs it books over a month, ones you would otherwise have missed, are usually worth well more than the plan, and everything after that is on top.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers around the clock, captures the whole list, and books it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-handyman-services",
    "bridge_label": "AI receptionist for handyman services",
    "faqs": [
        ("Is there a free answering service for a handyman?",
         "Truly free options are usually just voicemail or a basic auto-reply, which a person with a small job tends to ignore before calling the next handyman. The cheaper honest question is flat versus per-call. Top Shelf includes an AI receptionist in the Signature plan at $899 a month with no per-call fee, so the cost does not climb on your busiest weeks."),
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the small job it books instead of losing to voicemail.")],
    "trade_slug": "handyman-services", "trade_plural": "handyman businesses",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ How Do Handymen Get More Google Reviews? (how-to -> review-software) ============
{
    "slug": "get-more-handyman-reviews",
    "h1": "How Do Handymen Get More Google Reviews?",
    "title": "How Do Handymen Get More Google Reviews? | Top Shelf Business Solutions",
    "meta_desc": "A handyman review lists every job you fixed in one visit, which sells the next mixed-list homeowner. Get more by firing the ask automatically the second each job wraps.",
    "answer": "A handyman review is unusually powerful because it reads like a menu of everything you fixed in one visit, which is exactly the proof the next mixed-list homeowner wants. You finish more jobs than most trades, so you get more chances to be reviewed. Ask right when the work is done, make it one tap, and let it run automatically.",
    "sections": [
        {"h2_html": "Why a handyman review is your <em>strongest ad</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Think about who is reading. A homeowner is about to let a near-stranger wander the whole house, often while they are at work, so they scan your reviews for one thing: did this person show up, do clean and careful work, and treat the place with respect. That reassurance is worth more to a handyman than to almost any trade, because the worry is bigger and the visit is personal.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">And a handyman review does something special. It usually names several jobs at once, they hung the TV, fixed the gate, and put the crib together in one trip, so it doubles as a menu of what you can do. The next person reading has their own random list and just saw proof you handle exactly that kind of mixed bag. Repeat calls and neighbor referrals grow from that same wall of recent, specific reviews.</p>'},
        {"h2_html": "Turn a week of small jobs into <em>a week of reviews</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason you do not have more reviews is not unhappy customers, it is that the ask never happens. You wrap up a quick job, load the truck, and drive to the next before it crosses your mind, and asking a week later, once the moment has passed, rarely lands. The fix is to make the request automatic and the reply effortless.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Send the ask the instant a job is marked finished, by text and email, while the customer is still glad it is handled.</li><li>Drop them onto your Google profile with a single link, so leaving a review takes seconds and not a hunt through menus.</li><li>Let it fire after every job, big or tiny, so a steady run of little tickets becomes a steady run of reviews.</li><li>Answer each review that lands, which shows the next reader a real person is paying attention.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Stay honest and you stay safe: ask everyone the same way, and never screen out the unhappy or pay for a kind word. Handled automatically, the sheer volume of work a handyman already does becomes the review count that wins the next call.</p>'}],
    "bridge_h2": "Make your reputation build itself",
    "bridge_text": "Review software fires the ask the second a job wraps and drops the customer onto your profile in one tap, so a handyman doing dozens of small jobs a month collects reviews without ever stopping to ask.",
    "bridge_slug": "review-software-for-handyman-services",
    "bridge_label": "Review software for handyman services",
    "faqs": [
        ("Why do reviews matter so much for a handyman?",
         "Because a homeowner is trusting a near-stranger inside their house, often while they are out, so they lean on reviews harder than they would for most services. A handyman review also lists the specific jobs you did, which reads as proof to the next person with a similar list and turns readers into callers."),
        ("How do I get reviews when my jobs are so quick?",
         "That speed is an advantage, not a problem. You finish more jobs than most trades, so you get far more chances to ask, as long as the request goes out every time. Sending it automatically as soon as each job wraps is what turns all that volume into a steady flow of reviews.")],
    "trade_slug": "handyman-services", "trade_plural": "handyman businesses",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do My Handyman Quotes Go Unanswered? (problem -> automation) ============
{
    "slug": "why-handyman-quotes-go-unanswered",
    "h1": "Why Do My Handyman Quotes Go Unanswered?",
    "title": "Why Do My Handyman Quotes Go Unanswered? | Top Shelf Business Solutions",
    "meta_desc": "Handymen hand out so many small quotes that they pile up and go quiet, not over price, but because each is too small to chase by hand. Automation nudges every one for you.",
    "answer": "A handyman fires off far more quotes than a big-ticket trade, a number over text here, a rough figure in a driveway there, so they pile up fast and slip your mind. Most go quiet not over price, but because each small quote was too easy to lose track of, and nobody circled back before the customer moved on.",
    "sections": [
        {"h2_html": "You quote more than you can <em>track</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A handyman gives out prices all day long, and most of them never make it onto paper. A text asking what it would run to hang some shelves. A number you rattle off standing in a driveway. A rough figure for a punch-list you jot on the back of a receipt. Compared with a trade that sends a handful of big formal bids a month, you are quoting constantly, and that sheer volume is the whole problem.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Any one of those little quotes is easy to forget, and there are dozens of them. The homeowner who asked about the shelves is not saying no when they go quiet. They got distracted, or they are waiting to see if a friend knows someone, and your number is one of several floating around. Whoever gets back first usually gets the work, and on a small job that is almost never the person too busy to remember.</p>'},
        {"h2_html": "Small tickets go cold because nobody <em>chases them</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The trouble is not effort, it is math. Sitting down to chase a small quote by hand can feel like more bother than the little job is worth, so it never happens, and multiply that across every quick price you gave this week and a real stack of work quietly disappears. You are not going to hand-track all of it, and you should not have to.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every quote you give is logged in one place instead of living in your texts, your memory, and the odd receipt.</li><li>Each one gets a gentle, timed check-in sent for you, so the small tickets get chased even though none is worth stopping your day for.</li><li>The messages read like you wrote them, so a nudge feels like attentive service and not a robot.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is exactly what automation is for: the follow-up that is too small and too frequent to do by hand, run on every quote without you lifting a finger. While a busy competitor forgets, your quiet quotes each get a timely nudge, so a good share of the everyday work you already priced comes back to you instead of vanishing.</p>'}],
    "bridge_h2": "Chase every small quote without lifting a finger",
    "bridge_text": "Automation logs every quick price you give and sends each one a timed nudge on its own, so the small jobs you already quoted come back to you instead of drifting off to whoever answered next.",
    "bridge_slug": "automation-for-handyman-services",
    "bridge_label": "Automation for handyman services",
    "faqs": [
        ("Are small handyman quotes even worth chasing?",
         "Added up, absolutely. No single small quote is worth much, but you give so many that the ones going quiet add up to real money over a month. Since chasing each by hand is not worth your time, the answer is to automate it, so every quote gets a nudge whether or not it is a big one."),
        ("How do I keep track of all the little quotes I hand out?",
         "Not in your head or your text thread, which is where they get lost. The point of a system is that every quote you give, even a quick number over text, is captured and set to follow up on its own, so none of them slips away quietly while you are on the next job.")],
    "trade_slug": "handyman-services", "trade_plural": "handyman businesses",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Do I Stop Playing Phone Tag With Handyman Customers? (problem -> ai-receptionist) ========
{
    "slug": "stop-phone-tag-handyman",
    "h1": "How Do I Stop Playing Phone Tag With Handyman Customers?",
    "title": "How Do I Stop Playing Phone Tag With Handyman Customers? | Top Shelf Business Solutions",
    "meta_desc": "Stop phone tag by making sure every handyman call gets answered and booked the first time, instead of trading voicemails between jobs, so nothing rolls to the next name.",
    "answer": "You stop playing phone tag by making sure every call gets answered the first time, instead of trading voicemails between jobs. A handyman working solo cannot pick up mid-task, so calls pile up and customers give up. An AI receptionist answers on the first ring, takes down the whole list, and books it, so there is nothing to call back.",
    "sections": [
        {"h2_html": "Phone tag starts because you <em>cannot pick up mid-job</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A handyman works with both hands full. When the phone rings you are up a ladder, holding a drill, or halfway under a sink, and none of those are moments you can stop and take a call. So it rolls to voicemail, you call back at five, they are at dinner, you leave a message, and two days of tag later they booked the handyman who was easier to reach. The busier you are, the more of this you do, so your best weeks lose the most work to voicemail.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The job was never the problem. The back and forth was. A person with a small thing to fix is not going to chase you through three rounds of voicemail, they will move down their search until someone picks up. Closing that gap does not mean answering your phone on a ladder. It means something reliable answers for you the first time, every time.</p>'},
        {"h2_html": "Something that answers and books <em>ends the tag</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Phone tag ends when the first call actually gets handled instead of parked in a voicemail box you check at night. An AI receptionist answers on the first ring while you keep working, finds out what the caller needs, whether it is one quick job or a list of ten, gets the address, and books a visit or a time window on your calendar. There is no message for you to return, because the work is already captured and scheduled.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is different from forwarding calls to your cell, which just moves the voicemail to a different phone you still cannot answer mid-job. And unlike a generic call center, it knows a repeat customer from a first-timer and can steer new work toward a day you are already in that neighborhood. You come off the job to an appointment on the calendar, not a stack of callbacks to chase.</p>'}],
    "bridge_h2": "End the tag, catch every call",
    "bridge_text": "An AI receptionist answers on the first ring while your hands are full, takes down the whole list, and books it, so there is no voicemail to return and no job lost to the next name in the search.",
    "bridge_slug": "ai-receptionist-for-handyman-services",
    "bridge_label": "AI receptionist for handyman services",
    "faqs": [
        ("Can I just forward calls to my cell to stop phone tag?",
         "Forwarding only helps when your hands are free. It still rolls to voicemail when you are on a ladder, under a sink, or already on another call, which is most of your day. Something that always answers and books the job is what actually ends the tag, instead of moving the voicemail to a different phone."),
        ("Would a customer rather reach a real person?",
         "For a small job, what a caller wants most is to know a real handyman will show up and handle their list, and a friendly voice that takes down the details and books a time beats a voicemail box every time. It is upfront about what it is, and hands anything that needs you straight to you.")],
    "trade_slug": "handyman-services", "trade_plural": "handyman businesses",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== Should a Handyman Let Customers Book Jobs Online? (how-to -> online-booking) ========
{
    "slug": "should-a-handyman-offer-online-booking",
    "h1": "Should a Handyman Let Customers Book Jobs Online?",
    "title": "Should a Handyman Let Customers Book Jobs Online? | Top Shelf Business Solutions",
    "meta_desc": "Yes, for routine work. Letting handyman customers self-schedule a TV mount or a short punch-list on your real availability ends the phone tag and books the gaps for you.",
    "answer": "Yes, for the routine work. A lot of handyman jobs, a TV mount, furniture assembly, a short punch-list, are not urgent, and those customers would happily book online instead of waiting for a callback. A booking link on your real availability turns the back and forth into an appointment that lands on your calendar while you work.",
    "sections": [
        {"h2_html": "A small job is not worth a <em>week of phone tag</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For the routine work, yes, a handyman should let customers book online. When a job is small, the effort to book it has to be small too. A homeowner wants a couple hours of help with a list, or just a TV hung before the weekend, and they are happy to schedule it, but if they have to call during the day, wait for a callback, and trade voicemails, the reward stops being worth the hassle. So they put it off, or they book the handyman who let them lock in a time on the spot.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A booking link lets them grab an open slot the moment they think of it, at night or on a lunch break, without reaching you first. You come off a job to find the visit already on your calendar with the details attached, instead of a missed call you now have to chase between stops.</p>'},
        {"h2_html": "You stay in control, and it fills the <em>gaps between jobs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Letting customers book online does not mean handing over your calendar. You set which job types are bookable, how long each runs, how much notice you need, and how much buffer to leave for drive time, with a minimum visit length so a ten-minute job never costs you a whole trip for nothing. A true rush can still be pointed to your phone to call now, while only genuinely routine work self-schedules.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Done right, it also fills the loose spots in your week. A one-hour mount or a quick repair fits neatly into the gap between two bigger jobs, and a booking tool that knows your real availability can offer those openings instead of leaving them empty. It syncs to the calendar you already use so it cannot double-book you, and the confirmation and reminder it sends are what cut down no-shows, which matters most when the whole ticket is small.</p>'}],
    "bridge_h2": "Let customers book without the callback",
    "bridge_text": "Online booking lets routine handyman jobs schedule themselves on your real availability, with the confirmations and reminders that keep customers showing up, so you stop trading voicemails over small work.",
    "bridge_slug": "online-booking-for-handyman-services",
    "bridge_label": "Online booking for handyman services",
    "faqs": [
        ("Will online booking send a rush job to a slot three days out?",
         "Not if it is set up right. You decide which job types can self-schedule and which route to a call first, so a genuine rush is pointed to your phone while only the routine work books itself. You keep control of what lands on the calendar and when."),
        ("Can customers book by the hour or by the job?",
         "Both, however you want to sell it. You can offer set tasks like a TV mount or furniture assembly, or blocks of time like a two-hour or half-day visit, with a minimum length so a tiny job never costs you a whole trip for nothing.")],
    "trade_slug": "handyman-services", "trade_plural": "handyman businesses",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Do I Keep My Handyman Schedule Full Between Big Jobs? (problem -> crm) ========
{
    "slug": "keep-handyman-schedule-full",
    "h1": "How Do I Keep My Handyman Schedule Full Between Big Jobs?",
    "title": "How Do I Keep My Handyman Schedule Full Between Big Jobs? | Top Shelf Business Solutions",
    "meta_desc": "Keep a handyman schedule full between big jobs by mining the customers you already have, seasonal nudges, leftover to-dos, and repeat work, so slow days book themselves.",
    "answer": "You keep the schedule full between big jobs by mining the customers you already have. Every home you have worked in has a growing list of small stuff, and a light, timely nudge brings that work back to fill the gaps. A CRM tracks past customers and leftover to-dos and follows up for you, so slow days book themselves.",
    "sections": [
        {"h2_html": "The full calendar is hiding in your <em>old customers</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When work slows between bigger jobs, the instinct is to go find brand-new customers, but the cheapest work you can get is already in your phone. Every home you have worked in has a rolling list of small stuff, a shelf that never went up, a door that sticks, a fixture to swap, and a light, timely nudge is often all it takes to turn that into a booked afternoon. You have already been inside, they already trust you, so the next list is yours if you stay in touch.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The trouble is you cannot personally remember to reach back out to hundreds of homes, so most of that repeat work drifts to whoever the homeowner happens to think of when the list finally piles up. Keeping the calendar full between big jobs is really a follow-up problem, not a demand problem.</p>'},
        {"h2_html": "How to keep the small jobs <em>flowing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Filling the gaps is less about hustling for new leads and more about working the list you already have, on a schedule so it happens whether or not you remember:</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Follow up on the two or three things you did not get to last visit, so leftover work comes back to you.</li><li>Send seasonal nudges to past customers, a spring to-do list, fixes before the holidays, fall weatherproofing, so repeat work returns on its own.</li><li>See who has not called in a while and reach out before they forget your name.</li><li>Let routine jobs book themselves online into the open slots between your bigger commitments.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Do that consistently and the slow days start booking themselves, because a steady trickle of small jobs from customers you already have is what fills the space around the big ones. A CRM runs all of it for you, so the schedule stays full without you working the phones every time it goes quiet.</p>'}],
    "bridge_h2": "Keep the calendar full between big jobs",
    "bridge_text": "The repeat work that fills your slow days is already in your customer list. A CRM tracks past customers and leftover to-dos and follows up for you, so small jobs keep booking the gaps.",
    "bridge_slug": "crm-for-handyman-services",
    "bridge_label": "CRM for handyman services",
    "faqs": [
        ("How do handymen stay busy in the slow season?",
         "By working their past-customer list instead of waiting for new calls. Seasonal reminders and check-ins on leftover to-dos bring repeat work back around, and letting routine jobs book online fills the open slots. The homes you have already helped are the most reliable source of work when things go quiet."),
        ("Is repeat work really cheaper than finding new customers?",
         "Almost always. A past customer already knows and trusts you, so there is no ad spend and no cold pitch, just a reminder at the right moment. Bringing back one home you helped last year costs far less than winning a stranger, which is why staying in touch pays off.")],
    "trade_slug": "handyman-services", "trade_plural": "handyman businesses",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
