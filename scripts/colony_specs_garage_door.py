"""Colony page specs for GARAGE DOOR COMPANIES (Home Services hub). generate_colony.py
loads every scripts/colony_specs_*.py and builds one lightweight question page per dict.

Each topic is ONE real question a garage-door-business owner would actually search, answered
directly up top (the 40-60 word AEO answer), then two short body sections, then a prominent
"the fix" bridge into the ONE money page that solves it. Nine distinct questions, a mix of
problem/symptom, how-to, and cost, spread across all seven garage-door money pages.

Honest by rule: no invented stats, prices, or clients; hedged where the truth is "it depends";
no dollar figures except the platform's own tiers. Voice is plain and peer-to-owner.
"""

TOPICS = [
# ================= 1. Missed call -> AI receptionist (problem) =================
{
    "slug": "missed-call-goes-to-competitor",
    "trade_slug": "garage-door-companies", "trade_plural": "garage door companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "Why Do Customers Call the Next Company When I Miss a Call?",
    "title": "Why Do Customers Call the Next Company When I Miss a Call? | Top Shelf Business Solutions",
    "meta_desc": "Miss a call and the homeowner with a trapped car just dials the next garage door company. Here is why it happens and how to answer every call and win the job.",
    "answer": "When a garage door breaks, the homeowner has a car trapped inside and calls three companies in a row. Whoever answers first usually wins the job. An AI receptionist picks up every call you miss while you are under a door, captures the details, and books the job before your competitor's phone even rings.",
    "sections": [
        {"h2_html": "A garage door problem is an <em>emergency</em>, and emergencies do not wait",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a spring snaps or a door jams shut with a car stuck inside, the homeowner is not casually shopping around. They have a problem right now, and they work straight down the list of garage door companies until someone picks up. If your phone rings while you are under a door, up on a ladder, or driving to the next job, the call rolls to voicemail, and most people do not leave one. They just dial the next number.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The job was not lost on price or on your reviews. It was lost because someone else answered first. In a same-day market, the company that picks up usually books the work, and the one that calls back an hour later reaches a homeowner who is already scheduled with somebody else. Every call you miss on a busy day is a job quietly handed to a competitor you never even knew you were bidding against.</p>'},
        {"h2_html": "You cannot answer the phone while you are <em>fixing a door</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The honest part is that you cannot run a repair with a phone pressed to your ear, and hiring a full-time person just to sit by the line does not pencil out for most shops. So the calls you miss are not a discipline problem you can fix by trying harder. They are a math problem, and they get worse exactly when the work gets busy and the jobs are most worth having.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap does not mean chaining yourself to the phone. It means having something answer for you the moment you cannot, in a normal conversational voice, that finds out whether it is a broken spring, a door off its track, or a dead opener, then books the job on your real schedule and texts you the details. The homeowner gets a helpful answer in seconds instead of a beep, and you hear about the job while it is still yours to win.</p>'}],
    "bridge_h2": "The fix is an <em>AI receptionist</em> that never misses",
    "bridge_text": "The reason you lose these jobs is simple: you cannot answer while you are fixing a door. An AI receptionist for garage door companies picks up every call you miss, finds out what broke, and books the job on your schedule, so the homeowner reaches a helpful voice in seconds instead of dialing your competitor. You keep your own number, and every call stays yours.",
    "bridge_slug": "ai-receptionist-for-garage-door-companies",
    "bridge_label": "See the AI receptionist",
    "faqs": [
        ("Will an AI receptionist sound like a robot to my customers?",
         "No. It answers in a natural, conversational voice and handles the basics a caller needs, what broke, where they are, and when you can come out. Most callers just want a fast, helpful answer, and a human-sounding pickup in seconds beats a voicemail every time. Anything it cannot handle, it routes to you."),
        ("What happens to the call if the AI cannot handle it?",
         "It takes the details and hands the call to you with a text, so nothing is lost. You set which situations get sent straight through, so a true emergency reaches you right away while routine bookings are handled without pulling you off the job you are on.")],
},
# ================= 2. Quotes go nowhere -> CRM (problem) =================
{
    "slug": "replacement-quotes-go-nowhere",
    "trade_slug": "garage-door-companies", "trade_plural": "garage door companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "Why Do My Garage Door Replacement Quotes Go Nowhere?",
    "title": "Why Do My Garage Door Replacement Quotes Go Nowhere? | Top Shelf Business Solutions",
    "meta_desc": "Your garage door replacement quotes go nowhere because nobody follows up. Here is why homeowners go quiet and how to turn old quotes into booked installs.",
    "answer": "Your replacement quotes go nowhere because nobody follows up. A homeowner gets your price on a new door, says they need to think about it, then buys from whichever company called back. A CRM follows up for you, by text and email, on a schedule you set, so the quotes you already sent keep turning into booked installs.",
    "sections": [
        {"h2_html": "A new door is a <em>considered purchase</em>, not an impulse buy",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A broken spring gets fixed today, but a full door replacement is a big spend the homeowner sits on. They get your number, maybe two others, and then life gets in the way. They are not ignoring you, they just went quiet, and quiet is where most replacement jobs die. Weeks later they finally decide to move, and by then the company on their mind is whoever happened to check in last.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">You already did the hard part. You took the call, drove out, measured, and priced the job. Letting that quote sit with no follow-up is leaving finished work on the table, because the homeowner was never a no. They were a not yet, and not yet is exactly the customer a little timely attention turns into a booked install.</p>'},
        {"h2_html": "Following up on every quote by hand <em>never actually happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every owner means to circle back on open quotes. Then the phone rings, a truck needs a part, three jobs run long, and the sticky note with the homeowner name gets buried. Manual follow-up is the first thing to slip in a busy week, and the bigger the quote, the longer the homeowner tends to take, which is precisely when your memory of them fades.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The answer is not more willpower, it is a system that remembers for you. When every quote, repair customer, and lead lives in one place, a few well-timed check-ins can go out on their own, by text and email, on a cadence you approve. The homeowner still deciding on a door hears from you at the right moment instead of hearing nothing, so your pipeline stops depending on which name you happen to remember on a slow afternoon. And because it all runs off one list, you can see at a glance which quotes are still open and which homeowners are heating up, so the ten minutes you do have goes to the person closest to saying yes instead of a name picked at random.</p>'}],
    "bridge_h2": "The fix is a <em>CRM</em> that follows up for you",
    "bridge_text": "Your quotes are not bad, they just go quiet. A CRM for garage door companies keeps every replacement quote and repair customer in one place and follows up automatically, by text and email, on a schedule you set. The homeowner still deciding on a new door hears from you again at the right moment, so the estimate you already did the work for turns into a booked install.",
    "bridge_slug": "crm-for-garage-door-companies",
    "bridge_label": "How the CRM follows up",
    "faqs": [
        ("Does the CRM follow up on old quotes I already sent?",
         "Yes. You can bring in the quotes and customers you already have, and the CRM starts following up on the ones sitting quiet, by text and email, on a schedule you approve. Estimates you did the work for weeks ago can still turn into booked jobs."),
        ("Will the follow-up feel pushy to the homeowner?",
         "Not if it is set up right. A couple of helpful, well-timed check-ins remind a homeowner you are ready when they are, which is what most people actually want after getting a quote. You control the timing and the wording, and you can step in and message anyone directly.")],
},
# ================= 3. Website cost -> Websites & SEO (cost) =================
{
    "slug": "garage-door-website-cost",
    "trade_slug": "garage-door-companies", "trade_plural": "garage door companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "How Much Does a Garage Door Company Website Cost?",
    "title": "How Much Does a Garage Door Company Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "What a garage door website costs depends on whether it is a template, a freelancer, or a full agency build. Here is what really drives the price.",
    "answer": "It depends on what you are actually buying. A do-it-yourself template is cheap monthly but you build and maintain it, a freelancer costs more, and a full agency build costs the most. What matters more than the sticker price is whether the site ranks and books jobs or just sits there looking nice.",
    "sections": [
        {"h2_html": "The price swings on <em>what the site is built to do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Two garage door websites can cost wildly different amounts and look similar on the surface, so the sticker price alone tells you almost nothing. What you are really paying for is the work underneath: whether the site is built to rank for the searches homeowners actually type, whether it loads fast on a phone at the side of the road, and whether a visitor can call you in one tap or has to hunt for a number.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Roughly, the tiers go like this. A template builder is the cheapest and puts a page online, but the ranking, speed, and lead capture are on you. A freelancer costs more and can look sharp, though quality varies a lot. A full build costs the most and is meant to bring in jobs, not just exist. Cheapest is not the goal, and neither is most expensive. The goal is a site that pays for itself.</p>'},
        {"h2_html": "A site that does not <em>bring in jobs</em> is the expensive one",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The trap is judging a website by its monthly cost instead of what it earns. A cheap page that never ranks and never gets a call is not a bargain, it is money spent on something that does nothing. A site that shows up when a homeowner searches garage door repair near me, and turns that visit into a booked job, pays for itself many times over even if it costs more up front.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Two other things move the real cost. First, ownership: a site you own keeps working and stays yours, while a rented profile on a lead site can vanish or resell your calls the day you stop paying. Second, whether search work is included, because a beautiful site nobody can find is just an expensive brochure. The honest answer to what yours should cost depends on where you are starting from, which is exactly what a free audit is for.</p>'}],
    "bridge_h2": "What you should actually <em>pay for</em>",
    "bridge_text": "The real question is not the sticker price, it is whether the site earns its keep. A website built for garage door companies is built to rank for searches like garage door repair near me, load fast on a phone, and turn a visitor into a call, instead of just looking nice. Start with a free audit and we will show you what your current site is doing for you and what a better one would cost for your situation.",
    "bridge_slug": "websites-seo-for-garage-door-companies",
    "bridge_label": "See websites and SEO",
    "faqs": [
        ("Why does one garage door website cost so much more than another?",
         "Because you are buying different things. A cheap template gets you a page that exists. A build worth paying for is designed to rank for local searches, load fast on a phone, and turn visitors into calls, and it is owned by you, not rented from a platform you cannot leave with your traffic."),
        ("Is a cheap do-it-yourself website builder good enough?",
         "It can put something online, and for some shops that is a start. The catch is that it is on you to make it rank, keep it fast, and turn visits into calls, which is the part that actually brings in jobs. A free audit will show you honestly whether yours is pulling its weight.")],
},
# ================= 4. More reviews -> Review software (how-to) =================
{
    "slug": "get-more-garage-door-reviews",
    "trade_slug": "garage-door-companies", "trade_plural": "garage door companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "How Do I Get More Garage Door Reviews on Google?",
    "title": "How Do I Get More Garage Door Reviews on Google? | Top Shelf Business Solutions",
    "meta_desc": "Most happy garage door customers would leave a review if you asked at the right moment. Here is how to get more Google reviews without chasing anyone.",
    "answer": "Most of your happy garage door customers would leave a review if you asked at the right moment and made it one tap. Review software sends that ask automatically right after the job is done, by text, with a link straight to your Google profile, so you stop depending on the few who remember on their own.",
    "sections": [
        {"h2_html": "The problem is not unhappy customers, it is <em>timing and asking</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You fix doors well and most customers are glad you came. The trouble is that a happy customer with a working door goes right back to their day and never thinks to post about it. Nobody wakes up planning to review a garage door repair. So the reviews you have came from the rare person who went out of their way, and that trickle does not match the amount of good work you actually do.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Asking in person feels awkward, and asking days later means the moment has passed and the details are fuzzy. Meanwhile the homeowner choosing a company tomorrow is reading the profile with the recent wall of reviews, not the one with eight from two years ago. The gap between the work you do and the reputation people see is a timing and asking problem, and both are fixable.</p>'},
        {"h2_html": "Ask right after the job, and make it <em>one tap</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The best moment to ask is right after the door is working again, while the relief is fresh. The reliable way to catch that moment every time is to automate it: the second a job is marked done, a text goes out thanking the customer with a link that drops them straight onto your Google profile, so leaving a review takes one tap instead of a hunt. No cornering people, no sticky notes, no asking three weeks later.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Two things make it compound. Reply to every review, good or bad, because a calm, professional response to a rare critical one often reassures the next reader more than a spotless record would, and responding is a signal that helps you show up in local search. And keep the requests honest: ask every customer, never filter out the unhappy ones and never pay for reviews. Do it steadily and recent reviews keep feeding your profile, which brings more calls, which brings more reviews.</p>'}],
    "bridge_h2": "The fix is <em>review software</em> that asks for you",
    "bridge_text": "You have done plenty of good work. It just is not showing up on Google, because happy customers forget to post and asking in the moment feels awkward. Review software for garage door companies sends the ask automatically right after the job, makes leaving a review one tap, and helps you reply to each one, so your reputation starts matching the work you actually do.",
    "bridge_slug": "review-software-for-garage-door-companies",
    "bridge_label": "See the review system",
    "faqs": [
        ("Is it against Google's rules to ask customers for reviews?",
         "Asking every customer for an honest review is allowed and encouraged. What is not allowed is filtering out unhappy customers or paying for reviews, and this does not do that. It simply asks everyone at the right moment and makes leaving one easy."),
        ("When does it ask the customer for a review?",
         "Right after the job is finished, when the door is working again and the customer is happiest, sent automatically by text with a one-tap link to your Google profile. You can adjust the timing and the wording so it sounds like you, not like a form letter.")],
},
# ================= 5. Book tune-ups -> Online booking (how-to) =================
{
    "slug": "book-tune-ups-online",
    "trade_slug": "garage-door-companies", "trade_plural": "garage door companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "How Do I Book Garage Door Tune-Ups Without the Phone Tag?",
    "title": "How Do I Book Garage Door Tune-Ups Without the Phone Tag? | Top Shelf Business Solutions",
    "meta_desc": "Stop playing phone tag over garage door tune-ups. Here is how online booking lets homeowners self-schedule on your real availability, straight to your calendar.",
    "answer": "Seasonal tune-ups are easy money that phone tag kills. A booking link lets a homeowner pick a tune-up slot straight from your website or a text, on your real availability, without reaching you first. You wake up to the appointment already on your calendar instead of a voicemail you now have to chase down.",
    "sections": [
        {"h2_html": "Tune-ups lose to <em>phone tag</em> more than to price",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A tune-up is not an emergency, so it is the first thing that falls off when scheduling it turns into work. A homeowner remembers their door has gotten loud, thinks they should get it serviced, and calls. You are on a job, so you call back that evening, they miss it, and after a round of voicemails the whole thing quietly drops. Nobody decided not to book. The back and forth just wore the intention down.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is a shame, because maintenance is some of the best work you can carry. It fills the slow gaps between emergency calls, it is predictable, and a customer whose door you tuned is the one who calls you first when a spring finally goes. Every tune-up lost to phone tag is a booked hour and a future repair customer walking away over nothing but scheduling friction.</p>'},
        {"h2_html": "Let homeowners book themselves, on <em>your</em> real availability",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The way to remove the friction is to let the homeowner grab a time the moment they feel like it, without needing to reach you first. A booking link sits on your website, your Google profile, and the text you send after a call, and it only ever shows the times you are genuinely open, because it reads your real calendar. They pick a slot, it lands on your schedule with their address and what the door is doing, and the phone tag never starts.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">You stay in control of the rules. You set how much notice you need, how long a tune-up runs, and how much drive-time buffer to leave between stops, so nothing double-books you against a repair you already have. Automatic confirmations and reminders go out on their own, which is the single biggest lever on no-shows, so the tune-up you booked while asleep actually shows up. Every booking also drops into the same customer list as your repairs, so the appointment and the customer history live together instead of on a separate pad by the phone.</p>'}],
    "bridge_h2": "The fix is <em>online booking</em> homeowners can use anytime",
    "bridge_text": "Phone tag is the whole problem, and a booking link removes it. Online booking for garage door companies lets a homeowner grab a tune-up or service slot straight from your website, your Google profile, or a text, on your real availability. It lands on your calendar with the details and sends the reminders that cut down no-shows, so seasonal work stops slipping away to voicemail.",
    "bridge_slug": "online-booking-for-garage-door-companies",
    "bridge_label": "See online booking",
    "faqs": [
        ("Will online booking double-book me against a job I am already on?",
         "No. It reads your real calendar and only offers times you are actually free, and you set how much notice you need and how much drive-time buffer to leave between jobs. A tune-up cannot land on top of a repair you already have scheduled."),
        ("Can homeowners still call instead of booking online?",
         "Of course. Online booking is another way in, not the only one. Some people prefer to book themselves late at night, others want to talk it through, and both work. It pairs with the AI receptionist, which can book a caller who would rather not tap through a form.")],
},
# ================= 6. Auto follow-up after repair -> Automation (how-to) =================
{
    "slug": "follow-up-after-repair-automatically",
    "trade_slug": "garage-door-companies", "trade_plural": "garage door companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "How Do I Follow Up After a Garage Door Repair Automatically?",
    "title": "How Do I Follow Up After a Garage Door Repair Automatically? | Top Shelf Business Solutions",
    "meta_desc": "Most garage door companies never follow up after a repair. Here is how to send thank-yous, review asks, and tune-up reminders automatically and win repeat work.",
    "answer": "After a repair, most companies never reach out again, so the customer forgets who fixed their door. Automation sends a thank-you and a review request right after the job, then a tune-up reminder months later, all on a schedule, so one repair turns into repeat work without you remembering to send anything.",
    "sections": [
        {"h2_html": "The job ends, and so does the <em>relationship</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For most garage door shops, the customer relationship ends the moment the truck pulls away. You fixed the door, they paid, and that was that. Then a year later the same customer needs a new opener, cannot remember your name, and searches from scratch, so you compete for a customer you already earned once. The work you did built goodwill, and letting it go silent lets that goodwill quietly expire.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Repeat and referral work is the cheapest business you can get. It costs nothing to acquire and the trust is already there. But staying in touch by hand across every customer you have ever served is impossible during a normal week, so the follow-up that would keep those people yours simply never gets sent, and the door you fixed becomes somebody else next job.</p>'},
        {"h2_html": "Put the after-the-job touches <em>on a schedule</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reliable way to stay in touch is to stop relying on memory. When a job is marked done, a short sequence can run on its own: a thank-you text that day, a review request while the customer is happiest, and a tune-up or safety-check reminder months later when it makes sense for the kind of work you did. You set the timing once, and it goes out for every customer whether you are slammed or on vacation.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is not about replacing the calls that need a real conversation. You still handle those. It is about making sure the easy, high-value touches actually happen instead of getting buried. Done steadily, one repair becomes a review, a repeat visit, and a referral, and your past customer list turns into a source of work you are not currently tapping. None of it depends on the season or on how slammed you happen to be, which is the whole point, because the weeks you are too busy to think about follow-up are exactly the weeks it keeps running quietly in the background.</p>'}],
    "bridge_h2": "The fix is <em>automation</em> that runs after the job",
    "bridge_text": "The work does not have to end when the truck pulls away. Automation for garage door companies sends the thank-you, the review request, and the tune-up reminder on a schedule, all tied to the job you just finished. One repair becomes a review, a repeat visit, and a referral, without you keeping a mental list of who to text and when.",
    "bridge_slug": "automation-for-garage-door-companies",
    "bridge_label": "See how automation works",
    "faqs": [
        ("Does this replace calling my customers personally?",
         "No. It handles the routine touches, the thank-you, the review ask, and the tune-up reminder, so they actually go out on time. You still make the real calls that need a conversation. It just makes sure the easy follow-ups do not get forgotten during a busy week."),
        ("How does it know when to send a tune-up reminder?",
         "It works off the job you completed and a schedule you set, so a customer who had a repair or a new door gets a reminder months later when a tune-up makes sense. You decide the timing, and it goes out without you tracking dates by hand.")],
},
# ================= 7. Not on the map -> Marketing (problem) =================
{
    "slug": "not-showing-on-google-maps",
    "trade_slug": "garage-door-companies", "trade_plural": "garage door companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "Why Doesn't My Garage Door Company Show Up on Google Maps?",
    "title": "Why Doesn't My Garage Door Company Show Up on Google Maps? | Top Shelf Business Solutions",
    "meta_desc": "Your garage door company does not show up on Google Maps because your profile is thin. Here is why the map pack ignores you and how to get into it.",
    "answer": "You do not show up on Google Maps because your Business Profile is thin, unverified, or sitting untouched next to competitors who post and collect reviews every week. Getting into the local map pack takes a complete, active profile, steady fresh reviews, and consistent local presence, which is what garage door marketing keeps running for you.",
    "sections": [
        {"h2_html": "The map pack rewards profiles that <em>stay active</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a homeowner searches garage door repair near them, the three businesses in the map box at the top get the bulk of the calls, and most people never scroll past them. Landing there is not luck or paid placement. Google leans on how complete and active your Business Profile is, how close you are to the searcher, how many recent reviews you have, and whether the profile looks alive or abandoned.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is usually why you are missing. A profile that is unclaimed, half filled out, or untouched for months reads as stale next to a competitor posting photos of finished doors and gathering reviews every week. You are not being punished. You are just being outworked by a business that treats its profile as the storefront it now is, while yours sits closed.</p>'},
        {"h2_html": "Getting seen is <em>upkeep</em>, not a one-time setup",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The first step is the boring one: claim and verify the profile, then fill in every field, the service area you actually cover, hours, services, and real photos of your work. That alone puts a lot of shops ahead of a competitor who never bothered. But a complete profile is the floor, not the finish, because Google favors the businesses that keep showing signs of life.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Staying visible means steady upkeep: regular posts, fresh photos, a reliable flow of new reviews, and the same name, address, and phone number everywhere you appear online. It builds over weeks and months, not overnight, and anyone promising instant top placement is not being straight with you. The work is simple but constant, which is exactly the kind of thing that slides when you are busy actually fixing doors. It also helps to keep your listing details matching your website and your other profiles, because a wrong phone number or conflicting hours makes Google trust the listing less and quietly pushes you further down the results.</p>'}],
    "bridge_h2": "The fix is <em>local marketing</em> that keeps you visible",
    "bridge_text": "Showing up on the map is not luck, it is upkeep. Marketing for garage door companies keeps your Google Business Profile complete and active, pushes fresh posts and photos, and builds the steady reviews and local presence that lift you into the map pack. When a homeowner searches garage door repair near them, you are the one they see first instead of a competitor.",
    "bridge_slug": "marketing-for-garage-door-companies",
    "bridge_label": "How local marketing works",
    "faqs": [
        ("Why do competitors show up on the map when I do not?",
         "Usually because their Google Business Profile is complete, verified, and active, with recent posts and a steady stream of reviews, while an untouched profile looks abandoned to Google. The map pack rewards profiles that stay current, which is exactly the upkeep most busy shops let slide."),
        ("How long until I start showing up in local results?",
         "It builds over weeks and months, not overnight, as the profile fills out and reviews come in. There is no switch that puts you at the top instantly, and anyone promising that is not being straight with you. A free audit will show you where you stand today.")],
},
# ================= 8. After-hours calls -> AI receptionist (problem) =================
{
    "slug": "losing-after-hours-calls",
    "trade_slug": "garage-door-companies", "trade_plural": "garage door companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "Why Do I Lose After-Hours Garage Door Calls?",
    "title": "Why Do I Lose After-Hours Garage Door Calls? | Top Shelf Business Solutions",
    "meta_desc": "A garage door emergency at 9 p.m. goes to whoever answers. Here is why you lose after-hours calls and how to capture them without being on call all night.",
    "answer": "A spring snaps at 9 p.m. and the homeowner cannot get their car out, so they call until someone answers. If your line goes to voicemail after hours, that emergency job goes to whoever picks up. An AI receptionist answers nights and weekends, books the job, and flags the true emergencies for you.",
    "sections": [
        {"h2_html": "Garage door emergencies do not <em>keep business hours</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Doors break at the worst times. A spring lets go as someone heads out for work early, or the door refuses to close at night and the family will not leave the house wide open. These are the calls people make when they are stressed and cannot wait until morning, and they are often the most profitable jobs of the week. They are also the ones a nine-to-five voicemail greeting hands straight to a competitor.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A homeowner in that spot does not leave a message and wait. They call the next company, and the one after that, until a person answers. So the issue is not that after-hours demand is small. It is that the demand is real and urgent, and a recording is the one thing guaranteed to send it elsewhere. You lose the job before you ever knew it existed.</p>'},
        {"h2_html": "You should capture the call <em>without living on call</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The trap most owners fall into is answering the phone at all hours themselves, which burns you out and still misses calls when you are asleep or on another line. Hiring an overnight answering service is expensive and often means a stranger reading a script who cannot actually book a garage door job. Neither option fits a shop that just wants to stop losing good after-hours work.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The better answer is something that picks up every night-and-weekend call for you, talks like a normal person, and sorts a true emergency from a call that can wait until morning. It books the routine ones onto tomorrow schedule and alerts you only for the situations you decide are worth the interruption, like a car trapped inside or a door stuck open. You capture the job and still get your evening back. The calls it books do not sit in a voicemail box waiting for morning either, they land on your schedule overnight, so you start the day with the work already lined up instead of a list of missed numbers to chase.</p>'}],
    "bridge_h2": "The fix is an <em>AI receptionist</em> for nights and weekends",
    "bridge_text": "Emergencies do not keep business hours, and neither should your phone. An AI receptionist for garage door companies answers after hours and on weekends, finds out whether it is a true emergency like a snapped spring or a trapped car, books the job, and alerts you, so the late-night calls you used to lose to voicemail turn into the first appointment on tomorrow's schedule.",
    "bridge_slug": "ai-receptionist-for-garage-door-companies",
    "bridge_label": "How the AI receptionist works",
    "faqs": [
        ("Do I have to answer every after-hours call myself now?",
         "No, that is the point. The AI receptionist answers nights and weekends for you, books what it can, and only alerts you for the situations you decide are worth waking up for, like a true emergency. You capture the job without being on call around the clock."),
        ("Can it tell a real emergency from a call that can wait?",
         "It asks the questions that sort that out, whether a car is trapped, whether the door is stuck open and the house is exposed, and flags those for you while booking the routine calls for the next day. You set the rules for what counts as urgent.")],
},
# ================= 9. Losing to better websites -> Websites & SEO (problem) =================
{
    "slug": "losing-jobs-to-better-websites",
    "trade_slug": "garage-door-companies", "trade_plural": "garage door companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "Why Do I Lose Garage Door Jobs to Companies With Better Websites?",
    "title": "Why Do I Lose Garage Door Jobs to Companies With Better Websites? | Top Shelf Business Solutions",
    "meta_desc": "Homeowners pick the garage door company with the better website. Here is why you lose jobs before the call and how a stronger site wins the comparison.",
    "answer": "A homeowner comparing three garage door companies clicks the one whose website looks trustworthy and loads fast on a phone. If your site is dated, slow, or missing, you lose the job before the call, even when your work is better. A modern site built to rank and convert wins that comparison for you.",
    "sections": [
        {"h2_html": "The homeowner judges your work by your <em>website first</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before anyone experiences your work, they see your website, and they decide fast. A homeowner comparing a few garage door companies opens each site on their phone and, within seconds, forms an opinion about who looks legitimate and safe to let into their home. A clean site that loads quickly, shows real reviews, and lists the service area earns the call. A slow, dated, or missing site quietly loses it, no matter how good you are with an actual door.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is the frustrating part. You may be the more skilled and more honest company, but the homeowner cannot see that yet. They can only see the storefront, and right now a competitor with a better-built site is walking off with jobs you would have done better. The comparison is happening whether you compete in it or not.</p>'},
        {"h2_html": "A site built to <em>rank and convert</em> wins before the call",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Winning that comparison comes down to a few concrete things, not fancy design. The site has to load fast on a phone, because a homeowner with a broken door will not wait for a slow page. It has to build trust immediately, with reviews, your service area, and clear proof you are a real local company. And it has to make calling you the obvious next step, with a tap-to-call number that follows them down the page.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">There is an earlier win too. A site built to rank shows up when someone searches garage door repair near me, so you are in the comparison in the first place instead of never being seen. Getting found and then earning the click are two halves of the same job, and a site you own does both and keeps the lead yours, instead of a lead site reselling the same call to three companies. Owning the site also means the reviews, the photos, and the traffic keep building for you over time instead of disappearing the day you stop paying a middleman.</p>'}],
    "bridge_h2": "The fix is a <em>website</em> built to win the comparison",
    "bridge_text": "When a homeowner is choosing between you and two other companies, the website is the audition. A site built for garage door companies loads fast on a phone, shows your reviews and service area, and makes calling you the obvious next step, so you win the jobs you are currently losing before the phone even rings. Start with a free audit of how yours stacks up today.",
    "bridge_slug": "websites-seo-for-garage-door-companies",
    "bridge_label": "How websites and SEO work",
    "faqs": [
        ("My work is better than my competitor's. Why does their website win?",
         "Because the homeowner cannot see your work yet, they can only see your website. If theirs loads fast, shows reviews, and makes calling easy while yours is dated or slow, they click theirs first. A better site lets your reputation do its job before the call."),
        ("Does the website really matter if most of my jobs come from referrals?",
         "It matters more than it seems. Even a referred customer often looks you up before calling, and a weak or missing site can plant doubt right when they were about to trust you. The site backs up the referral instead of quietly undercutting it.")],
},
]
