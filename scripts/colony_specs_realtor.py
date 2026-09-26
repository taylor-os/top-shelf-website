"""Colony question pages for real estate agents (plan §5 colony template). generate_colony.py
imports TOPICS from every scripts/colony_specs_*.py. Each dict is ONE real question an agent
would search, answered directly up top, then funneled to the money page that solves it via the
"the fix" bridge. Lighter than a money page: H1 = one question, a 40-60 word answer, 2 body
sections, the bridge to the ONE implied money page + the Real Estate hub, a 2-question FAQ.

Bridges spread across the 7 realtor money pages (crm and websites-seo each carry two). Honest,
no invented stats or prices (only Top Shelf's real published prices appear), no em/en dashes.
"""

TOPICS = [
# ============================ Q1 -> AI Receptionist (problem) ============================
{
    "slug": "why-buyers-hire-the-first-agent",
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "h1": "Why Do Buyers Hire The Agent Who Answers First?",
    "title": "Why Do Buyers Hire The Agent Who Answers First? | Top Shelf Business Solutions",
    "meta_desc": "Buyers hire the agent who answers first because a home feels urgent, and the first real response earns their trust. A missed call is usually a lost client.",
    "answer": "Buyers hire the agent who answers first because buying a home feels urgent, and the first real person to pick up earns the trust before anyone else gets a chance. When you are in a showing and a call goes to voicemail, that buyer usually just dials the next agent on the list.",
    "sections": [
        {"h2_html": "A buyer's call is a <em>timer</em>, not a message",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a buyer calls about a listing, they are not leaving a message and settling in to wait. They are working down a list, and the first agent who picks up and sounds like they know the property is usually the one who gets the appointment. A home is an emotional, time-sensitive purchase, and the buyer reads a fast answer as a sign you will be easy to work with once things get real.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail breaks that. By the time you call back between showings, the buyer has often already reached someone else, booked the tour, and started building a rapport you now have to compete with. The call was never a low-quality lead. It was a good lead that went to whoever answered, and answering is the one part most agents cannot control while they are standing in someone else\'s living room.</p>'},
        {"h2_html": "You cannot answer from inside a <em>showing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The hard part is that the busier you are, the more calls you miss. The afternoon you are running three showings is the same afternoon new buyers are calling, and you physically cannot step out mid-tour to take every one. Nights, weekends, and open houses are worse, and those are exactly the hours motivated buyers pick up the phone to ask about a place they just drove past.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The answer is not to somehow take more calls yourself. It is to make sure every call gets answered by someone, instantly, so no buyer ever hits voicemail and moves on. A caller who reaches a warm, professional greeting, gets their basic questions handled, and has a time booked stays your lead, whether you were free at that moment or not. That is speed to lead, and in real estate it is often the whole ballgame.</p>'}],
    "bridge_h2": "An AI receptionist that answers on the <em>first ring</em>",
    "bridge_text": "An AI receptionist answers every call the second it comes in, day or night, even when you are mid-showing or asleep. It greets the caller in a natural voice, answers the basic questions about a listing, captures their details, and can book the showing on your calendar, then hands you the lead so you follow up as the agent who was there first. You stop losing buyers to voicemail.",
    "bridge_slug": "ai-receptionist-for-real-estate-agents",
    "bridge_label": "See the AI receptionist",
    "faqs": [
        ("What does the receptionist do that my voicemail does not?",
         "Voicemail makes a motivated buyer stop and wait, which most of them will not do. The AI receptionist actually talks to the caller, answers their questions about the listing, captures who they are and what they want, and can book the showing, so the lead is handled instead of parked."),
        ("Will callers know it is not a live person?",
         "It answers in a natural voice and handles the common questions smoothly, and most callers simply feel taken care of. Anything it cannot answer it captures and routes to you right away, so a real person follows up quickly instead of the caller reaching a dead end.")],
},
# ============================ Q2 -> CRM (problem/symptom) ============================
{
    "slug": "why-real-estate-leads-go-cold",
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "h1": "Why Do My Real Estate Leads Keep Going Cold?",
    "title": "Why Do My Real Estate Leads Keep Going Cold? | Top Shelf Business Solutions",
    "meta_desc": "Real estate leads go cold because most buyers and sellers are months from transacting and forget you without follow-up. The lead was rarely bad, just neglected.",
    "answer": "Real estate leads go cold because most buyers and sellers are months away from transacting, and without steady follow-up they simply forget who you are. The lead was rarely bad. It just needed a light touch every few weeks, which is the thing there is never time for between showings and closings.",
    "sections": [
        {"h2_html": "The lead was fine. The <em>follow-up</em> was the problem",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A buyer calls in March who is not ready until August. A homeowner says they are thinking about selling next year. Neither of those is a bad lead, but both disappear if nobody stays in touch, because by the time they are ready they have forgotten your name and called whoever was in front of them last. In real estate the money is in the months between the first contact and the closing, and that gap is where most leads quietly slip away.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The reason is not laziness. It is that a light, human check-in every few weeks across dozens of people is impossible to run out of your head while you are also showing homes, writing offers, and getting to closings. So the follow-up that would have kept the lead warm never happens, and the lead goes cold on its own.</p>'},
        {"h2_html": "A database you cannot work by <em>memory</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You cannot personally remember to touch four hundred contacts on the right schedule, so most of them sit untouched. That includes your past clients and your sphere, which are the cheapest business you will ever get, and the easiest to lose to an agent who simply stayed in contact.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>New leads that come in during a busy week get a first reply and then nothing.</li><li>Buyers who are months out drift because there is no system reminding you to reach back.</li><li>Past clients forget you between transactions, so the referral goes to whoever they saw most recently.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Fixing it is not about working harder. It is about a system that follows up for you, on a schedule you set, so a lead staying warm no longer depends on you remembering.</p>'}],
    "bridge_h2": "A CRM that <em>follows up for you</em>",
    "bridge_text": "A CRM keeps every lead, past client, and sphere contact in one place and works them on a schedule you set, with texts and emails that go out on time whether or not you remember. The buyer who is half a year out still hears from you, still sees your name, and still calls you when they are ready. Your database quietly becomes your pipeline instead of a list of people who forgot you.",
    "bridge_slug": "crm-for-real-estate-agents",
    "bridge_label": "See the CRM",
    "faqs": [
        ("How is this different from just setting reminders?",
         "Reminders still depend on you doing the task every time. A CRM sends the check-ins, market notes, and anniversary touches for you on the cadence you approve, and only pulls you in when a lead actually needs a personal call, so nothing slips just because you had a busy week."),
        ("Does it help with past clients or only new leads?",
         "Both, and past clients are where the quiet money is. Repeat business and referrals close faster and cost nothing to get, and the CRM keeps you in front of those people automatically so that business shows up instead of going to whoever they happened to see most recently.")],
},
# ============================ Q3 -> Online Booking (problem/how-to) ============================
{
    "slug": "stop-phone-tag-over-showings",
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "h1": "How Do I Stop Playing Phone Tag Over Showings?",
    "title": "How Do I Stop Playing Phone Tag Over Showings? | Top Shelf Business Solutions",
    "meta_desc": "Stop phone tag over showings with a booking link where buyers find you, so they self-schedule on your real calendar and the appointment lands automatically.",
    "answer": "Stop playing phone tag by putting a booking link where buyers already find you, so they pick an open showing time themselves instead of waiting for a callback. The link reads your real calendar, offers only times you are free, and drops the appointment straight onto your schedule with the details attached.",
    "sections": [
        {"h2_html": "Phone tag quietly costs you <em>appointments</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A buyer wants to see a place. You are with another client, so you call back an hour later, they do not pick up, you trade voicemails, two days pass, and they tour it with the agent who could lock in a time on the spot. The appointment was never the problem. The back and forth was. When someone is motivated enough to reach out, making them wait for a callback is the fastest way to lose them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A booking link lets them grab an open slot the moment they feel it, day or night, without reaching you first. You stop chasing people to schedule the thing they already asked for, and you wake up to appointments that set themselves overnight.</p>'},
        {"h2_html": "Self-scheduling, but on <em>your</em> rules",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Letting buyers book themselves does not mean losing control of your calendar. You set how much notice you need, how long each appointment runs, how much buffer to leave for driving across town, and which hours are open at all. The form can ask a few questions first, so a serious buyer books a showing and a maybe gets a quick call from you instead.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Because it reads the calendar you already use, it can never double-book you against a closing or another showing, and it sends the client a confirmation and a reminder, which is what actually cuts down no-shows. Put the link on your listings, your site, your email signature, and the text you send after a sign call, and every one of those becomes a place someone can book you in one tap.</p>'}],
    "bridge_h2": "Online booking that <em>ends the phone tag</em>",
    "bridge_text": "Online booking lets a buyer or seller pick a showing or a listing consult straight from your website, your listings, or a text link, on your real availability, so the appointment lands on your calendar with the details you need to show up ready. It syncs to the calendar you already use, sends confirmations and reminders, and works alongside the AI receptionist for callers who would rather talk than tap.",
    "bridge_slug": "online-booking-for-real-estate-agents",
    "bridge_label": "See online booking",
    "faqs": [
        ("Will it double-book me against a showing I already have?",
         "No. It reads your real Google or Outlook calendar and only ever offers times you are actually free, and new bookings drop straight onto that calendar. You can also set buffers so you are never booked with no time to drive between properties."),
        ("Can buyers and sellers book different types of appointments?",
         "Yes. You can offer a buyer showing and a seller listing consult as separate types, each with its own questions and length, so every booking captures the details you need for that kind of meeting before it ever hits your calendar.")],
},
# ============================ Q4 -> Review Software (how-to) ============================
{
    "slug": "how-to-get-more-realtor-reviews",
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "h1": "How Do I Get More Reviews As A Realtor?",
    "title": "How Do I Get More Reviews As A Realtor? | Top Shelf Business Solutions",
    "meta_desc": "Get more reviews as a realtor by asking every happy client right after closing, in one tap. Software that sends the ask automatically is what fills your profile.",
    "answer": "Get more reviews by asking every happy client at the right moment, right after closing, and making it a single tap to your Google profile. Most clients are glad to leave one, they just forget, so software that sends the ask automatically and links straight to the review form is what actually turns closings into reviews.",
    "sections": [
        {"h2_html": "Happy clients forget. The <em>timing</em> is everything",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The problem is almost never that your clients are unhappy. It is that the day they are happiest, the day the keys change hands, is exactly the day you are too busy to ask, and by the time you think of it three weeks later the glow has worn off and the review never gets written. Your reputation ends up thinner than the work you actually did.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The fix is to ask at the peak moment and to make saying yes effortless. Right after closing, an automatic text and email goes out with a link that opens your Google review form in one tap. No cornering people in person, no sticky note to remember, no awkward second ask. You simply catch every client while they still feel great about you.</p>'},
        {"h2_html": "Why reviews decide your <em>next listing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before a seller picks a listing agent, they Google you and read what your past clients said. A thin profile with a few old reviews quietly costs you listings you never even hear about, because the homeowner just called the agent with the wall of recent five-star reviews instead. Recent reviews also feed your Google Business Profile, which lifts you in the local results a seller sees when they search for an agent nearby.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It compounds. More reviews bring more visibility, which brings more clients, which brings more reviews, and the reputation you build is tied to you, not your brokerage. Asking everyone honestly is also the only right way to do it. Filtering out unhappy clients or paying for reviews breaks the platforms\' rules, and good software simply asks every client at the right time and makes it easy to say yes.</p>'}],
    "bridge_h2": "Review software that asks at the <em>right moment</em>",
    "bridge_text": "Review software asks every happy buyer and seller for a review the moment they are happiest, right after closing, by text and email with a one-tap link to your Google profile. It flags every new review so you can reply to each one, good or bad, and it fires automatically off a closing logged in your CRM, so your reputation keeps bringing referrals instead of depending on the few clients who remember to post on their own.",
    "bridge_slug": "review-software-for-real-estate-agents",
    "bridge_label": "See review software",
    "faqs": [
        ("Is automating review requests against Google's rules?",
         "No. Asking every client for an honest review is fine and encouraged. What is not allowed is filtering out unhappy clients or paying for reviews, and this does not do that. It simply asks everyone at the right moment and makes leaving an honest review a single tap."),
        ("When exactly does it ask for the review?",
         "Right after closing, when the client is happiest, sent automatically by text and email with a one-tap link. You can adjust the timing and the wording so it still sounds like you rather than a form letter.")],
},
# ============================ Q5 -> Websites & SEO (cost) ============================
{
    "slug": "real-estate-agent-website-cost",
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "h1": "How Much Does A Real Estate Agent Website Cost?",
    "title": "How Much Does A Real Estate Agent Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A real estate agent website runs from a few hundred dollars for a template to several thousand for a custom build. With Top Shelf it is free on plans from $299/mo.",
    "answer": "A real estate agent website can range from a few hundred dollars for a template up to several thousand for a custom build, plus monthly IDX fees. With Top Shelf a custom site is included free on every plan, from $299 a month, or $1,500 one time if you just want to own the site outright.",
    "sections": [
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Real estate website pricing is all over the map because you are really paying for a few different things at once. A basic template you fill in yourself sits at the low end. A custom-designed site built to rank in your market and capture leads sits at the high end and can run into the thousands. On top of the build there is usually a monthly cost for an IDX or MLS feed so your listings show, and often a separate charge for any real search engine work.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The number that matters is not the sticker price of the site. It is what the site does for you afterward. A cheap template that never ranks and never captures a lead is expensive at any price, and a site that quietly brings you buyers and sellers pays for itself many times over. Judge the cost by the leads, not the line item.</p>'},
        {"h2_html": "Watch for the <em>hidden ongoing costs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The build price is rarely the whole story. Ask who owns the site and the domain when you stop paying, because some providers keep both and leave you starting over if you leave. Ask whether SEO, listing feeds, and edits are included or billed on the side. A brokerage template is often free but looks like every other agent at the firm and is not built to rank for your specific neighborhoods.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps this simple. A custom five-page website is included free on every plan, starting at $299 a month with no setup fee, and it is registered to you, not us or your brokerage. If you would rather just own a site outright with no plan, that is $1,500 one time, yours to keep. Either way the site is built to rank locally and capture leads into your own system.</p>'}],
    "bridge_h2": "A site built to <em>rank and capture leads</em>",
    "bridge_text": "A real estate website built for SEO ranks for your name and your neighborhoods, shows up before the portals for the local searches you can win, and captures a buyer or seller the moment they land, so the traffic and the leads belong to you instead of Zillow. With Top Shelf the site is included free on every plan or $1,500 to own outright, and it feeds the same CRM that follows up on every lead it earns.",
    "bridge_slug": "websites-seo-for-real-estate-agents",
    "bridge_label": "See websites and SEO",
    "faqs": [
        ("Is a website really included free on the plans?",
         "Yes. A new custom five-page site is built and published free on every Top Shelf plan, starting at $299 a month with no setup fee. The only time a website costs a flat price is if you want to buy one on its own without a plan, which is $1,500 one time."),
        ("Do I own the website or does the provider keep it?",
         "You own it. Your website, domain, logo, and customer list are in your name from day one, so if you ever leave you keep all of it. That is not true of every provider, so it is always worth asking before you sign.")],
},
# ============================ Q6 -> Marketing (how-to) ============================
{
    "slug": "how-to-get-more-listings",
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "h1": "How Do I Get More Listings As A Real Estate Agent?",
    "title": "How Do I Get More Listings As A Real Estate Agent? | Top Shelf Business Solutions",
    "meta_desc": "Get more listings by becoming the agent a neighborhood already recognizes. Sellers call the name they know, so consistent local presence turns into listing calls.",
    "answer": "Get more listings by becoming the agent a neighborhood already recognizes before anyone decides to sell. Most sellers call the name they know, not the top search result, so showing up consistently in one area and staying in front of your past clients is what turns into listing calls months later.",
    "sections": [
        {"h2_html": "Sellers call the name they <em>already know</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most homeowners do not shop for a listing agent the way they shop for a plumber. They think of the one whose name they already recognize, whose sign they have seen on the street, whose post they scrolled past, whose card sat on the fridge for two years. By the time someone is actually ready to sell, they have usually already decided who to call, and no last-minute ad changes that.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is why more listings comes from familiarity built over time, not from shouting at an entire metro. Winning recognition in a defined area before people are ready is worth more than any single campaign, because it puts you at the front of their mind for the one moment that matters.</p>'},
        {"h2_html": "Farm one area instead of the <em>whole city</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Marketing to a whole city is expensive and forgettable. Picking a neighborhood or a few subdivisions and showing up there consistently, a sold post here, a market update there, a note about a new listing down the street, builds the specific recognition that turns into a listing call later. Your Google Business Profile matters too, because when someone searches for an agent nearby it is often the first thing they see, and a profile with recent activity beats one that looks abandoned.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Your past clients and sphere are the other half. They are your cheapest source of business and the easiest to lose touch with, so a steady, low-effort presence keeps you top of mind and sends the referral to you instead of whoever they saw most recently. It is slower than a big ad spend, and it is the approach that actually compounds.</p>'}],
    "bridge_h2": "Marketing that makes you the <em>name they know</em>",
    "bridge_text": "Marketing for real estate agents keeps you visible in a specific neighborhood and in front of your own sphere between transactions, through your Google Business Profile and consistent local content, so when someone nearby finally decides to sell, or a past client thinks of a referral, your name is already the one they reach for. It is the public-facing side of your business, and it pairs with the CRM that follows up privately with everyone already in your database.",
    "bridge_slug": "marketing-for-real-estate-agents",
    "bridge_label": "See marketing",
    "faqs": [
        ("What does farming a neighborhood actually mean?",
         "It means consistently showing up in one specific area, a subdivision or a handful of zip codes, with local content and updates, instead of spreading a budget thin across a whole city. Over months, that repetition is what makes people in that area recognize your name when they are ready to sell."),
        ("How long before this brings in listings?",
         "Recognition builds over months, not days, which is exactly why most agents quit before it pays off. There is no honest shortcut to being the name a neighborhood trusts, but a steady presence compounds, and a free audit will show you what your current visibility looks like to someone searching nearby today.")],
},
# ============================ Q7 -> Automation (how-to) ============================
{
    "slug": "stay-in-touch-with-past-clients",
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "h1": "How Do I Stay In Touch With Past Clients Automatically?",
    "title": "How Do I Stay In Touch With Past Clients Automatically? | Top Shelf Business Solutions",
    "meta_desc": "Stay in touch with past clients automatically with scheduled check-ins, market updates, and closing anniversaries that send themselves, so referrals keep coming.",
    "answer": "Stay in touch with past clients automatically by putting them on a set schedule of check-ins, market updates, and closing anniversaries that send themselves by text and email. You approve the cadence once, the system sends the touches on time, and you step in personally only when someone replies or is ready to move.",
    "sections": [
        {"h2_html": "Your sphere forgets you <em>faster than you think</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Past clients and people you already know are your cheapest source of business and the easiest to lose. You close a sale, everyone is happy, and then life gets busy and you go quiet for a year. When that client or their neighbor is finally ready to move, the referral goes to whichever agent they saw most recently, not the one who sold their house and then vanished. The goodwill was real. It just needed to be kept warm.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Doing that by hand across hundreds of past clients is the task that never survives a busy week. You cannot personally remember who closed two years ago this month or who should hear about a sale on their street, so the touches that would keep you top of mind simply do not happen.</p>'},
        {"h2_html": "Set the cadence once, let it <em>run</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Automation fixes the memory problem. You decide what your past clients should hear and how often, a closing anniversary note, a quarterly market update, a friendly local check-in, and the system sends each one on time for you. It is light and personal, not another sales blast, and it keeps your name in front of the people most likely to refer you without turning into a pitch in their inbox.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">You still do the human part. When someone replies, or a note lands the month they were quietly thinking about selling, you pick up the phone as yourself. The automation just makes sure the reason to reach out actually goes out, every time, instead of depending on you keeping a mental list you will never keep.</p>'}],
    "bridge_h2": "Automation that keeps your <em>sphere warm</em>",
    "bridge_text": "Automation for real estate agents keeps past clients and quiet leads on script without you remembering a thing, sending closing anniversaries, market updates, and light check-ins on the schedule you set, and reviving a lead that went cold instead of letting it fall out of your memory. It runs against the same database as your CRM, so nothing duplicates a contact, and every reply still comes to you to handle personally.",
    "bridge_slug": "automation-for-real-estate-agents",
    "bridge_label": "See automation",
    "faqs": [
        ("Does automating this make me sound like a robot?",
         "Not if it is done right. The touches are light and personal, a market note or a check-in in your own words, sent on a schedule rather than blasted out. You set the tone once, and you can jump in and message anyone directly whenever you want, so it reads like you kept in touch, not like a machine did."),
        ("What is the difference between this and the CRM?",
         "They run on the same database. The CRM is where your contacts and follow-up live, and automation is the engine that sends the scheduled touches for you. In practice they work as one system, so a past client gets the right message at the right time without you setting a single reminder.")],
},
# ============================ Q8 -> Websites & SEO (problem/symptom) ============================
{
    "slug": "why-zillow-gets-my-leads",
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "h1": "Why Does Zillow Get My Leads Instead Of Me?",
    "title": "Why Does Zillow Get My Leads Instead Of Me? | Top Shelf Business Solutions",
    "meta_desc": "Zillow gets your leads because the portals outrank most agent sites and control who the inquiry goes to. Your own ranking site is how you keep those leads.",
    "answer": "Zillow gets your leads because the portals outrank most individual agent sites and own the search result a buyer lands on, so when that buyer inquires, the portal decides which agent gets the lead, sometimes for a cut of your commission. Without your own site ranking, you are renting back buyers you could have had for free.",
    "sections": [
        {"h2_html": "The portals are not competing, they are <em>reselling your buyers</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Zillow, Realtor.com, and Redfin outrank most individual agent sites because they publish enormous amounts of content and have years of authority behind them. A buyer searching for homes in your city, or even for an agent in your city, usually lands on a portal first. When they request information there, the portal decides which agent gets the lead, sometimes in exchange for a referral fee out of your own commission.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So your site not ranking is not just a vanity problem. It is the reason a lead you should have gotten for free gets handed to whoever is on rotation that week, or sold back to you. You are paying, in fee or in commission, for buyers who were searching in your own market.</p>'},
        {"h2_html": "Rank for the searches you can <em>actually win</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank Zillow this year for a broad term like homes for sale in your metro, and you do not need to. You can rank for your own name, for the specific neighborhoods and subdivisions you work, and for searches like a neighborhood plus the word realtor, where a national portal has nothing local to say and your site can. Content built around the areas you actually sell in is what search engines, and buyers, reward.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">You probably still want a presence on the portals for now, since most buyers check them. The point is not to replace Zillow. It is to also own a channel where the leads are entirely yours instead of shared or sold, and where a visitor becomes a contact in your own system instead of a number in someone else\'s.</p>'}],
    "bridge_h2": "Own a channel Zillow <em>cannot touch</em>",
    "bridge_text": "A real estate website built for SEO ranks for your name and your neighborhoods, shows up before the portals for the local searches you can win, and captures a buyer or seller the moment they land, so the traffic and the leads belong to you instead of Zillow or Realtor.com. It feeds the same CRM that follows up on every lead it earns, so nothing it captures goes cold.",
    "bridge_slug": "websites-seo-for-real-estate-agents",
    "bridge_label": "See websites and SEO",
    "faqs": [
        ("Do I still need Zillow if I have my own site?",
         "Probably yes, for now. Most buyers still check the portals, so leaving entirely would cost you reach. The point is not to replace them, it is to also own a channel where the leads are entirely yours instead of shared or sold back to you."),
        ("Will my own site actually outrank Zillow?",
         "Not for broad searches like homes for sale in your city. It can realistically rank for your name, your specific neighborhoods, and long-tail local searches a national portal has no reason to target, which is exactly where an individual agent can win and where your best leads come from.")],
},
# ============================ Q9 -> CRM (cost) ============================
{
    "slug": "real-estate-crm-cost",
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "h1": "How Much Does A Real Estate CRM Cost?",
    "title": "How Much Does A Real Estate CRM Cost? | Top Shelf Business Solutions",
    "meta_desc": "A real estate CRM can cost from free to a few hundred dollars a month per user. With Top Shelf the CRM is part of the Signature plan at $899/mo, no setup fee.",
    "answer": "A real estate CRM can run anywhere from a free tier to a few hundred dollars a month per user, depending on features and how much follow-up is automated. With Top Shelf the CRM is part of the Signature plan at $899 a month, which also includes the AI receptionist, monthly SEO, and reviews, with no setup fee.",
    "sections": [
        {"h2_html": "What you are really <em>paying for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A real estate CRM can cost nothing to start or a few hundred dollars a month per user, and the spread comes down to what it actually does. A cheap or free CRM is usually just a contact list you still have to work by hand. The ones that cost more are the ones that follow up for you, with automatic texts and emails, lead capture, and reminders that fire on their own. You are not paying for storage. You are paying for the follow-up that a busy agent will never do manually.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Watch for the add-ons, because that is where the real price hides. Per-user fees, charges for texting, setup or onboarding costs, and extra tools bolted on the side can turn a cheap headline price into a large monthly bill. Ask what is included before you compare two numbers.</p>'},
        {"h2_html": "Judge the cost against the <em>leads it saves</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The honest way to price a CRM is against what a lost lead costs you. A single commission dwarfs a year of almost any CRM, so if the system keeps even one buyer from going cold, or brings back one past client, it has usually paid for itself several times over. A cheap CRM that you never actually use is the expensive one.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">With Top Shelf the CRM is not a separate line item. It is part of the Signature plan at $899 a month, which also includes the AI receptionist that answers your calls, monthly SEO, reviews, and reactivation, with no setup fee and no long contract. Your contacts stay in your name and exportable, so if you ever leave, your database goes with you. The most honest starting point is a free audit, so you pay for what you actually need.</p>'}],
    "bridge_h2": "The CRM, and everything that <em>feeds it</em>",
    "bridge_text": "A CRM for real estate agents keeps every lead, past client, and sphere contact in one place and follows up for you, so the buyer who is months out and the seller who is only thinking about it stay yours instead of going cold. With Top Shelf it is part of the platform alongside the AI receptionist and online booking, so a captured call lands in your database and gets worked automatically, and your contacts stay yours if you ever leave.",
    "bridge_slug": "crm-for-real-estate-agents",
    "bridge_label": "See the CRM",
    "faqs": [
        ("Is the CRM sold on its own or only in a plan?",
         "At Top Shelf the CRM comes as part of the Signature plan at $899 a month, which also includes the AI receptionist, monthly SEO, and done-for-you reviews, rather than a standalone CRM fee. There is no setup fee and no long contract, and a free audit will tell you whether that plan actually fits your business."),
        ("Do I keep my contacts if I stop paying or switch brokerages?",
         "Yes. Your contacts and notes are in your name and exportable any time, so if you switch offices or leave, your database goes with you. You are not renting access to your own client list, which is not true of every system, so it is worth confirming before you commit.")],
},
]
