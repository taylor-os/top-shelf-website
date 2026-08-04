# Top Shelf — nine-agent website audit
**Run 2026-08-04 · one CEO lens + eight industry buyers · live site, not staging**

Private: `.htaccess` 404s `/docs/` and any `.md`, so this is not web-reachable.

Nine independent agents read the live site. Each fetched real pages and quoted real
copy. Below, every claim they made that mattered has been checked against the source
before being repeated — including four I threw out.

---

## 0 · What I verified myself before repeating it

The agents were briefed to be adversarial. That produces sharp findings and also
false alarms. I checked the load-bearing ones.

### CONFIRMED — act on these

| Finding | Evidence |
|---|---|
| **The audit form submits into nothing** | `contact.html:99` → `action="https://formspree.io/f/FORMSPREE_ID"`. Live POST returns `404 {"error":"Form not found","code":"FORM_NOT_FOUND"}`. No JS intercepts it — the submit listener at `site.js:324` belongs to the chat widget. |
| **Same dead placeholder is the quiz's fallback** | `gap-quiz.js:23`. Guarded though: line 167 checks for the literal string and skips it, so the quiz degrades rather than erroring. Its primary endpoint (Railway `/api/website-lead`) is live. |
| **Five pages ship visible mail-merge artifacts** | `industry-custom.html:486` "of Your **Your Business Business**" · `:487` "**Your-style** gaps" · `industry-legal.html:452` "Your **Law Firms** Business" · `industry-restaurants.html:457` "**The-style** gaps" · `solution-pos.html:126` "**The** That's Costing You" |
| **Law Firms missing from the contact dropdown** | Options are Bar/Restaurant, Dental/Medical, Home Services, Auto, Retail, Salon/Spa, Other. Law Firms has a nav entry, a footer link on every page, and a full industry page. The **Gap Finder quiz already has "Law firm"** — the form is the thing out of sync. |
| **The industry-page pattern is real** | `grep` for the CTA line returns Cedar-style, Harlan-style, Maple-style, Redline-style, Ridgeline-style, Willow-style — the placeholder takes the *fictional business's first word*. Where the business name starts with "The" or is literally "Your Business", it renders as garbage. |

### NOT CONFIRMED — do not act on these

Four agents reported contradictory statistics. **They are misreading the count-up
animation.** The cards carry `data-count` and animate from zero on scroll
(`site.js:54–72`).

| Reported "contradiction" | Actual source value |
|---|---|
| "16% vs 62% unanswered" | `data-count="62"` — one value |
| "22% vs 85% never call back" | `data-count="85"` — one value |
| "$33K vs $126K" | `data-count="126"` — one value |
| "11x vs 21x" on solution-crm | `21x` only; no `11x` exists anywhere |
| "2% / 4% vs 44% / 88%" on SEO page | body and cards both say 44% / 88% |

**But this is its own finding, and a better one.** Five independent readers, reading
carefully and adversarially, all came away believing the numbers contradicted each
other. Marcus put it best: *"I watched '7%' become '62%' while reading. On a page
selling numerical honesty, don't let numbers visibly move."* If careful readers
misread them, skimmers do too — and so do AI crawlers, which matters for the AEO
work. **Recommendation: render the final value server-side and drop the count-up on
stat cards.** The animation is costing credibility to buy motion.

Also not confirmed: the "invisible nav dropdown click-trap." The dropdown is
`visibility:hidden` when closed, which does block pointer events, and the
`::before` hover-bridge is inside it and inherits that. Two agents reported phantom
navigation, so something is sensitive near the header — but it isn't the bug they
diagnosed. Worth a manual check, not a code change on this evidence.

Unverified: the auto page's *"average independent garage's missed-call rate near
38% during busy hours"* sits in the same sentence as the marchex-cited 21%. Whether
marchex supports the 38% needs the source read. **The agent's structural point
stands regardless: one citation is covering two claims.**

---

## 1 · The CEO lens

Strongest strategic read, condensed:

**The gap metaphor is a genuine asset.** *"You're not losing money because your work
is bad."* Hibu and Thryv sell "grow your business." You sell "stop the specific
bleeding." That is a sharper wedge and every persona responded to it.

**But the ten-service list undoes it.** *"The moment a prospect reaches 'Ten Services.
One Flywheel,' you stop being the specialist who finds the gap and become the
generalist who does everything — which is precisely Hibu and Thryv's silhouette. You
name them as villains and then present their org chart."*

That is the sharpest sentence in all nine reports. **Your differentiator is asset
ownership plus honest reporting, not breadth.** Breadth is the thing you share with
the companies you attack.

