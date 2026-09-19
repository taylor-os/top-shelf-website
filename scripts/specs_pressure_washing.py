"""Per-page content specs for the SEO corpus (plan §5), Pressure Washing batch.
generate_corpus.py imports SPECS from a specs module; each dict is one page's UNIQUE,
hand-written, trade-specific content. The generator owns the mechanics (shell, schema,
events, interlinks, keyword placement); the spec owns the substance that clears the
uniqueness gate. Never templated find-and-replace, never the plumber or house-cleaning
content reworded.

Pressure washing runs on ESTIMATE-SHOPPING and RECURRING RE-WASHES. Most calls are a
homeowner pricing a house wash, driveway, deck, roof, or a commercial lot who is dialing a
few companies and books whoever answers and looks professional. The crew is on a job
behind loud equipment and soaked, so the calls that decide the week roll to voicemail. The
phone spikes hard in spring and early summer when everyone notices winter buildup at once.
Dramatic before-and-after photos are the entire marketing story on Google and social, and
reviews decide trust. The follow-up on open quotes, the reactivation of past customers for
an annual wash, and commercial and HOA recurring contracts are the quiet goldmine. A fast
site with an instant quote request beats renting your own calls back from a lead-seller.

This batch is four pages, not seven (the ai-receptionist dict carries "demo": True). Each
example body ends with the literal "Illustrative example, not a client." per the honesty
rule; if the generator also appends that line, dedupe there.
"""

