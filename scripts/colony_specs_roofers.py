"""Colony page specs for Roofers (plan section 5 colony template + section 6 link-sculpting).
generate_colony.py loads TOPICS from every scripts/colony_specs_*.py and owns the mechanics
(shell, hero, bridge block, FAQ, FAQPage + BreadcrumbList schema, GA4 events). Each dict owns
one UNIQUE, hand-written question and a direct answer that clears the uniqueness gate.

Ten genuinely-searched roofing-owner questions, a mix of problem/symptom, how-to, and cost,
each answered plainly then funneled to the single money page that solves it. Home Services hub,
trade_slug "roofers". Bridge targets are the seven existing roofer money pages, spread across
the ten so every service gets colony support and the high-intent ones (AI receptionist, CRM,
online booking) get two feeders each.
"""

TOPICS = [
# ==================== 1. Storm call surge -> AI receptionist ====================
{
    "slug": "why-i-miss-storm-calls",
    "h1": "Why Do I Miss Calls After a Storm?",
    "title": "Why Do I Miss Calls After a Storm? | Top Shelf Business Solutions",
    "meta_desc": "You miss storm calls because a surge of homeowners dials every roofer at once while your crews are on roofs and one phone cannot keep up.",
    "answer": "Because a storm sends a whole town looking for a roofer in the same two days, and the calls arrive while your crews are already on roofs and your estimators are booked. One phone and one person cannot answer a surge, so the overflow rolls to voicemail, and most of those homeowners simply dial the next roofer.",
    "sections": [
        {"h2_html": "The first roofer to answer usually <em>signs the roof</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Roofing runs on speed, and never more than in the days after hail or high wind. A homeowner with a damaged roof does not call one roofer, they call three, and they hire whoever picks up and gets someone out to look. So the calls that decide your week are the ones coming in right now, while your crews are already on roofs and your estimators are mid-inspection.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A single phone answered by a single person cannot keep up with that. The second and third caller hit voicemail, and a homeowner staring at water damage does not leave a message and wait, they dial the next company on the list. The lead was never lost to a better roofer. It was lost to whoever happened to answer while you were forty feet up on someone else's roof.</p>'''},
        {"h2_html": "A voicemail box cannot <em>triage a surge</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your phones do not ring at a steady pace. They are quiet for weeks, then a storm rolls through and you get a season of calls in two days, most of them after hours, most from people who will hire the first roofer to show up. A voicemail box cannot sort that, and a generic call center does not know an insurance claim from a cash repair. What actually closes the gap is something that answers every call at once and knows what to ask.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers on the first ring, day or night, including the midnight-after-the-storm call and the Sunday inquiry off your yard sign.</li><li>Takes a whole surge at once, so a rush of callers all get answered instead of stacking up in voicemail.</li><li>Asks what you would ask: storm damage or normal wear, is the roof actively leaking, insurance claim or paying out of pocket, roof age, and the address.</li><li>Books the free inspection on your real calendar and texts you the lead on the spot.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">You do not need to recover many calls for that to matter. A roof replacement is a big-ticket job, so one homeowner you would have lost to voicemail is worth far more than the cost of never missing them again.</p>'''}],
    "bridge_h2": "An AI receptionist catches the calls you <em>cannot get to</em>",
    "bridge_text": "An AI receptionist answers on the first ring, day or night, qualifies the homeowner, finds out whether the roof is actively leaking or storm damaged, and books a free inspection on your calendar, all while your crews stay on the roof. The surge gets answered instead of stacking up in voicemail, and every lead is yours.",
    "bridge_slug": "ai-receptionist-for-roofers",
    "bridge_label": "See the AI receptionist for roofers",
    "faqs": [
        ("Can it really handle a flood of calls at once?",
         "Yes. That is what it is built for. It answers every call at the same time, so a storm that would send a dozen homeowners to voicemail instead gets a dozen inspections booked. It does not put people on hold or clock out at 5 p.m."),
        ("Do I keep my own phone number?",
         "Yes. It answers on your existing number, or a new one registered in your name, and every caller and lead is yours and exportable any time. You are never handing your number or your leads to us.")],
    "trade_slug": "roofers", "trade_plural": "roofers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==================== 2. Estimates go cold -> CRM ====================
{
    "slug": "why-roofing-estimates-go-cold",
    "h1": "Why Do My Roofing Estimates Go Cold?",
    "title": "Why Do My Roofing Estimates Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Roofing estimates go cold because a roof is a slow decision and most bids never get a second touch. Here is how to follow up on every one.",
    "answer": "Because a roof is a big decision homeowners sit on for weeks, and most bids never get a second touch. You inspect, hand over a price, they say they need to think or wait on insurance, and nobody follows up. They sign with whoever stayed in front of them, not the roofer who bid first.",
    "sections": [
        {"h2_html": "Most roofers have a follow-up problem, not a <em>lead problem</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You inspect a roof, hand over a bid, and the homeowner says they need to think about it, talk to a spouse, or wait on the insurance check. That is normal in roofing, where a replacement is a big decision people sit on for weeks. The trouble is what happens next: most bids never get a second touch, because the person who should follow up is on a ladder, and by the time anyone circles back the homeowner has already signed with the roofer who stayed in front of them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That roofer is rarely the one who inspected first or bid lowest. It is the one whose name kept showing up while the homeowner was deciding. The bid going cold is not a pricing problem or a quality problem. It is a follow-up problem, and it is the cheapest kind to fix, because you already did the hard part when you climbed the roof and wrote the estimate.</p>'''},
        {"h2_html": "The bids waiting on insurance are the ones you <em>lose</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">After a storm you can take more leads in a week than you normally see in a month, and no estimator can remember to circle back to all of them. The ones waiting on an adjuster, the ones getting a second opinion, the ones who called scared and then calmed down, all of them slip unless something keeps track. A claim can take weeks to clear, which is exactly long enough for a homeowner to forget who looked at their roof.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every lead, inspection, note, and bid lives in one place instead of a truck console and three phones.</li><li>Follow-ups fire on the cadence you set, so a homeowner waiting on a claim gets a check-in at the right time without anyone setting a reminder.</li><li>You see which bids are heating up, so your estimator's limited callback time goes to the roof about to sign.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The point is simple: the roof you already inspected should not go to a competitor just because the check came through on a day you were too busy to call.</p>'''}],
    "bridge_h2": "A CRM follows up on every bid <em>so you do not have to</em>",
    "bridge_text": "A CRM keeps every inspection and open bid in one place and works it on the schedule you set, with texts and emails that go out on time whether or not anyone remembers. The homeowner still deciding weeks later keeps hearing from you, so the bid comes back to you instead of the roofer who followed up last.",
    "bridge_slug": "crm-for-roofers",
    "bridge_label": "See the CRM for roofers",
    "faqs": [
        ("Does it follow up on estimates on its own?",
         "Yes, on a schedule you approve. New leads get an instant reply, and open bids get check-ins on the cadence you set, all sent for you. Your estimators can still jump in and message a homeowner directly when a bid needs a personal push."),
        ("What about bids waiting on an insurance decision?",
         "Those get a longer, gentler cadence, because a claim can take weeks. The homeowner still waiting on an adjuster keeps hearing from you at the right intervals, so you are the roofer they call when the check comes, not whoever reached out most recently.")],
    "trade_slug": "roofers", "trade_plural": "roofers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==================== 3. Website cost -> Websites & SEO ====================
{
    "slug": "roofing-website-cost",
    "h1": "How Much Does a Roofing Website Cost?",
    "title": "How Much Does a Roofing Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A custom roofing website is $1,500 one-time, or built and included free on any Top Shelf plan starting at $299. Here is what drives the cost.",
    "answer": "It depends on whether you buy a site outright or get it as part of a plan. A custom roofing website on its own is $1,500 one-time with Top Shelf, yours to keep. On any monthly plan, starting at $299, the website is built and included free, so the site itself costs nothing up front.",
    "sections": [
        {"h2_html": "What actually drives the price of a <em>roofing website</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A roofing website can cost almost nothing or several thousand dollars, and the range is real, so the honest answer starts with what you are actually buying. A template you fill in yourself is cheap and usually looks it. A custom site built to rank in local search, load fast, and turn a worried homeowner into a booked inspection takes real work, and that is what you are paying for when the number goes up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The things that move the price are the number of pages, whether it is written to rank for the towns and roof types you actually work, whether it captures leads into a system that follows up, and who maintains it after launch. A brochure that just sits there is the cheapest to build and the most expensive to own, because it never books a job. A site that ranks and captures leads costs more up front and pays for itself the first storm it catches.</p>'''},
        {"h2_html": "Cheap, free, and included are <em>not the same thing</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">With Top Shelf there are two honest paths. You can buy a custom five-page site outright for $1,500 one-time, and it is yours to keep, with no plan and no monthly. Or you get the website built and included free on a monthly plan that starts at $299, which also handles your Google Business Profile, online booking, and automated review requests. There is no setup fee either way.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The distinction matters, because included free does not mean the plan is free. On a plan you are paying for the whole system that keeps the site working, the ranking, the booking, and the follow-up, and the website simply comes with it instead of as a separate bill. Buying the site outright makes sense if you only want a page you own. Getting it on a plan makes sense if you want the site to actually bring in inspections. Either way the site, the domain, and the content are in your name.</p>'''}],
    "bridge_h2": "A roofing website should <em>pay for itself</em>",
    "bridge_text": "The real question is not the sticker price, it is whether the site ranks for the searches homeowners actually type and turns them into booked inspections. A brochure that never ranks is expensive at any price. See how a roofing site built for SEO captures the leads a storm sends searching, instead of handing them to a directory.",
    "bridge_slug": "websites-seo-for-roofers",
    "bridge_label": "See websites and SEO for roofers",
    "faqs": [
        ("Is the website really free on a plan?",
         "The website is built and included at no extra charge on every monthly plan, with no setup fee. You are paying for the plan, which also handles your Google profile, booking, and review requests. If you would rather just buy a site with no plan, that is $1,500 one-time, yours to keep."),
        ("Do I own the website either way?",
         "Yes. Whether you buy it on its own or get it on a plan, the site, the domain, and the content are in your name and yours to keep. Nothing about your website or your customer list is held hostage to keep you paying.")],
    "trade_slug": "roofers", "trade_plural": "roofers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==================== 4. More reviews -> Review software ====================
{
    "slug": "how-to-get-roofing-reviews",
    "h1": "How Do I Get More Roofing Reviews?",
    "title": "How Do I Get More Roofing Reviews? | Top Shelf Business Solutions",
    "meta_desc": "Get more roofing reviews by asking every happy homeowner the moment the job wraps, with a one-tap link to your Google profile. Here is how.",
    "answer": "Ask every satisfied homeowner at the moment they are happiest, the afternoon the job wraps and they are looking up at a roof that no longer leaks, and make leaving one a single tap straight to your Google profile. The reviews you are missing are not from unhappy customers, they are from happy ones who simply forgot.",
    "sections": [
        {"h2_html": "Homeowners read your reviews before they <em>hand you a big check</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before a homeowner hands a roofer thousands of dollars, they Google you and read what your past customers said. A roof is not a purchase people take lightly, and there are enough storm-chasing outfits and fly-by-night crews out there that homeowners are wary by default. A thin profile with a handful of old reviews quietly costs you jobs you never hear about, because the homeowner just called the roofer with the wall of recent five-star reviews instead.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The problem is not that your customers are unhappy. It is that happy customers forget to post, and asking feels awkward when you are wrapping up a job and already thinking about the next roof. So the reputation you have actually earned up on real roofs never makes it online, where the next homeowner is deciding who to trust. Fixing that is mostly about timing and making it easy, not about doing better work than you already do.</p>'''},
        {"h2_html": "Ask at the right moment, and <em>respond to every one</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The best time to ask is the afternoon the job is finished and the homeowner is standing in the driveway looking at a roof that no longer leaks. That is when review software sends the ask for you, by text and email, with a link that drops them straight onto your Google profile in one tap. No cornering people, no business cards nobody acts on, and no asking three weeks later when the relief has worn off.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The other half is responding. A thoughtful reply to each review tells the next homeowner you stand behind your work, and it is one of the signals that helps you show up in local search. Good reviews get a thank you, and a rare critical one, the storm job that ran long or the mix-up on a start date, gets a calm, professional response instead of silence. Do both consistently and your profile compounds: more reviews lift you in local results, which brings more jobs, which bring more reviews.</p>'''}],
    "bridge_h2": "Review software asks every homeowner, <em>automatically</em>",
    "bridge_text": "You do not have to remember to ask, or feel awkward doing it. Review software sends the request the moment a job is marked complete, by text and email, with a one-tap link to your Google profile, and flags every new review so you can reply fast. See how it turns finished roofs into the reputation that wins the next one.",
    "bridge_slug": "review-software-for-roofers",
    "bridge_label": "See review software for roofers",
    "faqs": [
        ("Is it against the rules to automate review requests?",
         "No. Asking every customer for an honest review is fine and encouraged. What is not allowed is filtering out unhappy customers or paying for reviews, and this does neither. It simply asks everyone at the right moment and makes saying yes easy."),
        ("What happens when I get a bad review?",
         "You find out right away instead of weeks later, and you get help posting a calm, professional reply. One thoughtful response sitting under a wall of genuine positive reviews often reassures a wary homeowner more than a spotless record would.")],
    "trade_slug": "roofers", "trade_plural": "roofers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==================== 5. Book more free inspections -> Online booking ====================
{
    "slug": "book-more-free-roof-inspections",
    "h1": "How Do I Book More Free Roof Inspections?",
    "title": "How Do I Book More Free Roof Inspections? | Top Shelf Business Solutions",
    "meta_desc": "Book more free roof inspections by letting homeowners self-schedule on your real availability from your site, ads, and Google profile. Here is how.",
    "answer": "Stop making worried homeowners wait for a callback. Put a booking link on your website, your Google profile, and your storm-season ads so they can grab an open inspection slot the moment they feel it, day or night. The form qualifies the roof first, so your estimator's day fills with visits worth the drive.",
    "sections": [
        {"h2_html": "Phone tag is quietly costing you <em>inspections</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A homeowner notices a missing shingle or a water stain and wants someone to look at it. Your estimator is on a roof, so they call back two hours later, the homeowner is at work, they trade voicemails, a day passes, and the roof gets looked at by the company that could lock in a time on the spot. The inspection was never the problem. The back and forth was. When someone is worried enough about their roof to reach out, the worst thing you can do is make them wait for a callback.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A booking link removes the wait entirely. The homeowner grabs an open inspection slot the moment they feel it, day or night, without reaching anyone first, and your estimator wakes up to the visit already set instead of a missed call they now have to chase between jobs. Motivated homeowners book themselves the instant they can, which is exactly when you want to catch them.</p>'''},
        {"h2_html": "Let them book themselves, but <em>qualify the roof first</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Self-scheduling does not mean sending an estimator across town for nothing. The booking form asks what matters first: storm damage or normal wear, whether the roof is actively leaking, insurance claim or paying directly, the age of the roof, and the address. A clear storm-damage claim books an inspection, and a vague question gets routed to a quick call, so your estimator's day fills with roofs worth the drive. You set the rules: how many inspections a day, how long each takes, and how much drive time to leave between them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Then the link goes everywhere a homeowner already meets you: your website, your Google Business Profile, your storm-season ads, and the text you send after a missed call. Each one turns from a dead end that needs a callback into a place someone can book in one tap. After a storm, when everyone is calling every roofer at once, letting people book themselves is the difference between catching the surge and drowning in it, and the automatic reminder that follows is what keeps the slot.</p>'''}],
    "bridge_h2": "Online booking turns every page into an <em>inspection slot</em>",
    "bridge_text": "A booking link goes everywhere a homeowner meets you, your site, your Google profile, your ads, and the text after a missed call, and reads your real calendar so it never double-books an estimator. It qualifies the roof before it books and sends a reminder that cuts no-shows. See how it catches the surge instead of drowning in it.",
    "bridge_slug": "online-booking-for-roofers",
    "bridge_label": "See online booking for roofers",
    "faqs": [
        ("Will self-booking send my estimator out on junk leads?",
         "Not if the form is set up right. It asks about damage, leaks, roof age, and whether it is an insurance claim, so a real prospect books an inspection and a vague inquiry is routed to a quick call first. Your estimator's time goes to roofs worth the drive."),
        ("Does it cut down on no-shows for free inspections?",
         "It helps. Automatic confirmations and reminders by text and email are the biggest lever on no-shows, and every booking includes them. A homeowner who booked the time themselves and got a reminder is far more likely to be home.")],
    "trade_slug": "roofers", "trade_plural": "roofers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==================== 6. Leads without buying -> Marketing ====================
{
    "slug": "roofing-leads-without-buying-them",
    "h1": "How Do I Get Roofing Leads Without Buying Them?",
    "title": "How Do I Get Roofing Leads Without Buying Them? | Top Shelf Business Solutions",
    "meta_desc": "Get roofing leads without buying them by owning your Google profile, reviews, and local presence, so homeowners come to you, not a shared form.",
    "answer": "Own the channels the lead sellers rent back to you. A Google Business Profile you keep active, real reviews, and steady local presence in the towns you actually work make homeowners find and recognize you before a storm hits, so the call comes straight to you instead of a shared form sold to several roofers at once.",
    "sections": [
        {"h2_html": "The lead sellers are renting you back <em>your own homeowners</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The big directories and lead services outrank most individual roofer sites because they publish thousands of pages and have years of authority behind them. A homeowner searching for a roofer often lands on one of those first, fills out a form, and that single lead gets sold to several roofers who then race to call it and undercut each other. You are not really buying a customer, you are buying a shared contact and a bidding war.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It also stops the day you stop paying. Every dollar you hand a lead service disappears the moment the card declines, and the demand was never yours to begin with. That is the trap: you rent access to homeowners in your own town, at a price, forever, instead of owning a channel where the call comes straight to you. The way out is to build the presence the lead sellers are charging you to borrow.</p>'''},
        {"h2_html": "Become the roofer homeowners already know <em>before the storm</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a homeowner searches for a roofer after a storm, your Google Business Profile is often the first thing they see, before your website and before a directory. A profile that sits untouched for months looks abandoned next to one with recent job photos, before-and-after shots, and posts about the last storm you responded to. Keeping it active is a quiet, constant advertisement running in the exact moment a worried homeowner is looking.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Pair that with real reviews and steady visibility in the towns your crews actually work, and you build the specific recognition that turns into a call when a roof fails down the street. It is slower than buying leads, and that is the honest tradeoff, but it compounds and it is yours. The roofer who was invisible until the storm is bidding against everyone else at the most expensive moment. The one who stayed familiar all season just gets the call.</p>'''}],
    "bridge_h2": "Marketing makes you the name they <em>already know</em>",
    "bridge_text": "Buying leads is renting demand at the most expensive moment, against everyone else buying the same list. Marketing builds recognition you own: an active Google profile, local content, and visibility in the towns you work, so when a roof fails down the street, yours is the name the homeowner already trusts. See how it compounds instead of resetting every month.",
    "bridge_slug": "marketing-for-roofers",
    "bridge_label": "See marketing for roofers",
    "faqs": [
        ("Is this faster than just buying leads?",
         "No, and that is the honest tradeoff. Bought leads show up today; owned presence builds over months. The difference is that a purchased lead is sold to your competitors too and stops the day you stop paying, while recognition you build keeps working and is entirely yours."),
        ("Do you post to my Google Business Profile for me?",
         "Yes. We keep it active with job photos, before-and-after shots, and local posts on a regular schedule, so it looks current and established whenever a homeowner searches for a roofer near them.")],
    "trade_slug": "roofers", "trade_plural": "roofers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==================== 7. Automatic estimate follow-up -> Automation ====================
{
    "slug": "follow-up-roofing-estimates-automatically",
    "h1": "How Do I Follow Up on Roofing Estimates Automatically?",
    "title": "How Do I Follow Up on Roofing Estimates Automatically? | Top Shelf Business Solutions",
    "meta_desc": "Follow up on roofing estimates automatically with a text and email sequence that fires when you leave a bid and runs until the homeowner books.",
    "answer": "Set up a sequence that fires the moment you leave a bid: a same-day thank-you, an answer to the questions homeowners always ask, and a check-in while the decision is fresh, all sent by text and email until they book or say no. Bids waiting on insurance get a longer, gentler cadence so they never go quiet.",
    "sections": [
        {"h2_html": "The second touch wins the roof, and it is the one that <em>gets skipped</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The work that wins roofing jobs is not glamorous. It is the second text on a bid, the reminder the day before an inspection, the review ask the afternoon a roof is done. Each one is small, and each one gets skipped during a busy week because the person who should send it is up a ladder. After a storm, when the volume triples, the follow-through is the first thing to fall, and it is exactly the thing that turns inspections into signed roofs.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Doing it by hand does not scale. You cannot personally remember to send the right message to forty homeowners at the right moment while running crews, and even the disciplined estimator loses the thread when the phones surge. The steps are predictable, which is exactly why they should not depend on anyone remembering them. Miss the second touch on a storm-week bid and it is gone, not because your price was wrong but because silence let the homeowner drift to the roofer who kept in touch.</p>'''},
        {"h2_html": "A sequence that runs on every bid, <em>warm or waiting</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Once you leave an estimate, the homeowner gets a well-timed sequence: a same-day thank-you, an answer to the questions people always ask, and a check-in while the decision is fresh, all sent automatically until they book or clearly say no. The bids waiting on an insurance decision get a longer, gentler cadence, so a homeowner still deciding weeks later is still hearing from you instead of the roofer who happened to call last.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Estimate follow-ups fire after every inspection, on the schedule you approve.</li><li>Inspection reminders go out before the visit, so fewer homeowners forget and fewer slots are wasted.</li><li>A review request sends the moment a job is marked complete, while the homeowner is happiest.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It runs against the same CRM database, so it knows where each homeowner is and does not double-text someone who already booked. You still make every real call. Automation just makes sure the routine ones actually happen.</p>'''}],
    "bridge_h2": "Automation keeps every bid warm <em>without a reminder</em>",
    "bridge_text": "Automation sends the routine follow-ups, the thank-you, the claims answer, the well-timed check-in, on every bid and every job, whether you have one inspection this week or forty after a storm. You still make the calls that need a person. The predictable texts simply go out on time, so a bid never goes cold because someone was up a ladder.",
    "bridge_slug": "automation-for-roofers",
    "bridge_label": "See automation for roofers",
    "faqs": [
        ("Does this replace me actually calling homeowners?",
         "No. It handles the predictable texts and reminders so nobody has to remember them, and it frees your estimators for the calls that need a person, like walking a homeowner through a claim or closing a bid that is on the fence."),
        ("Will it double-text someone who already booked?",
         "No. It runs against the same CRM database, so it knows where each homeowner is in the process and will not send an estimate follow-up to someone who already signed or a review ask before the job is done.")],
    "trade_slug": "roofers", "trade_plural": "roofers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==================== 8. AI receptionist cost -> AI receptionist ====================
{
    "slug": "roofing-ai-receptionist-cost",
    "h1": "How Much Does an AI Receptionist Cost for a Roofing Company?",
    "title": "How Much Does an AI Receptionist Cost for a Roofing Company? | Top Shelf Business Solutions",
    "meta_desc": "The AI receptionist comes with Top Shelf's Signature plan at $899 a month, bundled with the CRM, website, and SEO. Here is what that covers.",
    "answer": "With Top Shelf the AI receptionist is part of the Signature plan at $899 a month, not a separate line item. That same plan also includes your CRM, website, and monthly SEO, so you are not paying a standalone answering-service fee, you are getting the phone answered as one piece of the whole platform, with no setup fee.",
    "sections": [
        {"h2_html": "Why it is priced as a platform, not an <em>answering service</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A phone bot that answers and then drops the lead into the same process that was already losing calls is not worth much. That is why Top Shelf does not sell the AI receptionist as a standalone answering service. It comes with the Signature plan at $899 a month, bundled with the CRM that follows up on every lead, online booking, a website, and monthly SEO, so the call it captures at 11 p.m. after a storm actually gets worked instead of sitting in a new kind of voicemail.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Compared with the alternative, the math is straightforward without inventing numbers. A full-time human receptionist costs far more than a plan, still clocks out at five, and cannot answer a dozen storm calls at once. The AI receptionist answers every call, day or night, and never calls in sick. You are paying for a system that catches the surge and then does something with it, not a person or a bot in isolation.</p>'''},
        {"h2_html": "What the $899 Signature plan actually <em>includes</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The Signature plan is one flat monthly rate with no setup fee, and the AI receptionist is one piece of it. The same $899 also includes the full Top Shelf CRM, a website built for you, advanced SEO every month, review responses written for you, customer reactivation, and lead follow-up in under five minutes. It is month to month, so you are not locked into a contract to keep it.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">If all you want right now is the basics, the Essentials plan is $299 a month and covers the website, Google profile, booking, and review requests, but the AI receptionist starts at Signature. The only cost on top of the plan is telecom usage, the phone numbers and text messages, billed at pass-through cost the same as everywhere in the industry. The honest way to know which plan fits is a free audit, which puts real numbers to how many calls you are missing today.</p>'''}],
    "bridge_h2": "See what the AI receptionist <em>actually does on a call</em>",
    "bridge_text": "Price makes sense once you hear it work. The AI receptionist answers on the first ring, day or night, finds out whether a roof is actively leaking or storm damaged, and books a free inspection on your calendar, then texts you the details. See exactly how it handles a live storm call before you decide whether the Signature plan is worth it.",
    "bridge_slug": "ai-receptionist-for-roofers",
    "bridge_label": "See the AI receptionist for roofers",
    "faqs": [
        ("Can I get just the AI receptionist without the rest?",
         "It comes as part of the Signature plan at $899 a month, bundled with the CRM, website, and monthly SEO, because a receptionist that books a lead is only worth it when something follows up on that lead too. There is no setup fee, and the plan is month to month."),
        ("Are there costs on top of the monthly plan?",
         "Only telecom usage, the phone numbers and text messages, billed at pass-through cost the same as everywhere in the industry. There are no hidden setup fees or surprise line items, and everything shows on a plain-English dashboard.")],
    "trade_slug": "roofers", "trade_plural": "roofers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==================== 9. Slow-season work -> CRM ====================
{
    "slug": "roofing-slow-season-work",
    "h1": "How Do I Keep My Roofing Crews Busy in the Slow Season?",
    "title": "How Do I Keep My Roofing Crews Busy in the Slow Season? | Top Shelf Business Solutions",
    "meta_desc": "Keep roofing crews busy in the slow season by working the database you already have, past customers and old bids a CRM reactivates on schedule.",
    "answer": "Work the database you already have. Between storms, the cheapest jobs come from past customers and old bids, homeowners due for a repair or a roof they put off replacing. A CRM keeps every one of them on a follow-up schedule, so a quiet stretch turns into reactivation calls instead of an empty calendar and idle crews.",
    "sections": [
        {"h2_html": "The slow season is a <em>follow-up problem</em>, too",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Roofing demand comes in waves. A storm sends a whole town looking for a roofer in the same week, and then the phones go quiet and the crews you staffed up for the surge have nothing booked. Most roofers treat that as just the season, but a lot of the slow-season work is already sitting in the business, in the homeowners you have worked for and the bids that never closed.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The roof you replaced a few years back is due for a look. The repair a homeowner deferred is still deferred. The bid that went cold in the spring might close now that the claim cleared. None of that calls you on its own, and nobody has time to work through a few hundred old contacts by memory. It is the same follow-up problem that loses storm bids, just showing up as an empty calendar instead of a lost lead.</p>'''},
        {"h2_html": "Turn a quiet calendar into <em>reactivation work</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Past customers and old bids are the cheapest roofs you will ever sell, because you already paid to earn them once. A CRM keeps every one in a database you own and works them on a schedule, so a slow stretch becomes outreach instead of idle time. You are not buying new leads, you are mining the ones you already have.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Maintenance reminders to past customers whose roofs are aging into repair or replacement.</li><li>Seasonal check-ins that give homeowners a reason to call before a small problem becomes a big one.</li><li>Revived bids, so an estimate that went cold gets a nudge once a claim is likely settled.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">You see who is warming up, so the calls your team does have time for go to the homeowners most likely to book. And the list stays yours and exportable, so the database you spend the busy season filling actually earns its keep when the storms are not coming.</p>'''}],
    "bridge_h2": "Your slow-season pipeline is already in <em>your database</em>",
    "bridge_text": "Past customers and old bids are the cheapest roofs you will ever sell, and they sit unused when the phones go quiet. A CRM keeps every one on a follow-up schedule and runs reactivation campaigns for you, so a slow stretch becomes maintenance visits, deferred replacements, and revived bids instead of idle crews. See how the database becomes your off-season pipeline.",
    "bridge_slug": "crm-for-roofers",
    "bridge_label": "See the CRM for roofers",
    "faqs": [
        ("What is a reactivation campaign?",
         "It is a scheduled set of check-ins to past customers and old leads, a maintenance reminder, a seasonal roof check, a nudge on a bid that went cold, all sent for you. It gives homeowners you already know a reason to call again during the months new leads are thin."),
        ("Do I keep my customer list?",
         "Yes. Every past customer, note, and old bid is in your name and exportable any time. The point is to make the list you already paid to build actually produce work, especially when the storm calls are not coming in.")],
    "trade_slug": "roofers", "trade_plural": "roofers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ==================== 10. Inspection no-shows -> Online booking ====================
{
    "slug": "roof-inspection-no-shows",
    "h1": "Why Do My Roof Inspection Appointments No-Show?",
    "title": "Why Do My Roof Inspection Appointments No-Show? | Top Shelf Business Solutions",
    "meta_desc": "Roof inspection appointments no-show because a free, loosely agreed visit is easy to forget. Automatic text and email reminders keep the slot.",
    "answer": "Usually because the inspection was free, loosely agreed on a phone call, and never confirmed, so the homeowner forgets or stops worrying once the panic fades. A free roof inspection with no reminder is the easiest thing on a homeowner's week to skip. Automatic confirmations and reminders by text and email are what actually keep the slot.",
    "sections": [
        {"h2_html": "A free inspection is the easiest thing to <em>forget</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A no-show is rarely about a bad homeowner. It is about low commitment. The inspection was free, agreed loosely on a phone call, and never confirmed, so it never quite became a real appointment in the homeowner's mind. Add in the way storm panic fades once the sky clears and the roof looks fine from the ground, and a free visit slides right off a busy week.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The cost lands on you twice. Your estimator drives across town for nothing, and the slot they held could have gone to another homeowner who would have been home. A day of no-shows is a day of windshield time and empty openings, which is expensive in a business where the estimator's hours are the constraint. Multiply a couple of those across a busy week and the no-shows quietly cap how many roofs your estimator can get eyes on. The fix is not scolding homeowners, it is lowering the odds they forget in the first place.</p>'''},
        {"h2_html": "Confirmations and reminders are the <em>biggest lever</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The single biggest thing that reduces no-shows is boringly simple: an automatic confirmation when the inspection is booked and a reminder before it happens, by text and email. A homeowner who picked the time themselves and then got a reminder is far more likely to be home than one who loosely agreed to a callback window. It turns a vague intention into an appointment they expect.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A booking system does that for every inspection automatically, and it reads your real calendar so it never double-books an estimator. When someone does cancel, the slot frees up instead of sitting empty, so your team can fill it. And because the booking form qualifies the roof up front, the never-serious inquiries get filtered to a quick call before they ever take a slot, so the inspections that do get booked are the ones worth the drive and the most likely to happen.</p>'''}],
    "bridge_h2": "Online booking sends the reminder <em>that keeps the slot</em>",
    "bridge_text": "Every booking made through the system comes with an automatic confirmation and reminder by text and email, which is the single biggest lever on no-shows. A homeowner who picked the time themselves and got a reminder is far more likely to be home when your estimator pulls up. See how self-booking fills the calendar with inspections that actually happen.",
    "bridge_slug": "online-booking-for-roofers",
    "bridge_label": "See online booking for roofers",
    "faqs": [
        ("Do reminders really reduce no-shows?",
         "They are the biggest lever there is. Automatic confirmations and reminders by text and email, sent before every inspection, make a homeowner far more likely to be home than a loosely agreed callback ever will. Every booking through the system includes them."),
        ("What happens when someone cancels?",
         "The slot frees up on your calendar instead of sitting empty, so your estimator can fill it with another inspection rather than driving out for a visit that is not happening. You get the time back instead of losing the day.")],
    "trade_slug": "roofers", "trade_plural": "roofers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
