"""Pass 5: remove the done-for-you agency copy (SEO, marketing, ads, map pack, free audit, unmetered).

Appended to focus_reprice.SENTENCES (same row semantics). Re-runnable. Comparison-page rows first,
then the colony bridges, then the hub/website rows and the generic free-audit and meter rows.
"""

ROWS = []

# --- comparison pages (vs_specs_*, generate_vs, colony_specs_category)
ROWS += [('re:Top Shelf is the done-for-you version for local owners: set up, run, and managed for you, on one(?: '
  'bill\\.)?',
  'Top Shelf is a right-sized CRM for local owners with an AI receptionist built in, set up for you.'),
 ('Top Shelf is the done-for-you version of the same all-in-one idea, built for a local business owner who '
  'would rather have it set up and run for them than learn and manage a platform.',
  'Top Shelf is a right-sized CRM built for a local business owner who would rather not learn and manage a '
  'big platform, and it comes set up for you.'),
 ('You get the website, local SEO, AI phone receptionist, CRM, automated follow-up, reviews, and marketing '
  'on one monthly bill, with no setup fee, and your number, your leads, and your data stay yours.',
  'You get the CRM, an AI receptionist that answers and books calls, missed-call text-back, online booking, '
  'and review requests on one plan, with no setup fee, and your number, your leads, and your data stay '
  'yours.'),
 ('Same all-in-one goal, opposite operating model: do it yourself, or have it done for you.',
  'The choice is a deep platform you build out yourself, or a simpler CRM that is ready to use.'),
 ('Top Shelf starts from the same all-in-one idea and flips the operating model. Instead of handing you the '
  'software to run, we set it up and run it for you: a website with local SEO, an AI phone receptionist that '
  'answers and books calls, a <a href="solution-crm.html">CRM with automated follow-up</a> on every lead, '
  'review generation, and ongoing marketing, all managed for you and billed as one monthly bill with no '
  'setup fee. You are not logging into a dashboard to build funnels or wire up automations late at night. '
  'That part is our job.',
  'Top Shelf starts from the same all-in-one idea and keeps it small. It is a <a '
  'href="solution-crm.html">CRM built for a local business</a>, with an AI phone receptionist that answers '
  'and books calls, missed-call text-back, follow-up reminders on every lead, review requests, and online '
  "booking, all on one plan with no setup fee. We set up the receptionist's questions and booking rules for "
  'you, so you are not building funnels or wiring up automations late at night before it works.'),
 ('You get the results and the reporting without having to become the person who operates the platform. If '
  'your goal is to have a modern setup working for your business rather than to run marketing software '
  'yourself, that is the whole point of the done-for-you model.',
  'You use the CRM day to day, but you do not have to become a platform expert to do it. If your goal is a '
  'modern setup working for your business rather than a marketing platform to build out yourself, that is '
  'the point of a right-sized CRM.'),
 ('If you would rather run your business and have the marketing handled, the done-for-you model usually fits '
  'better. You trade some hands-on control for having people set everything up, run it, and keep it working, '
  'on one predictable bill. Top Shelf\'s <a href="pricing.html">plans</a> are built around that trade, from '
  'a managed website and local SEO on up to a fully done-for-you setup. Some owners love operating the '
  "platform themselves, and some would rather that be someone else's job.",
  'If you would rather run your business than build out software, a simpler CRM that comes set up usually '
  'fits better. You trade some depth and control for a receptionist that is answering in days, on one plan. '
  'Top Shelf\'s <a href="pricing.html">Signature plan</a> is built around that trade, and a professional '
  'website is a separate $499 option if you need one. Some owners love building inside a big platform, and '
  'some just want the calls answered and the follow-up done.'),
 ('The same all-in-one, set up and run for you', 'The same all-in-one idea, set up for you'),
 ('We are our own done-for-you platform and agency for local businesses.',
  'We build our own CRM for local businesses.'),
 ('Top Shelf is the done-for-you version of that all-in-one idea for a local owner: we set it up, run it, '
  'and manage it, and you get one bill instead of a dashboard to learn.',
  'Top Shelf is a right-sized take on that all-in-one idea for a local owner: we set it up for you, and you '
  'get a simpler CRM with an AI receptionist built in instead of a platform to master.'),
 ('Done-for-you does not mean anyone holds your business hostage.', ''),
 ('See what a done-for-you setup would <em>look like for you</em>',
  'See what the CRM would <em>look like for you</em>'),
 ('Top Shelf is a done-for-you all-in-one that also answers and books your calls.',
  'Top Shelf is a CRM for local businesses that also answers and books your calls.'),
 ('Top Shelf is a done-for-you alternative that builds and manages your website and local SEO, adds an AI '
  'receptionist that answers and books your calls, runs your CRM and automated follow-up, and handles '
  'reviews and marketing, on one monthly bill, with your number and leads staying yours.',
  'Top Shelf is a CRM for local businesses with online booking, an AI receptionist that answers and books '
  'your calls, follow-up on every lead, and review requests, on one plan set up for you, with your number '
  'and leads staying yours.'),
 ('The trade-off is simply what it is: powerful software you operate yourself, centered on booking and '
  'management, rather than a team that runs your whole online presence for you.',
  'The trade-off is simply what it is: powerful software you operate yourself, centered on booking and '
  'management, with the phone and lead follow-up left to your front desk.'),
 ('Top Shelf starts from the other end of that model. Instead of software you run, it is a done-for-you '
  'service a team runs for you. That team builds and manages your website and local SEO so customers can '
  'find you in local search, sets up your <a href="solution-booking.html">online booking</a>, and puts an',
  'Top Shelf starts from the phone and the follow-up. It is a CRM built for a local business, set up for you '
  'with no setup fee. It includes <a href="solution-booking.html">online booking</a> and puts an'),
 ('A built-in CRM texts and emails new leads automatically, review generation asks happy customers for a '
  'rating at the right moment, and your marketing runs from the same place, all on one monthly bill with no '
  'setup fee.',
  'The CRM keeps every new lead in your pipeline with follow-up reminders, and review requests ask happy '
  'customers for a rating at the right moment, all on one plan with no setup fee.'),
 ('What it does is run the website, the phone, and the follow-up so the owner does not have to.',
  'What it does is answer the phone, book the appointment, and keep the follow-up from slipping.'),
 ('If your priority is having one company build your site, help customers find you locally, answer and book '
  'the phone, and follow up on every lead without you managing any of it, Top Shelf is built for that.',
  'If your priority is a simpler CRM that answers and books the phone and keeps every lead followed up, Top '
  'Shelf is built for that.'),
 ('Some businesses even do both, keeping dedicated booking software while a done-for-you partner runs the '
  'website, the phone, and the marketing around it.',
  'Some businesses even do both, keeping dedicated booking software and adding Top Shelf for the phone and '
  'the follow-up around it.'),
 ('The honest split comes down to who does the work and what you want to be great at.',
  'The honest split comes down to what you want to be great at.'),
 ('Booking, the phone, and the follow-up, all done for you',
  'Booking, the phone, and the follow-up, in one plan'),
 ('Top Shelf sets up online booking and adds an AI receptionist that answers and books calls, and a team '
  'runs it for you.',
  'Top Shelf includes online booking and an AI receptionist that answers and books calls, and we set both up '
  'for you.'),
 ('The difference is the model: Mindbody is deep booking and management software you operate yourself, while '
  'Top Shelf manages your booking, your phone, and your whole online presence as a done-for-you service.',
  'The difference is focus: Mindbody is deep booking and management software, while Top Shelf is a simpler '
  'CRM built around answering the phone, booking, and following up.'),
 ('Top Shelf takes a different approach and focuses on your own website and Google presence so customers '
  'find and call you directly, with the leads staying yours rather than living inside a marketplace.',
  'Top Shelf takes a different approach and focuses on the calls and bookings that come to you directly, '
  'with the leads staying yours rather than living inside a marketplace.'),
 ('See what done-for-you looks like next to <em>software you run yourself</em>',
  'See what the CRM adds next to <em>a booking app alone</em>'),
 ('re:Top Shelf is a done-for-you all-in-one: website, local SEO, an AI receptionist that books calls, '
  'reviews, and(?: marketing\\.)?',
  'Top Shelf is a CRM with an AI receptionist that answers and books new-patient calls, plus review '
  'requests.'),
 ('Top Shelf is a done-for-you, managed all-in-one: it also builds and runs your website and local SEO, '
  'answers and books new-patient calls with an AI receptionist, generates reviews, and runs your marketing, '
  'all on one bill, with your number and your leads staying yours.',
  'Top Shelf is a right-sized CRM with an AI receptionist built in: it answers and books new-patient calls, '
  'texts back missed calls, follows up on every lead, and sends review requests, all on one plan set up for '
  'you, with your number and your leads staying yours.'),
 ('Building your website, ranking in local search, and running your marketing sit outside what a '
  'communication platform sets out to do.',
  ''),
 ('Top Shelf is not a tool you log into and operate. It is a done-for-you system that a team sets up and '
  'runs for you, covering the whole path a new patient travels from finding you to booked. That starts with '
  'a website and local SEO so people searching for your service actually land on you, and it includes an',
  'Top Shelf is a right-sized CRM for a local practice, set up for you with no setup fee, and it covers the '
  'path a new patient travels from first call to booked. At its center is an'),
 ('A CRM follows up on every lead automatically, <a href="solution-reviews.html">review generation</a> turns '
  'your happy customers into the reviews that win the next caller, and your marketing runs on top of it, all '
  'managed for you and billed as one line instead of a stack of logins.',
  'The CRM keeps every lead in front of you with follow-up reminders, and <a '
  'href="solution-reviews.html">review requests</a> turn your happy customers into the reviews that win the '
  'next caller, all on one plan instead of a stack of logins.'),
 ('If your bigger problem is being found by new patients and turning those calls into booked appointments, '
  'and you would rather someone built the website, ran the local SEO, answered the phone, gathered the '
  'reviews, and handled the marketing for you, an all-in-one, done-for-you setup usually fits better.',
  'If your bigger problem is turning new-patient calls into booked appointments, and you want the phone '
  'answered, every lead followed up, and reviews requested without adding staff, a CRM with an AI '
  'receptionist built in usually fits better.'),
 ('Some offices even want both, a communication platform for their existing patients and a done-for-you '
  'engine for growth.',
  'Some offices even want both, a communication platform for their existing patients and Top Shelf for '
  'catching and booking new ones.'),
 ('One managed all-in-one, from found to booked', 'One CRM, from first call to booked'),
 ('Top Shelf is a done-for-you all-in-one that also builds your website, runs your local SEO, answers and '
  'books new-patient calls, gathers reviews, and handles marketing. If your goal is being found by new '
  'patients and having the front desk and follow-up run for you, Top Shelf is built for that job.',
  'Top Shelf is a CRM with an AI receptionist built in that answers and books new-patient calls, follows up '
  'on every lead, and sends review requests. If your goal is booking more new patients without the front '
  'desk missing calls or dropping follow-up, Top Shelf is built for that job.'),
 ('re:Top Shelf is the done-for-you alternative for local service businesses, with a real AI receptionist(?: '
  'answering the phone and the whole setup managed for you\\.)?',
  'Top Shelf is a simpler CRM with an AI receptionist that answers and books calls.'),
 ('Top Shelf is the done-for-you alternative built for local service businesses. Instead of handing you a '
  'dashboard to operate, a team builds and runs the whole setup for you: a website built to rank in local '
  'search, a real AI receptionist that answers the phone and books the job, a CRM that follows up on every '
  'lead, review generation, and marketing, all on one bill. The honest way to choose is to decide whether '
  'you want to run the software yourself or have it run for you, and to make sure',
  'Top Shelf is a simpler alternative built for local service businesses. It is a right-sized CRM, set up '
  'for you with no setup fee: a real AI receptionist that answers the phone and books the job, missed-call '
  'text-back, follow-up on every lead, review requests, and invoices by text, all on one plan. The honest '
  'way to choose is to decide how much platform you actually need, and to make sure'),
 ('The only real question is whether running the software is work you want to own, or work you would rather '
  'hand off.',
  'The only real question is how much of that platform you will actually use.'),
 ('Top Shelf starts from the opposite end. Rather than handing you software to run, we build and manage the '
  'whole thing for you: the website, the local SEO, the CRM and its automated follow-up, review generation, '
  'and the marketing that feeds it. You get one point of contact and one bill instead of a dashboard to '
  'learn.',
  'Top Shelf starts from the opposite end. Rather than a broad platform with add-ons, it is a right-sized '
  'CRM with follow-up, review requests, online booking, and invoices by text, set up for you with no setup '
  'fee. You get one plan and one point of contact instead of a long list of tools to learn.'),
 ('This is a difference in who does the work, not a knock on doing it yourself. A platform you operate '
  'rewards the owner who has the time and the temperament to run it. A done-for-you service fits the owner '
  'who would rather spend that time on the actual job and let someone else keep the website, the phone, and '
  'the follow-up running.',
  'This is a difference in scope, not a knock on Thryv. A broad platform rewards the owner who has the time '
  'and the temperament to run all of it. A right-sized CRM fits the owner who would rather spend that time '
  'on the actual job and let the receptionist and the follow-up run in the background.'),
 ('We build your site to rank in local search and to turn visitors into calls, but no honest provider',
  'If you buy our $499 website, it is built so Google can read it and to turn visitors into calls, but no '
  'honest provider'),
 ('Top Shelf is done-for-you: a team builds and runs your website, AI receptionist, CRM, reviews, and '
  'marketing for you, on one bill. Thryv is a capable platform, so the real difference is who does the '
  'day-to-day work, not whether the tools exist.',
  'Top Shelf is a right-sized CRM with an AI receptionist built in, review requests, and follow-up, set up '
  'for you on one plan. Thryv is a capable platform, so the real difference is scope and setup, not whether '
  'the tools exist.'),
 ('See what we would run <em>for you</em>', 'See what we would set up <em>for you</em>'),
 ('Top Shelf includes both inside an all-in-one, done-for-you platform, one bill.',
  'Top Shelf includes both inside a CRM with an AI receptionist built in.'),
 ('Top Shelf covers reviews and messaging too, but as one part of an all-in-one, done-for-you platform that '
  'also builds your website, answers your phone, and follows up on every lead, all managed for you on one '
  'bill. The real choice is a focused tool you run versus the whole front office run for you.',
  'Top Shelf covers reviews and messaging too, but as one part of a CRM that also answers your phone with an '
  'AI receptionist, texts back missed calls, and follows up on every lead, all on one plan set up for you. '
  'The real choice is a focused tool versus one system for the whole front office.'),
 ('but they sit inside a wider platform, and it is done for you rather than handed over as software to '
  'operate. The same setup that asks your happy customers for a <a href="solution-reviews.html">review</a> '
  'also builds your website and answers your phone with an',
  'but they sit inside a wider CRM that comes set up for you. The same system that asks your happy customers '
  'for a <a href="solution-reviews.html">review</a> also answers your phone with an'),
 ('The model is the real difference. Podium is one focused tool you run; Top Shelf is the whole front '
  'office, run for you, on one bill. You are not signing up for messaging in one place, a website company in '
  'another, an SEO service somewhere else, and a call answering service on top, then stitching them together '
  'and paying four invoices. It is one team, one platform, one monthly price, and',
  'Scope is the real difference. Podium is one focused tool; Top Shelf is the whole front office in one CRM. '
  'You are not signing up for messaging in one place, a CRM in another, and a call answering service on top, '
  'then stitching them together and paying three invoices. It is one platform on one plan, and'),
 ('For an owner who would rather run the business than run the software, that is the whole point.',
  'For an owner who would rather run the business than juggle software, that is the whole point.'),
 ('You are wearing every hat, your site is dated or missing, calls go unanswered while you are on a job, and '
  'you do not have the time or the wish to log into one more dashboard. In that case an all-in-one platform '
  'that builds the site, answers the phone, gathers the reviews, and follows up, all managed for you, '
  'usually does more of the work while asking less of your attention.',
  'You are wearing every hat, calls go unanswered while you are on a job, and you do not have the time or '
  'the wish to juggle several dashboards. In that case one CRM that answers the phone, books the job, '
  'requests the reviews, and follows up usually does more of the work while asking less of your attention.'),
 ('You can also see what Top Shelf includes at every tier on the <a href="pricing.html">pricing</a> page.',
  'You can also see what the Signature plan includes on the <a href="pricing.html">pricing</a> page.'),
 ('Reviews and messaging, inside one done-for-you platform', 'Reviews and messaging, inside one CRM'),
 ('Top Shelf generates reviews and handles your customer messaging as one part of a platform that also '
  'builds your website, answers your phone with an AI receptionist, and follows up on every lead through the '
  'CRM.',
  'Top Shelf requests reviews and handles your customer messaging as one part of a CRM that also answers '
  'your phone with an AI receptionist and follows up on every lead.'),
 ('There is no setup fee, we manage the whole thing for you, and',
  'There is no setup fee, we set it up for you, and'),
 ('Podium is a focused software platform you operate, while Top Shelf folds reviews and messaging into an '
  'all-in-one, done-for-you platform that also builds your website, answers your phone, and follows up on '
  'leads, all managed for you on one bill.',
  'Podium is a focused software platform, while Top Shelf folds reviews and messaging into a CRM that also '
  'answers your phone with an AI receptionist and follows up on leads, on one plan.'),
 ('The difference is that they are one part of a wider setup we run for you, not a separate tool you log '
  'into and manage, so they work alongside your website, your phone, and your follow-up instead of standing '
  'on their own.',
  'The difference is that they are one part of the same CRM, not a separate tool you log into, so they work '
  'alongside your phone and your follow-up instead of standing on their own.'),
 ("Top Shelf's platform centers on getting you found, answering the phone, booking the job, and following up "
  'on every lead.',
  "Top Shelf's platform centers on answering the phone, booking the job, and following up on every lead, and "
  'it also lets you send an invoice by text and take card payments.'),
 ('Top Shelf builds your site, answers your phone, and follows up, with review generation included.',
  'Top Shelf is a CRM that answers your phone and follows up, with review requests included.'),
 ('Top Shelf includes review generation as one part of an all-in-one, done-for-you platform for a single '
  'local business that also builds the site, answers the phone, and follows up, all on one bill.',
  'Top Shelf includes review requests and review replies as one part of a CRM for a single local business '
  'that also answers the phone and follows up, all on one plan.'),
 ('Instead of a standalone reputation tool you log into and run, Top Shelf is an all-in-one, done-for-you '
  'platform for a single local business. The same team that asks your happy customers for a <a '
  'href="solution-reviews.html">review</a> at the right moment and replies to every rating in your voice '
  'also builds your website and local SEO, answers your phone with an AI receptionist, and runs the CRM that '
  'follows up on every lead.',
  'Instead of a standalone reputation tool, Top Shelf is a CRM for a single local business, set up for you. '
  'The same system that asks your happy customers for a <a href="solution-reviews.html">review</a> at the '
  'right moment and helps you reply to every rating also answers your phone with an AI receptionist and '
  'follows up on every lead.'),
 ('The other difference is who does the work. Top Shelf is managed for the owner, so you are not the one '
  'operating a dashboard or remembering to send the ask; the system runs, and you get the results.',
  'The other difference is how much you have to remember. Review requests go out on their own after a job, '
  'so you are not the one remembering to send the ask.'),
 ('instead of a reputation tool sitting on top of a separate website, phone line, and CRM',
  'instead of a reputation tool sitting on top of a separate phone line and CRM'),
 ('You can see how the pieces work together across your marketing.', ''),
 ('If you are a single local business and what you actually want is more real five-star proof without '
  'becoming the person who runs the software, an all-in-one that handles reviews as one part of building the '
  'site, answering the phone, and following up will usually serve you better,',
  'If you are a single local business and what you actually want is more real five-star proof without '
  'running a separate reputation platform, a CRM that handles reviews as one part of answering the phone and '
  'following up will usually serve you better,'),
 ('the same all-in-one that builds your website, answers your phone, and follows up on every lead',
  'the same all-in-one that answers your phone and follows up on every lead'),
 ('For a single local business that wants its reviews handled as one part of an all-in-one, done-for-you '
  'setup, yes. Top Shelf includes review generation, monitoring, and responses inside the same system that '
  'builds your site, answers your phone, and follows up.',
  'For a single local business that wants its reviews handled as one part of an all-in-one CRM, yes. Top '
  'Shelf includes review requests and review replies inside the same system that answers your phone and '
  'follows up.'),
 ('Top Shelf includes review generation as one part of a wider all-in-one that also builds your website, '
  'answers your phone, and runs your follow-up.',
  'Top Shelf includes review requests as one part of a wider all-in-one that also answers your phone and '
  'runs your follow-up.'),
 ('so it runs inside your website, phone, and CRM', 'so it runs inside your phone and CRM'),
 ('Vagaro Alternative: An All-in-One, Done-for-You Platform',
  'Vagaro Alternative: An All-in-One CRM That Answers Calls'),
 ('Top Shelf is an all-in-one, done-for-you platform that also answers calls.',
  'Top Shelf is an all-in-one CRM that also answers and books calls.'),
 ('Top Shelf is an all-in-one, done-for-you platform for those same local businesses. It includes online '
  'booking, but it also adds an AI receptionist that answers and books the calls a booking app never '
  'catches, plus your website, local SEO, review generation, and marketing, all managed for you on one bill. '
  'If you want strong software to operate, Vagaro is a fair pick. If you want the whole front office handled '
  'for you, that is where Top Shelf is different.',
  'Top Shelf is an all-in-one CRM for those same local businesses. It includes online booking, but it also '
  'adds an AI receptionist that answers and books the calls a booking app never catches, plus missed-call '
  'text-back, review requests, and follow-up, all on one plan set up for you. If you want deep booking and '
  'checkout software, Vagaro is a fair pick. If you want the phone answered and every client followed up, '
  'that is where Top Shelf is different.'),
 ('Getting found by new customers, answering the phone when it rings, gathering reviews, and running '
  'marketing are separate jobs, and a booking platform is not built to do those for you.',
  'Answering the phone when it rings, following up, and gathering reviews are separate jobs, and a booking '
  'platform is not built to do those for you.'),
 ('Top Shelf is more than a booking app, and it is not something you have to run yourself. It is an '
  'all-in-one, done-for-you platform plus an agency that manages the whole thing for you.',
  'Top Shelf is more than a booking app. It is an all-in-one CRM built for a local business, set up for you '
  'with no setup fee.'),
 ('Top Shelf builds and manages your website and local SEO so new clients can find you, generates reviews so '
  'the ones who love you say so publicly, and runs your follow-up and marketing so quiet weeks fill back up.',
  'Top Shelf sends review requests so the clients who love you say so publicly, and keeps your follow-up '
  'going so quiet weeks fill back up.'),
 ('All of it arrives as one managed service on one bill', 'All of it comes on one plan'),
 ('If your real problem is the opposite, being hard to find online, missing calls while you work, thin '
  'reviews, and no time to market, then an all-in-one that answers the phone, gets you found, and handles '
  'the follow-up will usually do more for your calendar than a booking app alone. Plenty of businesses even '
  'keep the booking tool they like and add Top Shelf for the website, phone, reviews, and marketing on top.',
  'If your real problem is the opposite, missing calls while you work, thin reviews, and no time to follow '
  'up, then an all-in-one that answers the phone, books the client, and handles the follow-up will usually '
  'do more for your calendar than a booking app alone. Plenty of businesses even keep the booking tool they '
  'like and add Top Shelf for the phone, reviews, and follow-up on top.'),
 ('One managed platform that books, answers, and markets for you',
  'One CRM that books, answers, and follows up'),
 ('Top Shelf includes online booking, but it is an all-in-one, done-for-you platform, not only a scheduler. '
  'It also builds and manages your website and local SEO, answers and books your phone calls with an AI '
  'receptionist, generates reviews, and runs your follow-up and marketing, all managed for you rather than '
  'software you operate yourself.',
  'Top Shelf includes online booking, but it is an all-in-one CRM, not only a scheduler. It also answers and '
  'books your phone calls with an AI receptionist, texts back missed calls, sends review requests, and runs '
  'your follow-up, all set up for you.'),
 ('Some businesses keep the booking tool they like and add Top Shelf on top for the website, the phone '
  'answering, review generation, and marketing.',
  'Some businesses keep the booking tool they like and add Top Shelf on top for the phone answering, review '
  'requests, and follow-up.'),
 ('Top Shelf is a done-for-you, right-sized alternative for a small local business.',
  'Top Shelf is a right-sized CRM for a small local business, set up for you.'),
 ('Top Shelf is a different fit: a done-for-you platform and agency, right-sized for a small local business '
  'that wants its phone answered, its website and marketing handled, and its leads followed up, all managed '
  'for the owner on one flat monthly bill.',
  'Top Shelf is a different fit: a right-sized CRM for a small local business that wants its phone answered, '
  'its jobs booked and dispatched, and its leads followed up, all set up for you on one plan.'),
 ('If you want the essentials handled for you without running heavy software, Top Shelf is the better fit.',
  'If you want the essentials in a simpler CRM without heavy software to staff, Top Shelf is the better '
  'fit.'),
 ('Instead of software your team operates, it is a done-for-you platform and agency that is managed for the '
  'owner. Top Shelf builds and runs your website and local SEO, <a href="solution-ai-phone.html">answers '
  'your phone with an AI receptionist</a> that books the job, runs a CRM that follows up on every lead '
  'automatically, and handles your reviews and marketing.',
  'Instead of a full operations suite, it is a CRM built for a small local business and set up for you. Top '
  'Shelf <a href="solution-ai-phone.html">answers your phone with an AI receptionist</a> that books the job, '
  'puts it on a simple dispatch board, keeps every lead followed up, and sends review requests when the work '
  'is done.'),
 ('The heart of the difference is who does the work.',
  'The heart of the difference is how much system you need.'),
 ('With Top Shelf, the work of answering calls, following up, and keeping the marketing going is handled for '
  'you, so a small business gets the results without hiring the team or learning the software.',
  'With Top Shelf, the AI receptionist answers calls and the CRM keeps follow-up on track, so a small '
  'business gets the results without hiring an office to run heavy software.'),
 ('Top Shelf is right-sized for that business: the essentials handled for you, on a flat bill, with no heavy '
  'software to staff.',
  'Top Shelf is right-sized for that business: the essentials in one CRM, set up for you, with no heavy '
  'software to staff.'),
 ('One flat bill, handled for you, sized for a local business',
  'One plan, set up for you, sized for a local business'),
 ('Top Shelf is a done-for-you service that handles the website, phone, follow-up, and marketing for a small '
  'local business, with no heavy software for the owner to run.',
  'Top Shelf is a right-sized CRM that handles the phone, booking, follow-up, and reviews for a small local '
  'business, with no heavy software to staff.'),
 ('If you want the essentials handled for you, Top Shelf is the better fit.',
  'If you want the essentials in a simpler system, Top Shelf is the better fit.'),
 ('No, and that is the main difference in model.', 'Not extra staff, and that is the main difference.'),
 ('With Top Shelf, answering calls, following up on leads, and keeping the marketing going are all handled '
  'for you, so a small business gets the results without hiring an office to run software.',
  'With Top Shelf, the AI receptionist answers calls and the CRM keeps every lead followed up, so a small '
  'business gets the results without hiring an office to run software.'),
 ('Your website and local SEO, an AI receptionist that answers the phone and books the job, a CRM that '
  'follows up on every lead, and your reviews and marketing.',
  'An AI receptionist that answers the phone and books the job, a CRM that follows up on every lead, a '
  'dispatch board, review requests, estimates, and invoices by text, with card payments.'),
 ('See what a right-sized, done-for-you setup <em>looks like</em>',
  'See what a right-sized CRM <em>looks like</em>'),
 ('Looking for a Jobber Alternative? Here Is the Done-For-You Option',
  'Looking for a Jobber Alternative? Here Is One That Answers Your Phone'),
 ('Top Shelf is the all-in-one, done-for-you alternative that answers your phone and follows up on every '
  'lead.',
  'Top Shelf is the all-in-one CRM alternative that answers your phone and follows up on every lead.'),
 ('Top Shelf is the all-in-one, done-for-you alternative: instead of a tool you operate, a team builds your '
  'website, handles your local SEO, answers your phone with an AI receptionist, and follows up on every '
  'lead, all on one monthly bill. The real choice is not which software is better, but whether you want to '
  'run the system yourself or have it run for you.',
  'Top Shelf is the all-in-one CRM alternative built around the front office: an AI receptionist answers '
  'your phone and books the job, missed calls get a text back, and every lead gets followed up, all on one '
  'plan set up for you. The real choice is not which software is better, but which part of the business you '
  'need help with most.'),
 ('before a job is ever booked: getting found, answering the phone, and following up on every lead.',
  'before a job is ever booked: answering the phone and following up on every lead.'),
 ('Top Shelf is not one more tool you log into and operate. It is an all-in-one platform with a team behind '
  'it that runs the work for you. We build your website, handle your local SEO, answer your phone with an <a '
  'href="solution-ai-phone.html">AI receptionist</a> that books the job, run a CRM that follows up on every '
  'lead, generate reviews, and handle your marketing, all on one monthly bill. Where field-service software '
  'hands you the controls, Top Shelf hands you the finished result.',
  'Top Shelf is a right-sized CRM built for the front office, and we set it up for you. It answers your '
  'phone with an <a href="solution-ai-phone.html">AI receptionist</a> that books the job, texts back missed '
  'calls, keeps every lead followed up, and sends review requests, all on one plan. Where most field-service '
  'software starts once the job is booked, Top Shelf starts with the call.'),
 ('It is the done-for-you version of the front office rather than a kit of tools you run.',
  'It is the front office in one system rather than a kit of separate tools.'),
 ('If the trouble is the other end of the business, the phone going to voicemail, leads going cold, no time '
  'to build a site or run marketing or chase every quote, and you would rather have it handled than log into '
  'one more system, then the done-for-you approach fits better.',
  'If the trouble is the other end of the business, the phone going to voicemail, leads going cold, and no '
  'time to chase every quote, then a CRM with an AI receptionist built in fits better.'),
 ('If getting found and getting jobs is already handled and what you need is software',
  'If the phone and lead follow-up are already handled and what you need is software'),
 ('One CRM that follows up on every lead, run for you',
  'One CRM that follows up on every lead, set up for you'),
 ('Top Shelf is a done-for-you platform that builds your site, handles your local SEO, answers your phone, '
  'follows up on leads, and runs your marketing.',
  'Top Shelf is a CRM that answers your phone with an AI receptionist, books the job, and follows up on '
  'leads.'),
 ('re:Top Shelf is the done-for-you alternative that answers your phone, builds your site, and follows up(?: '
  'for you\\.)?',
  'Top Shelf is a CRM alternative that answers your phone and follows up on every lead.'),
 ('Top Shelf is a done-for-you alternative built for local businesses: your website and local SEO, an AI '
  'receptionist that answers the phone, a CRM that follows up on every lead, review generation, and '
  'marketing, all set up and managed for you on one monthly bill. The real difference is the model. '
  'Housecall Pro is software you operate; Top Shelf is a team that runs the front office for you.',
  'Top Shelf is a right-sized CRM built for local businesses: an AI receptionist that answers the phone and '
  'books the job, a CRM that follows up on every lead, missed-call text-back, and review requests, all set '
  'up for you on one plan. The real difference is focus. Housecall Pro is built around running the job; Top '
  'Shelf is built around catching the call and the lead.'),
 ('Those are still tools you switch on and manage yourself, which is exactly right for owners who want that '
  'control, and exactly the part some owners would rather hand off.',
  'Those are still tools you switch on and manage yourself, which is exactly right for owners who want that '
  'control.'),
 ('Top Shelf is built around a different answer to who does the work. Instead of software you operate, it is '
  'a done-for-you platform and agency: a team builds your website, runs your local SEO, sets up the CRM, '
  'answers your phone, generates reviews, and handles the marketing, then manages all of it for you. You get '
  'one monthly bill instead of a stack of logins to keep up with.',
  'Top Shelf is built around the front office. It is a right-sized CRM with an AI receptionist built in, and '
  'we set it up for you, including the questions the receptionist asks and your booking rules. You get one '
  'plan instead of a stack of logins to keep up with.'),
 ('Two things stay true no matter which plan you are on.', 'Two things stay true either way.'),
 ('And Top Shelf is honest about what it is not: it is not field-operations software, so if you want to run '
  'dispatch, work orders, and technician scheduling yourself, that is not what this replaces. What it '
  'replaces is the pile of front-office work, getting found, answering, following up, and marketing, that an '
  'owner rarely has the time to do well alone.',
  'And Top Shelf is honest about what it is not: it has a simple dispatch board, but it is not a full '
  'field-operations suite, so if you want to run deep work orders and technician scheduling yourself, that '
  'is not what this replaces. What it replaces is the pile of front-office work, answering, booking, '
  'following up, and asking for reviews, that an owner rarely has the time to do well alone.'),
 ('If your main need is the opposite, getting found online, having the phone answered, and having every lead '
  'followed up and every review requested for you without adding another system to run, then a done-for-you '
  'platform is the better fit.',
  'If your main need is the opposite, having the phone answered, every lead followed up, and every review '
  'requested without building it all yourself, then a CRM with an AI receptionist built in is the better '
  'fit.'),
 ('Top Shelf is a done-for-you platform that handles the front office, your website, phone, follow-up, '
  'reviews, and marketing, and manages it for you.',
  'Top Shelf is a CRM that handles the front office, your phone, follow-up, and reviews, and it comes set up '
  'for you.'),
 ('If you want the getting-found and getting-booked side handled for you, that is what Top Shelf does.',
  'If you want the calls answered and booked and every lead followed up, that is what Top Shelf does.'),
 ('No, and that is the point of the model. Top Shelf sets up and manages the website, the AI receptionist, '
  'the CRM, the reviews, and the marketing for you, and sends one monthly bill. You get the results and the '
  'reporting without logging into a platform to keep it running.',
  'You use the CRM, but you do not have to build it. Top Shelf sets up the AI receptionist, its intake '
  'questions and booking rules, and the CRM for you, with no setup fee. After that the receptionist answers, '
  'missed calls get a text back, and review requests go out without you remembering to send them.'),
 ('re:Smith\\.ai is a specialist virtual receptionist and intake service, human agents plus AI\\.(?: Top '
  'Shelf is an all-in-one platform where the AI receptionist is one part, alongside your website, marketing, '
  'and CRM follow-up, on one flat bill\\.)?(?! Top Shelf is a CRM)',
  'Smith.ai is a specialist virtual receptionist and intake service, human agents plus AI. Top Shelf is a '
  'CRM with an AI receptionist built in.'),
 ('Top Shelf is an all-in-one, done-for-you platform for local small businesses, where an AI receptionist '
  'that answers and books is one part of a package that also builds your website and local SEO, runs your '
  'marketing, and follows up on every lead through a CRM, all on one flat monthly bill. The question is not '
  'who answers the phone better, it is whether you want a specialist for the front desk or one company '
  'running the whole front office.',
  'Top Shelf is a right-sized CRM for local small businesses, where an AI receptionist that answers and '
  'books is one part of a package that also texts back missed calls, sends review requests, and follows up '
  'on every lead, all on one plan. The question is not who answers the phone better, it is whether you want '
  'a specialist for the front desk or one system for the whole front office.'),
 ('It does mean the website that brings those calls in, and the marketing behind it, are still yours to '
  'build and run, on your own or through other vendors, and the tools your leads live in',
  'It does mean the tools your leads live in'),
 ('Top Shelf is not an answering service, it is the whole front office, done for you.',
  'Top Shelf is not an answering service, it is a CRM for the whole front office, set up for you.'),
 ('The same platform builds your website and local SEO so the calls start coming, runs the marketing that '
  'keeps them coming, and hands every captured lead to a CRM that follows up on its own,',
  'The same platform hands every captured lead to a CRM that follows up,'),
 ('You get one company, one login, and one flat monthly bill for the parts that usually arrive from four '
  'different vendors.',
  'You get one company, one login, and one plan for the parts that usually arrive from several different '
  'vendors.'),
 ('and you would rather one company build the site, bring in the calls, answer them, and follow up than '
  'stitch together a receptionist service, a web designer, a marketer, and a CRM yourself,',
  'and you would rather have one system answer the calls, book them, and follow up than stitch together a '
  'receptionist service and a separate CRM yourself,'),
 ('Top Shelf is an all-in-one platform for local businesses where an AI receptionist is one part, alongside '
  'your website, local SEO, marketing, and a CRM that follows up on every lead, all on one flat bill.',
  'Top Shelf is an all-in-one CRM for local businesses where an AI receptionist is one part, alongside '
  'missed-call text-back, review requests, and follow-up on every lead, all on one plan.'),
 ('If you want the whole front office run for you, that is what Top Shelf is built for.',
  'If you want the whole front office in one system, that is what Top Shelf is built for.'),
 ('or move the whole thing over so one company runs it. Either way there is no setup fee',
  'and we can add an AI chatbot to it. There is no setup fee'),
 ('re:Top Shelf is a done-for-you service that helps fill one by answering and booking the(?: new-client '
  'call\\. The honest difference\\.)?',
  'Top Shelf is a CRM that helps fill one by answering and booking the new-client call.'),
 ('Top Shelf is a done-for-you platform and agency built to help fill a practice: getting the firm found, '
  'answering and booking the new-client call, and following up on every lead.',
  'Top Shelf is a CRM with an AI receptionist built in, made to help fill a practice: answering and booking '
  'the new-client call and following up on every lead.'),
 ('If your gap is capturing new clients and getting found, that is ours.',
  'If your gap is capturing new clients, that is ours.'),
 ('That is a different thing from a service that answers your new-client call at nine at night, or a team '
  'that keeps your website, reviews, and lead follow-up running for you while the lawyers practice law.',
  'That is a different thing from a receptionist that answers your new-client call at nine at night, or a '
  'CRM that keeps lead follow-up and review requests running while the lawyers practice law.'),
 ('Top Shelf is not another piece of software for your team to learn and run. It is a done-for-you platform '
  'and agency, managed for the owner, on one monthly bill. Instead of the back office, it works on the front '
  'of the firm: the website and local search presence that helps prospective clients find you, an',
  'Top Shelf is not another practice management system for your team to learn. It is a right-sized CRM, set '
  'up for you with no setup fee, on one plan. Instead of the back office, it works on the front of the firm: '
  'an'),
 ('and review generation that builds the reputation new clients check first.',
  'and review requests that build the reputation new clients check first.'),
 ('If your real problem is that new-client calls slip to voicemail, leads never get a second touch, or '
  'people in your area cannot easily find and choose your firm,',
  'If your real problem is that new-client calls slip to voicemail or leads never get a second touch,'),
 ('and one done-for-you service to bring it in.', 'and one CRM to bring it in.'),
 ('One managed service to answer and book the intake call', 'One CRM to answer and book the intake call'),
 ('Top Shelf is built to help fill a practice: getting the firm found, answering and booking the new-client '
  'call, and following up on leads.',
  'Top Shelf is built to help fill a practice: answering and booking the new-client call and following up on '
  'leads.'),
 ('It is one managed monthly bill with no setup fee.', 'It is one monthly plan with no setup fee.'),
 ('and with Top Shelf, someone who runs it for you.', 'and with Top Shelf, it comes set up for you.'),
 ('the website, reviews, and marketing all feed the same pipeline',
  'missed calls, review requests, and follow-up all run from the same pipeline'),
 ('Top Shelf takes the model one step further than most all-in-one software: it is done for you. You are not '
  'buying a platform to run yourself and hoping you have time to configure it, you have a team running the '
  'phone, the follow-up, the site, and the marketing on your behalf.',
  'Top Shelf keeps the model simple: it is a right-sized CRM, and it comes set up for you. You are not '
  "buying a platform and hoping you have time to configure it. We set up the AI receptionist's questions and "
  'booking rules, so it is answering in days.'),
 ('one done-for-you system that just works together is usually the better trade.',
  'one connected system that comes set up for you is usually the better trade.'),
 ('One connected system, run for you', 'One connected system, set up for you'),
 ('and it is done for you rather than one more dashboard to manage.',
  'and it comes set up for you rather than as a blank dashboard to configure.'),
 ('Website, calls, CRM, reviews, follow-up, and marketing under one roof, on one bill, with one number to '
  'call.',
  'Calls, CRM, booking, follow-up, reviews, and payments in one app, on one bill, with one number to call.'),
 ('One Team, One Bill', 'One App, One Bill'),
 ('A new site gets built, and you own it', 'Want a new site? You own it.'),
 ('We build you a fast, modern website from scratch, and it belongs to you from day one, with the content '
  'yours to keep.',
  'Our professional website is $499 one time, and it belongs to you from day one, with the content yours to '
  'keep.'),
 ('A platform is only truly all-in-one for you if it covers that list and, ideally, runs it for you.',
  'A platform is only truly all-in-one for you if it covers that list and, ideally, comes set up for you.'),
 ('Top Shelf pairs the software with the team that runs it, on one bill starting at $99 a month, with no '
  'setup fee.',
  'Top Shelf is a right-sized CRM with an AI receptionist built in, set up for you, starting at $99 a month '
  'with no setup fee.'),
 ('Software plus the team that runs it', 'Software that comes set up for you'),
 ('Top Shelf gives you the connected software and the people who run it for you, so the tools actually get '
  'used and your customers stay yours.',
  'Top Shelf gives you connected software that is set up for you, with an AI receptionist and follow-up that '
  'run on their own, so the tools actually get used and your customers stay yours.'),
 ('Top Shelf is built to pass its own checklist: your assets are yours from day one, reporting is in plain '
  'language tied to dollars, plans are month to month, and it is one team rather than a call center. And the '
  'fair caveat still stands. If you already have a capable marketing person in-house, doing it yourself can '
  'make more sense.',
  'To be clear, Top Shelf is not a marketing agency, and it does not run your marketing. It is a CRM with an '
  'AI receptionist built in, set up for you with no setup fee, so the review requests and lead follow-up '
  'that usually slip go out on their own. Your number, your leads, and your data stay yours, and the plan is '
  'month to month. If you want someone to run your marketing for you, use the checklist above on any agency '
  'you consider.'),
 ('Done for you, owned by you', 'When the work is follow-up, let software do it'),
 ('Done-for-you marketing is worth it when the work gets done, the results are yours to keep, and you can '
  'see in plain dollars that it is working. That is the standard Top Shelf is built to.',
  'A lot of what slips is follow-up: asking for reviews, getting back to leads, answering the phone. Top '
  "Shelf's CRM and AI receptionist handle that on their own, set up for you, and your customers stay yours."),
 ('Top Shelf is built as that middle. You get the software and the team that runs it on one bill, starting '
  'at $99 a month with no setup fee and no long contract, and your website, number, Google profile, and '
  'customer list stay in your name.',
  'Top Shelf covers part of that middle. It is a CRM with an AI receptionist built in, set up for you with '
  'no setup fee, so calls get answered, leads get followed up, and review requests go out on their own. It '
  'starts at $99 a month with no long contract, and your number, your leads, and your data stay yours. It '
  'does not run your ads or your marketing.'),
 ('For most owners with more work than hours, the answer is both together.',
  'For most owners with more work than hours, software that runs the follow-up on its own is a good place to '
  'start.'),
 ('The middle between agency and software', 'Software that does the follow-up for you'),
 ('You should not have to choose between paying an agency that owns your assets and running software you '
  'have no time for. Top Shelf gives you both at once: run for you, owned by you, on one bill.',
  'If the work that keeps slipping is answering calls, following up, and asking for reviews, you may not '
  "need an agency. Top Shelf's CRM and AI receptionist do that work on their own, set up for you, and "
  'everything stays yours.')]

