"""Colony page specs for NAIL SALONS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a nail salon owner would search, answered directly up top (the 40-60 word
AEO answer), then two body sections, then a "the fix" bridge that funnels the page's authority
into the ONE money page the question implies. Lighter than a money page.

A NAIL SALON runs on high-volume mani/pedi work, a mix of booked appointments AND walk-ins, and a
fast two to three week fill/rebooking cadence that is the retention engine. Techs work with both
hands on a client (or a client sits with her fingers under the lamp), so the phone rings out; a
nail-art Instagram portfolio is the discovery driver; groups and events (birthdays, bridal parties)
book together; and the menu is gel, acrylic, dip, and spa pedicures. Every dict here owns UNIQUE,
hand-written, nail-salon-specific substance (the generator owns shell, schema, events, keyword
placement). Stay DISTINCT from a hair salon: nail clients pick by the work shown and how easily they
can book and switch freely, not by a years-long loyalty to one stylist for color and cut.

Same honesty rules as the money specs: no invented stats, prices, or clients; hedge instead of
overpromise; only the real Top Shelf prices ($299/$899 plans, $1,500 one-time site) ever appear,
and the salon's OWN service pricing (mani, pedi, gel, acrylic, dip) stays generic with no numbers;
no em/en dashes anywhere; never "leak" as a metaphor. ETHICS: the AI receptionist does scheduling
and intake ONLY, is upfront that it is an assistant, and hands anything needing judgment to the salon.

Six questions, mixed cost / problem / how-to, spread across three money pages:
  1 nail-salon-website-cost              (cost)     -> websites-seo-for-nail-salons
  2 nail-salon-answering-service-cost    (cost)     -> ai-receptionist-for-nail-salons
  3 is-a-crm-worth-it-for-a-nail-salon   (cost)     -> crm-for-nail-salons
  4 why-nail-salons-miss-calls           (problem)  -> ai-receptionist-for-nail-salons
  5 why-nail-clients-dont-rebook         (problem)  -> crm-for-nail-salons
  6 how-do-nail-salons-get-more-clients  (how-to)   -> marketing-for-nail-salons
"""

