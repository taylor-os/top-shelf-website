"""Reprice the copy to the Signature plan and the $499 website. Re-runnable.

Applied to the built pages AND the generator sources (spec files), so a
regenerated page carries the new copy. Rows are (regex, replacement); an empty
replacement deletes the sentence and the space before it.
"""
import re

import focus_agency
import focus_catalog as cat

SIG = "$99 a month for up to 10 users"
SITE = "a professional website is $499 one time"

R = [
    # Essentials / Platinum lines: gone
    (r"\s*Essentials is \$299 a month, Signature is \$899, and Platinum is \$2,500 by application, with no setup fee, nothing up front, and month to month so you can cancel anytime\.",
     " The Signature plan is %s and $199 a month for 11 to 25 users, with no setup fee and nothing up front, month to month." % SIG),
    (r"\s*(?:The )?Essentials(?: plan)? is \$299 a month (?:and covers|for) website upkeep, local SEO, online booking, and reviews\.", ""),
    (r"\s*With no website, Get Found is \$795\.", ""),
    (r"\s*With a poor website and a weak Google listing, Get Found Plus is \$1,995 and includes a new 5-page website\.", ""),
    (r"\s*If your website is fine, Get Found: Listing \+ Reviews is \$500\.", ""),
    (r" on the Essentials Plan", ""),
    # Signature at $899
    (r"The Signature plan is \$899 a month and adds the AI receptionist and CRM( that [^.]*)?\.",
     lambda m: "The Signature plan is %s and includes the AI receptionist and the CRM%s." % (SIG, m.group(1) or "")),
    (r"The Signature plan at \$899 a month adds the AI receptionist and the CRM( that [^.]*)\.",
     lambda m: "The Signature plan, %s, includes the AI receptionist and the CRM%s." % (SIG, m.group(1))),
    (r"Top Shelf includes it in the Signature plan at \$899 a month\.",
     "Top Shelf includes it in the Signature plan, %s." % SIG),
    (r"It comes in the Signature plan at \$899 a month, with no setup fee, alongside the phone and follow-up that feed it\.",
     "It comes in the Signature plan at %s, with no setup fee, alongside the phone and follow-up that feed it." % SIG),
    (r"(It comes in|It is included in) the Signature plan, flat, at \$899 a month, with no per-call or per-minute meter(?: running)?\.",
     lambda m: "%s the Signature plan at %s. Each phone line is $50 a month and covers normal use." % (m.group(1), SIG)),
    (r"Signature plan · \$899/mo", "Signature plan · from $99/mo"),
    # done-for-you $2,500 lines
    (r"A fully done-for-you plan runs \$2,500 a month, or you can buy a custom five[ -]page site outright for \$1,500 one[- ]time with no plan at all\.",
     "A professional website is $499 one time, and you do not need a plan to buy one."),
    (r"A done-for-you plan is \$2,500 a month, or a one-time custom (?:five page )?site is \$1,500\.",
     "The Signature plan is %s, and %s." % (SIG, SITE)),
    # $1,500 site lines
    (r"If you buy the one-time \$1,500 site,? it is yours to keep\.", "If you buy the $499 website, it is yours to keep."),
    (r"The one-time \$1,500 site is yours to keep\.", "The $499 website is yours to keep."),
    (r"The site is a one-time \$1,500 build, and it is yours to keep\.", "The website is $499 one time, and it is yours to keep."),
    (r"A (?:custom )?(?:five page )?site(?: on its own)? is \$1,500 one-time, yours to keep, with no plan and no commitment\.",
     "A professional website on its own is $499 one time, yours to keep, with no plan and no commitment."),
    (r"Top Shelf builds (?:one|a custom (?:five page )?site) for \$1,500 one-time(?:, and you own it| and you own it)?\.",
     "Top Shelf builds a professional website for $499 one time, and you own it."),
    (r"Top Shelf builds a custom (?:five page )?site for \$1,500 one-time, and no monthly plan is needed to buy one\.",
     "Top Shelf builds a professional website for $499 one time, and no plan is needed to buy one."),
    # $299 "optional plan" lines
    (r"A monthly plan starting at \$299 is optional\.", "The Signature plan, from $99 a month, is optional."),
    (r"A monthly plan is optional and starts at \$299 a month, where the ongoing SEO that (?:actually )?gets it (?:ranking|found) is handled for you(, and there is no setup fee either way)?\.",
     lambda m: "The Signature plan is optional and starts at $99 a month%s." % (", and there is no setup fee either way" if m.group(1) else "")),
    (r"Or add a monthly plan starting at \$299 to keep it working, where the ongoing SEO that actually gets it ranking is handled for you\.",
     "Add the Signature plan, from $99 a month, to run your calls, follow-up and reviews from one app."),
    # --- second pass rows (census after pass 1)
    (r'<p class="[^"]*plan"><span class="owner-plan-lead">on the</span> <span class="owner-plan-name">Essentials Plan</span></p>', ""),
    (r"Signature (plan )?(?:&middot;|·) \$899/mo", lambda m: "Signature %s&middot; from $99/mo" % (m.group(1) or "")),
    (r"\(\$299/\$899/\$2,500(?: monthly)?\s+plans,\s+\$1,500\s+one-time\s+site\)", "($99/$199 Signature plan, $499 website)"),
    (r"Top Shelf builds yours for \$1,500 one-time(, and you own it)?\.", "Top Shelf builds yours for $499 one time, and you own it."),
    (r"Essentials is \$299 a month(?:, Signature is \$899 a month, and Platinum is \$2,500 a month by application| and Signature is \$899 a month)\.",
     "The Signature plan is %s." % SIG),
    (r"\s*Essentials is \$299 a month for website upkeep, local SEO, reviews, and marketing\.", ""),
    (r"A website is a one-time build that you own: a custom 5-page site is \$1,500\.", "A website is a one-time build that you own: a professional website is $499."),
    (r"Or add a monthly plan starting at \$299 to keep it working, where the ongoing SEO that gets it ranking is handled for you\.",
     "Add the Signature plan, from $99 a month, to run your calls, follow-up and reviews from one app."),
    (r"Signature plan,? flat,? at \$899 a month,? with no per-call or per-minute meter running,", "Signature plan at %s," % SIG),
    (r"Signature plan at \$899 a month(?:,? flat)?,? with no (?:separate )?per[- ]call(?: or per-minute)? (?:fee|meter(?: running)?|charge)", "Signature plan at %s" % SIG),
    (r"Signature plan at \$899 a month,? flat,? with no per[- ]call fee", "Signature plan at %s" % SIG),
    (r"(?:Top Shelf's )?Signature plan at \$899/mo", lambda m: m.group(0).replace("$899/mo", "$99/mo for up to 10 users")),
    (r"\$899/mo Signature", "$99/mo Signature"),
    (r"Signature plan at \$899 a month", "Signature plan at %s" % SIG),
]
COMPILED = [(re.compile(p), r) for p, r in R]