# --- colony 'The fix' bridges that sold marketing: point at the Signature plan features
ROWS += [('Most appliance repair calls begin in the map pack. Keeping your Google profile active, focused on the '
  'towns you cover, and full of recent reviews is how you show up first when an appliance quits nearby.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the repair company they can already see', 'Catch every call your visibility brings in'),
 ('Most collision work starts with a search right after a wreck. Marketing that puts you in the map pack, '
  'builds real reviews, and answers the insurance questions is how you get chosen at the moment a driver '
  'needs a shop.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found and chosen after the accident', 'Catch every call your visibility brings in'),
 ('Most detailing customers begin with a search or a scroll. Keeping your Google profile active and full of '
  'reviews, and your finished work in front of people, is how you show up when someone nearby wants their '
  'car detailed.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get seen where the bookings start', 'Catch every call your visibility brings in'),
 ('Most new customers start with a search and decide on your reviews. Keeping your Google profile active and '
  'your reviews honest and recent is how you show up and earn the call when a driver needs a shop nearby.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found by the drivers searching now', 'Catch every call your visibility brings in'),
 ('Most bankruptcy clients begin with a private search in a hard moment. Getting your Google presence '
  'verified, active, and full of genuine reviews, and answering the questions people ask, is how you show up '
  'and earn the free consultation.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found where people quietly search', 'Catch every call your visibility brings in'),
 ('Most men pick a barber from the map and a quick scroll of the work. Keeping your Google profile active '
  'and full of recent cuts and reviews is how you become the close, trusted shop he walks into.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the shop they can already see', 'Catch every call your visibility brings in'),
 ('Most new patients start with a local search in a moment of pain. Keeping your Google profile active, your '
  'reviews strong, and your booking one tap is how you become the office they pick when their back gives out '
  'nearby.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the chiropractor they find first', 'Catch every call your visibility brings in'),
 ('Marketing for commercial real estate keeps you visible to the owners, tenants, and investors in your '
  'submarket and builds the reputation a business checks before trusting you with a deal, so the mandate '
  'comes to the name they already know.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Marketing that makes you the name your market knows', 'Catch every call your visibility brings in'),
 ('Most criminal defense clients start with a panicked search after an arrest. Marketing that keeps you '
  'visible on Google, full of genuine reviews, and in front of your referral sources is how you get chosen '
  'at that moment.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found where the cases start', 'Catch every call your visibility brings in'),
 ('Most day spa growth starts in the map pack and your reviews, and around the gifting seasons when people '
  'search for a spa day to give, then compounds when you rebook the guests you already have. Marketing that '
  'does both keeps the calendar full.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found, then keep them coming back', 'Catch every call your visibility brings in'),
 ('Most new patients start with a search and pick from the map pack. Marketing that keeps your profile '
  'active, your reviews growing, and your site answering the insurance question is how you get chosen when '
  'someone nearby needs a dentist.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found where new patients look', 'Catch every call your visibility brings in'),
 ('Most new patients, medical and cosmetic, start with a search. Keeping your Google profile active, your '
  'reviews fresh, and your local presence strong is how you show up and earn the booking when someone nearby '
  'is choosing a dermatologist.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the practice they find first', 'Catch every call your visibility brings in'),
 ('Marketing for electricians keeps your Google Business Profile active and leans your photos, posts, and '
  'local content toward the work you want more of, so you build a reputation for generator installs and show '
  'up when a homeowner searches after the power goes out. You become the name they already know to call.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get known for generators before the next outage', 'Catch every call your visibility brings in'),
 ('Estate planning clients arrive on their own schedule, not yours. Marketing that keeps your firm visible, '
  'trusted, and in front of your referral partners is how you are the one they call when the moment finally '
  'comes.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Become the name they call when they are ready', 'Catch every call your visibility brings in'),
 ('Most family law clients start with a quiet search and choose the firm that feels safe. Keeping your '
  'Google presence active and your reviews genuine is how you show up, and get chosen, when someone nearby '
  'needs help.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the firm they find, and trust', 'Catch every call your visibility brings in'),
 ('More fence customers come from showing up on Google when homeowners search, collecting reviews that make '
  'you the obvious call, and turning every visible fence into a neighbor referral. That is what fence '
  'marketing is built to do.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found, get reviewed, get referred', 'Catch every call your visibility brings in'),
 ('Most flooring jobs start with a homeowner shopping visually. Keeping your Google profile active, your '
  'galleries full of finished floors, and your reviews genuine is how you show up as the trusted local name '
  'when someone nearby starts looking.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the flooring company they can already see', 'Catch every call your visibility brings in'),
 ('Most foundation calls begin with a scared homeowner researching who to trust. Keeping your Google profile '
  'active, your reviews steady, and your answers honest is how you become the credible name they call when a '
  'crack appears nearby.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the foundation name they already trust', 'Catch every call your visibility brings in'),
 ('Showing up on the map is not luck, it is upkeep. Marketing for garage door companies keeps your Google '
  'Business Profile complete and active, pushes fresh posts and photos, and builds the steady reviews and '
  'local presence that lift you into the map pack. When a homeowner searches garage door repair near them, '
  'you are the one they see first instead of a competitor.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('The fix is <em>local marketing</em> that keeps you visible', 'Catch every call your visibility brings in'),
 ('Getting more clients means working your referrals and repeat clients while staying visible and credible '
  'where homeowners search. Marketing built for contractors keeps the warm leads warm and puts you in front '
  'of the new ones looking for a builder.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Turn your reputation into a steady stream of projects', 'Catch every call your visibility brings in'),
 ('Getting more members starts with being the active, well-reviewed name in the map pack when someone nearby '
  'decides to start, especially at the New Year, then following up so the interest turns into a sign-up.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the gym they find first', 'Catch every call your visibility brings in'),
 ('Most new salon clients start on Google, Instagram, and your reviews. Keeping your profile active, your '
  'work in front of people, and your reviews growing is how you show up when someone nearby is ready to '
  'book.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found where clients are looking', 'Catch every call your visibility brings in'),
 ('Getting more clients is about being visible and trusted where local demand shows up. Marketing keeps your '
  'Google profile active, your reviews fresh, and your name first in the neighborhoods you cover.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the handyman they already know', 'Catch every call your visibility brings in'),
 ('Marketing for home inspectors keeps you visible to the agents who send work and to buyers searching home '
  'inspector near me, through your Google Business Profile, steady reviews, and a light touch that keeps you '
  'top of mind, so the next referral is already yours. It pairs with the CRM that follows up privately with '
  'every agent and past buyer in your list.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Become the inspector agents recommend', 'Catch every call your visibility brings in'),
 ('Most cleaning clients start on Google the day they decide to hire someone. Keeping your profile active, '
  'well-reviewed, and focused on the neighborhoods you serve is how you are the name they see and trust in '
  'that moment.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the cleaner they find first', 'Catch every call your visibility brings in'),
 ('Marketing for HVAC companies keeps you visible year round, on Google and in the neighborhoods you serve, '
  'and turns your past-customer list into booked tune-ups during the slow months. A free audit finds the gap '
  'between your busy season and your quiet one.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Stay busy when the <em>weather is mild</em>', 'Catch every call your visibility brings in'),
 ('Marketing for HVAC companies works best when it is tied to the website, reviews, and follow-up that '
  'convert the attention it earns, not bought as a standalone ad budget. A free audit finds the gap between '
  'what you spend to get seen and what actually turns into booked work.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Marketing that <em>connects to the jobs</em>', 'Catch every call your visibility brings in'),
 ('Marketing for an immigration firm is being easy to find in the language people search, easy to reach when '
  'they call, and worth referring after the case. We handle the search, the profile, and the reviews that '
  'make that happen.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found, get reached, get referred', 'Catch every call your visibility brings in'),
 ('More junk removal customers come from ranking for near-me searches, a steady flow of reviews, and repeat '
  'referral accounts. Marketing that runs all three keeps the trucks full without buying leads.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found, get chosen, get called back', 'Catch every call your visibility brings in'),
 ('Most new customers start by searching for a landscaper nearby and calling a name they can see and trust. '
  'Marketing keeps your Google profile active, your reviews fresh, and your name in the map pack for the '
  'towns you cover.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the landscaper they find first', 'Catch every call your visibility brings in'),
 ('Commercial and HOA decision-makers vet your online presence before they meet you. Marketing keeps your '
  'Google profile active, your reviews recent, and your name visible in the areas those properties sit, so '
  'you make the shortlist.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the crew the board can already see', 'Catch every call your visibility brings in'),
 ('Most locksmith calls start with a search or the map pack. Keeping your Google profile verified, active, '
  'and full of recent reviews is how you show up there when someone is locked out nearby.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found the moment someone needs a locksmith', 'Catch every call your visibility brings in'),
 ('Most new massage clients start by searching and sizing you up on trust. Keeping your Google profile '
  'active, your space on show, and your reviews fresh is how you turn up first and win the booking when '
  'someone nearby is looking.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the practice they can already see', 'Catch every call your visibility brings in'),
 ('Most med spa growth starts in the map pack, in your reviews, and on Instagram, then compounds when you '
  'rebook the clients you already have. Marketing that does both is how a med spa fills the calendar and '
  'keeps it full.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Most mobile mechanic customers start on Google and come back if you stay in touch. Keeping your profile '
  'active and full of reviews, then following up with past customers, is how a come-to-you business grows.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found, and stay found', 'Catch every call your visibility brings in'),
 ('Marketing for mortgage brokers keeps you visible and trusted where borrowers and referral agents look '
  'before they ever call, your Google profile, your reviews, and a steady public presence, so when someone '
  'is ready to hand over their financial life or an agent needs a broker to recommend, your name is the one '
  'they already know. It pairs with the CRM that follows up privately with everyone in your database, and it '
  'stays compliant, never promising a rate or an approval.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the broker borrowers and agents already know', 'Catch every call your visibility brings in'),
 ('More customers come from being easy to find, easy to trust, and hard to forget. Marketing that keeps your '
  'profile ranking, your reviews growing, and your past movers coming back is how you get there.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found, get chosen, get referred', 'Catch every call your visibility brings in'),
 ('Most nail salon growth starts in the map pack, in your reviews, and on an Instagram full of your nail '
  'art, then compounds when you rebook the clients you already have. Marketing that does both is how a nail '
  'salon fills the chairs and keeps them full.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Most new patients start with a search and pick from the map pack. Marketing that keeps your profile '
  'active, your reviews growing, and your site answering the vision-plan question is how you get chosen when '
  'someone nearby needs an optometrist.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Most orthodontic patients begin with a Google search or a dentist referral. Marketing keeps your profile '
  'ranking, your reviews steady, and your referral network warm, then makes sure every consult it earns is '
  'answered and followed up.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get seen, then catch every case', 'Catch every call your visibility brings in'),
 ('Most local painting calls begin with a name a homeowner already recognizes. Keeping your Google profile '
  'active, full of real project photos, and well reviewed is how you become that name before the repaint is '
  'decided nearby.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the painter they already know', 'Catch every call your visibility brings in'),
 ('Most injury cases begin with a search, not a billboard. Keeping your Google profile active, your reviews '
  'growing, and your site ranking is how you get in front of an accident victim right when they are choosing '
  'who to call.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('More clients come from being easy to find when someone searches for a trainer nearby, and easy to start '
  'with once they do. Marketing gets you in front of the right people; the follow-up and fast replies turn '
  'that attention into consults on your calendar.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found and get booked', 'Catch every call your visibility brings in'),
 ('Most pest control leads begin in the local map pack and among the neighbors who see your truck. Keeping '
  'your Google profile active and full of recent reviews is how your name is the one a frightened homeowner '
  'calls.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found where the panic search lands', 'Catch every call your visibility brings in'),
 ('Physical therapy patients come from referring physicians and from local search at once. Staying reliable '
  'for the doctors who send patients, and easy to find and book for the ones who search, is how you keep '
  'both engines full.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the clinic they find and refer to first', 'Catch every call your visibility brings in'),
 ('Most local plumbing calls begin in the map pack. Keeping your Google profile verified, active, and full '
  'of recent reviews is how you show up there when a pipe breaks nearby.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get seen where the calls start', 'Catch every call your visibility brings in'),
 ('Most new pool customers begin in the map pack. Keeping your Google profile verified, active, and full of '
  'recent reviews is how you show up there when someone nearby needs weekly service or a pool opened.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get seen where pool customers start', 'Catch every call your visibility brings in'),
 ('Most pressure washing jobs start with a search and a glance at the map pack. Keeping your Google profile '
  'active, full of before-and-after work, and stacked with reviews is how you become the name a homeowner '
  'calls the moment they notice the dirt.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the pressure washer they can already see', 'Catch every call your visibility brings in'),
 ('Most new owner accounts start with a referral or a local search. Marketing for property management keeps '
  'your Google profile verified, active, and full of recent reviews, and keeps your name in front of the '
  'owners and landlords already in your orbit, so when someone nearby is finally fed up with their manager, '
  'yours is the company they call.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Become the manager owners find first', 'Catch every call your visibility brings in'),
 ('Marketing for real estate agents keeps you visible in a specific neighborhood and in front of your own '
  'sphere between transactions, through your Google Business Profile and consistent local content, so when '
  'someone nearby finally decides to sell, or a past client thinks of a referral, your name is already the '
  'one they reach for. It is the public-facing side of your business, and it pairs with the CRM that follows '
  'up privately with everyone already in your database.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Marketing that makes you the <em>name they know</em>', 'Catch every call your visibility brings in'),
 ('Buying leads is renting demand at the most expensive moment, against everyone else buying the same list. '
  'Marketing builds recognition you own: an active Google profile, local content, and visibility in the '
  'towns you work, so when a roof fails down the street, yours is the name the homeowner already trusts. See '
  'how it compounds instead of resetting every month.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Marketing makes you the name they <em>already know</em>', 'Catch every call your visibility brings in'),
 ('More solar leads come from being easy to find and easy to trust where homeowners research. Keeping your '
  'Google profile active, your reviews growing, and your local pages answering real questions is how you '
  'show up when someone nearby starts looking.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Become the solar name they find first', 'Catch every call your visibility brings in'),
 ('Most tire customers start with a search the instant a tire goes flat or the tread is gone. Keeping your '
  'Google profile active, well-reviewed, and first in the map pack for the towns you serve is how you are '
  'the shop they call, not the one that let its listing go stale.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get seen the moment a tire goes', 'Catch every call your visibility brings in'),
 ('Most transmission jobs begin with a driver searching nearby the moment it starts to go. Keeping your '
  'Google profile active, your reviews genuine, and your referral partners warm is how you show up when it '
  'happens.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found where the big jobs start', 'Catch every call your visibility brings in'),
 ('Most tree work goes to whoever is visible and trusted when a homeowner needs a tree handled. Marketing '
  'keeps your profile ranking, your reviews building, and your name in front of past customers before the '
  'season hits.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the crew they find and trust first', 'Catch every call your visibility brings in'),
 ('Most urgent care visits begin with a near me or open now search. Keeping your Google profile verified, '
  'active, and full of recent reviews, and reaching the employers who send screenings, is how you show up '
  'when it counts.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found the moment someone needs care', 'Catch every call your visibility brings in'),
 ('Most new-client searches begin in the map pack. Keeping your Google profile verified, active, and full of '
  'recent reviews is how a clinic shows up when an owner nearby is choosing who to call.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Get found where new clients start', 'Catch every call your visibility brings in'),
 ('Most window cleaning jobs start with a search and a glance at the map pack, and reviews decide the click. '
  'Keeping your Google profile active and stacked with recent reviews in the towns you serve is how you '
  'become the name a customer calls when the glass needs doing.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the window cleaner they can already trust', 'Catch every call your visibility brings in'),
 ('Keeping your Google profile active, your reviews steady, and your social full of real classes is how a '
  'nearby beginner finds you, trusts you, and books a first class instead of scrolling past to the studio '
  'that showed up looking current.',
  'Top Shelf handles what happens after someone finds you. An AI receptionist answers and books the call, a '
  'missed call gets a text back, each finished job sends a review request, and the CRM reminds you to follow '
  'up on every lead.'),
 ('Be the studio a beginner finds first', 'Catch every call your visibility brings in'),
 ('re:(?<=[\\s"])Marketing\\ for\\ appliance\\ repair(?=\\s*<span class="arr">|",)',
  'See Top Shelf for appliance repair'),
 ('re:(?<=[\\s"])Marketing\\ for\\ auto\\ body\\ shops(?=\\s*<span class="arr">|",)',
  'See Top Shelf for auto body shops'),
 ('re:(?<=[\\s"])Marketing\\ for\\ auto\\ detailers(?=\\s*<span class="arr">|",)',
  'See Top Shelf for auto detailers'),
 ('re:(?<=[\\s"])Marketing\\ for\\ auto\\ repair\\ shops(?=\\s*<span class="arr">|",)',
  'See Top Shelf for auto repair shops'),
 ('re:(?<=[\\s"])Marketing\\ for\\ bankruptcy\\ attorneys(?=\\s*<span class="arr">|",)',
  'See Top Shelf for bankruptcy attorneys'),
 ('re:(?<=[\\s"])Marketing\\ for\\ barbershops(?=\\s*<span class="arr">|",)',
  'See Top Shelf for barbershops'),
 ('re:(?<=[\\s"])Marketing\\ for\\ chiropractors(?=\\s*<span class="arr">|",)',
  'See Top Shelf for chiropractors'),
 ('re:(?<=[\\s"])Marketing\\ for\\ commercial\\ real\\ estate(?=\\s*<span class="arr">|",)',
  'See Top Shelf for commercial real estate'),
 ('re:(?<=[\\s"])Marketing\\ for\\ criminal\\ defense\\ lawyers(?=\\s*<span class="arr">|",)',
  'See Top Shelf for criminal defense lawyers'),
 ('re:(?<=[\\s"])Marketing\\ for\\ day\\ spas(?=\\s*<span class="arr">|",)', 'See Top Shelf for day spas'),
 ('re:(?<=[\\s"])Marketing\\ for\\ dentists(?=\\s*<span class="arr">|",)', 'See Top Shelf for dentists'),
 ('re:(?<=[\\s"])Marketing\\ for\\ dermatologists(?=\\s*<span class="arr">|",)',
  'See Top Shelf for dermatologists'),
 ('re:(?<=[\\s"])See\\ marketing\\ for\\ electricians(?=\\s*<span class="arr">|",)',
  'See Top Shelf for electricians'),
 ('re:(?<=[\\s"])Marketing\\ for\\ estate\\ planning\\ attorneys(?=\\s*<span class="arr">|",)',
  'See Top Shelf for estate planning attorneys'),
 ('re:(?<=[\\s"])Marketing\\ for\\ family\\ law\\ attorneys(?=\\s*<span class="arr">|",)',
  'See Top Shelf for family law attorneys'),
 ('re:(?<=[\\s"])Marketing\\ for\\ fence\\ companies(?=\\s*<span class="arr">|",)',
  'See Top Shelf for fence companies'),
 ('re:(?<=[\\s"])Marketing\\ for\\ flooring\\ companies(?=\\s*<span class="arr">|",)',
  'See Top Shelf for flooring companies'),
 ('re:(?<=[\\s"])Marketing\\ for\\ foundation\\ repair(?=\\s*<span class="arr">|",)',
  'See Top Shelf for foundation repair'),
 ('re:(?<=[\\s"])How\\ local\\ marketing\\ works(?=\\s*<span class="arr">|",)',
  'See Top Shelf for garage door companies'),
 ('re:(?<=[\\s"])Marketing\\ for\\ general\\ contractors(?=\\s*<span class="arr">|",)',
  'See Top Shelf for general contractors'),
 ('re:(?<=[\\s"])Marketing\\ for\\ gyms(?=\\s*<span class="arr">|",)', 'See Top Shelf for gyms'),
 ('re:(?<=[\\s"])Marketing\\ for\\ hair\\ salons(?=\\s*<span class="arr">|",)',
  'See Top Shelf for hair salons'),
 ('re:(?<=[\\s"])Marketing\\ for\\ handyman\\ services(?=\\s*<span class="arr">|",)',
  'See Top Shelf for handyman services'),
 ('re:(?<=[\\s"])Marketing\\ for\\ home\\ inspectors(?=\\s*<span class="arr">|",)',
  'See Top Shelf for home inspectors'),
 ('re:(?<=[\\s"])Marketing\\ for\\ house\\ cleaning\\ companies(?=\\s*<span class="arr">|",)',
  'See Top Shelf for house cleaning companies'),
 ('re:(?<=[\\s"])See\\ HVAC\\ marketing(?=\\s*<span class="arr">|",)', 'See Top Shelf for HVAC companies'),
 ('re:(?<=[\\s"])Marketing\\ for\\ immigration\\ lawyers(?=\\s*<span class="arr">|",)',
  'See Top Shelf for immigration lawyers'),
 ('re:(?<=[\\s"])Marketing\\ for\\ junk\\ removal(?=\\s*<span class="arr">|",)',
  'See Top Shelf for junk removal'),
 ('re:(?<=[\\s"])Marketing\\ for\\ landscapers(?=\\s*<span class="arr">|",)',
  'See Top Shelf for landscapers'),
 ('re:(?<=[\\s"])Marketing\\ for\\ locksmiths(?=\\s*<span class="arr">|",)', 'See Top Shelf for locksmiths'),
 ('re:(?<=[\\s"])Marketing\\ for\\ massage\\ therapists(?=\\s*<span class="arr">|",)',
  'See Top Shelf for massage therapists'),
 ('re:(?<=[\\s"])Marketing\\ for\\ med\\ spas(?=\\s*<span class="arr">|",)', 'See Top Shelf for med spas'),
 ('re:(?<=[\\s"])Marketing\\ for\\ mobile\\ mechanics(?=\\s*<span class="arr">|",)',
  'See Top Shelf for mobile mechanics'),
 ('re:(?<=[\\s"])Marketing\\ for\\ mortgage\\ brokers(?=\\s*<span class="arr">|",)',
  'See Top Shelf for mortgage brokers'),
 ('re:(?<=[\\s"])Marketing\\ for\\ movers(?=\\s*<span class="arr">|",)', 'See Top Shelf for movers'),
 ('re:(?<=[\\s"])Marketing\\ for\\ nail\\ salons(?=\\s*<span class="arr">|",)',
  'See Top Shelf for nail salons'),
 ('re:(?<=[\\s"])Marketing\\ for\\ optometrists(?=\\s*<span class="arr">|",)',
  'See Top Shelf for optometrists'),
 ('re:(?<=[\\s"])Marketing\\ for\\ orthodontists(?=\\s*<span class="arr">|",)',
  'See Top Shelf for orthodontists'),
 ('re:(?<=[\\s"])Marketing\\ for\\ painters(?=\\s*<span class="arr">|",)', 'See Top Shelf for painters'),
 ('re:(?<=[\\s"])Marketing\\ for\\ personal\\ injury\\ lawyers(?=\\s*<span class="arr">|",)',
  'See Top Shelf for personal injury lawyers'),
 ('re:(?<=[\\s"])Marketing\\ for\\ personal\\ trainers(?=\\s*<span class="arr">|",)',
  'See Top Shelf for personal trainers'),
 ('re:(?<=[\\s"])Marketing\\ for\\ pest\\ control\\ companies(?=\\s*<span class="arr">|",)',
  'See Top Shelf for pest control companies'),
 ('re:(?<=[\\s"])Marketing\\ for\\ physical\\ therapists(?=\\s*<span class="arr">|",)',
  'See Top Shelf for physical therapists'),
 ('re:(?<=[\\s"])Marketing\\ for\\ plumbers(?=\\s*<span class="arr">|",)', 'See Top Shelf for plumbers'),
 ('re:(?<=[\\s"])Marketing\\ for\\ pool\\ service\\ companies(?=\\s*<span class="arr">|",)',
  'See Top Shelf for pool service companies'),
 ('re:(?<=[\\s"])Marketing\\ for\\ pressure\\ washing(?=\\s*<span class="arr">|",)',
  'See Top Shelf for pressure washing'),
 ('re:(?<=[\\s"])Marketing\\ for\\ property\\ management(?=\\s*<span class="arr">|",)',
  'See Top Shelf for property management'),
 ('re:(?<=[\\s"])See\\ marketing(?=\\s*<span class="arr">|",)', 'See Top Shelf for real estate agents'),
 ('re:(?<=[\\s"])See\\ marketing\\ for\\ roofers(?=\\s*<span class="arr">|",)', 'See Top Shelf for roofers'),
 ('re:(?<=[\\s"])Marketing\\ for\\ solar\\ installers(?=\\s*<span class="arr">|",)',
  'See Top Shelf for solar installers'),
 ('re:(?<=[\\s"])Marketing\\ for\\ tire\\ shops(?=\\s*<span class="arr">|",)',
  'See Top Shelf for tire shops'),
 ('re:(?<=[\\s"])Marketing\\ for\\ transmission\\ shops(?=\\s*<span class="arr">|",)',
  'See Top Shelf for transmission shops'),
 ('re:(?<=[\\s"])Marketing\\ for\\ tree\\ services(?=\\s*<span class="arr">|",)',
  'See Top Shelf for tree services'),
 ('re:(?<=[\\s"])Marketing\\ for\\ urgent\\ care(?=\\s*<span class="arr">|",)',
  'See Top Shelf for urgent care'),
 ('re:(?<=[\\s"])Marketing\\ for\\ veterinary\\ clinics(?=\\s*<span class="arr">|",)',
  'See Top Shelf for veterinary clinics'),
 ('re:(?<=[\\s"])Marketing\\ for\\ window\\ cleaning(?=\\s*<span class="arr">|",)',
  'See Top Shelf for window cleaning'),
 ('re:(?<=[\\s"])Marketing\\ for\\ yoga\\ studios(?=\\s*<span class="arr">|",)',
  'See Top Shelf for yoga studios')]

# --- hubs, websites pages, free audit, meter/flat (generic rows last)
ROWS += [('website and local SEO</a> feed it by getting you into the map pack where a warm-fridge search actually '
  'starts and naming the brands you service so the homeowner knows they are in the right place, and your '
  'marketing keeps a steady flow of reviews and repeat work coming in all year, because appliances break '
  'every day, not in two seasons.',
  'website</a> names the brands you service so the homeowner knows they are in the right place, and every '
  'request it takes lands in the same CRM.'),
 ('website and local SEO</a> feed it by getting you into the map pack, where a person privately searches for '
  'help at midnight, ahead of the debt-relief mills paying for ads.',
  'website</a> sends the form a person fills out privately at midnight into the same place.'),
 ('website and local SEO</a> feed the whole thing by getting you found in the map pack where the calls '
  'actually start.',
  'website</a> sends its booking requests into the same place.'),
 ('website and local SEO</a> feed the whole thing by making a serious firm look serious and getting you '
  'found for your market and asset class, and your marketing keeps you visible to the owners and tenants you '
  'want to represent.',
  'website</a> makes a serious firm look serious, and every inquiry it takes lands in the same CRM.'),
 ('website and local SEO</a> feed it by getting you into the map pack, where a frightened person searches '
  'for a lawyer at midnight.',
  'website</a> sends the form a frightened person fills out at midnight into the same place.'),
 ('website and local SEO</a> feed it by getting you found where people search for a dentist near them.',
  'website</a> sends its booking requests into the same place.'),
 ('website and local SEO</a> get you found for the conditions and treatments you offer nearby.',
  'website</a> lists the conditions and treatments you offer and sends its booking requests into the same '
  'place.'),
 ('website and local SEO</a> feed the whole thing by getting you found when a homeowner searches for an '
  'electrician near them, and your marketing keeps your profile active and points demand toward the panel '
  'and generator work you actually want more of.',
  'website</a> puts the panel and generator work you want more of up front, and every request it takes lands '
  'in the same CRM.'),
 ('website and local SEO</a> feed it by getting you found when someone finally searches for an estate '
  'planning attorney nearby, with the genuine reviews that reassure a cautious, often older client.',
  'website</a> shows the genuine reviews that reassure a cautious, often older client and sends every '
  'inquiry into the same place.'),
 ('website and local SEO</a> feed it by getting you into the map pack, where someone quietly searches for a '
  'family law attorney late at night.',
  'website</a> sends the form someone fills out quietly late at night into the same place.'),
 ('website and local SEO</a> feed it by showing your wood, vinyl, aluminum, and chain-link work and ranking '
  'for the fence searches homeowners actually make, and your marketing turns the most visible thing you '
  'build, a clean run on the property line, into neighbor referrals and a steady flow of reviews.',
  'website</a> shows your wood, vinyl, aluminum, and chain-link work, and every quote request it takes lands '
  'in the same CRM.'),
 ('website and local SEO</a> feed it with galleries of real finished rooms and rankings for the floors and '
  'towns homeowners search, because floors get shortlisted with the eyes before anyone calls, and your '
  'marketing turns every finished floor into the photos and honest reviews a careful buyer wants.',
  'website</a> shows galleries of real finished rooms, because floors get shortlisted with the eyes before '
  'anyone calls, and every measure request it takes lands in the same CRM.'),
 ('website and local SEO</a> feed it by making a scared midnight searcher trust you before they call, with '
  'your credentials, your process from free inspection to engineered estimate, your transferable warranty, '
  'and before-and-after photos of real jobs, then ranking for the towns you serve, and your marketing builds '
  'the steady, genuine reviews and honest, non-alarmist answers that make you the straight shooter a wary '
  'homeowner calls first.',
  "website</a> earns a scared midnight searcher's trust before they call, with your credentials, your "
  'process from free inspection to engineered estimate, your transferable warranty, and before-and-after '
  'photos of real jobs.'),
 ('website and local SEO</a> feed it with a portfolio of finished kitchens, additions, and whole-home '
  'renovations, proof you are licensed and insured, and rankings for the towns you build in, and your '
  'marketing keeps the reviews building and the word-of-mouth engine turning, because most remodels are '
  'still won on trust.',
  'website</a> shows a portfolio of finished kitchens, additions, and whole-home renovations and proof you '
  'are licensed and insured, because most remodels are still won on trust.'),
 ('website and local SEO</a> feed the whole thing by ranking for home inspector near me and the towns you '
  'cover, so a buyer under a deadline finds you and books, and your marketing keeps you in front of the '
  'agents who send the steady work.',
  'website</a> lets a buyer under a deadline book you in one tap, and that booking lands in the same CRM.'),
 ('website and local SEO</a> feed it by getting you into the map pack and speaking to visitors in the '
  'language they searched in.',
  'website</a> speaks to visitors in the language they searched in.'),
 ('website and local SEO</a> feed it with a photo-for-a-quote path, an obvious same-day booking option, and '
  'rankings for junk removal near me, and your marketing builds the recent reviews that win the map pack and '
  'the repeat referral accounts, realtors, property managers, and movers, that keep a truck busy without '
  'buying leads.',
  'website</a> feeds it with a photo-for-a-quote path and an obvious same-day booking option.'),
 ('website and local SEO</a> feed it by putting a tap-to-call button in front of a stranded searcher and '
  'ranking for locksmith near me and 24 hour locksmith, and your marketing builds the recent reviews and the '
  'visible licensed, insured, and bonded trust signals a security purchase leans on harder than almost any '
  'trade.',
  'website</a> puts a tap-to-call button in front of a stranded searcher and shows the licensed, insured, '
  'and bonded trust signals a security purchase leans on harder than almost any trade.'),
 ('website and local SEO</a> get you ranking for the treatments and towns you serve.',
  'website</a> lists the treatments you offer and sends its consult requests into the same place.'),
 ('website and local SEO</a> feed the whole thing by ranking for a mortgage broker near me and earning the '
  'trust a borrower needs before sharing their financial life, and your marketing keeps you visible to the '
  'agents and past clients who send the steadiest business.',
  'website</a> earns the trust a borrower needs before sharing their financial life, and every inquiry it '
  'takes lands in the same CRM.'),
 ('website and local SEO</a> put your reviews and your license front and center the moment someone searches '
  'for a mover near them.',
  'website</a> puts your reviews and your license front and center.'),
 ('website and local SEO</a> merchandise the optical and get you found where people search.',
  'website</a> merchandises the optical and sends its exam requests into the same place.'),
 ('website and local SEO</a> get you ranking for braces, Invisalign, and orthodontist near me in the towns '
  'you serve.',
  'website</a> sends its consult requests into the same place.'),
 ('website and local SEO</a> feed the whole thing by getting you into the map pack, where an injury search '
  'actually starts, ahead of firms with far bigger ad budgets.',
  'website</a> sends every intake form into the same place.'),
 ('website and local SEO</a> feed the whole thing by ranking a page for every pest and town you cover, so a '
  'bed bug or termite search finds you in the map pack, and your marketing keeps that pipeline full.',
  'website</a> sends every service request into the same CRM.'),
 ('website and local SEO</a> get you found by the direct-access patients searching nearby.',
  'website</a> lets a direct-access patient book an evaluation in one tap.'),
 ('website and local SEO</a> feed the whole thing by getting you found in the map pack where the calls '
  'actually start, and your marketing keeps the pipeline full.',
  'website</a> puts a tap-to-call button up front and sends every request into the same CRM.'),
 ('website and local SEO</a> get you found for pool service near me, where the next route customer starts.',
  "website</a> sends the next route customer's request into the same place."),
 ('website and local SEO</a> put your before-and-after work and a quick quote request in front of the person '
  'searching for pressure washing near them.',
  'website</a> puts your before-and-after work and a quick quote request in front of every visitor.'),
 ('website and local SEO</a> feed the whole thing by ranking for property management company near me and '
  'giving owners a path to a proposal and tenants a path to apply, and your marketing keeps your Google '
  'profile active and your name in front of the owners already in your orbit.',
  'website</a> gives owners a path to a proposal and tenants a path to apply.'),
 ('website and local SEO</a> rank for your name and your neighborhoods so a buyer becomes your own contact '
  'instead of a portal lead, your marketing keeps you the name a neighborhood recognizes, and',
  'website</a> turns a buyer into your own contact instead of a portal lead, and'),
 ("website and local SEO</a> earn a cautious homeowner's trust and get you found for solar installers near "
  'them, so more of the pipeline is yours instead of rented.',
  "website</a> earns a cautious homeowner's trust, so more of the pipeline is yours instead of rented."),
 ('website and local SEO</a> prove you are licensed and insured and get you found for tree removal near me, '
  'which is the first thing a nervous homeowner checks before letting a saw into a tree over their house.',
  'website</a> proves you are licensed and insured, which is the first thing a nervous homeowner checks '
  'before letting a saw into a tree over their house.'),
 ('website and local SEO</a> get you found for near-me and open-now searches with accurate hours.',
  'website</a> shows accurate hours to every patient who checks.'),
 ('website and local SEO</a> get you found in the map pack where new clients start.',
  'website</a> sends new-client requests into the same place.'),
 ('website and local SEO</a> get you found for window cleaning near me and put the reviews that sell this '
  'trade front and center, because clean glass barely reads in a photo.',
  'website</a> puts the reviews that sell this trade front and center, because clean glass barely reads in a '
  'photo.'),
 ('website and SEO</a> get you into the map pack when a homeowner searches garage door repair near them, '
  'which is where most of these calls actually start, and your marketing keeps that profile active and full '
  'of finished-door photos so you are the name they see first.',
  'website</a> shows your finished doors and sends every request into the same CRM.'),
 ('website and SEO</a> list the dozens of small jobs you really do, so a visitor spots their own task and '
  'finds you nearby, and your marketing keeps you the recognized name a neighborhood already trusts.',
  'website</a> lists the dozens of small jobs you really do, so a visitor spots their own task.'),
 ('website and SEO</a> get you found in the neighborhoods you already serve, so your routes stay tight, and '
  'your marketing keeps you the trusted, well-reviewed name in the map pack.',
  'website</a> names the neighborhoods you already serve, so your routes stay tight.'),
 ('website and SEO</a> get you found when a homeowner searches for AC or furnace help nearby, and your '
  'marketing keeps you visible through the mild shoulder months so the phone is not silent between seasons.',
  'website</a> sends every AC and furnace request into the same CRM.'),
 ('website and SEO</a> put a page in front of each town you serve and rank for a landscaper near me, and '
  'your marketing keeps the profile a cautious HOA board reads before it calls.',
  'website</a> shows the work a cautious HOA board wants to see before it calls.'),
 ('website and SEO</a> rank you for the towns you cover and show the real before-and-after work that sells '
  'painting on sight, and your marketing makes you the familiar name a homeowner already trusts before the '
  'repaint they put off finally becomes this weekend.',
  'website</a> shows the real before-and-after work that sells painting on sight.'),
 ('website and SEO</a> get you found instead of a lead directory that resells the same call, and your '
  'marketing keeps you familiar in the towns you work, so you are not bidding cold at the most expensive '
  'moment.',
  'website</a> brings in calls that are yours instead of a lead directory that resells the same call.'),
 ('Your marketing and local SEO feed the whole thing by getting you into the map pack where drivers look '
  'right after a wreck.',
  'Your website sends every estimate request into the same CRM.'),
 ('Your marketing and local SEO keep you in the map pack, where a driver deciding whom to trust with an '
  'expensive machine leans on your reviews.',
  'Review requests keep fresh reviews coming in, which a driver deciding whom to trust with an expensive '
  'machine leans on.'),
 ('With no walk in traffic, your Google profile and your website are the storefront, and Top Shelf builds '
  'and ranks both so drivers searching for a mobile mechanic nearby find you.',
  'With no walk in traffic, your Google profile and your website are the storefront, and a Top Shelf website '
  'is built so Google can read it.'),
 ('SEO that gets you found', 'a website built so Google can read it'),
 ('plus websites, SEO, and reviews.', 'plus reviews and a professional website.'),
 ('plus websites and SEO.', 'plus a professional website.'),
 ('and a site built to look credible and rank.', 'and a site built to look credible.'),
 ('a site built to rank.', 'a site built so Google can read it.'),
 ('a site that ranks.', 'a site built so Google can read it.'),
 ('and a ranking site.', 'and a site built so Google can read it.'),
 ('Software and Marketing Built for', 'Software and Websites Built for'),
 ('re:(?<=oftware) and marketing(?= for| in one platform)', ' and websites'),
 ('answering, follow-up, booking, and marketing usually live',
  'answering, follow-up, booking, and reviews usually live'),
 ('answering, follow-up, and marketing', 'answering, follow-up, and reviews'),
 ('answering, rebooking, and marketing', 'answering, rebooking, and reviews'),
 ('Top Shelf puts the answering, the follow-up, and the marketing in one place',
  'Top Shelf puts the answering, the follow-up, and the reviews in one place'),
 ('re:,? (?:and|while) steady local marketing [^.<"]*', ''),
 ('re:\\s*Your marketing (?:keeps|builds|makes|runs)[^.<"]*\\.', ''),
 ('It depends on how much you want handled for you. The Signature plan is $99 a month for up to 10 users and '
  'includes the AI receptionist and the CRM that run intake and follow-up. The Signature plan is $99 a month '
  'for up to 10 users, and a professional website is $499 one time.',
  'The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM that '
  'run intake and follow-up. A professional website is $499 one time.'),
 ('It depends on how much you want handled for you. The Signature plan is $99 a month for up to 10 users and '
  'includes the AI receptionist and the CRM. The Signature plan is $99 a month for up to 10 users, and a '
  'professional website is $499 one time.',
  'The Signature plan is $99 a month for up to 10 users and includes the AI receptionist and the CRM. A '
  'professional website is $499 one time.'),
 (', which is what garage door marketing keeps running for you', ''),
 ('re:,? (?:and )?shows up in the map pack for the (?:towns|areas|neighborhoods) you (?:cover|serve)', ''),
 ('re:\\s*We build (?:pages for your core|those pages first)[^.<"]*then expand[^.<"]*\\.', ''),
 ('We build it to rank in your service area and capture every visitor, then hand each lead off to follow-up.',
  'We build it so Google can read it and so it captures every visitor, then hand each lead off to '
  'follow-up.'),
 ('An audit will lay out every search your area is running that your site does not turn up for yet.', ''),
 ('Websites &amp; SEO for', 'Websites for'),
 ('Websites & SEO for', 'Websites for'),
 ('Websites and SEO for', 'Websites for'),
 ('See websites and SEO for', 'See websites for'),
 ('re:See websites (?:and|&amp;|&) SEO(?= <|")', 'See websites'),
 ('How websites and SEO work', 'How our websites work'),
 ('Book your free audit call', 'Book a call'),
 ('Get a free audit of your setup. We will show you what you actually own today, what a clean switch would '
  'look like, and how much you could keep instead of losing, whether you work with us or not.',
  'Try the CRM and see what a clean switch would look like.'),
 ('If in-text payments are a must-have for you, say so in your free audit and we will give you a straight '
  'answer on fit rather than overpromising.',
  ''),
 ('A free audit shows you exactly where calls, leads, and reviews are getting missed today, and you can '
  'judge for yourself whether one all-in-one setup or a focused tool like Podium is the better answer.',
  'You can judge for yourself whether one all-in-one setup or a focused tool like Podium is the better '
  'answer.'),
 ('It starts with a free audit that shows you exactly where you stand and what the move would involve, '
  'whether you hire us or not.',
  ''),
 (' or start with a free audit that shows where jobs are slipping', ''),
 ('re:(?:Get|See) a free audit (?:of|that)[^.<"]*?, (?:with [^.<"]*?)?whether you (?:work with us|hire us) '
  'or not\\.',
  'Try the CRM and see how it answers calls, books jobs, and follows up on every lead.'),
 ('re:(?:Either way, )?[Ss]tart with a free audit[^.<"]*\\.', ''),
 ('re:A free audit (?:is|shows|can|will|finds)[^.<"]*\\.', ''),
 ('re:The most honest starting point is a free audit[^.<"]*\\.', ''),
 ('re:,? which is (?:exactly )?what (?:a|the) free audit (?:shows you|looks at|is for|will show you)(?:, '
  'whether you work with us or not)?(?=[.,])',
  ''),
 ('re:,? which a free audit will show you(?=\\.)', ''),
 ('re:,? (?:but|and|though|then|so) (?:a|the) free audit [^.<"]*(?=\\.)', ''),
 ('re:(?<=[a-z]) without the meter(?=<|")', ', day or night'),
 ('A live service that bills per call or per minute climbs exactly when you are busiest, while the AI '
  'receptionist is a flat part of your plan with no meter and no after-hours surcharge.',
  'A live service that bills per call or per minute climbs exactly when you are busiest. The AI receptionist '
  'is part of the Signature plan with no after-hours surcharge. Each phone line is $50 a month and covers '
  'normal use.'),
 ('An AI receptionist answers on the first ring, day or night, for a flat monthly fee with no per-call '
  'meter.',
  'An AI receptionist answers on the first ring, day or night, as part of a monthly plan. Each phone line is '
  '$50 a month and covers normal use.'),
 ('re:There is no setup fee on any of it, and (?:there is )?no per-call meter, so [^.<"]*\\.',
  'There is no setup fee on any of it. Each phone line is $50 a month and covers normal use.'),
 (', and never runs a meter, all on a flat monthly plan', ', all on a monthly plan'),
 ('A metered service bills you hardest during the storm week when the calls flood in, while the Signature '
  'plan stays $99 a month for up to 10 users.',
  'A metered service bills you hardest during the storm week when the calls flood in, while the Signature '
  'plan is $99 a month for up to 10 users. Each phone line is $50 a month and covers normal use.'),
 ("Top Shelf's AI receptionist is a flat part of the Signature plan at $99 a month for up to 10 users, so "
  'the cost does not climb with your call volume.',
  "Top Shelf's AI receptionist is part of the Signature plan at $99 a month for up to 10 users. Each phone "
  'line is $50 a month and covers normal use.'),
 ('It is a flat part of the Signature plan at $99 a month for up to 10 users with no benefits,',
  'It is part of the Signature plan at $99 a month for up to 10 users, with no benefits,'),
 ('in the Signature plan at $99 a month for up to 10 users flat, no per-call fee.',
  'in the Signature plan at $99 a month for up to 10 users.'),
 ('around the clock, flat, in the Signature plan', 'around the clock in the Signature plan'),
 (', predictably and at a flat price', ''),
 ('for a flat monthly fee that does not climb with call volume or add a surcharge on a holiday weekend.',
  'as part of a monthly plan, with no surcharge on a holiday weekend.'),
 ('There is no setup fee, and no per-call charge on the receptionist.',
  'There is no setup fee. Each phone line is $50 a month and covers normal use.'),
 ('all on the flat Signature plan with nothing climbing as the calls pile up.', 'all on the Signature plan.'),
 ('all on the flat plan with nothing climbing as the calls pile up.', 'all on the Signature plan.'),
 ('with no per-call fee or after-hours surcharge.', 'with no after-hours surcharge.'),
 ('The flat price is the point, so a great month does not turn into a big bill.', ''),
 ('A flat plan is what makes the busy season profitable instead of expensive.', ''),
 ('with no after-hours surcharge and no overage for a heavy month', 'with no after-hours surcharge'),
 ('with no after-hours surcharge or overage', 'with no after-hours surcharge'),
 ('with no after-hours or overage surcharge', 'with no after-hours surcharge'),
 ('with no surcharge and no overage', 'with no surcharge'),
 ('with no surcharge or overage', 'with no surcharge'),
 (', all on a flat monthly plan', ', all on a monthly plan'),
 (', all as one flat part of your plan', ', all as part of your plan'),
 ('at a flat monthly rate', 'on a monthly plan'),
 ('The Signature plan is one flat monthly rate', 'The Signature plan is one monthly rate'),
 ('one flat monthly bill', 'one monthly bill'),
 ('one flat bill', 'one bill'),
 ('on a flat bill', 'on one bill')]

# --- cleanup: a phone-line sentence added where one already followed, and the old flat-plan question
ROWS += [
    (r're:normal use\.\s+Each phone line is \$50 a month and covers normal use\.', 'normal use.'),
    ('Is a flat plan really cheaper than paying per call?', 'Is a monthly plan really cheaper than paying per call?'),
]

# --- audit-style promises left under "Try the CRM", the booking page, and a few leftovers
TRY = "Try the CRM and see how it answers calls, books jobs, and follows up on every lead."
ROWS += [
    ("We will show you exactly where calls, leads, and jobs are slipping away, whether you work with us or not.", TRY),
    ("See what your current setup is missing, whether you work with us or not.", TRY),
    ("We'll walk through where your business is losing money and what fixing it is worth, whether you work with us or not.",
     "We'll show you the CRM and answer your questions about the Signature plan and the $499 website."),
    ("Pick a day and time, and we will walk through where your business is losing money and how to fix it.",
     "Pick a day and time, and we will show you the CRM and answer your questions."),
    ("We Talk Through Your Numbers", "We Show You the CRM"),
    ("Your calls, reviews, Google ranking, follow-up, we show you where the gap is and what it's costing you, in plain English.",
     "We walk you through the CRM, the AI receptionist and the website, and answer your questions in plain English."),
    ("You leave with real numbers and a clear next step. Work with us or don't, the plan is yours to keep either way.",
     "You leave knowing what the plan includes and what it costs. Sign up or don't, it is your call."),
    ("You keep the numbers we find whether you hire us or not.", ""),
    ("We do the digging before we talk.", ""),
    ("Websites &amp; SEO <em>for", "Websites <em>for"),
    ("Top Shelf runs those pieces together on one platform", "Top Shelf puts the phone, booking, review requests, and follow-up on one platform"),
]

# --- remaining "flat" claims about the receptionist
ROWS += [
    ("and the flat plan that catches it", "and the plan that catches it"),
    ("for up to 10 users flat", "for up to 10 users"),
    ("Is a flat plan cheaper than a live service that bills per call?", "Is a monthly plan cheaper than a live service that bills per call?"),
    ("answers 24/7 at a flat rate", "answers 24/7 on a monthly plan"),
    ("consistent, flat-rate booking that never goes on hold", "consistent booking that never goes on hold"),
    ("books it at a flat rate usually wins", "books it usually wins"),
    ("The plans are flat and clear.", "The pricing is plain."),
    ("See how many calls a flat-rate receptionist would", "See how many calls an AI receptionist would"),
    ("One flat-rate receptionist, plus the follow-up behind it", "One AI receptionist, plus the follow-up behind it"),
]

# A replacement whose key has no apostrophe gets a raw ' from focus_reprice, which ends a
# single-quoted string in a spec file. Use a typographic apostrophe there instead.
ROWS = [(o, n.replace("'", "\u2019") if "'" in n and "'" not in o else n) for o, n in ROWS]
