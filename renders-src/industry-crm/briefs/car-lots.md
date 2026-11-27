# Car lots: screen brief (independent used-car lot, about a third buy here pay here)

Source of truth: the real Dealer Suite in top-shelf-crm (`docs/dealer-suite/how-your-lot-runs.md`, the layout-pass, P9 loans, P10 and customer-pay summaries, `lot-home.tsx`, `deal-stage-strip.tsx`, `financing-card.tsx`, `desk-card.tsx`, `bottom-nav.tsx`, `DealerPermissions.php`) and the 8 dealer screenshots in `renders/dealer-program-shots/dealer/`. Layout, words and who-sees-what below follow that kit. Only the look (emerald kit) and the sample data change.

What the current draft picks got wrong (do not repeat): they are the raw gold-on-black prod shots of Mesquite Creek Motors with "$0.00" Money in today, "57 down payments not recorded", "48 titles owed", "32 store-wide overdue", "25 new leads not reached", "11 overdue" per salesperson, 325 area code, and two of three images are the same Home. They make the lot look broken. Every number below is small, believable and adds up.

---

## 1. Business and cast

**Larkspur Motor Co.**, Garland, TX. One lot, 34 cars in stock, prices $7,995 to $15,900. Sells about 25 cars a month; about a third go out on the lot's own in-house loans (buy here pay here), the rest cash or an outside lender. 71 open in-house loans. Lot line (972) 555-0148. Runs Monday to Saturday, 9 am to 7 pm. No street address shown anywhere.

Staff (4):
- **Curtis Bramlett**, owner. Also acts as sales manager (gives the OK on deals) and backs up collections.
- **Yolanda Pierce**, finance manager. Writes loans, takes payments, works Collections every afternoon, does title work.
- **Andre Whitfield**, salesperson.
- **Luis Cantú**, salesperson.

Customers (10, all fictional):
| Name | Phone | Role in the screens |
|---|---|---|
| Terrence Mayfield | (469) 555-0132 | On the deal jacket: 2016 Chevrolet Equinox LT, trading a 2009 Chevrolet Impala, we finance it |
| Marisol Vega | (214) 555-0177 | Called after hours Monday, got a text back, AI booked her for today 5:30 pm on the 2017 Nissan Rogue SV |
| Brianna Holloway | (469) 555-0119 | In-house loan, 11 days behind, promised to pay today; the customer pay page is hers |
| Rodney Pruitt | (972) 555-0163 | In-house loan, missed his promise Saturday |
| Rosa Ibarra | (214) 555-0108 | In-house loan, promised today |
| Kim-Linh Tran | (469) 555-0145 | Sold Monday, loan not written yet, $1,000 down not recorded |
| Gary Lindqvist | (972) 555-0124 | Cash buyer Saturday, title owed |
| Jasmine Okoro | (214) 555-0151 | Test drive today 11:30 am, 2019 Kia Soul |
| Trey Lusk | (469) 555-0186 | Website lead this morning, 2014 Toyota Camry SE, nobody has taken him yet |
| Tasha Greer | (972) 555-0139 | Missed call this morning, texted back, "looking for a truck under $15k" |

Background names for collections rows only: Calvin Boateng, Darlene Fisk, Wendell Ochoa.

Sample day: **Tuesday, Nov 17**, about 10:40 am (owner and finance screens). The text thread is from Monday night. Do not use any name from the real demo (Mesquite Creek, Dale Whitaker, Rhonda Vasquez, Tina Nguyen, Marcus Bell, Jake Ortiz, Hector Saldana, Maria Lopez, Monica Lopez, Harold Ocampo, Antoinette Rhodes) or from Reids.

