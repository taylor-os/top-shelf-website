"""Colony page specs for PAINTERS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a painting-business owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, painter-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500 plans,
$1,500 one-time site) ever appear; no em/en dashes anywhere; "find the gap", never "leak" as a
money metaphor.

The painter reality this file is written to: painting is a considered, planned, big-ticket
purchase, not a 2am emergency. Homeowners line up three estimates and hire whoever answered or
followed up. The money slips through the gap between the walkthrough and the signature. The
urgency is the QUOTE that goes cold, never a leak. Every slug is painting-specific so none
collide with the other trades' colony pages.

Nine questions, mixed find-clients / cost / how-to / problem, spread across all seven money pages:
  1 how-painters-find-clients            (how-to)  -> marketing-for-painters
  2 best-crm-for-painters                (how-to)  -> crm-for-painters
  3 painting-website-cost                (cost)    -> websites-seo-for-painters
  4 answering-service-for-painters-cost  (cost)    -> ai-receptionist-for-painters
  5 get-more-painting-reviews            (how-to)  -> review-software-for-painters
  6 why-painting-estimates-go-cold       (problem) -> automation-for-painters
  7 stop-missing-painting-calls          (problem) -> ai-receptionist-for-painters
  8 book-painting-estimates-online       (how-to)  -> online-booking-for-painters
  9 painting-leads-without-lead-sellers  (problem) -> websites-seo-for-painters
"""

