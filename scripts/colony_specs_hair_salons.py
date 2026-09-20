"""Colony page specs for HAIR SALONS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a hair-salon owner would search, answered directly up top (the 40-60
word AEO answer), then two body sections, then a "the fix" bridge that funnels the page's
authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, hair-salon-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear, and CRM + AI receptionist both live in the $899 Signature
plan; a salon's own service pricing stays generic; no em/en dashes anywhere; never "leak" as a
metaphor.

The hair-salon slant that keeps this DISTINCT from the barbershop colony and every other trade:
color and cut with a stylist a client is loyal to, a five-to-eight-week color and root rebooking
cadence that is the retention engine, a stylist with both hands busy behind the chair so the desk
phone rings out, new-client discovery driven by Instagram, the portfolio, and reviews, and
no-shows on booked chairs. Booked chairs, not walk-ins; no booth rent.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 hair-salon-website-cost              (cost)     -> websites-seo-for-hair-salons
  2 hair-salon-answering-service-cost    (cost)     -> ai-receptionist-for-hair-salons
  3 is-a-crm-worth-it-for-a-hair-salon   (cost)     -> crm-for-hair-salons
  4 why-hair-salons-miss-calls           (problem)  -> ai-receptionist-for-hair-salons
  5 why-salon-clients-dont-rebook        (problem)  -> crm-for-hair-salons
  6 how-do-hair-salons-get-more-clients  (how-to)   -> marketing-for-hair-salons
"""

