"""Per-page content specs for the SEO corpus (plan §5), fence companies batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell, schema,
events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns the UNIQUE,
hand-written, fence-specific substance that clears the uniqueness gate. Never templated
find-and-replace, never the plumber, general-contractor, foundation-repair, or mover content reworded.

Fence companies sell a considered, mid-ticket home-improvement job to a homeowner who WANTS a fence
(privacy, a new pet, a pool that has to meet code, curb appeal, a new-construction lot) rather than one
who is stuck with an emergency. The homeowner lines up several estimates and hires the company that
answers, shows up to measure soonest, and looks trustworthy; the deciding window runs days to weeks and
often waits on an HOA approval or a property-line and permit question; demand is local and seasonal,
climbing through spring and summer and with new-home construction; and the crew that misses the estimate
call is usually out on an install setting posts. So the substance leans on capturing every estimate
request while the crew is on the tools, following up quotes over the deciding weeks, reactivating past
customers for repairs, gates, and additions plus the highly visible neighbor referral a new fence earns,
and a proof-heavy, gallery-led presence (clean straight fence lines and an easy estimate request) that
converts a homeowner picturing the fence in their own yard. Keep distinct from general contractors
(whole remodels) and foundation repair (a frightened, engineered sale).

Home Services hub. Four service angles here in one file (the ai-receptionist dict carries
"demo": True). Each example body ends with the literal "Illustrative example, not a client." per
the honesty rule; if the generator also appends that line, dedupe there.
"""