# --- Exact-sentence rows (Task 4, pass 3). Each old sentence -> its new copy.
# Whitespace in a key matches any run of whitespace (line breaks in sources),
# and an apostrophe matches ' / &#x27; / &rsquo; / \' (the match's own form is
# reused). An empty replacement deletes the sentence and one side's whitespace.
# A key starting "re:" is a raw regex. Longer, more specific rows come first.
W = "$99 a month for up to 10 users"
PHONE = "Each phone line is $50 a month and covers normal use."
SENTENCES = [
    # buttons and aside card in the generator shells
    ('Get Your Free Audit <span', 'Try the CRM <span'),
    ('Get a Free Audit <span', 'Try the CRM <span'),
    ('<h3>Free business audit</h3>', '<h3>Try the CRM</h3>'),
    ('ok = {"$299", "$899", "$2,500", "$1,500"}', 'ok = {"$99", "$199", "$50", "$499"}'),

    # honesty notes in spec/generator docstrings
    ("only the real Top Shelf prices ($299 and $899 monthly plans, $1,500 one-time site) ever appear, the Signature plan at $899 carries the CRM and the AI receptionist,",
     "only the real Top Shelf prices ($99/$199 Signature plan, $50 per phone line, $499 website) ever appear, the Signature plan carries the CRM and the AI receptionist,"),
    ("the ONLY prices that ever appear are the real ones (Essentials $299, Signature $899, Platinum $2,500, and the $1,500 one-time standalone site); the CRM and AI receptionist are the $899 Signature plan, never the $299 tier.",
     "the ONLY prices that ever appear are the real ones ($99/$199 Signature plan, $50 per phone line, $499 website); the CRM and AI receptionist are in the Signature plan."),
    ("only Top Shelf's real published prices ever appear ($299 plans, $899 Signature with CRM + AI, $1,500 one-time site);",
     "only Top Shelf's real published prices ever appear ($99/$199 Signature plan with CRM + AI, $50 per phone line, $499 website);"),
    ("with the CRM and AI receptionist bundled in the $899 Signature plan;", "with the CRM and AI receptionist bundled in the Signature plan;"),
    ("and CRM + AI receptionist both live in the $899 Signature plan;", "and CRM + AI receptionist both live in the Signature plan;"),
    ("Prices are limited to Top Shelf's real ladder; only the Essentials entry ($299/mo, which includes the website) is cited, and only where it is true.",
     "Prices are limited to Top Shelf's real ones ($99/$199 Signature plan, $499 website), cited only where true."),
    ("(the $1,500 one-time site and the $299/$899/$2,500 monthly plans, CRM+AI in the $899 Signature)",
     "(the $499 website and the $99/$199 Signature plan with CRM+AI, $50 per phone line)"),
    ("($299/$899/$2,500 plans, $1,500 one-time site, CRM + AI = the $899 Signature plan)",
     "($99/$199 Signature plan with CRM + AI, $50 per phone line, $499 website)"),
    ("($299 / $899 / $2,500 monthly plans, $1,500 one-time standalone site)", "($99/$199 Signature plan, $50 per phone line, $499 website)"),
    ("($299/$899/$2,500 monthly plans, $1,500 one-time site)", "($99/$199 Signature plan, $50 per phone line, $499 website)"),
    ("($299 and $899 monthly plans, $1,500 one-time site)", "($99/$199 Signature plan, $50 per phone line, $499 website)"),
    ("($299/$899 plans, $1,500 one-time site)", "($99/$199 Signature plan, $50 per phone line, $499 website)"),
    ("($299 / $899 / $2,500 / $1,500)", "($99/$199 Signature plan, $50 per phone line, $499 website)"),
    ("($299/$899/$2,500/$1,500)", "($99/$199 Signature plan, $50 per phone line, $499 website)"),
    ("($899 Signature is the plan that carries review generation)", "(the $99/$199 Signature plan carries review generation)"),
    ("(source of truth): Essentials plan is $299/mo and includes the website; Signature plan is $899/mo and is where the CRM and the AI receptionist actually live; a standalone 5-page site is $1,500 one-time. (The $2,500 figure is the Platinum monthly plan, not a website build price, so the website-cost page uses the real $1,500 one-time / free-on-plan-from-$299 framing.)",
     "(source of truth): the Signature plan is $99/mo for up to 10 users and $199/mo for 11 to 25, and is where the CRM and the AI receptionist live; the website is $499 one time and is not part of the plan."),

    # cost-to-modernize (colony_specs_category): the old price ladder, rewritten whole
    ("Getting a local business online costs a one-time $1,500 for a website, or $299 to $2,500 a month managed. Here is the honest ladder of what each level buys.",
     "A professional website from Top Shelf is $499 one time, and the Signature plan is $99 a month for up to 10 users. Here is what each one buys."),
    ("Getting a local business online costs a one-time $1,500 for a website, or $299 to $2,500 a month managed.",
     "A professional website from Top Shelf is $499 one time, and the Signature plan is $99 a month for up to 10 users."),
    ("A custom website is $1,500 one-time. A managed monthly setup that also gets you found, answers the phone, and follows up runs from $299 to $2,500 a month, depending on how much you want handled for you.",
     "A professional website is $499 one time. The Signature plan, which answers the phone, books jobs, and follows up, is $99 a month for up to 10 users and $199 a month for 11 to 25."),
    ("The honest cost <em>ladder</em>", "What each piece <em>costs</em>"),
    ("Getting set up online is not one price, it is a ladder, and where you land depends on how much you want handled for you. Here is the real ladder at Top Shelf, with no setup fee on any of it.",
     "There are two things to buy, and you can buy either one on its own. Neither has a setup fee."),
    ("<li>A custom five-page website on its own is $1,500 one-time, yours to keep, with no plan attached.</li><li>Essentials at $299 a month keeps your website current (specials, inventory changes and SEO updates), and includes Google Business Profile optimization, basic SEO, online booking, automated review requests, and missed-call text-back.</li><li>Signature at $899 a month adds the full CRM, an AI receptionist that answers 24/7 and books the job, advanced SEO every month, customer reactivation, specials sent to your customer list by email and text, and review responses written for you.</li><li>Platinum at $2,500 a month adds managed ads, social media, and Google Business Profile posts.</li>",
     "<li>A professional website is $499 one time and yours to keep. It comes with a mobile-friendly custom design, a build Google can read, a contact and booking form that feeds the CRM, and a logo if you need one.</li><li>The Signature plan is $99 a month for up to 10 users and $199 a month for 11 to 25. It includes the CRM, an AI receptionist that answers and books jobs, missed-call text-back, online booking, a dispatch board, a customer hub, invoices by text, review requests and replies, on-my-way texts, estimates, card payments, and an AI chatbot for the website you already have.</li><li>Each phone line is $50 a month and covers normal use. Usage above that is billed.</li>"),
    ("One thing worth saying plainly, because it is easy to assume otherwise: the CRM and the AI receptionist are part of Signature at $899, not the $299 tier. Essentials gets you online and capturing calls, and Signature is where the system starts following up and answering the phone for you.",
     "One thing worth saying plainly: the website is not part of the Signature plan. If you already have a site you like, keep it, and the plan adds the AI chatbot to it."),
    ("The number moves for one reason: how much of the work is done for you, and whether you are buying a one-time build or an ongoing system. A website on its own is a fixed, one-time cost, a strong first impression that then sits there. The monthly plans are the opposite, a system that keeps working, ranking you, answering calls, and chasing leads month after month.",
     "The number moves for two reasons: whether you need a new website, and how many people on your team use the CRM. The website is a fixed, one-time cost. The plan is monthly and runs month to month, answering calls and chasing leads for as long as you keep it."),
    ("A couple of honest notes on the edges. The only pass-through cost is telecom, the phone numbers and text messages billed at cost, the same everywhere in the industry. On Platinum your ad budget goes straight to Google or Meta and you set it, so it never runs through us. Beyond that there are no setup fees and no surprise line items. The fastest way to know which rung you actually need is a free audit of your real numbers, which often shows the cheapest fix is the one you were overlooking.",
     "A couple of honest notes on the edges. Phone lines are $50 a month each and cover normal use, and usage above that is billed. Over 25 users, call us for pricing. Beyond that there are no setup fees and no surprise line items."),
    ("See exactly what each plan includes", "See exactly what the plan includes"),
    ("The honest ladder runs from a one-time $1,500 website to $299, $899, and $2,500 a month depending on how much you want run for you. The pricing page lays out every plan line by line, with no setup fee and nothing hidden.",
     "The website is $499 one time and the Signature plan starts at $99 a month. The pricing page lists everything in the plan line by line, with no setup fee and nothing hidden."),
    ("Up front, yes. A standalone site is $1,500 once, while the plans are monthly. But a site on its own does not get you found or answer your phone. The monthly plans do not include a website build. They add the system that actually brings in calls. It comes down to whether you need a website or you need customers.",
     "Up front, yes. The website is $499 once, while the plan is monthly. But a website on its own does not answer your phone or follow up on the people who fill out its form. The plan does not include a website build. It adds the system that answers calls and books the work. It comes down to whether you need a website, the system, or both."),
    ("Does the $299 plan include the CRM and AI receptionist?", "Does the Signature plan include the CRM and AI receptionist?"),
    ("No, and it is worth being clear about. Essentials at $299 covers keeping your website current, Google Business Profile, basic SEO, online booking, review requests, and missed-call text-back. The full CRM and the AI receptionist that answers 24/7 are on the Signature plan at $99 a month for up to 10 users.",
     "Yes. There is one plan, Signature, and it includes the full CRM and the AI receptionist that answers and books jobs, along with missed-call text-back, online booking, review requests, and card payments. It is $99 a month for up to 10 users."),
    ("Top Shelf pairs the software with the team that runs it, on one bill starting at $299 a month, with no setup fee.",
     "Top Shelf pairs the software with the team that runs it, on one bill starting at $99 a month, with no setup fee."),
    ("on one bill, starting at $299 a month with no setup fee and no long contract,", "on one bill, starting at $99 a month with no setup fee and no long contract,"),

    # answering-service and CRM articles: the AI receptionist inside Signature
    ("Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan, $899 a month.",
     "Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan, %s." % W),
    ("Top Shelf includes an AI receptionist that books consults 24/7 in the $899 Signature plan.",
     "Top Shelf includes an AI receptionist that books consults 24/7 in the Signature plan, from $99 a month."),
    ("Top Shelf includes an AI receptionist that answers 24/7 at $899/mo.",
     "Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan, from $99/mo."),
    ("Top Shelf includes an AI receptionist that answers 24/7 in the $899 Signature plan.",
     "Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan, from $99 a month."),
    ("Top Shelf includes an AI receptionist that answers calls, texts, and DMs in the $899 Signature plan.",
     "Top Shelf includes an AI receptionist that answers calls, texts, and DMs in the Signature plan, from $99 a month."),
    ('texts, and DMs in the $899 Signature"', 'texts, and DMs in the Signature plan."'),
    ("Top Shelf includes an AI receptionist that answers all of it and books the exam in the $899 Signature plan.",
     "Top Shelf includes an AI receptionist that answers all of it and books the exam in the Signature plan, from $99 a month."),
    ("in the Signature plan from $899/mo.", "in the Signature plan from $99/mo."),
    ("It is in Top Shelf's $899 Signature plan, not a separate bill.", "It is in the Top Shelf Signature plan, from $99 a month, not a separate bill."),
    ("Top Shelf includes it in the $899 Signature plan.", "Top Shelf includes it in the Signature plan, from $99 a month."),
    ("It comes in Top Shelf's $899 Signature plan.", "It comes in the Top Shelf Signature plan, from $99 a month."),
    ("Included in Top Shelf Signature at $899/mo.", "Included in Top Shelf Signature, from $99/mo."),
    ("It comes in the Signature plan, flat, at $899 a month, with no per call or per minute meter running.",
     "It comes in the Signature plan at %s. %s" % (W, PHONE)),
    ("and it comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter.",
     "and it comes in the Signature plan at %s." % W),
    ("and runs intake comes in the Signature plan at $899 flat, with no per-call fee.",
     "and runs intake comes in the Signature plan, from $99 a month."),
    ("while the AI receptionist is a flat part of the $899 Signature plan with no meter.",
     "while the AI receptionist is part of the Signature plan, from $99 a month. %s" % PHONE),
    ("Top Shelf answers all of it 24/7 on the flat $899 Signature plan, with no per-call fee.",
     "Top Shelf answers all of it 24/7 on the Signature plan, from $99 a month."),
    ("Top Shelf answers it all 24/7 for a flat $899 a month, no per-call meter.",
     "Top Shelf answers it all 24/7 on the Signature plan, from $99 a month."),
    ("all for a flat $899 a month on the Signature plan with no per-call or per-minute meter no matter how hard it storms.",
     "all on the Signature plan at %s, plus $50 a month per phone line." % W),
    ("while the Signature plan stays a flat $899 a month no matter how busy the weather gets.",
     "while the Signature plan stays %s. %s" % (W, PHONE)),
    ("The Signature plan stays $899 a month no matter how busy the weather gets,",
     "The Signature plan stays %s no matter how busy the weather gets," % W),
    ("What the $899 Signature plan actually", "What the Signature plan actually"),
    ("The same $899 also includes the full Top Shelf CRM, a website built for you, advanced SEO every month, review responses written for you, customer reactivation, and lead follow-up in under five minutes.",
     "It is %s, and the same plan also includes the full Top Shelf CRM, missed-call text-back, online booking, review requests and replies, estimates, and card payments." % W),
    ("If all you want right now is the basics, the Essentials plan is $299 a month and covers website upkeep, Google profile, booking, and review requests, but the AI receptionist starts at Signature.", ""),
    ("The only cost on top of the plan is telecom usage, the phone numbers and text messages, billed at pass-through cost the same as everywhere in the industry.",
     "The only cost on top of the plan is the phone line, $50 a month per line, which covers normal use. Usage above that is billed."),
    ("The honest way to know which plan fits is a free audit, which puts real numbers to how many calls you are missing today.",
     "The price depends only on team size: %s, and $199 a month for 11 to 25." % W),
    ("Only telecom usage, the phone numbers and text messages, billed at pass-through cost the same as everywhere in the industry.",
     "Only the phone line, which is $50 a month per line and covers normal use. Usage above that is billed."),
    ("bundled with the CRM, website, and monthly SEO, because", "bundled with the CRM, because"),

    # website-cost articles: the $499 website
    ("The site is a one-time $1,500 build you own. But a site that ranks needs ongoing SEO to stay visible, which a build-and-leave rarely includes. A monthly plan is optional and adds that upkeep and the tools that capture its leads, so the site keeps working instead of aging out.",
     "The website is $499 one time, and you own it. The Signature plan is optional and adds the tools that answer and follow up on the leads it brings in."),
    ("A custom five-page HVAC site from Top Shelf is $1,500 once, and you own it.", "A professional HVAC website from Top Shelf is $499 one time, and you own it."),
    ("A custom five-page HVAC site from Top Shelf is $1,500 one-time to own outright.", "A professional HVAC website from Top Shelf is $499 one time, and you own it outright."),
    ("A custom five-page HVAC site is $1,500 one-time to own outright, with no plan and no commitment.", "A professional HVAC website is $499 one time, and you own it outright, with no plan and no commitment."),
    ("A monthly plan is optional and keeps the site working, Essentials at $299, Signature at $899, or Platinum at $2,500, with no setup fee. If the site you already have is solid, we optimize that one instead of charging you for a new build.",
     "The Signature plan, from $99 a month, is optional and adds the AI receptionist and CRM that answer and follow up on the calls the site brings in, with no setup fee. If the site you already have is solid, keep it, and the plan adds an AI chatbot to it."),
    ("A custom five-page site is a separate one-time build at $1,500, yours to keep, and you do not need a plan to buy one.",
     "A professional website is a separate one-time build at $499, yours to keep, and you do not need a plan to buy one."),
    ("Top Shelf folds marketing into one flat monthly plan starting at $299.", "Top Shelf makes sure the calls it brings in get answered, from $99 a month."),
    ("Rather than a separate ad-agency retainer, Top Shelf folds marketing into one flat monthly plan starting at $299, alongside the tools that convert it.",
     "Whatever you spend, the Top Shelf Signature plan, from $99 a month, answers and follows up on the calls that spend brings in."),
    ("That is why Top Shelf does not sell marketing as a separate ad-agency retainer. It comes folded into one flat monthly plan, Essentials at $299, Signature at $899, or Platinum at $2,500, alongside the website, reviews, booking, and follow-up that turn attention into jobs.",
     "That is the part Top Shelf handles. The Signature plan, from $99 a month, answers every call, books the job, sends review requests, and follows up, so the attention you pay for turns into jobs."),
    ("Prices vary widely, but with Top Shelf a custom site is $1,500 one time and yours to own outright,",
     "Prices vary widely, but with Top Shelf a professional website is $499 one time and yours to own outright,"),
    ("A custom site, with your portfolio and town pages built in, is $1,500 one time, and you own it outright.",
     "A professional website, with your portfolio and the towns you serve built in, is $499 one time, and you own it outright."),
    ("Plans start at $299 a month, the monthly SEO that keeps you showing up is done for you, and there is no setup fee.",
     "The Signature plan starts at $99 a month and adds the CRM and AI receptionist, and there is no setup fee."),
    ("The site is a flat $1,500 one-time build that you own.", "The website is $499 one time, and you own it."),
    ("A plan from $299 a month is optional, and it is where the monthly SEO to keep you visible through the seasons is done for you, which is what most landscapers need. The site on its own makes sense if you can handle that search work yourself.",
     "The Signature plan, from $99 a month, is optional and adds the CRM and AI receptionist that answer and follow up on the estimates the site brings in."),
    ("Top Shelf builds a custom five-page site for $1,500 one-time, and you own it.", "Top Shelf builds a professional website for $499 one time, and you own it."),
    ("The website is a one-time $1,500 build that you own.", "The website is $499 one time, and you own it."),
    ("A monthly plan is optional, starting at $299 a month, and adds the tools", "The Signature plan is optional, starting at $99 a month, and adds the tools"),
    ("It is a one-time $1,500 build you own, and a plan from $299 a month keeps it working, so the site earns its keep.",
     "It is $499 one time and you own it, and the Signature plan, from $99 a month, answers and follows up on every lead it sends you."),
    ("for $1,500 one-time, and you own it.", "for $499 one time, and you own it."),
    ("A custom site that shows your floors and books the measure is $1,500 one-time,", "A professional website that shows your floors and books the measure is $499 one time,"),
    ("A monthly plan is optional and starts at $299 a month, where the ongoing SEO that actually gets it ranking is handled for you and it plugs into the same system that answers the calls and follows up on the trials it captures.",
     "The Signature plan is optional and starts at $99 a month, and it answers the calls and follows up on the trials the site captures."),
    ("A monthly plan is optional and starts at $299 a month, where the ongoing SEO that gets it ranking for near-me searches is handled for you, and there is no setup fee either way.",
     "The Signature plan is optional and starts at $99 a month, and there is no setup fee either way."),
    ("A monthly plan is optional and starts at $299 a month, where the ongoing SEO that gets it ranking for junk removal near me is handled for you.",
     "The Signature plan is optional and starts at $99 a month."),
    ("A monthly plan is optional and starts at $299 a month, where the ongoing work of getting it ranked is handled for you.",
     "The Signature plan is optional and starts at $99 a month."),
    ("Or add a monthly plan starting at $299 to keep it working, where the ongoing SEO that helps owners actually find you is handled for you, and the Signature plan at $899 adds the phone and follow-up that answer and rebook the clients the site brings in.",
     "Or add the Signature plan, from $99 a month, for the phone and follow-up that answer and rebook the clients the site brings in."),
    ("Or add a monthly plan starting at $299 to keep it working, where the ongoing SEO that gets it ranking for your towns is handled for you.",
     "Or add the Signature plan, from $99 a month, to answer and follow up on the calls it brings in."),
    ("Or add a monthly plan starting at $299 to keep it working, where the ongoing SEO that gets it ranking for the towns you cover is handled for you.",
     "Or add the Signature plan, from $99 a month, to answer and follow up on the calls it brings in."),
    ("A custom five page site, built to do everything above, is $1,500 one-time, yours to keep with no commitment.",
     "A professional website, built to do everything above, is $499 one time, yours to keep with no commitment."),
    ("A custom five page site built to do everything above is $1,500 one-time,", "A professional website built to do everything above is $499 one time,"),
    ("A custom site that does that is $1,500 one-time with Top Shelf, and you own it.", "A professional website that does that is $499 one time with Top Shelf, and you own it."),
    ("The one-time custom build is $1,500 with no setup fee, and you own it outright.", "The professional website is $499 one time with no setup fee, and you own it outright."),
    ("A monthly plan starting at $299 is optional and keeps the site working, with the ongoing SEO handled for you.", "The Signature plan, from $99 a month, is optional."),
    ("Top Shelf builds a custom five page site that does all of that for $1,500 one-time, yours to keep.",
     "Top Shelf builds a professional website that does all of that for $499 one time, yours to keep."),
    ("Whether you pay a little for a template you build yourself or more for a custom site with ongoing SEO,",
     "Whether you pay a little for a template you build yourself or more for a custom site,"),
    ("on one platform, starting at $299 a month, so a patient", "on one platform, starting at $99 a month, so a patient"),
    ("Top Shelf builds yours for $1,500, and you own it.", "Top Shelf builds yours for $499, and you own it."),
    ("Top Shelf builds yours for $1,500.", "Top Shelf builds yours for $499."),
    ("A custom five page site is $1,500 one-time, yours to keep.", "A professional website is $499 one time, yours to keep."),
    ("If you buy the one-time $1,500 site, it is yours to keep", "If you buy the $499 website, it is yours to keep"),
    ("Top Shelf builds it for $1,500, and you own it.", "Top Shelf builds it for $499, and you own it."),
    ("Top Shelf builds one for $1,500 one time, and you own it.", "Top Shelf builds one for $499 one time, and you own it."),
    ("A custom five page site by itself runs $1,500 one time, built for you and yours to keep.", "A professional website runs $499 one time, built for you and yours to keep."),
    ("Or you take it built at no extra charge on any monthly plan, which starts at $299 and includes the ongoing SEO that keeps it climbing.", ""),
    ("Setup is included with no separate fee, whichever path you pick.", "There is no setup fee."),
    ("Is $1,500 a fair price for a handyman website?", "Is $499 a fair price for a handyman website?"),
    ("Is $1,500 a fair price for a painting website?", "Is $499 a fair price for a painting website?"),
    ("It sits in the normal range for a custom-built site, well above a fill-in template and well below a long agency contract.",
     "It is on the low end for a custom-built site, above a fill-in template and well below a long agency contract."),
    ("At Top Shelf a custom five page site is $1,500 one-time and yours to keep,", "At Top Shelf a professional website is $499 one time and yours to keep,"),
    ("It lives in the Signature plan at $99 a month for up to 10 users, with the AI receptionist and monthly SEO, while plans start at $299 a month.",
     "It lives in the Signature plan at %s, alongside the AI receptionist." % W),
    ("Free on any plan from $299/mo, or $1,500 to own outright.", "$499 one time, and you own it outright."),
    ("Top Shelf builds it for $1,500 one-time, and plans from $299 a month keep it working.", "Top Shelf builds it for $499 one time, and you own it."),
    ("site described above for $1,500 one-time, and it is yours to keep.", "site described above for $499 one time, and it is yours to keep."),
    ("A monthly plan is optional. Plans begin at $299 a month and carry the ongoing SEO that keeps a site ranking.", "The Signature plan, from $99 a month, is optional."),
    ("With Top Shelf you own the site outright for $1,500 one-time, and an optional plan from $299 a month adds the SEO that gets it found.",
     "With Top Shelf you own the website outright for $499 one time, and it is built so Google can read it."),
    ("Top Shelf builds one that ranks and books for $1,500 one-time, and you own it.", "Top Shelf builds one that books for $499 one time, and you own it."),
    ("The site is a one-time $1,500 build and it is yours to keep.", "The website is $499 one time, and it is yours to keep."),
    ("Top Shelf folds the website into every monthly plan, which begins at $299, and handles the SEO that keeps your pest and town pages showing up. If you would rather buy it once and owe nothing after, a five page build is $1,500 flat and stays yours.",
     "Top Shelf builds a professional website for $499 one time, built so Google can read it, and it stays yours."),
    ("Neither route carries a setup fee, and since Google answers to no one, the only honest promise is to do the work that earns rankings and show you where you stand today.",
     "There is no setup fee, and since no one controls Google, no honest company can promise you a ranking."),
    ("Top Shelf builds a custom one for $1,500 one-time, and you own it.", "Top Shelf builds one for $499 one time, and you own it."),
    ("Top Shelf builds yours for $1,500 one time, and you own it.", "Top Shelf builds yours for $499 one time, and you own it."),
    ("A custom site on its own is $1,500 one time, yours to keep,", "A professional website on its own is $499 one time, yours to keep,"),
    ("With Top Shelf it is $1,500 one time, and you own it.", "With Top Shelf it is $499 one time, and you own it."),
    ("With Top Shelf a custom site is $1,500 one time, and you own it outright.", "With Top Shelf a professional website is $499 one time, and you own it outright."),
    ("A monthly plan from $299 a month is optional and keeps it working.", "The Signature plan, from $99 a month, is optional."),
    ("A custom five-page website is $1,500 one time, and it is registered to you,", "A professional website is $499 one time, and it is registered to you,"),
    ("A monthly plan is optional and keeps the site working, starting at $299 a month with no setup fee.", "The Signature plan is optional, starting at $99 a month with no setup fee."),
    ("Either way the site is built to rank locally and capture leads into your own system.", "Either way the site is built so Google can read it, and it captures leads into your own system."),
    ("With Top Shelf the site is $1,500 to own outright,", "With Top Shelf the website is $499 to own outright,"),
    ("A custom five-page site is a $1,500 one-time build, and you own it.", "A professional website is $499 one time, and you own it."),
    ("A plan is optional and keeps the site working, starting at $299 a month with no setup fee.", "The Signature plan is optional, starting at $99 a month with no setup fee."),
    ("A custom roofing website is $1,500 one-time with Top Shelf, and you own it.", "A professional roofing website is $499 one time with Top Shelf, and you own it."),
    ("A plan from $299 a month keeps it working.", ""),
    ("A custom roofing website is $1,500 one-time with Top Shelf, yours to keep.", "A professional roofing website is $499 one time with Top Shelf, yours to keep."),
    ("A monthly plan, starting at $299, is optional and keeps the site working.", "The Signature plan, from $99 a month, is optional."),
    ("You buy a custom five-page site outright for $1,500 one-time,", "You buy a professional website outright for $499 one time,"),
    ("If you want it kept working, you add a monthly plan that starts at $299, which handles small edits to the site, your Google Business Profile, online booking, and automated review requests.",
     "If you want the calls it brings in answered and followed up, you add the Signature plan, from $99 a month, which includes the AI receptionist, online booking, and automated review requests."),
    ("The website is a $1,500 one-time build, yours to keep.", "The website is $499 one time, yours to keep."),
    ("A custom five page site on its own is $1,500 one-time, yours to keep, with no plan attached.", "A professional website on its own is $499 one time, yours to keep, with no plan attached."),
    # "keeps it working" implied the plan maintains the site; it does not
    ("A monthly plan is optional and keeps it working.", "The Signature plan is optional."),
    ("A monthly plan is optional and keeps the site working.", "The Signature plan is optional."),
    ("A monthly plan is optional upkeep, and stopping the plan does not change that.", "The Signature plan is optional, and stopping it does not change that."),
    ("A monthly plan is optional, with no setup fee.", "The Signature plan is optional, with no setup fee."),
    ("A monthly plan is optional.", "The Signature plan is optional."),

    # comparison (vs) pages
    ("The pricing is plain: Essentials is $299 a month, the Signature plan that adds the AI receptionist and CRM is $899 a month, a fully done-for-you plan is $2,500 a month, or a one-time custom five page site is $1,500,",
     "The pricing is plain: the Signature plan with the AI receptionist and CRM is %s, and a professional website is $499 one time," % W),
    ("A fully done-for-you plan is $2,500 a month, or a one-time custom site is $1,500.", "A professional website is $499 one time."),
    ("If your gap is getting found first, the Essentials plan at $299 a month covers website upkeep and local SEO.", "If you need a new website too, it is $499 one time."),
    ("Essentials is $299 a month for website upkeep and local SEO, Signature is $899 a month and adds the AI receptionist and CRM, and a fully done-for-you plan is $2,500 a month.",
     "The Signature plan is %s and includes the AI receptionist and CRM." % W),
    ("If you just want a site, a one-time custom five-page website is $1,500.", "If you just want a website, it is $499 one time."),
    ("Top Shelf's plans start at $299 a month for website upkeep and local SEO with the Essentials plan, step up to $899 a month for the Signature plan that adds the AI phone receptionist and the CRM with automated follow-up, and reach $2,500 a month for the fully done-for-you setup where we run the marketing end to end.",
     "The Top Shelf Signature plan is %s and includes the AI phone receptionist and the CRM with automated follow-up." % W),
    ("If you would rather do a one-time project, a custom five-page website is $1,500.", "If you would rather do a one-time project, a professional website is $499."),
    ('Top Shelf offers <a href="pricing.html">plans</a> that start at $299 a month with no setup fee, and the honest first step is a free look at where your leads are actually going.',
     'The Top Shelf <a href="pricing.html">Signature plan</a> starts at %s, with no setup fee.' % W),
    ("Plans start at $299 a month for Essentials, and Signature is $899 a month and adds the AI receptionist and the CRM.",
     "The Signature plan is %s and includes the AI receptionist and the CRM." % W),
    ("A fully done-for-you engagement is $2,500 a month, and a one-time custom five-page site is $1,500.", "A professional website is $499 one time."),
    ("re:(?<=[\"'>])\\s*Signature is \\$899 a month and adds the AI receptionist and the CRM\\.",
     "The Signature plan is %s and includes the AI receptionist and the CRM." % W),
    ("Fully done-for-you is $2,500 a month, or you can get a one-time custom five-page site for $1,500.", "A professional website is $499 one time."),
    ("The AI receptionist and CRM come together in the Signature plan at $99 a month for up to 10 users; the Essentials plan is $299 a month for website upkeep, local SEO, reviews, and marketing; a fully done-for-you plan is $2,500 a month; and a one-time custom five-page website is $1,500.",
     "The AI receptionist and CRM come together in the Signature plan at %s, and a professional website is $499 one time." % W),
    ("re:(?<=[\"'>])\\s*Signature is \\$899 a month and adds the AI receptionist, CRM, and automated follow-up\\.",
     "The Signature plan is %s and includes the AI receptionist, CRM, and automated follow-up." % W),
    ("A fully done-for-you plan is $2,500 a month, or you can get a one-time custom five-page website for $1,500.", "A professional website is $499 one time."),
    ("Essentials is $299 a month, and Signature at $899 a month adds the AI receptionist and CRM.",
     "The Signature plan is %s and includes the AI receptionist and CRM." % W),
    ("builds your website, works on your local SEO so people can find you, and answers", "builds your website and answers"),
    ("builds your website, works on your local SEO, answers", "builds your website, answers"),
    ("Top Shelf starts at $299 a month for Essentials, which covers website upkeep, local SEO, reviews, and marketing, handled for you.", ""),
    ("Signature is $899 a month and adds the AI phone receptionist and the CRM that follows up on every lead.",
     "The Signature plan is %s and includes the AI phone receptionist and the CRM that follows up on every lead." % W),
    ("If you want everything run at the highest level, the fully done-for-you plan is $2,500 a month, and a one-time custom five-page website is $1,500.", "A professional website is $499 one time."),
    ("If you want the calls and the marketing that create them handled too, the fully done-for-you plan is $2,500 a month, an entry plan with website upkeep and local SEO is $299 a month on Essentials, and a one-time custom five-page site is $1,500.",
     "If you need a new website too, it is $499 one time."),
    ("Signature is $899 a month and adds the AI receptionist and the CRM with automated follow-up.",
     "The Signature plan is %s and includes the AI receptionist and the CRM with automated follow-up." % W),
    ("If you want everything handled at the highest level, the full done-for-you program is $2,500 a month, and a one-time custom five-page website is $1,500.", "A professional website is $499 one time."),
    ("Top Shelf starts at $299 a month for website upkeep and local SEO, and the Signature plan at $99 a month for up to 10 users adds the AI receptionist and CRM that answer and follow up on every call and lead, with online booking included throughout.",
     "The Top Shelf Signature plan, %s, includes the AI receptionist and CRM that answer and follow up on every call and lead, with online booking included." % W),
    ("Top Shelf is a flat monthly price with no setup fee: $299 a month for website upkeep and local SEO, and $899 a month for the Signature plan that adds the AI receptionist and CRM.",
     "Top Shelf is a monthly price with no setup fee: the Signature plan is %s and includes the AI receptionist and CRM." % W),
    ("A fully done-for-you plan is $2,500 a month, and a one-time custom five-page site is $1,500.", "A professional website is $499 one time."),
    ("It is one bill for the whole managed service, so there is no per-call meter and no stack of separate tools to reconcile.",
     "It is one bill, so there is no stack of separate tools to reconcile."),
    ("Essentials starts at $299 a month for website upkeep and local SEO foundation, and a fully done-for-you setup runs $2,500 a month.", ""),
    ("Essentials is $299 a month, Signature is $899 a month, and Platinum is $2,500 a month, with no setup fee.",
     "The Signature plan is %s and $199 a month for 11 to 25, with no setup fee." % W),
    ("Essentials is $299, Signature is $899, and Platinum is $2,500, with no setup fee.",
     "The Signature plan is %s and $199 a month for 11 to 25, with no setup fee." % W),

    # pass 4: the plan no longer does SEO, holds the website, or runs unmetered
    (r"re:It (?:keeps the site working, and|is where) the ongoing SEO that (?:actually )?gets it (?:ranking|found)(?: for [^.]*?)? is handled for you(?:, with no setup fee either way|, and there is no setup fee either way)\.",
     "It adds the AI receptionist and CRM that answer and follow up on the leads the site brings in, and there is no setup fee either way."),
    (r"re:It (?:keeps the site working, and|is where) the ongoing SEO that (?:actually )?gets it (?:ranking|found)(?: for [^.]*?)? is handled for you\.",
     "It adds the AI receptionist and CRM that answer and follow up on the leads the site brings in."),
    ("A plan bundles the build with the SEO and updates, which is where most of the long-term value lives.",
     "An agency plan bundles the build with SEO and updates, and that is where the monthly cost lives."),
    ("bundled with the CRM, website, and monthly SEO, with no per-call or per-minute meter and no setup fee.", "bundled with the CRM, with no setup fee."),
    ("bundled with the CRM, website, and SEO.", "bundled with the CRM."),
    ("bundled with the AI receptionist, monthly SEO, and reviews,", "bundled with the AI receptionist and review requests,"),
    ("which also includes the AI receptionist, monthly SEO, and done-for-you reviews,", "which also includes the AI receptionist and review requests,"),
    ("which also includes the AI receptionist, monthly SEO, and reviews,", "which also includes the AI receptionist and review requests,"),
    ("which also includes the AI receptionist that answers your calls, monthly SEO, reviews, and reactivation,", "which also includes the AI receptionist that answers your calls and review requests,"),
    ("bundled with the CRM that follows up on every lead, online booking, a website, and monthly SEO, so", "bundled with the CRM that follows up on every lead and online booking, so"),
    ("That same plan also includes your CRM, website, and monthly SEO, so", "That same plan also includes your CRM, so"),
    (r"re:while the AI receptionist is a flat part of (?:your|the Signature) plan with no meter\.",
     "while the AI receptionist is part of the Signature plan. " + PHONE),
    (", and it answers every call with no separate per-minute charge.", ". " + PHONE),
    ("with no after-hours surcharge or per-call overage.", "with no after-hours surcharge."),
    ("for up to 10 users, flat, ", "for up to 10 users, "),
    ("The pricing page lays out every plan line by line", "The pricing page lays out the plan line by line"),    ("Top Shelf makes sure the calls it brings in get answered, from $99 a month.", "Top Shelf answers the calls your marketing brings in, from $99 a month."),
]
SENTENCES += focus_agency.ROWS  # pass 5: the done-for-you agency copy