TOPICS = [
# ==================== How Much Does a Hair Salon Website Cost? (cost -> websites-seo) ====================
{
    "slug": "hair-salon-website-cost",
    "h1": "How Much Does a Hair Salon Website Cost?",
    "title": "How Much Does a Hair Salon Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A hair salon website ranges from a cheap template to a custom build, but what matters is whether it books clients. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A hair salon website runs from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more than the price is whether it books clients, shows your work, and ranks for hair salon near me. Top Shelf builds a custom site for $1,500 one-time, or includes one free on any monthly plan starting at $299.",
    "sections": [
        {"h2_html": "What a salon website actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A hair salon website earns its keep by turning someone who is browsing into a booked appointment, and a salon has a few specific jobs a generic template rarely does well. Get these right and the site pays for itself; miss them and even a pretty page sits quiet.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Online booking that works the way a salon books, by service and by stylist, with the right amount of chair time set aside, so a new color client is not squeezed into a fifteen minute slot.</li><li>A real gallery of your work, because color and cut are visual and a new client decides from your photos long before she reads a word.</li><li>Built to show up for hair salon near me and for the services you want more of, since that search is where most new clients start.</li><li>Your reviews and your Instagram front and center, so the trust you have already earned is doing the selling.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A beautiful site that hides the booking button and never ranks is the most expensive kind, because you paid for it and it brings you nobody new.</p>'},
        {"h2_html": "What a salon should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">None of that depends on spending the most. It depends on the site being built to book and to be found, then kept fresh so it keeps ranking. Top Shelf keeps the choice simple. A custom site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Before you compare quotes, it is worth asking three questions of anyone you talk to: who owns the site, what a simple change costs, and whether you keep it if you leave, because a cheap monthly builder can quietly hold your site and your photos hostage. What no honest company can promise is a specific ranking by a specific date, because no one controls Google. A free audit can show you where your current site stands and how much booking it is leaving on the table first.</p>'}],
    "bridge_h2": "Get a site that books for itself",
    "bridge_text": "A salon website is only worth the clients it books. Ours is built to rank for the searches near you, show your work, and turn a browser into a booked appointment, then wired to rebook her after.",
    "bridge_slug": "websites-seo-for-hair-salons",
    "bridge_label": "Websites & SEO for hair salons",
    "faqs": [
        ("Is a cheap template site good enough for a salon to start with?",
         "It can get you online, but a template you fill in yourself is rarely built to book by stylist and service, to rank for hair salon near me, or to show your work the way color and cut deserve. If a site is not bringing in new clients, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it, and to your photos, if you leave, before you sign anything.")],
    "trade_slug": "hair_salons", "trade_plural": "hair salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ What Does a Hair Salon Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "hair-salon-answering-service-cost",
    "h1": "What Does a Hair Salon Answering Service Cost?",
    "title": "What Does a Hair Salon Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for salons often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 and books in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for salons usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers calls and texts 24/7 and books the appointment comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. A salon also gets a lot of its calls and messages at the worst times to answer them: during a color service, on a packed Saturday, or late at night after someone sees your work online. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of price-shoppers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty caller or a slow operator costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">And a generic call center reading a script still cannot book the right service with the right stylist, so you can pay for coverage and still lose the appointment.</p>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a new client calling to book does not leave a voicemail, she calls the next salon until someone picks up. The real cost of no coverage is not a monthly fee, it is the new client, and every visit she would have made all year, going to whoever answered first. That is a lot to lose because a stylist had both hands full behind the chair.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers calls, texts, and messages on the first ring, day or night, books the right service with the right stylist for the right amount of time, and hands anything that needs your judgment, a big color correction or a consultation, straight to you. It does scheduling and intake, nothing your stylists are trained for. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One new color client it books on a Sunday can be worth well more than the plan costs once she keeps coming back, and everything it catches after that is on top.</p>'}],
    "bridge_h2": "Answer every client without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers calls and texts 24/7, books the right service with the right stylist, and hands the judgment calls to you, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-hair-salons",
    "bridge_label": "AI receptionist for hair salons",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the after-hours new client it books instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or holidays?",
         "No. It answers 24/7 as part of the plan, including the late-night Instagram message and the Sunday call that are often how new clients first reach you, with no after-hours surcharge or overage.")],
    "trade_slug": "hair_salons", "trade_plural": "hair salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============== Is a CRM Worth It for a Hair Salon? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-hair-salon",
    "h1": "Is a CRM Worth It for a Hair Salon?",
    "title": "Is a CRM Worth It for a Hair Salon? | Top Shelf Business Solutions",
    "meta_desc": "For most salons a CRM pays for itself by rebooking one color client and reviving one who drifted away. It comes in Top Shelf's Signature plan at $899/mo, not a separate bill.",
    "answer": "For most hair salons, yes. A CRM pays for itself the first time it rebooks a color client who would have drifted off, or brings back a regular you have not seen in months. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a salon when you have more clients than you can personally keep track of, which is most chairs that have been busy for a year or two. It is not worth it if you are a single stylist with a handful of regulars whose names, formulas, and next visits you genuinely hold in your head, though that rarely stays true as you grow. The honest test is simple: how many color clients left last month without booking their next visit, and how many regulars have not been in for six months or more? Those are the appointments a CRM is built to bring back. A color client is not a one-time sale, she is a standing visit every five or six weeks for as long as she stays, and that cadence is the whole retention engine a CRM is there to protect.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a salon is not the software, it is the repeat work that stops slipping away. A color client due for her roots, a regular whose cut is overdue, a client who paid for a package and forgot to use it: each one is revenue you have already earned and are one reminder away from rebooking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It prompts every client to rebook on the cadence her service needs, so the six week color client hears from you right before the regrowth shows and stays on the schedule.</li><li>It finds the clients who have gone quiet and sends a warm win-back for you, so a name you had written off turns back into a standing appointment.</li><li>It keeps every client, with her formulas, notes, preferred stylist, and full history in one place, so whoever is behind the chair picks up where the last visit left off.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: rebook one client you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your client list to work",
    "bridge_text": "The clients you have already seen are the easiest chairs to fill. A CRM rebooks every one on the right cadence and wins back the ones who drifted, so they come to your chair instead of the salon down the street.",
    "bridge_slug": "crm-for-hair-salons",
    "bridge_label": "CRM for hair salons",
    "faqs": [
        ("Is a CRM overkill for a small salon or a single stylist?",
         "Not usually. Even one busy chair sees more clients, formulas, and rebooking dates than anyone can track by memory. The point is not size, it is whether rebooking is falling through. If color clients leave without their next visit booked and regulars forget to come back, a CRM earns its keep."),
        ("How is a CRM different from the notes in my booking app or my phone?",
         "A list of contacts does not prompt a client to rebook, does not remember who is overdue, and does not send a win-back to the ones who drifted. A CRM does all of that on a schedule, so the repeat work shows up instead of depending on you to remember at the end of a long day.")],
    "trade_slug": "hair_salons", "trade_plural": "hair salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ Why Do Hair Salons Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-hair-salons-miss-calls",
    "h1": "Why Do Hair Salons Miss So Many Calls?",
    "title": "Why Do Hair Salons Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Salons miss calls because the stylist has both hands in a client's hair when the phone rings, and a new client does not leave a voicemail, she books the salon that answered.",
    "answer": "Salons miss calls because they come while your hands are literally in a client's hair, and a new client calling to book will not leave a voicemail. She hangs up and calls the next salon. The busiest days, when every chair is full, are exactly when the most calls ring out and the most new clients slip away.",
    "sections": [
        {"h2_html": "The phone rings when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Doing hair is a hands-full, eyes-on trade. When the phone rings, a stylist is mid-color, combing out a fresh cut, or foiling a client who cannot exactly sit with wet product while someone hunts for a pen. None of those are moments you can stop and take a call, and the front desk, if there is one, is checking someone out or answering another line. A salon runs on booked chairs, not walk-ins, so a call that rings out is not a client who will wander in later, it is one deciding right now who to book. The busier the salon, the more calls go unanswered, which means your best days are also the ones where the most new clients slip away.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a new client it is not one. Someone who found you online and is ready to book is not going to leave a message and wait for a callback. She scrolls to the next salon and books whoever answers, and by the time you wipe your hands and check the phone, that appointment is already somewhere else.</p>'},
        {"h2_html": "A missed call is not one appointment, it is a <em>year of visits</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call weighs the same. A regular will call back or text later, but a first-time client will not, and she is the expensive one to lose, because a new color or cut client who sticks is a standing appointment every five or six weeks for as long as she stays. Miss her call and you did not lose one booking, you lost a year of them to the salon that picked up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It gets worse after hours. A huge share of new-client interest arrives at night, when someone sees a transformation on Instagram, taps through, and wants to book while the inspiration is fresh, or reads your reviews on a lunch break and reaches out. If nobody answers that call or that message until tomorrow, the moment has passed. Closing the gap takes coverage that never sleeps and can actually book: something that answers calls and texts on the first ring, day or night, sets the right service with the right stylist, and hands a consultation or a color correction to you, so the new client is captured instead of handed down the street.</p>'}],
    "bridge_h2": "Stop losing new clients to voicemail",
    "bridge_text": "An AI receptionist answers every call and text on the first ring, day or night, books the right service with the right stylist, and hands the judgment calls to you, so the new client never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-hair-salons",
    "bridge_label": "AI receptionist for hair salons",
    "faqs": [
        ("Would a new client rather reach a real person?",
         "What a new client wants most is to know a real salon has her booked, and a warm reply that captures the details and sets the appointment beats a voicemail box every time. The AI receptionist is upfront about what it is, handles the booking, and hands anything that needs a stylist's judgment straight to you."),
        ("Can I just forward the salon phone to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are mid-color or already on another call, and it does nothing for the late-night Instagram message. Something that always answers and books is what catches the clients a forward would still miss.")],
    "trade_slug": "hair_salons", "trade_plural": "hair salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ Why Don't My Salon Clients Rebook? (problem -> crm) ============
{
    "slug": "why-salon-clients-dont-rebook",
    "h1": "Why Don't My Salon Clients Rebook?",
    "title": "Why Don't My Salon Clients Rebook? | Top Shelf Business Solutions",
    "meta_desc": "Most salon clients don't rebook not because they were unhappy, but because nobody prompted them. They left without booking the next visit, got busy, and the color cadence slipped.",
    "answer": "Most salon clients who do not rebook were not unhappy, nobody prompted them. She left without booking her next visit, meant to call, then got busy and the color cadence slipped. A client who goes quiet is usually not gone for good, she is a standing appointment that never got its next reminder.",
    "sections": [
        {"h2_html": "A quiet client is usually forgotten, not <em>unhappy</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a client who stopped coming as one you did something wrong, so you let her go. But most of the time she did not decide against you at all. She loved the color, meant to book the next one, and walked out the door into a busy life without a standing appointment on the calendar. Six or eight weeks later the roots are showing, she is scrolling for somewhere that can fit her in this week, and if she does not think of you first, she books whoever she finds.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The client who keeps coming back is rarely the one who loved the work most. She is the one who got a friendly nudge right when she was due, with an easy way to grab a time. That timely prompt is what turns a one-time visit into a client for years, and it is exactly the thing there is no time for between color services on a full day.</p>'},
        {"h2_html": "Why the rebook <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Salons do not skip rebooking because they do not care. They skip it because the day is full. You finish a color, turn the chair, squeeze in the client who ran late, and by close the woman who left at eleven without booking is out of sight. Asking every client to rebook at the desk depends on someone remembering in the rush, so it happens when things are slow, which is exactly when you least need it.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system tracking who is due back and on what cadence, so color, cuts, and treatments all blur together.</li><li>The rebook depends on a stylist or the front desk remembering, so it competes with the actual work and loses.</li><li>By the time anyone circles back, she has already booked another chair.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a loyalty problem, and it is the kind of thing you fix once and it just runs. When every client gets a rebooking nudge on the cadence her service needs, written to sound like you, the color client hears from you right before her roots show and books again instead of drifting off.</p>'}],
    "bridge_h2": "Rebook every client, automatically",
    "bridge_text": "A CRM tracks who is due and sends the rebooking nudge on the cadence each service needs, so the color client books her next visit before her roots show instead of drifting to the salon down the street.",
    "bridge_slug": "crm-for-hair-salons",
    "bridge_label": "CRM for hair salons",
    "faqs": [
        ("How often should a salon prompt a client to rebook?",
         "On the cadence the service needs, which a CRM handles per client. A color client is usually due around the five or six week mark, a cut on her own rhythm, a treatment on its. The key is that the nudge happens at all and on time, right before she starts looking elsewhere."),
        ("Does an automated rebooking reminder feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible time. A short, warm note that she is about due reads as attentive, not spammy, and most clients are glad for the reminder because they meant to book and forgot. You can always message anyone directly too.")],
    "trade_slug": "hair_salons", "trade_plural": "hair salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ How Do Hair Salons Get More Clients? (how-to -> marketing) ============
{
    "slug": "how-do-hair-salons-get-more-clients",
    "h1": "How Do Hair Salons Get More Clients?",
    "title": "How Do Hair Salons Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "Hair salons get more clients by being easy to find on Google and the map pack, showing their work on Instagram, and collecting reviews, then rebooking the clients they already have.",
    "answer": "Hair salons get more new clients by being easy to find the moment someone searches hair salon near me, showing their work where clients look, and having reviews that build trust. The map pack, a strong Instagram or portfolio, and steady reviews are where new clients start. The cheapest growth, though, is rebooking the clients you already have.",
    "sections": [
        {"h2_html": "Where new salon clients <em>actually come from</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">New salon clients are not won with one clever trick, they arrive through a handful of doors, and most salons are quietly neglecting at least one. Knowing where they start tells you where to put your effort.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Search and the map pack: when someone searches hair salon near me, Google shows three local listings with star ratings first, and most people pick from those three. A verified, active Google Business Profile with recent reviews is how you get into them.</li><li>Instagram and your portfolio: color and cut are visual, and a new client decides from your photos. The salon posting real before-and-afters steadily is the one that gets the late-night message.</li><li>Reviews: a wall of recent, genuine reviews does more selling than anything you can say about yourself, and it feeds your ranking at the same time.</li><li>Word of mouth, made easy: happy clients refer, but only when it is simple, so a share link or a small nudge turns a compliment in the chair into a booking.</li></ul>'},
        {"h2_html": "How to actually get more, <em>consistently</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The salons that grow are not doing something magic, they are doing the ordinary things every week without letting them slide when the chairs fill up. That consistency is what falls apart by hand and what a real system keeps running.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Keep the Google profile verified, complete, and active, and build a steady flow of real reviews by asking every happy client at the right moment. Post your work where new clients are looking, not once in a while but on a rhythm. And do not spend everything chasing strangers while the clients you already have quietly drift off: the cheapest new booking is a regular you rebook or a lapsed client you win back, which is why marketing and a CRM work best together. What no one can honestly promise is a specific spot on the map or a set number of new clients, because Google and Instagram decide who sees you. But the levers above are the ones that move it, and a free audit can show you which door is costing you the most new clients before you spend a dollar.</p>'}],
    "bridge_h2": "Get found where clients are looking",
    "bridge_text": "Most new salon clients start on Google, Instagram, and your reviews. Keeping your profile active, your work in front of people, and your reviews growing is how you show up when someone nearby is ready to book.",
    "bridge_slug": "marketing-for-hair-salons",
    "bridge_label": "Marketing for hair salons",
    "faqs": [
        ("What is the fastest way for a salon to get more clients?",
         "Usually the Google Business Profile, because the map pack is where most local searches start. Getting it verified, complete, and collecting recent reviews can lift you within a few weeks. Alongside it, rebooking the clients you already have is the fastest revenue of all, since they already trust you."),
        ("Do I need to be on every social platform to get salon clients?",
         "No. One platform you actually keep up, usually Instagram for a salon because the work is visual, beats five you neglect. Post your real before-and-afters on a steady rhythm and make sure the profile points to easy booking, and that does more than being everywhere at once.")],
    "trade_slug": "hair_salons", "trade_plural": "hair salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
]
