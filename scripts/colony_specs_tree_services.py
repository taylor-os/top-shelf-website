"""Colony page specs for TREE SERVICES (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a tree-service owner would search, answered directly up top (the
40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the page's
authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, tree-service-specific substance (the generator owns
shell, schema, events, keyword placement). Same honesty rules as the money specs: no invented
stats, percentages, prices, or clients; hedge instead of overpromise; only the real prices
($299/$899/$2,500 plans, $1,500 one-time site) ever appear, and never an invented tree price; no
em or en dashes anywhere; never "leak" as a metaphor. Ethics: the AI receptionist handles intake
and scheduling only, it never binds a removal quote, and nothing here promises a tree is safe.

The tree-service reality this colony leads with, and does not converge on the plumber/roofer set:
storm-driven surges where every homeowner with a limb on the roof calls at once, licensed and
insured as the first trust question, big-ticket removals that draw second bids, a crew sixty feet
up running a saw who cannot answer, and seasonal, weather-driven demand.

Six questions, mixed cost / problem / how-to, spread across three money pages:
  1 tree-service-website-cost              (cost)    -> websites-seo-for-tree-services
  2 tree-service-answering-service-cost    (cost)    -> ai-receptionist-for-tree-services
  3 is-a-crm-worth-it-for-a-tree-service   (cost)    -> crm-for-tree-services
  4 why-tree-services-miss-calls           (problem) -> ai-receptionist-for-tree-services
  5 why-tree-service-estimates-go-cold     (problem) -> crm-for-tree-services
  6 how-do-tree-services-get-more-customers (how-to) -> marketing-for-tree-services
"""