TOPICS = [
# ==================== How Much Does a Nail Salon Website Cost? (cost -> websites-seo) ====================
{
    "slug": "nail-salon-website-cost",
    "h1": "How Much Does a Nail Salon Website Cost?",
    "title": "How Much Does a Nail Salon Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A nail salon website ranges from a cheap template to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A nail salon website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more is whether it shows your nail art, makes booking a fill or pedicure effortless, and gets found for nail salon near me. Top Shelf builds a custom five page site for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a nail salon website actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">People choose a nail salon with their eyes. Before anyone calls, she is scrolling photos to see whether your sets, your nail art, and your pedicures look like the work she wants, so the single most important job a nail salon website has is to show that work well. This is not a hair salon, where a client tends to stay with one stylist for years. Nail clients pick by the look and by how easy you are to book, and they switch to whoever makes both effortless, so the site has to earn the visit on the spot.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A real nail-art gallery, front and center, because photos of your work sell the booking better than any paragraph can.</li><li>One-tap booking for a fill, a full set, or a pedicure, so a client can grab a time the moment she decides instead of hunting for your number.</li><li>Clear walk-in information, your hours and what you take, since a lot of nail business is same-day and someone deciding on the drive over needs to know she can just come in.</li><li>Your gel, acrylic, dip, and spa-pedicure menu laid out plainly, on a site that loads fast and ranks when she searches nail salon near me on her phone.</li></ul>'},
        {"h2_html": "What a nail salon should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Once you know what the site has to do, the price makes more sense. A do-it-yourself builder is cheap each month, but you do the work and it rarely ranks or shows your nail art the way it deserves. A one-time custom build costs more up front and is yours to keep, though a site alone does little if nobody is handling the ongoing SEO that gets it found. An agency that bundles the build with that SEO and the booking behind it is where most of the long-term value lives, and also where the monthly cost lives. A beautiful site that never ranks and buries the booking link is the most expensive kind, because you paid for it and it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that fills the chair",
    "bridge_text": "A nail salon website is only worth the bookings it brings in. Ours is built to show your nail art, rank for the towns you serve, and turn a client searching for a salon near her into a booked fill or pedicure.",
    "bridge_slug": "websites-seo-for-nail-salons",
    "bridge_label": "Websites & SEO for nail salons",
    "faqs": [
        ("Is a cheap template site good enough for a nail salon to start with?",
         "It can get you online, but a template you fill in yourself rarely ranks or shows your nail art the way it should, and you do the upkeep. In a business where clients pick by the work they see and how easily they can book, a site that does neither is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep. On a monthly plan the site is built for you as part of the plan, and we will tell you plainly what happens to it, and to your photos, if you leave, before you sign anything.")],
    "trade_slug": "nail_salons", "trade_plural": "nail salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ What Does a Nail Salon Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "nail-salon-answering-service-cost",
    "h1": "What Does a Nail Salon Answering Service Cost?",
    "title": "What Does a Nail Salon Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for nail salons often bill per call or minute. Top Shelf includes an AI receptionist that books calls 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for nail salons usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call and text and books the appointment comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. A nail salon also fields the most calls at the worst moments for a live front desk: a packed Saturday when every tech is at a table, and the evenings and weekends when someone decides on a whim to book, which is when after-hours minutes tend to cost the most. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of quick questions runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty caller or a slow operator costs you more than a quick booking.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a client who wants a fill or a pedicure this afternoon does not leave a voicemail, she books with the salon that picked up. The real cost of no coverage is not a monthly fee, it is the same-day appointment, and the standing visit every couple of weeks she would have kept all year, that went to whoever answered. But a generic call center reading a script does not know a gel fill from a full set of acrylics, or that nail art and a spa pedicure need far more chair time than a polish change, so you can pay for coverage and still get bad bookings.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring by phone and text, day or night, sounds warm instead of rushed, and books the right service for the right chair time onto the right tech. It handles scheduling and booking only, and it is upfront that it is an assistant rather than pretending to be a person. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One same-day fill you would have lost while every tech was under the lamp can be worth more than the plan, and the regular she becomes is on top of that.</p>'}],
    "bridge_h2": "Answer every booking without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers by phone and text 24/7, tells a gel fill from a full set, and books it onto the right tech, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-nail-salons",
    "bridge_label": "AI receptionist for nail salons",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the same-day booking it captures instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or holidays?",
         "No. It answers 24/7 as part of the plan, including the Saturday rush and the late-night booking someone makes after seeing a set she wants, with no after-hours surcharge or overage.")],
    "trade_slug": "nail_salons", "trade_plural": "nail salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============== Is a CRM Worth It for a Nail Salon? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-nail-salon",
    "h1": "Is a CRM Worth It for a Nail Salon?",
    "title": "Is a CRM Worth It for a Nail Salon? | Top Shelf Business Solutions",
    "meta_desc": "For most nail salons a CRM pays for itself by rebooking one gel client and reviving a lapsed regular. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most nail salons, yes. A CRM pays for itself the first time it rebooks a gel client before her polish grows out, or brings back a regular who quietly drifted away. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a nail salon when you have more clients on the short fill-and-rebook cadence than the front desk can keep straight, which is most established salons. It is not worth it if you are a single tech seeing a handful of clients a week and genuinely reaching every one of them, though that rarely stays true as you grow. Loyalty punch cards and prepaid packages add another layer, money already collected that only becomes revenue when the client comes back in to use it. The honest test is simple: how many gel and fill clients are past due for their next visit right now, how many punch cards and packages are sitting unused, and how many regulars have not been in for a couple of months? Those are the visits a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a nail salon is not the software, it is the recurring visits that stop slipping away. Nail work is some of the most predictable repeat business there is: a gel or fill client due every two to three weeks, a pedicure client on her own rhythm, a package with sessions left on it. Each one is a visit you have already half-earned and are one well-timed reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It reminds each client on the short cadence nail work runs on, so a fill or a pedicure rebooks without anyone at the desk tracking dates.</li><li>It keeps every client, her preferred tech, the colors and shapes she favors, any notes, and her full visit history in one place instead of an appointment book and what the front desk can remember.</li><li>It tracks loyalty punch cards and prepaid packages against the right client, so the people who paid ahead or are one visit from a reward actually come in and use it.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one lapsed regular or one overdue fill and it has paid for itself, and the standing visits after that are margin.</p>'}],
    "bridge_h2": "Turn your client list into recurring visits",
    "bridge_text": "The clients you already have are the cheapest bookings a nail salon can get. A CRM reminds each one when her fill is coming due and revives the ones who drifted, so they rebook with you instead of trying the salon down the block.",
    "bridge_slug": "crm-for-nail-salons",
    "bridge_label": "CRM for nail salons",
    "faqs": [
        ("Is a CRM overkill for a small nail salon?",
         "Not usually. Even a two or three tech salon serves more clients on a repeating cadence than anyone can track by memory. The point is not size, it is whether rebooking is falling through. If gel clients drift past due and punch cards go unused, a CRM earns its keep."),
        ("How is a CRM different from the booking app I already use?",
         "A booking app records appointments. It does not watch the short fill cadence, nudge a client who is coming due, flag a package going unused, or revive a regular you have not seen in months. A CRM does all of that on a schedule, so the repeat visits show up instead of depending on memory.")],
    "trade_slug": "nail_salons", "trade_plural": "nail salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ Why Do Nail Salons Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-nail-salons-miss-calls",
    "h1": "Why Do Nail Salons Miss So Many Calls?",
    "title": "Why Do Nail Salons Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Nail salons miss calls because every tech is at a table with a client. A same-day caller who reaches voicemail just books the salon that answered.",
    "answer": "Nail salons miss calls because they ring while every tech is at a table with a client, or a client sits with her fingers under the lamp. Someone who wants an opening this afternoon does not leave a voicemail, she books with the next salon that answers. A lot of interest also arrives after hours, when no one is at the desk.",
    "sections": [
        {"h2_html": "The call comes when every tech is <em>at a table</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A nail salon is a hands-full business. When the phone rings, a tech has both hands on a client mid-set, or a client is sitting with her fingers under the lamp waiting on the gel to cure, and neither can stop to grab it. On a busy Saturday there may be no one free at the desk at all. The busier the salon, the more calls ring out, which means your best days are also the ones where the most bookings slip away. It is not a discipline problem. A team at the tables cannot do the work in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for someone who wants her nails done this week it is not one. She will not leave a message and wait for a callback. She taps the next salon on the list, and the one after that, until someone picks up, and by the time anyone checks the voicemail box the appointment is already gone.</p>'},
        {"h2_html": "Your same-day and after-hours bookings are the ones you <em>lose</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A big share of nail business is not planned a week out: someone chips a nail the morning of an event, decides on a whim to get a pedicure before a trip, or wants a fresh set before the weekend and calls around to see who can fit her in today. That same-day demand is some of the easiest money a salon can book, and it is also the most fragile, because the caller simply keeps dialing until a salon says yes. A group booking for a birthday or a bridal party is even bigger, and it goes to whoever answered the phone.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">More of that interest arrives after hours than most owners expect, when a client sees a set she likes late at night or books on a Sunday while she is thinking about it, and that is exactly when the desk is dark. Closing the gap takes coverage that never sleeps and can tell a quick polish change from a full set of acrylics that needs real chair time. What works is something that answers on the first ring by phone and text, checks the book, and slots her in or holds the details, so the booking is caught instead of lost. It handles scheduling and booking only and hands anything that needs your judgment to you.</p>'}],
    "bridge_h2": "Stop losing bookings to voicemail",
    "bridge_text": "An AI receptionist answers every call and text on the first ring, day or night, checks your book, and slots in a same-day fill or holds a full set for you, so the booking never rolls to voicemail while your team is at the tables.",
    "bridge_slug": "ai-receptionist-for-nail-salons",
    "bridge_label": "AI receptionist for nail salons",
    "faqs": [
        ("Would a client rather reach a real person?",
         "What a client booking her nails wants most is to know she can get in and that a real salon has her down, and a warm reply that captures the details beats a voicemail box every time. The AI receptionist is upfront that it is an assistant, gets what she needs, and books it or hands it to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are mid-set, under the lamp with a client, or closed for the night, which is when many of your bookings come in. Something that always answers and books is what catches the calls a forward would still miss.")],
    "trade_slug": "nail_salons", "trade_plural": "nail salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ Why Don't My Nail Clients Rebook? (problem -> crm) ============
{
    "slug": "why-nail-clients-dont-rebook",
    "h1": "Why Don't My Nail Clients Rebook?",
    "title": "Why Don't My Nail Clients Rebook? | Top Shelf Business Solutions",
    "meta_desc": "Most nail clients do not rebook because no reminder came, not because they were unhappy. On a two to three week cadence a missed fill quietly becomes months away.",
    "answer": "Most nail clients do not rebook because no reminder ever came, not because they were unhappy. A client leaves thrilled without booking her next fill, life gets busy, and on a two to three week cadence her polish grows out before she thinks of it. She resurfaces weeks later at whatever salon is convenient. The visit was always going to repeat, it just needed a nudge.",
    "sections": [
        {"h2_html": "Silence usually means forgotten, not <em>unhappy</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a client who did not come back as one who was unhappy, so you move on. But most of the time she was thrilled walking out and fully meant to return. She just left without booking the next visit, the way most people do when the salon is busy, and then life got in the way. Nail work runs on a short clock: a gel manicure starts lifting in about two to three weeks, a fill comes due just as fast, and a pedicure keeps its own rhythm. She does not feel any of that as a decision to leave you, she quietly comes due, notices her nails one morning, and books wherever is convenient.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The salon she rebooks with is usually not the one with the best work. It is the one that reached her at the right moment, a friendly note that she is coming due with a link to grab a time before the gel lifts. That well-timed touch is what turns a growing-out set into a booked visit, and it is exactly the thing a busy front desk never gets around to between clients.</p>'},
        {"h2_html": "Why the rebooking <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nail salons do not skip the follow-up because they are careless. They skip it because the day fills up. The team is at the tables, seating walk-ins, and ringing people out, and no one can also hold the fill dates of a few hundred clients in her head. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest clients coming due.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system watching who is past due on the short fill cadence, so the reminder never goes out.</li><li>Clients forget they have punch cards or prepaid packages left, and no one flags the ones going unused before they lapse.</li><li>Regulars quietly stop coming in, and nobody notices in time to reach back out while they still remember your work.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not an effort problem, and it is the kind of thing you fix once and it just runs. When every client is reminded on the two to three week cadence nail work actually runs on, written to sound like your salon, the ones coming due keep hearing from you at the right moment, and the standing visits you already earned stop drifting to the salon down the block.</p>'}],
    "bridge_h2": "Bring every client back on cadence",
    "bridge_text": "A CRM watches the short fill cadence for every client and sends the reminder for you, so a gel client coming due, a punch card with visits left, and a regular who drifted all rebook with you instead of the salon that was simply convenient.",
    "bridge_slug": "crm-for-nail-salons",
    "bridge_label": "CRM for nail salons",
    "faqs": [
        ("How soon should I remind a nail client to rebook?",
         "On the cadence her service actually runs on: a gel or fill client as she comes due at about two to three weeks, a pedicure client on her own rhythm. The key is that the reminder happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like your salon and sent at a sensible moment. A short, friendly note that she is coming due reads as attentive, not spammy, and most clients appreciate the nudge because they meant to rebook and forgot. You can always step in and message anyone yourself.")],
    "trade_slug": "nail_salons", "trade_plural": "nail salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ How Do Nail Salons Get More Clients? (how-to -> marketing) ============
{
    "slug": "how-do-nail-salons-get-more-clients",
    "h1": "How Do Nail Salons Get More Clients?",
    "title": "How Do Nail Salons Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "Nail salons get more clients by showing up in the map pack, in Google reviews, and on Instagram with their nail art, then making it one tap to book.",
    "answer": "Nail salons get more clients by showing up where people actually look, the Google map pack, recent reviews, and an Instagram full of your nail art, and then making it effortless to book. New clients matter, but the fastest growth usually pairs that with rebooking the clients you already have on their short fill cadence.",
    "sections": [
        {"h2_html": "Show up where nail clients are <em>looking</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more nail clients is less about one clever tactic and more about being visible and appealing in the few places people actually decide. When someone searches for a nail salon near her, Google shows the map pack first, three local listings with star ratings, and most people choose from those three without scrolling. Nails are also uniquely visual: a large share of discovery happens on Instagram, where photos of your sets, seasonal designs, and nail art do the kind of convincing a text ad never could, and a great design gets shared far past your own followers.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep your Google Business Profile verified, complete, and active, because the map pack is where most local searches for a nail salon begin.</li><li>Build a steady flow of genuine, recent reviews, since a new client trusts other clients before she trusts your ad.</li><li>Post your nail art on Instagram regularly, because for nails the portfolio is the marketing, and it is how the late-night scroller finds you.</li><li>Make booking effortless from every one of those places, and make it clear walk-ins are welcome, because interest cools fast if she has to hunt for how to reach you.</li></ul>'},
        {"h2_html": "Then rebook the clients you <em>already have</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">New clients are only half of it, and usually the more expensive half. The cheapest growth a nail salon has is the client list it already earned. Nail work repeats on a short two to three week cadence and sells well as loyalty punch cards and prepaid packages, so a salon that consistently rebooks its existing clients and revives the lapsed ones grows faster than one pouring everything into new faces that come once and disappear.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">In practice that means pairing the visibility above with the follow-up behind it. Answer every call the moment it comes in so a same-day booking is not lost to voicemail, remind each client when her fill is coming due, nudge the clients who have punch cards or packages to come use them, and reach back out to the regulars who have gone quiet. Do the visible part to fill the top and the follow-up part to keep clients on cadence, and the two compound. What no honest company can promise is a specific number of new clients, but showing up where clients look and following up on the ones you have are the levers that reliably move bookings.</p>'}],
    "bridge_h2": "Get found, then keep them coming back",
    "bridge_text": "Most nail salon growth starts in the map pack, in your reviews, and on an Instagram full of your nail art, then compounds when you rebook the clients you already have. Marketing that does both is how a nail salon fills the chairs and keeps them full.",
    "bridge_slug": "marketing-for-nail-salons",
    "bridge_label": "Marketing for nail salons",
    "faqs": [
        ("What is the fastest way for a nail salon to get more clients?",
         "Usually to get visible where people already look, a complete Google Business Profile in the map pack, recent reviews, and an active Instagram showing your nail art, and to make booking one tap. Pair that with rebooking your existing clients on their fill cadence and the chairs fill from both directions."),
        ("Do I need paid ads to grow a nail salon?",
         "Not to start. A verified, well-reviewed Google profile, a steady stream of nail-art posts, and consistent rebooking of your current clients move bookings without an ad budget. Paid ads can add reach on top, but they work far better once the profile, reviews, and follow-up are already in place.")],
    "trade_slug": "nail_salons", "trade_plural": "nail salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
]