APOS = r"(?:'|&#x27;|&#39;|&rsquo;|’|\\')"


def _key_rx(key):
    if key.startswith("re:"):
        return key[3:]
    out = []
    for ch in key:
        if ch == " ":
            if not out or out[-1] != r"\s+":
                out.append(r"\s+")
        elif ch == "'":
            out.append(APOS)
        else:
            out.append(re.escape(ch))
    return "".join(out)


def _sentence_rx(key, new):
    body = _key_rx(key)
    if new == "":
        body = r"(?:\s+%s|%s\s*)" % (body, body)
    return re.compile(body)


def _sentence_rep(new):
    def rep(m):
        found = re.search(APOS, m.group(0))
        return new.replace("'", found.group(0)) if found else new
    return rep


SENTENCE_RX = [(_sentence_rx(k, n), _sentence_rep(n)) for k, n in SENTENCES]


def apply(text):
    for rx, rep in COMPILED:
        text = rx.sub(rep, text)
    for rx, rep in SENTENCE_RX:
        text = rx.sub(rep, text)
    return text


def main():
    for path in cat.site_pages() + cat.source_files():
        s = open(path, encoding="utf-8").read()
        t = apply(s)
        if t != s:
            open(path, "w", encoding="utf-8", newline="").write(t)


if __name__ == "__main__":
    main()