TOPICS = [
# ==================== How Do Painters Find New Clients? (how-to -> marketing) ====================
{
    "slug": "how-painters-find-clients",
    "h1": "How Do Painters Find New Clients?",
    "title": "How Do Painters Find New Clients? | Top Shelf Business Solutions",
    "meta_desc": "Painters find new clients by being the familiar name before a homeowner is ready to repaint. Here is where painting demand starts and how to show up there first.",
    "answer": "Painters find new clients by being visible before the homeowner is ready, since a repaint is planned for months. That means an active Google Business Profile full of before-and-after photos, steady reviews, and referrals from finished jobs, so when someone nearby finally decides to repaint, you are the familiar name they already trust.",
    "sections": [
        {"h2_html": "Painting demand is <em>planned, not sudden</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody calls a painter in a panic. A repaint is planned, sometimes for months. A homeowner stares at a tired living room or a fading exterior all winter and decides in the spring that this is finally the year. By the time they start calling for estimates, they have usually already formed an impression of who looks established and who they would trust with a crew in the house. So finding new clients is less about a clever ad the week they search and more about being visible and familiar in your service area before they are ready.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The painter who was invisible until the homeowner started shopping is competing on price against two other bids. The one whose finished jobs they had been seeing around the neighborhood walks into the estimate half sold. Getting found is really about becoming that second painter before the phone ever rings.</p>'},
        {"h2_html": "Where painters actually <em>get found</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Homeowners look for a painter in a few predictable places, and almost all of them are free to show up in if you stay active.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>The map pack, those three local listings on Google with star ratings, is the first thing most people see, and a profile full of recent before-and-after photos is a portfolio and an ad at once.</li><li>Reviews that describe how you treated the house, arrived on time, kept it tidy, protected the furniture, are what turn a nervous homeowner into a booked estimate.</li><li>Referrals and repeat customers, the cheapest work you can get, come back when you stay in touch instead of vanishing after the last coat.</li><li>Neighborhood visibility, the finished houses on the street and the yard sign out front, keeps your name in front of the people most likely to hire you next.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this is a campaign you run the week a homeowner searches. It is a steady presence that makes you the obvious call when the repaint they have been putting off finally becomes this weekend.</p>'}],
    "bridge_h2": "Be the painter they already know",
    "bridge_text": "Most local painting calls begin with a name a homeowner already recognizes. Keeping your Google profile active, full of real project photos, and well reviewed is how you become that name before the repaint is decided nearby.",
    "bridge_slug": "marketing-for-painters",
    "bridge_label": "Marketing for painters",
    "faqs": [
        ("What is the cheapest way for a painter to get new clients?",
         "The cheapest clients are the ones you have already earned. Past customers and referrals cost almost nothing and close the easiest, so staying in touch after a job is the highest-return thing you can do. After that, a well-kept Google Business Profile is free to set up and puts you in front of homeowners searching nearby."),
        ("How long before marketing brings in painting jobs?",
         "A neglected Google profile that gets active, complete, and full of real photos can start climbing in the map pack within a few weeks, and it compounds as reviews and posts build. Nobody controls Google, so no honest company promises a specific position, but consistency in your service area is what moves it.")],
    "trade_slug": "painters", "trade_plural": "painters",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ What's the Best CRM (and Estimating Follow-Up) for Painters? (how-to -> crm) ============
{
    "slug": "best-crm-for-painters",
    "h1": "What's the Best CRM (and Estimating Follow-Up) for Painters?",
    "title": "What's the Best CRM (and Estimating Follow-Up) for Painters? | Top Shelf Business Solutions",
    "meta_desc": "The best CRM for painters is the one that follows up on every estimate for you, because a painting job is won on the follow-up, not the feature list.",
    "answer": "The best CRM for a painting company is the one that actually follows up on every estimate you send, because painting jobs are won on the follow-up, not the software's feature list. Look for automatic quote follow-up, a customer history that stores the colors you used, and one that feeds your calls and calendar.",
    "sections": [
        {"h2_html": "The feature list is not what wins the <em>job</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Painters shopping for estimating or CRM software tend to compare feature checklists, but a painting job is not won by the fanciest quote template. It is won by whoever followed up after the walkthrough. Most painters do not have a lead problem, they have a follow-up problem: you spend an hour measuring an interior repaint, work up a careful quote, and the homeowner says they are getting a couple of other bids and will think it over. Then you get busy on the jobs you already have and never circle back.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The quote was never dead. It just needed one more call or text a few days later, and that is the thing there is never time for between jobs. So the best CRM for a painter is not the one with the longest feature list. It is the one that makes that follow-up happen on its own, every time, whether or not you remember.</p>'},
        {"h2_html": "What a painter should actually <em>look for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When people search for the best estimating software for painters, what they actually need is the quote plus the follow-up that closes it. A few things separate software that earns its keep from a fancier address book.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Automatic follow-up on every open estimate, on a schedule you set, written to sound like you, so a homeowner comparing three bids keeps hearing from you while the others go quiet.</li><li>A customer record that stores the brand, color, and sheen you used on each room, so a touch-up or a matching repaint years later is easy to quote and easy to win.</li><li>Seasonal reminders that go out on their own, exteriors as the weather warms, interiors and cabinets through the winter, so repeat work comes back without you tracking dates.</li><li>A system that connects to your phone and calendar, so a captured call becomes a followed-up lead instead of a note you re-key into a separate app.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf this is not a separate bill. The CRM is included in the Signature plan at $899 a month, with no setup fee, alongside the AI receptionist and follow-up that feed it. Recover one estimate you would have let go cold and it has paid for itself.</p>'}],
    "bridge_h2": "Put the follow-up on autopilot",
    "bridge_text": "The estimates you already sent are the cheapest jobs you can win back. A CRM keeps every open quote in front of you and follows up on a schedule for you, so the homeowner comparing bids books with you instead of the painter who stayed in touch.",
    "bridge_slug": "crm-for-painters",
    "bridge_label": "CRM for painters",
    "faqs": [
        ("Do painters need separate estimating software and a CRM?",
         "Usually not two tools. The estimate itself matters, but the money is won or lost on the follow-up after it, which is exactly what a CRM handles. A system that stores your quotes and then chases them for you covers what painters actually lose, without a second app to keep in sync."),
        ("Is a CRM worth it for a small painting business?",
         "Often yes, even for a one or two crew shop. The point is not size, it is whether follow-up is falling through. If quotes go quiet and past customers forget your name, a CRM earns its keep by bringing that work back. If you genuinely call everyone back already, you may not need one yet.")],
    "trade_slug": "painters", "trade_plural": "painters",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ How Much Should a Painting Company Website Cost? (cost -> websites-seo) ============
{
    "slug": "painting-website-cost",
    "h1": "How Much Should a Painting Company Website Cost?",
    "title": "How Much Should a Painting Company Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A painting company website ranges from cheap templates to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A painting company website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more than the sticker price is whether it ranks and shows your work. Top Shelf builds a custom five page site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The price quoted for a painting company website swings wildly because painters are not all buying the same thing. A cheap template you fill in yourself and a custom site built to rank in your service area are different products with the same name. Before you compare quotes, it helps to know what you are actually paying for.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A do-it-yourself website builder is cheap monthly, but you do the work, and it is rarely built to rank or to show off your jobs the way a visual trade needs.</li><li>A one-time custom build costs more up front and is yours to keep, but a site alone does little if nobody is doing the ongoing SEO to get it found.</li><li>An agency retainer bundles the build with ongoing SEO and updates, which is where most of the long-term value lives, and also where the monthly cost lives.</li><li>Hidden costs to ask about before you sign: who owns the site, what a change costs, and whether you keep it if you leave.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It is also fair to ask whether you can just have a chatbot build one. A tool can generate a page in minutes, but it will not rank for the towns you cover, it will not show real before-and-after photos of your jobs, and it will not be wired to capture the estimate. The cost of a website is never really the pixels, it is whether it gets found and turns a visitor into a walkthrough.</p>'},
        {"h2_html": "What a painter should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A painting company website earns its money one way: it turns a homeowner planning a repaint into a booked estimate. That means it has to load fast, rank for the towns you cover and the searches people make when they are ready to paint, show real before-and-after photos of homes like theirs, and put a call or book button in front of a visitor before they scroll. Painting sells on the eyes, so a site that hides your actual work behind stock images is leaving its best argument on the table. A beautiful site that never ranks and buries your number is the most expensive kind, because you paid for it and it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can find the gap between where your current site stands and where the searches actually are.</p>'}],
    "bridge_h2": "Get a painting site that pays for itself",
    "bridge_text": "A painting website is only worth what it brings in. Ours is built to rank for the towns you cover, show the work that sells painting on sight, and turn searches into booked estimates, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-painters",
    "bridge_label": "Websites & SEO for painters",
    "faqs": [
        ("Is $1,500 a fair price for a painting website?",
         "It sits in the normal range for a custom-built site, well above a fill-in template and well below a long agency contract. What matters more than the number is whether the site ranks for your towns and shows your work. At Top Shelf a custom five page site is $1,500 one-time and yours to keep, or free on any monthly plan."),
        ("Can I just use a website builder or a chatbot to make my painting site?",
         "You can get a page online cheaply that way, but a generated or template page rarely ranks for your service area and rarely shows the real before-and-after work that sells painting. The cost that matters is not the build, it is the jobs a site nobody finds never brings you.")],
    "trade_slug": "painters", "trade_plural": "painters",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ How Much Does an Answering Service for Painters Cost? (cost -> ai-receptionist) ============
{
    "slug": "answering-service-for-painters-cost",
    "h1": "How Much Does an Answering Service for Painters Cost?",
    "title": "How Much Does an Answering Service for Painters Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for painters often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers every call in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for painters usually bill per call, per minute, or on a monthly retainer, so a busy stretch gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call and books the estimate is included in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy month turns into a big bill. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of tire-kickers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty homeowner or a slow operator costs you more than a quick call.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A painter feels this most in the season. Estimate calls cluster in the spring and summer and after the workday, when a homeowner scrolling for painters finally decides to reach out, so a per-call meter climbs at the exact moment the estimate requests do.</p>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner lining up three painting estimates books with the first painter who picked up. The real cost of no coverage is not a monthly fee, it is the repaint that went to the shop that answered. But a generic call center reading a script cannot tell a two-room refresh from a whole-exterior job or a commercial bid, so you can pay for coverage and still get poor qualifying.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, asks what you would ask, interior or exterior, how many rooms, cabinets or trim, and the timeline, and books the estimate on your calendar. It is included in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One interior repaint or exterior job you would have lost to voicemail often covers the plan for months, and everything it catches after that is on top.</p>'}],
    "bridge_h2": "Answer every estimate call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers every call, qualifies the repaint the way you would, and books the estimate, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-painters",
    "bridge_label": "AI receptionist for painters",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service for painters?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when the estimate calls do, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the repaint it books instead of losing to voicemail."),
        ("Do I pay more during the busy painting season?",
         "No. It answers around the clock as part of the plan, including the spring and summer rush when the most estimate calls come in, with no surcharge and no overage. The flat price is the point, so a great month does not turn into a big bill.")],
    "trade_slug": "painters", "trade_plural": "painters",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ How Do Painters Get More Google Reviews? (how-to -> review-software) ============
{
    "slug": "get-more-painting-reviews",
    "h1": "How Do Painters Get More Google Reviews?",
    "title": "How Do Painters Get More Google Reviews? | Top Shelf Business Solutions",
    "meta_desc": "Painters get more Google reviews by asking at the reveal, when the room looks new, and making it one tap with a before-and-after photo. Here is how to do it every time.",
    "answer": "Painters get more Google reviews by asking every happy customer at the reveal, the moment the last coat dries and the room looks new, and making it a one-tap post they can add a photo to. Most painters do great work but forget to ask or ask too late, when the excitement has faded.",
    "sections": [
        {"h2_html": "The problem is timing and asking, not your <em>work</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most painters have plenty of happy customers and not many reviews, and the gap is not the quality of the work. It is that asking gets forgotten, feels awkward, or happens too late. The best moment is the one most painters miss: the reveal, when the last coat dries, the tape peels off, the furniture slides back, and the homeowner steps into a room that looks like a different house. Wait until you are packing the truck and it slips your mind. Ask three weeks later and the excitement, along with the motivation, is gone.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The second problem is friction. Even a thrilled customer will not hunt down your profile, log in, and figure out where to click. Every extra step loses a share of the people who meant to leave a review. If leaving one is not close to a single tap, most of the goodwill you earned in that house never makes it online.</p>'},
        {"h2_html": "How to get more, <em>consistently</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more reviews is less about a clever trick and more about doing the same simple thing after every single job, which is exactly what falls apart when you are busy. A repeatable process beats good intentions.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Ask every happy customer, every time, not just the ones you remember, so it is never left to chance.</li><li>Ask at the reveal, the moment the transformation is fresh and the homeowner is thrilled, when the request feels welcome rather than pushy.</li><li>Make it one tap with a direct link to your Google profile, by text and email, and nudge them to add a photo, because a painting review with a before-and-after attached sells the next job on its own.</li><li>Reply to every review, good or bad, which reassures the next reader and helps your local ranking.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Doing all of that by hand after each job is what slips first on a busy week. Software fixes it by sending the ask automatically the moment a job is marked done, so the request goes out every time without you thinking about it. One rule keeps you on the right side of Google policy: ask every customer honestly, and never filter out unhappy ones or pay for reviews.</p>'}],
    "bridge_h2": "Turn every finished repaint into a review",
    "bridge_text": "Review software asks every happy customer at the reveal and makes it one tap with a photo, so your listing fills with real before-and-after proof and the next homeowner comparing painters calls you first.",
    "bridge_slug": "review-software-for-painters",
    "bridge_label": "Review software for painters",
    "faqs": [
        ("Is asking customers for reviews against Google's rules?",
         "Asking every customer for an honest review is allowed and encouraged. What is not allowed is filtering out unhappy customers, offering incentives, or paying for reviews. Asking everyone at the reveal and making it easy is squarely within the rules."),
        ("Should painting reviews include before-and-after photos?",
         "Yes, and for a painting company that is the most valuable part. Painting is one of the few trades where the proof fits in a photo, so a review with a before-and-after attached convinces the next homeowner and quietly builds a portfolio on your Google listing that you never had to stage.")],
    "trade_slug": "painters", "trade_plural": "painters",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do My Painting Estimates Go Cold? (problem -> automation) ============
{
    "slug": "why-painting-estimates-go-cold",
    "h1": "Why Do My Painting Estimates Go Cold?",
    "title": "Why Do My Painting Estimates Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Painting estimates go cold because a repaint is a slow, big-ticket decision, and homeowners book whoever stayed in touch. Here is how to keep every quote warm while they decide.",
    "answer": "Painting estimates go cold because a repaint is a slow, big-ticket decision, not an urgent one. A homeowner gathers three bids, then sits on it for weeks while they save up or wait for the season, and books whoever stayed in touch. Silence rarely means your number was too high, it means the follow-up stopped.",
    "sections": [
        {"h2_html": "A repaint is a decision measured in <em>weeks, not hours</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Unlike a burst pipe, a repaint almost never has to happen this week. A homeowner has stared at the same tired walls for a year, so once they finally line up estimates, the deciding can stretch on: they wait for dry exterior weather, save toward a whole-house interior, or finish another project first. That long stretch between your walkthrough and their yes is where the job is actually won, and it is won on attention rather than on being the lowest bid.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Your estimate is also a bigger investment than most trades give. You spent an hour measuring rooms, talking through colors, sheens, and prep, and left a careful number for a cabinet refinish or a full exterior. Two or three painters did the same, and the quotes now sit side by side on the kitchen counter. Weeks later the winner is simply the one whose name kept resurfacing, while the others read the quiet as a no and moved on.</p>'},
        {"h2_html": "A cold estimate is a booked <em>deposit that never lands</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For a painter, an estimate that stalls is not just a missed job, it is a deposit that never got made. Painting is paid in stages, a deposit to reserve the crew, a progress payment as the work moves, the balance at the end, so every cold estimate is a slot on your calendar that stayed empty and a week of crew time you never sold. On a big interior or exterior, that is real money drifting off without a word.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">These estimates die because the long consideration cycle outlasts your memory. You cannot hold weeks of open quotes in your head while you are running crews, so the ones you meant to revisit quietly expire. Automation closes that gap by putting each estimate on its own timeline and sending the right nudge for you, a check-in the week after the walkthrough, a warm-weather reminder when exterior season opens, a note that revisits the colors from the consultation. You build it once, and the big jobs you already quoted keep converting instead of aging out in silence.</p>'}],
    "bridge_h2": "Keep every estimate warm while they decide",
    "bridge_text": "Automation puts each open estimate on a timeline and keeps it warm with painter-timed nudges, a check after the walkthrough, a reminder when exterior season turns, so the big jobs you quoted stay alive through the whole long decision.",
    "bridge_slug": "automation-for-painters",
    "bridge_label": "Automation for painters",
    "faqs": [
        ("How long is a painting estimate worth chasing?",
         "Longer than you would think. Because the decision runs slow, an exterior quote from the spring may not book until summer, and an interior can wait for a free weekend or the holidays, so a real estimate stays worth a nudge for weeks or even a couple of months. Automation keeps it warm without you tracking dates, and a free audit can find the gap where your estimates are quietly going cold today."),
        ("Should I drop my price when an estimate goes quiet?",
         "Usually not. On a big repaint, quiet almost never means you were too expensive, it means the decision is still open and nobody has checked back in. Cutting your number teaches homeowners to wait you out and thins the margin on a job already paid in stages. A well-timed follow-up wins far more of these than a discount ever will.")],
    "trade_slug": "painters", "trade_plural": "painters",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ How Do I Stop Missing Calls While I'm Up a Ladder? (problem -> ai-receptionist) ============
{
    "slug": "stop-missing-painting-calls",
    "h1": "How Do I Stop Missing Calls While I'm Up a Ladder?",
    "title": "How Do I Stop Missing Calls While I'm Up a Ladder? | Top Shelf Business Solutions",
    "meta_desc": "You miss calls because they ring while your hands are full, and a homeowner lining up painters does not leave a voicemail. Here is how to catch every estimate call.",
    "answer": "You miss calls because they ring while your hands are full, on a ladder cutting in a ceiling or spraying cabinets, and a homeowner lining up estimates does not leave a voicemail. They call the next painter. The fix is not working harder, it is making sure every call gets answered while you paint.",
    "sections": [
        {"h2_html": "The call comes exactly when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Painting is a hands-full trade. When the phone rings you are often on a ladder cutting in a ceiling, taping off a room, or elbow-deep in a cabinet spray job, and none of those are moments you can stop and take a call. The busier you are, the more calls you miss, which means your best weeks are also the ones where the most work slips away. It is not a discipline problem. One person cannot paint the job in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but it is not one. A homeowner lining up painters to compare is not going to leave a message and wait. They move down the list until someone answers and agrees to come look, and by the time you check your phone at lunch, the estimate is already booked with someone else.</p>'},
        {"h2_html": "The estimate goes to the painter who <em>answered</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Painting runs on that first contact more than most trades, because a homeowner cannot compare bids until someone shows up to give one. So the estimate, and the big-ticket repaint behind it, goes to whoever they reached, not always the best painter and rarely the one who was too busy to pick up. The calls you are most likely to miss are the ones worth the most.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never misses a ring and can qualify the job, not a voicemail box and not a call center that does not know a two-room refresh from a whole exterior. What actually works is something that answers on the first ring, finds out whether it is interior or exterior, how many rooms, cabinets or trim, and the timeline, gets the address, and either books the estimate or texts you the details, so you never touch the phone while you are on a ladder and never lose the call in the first place.</p>'}],
    "bridge_h2": "Stop losing estimates to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring while your hands are full, qualifies the repaint, and books the estimate or texts you the details, so the job never rolls to voicemail while you are up a ladder.",
    "bridge_slug": "ai-receptionist-for-painters",
    "bridge_label": "AI receptionist for painters",
    "faqs": [
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are on a ladder, spraying cabinets, or already on another call. Something that always answers and qualifies the job is what catches the estimate calls a forward would still miss."),
        ("Would a homeowner rather reach a real person?",
         "What a homeowner lining up painters wants most is to know someone picked up and will come look at the job. A calm voice that captures the details beats a voicemail box every time, and the receptionist is upfront about what it is and hands the booked estimate and the scope straight to you.")],
    "trade_slug": "painters", "trade_plural": "painters",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== Should a Painting Company Let Customers Book Estimates Online? (how-to -> online-booking) ========
{
    "slug": "book-painting-estimates-online",
    "h1": "Should a Painting Company Let Customers Book Estimates Online?",
    "title": "Should a Painting Company Let Customers Book Estimates Online? | Top Shelf Business Solutions",
    "meta_desc": "Should a painting company let customers book estimates online? For routine repaints, yes. Here is how self-scheduling ends phone tag without wasting your evenings.",
    "answer": "Yes. A lot of painting work, interior repaints, cabinet quotes, whole-exterior estimates, is planned, not urgent, and those homeowners would happily book a walkthrough online if you let them. A booking link on your real availability turns days of phone tag into an estimate that lands on your calendar while you work.",
    "sections": [
        {"h2_html": "Phone tag is quietly costing you <em>estimates</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner decides to repaint and wants someone to come look and give them a price. Your crew is on a job, so you call back that evening, they are putting the kids to bed, you trade voicemails, a day passes, and the estimate gets booked by the painter who could lock in a time on the spot. The homeowner was ready to schedule the moment they thought of it. The back and forth was the problem, not the interest, and a repaint is a big enough job that losing the estimate means losing real money.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Every one of those handoffs is a place the homeowner can drop out. When someone is motivated enough to reach out, making them wait for a callback is the surest way to lose a routine job you should have had, especially to a competitor whose site let them just pick a time.</p>'},
        {"h2_html": "Yes, if it <em>sorts the job first</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The honest worry is that online booking sends you across town to quote a single accent wall. A good booking flow prevents that by asking what matters first: interior or exterior, how many rooms or the size of the exterior, cabinets, trim, or a deck, residential or commercial, and the timeline. A real repaint books an estimate, and a tiny job or a vague inquiry can be routed to a quick call instead, so your evenings go to walkthroughs worth driving to.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">You stay in control of it. You set which jobs are bookable online, how long an estimate takes, how much notice you need, and how much drive-time buffer to leave, so you are never booked with no way to get there. It syncs to the calendar you already use so it cannot double-book you or a crew lead, and it sends a confirmation and a reminder that cut down no-shows. So the answer is yes, for the routine work, as long as it qualifies the job before it books.</p>'}],
    "bridge_h2": "Let homeowners book the walkthrough themselves",
    "bridge_text": "Online booking lets routine painting estimates schedule themselves on your real availability, sorted by scope first, so you stop trading voicemails and wake up to the walkthrough already on your calendar.",
    "bridge_slug": "online-booking-for-painters",
    "bridge_label": "Online booking for painters",
    "faqs": [
        ("Will online booking send me to quote jobs that are not worth the drive?",
         "Only if you let it. The form asks about the scope first, interior or exterior, how many rooms, cabinets, residential or commercial, so a real repaint books an estimate and a one-wall touch-up or a vague inquiry can be routed to a quick call. Your time goes to walkthroughs worth driving to."),
        ("Where should a painting company put its booking link?",
         "Everywhere a homeowner already meets you: your website, your Google Business Profile, your email signature, your project photos on social, and the text you send after a call. Each one turns from a dead end that needs a callback into a place someone can book an estimate in one tap.")],
    "trade_slug": "painters", "trade_plural": "painters",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Do I Get Painting Leads Without Paying Lead Sellers? (problem -> websites-seo) ========
{
    "slug": "painting-leads-without-lead-sellers",
    "h1": "How Do I Get Painting Leads Without Paying Lead Sellers?",
    "title": "How Do I Get Painting Leads Without Paying Lead Sellers? | Top Shelf Business Solutions",
    "meta_desc": "Stop renting painting leads from pay-per-lead sites that sell the same lead to three painters. Here is how to own leads that are yours with a website that ranks.",
    "answer": "You stop renting leads by owning the place homeowners find you: a website that ranks for the towns you cover and the painting searches people actually make. A pay-per-lead service sells the same lead to three painters who then underbid each other, and it stops the day you stop paying. A ranking site is yours.",
    "sections": [
        {"h2_html": "The lead-sellers rent you back your <em>own leads</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for a painter in your town and the top of the page is often a directory, a national booking middleman, or a pay-per-lead service, not the local shop. Those sites publish thousands of pages and have years of authority behind them, so when a homeowner searches, they land there first, fill out a form, and that lead gets sold, often to three or four painters at once who then race to underbid each other. Your site not ranking is not a vanity problem. It is the reason a homeowner you could have had for free turns into a lead you pay for and split with your competitors.</p>'},
        {"h2_html": "Own the leads with a site that <em>ranks and shows the work</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national directory this year for the broadest term, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you cover, and for the exact searches a homeowner makes when they are ready to hire: house painters near me, interior painters in your city, cabinet refinishing, exterior painting. Painting sells on the eyes, so a site with real before-and-after photos of homes like theirs wins a homeowner over and gives search engines genuine, specific content at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The difference is ownership. Every dollar you put into a pay-per-lead service disappears the day you stop paying, and the lead was never really yours anyway. A website you own keeps ranking, keeps capturing estimate requests, and keeps compounding in value for as long as it exists, and the lead it brings you is yours alone, not sold to the three painters bidding against you. A free audit can find the gap between where your site stands today and where those searches actually are.</p>'}],
    "bridge_h2": "Own your painting leads, do not rent them",
    "bridge_text": "A website built to rank for the towns you cover captures estimate requests that are yours alone, instead of a pay-per-lead service selling the same homeowner to three painters who underbid each other.",
    "bridge_slug": "websites-seo-for-painters",
    "bridge_label": "Websites & SEO for painters",
    "faqs": [
        ("Are pay-per-lead services worth it for painters?",
         "They can bring calls, but the same lead is usually sold to several painters who then race to underbid each other, and it all stops the day you stop paying. A website you own captures leads that are yours alone and keeps working long after it is built, without a fee coming out of every job."),
        ("How do painters get leads for free?",
         "The closest thing to free is ranking your own website and Google Business Profile for the towns you serve. It takes time to build rather than money per lead, and once it ranks the estimate requests belong to you. Referrals and past customers are the other low-cost source worth staying in touch with.")],
    "trade_slug": "painters", "trade_plural": "painters",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