Cars used (stock # format `#26-0xxx`, miles, price):
- 2016 Chevrolet Equinox LT · #26-0214 · 118,400 mi · $11,995
- 2017 Nissan Rogue SV · #26-0198 · 96,210 mi · $12,850
- 2019 Kia Soul + · #26-0207 · 71,020 mi · $11,450
- 2014 Toyota Camry SE · #26-0221 · 151,300 mi · $8,495
- 2018 Hyundai Elantra SEL · (Brianna's loan, L-1162)
- 2015 Ford F-150 XLT · (Rodney's loan, L-1187)
- Kim-Linh's car: 2017 Honda Civic LX

---

## 2. Roles and what they need first

**Owner (Curtis)**, at the desk by 8:30 with coffee.
1. Money in today, split loan payments vs down payments and cash / card / check.
2. Who owes me: how many past due and how much, missed promises.
3. Sold deals not finished: loans not written, down payments not recorded, titles owed (Texas gives him 30 days).
4. Cars: incoming, in recon, not on the website, sitting past 60 days.
5. Leads nobody has called back, and sold / gross today and this month.
- Trust: the numbers add up and each one opens the list behind it. Dismiss: anything that looks like a CRM for plumbers ("jobs", "dispatch"), or a Money in today of $0.00.

**Finance manager (Yolanda)**, on the desktop in the office, Collections every afternoon.
1. Who to call first: missed promises, then promises due today, then days late.
2. For each loan: amount to bring current, days late, last paid, last contact, any promise.
3. One-tap Call, Text pay link, Log contact, Add promise from the row.
4. Take a counter payment with a receipt in seconds.
5. Loans not written and title work from sold deals.
- Trust: late fees one per missed payment, never stacked; amounts to the cent. Dismiss: a "dunning" or "invoice overdue" screen that reads like a utility bill.

**Salesperson (Andre)**, on his phone on the lot, walking a customer to a car.
1. My appointments today and who is coming in.
2. New leads to take ("Take it") before the other guy does.
3. Start a deal / Add customer in one tap.
4. Find a car: stock #, last 6 of VIN, make, model.
5. Text the customer from the lot line, with the thread.
- Trust: his customers stay his ("Andre Whitfield's customer"). Dismiss: seeing cost or other people's commissions (he never sees cost, gross or payoff), or a phone screen he has to pinch.

**Car buyer / loan customer (Brianna)**, on her phone, usually after work.
1. How much is due now.
2. Pay it by card without calling.
3. A receipt by text.
4. The lot's name and number she knows.
5. Nothing scary: no full balance history, no SSN, no address.
- Trust: it looks like the lot, shows her first name and the amount she expected. Dismiss: a long login, or a page that shows her whole loan to anyone with the link.

---

## 3. Words

| Bone | Car-lot word (as in the real kit) |
|---|---|
| Customer | Customer (a new one from the web or a call is a "lead"; a walk-in is an "up") |
| Visit | Appointment (test drive, bring in pay stubs / down payment) |
| Deal | Deal; its page is the **deal jacket**; the list of where each customer stands is **Pipeline** |
| Work item | The car: stock #, VIN, photos, recon in **Repairs**; status Incoming / In recon / Ready / Frontline / On hold / Sold / Wholesale |
| Money | Down payment, in-house **loan** (L-####), payment, late fee, promise (to pay), past due, to bring current, payoff, pay link, receipt, gross |
| Conversation | Texts, Phone (missed calls), "Texting from the lot line" |
| Automation | Missed-call text, AI receptionist, to-dos / Tasks, promise reminders |
| Team | Owner, Sales manager, Salesperson, Finance manager |
| Customer view | Pay page (pay link), public inventory page |
| Website link | "On your website now" / "Not on the website" per car |

**Owner nav (desktop sidebar, real order and groups):**
Every day: Home, Customers, Inventory, Deals, Loans, Tasks (badge "store-wide overdue 3") · Talk: Texts (4), Phone (1) · Office: Sales, Pipeline, Title work, Reports, Repairs · Setup: Settings, Help.
Owner phone tab bar: Home · Customers · Inventory · Loans · More.

**Finance manager nav (desktop):** Every day: Home, Customers, Inventory, Deals, Loans, Tasks · Talk: Texts, Phone · Office: Sales, Pipeline, Title work · Setup: Help. (No Settings, no Reports, no Repairs.)
Finance phone tab bar: Home · Customers · Deals · Loans · More.

**Salesperson nav:** Every day: Home, Customers, Inventory, Deals, Tasks · Talk: Texts, Phone · Office: Sales, Pipeline · Setup: Help. No Loans (the owner hasn't turned on counter payments for salespeople), no Title work, no Reports.
Salesperson phone tab bar (Phone is on): Home · Customers · Texts · Phone · More.

Header on desktop: page name or breadcrumb (e.g. "Customers › Terrence Mayfield › Deal jacket") and "Search customers…". Home title is the lot's name with a "How your lot runs" link on the right.

**Words that must NOT appear:** job, job ticket, work order, repair order (that's the shop set), dispatch, crew, tech on the way, on my way, service call, estimate (say quote), invoice / invoices (say payment, pay link), booking / book now, client, patient, guest, member, membership, subscription, Dashboard (say Home), Contacts (say Customers), Opportunities (say Pipeline), deal stage names like "Proposal" or "Negotiation", lead score, conversion rate, delinquent account, debtor, deadbeat, guaranteed approval, everyone approved, no credit check, buy now pay later, any lender brand name, "Demo: nothing was really sent".

---

## 4. The 6 screens

Every image: emerald kit, light canvas, white cards, and the bottom strip "Sample screens · sample data, not a real business". Car photos: realistic, no dealer signage, no readable plates (blank or "TEXAS" frame only).

### Screen 1. Owner home: "the lot's day"
Role: owner (Curtis Bramlett) · Desktop 1440x900 · Job: in 10 seconds, what came in, who owes, what's unfinished, how the cars are sitting.

- **Sidebar** (emerald): top block "Larkspur Motor Co." / "Curtis Bramlett · Owner". Owner nav as in section 3, Home active. Footer avatar "CB Curtis Bramlett".
- **Header band**: "Home" left, search "Search customers…" right.
- **Title row**: "Larkspur Motor Co." (large) left; "How your lot runs" (help icon, emerald link) right.
- **Next step** (full-width card with emerald outline): eyebrow "NEXT STEP", line "Loan not written: Kim-Linh Tran, $9,480.00 to finance", primary button "Write a loan".
- **Left column**
  - "TODAY'S MONEY": three tiles: "9 Payments due today" · "2 Promises due today" · "1 Missed promises" (the 1 in red).
  - Card "Money in today" with "$4,286.00" right. Line 1: "Loan payments $2,786.00 · Down payments $1,500.00". Line 2 (muted labels): "Cash $1,915.00 · Card $1,871.00 · Check $500.00". Small note: "A cash sale counts only when its money is recorded as a down payment."
  - Card "Owed": "6 past due · $1,788.83" (red text, links to Collections). Nothing else (no refunds, no repair bills).
  - Card two rows: "Today  2 sold · $5,840 gross · $4,286.00 in" / "This month  14 sold · $38,615 gross".
- **Right column**
  - "CARS": four tiles: "3 Incoming" · "4 In recon" · "2 Not on the website" · "5 Past 60 days" (5 in amber, not red).
  - "CUSTOMERS WAITING": muted line "2 waiting for a salesperson". Two rows:
    - "Trey Lusk · Website · 2014 Toyota Camry SE · 7:52 am" · button "Assign"
    - "Tasha Greer · Missed call, texted back · 8:15 am · "Looking for a truck under $15k"" · button "Assign"
  - "SOLD, NEEDS FINISHING": card "Loan not written" / sub "Sold on your paper: no payments come due until the loan is written." / row "Kim-Linh Tran, $9,480.00 to finance  Write a loan →". Then row "1 down payment not recorded · $1,000.00" / sub "Record it so the deal shows it's paid." / "Kim-Linh Tran  $1,000.00  sold 11/16 →". Then "Title work · 4 titles owed · Oldest: Gary Lindqvist, 3 days since sold →" (amber, not red).

### Screen 2. Signature: the deal jacket (we finance it)
Role: owner viewing Andre's deal · Desktop 1440x900 · Job: one customer, one car, the trade, the figures and how they pay, on one page, with the steps to the title.

- Sidebar as screen 1, "Deals" active. Header breadcrumb "Customers › Terrence Mayfield › Deal jacket", search right.
- **Jacket header** (left two-thirds): "Terrence Mayfield" (large), "How this works" link right. Buttons "Call" and "Text". Line: "Andre Whitfield's customer" · chip "Working" · chip "No OK needed". Muted line: "Quote 1 sent by text · Mon, Nov 16, 6:40 pm".
- **Step strip** (pills, in-house path, 6 steps): "✓ Car" · "✓ Figures" · "✓ How they pay" · "4 Sold" (emerald outline, current) · "5 Loan / Down payment" · "6 Title".
- **Left column**
  - Card "Car": photo of a silver 2016 Equinox; "2016 Chevrolet Equinox LT"; "#26-0214 · 118,400 miles"; chip "On hold". "Asking $11,995". Note: "On hold for Terrence Mayfield: bringing his down payment Wednesday after work, hold through Wednesday." Field "Change car" with "Choose".
  - Card "How they pay": legend "How are they paying?" with a three-way control "Cash | We finance it | Outside lender", **We finance it** selected. Muted line "The finance manager or owner writes the loan." Payment grid titled "Payments (estimate)": columns 30 mo / 36 mo / 42 mo, rows 21.99% and 23.99%:
    - 21.99%: $457.32 · $400.26 · $360.00
    - 23.99%: $467.98 · **$411.20** (selected, emerald fill) · $371.20
    Link "Change rates and terms". Collapsed row at the bottom: "Outside lender tools" with chevron and muted "paperwork, funding, stips, back end".
- **Right column**
  - Card "Trade": "2009 Chevrolet Impala LT · 188,000 miles · allowance $1,000.00". Fields: "Trade allowance $1,000" · "Payoff owed $0" · "ACV (what the trade is worth to us) $800". Line "Trade worth $1,000 more than owed".
  - Card "Figures": "Selling price $11,995.00" (muted "At asking") · "Trade equity −$1,000.00" · "Tax $687.19" · "Doc, title and registration $300.00" · "Down payment −$1,500.00" · bold "Balance to finance (estimate) $10,482.19". Link "Change fees and tax on this deal".
- **Sticky bottom bar** (white, full width of content): left "Payment picked: 23.99% · 36 months · $411.20 a month"; right buttons "Send new quote" (outline) and "Mark sold" (emerald).
- Math check (keep): 11,995 − 1,000 − 1,500 + 687.19 + 300 = 10,482.19. Tax is 6.25% of (11,995 − 1,000).

### Screen 3. Finance manager: Loans › Collections
Role: finance manager (Yolanda Pierce) · Desktop 1440x900 · Job: the afternoon call list, who to call first and what to say, without opening each loan.

- Sidebar: "Larkspur Motor Co." / "Yolanda Pierce · Finance manager", finance nav, "Loans" active. Header "Loans", search right.
- Title "Loans", sub "Who's behind, who promised, and every in-house loan."
- Tabs: **Collections** (active) · All loans · Credit reporting · Loans settings.
- Summary line (bold): "6 past due · $1,788.83".
- Bucket chips (only non-empty ones show): "Missed promises 1" (red outline) · "Promises due today 2" · "Due today 9" · "1–15 days 2" · "16–30 days 1".
- Section "Missed promises 1", card:
  - "Rodney Pruitt" · right side "$471.00" / "to bring current"
  - "L-1187 · 2015 Ford F-150 XLT · weekly $142.00"
  - "18 days late · $426.00 past due + $45.00 late fees"
  - "Last paid: Oct 23, $142.00 · Last contact: Nov 12, call, said Saturday"
  - Red chip "Missed promise: $250.00 on Sat, Nov 14"
  - Buttons: "Call" · "Text pay link" · "Log contact" · "Add promise"
- Section "Promises due today 2", two cards in the same shape:
  - "Brianna Holloway" · "$204.09 to bring current" · "L-1162 · 2018 Hyundai Elantra SEL · every two weeks $189.09" · "11 days late · $189.09 past due + $15.00 late fee" · "Last paid: Oct 23, $189.09 · Last contact: Nov 16, text, pay link sent" · emerald chip "Promised $204.09 today" · buttons "Call" · "Take payment" · "Text pay link" · "Log contact"
  - "Rosa Ibarra" · "$109.40 to bring current" · "L-1171 · 2014 Nissan Altima S · weekly $94.40" · "7 days late · $94.40 past due + $15.00 late fee" · "Last paid: Nov 3, $94.40 · Last contact: Nov 13, call, will pay by link" · chip "Promised $109.40 today" · same buttons (third card may be cut by the fold).
- Off-screen rows that make the totals true (not drawn, keep for consistency): Calvin Boateng 12 days $413.75; Darlene Fisk 4 days $189.09; Wendell Ochoa 23 days $401.50.

### Screen 4. Salesperson on the lot: "My day"
Role: salesperson (Andre Whitfield) · Phone 390x844 · Job: between customers, see who's coming, grab the new lead, start a deal or find a car.

- Top bar: menu icon, "Home", search icon.
- Title "Larkspur Motor Co." and link "How your lot runs".
- **Next step** card: "NEXT STEP" / "New lead nobody has taken: Trey Lusk, 2014 Toyota Camry SE" / button "Take it".
- **My day** section header with two buttons on the right: "Add customer" (outline) and "Start a deal" (emerald).
- Figure tiles, 3 columns × 2 rows:
  - "0 My new leads not reached" · "0 My to-dos overdue" · "4 My to-dos due today"
  - "2 My appointments today" · "6 My customers in progress" · "2 Store's leads nobody has taken · See them"
- **Find a car**: search field "Search stock #, last 6 of VIN, make, model…".
- **Due today** list (the bottom one may be cut by the tab bar):
  - "11:30 am · Test drive: Jasmine Okoro · 2019 Kia Soul +" (Call / Text icons)
  - "5:30 pm · Marisol Vega · 2017 Nissan Rogue SV · booked by the AI receptionist"
  - "Call Terrence Mayfield: confirm Wednesday down payment"
  - "Text Gary Lindqvist: his plates are in"
- Bottom tab bar: Home (active) · Customers · Texts (badge 1) · Phone · More.
- No cost, gross, payoff or anyone else's numbers anywhere on this screen.

### Screen 5. The customer: pay page from a texted pay link
Role: loan customer (Brianna Holloway) · Phone 390x844 · Job: pay this week's car payment by card in under a minute.

Styled as the lot's own page, not the staff app: white background, the lot's modest accent (deep navy #1F3A5F) for the header and button, no emerald sidebar, no tab bar.
- Header: "Larkspur Motor Co." (wordmark), "(972) 555-0148" with phone icon, "Garland, TX".
- "Hi Brianna," then heading "Make a payment".
- Card: label "Due now", amount "$204.09" large, small "Includes a $15.00 late fee."
- Two choices (radio): "Due now · $204.09" (selected) and "Another amount" (collapsed; when open its hint reads "Amount, from $1.00 to $8,912.40").
- Card checkout block titled "Pay by card": fields "Card number", "MM / YY", "CVC", "ZIP". Small lock icon "Secure card checkout".
- Full-width button "Pay $204.09".
- Muted: "You'll get a receipt by text." and "Questions? Call or text (972) 555-0148."
- Nothing else: no last name, no address, no SSN, no APR, no payment history, no balance list.

### Screen 6. The after-hours call that became an appointment
Role: salesperson (Andre) opening the thread Tuesday morning · Phone 390x844 · Job: show a missed call at night turning into a booked test drive with nobody at the lot.

- Top bar: "Texts", search icon. Thread header: back arrow, "Marisol Vega", sub "Texting from the lot line, (972) 555-0148", button "Call". Under it a muted row "Andre Whitfield" (whose customer).
- Thread (Mon, Nov 16):
  - System row, centered: "Missed call · 8:47 pm"
  - Out (lot, tagged "Missed-call text"), 8:47 pm: "Hi, this is Larkspur Motor Co. Sorry we missed your call. We open at 9 tomorrow. What can we help you with?"
  - In, 8:50 pm: "Is the gray Rogue on yall website still there? I need something for work"
  - Out (tagged "AI receptionist"), 8:50 pm: "Yes, the 2017 Nissan Rogue SV is still on the lot. Want to come see it and take a drive? We have Tuesday at 11:30 am or 5:30 pm."
  - In, 8:52 pm: "5:30 works. Do you do financing at the lot? My credit isn't great"
  - Out (tagged "AI receptionist"), 8:52 pm: "We do offer financing here at the lot. Andre can go over everything with you in person. You're set for Tuesday at 5:30 pm with Andre Whitfield. Please bring your driver's license and a recent pay stub."
  - In, 8:53 pm: "ok thank you"
  - System card: "Appointment booked · Tue, Nov 17, 5:30 pm · Andre Whitfield · Test drive: 2017 Nissan Rogue SV" with a small "Open" link.
- Reply box "Text message", paperclip, send button.
- Bottom tab bar: Home · Customers · Texts (active) · Phone · More.

---

## 5. How it uses the bones

| Screen | Shared records it reads |
|---|---|
| 1 Owner home | Money (payments, down payments, by method, past due), Deal (sold, gross, needs finishing), Customer + Conversation (leads waiting, missed call), Work item + Website link (cars by status, not on the website), Team (overdue to-dos), Automation (promises due) |
| 2 Deal jacket | Deal, Customer, Work item (the car and the trade), Money (figures, payment grid, down payment), Conversation (quote sent by text), Team (whose customer, OK needed) |
| 3 Collections | Money (loans, past due, fees, promises, payments), Customer, Conversation (last contact, pay link sent), Automation (promise reminders) |
| 4 Salesperson my day | Visit (appointments), Customer (leads), Deal (customers in progress, Start a deal), Work item (Find a car), Automation (to-dos), Team (mine vs store) |
| 5 Pay page | Customer view, Money (amount due, card payment, receipt) |
| 6 Text thread | Conversation, Automation (missed-call text, AI receptionist), Visit (appointment booked), Customer, Team (assigned salesperson), Website link (the car on the site) |

Note for the backend: in the real Dealer Suite the car (inventory) and the in-house loan are their own records; for the shared bones treat the car as a Work item published through Website link, and the loan as a Money record with a payment schedule.

---

## 6. Watch-outs

- **Texts never carry a balance or amount owed** (real kit rule). The pay link text only says the link is there; the amount shows on the pay page.
- **Pay page**: first name only; no SSN, no address, no balance history, no APR. Card through a secure checkout.
- **AI and auto texts never quote a price, payment, APR, down payment or approval.** No "guaranteed approval", "everyone drives", "no credit check", "$X down" (Truth in Lending advertising triggers; Texas). The AI books the visit and hands numbers to a person.
- **No outbound texts after 9 pm or before 8 am** in samples; the AI reply in screen 6 is an answer to her own texts and ends at 8:53 pm.
- **Role walls**: a salesperson never sees car cost, gross or a loan payoff; finance and owner do. (Screen 2 is drawn as the owner for that reason.) Salespeople have no Loans page unless the owner turns on counter payments.
- **Late fees**: one per missed payment, never stacked on a partly paid one (FTC Credit Practices Rule, built into the kit). Show fees as "+ $15.00 late fee", never as penalties or interest piles.
- **Collections tone**: "past due", "to bring current", "promise", "last contact". No repossession, charge-off, 90+ days rows or bureau talk on the sample screens; they exist in the kit but scare a prospect in a sample.
- **APR shown only on the owner's deal jacket**, and plausible (21.99% to 23.99%). Never on customer-facing screens.
- **No lender names** (real or invented) anywhere. On a we-finance-it deal the outside-lender cards stay folded under "Outside lender tools", as in the kit.
- **Keep from the real kit**: the "Next step" card on every Home; "How your lot runs"; the in-house step strip Car → Figures → How they pay → Sold → Loan / Down payment → Title; "How are they paying? Cash · We finance it · Outside lender"; the jacket's Trade card with allowance / payoff / ACV and "Trade worth $X more than owed"; Collections tabs and bucket chips; Call · Text pay link · Log contact · Add promise; Money in today with "A cash sale counts only when its money is recorded as a down payment."; the role tab bars; each number is a count of a list (keep counts consistent across screens, as above).
- **Drop from the real kit**: gold/black theme, "Demo" tags in bubbles, the grey "Demo inventory" strip, "Quote 1 not really sent (demo)", placeholder car silhouettes (use real-looking photos), 325 area codes, Mesquite address.
- **Numbers that must agree across screens**: 6 past due · $1,788.83 (screens 1 and 3); 9 due today, 2 promises due today, 1 missed promise (1 and 3); Kim-Linh $9,480.00 loan not written and $1,000.00 down (1); 2 store leads waiting, Trey and Tasha (1 and 4); Marisol 5:30 pm today (4 and 6); Brianna $204.09 (3 and 5).
