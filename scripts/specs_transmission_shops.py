"""Per-page content specs for the SEO corpus (plan §5), transmission shops batch. Same contract
as scripts/corpus_specs.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, transmission-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the plumber, auto-repair, tire, or auto-body content reworded.

Auto hub, transmission angle. This is deliberately distinct from the general auto-repair batch
(warning-light drop-offs, recurring mileage service), the tire batch (price-and-availability
firehose, rotations, the next set), and the auto-body batch (collision, insurance claims). A
transmission is the scariest, highest-ticket repair most drivers ever face, so the caller is
anxious and price-and-trust shopping several shops, often after a dealer quote, and books the
shop that answers calmly and offers a free diagnostic or second opinion. The money lever is
winning the big job by responding fast while a tech is on a road test, and by following up the
free-check leads who left to think, get another opinion, or arrange financing; warranty and
financing matter, and reviews about honesty (not overselling an unnecessary rebuild) win the
trust. Four service angles are here in one file (the ai-receptionist dict carries "demo": True).
Each example body ends with the literal "Illustrative example, not a client." per the honesty
rule; if the generator also appends that line, dedupe there.
"""

SPECS = [
# ==================== AI Receptionist for Transmission Shops ====================
{
    "slug": "ai-receptionist-for-transmission-shops", "demo": True,
    "trade_slug": "transmission_shops", "trade_plural": "transmission shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "AI Receptionist for Transmission Shops",
    "title": "AI Receptionist for Transmission Shops | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Transmission Shops",
    "meta_desc": "A transmission shop answering service answers every call while your tech is on a road test, calms an anxious caller, offers your free check, and books it.",
    "service_schema_name": "AI Receptionist for Transmission Shops",
    "eyebrow": "For Transmission Shops",
    "h1_html": "AI Receptionist <em>for Transmission Shops</em>",
    "answer_block": "A transmission shop answering service answers every call the moment it rings, even when your tech is under a car or out on a road test. It stays calm with a driver weighing a big repair, offers your free diagnostic, and books the check, so the job is yours instead of the shop that answered.",
    "sections": [
        {"h2_html": "The call you miss is the big job that <em>goes to the shop that answered</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A driver whose transmission is slipping, or who just got a big repair quote from the dealer and cannot quite believe it, is not going to leave a voicemail. It is one of the most stressful, most expensive things that can go wrong with a car, so the caller is anxious and calling several shops in a row for a straight answer and a second opinion. They book the first one that picks up, sounds calm, and offers to look at it, not the one that let the phone ring out.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">But diagnosing a transmission is not a counter job. Your tech is under a car, out on a road test feeling for the shift that slips, or elbow deep in a rebuild, and nobody is free to grab the phone. So the call rolls to voicemail, and the biggest job of the week goes to whoever answered. An answering service picks up on the first ring, reassures the caller, offers your free diagnostic, and books the check, so the job is captured instead of lost to the shop down the road.</p>'},
        {"h2_html": "Built around how a <em>transmission shop actually gets calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The calls that hit a transmission shop are not quick questions. They are anxious drivers trying to find out whether it is really the transmission or something cheaper, what a rebuild is going to run, and whether they can trust you after a dealer told them the worst. Every one lands while your tech is out on a road test or buried in a job. A voicemail box cannot reassure a worried caller, and a generic call center does not know a slipping transmission from a bad mount.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers every call while your tech is on a road test or under a car, so an anxious driver reaches a calm, real answer instead of a voicemail and books with you.</li><li>Offers and books your free diagnostic or second opinion, the single thing that gets a scared, price-shopping caller through your door instead of the next shop.</li><li>Gathers the year, make, model, the symptoms, and whether they already have a quote from the dealer, then books the check on your schedule and texts you the details.</li><li>Answers the money questions that decide a big repair, financing and how the warranty works, from the answers you set, and treats a referral from another shop differently from a first-time caller.</li></ul>'},
        {"h2_html": "The math is <em>one job you would have lost</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not need to catch many calls for this to pay for itself. A rebuild is one of the biggest tickets that comes through your shop, so a single caller you would have lost to voicemail, the one weighing a rebuild against buying another car, is often worth more than the service costs for months. Because the whole model runs on free diagnostics, the calls it captures fill your bay with paying work, and everything after that first save is on top. The point is to stop handing your best-paying jobs to the shop that happened to answer while your tech was on a road test.</p>'},
        {"h2_html": "You own the number, the calls, and the <em>customer list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing shop number, or a new one registered in your name, not ours. Every caller, every vehicle, and every quote stays yours and exportable any time, so the customer list you build is an asset you own instead of something you rent back month to month, and no long contract holds your data hostage. The answering service is one piece of the Top Shelf platform, and paired with the CRM on the Signature plan it drops every call it captures into the same system that follows up, so a free check that did not book or a quote left to think over never quietly slips away.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A big repair, booked while your tech was <em>on a road test</em>",
        "body_html": "A driver's transmission has been slipping for a week, and the dealer just quoted them a number that made their stomach drop. On their lunch break they call independent shops for a second opinion, and yours is the second one they try. Your tech is out on a road test, so on any other day it goes to voicemail and they book whoever picks up next. Instead the service answers, explains that a free check will tell them what is really wrong, and books the diagnostic for the next morning while texting you the vehicle and the fact that they already have a dealer quote in hand. You come off the road test to a check already on the schedule and a driver who feels looked after, not a lost rebuild. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current shop number?",
         "Yes. It can answer on the number you already use, or set up a new one registered in your name. Either way the number and every call that comes through it belong to you and go with you if you ever leave."),
        ("Can it handle an anxious caller who just got a dealer quote?",
         "Yes, that is the point. It stays calm, hears the driver out, explains that a free check is the honest way to find out what is really wrong instead of guessing off a dealer's number, and books the diagnostic. A worried caller who feels heard books with you instead of dialing the next shop."),
        ("Will it offer and book my free diagnostic?",
         "Yes. The free check is what gets a scared, price-shopping driver through your door, so the service leads with it, books it on your real availability, and texts you the vehicle and the symptoms. It can also share what you offer for financing and how your warranty works, from the answers you set, so the money questions do not stall the booking."),
        ("Is it going to sound like a robot to a worried customer?",
         "It answers naturally and calmly, and it is upfront instead of pretending to be a person. Someone staring down a repair that can cost as much as a used car mostly needs to know a real shop will look at it for free, and a steady voice that captures the details beats a voicemail box every time. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your triage questions, your free-check booking, and your financing and warranty answers for you, so it is answering in days, not weeks. Start with a free audit and we will show you what your current phone setup is missing.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for transmission shops"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-transmission-shops.html", "The CRM that follows up on every call you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing big jobs to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many big-repair calls and free-check leads your current phone setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ========================= CRM for Transmission Shops =========================
{
    "slug": "crm-for-transmission-shops",
    "trade_slug": "transmission_shops", "trade_plural": "transmission shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "CRM for Transmission Shops",
    "title": "CRM for Transmission Shops | Top Shelf Business Solutions",
    "og_title": "CRM for Transmission Shops",
    "meta_desc": "A CRM for transmission shops follows up on every free check and quote that did not book, so a driver weighing a big repair comes back to you, not a competitor.",
    "service_schema_name": "CRM for Transmission Shops",
    "eyebrow": "For Transmission Shops",
    "h1_html": "CRM <em>for Transmission Shops</em>",
    "answer_block": "A CRM for transmission shops keeps every free diagnostic, quote, and customer in one place and follows up for you, so the driver who left to think over a big repair and shop a second opinion comes back to you instead of the shop that stayed in touch. The job you diagnosed becomes the job you win.",
    "sections": [
        {"h2_html": "The free diagnostics you already did are the rebuilds you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A transmission shop does not usually have a traffic problem so much as a follow-up problem. You give away the diagnostic, find the fault, and hand the driver a quote for a rebuild, and because it is a big number they say they need to think about it, talk to their spouse, or check one more shop. Then the bay fills up and nobody circles back. They shop two more quotes, sort out financing, and the job goes to whoever stayed in touch, not always the lowest number. The quote was never dead. It just needed one more call a few days later, and that is the thing there is never time for with a car up on the rack.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every free check and every open quote in front of you and works the follow-up on a schedule you set, by text and email, whether or not anyone at the counter remembers. The driver weighing a rebuild against a new car hears from you again while the other shops go quiet, and the biggest job on your board comes back to you.</p>'},
        {"h2_html": "A big repair is a decision, so it takes <em>more than one conversation</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody says yes to a major repair on the spot. The reason a transmission quote sits is almost never that the customer walked away for good. They are getting a second opinion, waiting on a paycheck, working out whether financing makes it doable, or deciding if a car this old is worth saving. Each one is a reason to reach back out with the answer to the thing that is actually holding them up, and each one is easy to forget when the next car is already in the bay.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every free check, every vehicle, and every quote lives in one place instead of a stack of paper diagnostics and your memory.</li><li>Open quotes get a follow-up on the schedule you set, so the driver deciding on a rebuild keeps hearing from you while the shops they also called go silent.</li><li>The reminders can carry the things that unstick a big repair, that you offer financing, how your warranty works, what the job includes, so the money and the worry are answered before they drift to someone else.</li><li>You can see who went quiet and reach the right customer at the right time, without keeping any of it in your head.</li></ul>'},
        {"h2_html": "The honest diagnosis is your <em>best referral engine</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A transmission customer is not a monthly regular the way an oil-change customer is, so the game is not constant repeat visits. It is being the shop people trust with the scariest repair on the car, and telling them the truth is what earns it. The driver you told did not need a full rebuild, just a solenoid or a fluid service, is the one who sends you their whole family, because a huge transmission bill avoided is a story people repeat. And the general repair shops and used-car lots that do not do transmission work in house send it to the specialist they remember, so keeping those referral partners warm is some of the easiest work you will book, and it is sitting in the list you already have.</p>'},
        {"h2_html": "You own the list, and it works with the <em>rest of the shop</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every customer, vehicle, and diagnostic record belongs to you and exports any time, never trapped inside software you rent. Because the CRM is part of the Top Shelf platform, a call the answering service picks up drops straight into your database and gets worked automatically, and a free check booked online is logged against the right customer with the vehicle and the symptoms already attached. The CRM and the answering service come together on the Signature plan, so the free diagnostics you give away actually turn into booked work instead of going cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The free check that <em>becomes the rebuild</em>",
        "body_html": "A driver comes in for the free diagnostic after their transmission started slipping, and you find it needs a rebuild. You write it up, but it is a big number, so they want one more opinion and to see whether they can finance it. Normally that is the last you hear of them. Instead the CRM sends a friendly check-in a few days later that mentions you offer financing, and a short note the week after about the warranty on the rebuild. The other shop they visited never followed up, so once the money comes together, yours is the only name still in front of them, and they book without shopping further. You never sat down to chase it. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing customers and past diagnostics?",
         "Yes. Your current customers, their vehicles, and the checks and quotes you have written come in and live in one place, and everything stays yours and exportable. The point is to make the customer list you already have actually work for you."),
        ("Will it follow up on the free checks and quotes that did not book?",
         "Yes, on the schedule you approve. A free diagnostic or an open quote that did not close gets a check-in a few days later and another after that, all sent for you, so a driver weighing a big repair keeps hearing from you while the other shops go quiet. You can jump in and message anyone directly any time."),
        ("Can it keep financing and warranty in front of a customer deciding on a big repair?",
         "Yes, and that is often what closes the job. The follow-ups can carry the things that actually unstick a rebuild, that you offer financing, how the warranty works, and what the price includes, so the reasons a driver hesitates are answered on a schedule instead of left to talk them out of it."),
        ("Can it help me stay in front of the shops and lots that refer transmission work to me?",
         "Yes. You can keep the general repair shops, dealers, and used-car lots that farm out transmission work in one place and reach them on a schedule, instead of hoping they remember you the next time a customer's transmission goes. Those referral sources are some of the most valuable relationships a specialist has, and they are worth working like any other lead."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your customers and vehicles, build your follow-up sequences, and connect it to your calls and your free-check bookings, so it is working in days. Start with a free audit and we will show you where jobs are slipping through today.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for transmission shops"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-transmission-shops.html", "The AI receptionist that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting free checks and quotes <em>go cold</em>",
    "cta_sub": "Get a free audit of how many of your free diagnostics and open quotes are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ====================== Marketing for Transmission Shops ======================
{
    "slug": "marketing-for-transmission-shops",
    "trade_slug": "transmission_shops", "trade_plural": "transmission shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "Marketing for Transmission Shops",
    "title": "Marketing for Transmission Shops | Top Shelf Business Solutions",
    "og_title": "Marketing for Transmission Shops",
    "meta_desc": "Transmission shop marketing keeps your Google Business Profile active and first in the map pack, so a driver searching after a dealer quote calls you first.",
    "service_schema_name": "Marketing for Transmission Shops",
    "eyebrow": "For Transmission Shops",
    "h1_html": "Marketing <em>for Transmission Shops</em>",
    "answer_block": "Transmission shop marketing keeps you visible where an anxious driver looks the moment the transmission starts slipping or a dealer quote scares them, your Google Business Profile and the map pack, so the honest, well-reviewed shop that offers a free check is the one they call instead of the shop that let its listing go stale.",
    "sections": [
        {"h2_html": "Transmission demand is <em>local, sudden, and high-stakes</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody shops for a transmission specialist ahead of time. Demand appears the instant the car starts slipping, refuses to shift, or drops a puddle of red fluid on the driveway, and it is intensely local, because a driver is not going to risk a long trip on a transmission that might quit. It is also the highest-stakes repair most drivers ever face, a bill that can rival the value of the car, so they do not just want a shop nearby, they want one they can trust not to take them for a ride.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That makes the whole game being visible and trusted in your area at the exact moment someone nearby is scared about their transmission, not running clever ads to drivers whose cars are shifting fine. The spend that pays off is the kind that makes you easy to find and easy to trust in that moment, so being first, well reviewed, and clearly offering a free check beats being loud everywhere.</p>'},
        {"h2_html": "Your Google profile is where a driver decides <em>who will not oversell them</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone searches for a transmission shop near them, the map pack, those three local listings with the star ratings, is the first thing they see, above the websites and above the ads. A driver staring down a huge repair does not just glance at the stars, they read the reviews for one thing above all: honesty. Everyone has heard the story of a shop that pushed a full rebuild when a simple fix would have done, so they are hunting for the reviews that say this shop was straight with me, found the real problem, and did not sell me something I did not need. A profile full of recent reviews that say exactly that, next to current hours and photos of your bay, quietly beats one that has sat untouched for a year. Keeping it active and honest is a standing advertisement in the exact spot a worried driver looks.</p>'},
        {"h2_html": "Be the free second opinion after the <em>dealer's quote</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A big share of transmission calls start at the dealer. A driver takes the car in, gets handed a quote to replace the whole unit that makes their stomach turn, and walks out thinking there has to be a better option. The very next thing many of them do is search for an independent transmission shop for a second opinion. If your profile is the active, well-reviewed one that clearly offers a free check, you are the obvious place to take that quote, and often the honest diagnosis finds the real fault is far smaller than the dealer made it sound. Being visible and trusted for that exact searcher, the one already holding a scary quote, is some of the highest-value demand you can catch.</p>'},
        {"h2_html": "Show up in the towns you cover, and back your <em>referral partners</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Marketing to a whole metro is expensive and forgettable, and it brings calls from drivers too far out to trust a failing transmission on the drive over. Focusing on the specific towns and neighborhoods your customers actually come from, with a profile, photos, and content built around those areas, is what puts you in the map pack where the real work is, and it is a tighter, cheaper target than a citywide spend. A strong, well-reviewed public presence also backs up your other channels, the general repair shops and used-car lots that farm out transmission work look you up before they trust you with a customer, and a profile full of honest reviews makes those referrals easier to earn and keep. This is the public-facing side of the business, aimed at drivers who are not your customer yet; the private follow-up to the people already in your database is the CRM.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A dealer quote sends them searching, and you are <em>the shop they can see</em>",
        "body_html": "A driver takes a slipping car to the dealer and comes away with a rebuild quote that feels impossible. Sitting in the parking lot, they search for a transmission shop near them to get a second opinion. Because your Google profile has been kept active all year, with recent photos of your shop, current hours, and a steady flow of reviews about honest work and fair prices, you sit at the top of the map pack and you clearly offer a free check. You look like the safe place to take that scary quote, so they call you instead of the shop a friend vaguely mentioned once. The shop that let its profile go quiet is nowhere on the map. Illustrative example, not a client."},
    "faqs": [
        ("Do you post to my Google Business Profile for me?",
         "Yes. We keep it active with photos of your shop and the work, updates, and local content on a regular schedule, and keep your hours, services, and the free check you offer accurate and easy to find, so it looks current whenever a driver searches for a transmission shop near them."),
        ("What does focusing on my service area actually mean?",
         "It means building your profile and content around the specific towns and neighborhoods your customers actually come from, instead of spreading a budget across a whole metro. A driver will not nurse a failing transmission across the city, so the calls worth catching are the nearby ones, and that is where a tight local focus puts you."),
        ("Can you make my free check and second opinion stand out?",
         "Yes, and it is one of the most valuable things we can do. The free diagnostic is what turns a scared, price-shopping driver, especially one holding a dealer quote, into a booked visit, so we make it clear and easy to find on your profile and in your posts, right where a worried searcher is looking."),
        ("How is this different from the CRM follow-up?",
         "The CRM follows up privately with people already in your database, your free checks and open quotes. Marketing is the public side, your Google profile, your reviews, and your local visibility, aimed at a driver who is not your customer yet but needs to find and trust you the moment the transmission goes."),
        ("How long before I see it working?",
         "A neglected profile can climb in the map pack within weeks once it is active and complete, and it compounds from there as reviews and content build. Setup is included, and a free audit will show you what your current online presence looks like to a driver searching near you today.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for transmission shops"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-transmission-shops.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the transmission shop they <em>can already see</em>",
    "cta_sub": "Get a free audit of how visible you actually are in your service area and on Google right now, whether you work with us or not. No credit card, never a call center.",
},
# =================== Websites & SEO for Transmission Shops ===================
{
    "slug": "websites-seo-for-transmission-shops",
    "trade_slug": "transmission_shops", "trade_plural": "transmission shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
    "breadcrumb_leaf": "Websites & SEO for Transmission Shops",
    "title": "Websites & SEO for Transmission Shops | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Transmission Shops",
    "meta_desc": "A transmission shop website built for SEO ranks for transmission repair near me, puts your free check up front, and captures the call, not a lead-seller.",
    "service_schema_name": "Websites & SEO for Transmission Shops",
    "eyebrow": "For Transmission Shops",
    "h1_html": "Websites &amp; SEO <em>for Transmission Shops</em>",
    "answer_block": "A transmission shop website built for SEO ranks for what a driver searches when the transmission starts slipping, transmission repair near me, transmission rebuild cost, free transmission check, and puts your free diagnostic, warranty, and real reviews up front, so the big job comes to you instead of a directory renting your own calls back to you.",
    "sections": [
        {"h2_html": "The lead-sellers are not competing with you, they are <em>renting you back your own calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for a transmission shop in your town and the top of the page is often a directory, a national booking middleman, or a pay-per-lead service, not the local specialist. Those sites publish thousands of pages and have years of authority behind them, so a driver who searches lands there first, fills out a form, and that lead gets sold, sometimes to several shops at once, sometimes back to you for a fee out of your own margin. Your site not ranking is not a vanity problem. It is the reason a call you should have gotten for free gets sold to you, or handed to whoever is paying that week.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It stings more for transmission work than for almost any trade, because a single one of these calls is a high-ticket job, not an oil change. The driver searching has no loyalty yet, is scared, and is comparing shops, so the request gets shopped around and your best-paying job of the month goes wherever the middleman routes it, not to the shop with the most honest reputation. A site of your own turns that same search into a call that lands with you and nobody else, with the customer, the vehicle, and the problem in your hands from the first ring.</p>'},
        {"h2_html": "Rank for what a driver types when the <em>transmission starts slipping</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national directory this year for the broadest term, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you cover, and for the exact searches a driver makes when the transmission acts up: transmission repair near me, transmission shop near me, transmission rebuild cost, transmission slipping, transmission fluid leak, and the one that matters most for you, a free transmission check or a second opinion near me. Pages built around the work you actually do, rebuilds, replacements, diagnostics, clutches, and the areas you actually serve, are what search engines, and a driver who needs help now, reward with the click.</p>'},
        {"h2_html": "A worried, skeptical buyer needs <em>proof and a free way in</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone whose transmission is failing is on a phone, not a desktop, and they are scared they are about to be sold the most expensive repair on the car. The site has to load fast and put a tap-to-call button and your service area in front of them right away, but for transmission that is not enough. It has to earn trust before they will pick up the phone: the free diagnostic offered plainly at the top, a word on financing so the price does not scare them off, the warranty that backs your rebuilds, an honest explanation of when a transmission really needs a rebuild and when it does not, and real reviews from drivers you treated straight. That is what turns a skeptical second-opinion shopper into a booked free check instead of another tab they close.</p>'},
        {"h2_html": "The calls are <em>yours</em>, permanently",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you put into a pay-per-lead service disappears the day you stop paying, and the call was never really yours anyway. A website you own keeps ranking, keeps capturing calls and free-check requests, and keeps compounding in value for as long as it exists, and it is registered to you, not a platform that can drop you or route your driver to a chain. The site plugs into the same CRM that follows up on every lead it captures and the answering service that answers the calls it drives, so nothing it earns you slips away.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A second-opinion search finds <em>you</em>, not a directory",
        "body_html": "A driver a couple of towns over has a slipping transmission and a scary dealer quote, and they search transmission repair near me on their phone for a second opinion. Instead of a national directory that would sell the lead to three shops, they find your site ranking for that town, with a page about rebuilds and diagnostics, a free check offered right at the top, a note about financing and your warranty, and real reviews from drivers you were honest with. They can see you are the safe place to take that quote, so they call you directly, with no per-lead fee and no middleman anywhere in the chain. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the transmission and second-opinion searches a national directory has no reason to target well, which is exactly where a local specialist can win."),
        ("How is this different from paying for leads?",
         "A pay-per-lead service rents you a call that it also sells to other shops, and it stops the day you stop paying. A website you own captures calls and free-check requests that are yours alone and keeps working long after it is built, without a per-lead fee coming out of your biggest jobs."),
        ("Should I put rebuild prices on the site?",
         "You cannot honestly post a firm rebuild price, because the number depends on what the diagnostic finds, and trying to would only scare a driver off. What converts instead is offering the free check up front and being open about financing and the warranty, so a worried buyer sees a low-risk way in rather than a big number with no context."),
        ("Do people really contact a shop about a big repair online?",
         "For a repair this size most drivers still want to talk, and a fast site with a tap-to-call button gets them to you in one tap. But plenty will request the free check or send the symptoms first when the site makes it easy, and that gives you a scared, high-intent lead you can call back and win."),
        ("How long until it starts ranking?",
         "The tight local and transmission-specific searches can start moving within weeks, while the broadest terms build over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-auto.html", "Everything Top Shelf does for transmission shops"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-transmission-shops.html", "Staying visible in your service area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and lead-sellers taking your calls, whether you work with us or not. No credit card, never a call center.",
},
]