**Credibility gap.** No team page, no founder name, no headcount, no explanation of
how ten disciplines get delivered at $899. An investor's first question — *who
delivers this?* — has no answer on 22 pages.

**Margin risk at scale.** The free website is recovered only across the six-month
term ($499 × 6 = $2,994), so **early churn is structurally unprofitable** — you eat
the build. "Review responses written and posted for you" is human labour that
doesn't scale at $899. Ten services × eight verticals = 80 delivery permutations at
a price supporting maybe three.

**Its "one thing":** fix the form. *"It is the only problem currently costing you
every dollar of inbound revenue, silently, while the site looks perfectly healthy."*

---

## 2 · The eight buyers

| Persona | Business | Would request audit? | Their single blocker |
|---|---|---|---|
| **Marcus** | Plumbing/HVAC, $1.4M | Yes — *only* after finding the sample report | No proof; can't hear the AI |
| **Ray** | 2-bay auto, $900K | Yes, **but would call, not use the form** | Can't hear the AI; the unsourced 38% |
| **Dr. Alvarez** | Dental, $800K | Yes — audit only, **would not fill the form** | **No BAA. Cannot legally buy.** |
| **Nick** | Bar/restaurant, $600K | Yes, narrowly — for the processing analysis | POS migration never addressed |
| **David** | 4-attorney law firm | Yes, **by phone, opening with an interrogation** | **Privilege, conflicts, bar ad rules** |
| **Dana** | Gift shop, $420K | Yes — for the free report, not to buy | **$899 unaffordable; POS unpriced** |
| **Tasha** | Salon + med spa, $650K | Soft yes | **Vagaro — replace or stack?** |
| **Greg** | Commercial cleaning, $1.1M | 55% — *"under 20% if I hadn't reached the pricing FAQ"* | Entire site assumes inbound consumer |

**Three of eight said they would phone rather than use the form.** Given the form is
dead, the ones who *did* use it got nothing — and concluded you don't return calls.

---

## 3 · What all eight agreed on

These are unanimous or near-unanimous across eight very different businesses. Highest
confidence findings in the whole exercise.

### 3.1 The ownership paragraph is your best copy — 8 of 8

> *"Your website, domain, Google Business Profile, phone number, and your entire
> customer list — every name, number, and job history — are yours from day one.
> Export it any time."*

Every single persona named this unprompted. Marcus: *"I read it twice."* Nick: *"the
single best paragraph on the whole site."*

**Why it works, per Marcus:** you immediately admit the limit — *"The CRM platform
and the automations that run on it are ours."* **Naming what they don't get is what
made them believe the part they do.** Precision where a liar would stay vague.

### 3.2 The six-month term disclosure saves the sale — 8 of 8

> *"We ask for six because that is honestly how long it takes... and we would rather
> say so now than surprise you later."*

Ray: *"bought back most of the trust the 38% stat cost you."* David, who reads
contracts for a living: *"That is the paragraph a company writes when it isn't
hiding anything."* Greg: without reaching it, his odds drop from 55% to under 20%.

**It is buried in body text below three price cards.** Marcus nearly left at the
cards assuming the contract was hidden. **Move it onto the cards.** You are doing the
honest thing quietly and the marketing thing loudly.

### 3.3 Zero named clients — 8 of 8, and it is the ceiling on everything

No logos. No testimonials. No attributed case studies. One named client — GDR, your
own company, on a page not in the nav.

The bite is that the *fictional* businesses are rendered in loving detail. Marcus:
> *"You wrote a fictional Marcus at Ridgeline Comfort & Repair — six gaps, a day in
> his life, where he is six months later. Spend that same effort on one real
> customer and you won't need the fictional one. Right now the most vivid business
> owner on your website is the one who doesn't exist, and I noticed."*

Nick found the self-indictment: the reviews page argues *"People trust a real
customer's face and voice far more than any claim you make about yourself"* — on a
site with no customer's face or voice.

**"REAL RESULTS" is the specific problem.** Three precise dollar figures ($24K bar,
260 reviews, $144K dental) with no name, no city, no year, and — verified — **no
disclaimer**, while the POS and marketing pages *do* carry disclaimers. The boldest
claims are the only unqualified ones. Nick, who runs a bar, ran the $24K arithmetic
and found it only works if that bar was 57% liquor sales — *"under-specified in
exactly the direction that flatters it."*

### 3.4 The industry pages are excellent; the solution pages betray them — 7 of 8

Universal shape: industry page earns real trust, then one click into a solution page
lands in home-services copy.