TOPICS = [
# ============ How Much Does a Tree Service Website Cost? (cost -> websites-seo) ============
{
    "slug": "tree-service-website-cost",
    "h1": "How Much Does a Tree Service Website Cost?",
    "title": "How Much Does a Tree Service Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A tree service website ranges from cheap templates to several thousand for a custom build. What matters more is whether it turns storm searches into estimate requests. Top Shelf builds yours for $1,500 one-time, or free on any plan.",
    "answer": "A tree service website can run from a couple hundred dollars for a template to several thousand for a custom build. What matters more than price is whether it earns trust fast, shows you are licensed and insured, and turns a storm search into an estimate request. Top Shelf builds a custom five page site for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a tree service site actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner searching for a tree service is usually searching in a hurry and a little scared. A branch is resting on the roof, a trunk is leaning toward the house, or a dead oak has them worried about the next windstorm. The site that wins that visitor does a few specific things, and none of them are about looking pretty.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Makes requesting an estimate the obvious next step, with a tap-to-call button and a short request form near the top, because a worried homeowner will not dig for your number.</li><li>Shows you are licensed and insured right away, since that is the first thing a homeowner asks before letting a crew put a saw in a tall tree over their house.</li><li>Loads fast and reads clearly on a phone, because most of these searches happen outside, standing under the tree in question.</li><li>Ranks for the searches people actually make, like tree removal near me and emergency tree service, in the towns you cover.</li><li>Shows real photos of your crew and your work, a large removal, a clean cleanup, so a stranger can trust you with something dangerous.</li></ul>'},
        {"h2_html": "What it costs, and what you should <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A tree service site earns its money one way: it turns a homeowner searching after a storm into a call your crew can bid. That is why the price tag matters less than what the site does with a visitor. A handsome site that never ranks and buries your number is the most expensive kind, because you paid for it and it brings you nothing, the same way the real cost of a missed call is the removal you never heard about.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that gets it ranking for the towns you cover is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that wins the storm call",
    "bridge_text": "A tree service website is only worth the work it brings in. Ours is built to rank for the towns you cover, prove you are insured, and turn a storm search into an estimate request, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-tree-services",
    "bridge_label": "Websites & SEO for tree services",
    "faqs": [
        ("Is a cheap template site good enough for a tree service?",
         "It can get you online, but a template you fill in yourself is rarely built to rank or to convince a nervous homeowner you are safe to hire. If a site is not getting found or turning storm searches into estimate requests, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "tree_services", "trade_plural": "tree services",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== What Does a Tree Service Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "tree-service-answering-service-cost",
    "h1": "What Does a Tree Service Answering Service Cost?",
    "title": "What Does a Tree Service Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "When a storm hits, everyone with a limb on the roof calls at once, and a live answering service meters you hardest right then. Top Shelf answers all of it 24/7 on the flat $899 Signature plan, with no per-call fee.",
    "answer": "When a storm rolls through, every homeowner with a limb on the roof calls at once, the exact surge a service that bills per call or per minute charges you hardest for. Your crew is sixty feet up running a saw and cannot pick up. Top Shelf answers it all 24/7 for a flat $899 a month, no per-call meter.",
    "sections": [
        {"h2_html": "The storm surge is the whole game, and it is when a meter <em>hurts most</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a big storm moves through, the phone does not ring here and there across the week, it lights up all at once. Every homeowner with a limb through the roof, a trunk across the driveway, or a split branch swinging over the porch is dialing within the same few hours, and each of them is working down a list of companies, not calling only you. That cluster of calls is the whole reason a tree service pays for phone coverage, and it is also the precise moment a live answering service costs you the most, because the usual ways they bill, per call, per minute, or a retainer with overage, all climb with exactly the volume a storm dumps on you. You face the biggest phone bill of the year in the same week the meter is running hardest.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Meanwhile your crew is no help, and not because anyone is slacking. When the wind is still blowing you are already out clearing the first tree, sixty feet up tied into a canopy, or on the ground running a saw and a chipper that drown out any ringtone. Nobody can stop a cut to take a call safely. So the surge you count on all season rolls to a meter you did not budget for, or worse, to voicemail, and a homeowner staring at a tree on the house does not leave a message. They hang up and call the next crew on the list.</p>'},
        {"h2_html": "What one storm call is worth, and the <em>flat plan that catches it</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Here is what makes a missed storm call so expensive: it is rarely a small job. The call that rolls to voicemail after a windstorm is usually an emergency removal, a tree lifted off the roof, a trunk cut off a car, a heavy limb pulled clear of the service line, the kind of ticket that runs into real money and is your highest-margin work of the year. A generic call center reading a script cannot tell that call apart from a homeowner who wants a someday price on shaping a hedge, so even paid coverage can fumble the one that matters while still billing you for the one that does not.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf answers it differently. An AI receptionist picks up on the first ring, storm night or Sunday, triages the way you would, and books the routine work or flags a genuine emergency to your phone, all for a flat $899 a month on the Signature plan with no per-call or per-minute meter no matter how hard it storms. Catch one emergency removal you would have lost to voicemail and the plan has paid for itself many times over. It handles intake and scheduling only. It never puts a price on a removal or promises a tree is safe, it gathers the details and hands the real emergencies straight to you to decide whether to roll a crew.</p>'}],
    "bridge_h2": "Answer every storm call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, tells a tree on a house from a someday trim, and books it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-tree-services",
    "bridge_label": "AI receptionist for tree services",
    "faqs": [
        ("What happens when a storm sends a rush of calls at once?",
         "The AI receptionist answers every one on the first ring at the same moment, so a surge that would overwhelm one person, or run up a charge per call on a live service, is simply handled. Each caller is triaged, the emergencies are flagged to you, and the routine estimates are booked, all on the flat plan with nothing climbing as the calls pile up."),
        ("Is a flat plan really cheaper than paying per call?",
         "For a tree service it usually is, and it is far more predictable. A metered service bills you hardest during the storm week when the calls flood in, while the Signature plan stays a flat $899 a month no matter how busy the weather gets. The bigger saving is the emergency removal it books instead of losing to voicemail while your crew is up in a tree.")],
    "trade_slug": "tree_services", "trade_plural": "tree services",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Is a CRM Worth It for a Tree Service? (cost -> crm) ============
{
    "slug": "is-a-crm-worth-it-for-a-tree-service",
    "h1": "Is a CRM Worth It for a Tree Service?",
    "title": "Is a CRM Worth It for a Tree Service? | Top Shelf Business Solutions",
    "meta_desc": "A big tree removal gets two or three bids over weeks, storm cleanups pile up, and the oak you trimmed two years ago is due again. A CRM brings those removals and trims back, in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most tree services, yes. A big removal gets two or three bids over weeks, so the crew that keeps following up wins it. A CRM does that for you, works your post-storm cleanup list, and brings the yards you trimmed years ago back for their next trim. It comes in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "A big removal is decided over weeks, and <em>follow-up wins it</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The jobs that pay a tree service best are the ones a homeowner thinks hardest about. When you walk a property and quote taking down a mature oak near the house, or clearing a fence line of storm-damaged trees, that is a real expense, so almost nobody says yes on the spot. They tell you they want to think it over or get one more look, then they collect two or three bids and sit with it for a week or two while the wind dies down and life gets busy. The estimate is not dead. It is parked, waiting on one more touch.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is the job a CRM wins. It keeps every open removal and trim bid in front of you and sends a check-in a couple of days later and another after that, on a schedule you approve and in words that sound like you. The homeowner weighing three crews on a costly removal keeps hearing from the one who followed up, which is rarely the cheapest and almost always the one still in front of them when they finally decide. Doing that from memory between jobs is exactly what falls apart in the middle of a busy season, so the bids you already earned drift to whoever happened to circle back.</p>'},
        {"h2_html": "Storm lists and the trees that <em>come due again</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The other half of the value is the work that comes back on its own when someone is paying attention. A busy storm week hands you a stack of one-time cleanups, names and addresses on scraps of paper that too often never get entered anywhere. Dropped into a CRM instead, each of those becomes a customer you can reach again, because the trees on that property did not stop growing. Beyond the storm list, the seasons do the selling: late winter is for dormant-season pruning, the weeks before storm season are when a nervous homeowner wants weak limbs gone, and a dry spell turns dead wood into an obvious hazard.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>The oak you thinned two years ago is due for another look, and a reminder that lands before the next windy stretch reaches a homeowner already worried about it.</li><li>A cleanup customer from the last storm gets a note the following spring about the weak limbs next door that will fail next, turning one emergency into a standing account.</li><li>Every property, its tree history, and your notes live in one place, so you reach the right yard with the right reminder instead of trusting your memory of a job from three seasons back.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this is a separate bill. The CRM comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The test is simple and it is the same as the phone: win back a single removal you would have let go cold, or reactivate a handful of trims from your old list, and it has already paid for itself.</p>'}],
    "bridge_h2": "Put your customer list to work",
    "bridge_text": "The estimates and past yards you already have are the cheapest jobs you can get. A CRM follows up on every one for you, so they call you next instead of the crew that stayed in touch.",
    "bridge_slug": "crm-for-tree-services",
    "bridge_label": "CRM for tree services",
    "faqs": [
        ("Which is worth more, chasing removal bids or reminding past customers?",
         "Both pay, and a CRM does not make you choose. Open removal bids are the fastest money, because the homeowner already wants the work and is only deciding who does it, while seasonal reminders to past yards are the cheapest, since the trust and the property knowledge are already there. The system works both at once without you tracking either by hand."),
        ("Will it remember which trees on a property are due for work?",
         "Yes. Each property carries its own history and notes, what you removed, what you trimmed, what you treated and when, so the reminder that goes out is specific to that yard instead of a generic blast. That is how a one-time storm cleanup becomes pruning next spring and the removal after that.")],
    "trade_slug": "tree_services", "trade_plural": "tree services",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do Tree Services Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-tree-services-miss-calls",
    "h1": "Why Do Tree Services Miss So Many Calls?",
    "title": "Why Do Tree Services Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Tree services miss calls because the crew is running a saw high in a tree when the phone rings, and after a storm everyone calls at once. A homeowner with a tree on the roof calls the next crew.",
    "answer": "Tree services miss calls because they come when the crew has both hands full, up in a bucket, running a chainsaw, or feeding the chipper, and after a storm they all ring at once. A homeowner with a tree on the roof does not leave a voicemail. They call the next crew. The fix is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes when your crew <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Tree work is a hands-full, high-noise trade. When the phone rings your climber is forty or sixty feet up tied into a canopy, the ground crew is running saws and feeding a chipper that drowns out any ringtone, and nobody can safely stop mid-cut to take a call. The busier the day, the more calls slip by, which means your best weeks are also the ones where the most work gets away. It is not a discipline problem. A crew taking a tree down cannot answer the phone at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a tree emergency it is not one. A homeowner watching a cracked limb sag over the roof is not going to leave a message and wait. They move down the list until a person answers, and by the time you check your phone between jobs, the removal is already gone to the next crew.</p>'},
        {"h2_html": "After a storm, missed calls are your most <em>expensive misses</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A missed storm emergency, a tree on a house, a trunk across the driveway, a limb hung up over a power line, is the highest-margin work you can get, and it comes when every other crew in town is slammed too. Those calls land in the same few days after a blow, exactly when a homeowner will pay a premium for whoever shows up prepared, and exactly when your own crew is already out clearing the last one and cannot reach the phone. So the calls you are most likely to miss are also the ones worth the most.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can tell an emergency apart from a call that can wait. A voicemail box cannot triage, and a generic call center does not know a tree through a roof from a someday stump grind. What actually works is something that answers on the first ring day or night, asks whether anyone is hurt and whether the tree is on the house or a line, gets the address, and either books the routine work or flags a true emergency straight to your phone. It handles the intake only. It will not promise a tree is safe or price the removal, so you decide whether to roll a crew without ever missing the call in the first place.</p>'}],
    "bridge_h2": "Stop losing storm calls to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, tells a tree on a house from a someday trim, and books it or flags it to you, so the storm call never rolls to voicemail while your crew is up in a tree.",
    "bridge_slug": "ai-receptionist-for-tree-services",
    "bridge_label": "AI receptionist for tree services",
    "faqs": [
        ("Would a customer rather reach a real person?",
         "In a storm emergency, what a homeowner needs most is to know a real crew is handling it, and a calm voice that captures the details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, and hands true emergencies straight to you. It never promises the tree is safe or prices the job, you do that on site."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are running a saw, up in a bucket, or already on another storm call. Something that always answers and triages is what catches the calls a forward would still miss.")],
    "trade_slug": "tree_services", "trade_plural": "tree services",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do My Tree Service Estimates Go Cold? (problem -> crm) ============
{
    "slug": "why-tree-service-estimates-go-cold",
    "h1": "Why Do My Tree Service Estimates Go Cold?",
    "title": "Why Do My Tree Service Estimates Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most tree service estimates go cold not over price but because nobody followed up. A big removal gets two or three bids, the homeowner takes time to decide, and the job goes to whoever checked back in.",
    "answer": "Most tree service estimates go cold not because your price was wrong, but because nobody followed up. A big removal is real money, so the homeowner gathers two or three bids and takes time to decide, and the job goes to whoever checked back in. A quiet estimate is usually a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "Silence usually means still deciding, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet removal bid as a no on price, so you drop it and move on. But a large removal is real money, often the most a homeowner has spent on the yard in years, so they do exactly what anyone does with a big-ticket decision: they gather two or three bids and take a few days to sit with it. They meant to think it over, then a storm rolled through or the week filled up, and your estimate slid down the pile. A week later they could not tell you apart from the other crews who walked the property.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The one who gets the job is usually not the cheapest. It is the one who stayed in front of them: a friendly check-in a couple of days later, a quick note answering the question they were stuck on. That second touch is what turns a maybe into a booked removal, and it is exactly the thing there is no time for between jobs.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Tree crews do not skip follow-up because they are lazy. They skip it because the day fills up. You finish a removal, roll to the next, handle the storm work that jumped the line, and by evening the estimate you walked Tuesday is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest estimates to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which removal and trim bids are still open and going cold.</li><li>The follow-up depends on you remembering, so it competes with the actual work and loses.</li><li>By the time you circle back, the homeowner has already booked the crew that beat you to it.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open estimate gets a couple of timed check-ins automatically, written to sound like you, the homeowner comparing bids keeps hearing from you while the others go quiet, and the removal you already walked stops slipping away.</p>'}],
    "bridge_h2": "Follow up on every estimate, automatically",
    "bridge_text": "A CRM keeps every open removal and trim bid in front of you and sends timed check-ins for you, so a homeowner comparing bids keeps hearing from you while the other crews go quiet.",
    "bridge_slug": "crm-for-tree-services",
    "bridge_label": "CRM for tree services",
    "faqs": [
        ("How many times should I follow up on a removal estimate?",
         "A couple of light touches over the first week or two catches most of the maybes without being pushy: a check-in a few days after you walk the property, then a short note answering common questions. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly check-in reads as attentive, not spammy, and most homeowners appreciate the nudge on a big decision they meant to get back to you on. You can always jump in and message anyone directly.")],
    "trade_slug": "tree_services", "trade_plural": "tree services",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Do Tree Services Get More Customers? (how-to -> marketing) ========
{
    "slug": "how-do-tree-services-get-more-customers",
    "h1": "How Do Tree Services Get More Customers?",
    "title": "How Do Tree Services Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Tree services get more customers by being easy to find and easy to trust the moment a storm hits, then turning past customers into repeat seasonal work. Here is where the calls actually come from.",
    "answer": "Tree services get more customers by being easy to find and easy to trust the moment someone needs a tree handled. That means showing up in the local map results for tree removal near me, carrying a steady stream of recent reviews, and being visible before storm season instead of scrambling after it. Your past customers are the other half.",
    "sections": [
        {"h2_html": "Get found where the <em>storm calls start</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a homeowner needs a tree handled, especially right after a storm, they reach for their phone and pick from the first few local results: the little map with three listings, star ratings, and a call button. Most people call one of those three without ever scrolling to the plain results below. So being in that map pack is where most new tree work actually begins, and it runs on your Google Business Profile, whether it is verified, complete, and active, how close you are to the searcher, and how many recent, genuine reviews you have.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Reviews carry extra weight for a tree service, because the work is dangerous and expensive and a stranger is deciding whether to trust your crew with a saw over their house. A steady wall of recent, honest reviews, next to a profile that shows you are licensed and insured, does more to win a nervous homeowner than any slogan. Getting the profile verified and complete, keeping it active, and building a steady flow of real reviews is the single biggest lever on new calls. What no one can honestly promise is a specific spot on the map, because Google decides that.</p>'},
        {"h2_html": "Be ready before the season, and mine the customers you <em>already have</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The other thing about tree work is that demand is seasonal and weather-driven. It spikes after storms and in the pruning seasons and goes quiet in between, so the crews that win the spike are the ones already visible when it arrives, not the ones starting to market the week the wind picks up.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep your profile and site active year round so you already rank when the storm hits, instead of climbing from cold that week.</li><li>Ask every happy customer for an honest review right after the job, so the trust is built before the next searcher needs it.</li><li>Stay in front of past customers with seasonal reminders, so the yards you already know call you first for the next trim or removal.</li><li>Send every new storm call into one list, so a one-time cleanup can become a customer for the life of the yard.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Getting more customers is not one trick. It is being findable, being trusted, and never letting the work you already earned go cold. Marketing brings the new calls in and the follow-up keeps them, which is why the two work best together. A free audit can show where your profile, reviews, and follow-up stand today.</p>'}],
    "bridge_h2": "Be the crew they find and trust first",
    "bridge_text": "Most tree work goes to whoever is visible and trusted when a homeowner needs a tree handled. Marketing keeps your profile ranking, your reviews building, and your name in front of past customers before the season hits.",
    "bridge_slug": "marketing-for-tree-services",
    "bridge_label": "Marketing for tree services",
    "faqs": [
        ("What is the fastest way for a tree service to get more calls?",
         "Usually the local map results, which run on your Google Business Profile, not a new website. Getting it verified, complete, and active, and building a steady flow of honest reviews, is what moves you into the three listings most homeowners call from. Nobody controls Google, so no honest company promises a specific position."),
        ("Do reviews really matter that much for a tree service?",
         "More than for most trades. The work is dangerous and expensive, so a nervous homeowner leans hard on what other people say before letting a crew put a saw in a tree over their house. A steady stream of recent, genuine reviews, next to proof you are licensed and insured, is one of the strongest things you can build.")],
    "trade_slug": "tree_services", "trade_plural": "tree services",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