SPECS = [
# ==================== AI Receptionist for Fence Companies ====================
{
    "slug": "ai-receptionist-for-fence-companies", "demo": True,
    "trade_slug": "fence_companies", "trade_plural": "fence companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "AI Receptionist for Fence Companies",
    "title": "AI Receptionist for Fence Companies | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Fence Companies",
    "meta_desc": "A fence company answering service answers every estimate call, even when your crew is setting posts, captures the fence details, and books the measure for you.",
    "service_schema_name": "AI Receptionist for Fence Companies",
    "eyebrow": "For Fence Companies",
    "h1_html": "AI Receptionist <em>for Fence Companies</em>",
    "answer_block": "A fence company answering service answers every call the moment it rings, even when your whole crew is out setting posts and hanging panels, gathers what the homeowner wants, privacy or picket, wood, vinyl, aluminum, or chain-link, how much yard, and books the measure, so the fence job belongs to you instead of the company that answered first.",
    "sections": [
        {"h2_html": "The estimate call you miss is the fence <em>another company builds</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner who has decided to fence the yard, for a new puppy, for privacy from a neighbor, to meet the code before the pool goes in, is not calling one fence company. They line up three or four, and they hire the one that answers, sounds like a real outfit, and comes out to measure soonest. Fencing runs on that responsiveness more than almost any trade, because a fence is a want the homeowner is excited about, not an emergency they are stuck with, and the company that shows up first to walk the yard and talk through options usually walks away with the job. But every hand you have is out on an install, digging post holes, setting posts in concrete, hanging panels, and nobody on a crew can stop to answer a phone, so the estimate call rings out and the job, worth far more than an afternoon of your time, goes to whoever picked up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A fence company answering service picks up on the first ring, sounds calm and professional, asks what they want built and how much yard they are fencing, gets the address, and books the measure or hands you a qualified lead with the details already down. The estimate is sitting on your calendar instead of lost to the company down the road that happened to be near a phone.</p>'},
        {"h2_html": "Built around how <em>fence companies actually get calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your calls do not come in while you are at a desk. They come in while your crew is out setting posts, while you are pricing the next yard from the truck, and in the evenings and weekends when a homeowner finally walks the backyard and decides this is the year for a fence. A voicemail box cannot hold a homeowner who is working down a list, and a generic call center reading a script does not know a six-foot cedar privacy fence from an aluminum pool enclosure, or which caller is ready to book a measure and which is still deciding whether to fence at all.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers every call and web request, including the evenings and weekends when homeowners actually sit down and decide to fence the yard.</li><li>Asks what you would ask: privacy, security, a pet, or a pool that has to meet code, which material they are leaning toward, roughly how much yard, and where the property is.</li><li>Books the measure straight onto your calendar and texts you the details, so you or your estimator show up already knowing the yard and the style.</li><li>Takes down the HOA and property-line questions a homeowner always leads with, instead of leaving them holding a voicemail and no answer.</li><li>Treats a referral or a past customer differently from a cold caller, so the people most likely to book never land in a voicemail box.</li></ul>'},
        {"h2_html": "The math is <em>one fence job</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not need to catch many calls for this to pay for itself. A fence job is a real ticket, a full yard of privacy fence or a run of ornamental aluminum is worth far more than an afternoon of chasing missed calls, so one estimate you would have lost while your crew was setting posts is often worth more than the service costs for months. Everything it captures after that first save is on top. And in spring and summer, when the calls bunch up and every crew you have is already booked on an install, that is exactly when the most estimates roll to voicemail, so it earns the most in the season that matters most. The point is to stop handing your booked weekends to the company that simply answered faster.</p>'},
        {"h2_html": "You own the number, the calls, and the <em>customer list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing business number, or a new one registered in your name, not ours. Every caller, every address, and every note about the yard and the style is yours and exportable any time, so the customer list you are building stays an asset you own instead of something you rent back month to month. There is no long contract holding your data hostage. The answering service is one piece of the Top Shelf platform, and it hands every estimate request it captures to the same CRM that follows up over the days a homeowner takes to compare quotes, so a job never slips through the gap between the first call and the signed estimate. A homeowner who would rather book the measure themselves can, while the ones who want to talk reach a real, professional answer instead of a recording.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "An evening fence call, booked while the <em>crew is on the truck</em>",
        "body_html": "It is 6pm in early spring and a homeowner who just brought home a puppy walks the backyard and decides it is finally time to fence it in. They call the three fence companies they found online. The first two ring out to voicemail because everyone is still finishing an install. Yours answers, asks whether they are after privacy or just containment, what material they like, and roughly how big the yard is, gets the address, and books a measure for Saturday morning while a note pings your phone. You wake up to the appointment already on your calendar with the yard, the style, and the homeowner's number attached, instead of hearing later that they hired whoever picked up. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current phone number?",
         "Yes. It can answer on your existing business number, or set up a new one registered in your name. Either way the number and every estimate that comes through it belong to you and go with you if you ever leave."),
        ("Can it handle a real fence inquiry, or just take a message?",
         "It does not guess at a price. It gathers what a real measure needs, what they want fenced and why, which material they are leaning toward, roughly how much yard, and where the property is, then books the measure on your calendar or hands you a qualified lead. You still set the scope and the price, but the job is captured instead of lost."),
        ("What happens to calls when my crew is out on an install?",
         "That is exactly when it earns its keep. It answers every call and web request the moment it comes in, no matter how buried your crew is setting posts, so the hours you cannot reach the phone stop being the hours you lose the most estimates."),
        ("Can it answer the HOA and property-line questions homeowners ask?",
         "It takes down what the homeowner knows, their HOA rules, where they think the line runs, whether they have a survey, so nothing is lost, and it is upfront that you will confirm the details at the measure. A homeowner gets a real, helpful answer instead of a voicemail, and your estimator arrives already knowing what to check."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your questions, your calendar, and your lead rules for you, so it is answering in days, not weeks. Start with a free audit and we will show you what your current setup is missing.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for fence companies"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-fence-companies.html", "The CRM that follows up on every estimate you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing fence jobs to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many estimate calls your current setup is letting slip through the gap, whether you work with us or not. No credit card, never a call center.",
},
# ========================= CRM for Fence Companies =========================
{
    "slug": "crm-for-fence-companies",
    "trade_slug": "fence_companies", "trade_plural": "fence companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "CRM for Fence Companies",
    "title": "CRM for Fence Companies | Top Shelf Business Solutions",
    "og_title": "CRM for Fence Companies",
    "meta_desc": "A CRM for fence companies follows up on every quote and past customer for you, so the fence a homeowner is weighing and the yard you built come back to you.",
    "service_schema_name": "CRM for Fence Companies",
    "eyebrow": "For Fence Companies",
    "h1_html": "CRM <em>for Fence Companies</em>",
    "answer_block": "A CRM for fence companies keeps every lead, past customer, and open quote in one place and follows up for you, so the family still comparing three estimates and the homeowner whose backyard you fenced two years ago both call you next instead of the company that stayed in touch. Your customer list quietly becomes your booked season.",
    "sections": [
        {"h2_html": "The quotes you already sent are the jobs you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most fence companies do not have a lead problem. They have a follow-up problem. You drive out, walk the yard, and send over a quote for a run of privacy fence, and then the homeowner goes quiet. They are gathering two or three other numbers, talking it over with a spouse, waiting on the HOA to approve the style, and a fence is rarely a same-day decision. Meanwhile the season pulls you onto the installs you already have booked, and you never circle back. Weeks later they hire another company, and it is usually not the cheapest one, it is the one that kept in touch and felt easiest to work with.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every open quote in front of you and follows up on a schedule you set, with texts and emails that go out on time whether or not the week got away from you. The homeowner comparing three fence companies keeps hearing from you while the others go silent, and being the one who never drops the thread is exactly what wins the job. None of it takes you off the tools, because the follow-up runs in the background while your crew builds, and you step in only when a homeowner actually replies.</p>'},
        {"h2_html": "Every yard you fence is a customer <em>for the next project</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Past customers are the cheapest work a fence company can get. You have already been in their yard, they have seen your crew leave a clean, straight line, and the next job, a gate that finally needs replacing, a section the wind took down, extending the fence when they redo the back patio, staining or repairs a few years on, is yours if you stay in touch. But you cannot personally remember to reach back out to everyone you have ever built for, so most of that repeat work drifts to whoever turns up when they search, long after they lost your card.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every customer, address, the style and material you installed, and your notes live in one place instead of a truck full of paper quotes and whatever you can remember.</li><li>You can see who you built for a few years back and reach them when a fence is due for a repair, a stain, or a gate, before a competitor turns up first.</li><li>Thank-you and referral asks go out after a job wraps, so the happy customer with a brand-new fence the whole street can see actually gets asked while it is fresh.</li></ul>'},
        {"h2_html": "The referral and the repeat job are a <em>goldmine you already own</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A fence is the most visible work you do. It sits on the property line where every neighbor and everyone who walks the street sees it, and a clean, straight run is a standing advertisement that quietly asks who built it. People planning a fence almost always ask the neighbor who just got one, so a crew that leaves good work is the easiest recommendation a customer ever makes. A steady, light touch, a thank-you when the job wraps, a check that the gate still swings true, a note when staining season comes around, keeps your name in front of the exact people most likely to hand you the next job or pass it to a neighbor. The same list quietly turns your best referral sources into partners, the builder who fences every new home, the pool company that needs a code-compliant enclosure on every install, the property manager who calls you for every rental, all sitting in one place where a check-in goes out on schedule without you thinking about it. That, more than any ad, is the steadiest pipeline a fence company has.</p>'},
        {"h2_html": "You own the list, and it <em>works with the rest of the system</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every customer, quote, and note is yours and exportable any time, not locked inside software you rent. The CRM is one piece of the Top Shelf platform and connects to the answering service, so a call it captures lands in your database and gets followed up on automatically, and to your booking, so a scheduled measure is logged against the right homeowner with the yard and the style already attached. The result is one place where every yard you have quoted, fenced, or been referred sits together, and nothing you spent money to earn goes cold in the gap between the first call and the signed estimate. You still message anyone directly whenever a job needs a real conversation, the system just makes sure the quiet ones never get forgotten. Over a few years that database becomes one of the most valuable things the business owns, a record of every fence you have built and every repair, gate, and neighbor still waiting to happen, and it stays yours no matter what.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The privacy-fence quote that <em>closes itself</em>",
        "body_html": "You quote a homeowner on a backyard run of cedar privacy fence on a Monday and they tell you they are getting one more price and waiting on the HOA to sign off. Normally that is the last you hear of it. Instead the CRM sends a friendly check-in a few days later and a short note the following week, both written to sound like you, and one lands right as the HOA approval comes through. The other two companies never followed up, so when the homeowner is ready, yours is the only name still in front of them, and they book with you without shopping any further. You never sat down to chase it. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing customers and past jobs?",
         "Yes. Your current customers, leads, and job history come in and live in one place, and everything stays yours and exportable. The point is to make the customer list you already have actually book you work."),
        ("Will it really follow up on my quotes automatically?",
         "Yes, on the schedule you approve. An open quote gets a check-in a few days later and more touches over the following weeks, all sent for you, so a homeowner comparing three fence companies keeps hearing from you while the others go quiet. You can jump in and message anyone directly any time."),
        ("Can it bring back past customers for repairs and additions?",
         "Yes. It flags the yards you fenced a few years back that may be due for a repair, a stain, a gate, or an extension, and it sends thank-you and referral asks after a job, so the repeat work and the neighbor referrals come back around without you keeping track."),
        ("How is this different from just keeping notes in my phone?",
         "A phone full of contacts does not follow up, does not remember which yard is due for a repair, and does not tell you which quote is going cold. The CRM does all of that on a schedule, so the repeat work and the quotes you already sent actually turn into booked jobs."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your customers, build your follow-up and referral sequences, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will find the gap where jobs are going cold today.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for fence companies"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-fence-companies.html", "The answering service that feeds it every estimate"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting quotes and customers <em>go cold</em>",
    "cta_sub": "Get a free audit of how many of your quotes and past customers are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ======================= Marketing for Fence Companies =======================
{
    "slug": "marketing-for-fence-companies",
    "trade_slug": "fence_companies", "trade_plural": "fence companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "Marketing for Fence Companies",
    "title": "Marketing for Fence Companies | Top Shelf Business Solutions",
    "og_title": "Marketing for Fence Companies",
    "meta_desc": "Fence company marketing keeps your Google Business Profile active and your photos first in the map pack, so you catch homeowners when they decide to fence.",
    "service_schema_name": "Marketing for Fence Companies",
    "eyebrow": "For Fence Companies",
    "h1_html": "Marketing <em>for Fence Companies</em>",
    "answer_block": "Fence company marketing keeps you visible where fence demand shows up, your Google Business Profile, your photos of clean, straight work, and the map pack, so when a homeowner nearby searches for a fence company as they decide to build, your name is the active, well-reviewed one they call instead of the company that let its profile go stale.",
    "sections": [
        {"h2_html": "Fence demand is <em>local and seasonal</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody shops for a fence company months ahead on a whim. The demand shows up when a homeowner brings home a dog, decides they want privacy from a new neighbor, has to enclose a yard before a pool can pass code, or moves into a new build with a bare lot, and it is intensely local, because they want a company that works their area and knows the local permit and HOA rules. It also swings hard with the calendar, quiet through the cold months, then climbing through spring and summer when everyone is out in the yard at once. New construction adds a second, steadier wave on top of that, because a bare lot is a fence waiting to happen and a builder needs a crew who can keep up. So the whole game is being visible and trusted in your service area the moment someone nearby decides to fence, not running clever ads at people with no yard project in mind. Get found first in that moment and the job is usually yours.</p>'},
        {"h2_html": "Your Google Business Profile is the new <em>storefront</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone searches for a fence company near them, the map pack, those three local listings with the star ratings, is the first thing they see, above the websites and above the ads. And a fence is a look as much as a job, so what sits beside that listing matters more here than for almost any trade: your photos. A profile left quiet for months, with no recent work and a thin trickle of reviews, looks abandoned next to one full of clean, straight fence lines, well-hung gates, and tidy job sites in styles a homeowner recognizes. Those photos do the selling a homeowner is already doing in their head, picturing the fence in their own yard.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Keeping the profile active, complete, and stocked with real photos of your work is a quiet advertisement running in the exact spot people look when they decide to fence. A steady stream of honest reviews does double duty, it is the trust a homeowner wants before they let a crew dig up their property line, and one of the signals that lifts you in the map pack, so the more real jobs you turn into reviews, the higher you sit the next time someone nearby searches.</p>'},
        {"h2_html": "Show up in the <em>towns you actually cover</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Marketing to a whole metro is expensive and forgettable, and it drums up calls for yards an hour past where you want to send a crew. Focusing on the specific towns and neighborhoods you serve, with a profile, photos, and content built around those areas, is what puts you in the map pack where you can actually take the work. It is a tighter, cheaper target than a citywide spend, and it lines up with how people search when a fence is on their mind, fence company near me, privacy fence, fence installation in their own town. It is also how you win the neighboring suburbs a searcher there would never assume you cover, because your profile and local pages name those areas plainly instead of leaving people to guess how far you travel. And it matters for the trades that feed you, the builders, pool companies, and property managers who need a fence crew nearby, because they search the same way and hire the local name they can count on to show up.</p>'},
        {"h2_html": "Be ready before the season, and stay in front of <em>past customers</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Fence demand runs on a calendar you can see coming, the spring thaw when homeowners get back in the yard, the summer pool-and-privacy rush, the new-construction waves that turn bare lots into work, and being visible right before each one beats scrambling once the phone is ringing. A steady local presence, seasonal posts, photos from real jobs, the occasional tip on choosing a material or navigating an HOA, keeps you top of mind for the next fence and reminds past customers you are still the crew to call when a gate sags or a storm takes a section down. This is the public-facing side of staying known. The private, one-to-one follow-up with the customers already in your database is the CRM, and the two work best together, one bringing new homeowners to your door and the other making sure the yards you already fenced never forget who built the fence.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The spring rush, and you are <em>already at the top</em>",
        "body_html": "Spring arrives and half the neighborhood is suddenly out in the yard at once, one homeowner with a new puppy, another who just put in a pool that has to be enclosed, a third staring at a fence the winter finally finished off. They all search for a fence company near them within the same few weeks. Because your Google profile has been kept active all year, with recent photos of clean, straight fence lines and a steady flow of reviews, you sit at the top of the map pack when the searches spike. The homeowners who need a fence that month call the names they can see and trust first, and yours is right there in front of them. The company that let its profile go quiet, with no recent photos and stale hours, is nowhere on the map and never learns the calls happened. Illustrative example, not a client."},
    "faqs": [
        ("Do you post to my Google Business Profile for me?",
         "Yes. We keep it active with photos of your finished fences, updates, and local content on a regular schedule, and keep your hours, services, and service area accurate, so it looks current whenever someone searches for a fence company near them."),
        ("Why do photos matter so much for a fence company?",
         "Because a fence is a look, and a homeowner is picturing it in their own yard before they call. Clean, straight lines, well-built gates, and tidy job sites on your profile do the selling for you, and they set you apart from a company with a bare listing and no work to show."),
        ("What does focusing on my service area actually mean?",
         "It means building your profile and content around the specific towns and neighborhoods your crews can reach easily, instead of spreading a budget across a whole metro. That is what gets you into the map pack where the local, ready-to-fence calls are."),
        ("How is this different from the CRM follow-up?",
         "The CRM follows up privately with people already in your database. Marketing is the public-facing side, your Google profile, photos, reviews, and local visibility, aimed at homeowners who are not your customer yet but need to find and trust you the season they decide to fence."),
        ("How long before I see it working?",
         "A neglected profile can climb in the map pack within weeks once it is active and complete, and it compounds from there as reviews and photos build. Setup is included, and a free audit will show you what your current online presence looks like to someone searching near you today.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for fence companies"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-fence-companies.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the fence company they <em>can already see</em>",
    "cta_sub": "Get a free audit of how visible you actually are in your service area and on Google right now, whether you work with us or not. No credit card, never a call center.",
},
# ==================== Websites & SEO for Fence Companies ====================
{
    "slug": "websites-seo-for-fence-companies",
    "trade_slug": "fence_companies", "trade_plural": "fence companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "breadcrumb_leaf": "Websites & SEO for Fence Companies",
    "title": "Websites & SEO for Fence Companies | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Fence Companies",
    "meta_desc": "A fence company website built for SEO ranks for fence company near me and your city, shows a gallery of clean work, and captures the estimate request directly.",
    "service_schema_name": "Websites & SEO for Fence Companies",
    "eyebrow": "For Fence Companies",
    "h1_html": "Websites &amp; SEO <em>for Fence Companies</em>",
    "answer_block": "A fence company website built for SEO ranks for the searches a homeowner makes when planning a fence, fence company near me, privacy fence, fence installation in your city, shows the gallery and reviews that let them picture the work in their own yard, and captures the estimate request straight to you instead of a lead-seller.",
    "sections": [
        {"h2_html": "The lead-sellers are not competing with you, they are <em>renting you back your own calls</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for a fence company in your town and the top of the page is often a directory or a pay-per-lead marketplace, not the local company. Those sites publish thousands of pages and carry years of authority, so a homeowner lands there first, fills out a form, and that inquiry gets sold, sometimes to several fence companies at once, sometimes back to you for a fee out of your own margin. You do the work of being a real local company with a real crew, and a middleman collects the rent on your own market. Your site not ranking is not a vanity problem. It is the reason an estimate you should have had for free gets sold to you, or handed to three competitors right alongside you, while the local company the homeowner was hoping to find sits invisible a click away. Ranking your own site is how you step out from behind that middleman and meet the homeowner directly, on the search they were already making, with no toll booth in between.</p>'},
        {"h2_html": "Rank for what a homeowner types when <em>planning a fence</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national directory this year for the broadest term, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you serve, and for the exact things people search when a fence is taking shape in their mind: fence company near me, privacy fence, wood fence, vinyl fence, aluminum and ornamental fence, chain-link, pool fence, fence installation and fence repair in your city. Pages built around the fences you actually build and the areas you actually cover are what search engines, and homeowners deep in planning, reward with the click.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This kind of search is slower and more considered than an emergency, and that works in your favor. A homeowner picturing a fence over a few weeks reads more, clicks deeper, and remembers the company whose pages answered their questions and showed the style they had in mind. It is also where the specific, higher-value work lives, the pool enclosure that has to meet code, the ornamental aluminum front yard, the long ranch or agricultural run, the commercial job, searches a national directory never bothers to answer well, and every one of them is a page you can own outright while the directories chase the generic term. A single page that ranks for the right fence search in the right town can pay for the whole site with one job, and then keep paying for years.</p>'},
        {"h2_html": "A homeowner picturing a fence in their yard reads your site <em>before they call</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A fence is a look the homeowner has to live behind for years, so before they ever call they are on your site trying to picture it, deciding whether your work looks clean and straight and whether you look like a real, established company or just a truck and a phone number. That is why a gallery matters more for a fence company than for almost any trade. Real photos of finished fences in the styles you build, wood privacy, vinyl, aluminum, chain-link, gates that hang true, sorted so a homeowner can find the one they are imagining, are what turn a visitor into an estimate request. Pair that with honest reviews, your license and insurance stated plainly, and clear answers to the questions every fence buyer has about HOA approval, permits, and property lines, and a nervous first-time buyer has every reason to reach out.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A lot of that deciding happens in the evening, after a homeowner has spent the day looking at the bare yard and finally sits down to do something about it, which is exactly when a site that loads fast, looks right on a phone, shows the work, and makes requesting an estimate effortless captures the job, instead of a voicemail box nobody is checking or a form buried three clicks deep. An easy estimate request, sitting right next to the gallery, is the single biggest lever on turning a browsing homeowner into a booked measure, so it belongs where a tired visitor can find it at a glance.</p>'},
        {"h2_html": "The leads are <em>yours</em>, permanently",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you pour into a pay-per-lead service disappears the day you stop paying, and the lead was never really yours anyway, it was sold to your competitors in the same breath. A website you own keeps ranking, keeps capturing estimate requests, and keeps compounding in value for as long as it exists, and it is registered to you, not a platform that can drop you tomorrow. The site plugs into the same CRM that follows up on every estimate request it captures over the days a homeowner takes to compare quotes, and the answering service that picks up the calls it drives, so a lead never lands in one place while the follow-up lives in another. The result is one site that ranks, shows the work, and hands every homeowner straight into the system that closes them, instead of a pretty page that looks nice and loses the lead in the gap between the first click and the signed estimate. You are building an asset, not renting attention, and every month it keeps ranking is a month of estimates a lead service would have charged you for one at a time.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A privacy-fence search that finds <em>you, not a directory</em>",
        "body_html": "A homeowner a couple of towns over decides they finally want privacy in the backyard and searches for a fence company near them. Instead of a national directory that would sell their details to three companies at once, they find your site ranking for that town, with a page about privacy fences and a gallery of clean cedar runs you actually built. They scroll the photos until they find the style they had in mind, read a few reviews, see that you are licensed and local, and request an estimate right there. The inquiry comes straight to you, you paid nothing per lead, and no middleman ever touched it. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the fence-type and local searches a national directory has no reason to target well, which is exactly where a local fence company can win."),
        ("How is this different from paying for leads?",
         "A pay-per-lead service rents you an inquiry it also sells to your competitors, and it stops the day you stop paying. A website you own captures estimate requests that are yours alone and keeps working long after it is built, without a fee coming out of every job."),
        ("Do I really need a photo gallery on the site?",
         "For a fence company, yes. A homeowner is buying a look they will live behind for years, and photos of your finished fences in the styles you build, sorted so they can find the one they are imagining, are often what turn a visitor into an estimate request."),
        ("Do I need to rank for every town I serve?",
         "You rank for the ones that matter most first. We build pages for your core service areas and the highest-intent fence searches, then expand, rather than spreading thin across a whole metro at once."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks; broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-home-services.html", "Everything Top Shelf does for fence companies"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-fence-companies.html", "Staying visible in your service area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and lead-sellers taking your estimates, whether you work with us or not. No credit card, never a call center.",
},
]