- Dr. Alvarez: *"crown seat"* and *"hygiene column"* → one click → *"You're up a
  ladder."* **"I am not up a ladder. I'm chairside with a handpiece and gloves on."**
- Tasha: *"drop your tools"* — *"I'm holding foils."* And the memberships page hero
  is **a row of beer taps**, shown to a med spa.
- Dana: the retail page says *"the quotes that go cold"* — *"Nobody has ever asked me
  to quote a ceramic."* Memberships says *"between jobs"* four times.
- Nick: pricing FAQ says *"one saved job a month often covers the plan"* — *"My 'job'
  is a $70 table."*

Dana names the pattern precisely: **"the deeper page was less relevant than the
shallower one. Going deeper should feel more known, not less."**

Confirmed in the site's own words — Why Us question 09: *"The industries on our site
are just examples."* David: *"I suspected it on page 2; they confirmed it on page 6."*

### 3.5 "Do I have to replace what I already run?" — unanswered for 5 of 8

The single most repeated practical blocker.

| Persona | Runs | Site says |
|---|---|---|
| Nick | Toast/Square POS | nothing — verified: *switch, migrate, replace your POS* appear zero times |
| Dana | Square | nothing — and the POS page **cites "(Square data)"** while never telling Square users what happens |
| Tasha | Vagaro | nothing — verified: Vagaro, Boulevard, Mindbody = zero mentions sitewide |
| Dr. Alvarez | Dentrix | nothing — no PMS named anywhere |
| Ray | shop-management software | nothing |

Nick: *"My POS is the nervous system of my restaurant... losing a Saturday costs me
more than a year of $899. Silence on the scariest question reads as 'the answer is
bad.'"*

Tasha: *"That silence reads as either 'they don't know our industry' or 'they're
hiding that you'd pay twice' — and both kill the call."*

### 3.6 The $9,605 comparison oversells and they all caught it — 5 of 8

Nick: *"My real alternative is $0 and keep doing nothing, and the table pretends that
option doesn't exist."* Ray: *"Nobody in my world hires any of those."* Dana: *"a
number designed for someone with a payroll."* Marcus found a genuine flaw: **the
$9,605 column is compared against "From $499," but Essential doesn't include the AI
receptionist or the CRM — two of the six rows.**

Marcus: *"I'm a guy who got burned by fine print, and I found fine print. It cost you
more than it gained you."*

### 3.7 The sample report is the best asset you own and it is buried — 6 of 8

*"Most sample reports are made up. This one is not... It is not a flattering picture
in places, and we published it anyway... Retype those six searches on your phone and
see."* With two **F grades** on your own client.

Marcus: *"That is the first thing on this entire website that a liar could not easily
fake, and it is the only reason my answer is yes."* Ray: *"a guy showing me the
actual brake rotor instead of telling me it's bad."*

**It is a link at the bottom of the last page.** Marcus reached it on step seven of
seven, by accident. Through six and a half pages his answer was no.

---

## 4 · Where they diverged — the most useful part

The site sells one bundle to eight businesses whose needs do not overlap.

### Price means completely different things

- **David (law):** *"$10,788 a year. One signed PI case covers that several times
  over. Price is not my objection and they should understand that — they have spent
  five pages defending a number I was never going to argue about."*
- **Dr. Alvarez (dental):** *"the number is not the obstacle."*
- **Dana (retail, $420K):** *"more than my rent increase... To cover $899 I need
  roughly 24 additional sales a month that would not otherwise have happened, every
  month, forever."* **Verdict: not affordable, and the site never makes the $499 case
  because it steers everyone to Signature.**
- **Nick (4% margins):** needs ~13–16 extra covers/month — *"achievable, which means
  the honest math would have helped them. They just never did it."*

**Decision this forces:** high-ticket verticals (legal, dental, HVAC) should not see
price defended at all — they should see capability and compliance. Thin-margin
verticals (retail, restaurant) need the break-even arithmetic **in their own units**.
Right now everyone gets the same page.

### The AI receptionist is your flagship and it is wrong for half of them

| | Reaction |
|---|---|
| Marcus, Ray | **Want it** — but *"I would not buy this without hearing it."* No recording anywhere. Both named a demo as the biggest single unlock. |
| Tasha (med spa) | **Brand risk.** *"My front desk is part of the experience. A robot picking up for a med spa is a downgrade."* |
| David (law) | **Liability.** *"captures the caller's name, matter, and urgency"* — that's a prospective client under Rule 1.18. Also *"sounds human"* + answering in the firm's name may be a Rule 7.1 problem. |
| Dr. Alvarez | **PHI.** A patient describes symptoms; audio is transcribed and stored by a third party. |
| Dana, Greg | **Useless.** *"My door has a bell on it."* / *"My phone barely rings."* Both are paying $400/mo of the Essential→Signature step-up for it. |

