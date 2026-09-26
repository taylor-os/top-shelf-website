"""Colony page specs for FLOORING COMPANIES (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a flooring-business owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, flooring-specific substance (the generator owns shell,
schema, events, keyword placement). Same honesty rules as the money specs: no invented stats,
prices, or clients; hedge instead of overpromise; only the real prices ($299/$899 plans, $1,500
one-time site) ever appear, and never an invented flooring or per-square-foot price; no em/en
dashes anywhere; "find the gap"/"goes cold", never "leak" as a metaphor. The AI receptionist does
scheduling and intake only, it never guesses a price or binds a quote, the owner still sets it.

Flooring is a visual, considered purchase: a homeowner choosing hardwood, luxury vinyl plank, tile,
or carpet wants to see samples and finished rooms, then get an in-home measure and quote, so the
business blends a showroom with in-home estimates. Buyers shop a few flooring companies and go with
the one that responds and books the measure, while the installer or estimator is on a job laying
floor and misses the call. So the substance leans on capturing every call while the crew is on the
floor, following up the still-choosing quotes over the weeks a homeowner compares samples, and
reactivating past customers for the next room, plus the product and project galleries that sell
floors. A flooring specialty, distinct from general contractors (whole remodels) and from fence.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 flooring-company-website-cost                (cost)    -> websites-seo-for-flooring-companies
  2 flooring-answering-service-cost              (cost)    -> ai-receptionist-for-flooring-companies
  3 is-a-crm-worth-it-for-a-flooring-company     (cost)    -> crm-for-flooring-companies
  4 why-flooring-companies-miss-calls            (problem) -> ai-receptionist-for-flooring-companies
  5 why-flooring-estimates-go-cold               (problem) -> crm-for-flooring-companies
  6 how-do-flooring-companies-get-more-customers (how-to)  -> marketing-for-flooring-companies
"""