SPECS = [
# ===================== AI Receptionist for Pressure Washing =====================
{
    "slug": "ai-receptionist-for-pressure-washing", "demo": True,
    "trade_slug": "pressure_washing", "trade_plural": "pressure washing companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "AI Receptionist for Pressure Washing",
    "title": "AI Receptionist for Pressure Washing | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Pressure Washing",
    "meta_desc": "A pressure washing answering service picks up every estimate call while your crew is soaked and running loud gear, then books the job on your calendar.",
    "service_schema_name": "AI Receptionist for Pressure Washing",
    "eyebrow": "For Pressure Washing",
    "h1_html": "AI Receptionist <em>for Pressure Washing</em>",
    "answer_block": "A pressure washing answering service answers every estimate call the moment it rings, even while your crew is soaked and running a surface cleaner, finds out what needs washing and where, and books the job straight onto your calendar. It runs on your own number, and every call belongs to you.",
    "sections": [
        {"h2_html": "The estimate call you miss is the job that <em>books the next company</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner who wants their house washed or their driveway cleaned is not loyal to anyone yet. They found three or four pressure washing companies on Google, they are calling down the list, and they book the first one that answers, sounds like a professional, and can come give a price. Whoever picks up usually wins, because there is nothing to compare yet and the caller just wants it handled. But you are the one doing the work, standing in the spray with a wand in your hand or a surface cleaner running, soaked and half-deaf from the machine, and you physically cannot hear the phone. So the call rolls to voicemail, and a homeowner shopping around does not leave one. They hang up and dial the next company, and that estimate, the one you would have won on the phone, goes to whoever picked up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An AI receptionist answers on the first ring even while you are mid-wash, sounds like someone who knows the trade, finds out what they need cleaned, how big it is, and where, and either books the estimate or the job straight onto your calendar. The call gets captured instead of lost to the company that happened to be free to pick up.</p>'},
        {"h2_html": "Built around how a <em>pressure washing crew actually works</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your phone rings hardest at the worst possible moment to answer it. You are up on a ladder soft washing a second story, behind a surface cleaner that drowns out everything, or driving between jobs with your hands full, and that is exactly when the estimate calls come in. A voicemail box cannot answer a question, and a generic call center reading a script does not know a soft wash from a driveway job, or why a roof needs different handling than a deck.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers every call while your crew is soaked, loud, and heads-down on a job, so no estimate goes to voicemail.</li><li>Knows the work: house wash, driveway and concrete, deck or fence, roof soft wash, or a commercial lot, and asks the right questions for each.</li><li>Gets the address, the surface, and the rough size, then books the estimate or the job on your calendar and texts you the details on the spot.</li><li>Handles the spring and early-summer rush, when everyone wants their house done at once and the phone never stops, without putting a single caller on hold.</li></ul>'},
        {"h2_html": "The math is <em>one house wash</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not need it to catch many calls to come out ahead. One house wash or one driveway you would have lost while your crew was heads-down on another job usually covers the cost for a good while, and a commercial or HOA account that starts from a single captured call can be worth far more over a season. Everything it books after that first save is extra. The point is simple: stop handing your estimates to whichever company happened to be standing next to a quiet phone.</p>'},
        {"h2_html": "You own the number, the calls, and the <em>customer list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing business number, or a new one registered in your name, not ours. Every caller, every address, and every job detail is yours and exportable any time, so the customer list you build is an asset you keep instead of something you rent back month to month. There is no long contract holding your data. The AI receptionist is one piece of the Top Shelf platform, and it hands every call it captures to the same CRM that follows up on the quote and reminds the customer next season, so a job you booked never quietly goes cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "Three spring estimate calls, booked while the <em>machine is running</em>",
        "body_html": 'It is the first warm Saturday of spring and every homeowner on the block suddenly wants the winter grime off their house. Your crew is running a surface cleaner across a driveway and cannot hear a thing. Three estimate calls come in that hour. Two competitors send them to voicemail, and the homeowners, who are only shopping, move on down their list. Yours answers all three, sounds professional, gets each address and what needs washing, and books two estimates and a driveway job straight onto your calendar. You finish the driveway you were on and check your phone to find the afternoon already filling up. Illustrative example, not a client.'},
    "faqs": [
        ("Does it work with my current phone number?",
         "Yes. It can answer on your existing business number, or set up a new one registered in your name. Either way the number and every call that comes through it belong to you and go with you if you ever leave."),
        ("Can it actually quote a job over the phone?",
         "It does not throw out a firm price sight unseen, and you would not want it to. It gathers exactly what you need to quote, the surfaces, the rough size, the address, and whether it is a house wash, driveway, roof, or commercial lot, then books the estimate or the job on your calendar so you can price it right."),
        ("Will it keep up when the phone blows up in spring?",
         "That is when it earns its keep. During the spring and early-summer rush it answers every call at once, no hold music and no busy signal, so the flood of estimate requests that used to overwhelm you all gets captured instead of half of it going to voicemail."),
        ("Is it going to sound like a robot?",
         "It answers naturally and is upfront rather than pretending to be a person. A homeowner who just wants their house washed mostly needs to know a real company is handling it and someone will come give a price, and a steady voice that captures the details beats a voicemail box every time. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your services, your questions, and your calendar for you, so it is answering in days, not weeks. Start with a free audit and we will show you what your current setup is missing.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for pressure washing companies"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-pressure-washing.html", "The CRM that follows up on every call you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing estimates to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many estimate calls and jobs your current setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ============================ CRM for Pressure Washing ============================
{
    "slug": "crm-for-pressure-washing",
    "trade_slug": "pressure_washing", "trade_plural": "pressure washing companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "CRM for Pressure Washing",
    "title": "CRM for Pressure Washing | Top Shelf Business Solutions",
    "og_title": "CRM for Pressure Washing",
    "meta_desc": "A CRM for pressure washing companies follows up on every estimate and past customer, so a house you washed once books again and quotes stop going cold.",
    "service_schema_name": "CRM for Pressure Washing",
    "eyebrow": "For Pressure Washing",
    "h1_html": "CRM <em>for Pressure Washing</em>",
    "answer_block": "A CRM for pressure washing companies keeps every lead, past customer, and open estimate in one place and follows up for you, so the homeowner sitting on a house-wash quote and the driveway you cleaned two springs ago both come back to you instead of the company that stayed in touch. Your customer list quietly becomes recurring work.",
    "sections": [
        {"h2_html": "The estimates you already sent are the jobs you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most pressure washing companies do not have a lead problem, they have a follow-up problem. You go look at a house, send over a price for a wash, and the homeowner says they want to think about it or get another couple of quotes. Then you get busy, the season is moving, and you never circle back. They booked whoever followed up, not always the lowest price, and often not you. That estimate was never dead. It just needed one more text or call a few days later, and that is the thing there is never time for when you are on a job from dawn to dark.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every open estimate in front of you and follows up on a schedule you set, with texts and emails that go out on time whether or not you remember. The homeowner comparing three companies hears from you again while the other two go quiet, and the job comes back around to you.</p>'},
        {"h2_html": "Every house you wash comes <em>dirty again</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This is the part of the trade that makes a CRM worth more here than almost anywhere. The mildew, algae, and grime you strip off a house or a roof start creeping back the moment you leave, and in a year or two it looks like you were never there. That is not a problem, it is a standing appointment nobody has booked yet. The customer who was thrilled with a clean house last spring would happily have it done again if someone reminded them, but they forget, and they forget your name, and next spring they search Google and hire whoever shows up first.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every customer, address, service history, and note lives in one place instead of a truck full of scribbled quotes and your memory.</li><li>Annual reminders go out on schedule, a yearly house wash, a driveway before a party, a roof soft wash, so the work comes back around without you tracking a single date.</li><li>You can see who has not booked in a while and reach the right customer with the right reminder at the right time of year.</li></ul>'},
        {"h2_html": "Commercial and HOA accounts are the <em>recurring goldmine</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner is worth coming back to once a year. A storefront, a restaurant with a greasy dumpster pad, a property manager with a dozen sidewalks and breezeways, or an HOA with common areas is worth coming back to every month or every quarter, on a contract. That recurring commercial and HOA work is the steadiest money in pressure washing, and it lives or dies on staying organized: knowing what is due, when you were last there, and who to invoice. A CRM holds every one of those accounts and their schedule, so recurring revenue keeps rolling instead of slipping because you lost track of a rotation.</p>'},
        {"h2_html": "You own the list, and it <em>works with everything else</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every customer and every note is yours and exportable any time, not locked inside software you rent. The CRM is one piece of the Top Shelf platform and connects to the AI receptionist, so a call it answers lands in your database and gets followed up on automatically, and to online booking and review requests, so a finished job logs against the right customer with the full history attached and quietly asks them for a review. Nothing you have earned goes cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The house wash quote that <em>closes itself</em>",
        "body_html": 'You quote a homeowner on a full house wash on a Tuesday and they tell you they want to get one more price. Normally that is the last you hear of it. Instead the CRM sends a friendly check-in two days later and a short note a few days after that, both written to sound like you. The other company never followed up, so when the homeowner is ready that weekend, yours is the only name still in front of them, and they book without shopping any further. A year later the same system reminds them the algae is creeping back, and they book again. You never sat down to chase any of it. Illustrative example, not a client.'},
    "faqs": [
        ("Does it import my existing customers and past jobs?",
         "Yes. Your current customers, leads, and job history come in and live in one place, and everything stays yours and exportable. The point is to make the customer list you already have actually work for you."),
        ("Will it really follow up on estimates automatically?",
         "Yes, on the schedule you approve. An open estimate gets a check-in a few days later and another after that, all sent for you, so a homeowner comparing prices keeps hearing from you while the other companies go quiet. You can jump in and message anyone directly any time."),
        ("Can it remind past customers to book an annual wash?",
         "Yes, and this is where it pays off in this trade. You set the cadence, a yearly house wash, a driveway before the holidays, a roof every couple of years, and the reminders go out automatically, so the grime that always comes back turns into a booking that comes back with it."),
        ("Can it handle my commercial and HOA accounts?",
         "Yes. Recurring accounts, their rotation, and what is due live in the CRM, so a monthly storefront or a quarterly HOA route stays on schedule and gets invoiced instead of slipping because you lost track of when you were last there."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your customers, build your follow-up and reminder sequences, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will show you where jobs are slipping through today.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for pressure washing companies"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-pressure-washing.html", "The AI receptionist that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting estimates and customers <em>go cold</em>",
    "cta_sub": "Get a free audit of how many of your estimates and past customers are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ========================== Marketing for Pressure Washing ==========================
{
    "slug": "marketing-for-pressure-washing",
    "trade_slug": "pressure_washing", "trade_plural": "pressure washing companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "Marketing for Pressure Washing",
    "title": "Marketing for Pressure Washing | Top Shelf Business Solutions",
    "og_title": "Marketing for Pressure Washing",
    "meta_desc": "Pressure washing marketing puts your before-and-after photos and reviews first in the map pack, so the neighbor who searches calls you, not the other company.",
    "service_schema_name": "Marketing for Pressure Washing",
    "eyebrow": "For Pressure Washing",
    "h1_html": "Marketing <em>for Pressure Washing</em>",
    "answer_block": "Pressure washing marketing keeps you visible where local demand shows up, your Google Business Profile and the map pack, and puts your best before-and-after photos and reviews in front of homeowners nearby, so when someone looks at their filthy driveway and searches, your name is the active, trusted one they call.",
    "sections": [
        {"h2_html": "The before-and-after photo is the <em>whole pitch</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Almost nothing in home services sells itself the way pressure washing does. A single side-by-side of a black, algae-streaked driveway next to a clean one, or a dingy roof brought back to its real color, does more than any slogan could, because the result is instant, obvious, and a little satisfying to look at. That is your marketing, and it is a gift most trades do not have. The companies that grow are the ones showing that transformation constantly, on Google and on social, so a homeowner staring at their own dirty concrete sees exactly what you could do to it and pictures their house next.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The mistake is doing the work and never capturing it. A clean driveway with no photo is a job well done and a marketing asset thrown away. Getting those reveals in front of the right local audience, over and over, is what turns a good crew into the name everyone in town already knows.</p>'},
        {"h2_html": "Your Google Business Profile is the new <em>storefront</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone searches for pressure washing near them, the map pack, those three local listings with the star ratings, is the first thing they see, above the websites and above the ads. A profile sitting untouched for months, with two old photos and a handful of reviews, looks abandoned next to one with a steady stream of fresh before-and-after shots, current services, and recent reviews. Keeping it active, complete, and full of your best work is a quiet advertisement running in the exact spot a homeowner looks the moment they decide the house needs doing.</p>'},
        {"h2_html": "Show up in the <em>towns you actually cover</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Marketing to a whole metro is expensive and forgettable, and it sends you calls from an hour outside your range. Focusing on the specific towns and neighborhoods you serve, with a profile, photos, and content built around those areas, is what puts you in the map pack where you can actually take the work. A neighborhood full of the same builder-grade driveways and the same north-facing roofs streaking at the same time is a tight, reachable target, and it is the one that turns into a route of jobs close together instead of a day lost to driving.</p>'},
        {"h2_html": "Ride the spring rush, and stay in front of <em>past customers</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Pressure washing demand is deeply seasonal. The phone starts ringing the first warm weekend of spring, when everyone notices the winter buildup at once, it stays loud through early summer, and it quiets down when the weather turns. Being visible and active right before that wave beats scrambling once it hits, so your profile should be full and climbing before the season opens, not after. A steady local presence, seasonal posts, fresh reveals, the occasional tip, keeps you top of mind for the new customer and reminds past ones that the grime is back. This is the public-facing side of the business; the private reminders to people already in your database are the CRM.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The first warm weekend, and you are <em>already at the top</em>",
        "body_html": 'The first genuinely warm Saturday of spring arrives and half the neighborhood walks outside, looks at a driveway that went black over winter, and pulls out a phone. Because your Google profile has been kept active all year, stacked with recent before-and-after photos, current services, and a steady flow of reviews, you sit at the top of the map pack when everyone searches at once. The homeowners who want it handled that week call the names they can see and trust first, and yours is right there with proof of the work attached. The company that let its profile go quiet over winter is nowhere on the map. Illustrative example, not a client.'},
    "faqs": [
        ("Do you post my before-and-after photos to Google for me?",
         "Yes. We keep your Google Business Profile active with your best before-and-after shots, service updates, and local content on a regular schedule, and keep your services and service area accurate, so it looks current and impressive whenever someone searches near them."),
        ("What does focusing on my service area actually mean?",
         "It means building your profile and content around the specific towns and neighborhoods you can reach quickly, instead of spreading a budget across a whole metro. That is what gets you into the map pack where the local, ready-to-book calls are."),
        ("How is this different from the CRM follow-up?",
         "The CRM follows up privately with people already in your database. Marketing is the public-facing side, your Google profile, reviews, and local visibility, aimed at homeowners who are not your customer yet but need to find and trust you the moment they notice the dirt."),
        ("Can you help me get ahead of the spring rush?",
         "Yes. We build your visibility before the season opens, so your profile is full and climbing when the first warm weekend sends everyone searching at once, instead of scrambling to look active after the calls have already started going to someone else."),
        ("How long before I see it working?",
         "A neglected profile can climb in the map pack within weeks once it is active, complete, and full of real photos, and it compounds from there as reviews and content build. Setup is included, and a free audit will show you what your current online presence looks like to someone searching near you today.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for pressure washing companies"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-pressure-washing.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the pressure washer they <em>can already see</em>",
    "cta_sub": "Get a free audit of how visible you actually are in your service area and on Google right now, whether you work with us or not. No credit card, never a call center.",
},
# ======================= Websites & SEO for Pressure Washing =======================
{
    "slug": "websites-seo-for-pressure-washing",
    "trade_slug": "pressure_washing", "trade_plural": "pressure washing companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "Websites & SEO for Pressure Washing",
    "title": "Websites & SEO for Pressure Washing | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Pressure Washing",
    "meta_desc": "A pressure washing website built for SEO ranks for pressure washing near me and house washing in your city, and captures the quote directly, not a lead-seller.",
    "service_schema_name": "Websites & SEO for Pressure Washing",
    "eyebrow": "For Pressure Washing",
    "h1_html": "Websites &amp; SEO <em>for Pressure Washing</em>",
    "answer_block": "A pressure washing website built for SEO ranks for the searches a homeowner makes when the house looks dirty, pressure washing near me, house washing, driveway and roof cleaning in your city, shows off your before-and-after work, and captures the quote request directly, so the job is yours instead of a lead-seller renting it back to you.",
    "sections": [
        {"h2_html": "The lead-sellers are not competing with you, they are <em>renting you back your own calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for pressure washing in your town and the top of the page is often a directory, a national booking middleman, or a pay-per-lead service, not the local company doing the actual work. Those sites publish thousands of pages and have years of authority behind them, so a homeowner searching lands there first, fills out a form, and that lead gets sold, sometimes to three companies at once, sometimes back to you for a fee out of your own margin. Your site not ranking is not a vanity problem. It is the reason a call you should have gotten for free gets sold to you, or handed to whoever paid the most that week.</p>'},
        {"h2_html": "Rank for what a homeowner types when the <em>driveway looks bad</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national directory this year for the broadest term, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you cover, and for the exact searches a homeowner makes when they finally get fed up with the grime: pressure washing near me, house washing in your city, driveway cleaning, roof cleaning, deck and fence washing, commercial pressure washing. Pages built around the services you actually offer and the areas you actually serve are what search engines, and homeowners ready to book, reward with the click.</p>'},
        {"h2_html": "Let the before-and-afters sell, and make the <em>quote one tap away</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Pressure washing has the best sales tool in home services built right in: the reveal. A site that puts real before-and-after galleries front and center does most of the convincing on its own, because a homeowner can see their own dirty driveway in your photos and picture the clean one. But the site has to be fast and it has to be easy, because most of these searches happen on a phone. A quick, obvious way to request a quote, snap a photo of the surface, punch in the address, get a callback, turns a visitor into a lead right there. A pretty site that buries the quote button is a wasted opportunity.</p>'},
        {"h2_html": "The calls and quotes are <em>yours</em>, permanently",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you put into a pay-per-lead service disappears the day you stop paying, and the lead was never really yours anyway. A website you own keeps ranking, keeps showing your work, and keeps capturing quote requests for as long as it exists, and it is registered to you, not a platform that can drop you or sell the same lead to your competition. The site plugs into the same CRM that follows up on every quote it captures and the AI receptionist that answers the calls it drives, so nothing it earns you slips away.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A dirty driveway finds <em>you</em>, not a directory",
        "body_html": 'A homeowner two neighborhoods over finally gets tired of a driveway that went black over the winter and searches house washing near me on their phone. Instead of a national directory that would sell the lead to three companies, they find your site ranking for that area, with a gallery of before-and-after driveways just like theirs and a quote button right at the top. They snap a photo of their concrete, enter the address, and request a quote in under a minute. It lands in your system as a lead that is yours alone. You paid nothing per lead, and no middleman ever touched it. Illustrative example, not a client.'},
    "faqs": [
        ("Will my site actually outrank the big directories?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the service searches a national directory has no reason to target well, house washing, driveway cleaning, roof cleaning in your city, which is exactly where a local company can win."),
        ("How is this different from paying for leads?",
         "A pay-per-lead service rents you a call that it also sells to your competitors, and it stops the day you stop paying. A website you own captures quote requests that are yours alone and keeps working long after it is built, without a per-lead fee coming out of every job."),
        ("Do my before-and-after photos really matter on the site?",
         "They are your strongest selling point. Pressure washing results are dramatic and instant, and a homeowner who sees a driveway or roof like theirs go from filthy to clean in your gallery is most of the way to booking. We build the site to show that work off and put the quote request right next to it."),
        ("Can visitors request a quote right from the site?",
         "Yes. The site is built so a visitor can request a quote in a tap, describe or photograph the surface, and enter their address, so a lead comes in ready for you to price instead of leaving a voicemail they will forget. It lands straight in your CRM."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks; broader terms take longer and compound over months, and it helps to be climbing before the spring rush. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for pressure washing companies"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-pressure-washing.html", "Staying visible in your service area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and lead-sellers taking your calls, whether you work with us or not. No credit card, never a call center.",
},
]