### Two verticals are legally blocked, not persuasion-blocked

**Dental (Dr. Alvarez):** verified — the word **BAA appears nowhere on the site**,
and the privacy policy contains no HIPAA, PHI, or business-associate language.
> *"Without a BAA I cannot legally use your CRM for patients, at any price."*

She also flagged *"We automatically invite happy patients to leave a Google review"* —
how does it know they're happy? If it surveys first and routes only satisfied
patients, that's review gating, against Google policy. And *"Review responses written
and posted for you"* means a third party publicly discussing her patients.

**Legal (David):** verified — privilege, confidential, conflict, ethics, bar all
return zero matches sitewide. Conflicts is the sharp one: *"Speed-to-lead without a
conflicts gate isn't a competitive advantage, it's a malpractice generator."* And
database reactivation to a former client list — *"think a domestic violence
family-law client whose abuser sees the text."*

Both noted the same irony: **the TCPA/SMS consent block is properly built.**
> *"You demonstrably know how to do compliance when the risk is yours."*

**Decision this forces:** Medical/Dental and Law Firms are two of your highest-value
verticals and neither can currently sign. Either add the compliance answer or stop
running the pages.

### The outsider problem (Greg, commercial cleaning)

Eight tiles. Seven get a sentence about their life — *"You can't answer the phone
from under a sink."* His reads *"Don't see your exact trade? Start here."*
> *"Every other tile is about the customer. Mine is about the menu."*

And the catch-all page's generic owner is *still a residential tradesman* — *"The
phone rings while your hands are full."* Then it closes with **"Your Your Business
Business."**
> *"The named industries got a Marcus. I got a mail merge, and nobody read it."*

His broader point is a market question worth answering: nothing on the site addresses
bids, contracts, renewals, or buying committees. The word "contract" appears only as
*his* commitment to *you*. Yet his contract values are larger and his follow-up worse
than the plumber's — he'd be a better customer than the persona you wrote for.

---

## 5 · Decisions, ranked

**Tier 0 — today**
1. **Fix the contact form.** Every other item multiplies by zero until leads arrive.
2. **Remove `.catch(done)` false success** in `site.js` — the chat widget currently
   says *"You're all set ✅"* even when delivery fails.
3. **Fix the five mail-merge artifacts.** ~10 minutes. Two are in closing CTAs.
4. **Add Law Firms to the dropdown.** The quiz already has it.

**Tier 1 — this week, cheap, high impact**
5. **Promote the sample report to the homepage.** Your only unfakeable proof, on page
   seven. Six of eight said it was decisive *after* finding it by accident.
6. **Put the six-month term on the pricing cards.**
7. **Kill the count-up animation on stat cards.** Five careful readers misread them.
8. **Add "Already on Square / Toast / Vagaro / Dentrix?" blocks.** Five personas'
   top blocker; probably one paragraph each.
9. **Add a demo recording of the AI receptionist.** Named as the single biggest
   unlock by both trades personas.

**Tier 2 — decisions, not edits**
10. **Get one real named client on the site.** Universal. Nothing else moves the
    ceiling. If there are none yet, Nick's advice: *"say so plainly — 'we're new,
    here's our founder, here's our guarantee' — which is more disarming than
    fictional Marco."*
11. **Attribute or relabel "REAL RESULTS."** Either name them or mark illustrative
    and show the math. Currently the only unqualified claims on the site.
12. **Answer HIPAA/BAA and bar-advertising, or pull those two industry pages.**
13. **Rewrite the solution pages per-vertical, or at minimum strip "job," "quote,"
    "up a ladder," "drop your tools," "between jobs"** from paths a non-trades
    buyer walks.
14. **Do the ROI arithmetic in each vertical's own units.** Every persona who could
    afford it did the math themselves and found it worked. Most owners won't.
15. **Rethink the $9,605 table** — compare against doing nothing, or against $899
    where the claim is actually true.
16. **Decide whether the "we do ten things" framing is helping.** The CEO agent
    argues it makes you look like the incumbents you attack.

---

## Method note

Nine agents, live site, real fetches. Every persona reaction is a qualitative
simulation — strong hypotheses to test, not statistical evidence. Every *factual*
claim above was verified against the source before inclusion, and four agent findings
were discarded as animation artifacts (§0).
