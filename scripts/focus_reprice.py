"""Reprice the copy to the Signature plan and the $499 website. Re-runnable.

Applied to the built pages AND the generator sources (spec files), so a
regenerated page carries the new copy. Rows are (regex, replacement); an empty
replacement deletes the sentence and the space before it.
"""
import re

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


def apply(text):
    for rx, rep in COMPILED:
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