TOPICS = [
# ============ How Much Does a Flooring Company Website Cost? (cost -> websites-seo) ============
{
    "slug": "flooring-company-website-cost",
    "h1": "How Much Does a Flooring Company Website Cost?",
    "title": "How Much Does a Flooring Company Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A flooring company website ranges from a cheap template to several thousand for a custom build. Top Shelf builds one that shows your floors and books the measure for $1,500 one-time, or free on any monthly plan.",
    "answer": "A flooring company website can run from a couple hundred dollars for a do-it-yourself template to several thousand for a custom build. What matters more than the price is whether it shows your finished floors, ranks locally, and books the in-home measure. Top Shelf builds one for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a flooring website actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before you compare quotes, it helps to know what a flooring website is actually for, because it is a different job from most trades. Homeowners buy floors with their eyes. Before anyone picks up the phone they want to see the species and stain of the hardwood, the look of the luxury vinyl plank, the tile pattern, the color and pile of the carpet, in real finished rooms, and they quietly rule out any company whose work they cannot see. So the site is doing the same job as your showroom, only it is open at eleven at night when a homeowner finally sits down to plan the room they cannot stand anymore.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Product and project galleries, organized by material and room, so a homeowner can find a space like theirs done well.</li><li>A clear sense of the materials you carry, honest reviews, and your service area stated plainly.</li><li>It has to load fast and look right on a phone, because that late-night browsing is where floors get shortlisted.</li><li>It has to rank for the searches homeowners actually make, flooring store near me, flooring installation near me, hardwood floor installation, luxury vinyl plank in your town.</li><li>And it has to make requesting an in-home measure or booking a showroom visit effortless, not buried three clicks deep.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A cheap template you fill in yourself rarely does any of that well, so the real question is not the sticker price, it is whether the site does the flooring job at all.</p>'},
        {"h2_html": "What drives the price, and what to <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Once you know the job, the reason quotes swing so widely makes sense: you are not all buying the same thing. A do-it-yourself builder is cheap monthly, but you do the work and it is seldom built to rank or to show floors well. A one-time custom build costs more up front and is yours to keep, though a site alone does little if nobody is doing the ongoing SEO to get it found. An agency plan bundles the build with the ongoing work, which is where most of the long-term value lives, and also where the monthly cost lives. Before you sign anything, ask who owns the site, what a change costs, and whether you keep it if you leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site that shows your floors and books the measure is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that shows your floors and books the measure",
    "bridge_text": "A flooring website earns its keep by showing your finished floors and turning a late-night browse into a booked in-home measure. Ours ranks for the towns and materials homeowners search, then hands every inquiry to the system that follows up.",
    "bridge_slug": "websites-seo-for-flooring-companies",
    "bridge_label": "Websites & SEO for flooring companies",
    "faqs": [
        ("Is a cheap template site good enough for a flooring company?",
         "It can get you online, but for flooring the site has to show finished floors in real rooms and make booking a measure easy, and a template you fill in yourself rarely ranks or displays a gallery well. If it is not getting found or turning browsers into booked measures, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep. On a monthly plan the site is built for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "flooring_companies", "trade_plural": "flooring companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======= What Does a Flooring Answering Service Cost? (cost -> ai-receptionist) =======
{
    "slug": "flooring-answering-service-cost",
    "h1": "What Does a Flooring Answering Service Cost?",
    "title": "What Does a Flooring Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for flooring companies often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers every call and books the measure in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for flooring companies usually bill per call, per minute, or a monthly retainer, so a busy stretch gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call, captures the rooms and material, and books the in-home measure comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good stretch turns into a big bill. A flooring company also gets a lot of its calls at the worst times for a live service to be cheap: evenings and weekends, when homeowners finally sit down to research floors after staring at a room they cannot stand. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of price-shoppers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a homeowner talking through hardwood versus vinyl costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner planning new floors is calling a few companies and going with the one that responds, sounds like a real flooring company, and books the measure soon. The real cost of no coverage is not a monthly fee, it is the whole room or whole floor that went to the shop that picked up. But a generic call center reading a script cannot tell engineered hardwood from a floating vinyl install, or which caller wants a whole-house quote and which just wants a price on a set of stairs, so you can pay for coverage and still get a lead that is barely qualified.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, asks which rooms they want done and what material they are leaning toward, gets the address, and books the in-home measure on your calendar or hands you a qualified lead. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. It does the scheduling and intake only, it does not guess at a price or commit you to a quote, so you still walk the job and set the number. One whole-house floor you would have lost while your hands were full is often worth well more than the plan costs, and everything it captures after that is on top.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers every call, asks which rooms and what material, and books the measure, all on a flat monthly plan while your crew stays on the floor.",
    "bridge_slug": "ai-receptionist-for-flooring-companies",
    "bridge_label": "AI receptionist for flooring companies",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when homeowners are shopping for floors at night and on weekends, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the whole-house measure it books instead of losing to voicemail."),
        ("Does it set the price or quote the job?",
         "No. It handles the scheduling and intake only, which rooms, roughly how much square footage, what material they are considering, then books the in-home measure or hands you the lead. You still walk the job and set the quote. It never guesses a price or commits you to one.")],
    "trade_slug": "flooring_companies", "trade_plural": "flooring companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ========= Is a CRM Worth It for a Flooring Company? (cost -> crm) =========
{
    "slug": "is-a-crm-worth-it-for-a-flooring-company",
    "h1": "Is a CRM Worth It for a Flooring Company?",
    "title": "Is a CRM Worth It for a Flooring Company? | Top Shelf Business Solutions",
    "meta_desc": "For most flooring companies a CRM pays for itself by rescuing one still-choosing quote and reviving past customers for the next room. It comes in Top Shelf's Signature plan at $899/mo, not a separate bill.",
    "answer": "For most flooring companies, yes. A CRM pays for itself the first time it wins back a quote a homeowner was still deciding on, or brings a past customer back for the next room. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a flooring company when you have more open quotes and past customers than you can personally keep track of, which is most established shops. It is not worth it if you are a one-person operation doing a couple of jobs and genuinely calling everyone back, though that rarely stays true as you grow. The honest test is simple: how many homes have you measured and quoted in the last month that went quiet while the homeowner compared samples, and how many past customers whose living room you floored have not heard from you since? A decision about floors a homeowner will walk on every day takes weeks, and a lot of those maybes are still winnable. Those are the jobs a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a flooring company is not the software, it is the work that stops slipping through the gap between the measure and the deposit. A homeowner sitting on a hardwood quote while they take sample boards home, a family whose living room you did last year and is ready for the bedrooms, the neighbor who admired the floor: each one is a job you have already half-earned and are one timely touch away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open quote across the deciding window, so a homeowner comparing samples and companies keeps hearing from you while the others go quiet.</li><li>It brings past customers back for the next room, the stairs, the basement, and asks for the review and the referral while the floor is still new.</li><li>It keeps every lead, measure, and note in one place instead of a truck console full of scribbled measurements and whatever you can remember.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one whole-house floor you would have let go cold and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your measures and past customers to work",
    "bridge_text": "The quotes you already measured and the homes you already floored are the cheapest jobs you can get. A CRM follows up on every one over the weeks a homeowner chooses, so they book you next instead of the company that stayed in touch.",
    "bridge_slug": "crm-for-flooring-companies",
    "bridge_label": "CRM for flooring companies",
    "faqs": [
        ("Is a CRM overkill for a small flooring company?",
         "Not usually. Even a one or two crew shop measures more homes and floors more rooms than anyone can track by memory. The point is not size, it is whether follow-up is falling through the gap between the measure and the deposit. If quotes go cold while homeowners compare samples and past customers forget your name, a CRM earns its keep."),
        ("How is a CRM different from keeping numbers in my phone?",
         "A phone full of contacts does not follow up on a quote, does not remember who is due for the next room, and does not tell you which measure is going cold. A CRM does all of that on a schedule, so the rooms you already quoted and the ones you have not done yet actually turn into jobs.")],
    "trade_slug": "flooring_companies", "trade_plural": "flooring companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== Why Do Flooring Companies Miss So Many Calls? (problem -> ai-receptionist) ========
{
    "slug": "why-flooring-companies-miss-calls",
    "h1": "Why Do Flooring Companies Miss So Many Calls?",
    "title": "Why Do Flooring Companies Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Flooring companies miss calls because they ring while the crew is on its knees laying floor, and a homeowner shopping for floors does not leave a voicemail, they call the next company.",
    "answer": "You miss calls because they come while your crew is on its knees laying floor, loading the trailer, or walking a job, and a homeowner shopping for new floors does not leave a voicemail. They call the next company on their list. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes while your crew is <em>on the floor</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Flooring is a hands-full, on-site trade. When the phone rings your estimator is on his knees with a trowel, your installer is mid-room with a nailer, you are loading material or walking a job with a customer, and none of those are moments you can stop and take a call. The busier you are, the more calls you miss, which means your best weeks are also the ones where the most work slips away. It is not a discipline problem. A crew cannot lay the floor in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A lot of flooring calls also come in the evenings and weekends, when homeowners finally sit down to research floors, and voicemail is no safety net for them. A homeowner working down a list of three flooring companies is not going to leave a message and wait. They move to the next name, and by the time you check your phone the measure is already booked with someone else.</p>'},
        {"h2_html": "A missed call is a whole room handed to <em>whoever picked up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A missed flooring call is not a small service trickle, it is a room or a whole floor. The homeowner is choosing both a product they will look at every day and the crew that will tear out the old floor and work in their house for a few days, so the company that answers, sounds real, and can get out to measure soon is the one they quietly size up as the safe choice. Miss the call and you are not passing on a quick visit, you are handing a large ticket to whoever answered faster, and a homeowner who cannot reach you does not assume you are busy with good work, they assume you are hard to pin down.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can tell a whole-house inquiry from a price on a set of stairs. A voicemail box cannot ask a single question, and a generic call center does not know hardwood from vinyl. What actually works is something that answers on the first ring, asks which rooms and what material, gets the address, and books the in-home measure or hands you a qualified lead. It does the scheduling and intake only, so you still set the quote when you walk the job, but the call never rolls to voicemail in the first place.</p>'}],
    "bridge_h2": "Stop losing floors to voicemail",
    "bridge_text": "An AI receptionist answers every call the moment it rings, even with your whole crew on the floor, asks which rooms and what material, and books the measure or hands you the lead, so the job never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-flooring-companies",
    "bridge_label": "AI receptionist for flooring companies",
    "faqs": [
        ("Would a homeowner rather reach a real person?",
         "When they are about to pick out floors and let a crew into their home, what a homeowner wants most is to know a real, organized company is handling it, and a calm voice that takes down the rooms and the material beats a voicemail box every time. The receptionist is upfront about what it is, captures the details, and books the measure for you to quote."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are on your knees laying floor, loading the trailer, or already with a customer. Something that always answers and captures the rooms and material is what catches the calls a forward would still miss.")],
    "trade_slug": "flooring_companies", "trade_plural": "flooring companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do My Flooring Estimates Go Cold? (problem -> crm) ============
{
    "slug": "why-flooring-estimates-go-cold",
    "h1": "Why Do My Flooring Estimates Go Cold?",
    "title": "Why Do My Flooring Estimates Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most flooring estimates go cold not over price but because nobody followed up while the homeowner was still choosing samples. The job went to whoever stayed in touch.",
    "answer": "Most flooring estimates go cold not because your price was wrong, but because nobody followed up while the homeowner was still choosing. They took samples home, gathered another price, and talked it over for weeks, and the job went to whoever stayed in touch. A quiet quote is usually a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "Choosing a floor takes weeks, and silence <em>loses the job</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet quote as a no on price, so you drop it and move on. But most of the time the homeowner did not decide against you at all. A decision about floors they will walk on every day rarely lands in an afternoon. After you measure and quote hardwood or luxury vinyl across a few rooms, they take sample boards home to see them in their own light, price a company or two more, and go back and forth with a spouse on style and budget. That deciding window is where estimates drift, not to a better price but to silence.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The company that wins is usually not the cheapest. It is the one who stayed in front of them through the choosing: a friendly check-in a few days after the measure, a short note answering the material-versus-material question they were stuck on, a nudge as the date they wanted it done by gets close. That steady, helpful presence is what turns a maybe into a booked job, and it is exactly the thing there is no time for when the crew is on the floor.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Flooring companies do not skip follow-up because they are lazy. They skip it because the crew is on the floor. You finish a room, load out, handle the next install, and by evening the quote you measured on Tuesday is out of sight. Doing it by memory means it only happens when work is slow, which is exactly when you have the fewest open quotes to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which measures are still open and going cold.</li><li>The follow-up depends on you remembering, so it competes with the actual install and loses.</li><li>By the time you circle back, the homeowner has already booked whoever checked in at the right moment.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open quote gets a few timed check-ins automatically, written to sound like you and spread across the weeks a homeowner compares samples, the family still deciding keeps hearing from you while the others go silent, and the floors you already measured stop slipping away.</p>'}],
    "bridge_h2": "Follow up on every measure, automatically",
    "bridge_text": "A CRM keeps every open quote in front of you and sends timed check-ins for you across the weeks a homeowner chooses, so the family comparing samples keeps hearing from you while the other flooring companies go quiet.",
    "bridge_slug": "crm-for-flooring-companies",
    "bridge_label": "CRM for flooring companies",
    "faqs": [
        ("How many times should I follow up on a flooring quote?",
         "A few light touches across the deciding window catches most of the maybes without being pushy: a check-in after the measure, a note answering the material-versus-material question, a nudge as their target date nears. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and paced sensibly. A short, friendly check-in while someone is comparing samples reads as helpful, not pushy, and most homeowners appreciate the nudge because they meant to get back to you and forgot. You can always jump in and message anyone directly.")],
    "trade_slug": "flooring_companies", "trade_plural": "flooring companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======= How Do Flooring Companies Get More Customers? (how-to -> marketing) =======
{
    "slug": "how-do-flooring-companies-get-more-customers",
    "h1": "How Do Flooring Companies Get More Customers?",
    "title": "How Do Flooring Companies Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Flooring companies get more customers by showing finished floors where homeowners shop with their eyes, an active Google profile, galleries, and reviews, then following up on every measure and past customer.",
    "answer": "Flooring companies get more customers by showing their finished floors where homeowners shop with their eyes, your Google Business Profile, galleries of real rooms you have installed, and honest reviews, then following up on every measure and past customer. Homeowners buy floors visually, so being the local company whose work they can already see is what earns the call.",
    "sections": [
        {"h2_html": "Homeowners shop for floors <em>with their eyes</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">New flooring is one of the most visible things a homeowner will change about their house, something they walk on and look at every single day, so before they ever call they want to see it: the species and stain of the hardwood, the look of the luxury vinyl plank, the tile pattern, the color and pile of the carpet. They browse photos, picture it in their own rooms, and quietly rule out any company whose work they cannot see. So getting more flooring customers is not about clever slogans, it is about putting real, finished floors in front of people who are trying to imagine new ones, in the exact spots they look.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Get that right and you are on the short list before the first call, because a homeowner has already seen a room like theirs done well by you. Get it wrong, a stale profile, no photos of finished work, a handful of old reviews, and you are quietly crossed off a list you never knew you were on. The floors you lay are beautiful. Marketing is how a homeowner sees that before they decide who to invite out to measure.</p>'},
        {"h2_html": "Where the customers actually <em>come from</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A handful of channels, done consistently, is what fills the calendar, and none of them require a gimmick. When someone searches for flooring near them, the map pack, those local listings with the star ratings, is the first thing they see. A profile that is active and full of real before and after photos of finished living rooms, kitchens, and stairs looks like exactly the company a homeowner picturing new floors is hoping to find, while a quiet one with a thin trickle of reviews looks slow or gone.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Focus on the towns and materials you actually install, flooring store near me, hardwood floor installation, luxury vinyl plank, carpet installer, tile flooring in your own town, rather than a whole metro.</li><li>Turn every finished floor into photos and honest reviews, which are both the proof a careful buyer wants and a signal that lifts you in local search.</li><li>Stay in front of the customers you already have, because a finished floor advertises itself when guests and neighbors walk across it and ask who did it, so the next room and the referral come back to you.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">No honest company can promise a specific spot on Google, because Google decides that, but keeping the profile verified and active, the galleries current, and the reviews genuine is what moves it, and it compounds over time. A free audit can show you what your presence looks like to a homeowner shopping for floors today.</p>'}],
    "bridge_h2": "Be the flooring company they can already see",
    "bridge_text": "Most flooring jobs start with a homeowner shopping visually. Keeping your Google profile active, your galleries full of finished floors, and your reviews genuine is how you show up as the trusted local name when someone nearby starts looking.",
    "bridge_slug": "marketing-for-flooring-companies",
    "bridge_label": "Marketing for flooring companies",
    "faqs": [
        ("What is the fastest way for a flooring company to get more customers?",
         "Usually the quickest win is the Google Business Profile: getting it verified, complete, and stocked with real photos of finished floors and genuine reviews, because that is what a homeowner sees first when they search for flooring near them. It compounds as photos and reviews build. Nobody controls Google, so no honest company promises a specific position."),
        ("Do photos of my finished floors really bring in customers?",
         "For flooring, yes. New floors are a visual, everyday purchase, and a homeowner wants to see a room like theirs done well before they invite anyone out to measure. Real before and after photos of your work are often what turn a searcher into a booked measure, and they feed the same profile that lifts you in local search.")],
    "trade_slug": "flooring_companies", "trade_plural": "flooring companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
