# Salon & Spa screen brief (salon-spa)

Truth source: the real salon kit (`top-shelf-crm-salon`, branch feat/salon-kit): spec `2026-11-23-salon-kit-design.md`, plans S0, S1, S2a, S2b, `app/Industries/Salon/SalonIndustry.php`, the checkout pages, and the S0 verify screenshots. Words in "quotes" below are the kit's own strings. Keep them exactly.

All screens are dated **Friday, Dec 4, 2026** unless a screen says otherwise.

---

## 1. Business and cast

**Studio Marlowe Salon & Spa**, McKinney TX. One location: 6 styling chairs, 2 nail stations, 2 treatment rooms. 9 people. Open Tue-Sat 9:00 AM to 7:00 PM, closed Sun-Mon. Phone (469) 555-0118. Runs on the Hair salon preset (deposits 25%, 48-hour cancellation window, late cancel / no-show fee 50%, tip buttons 18 / 20 / 25%).

| Person | Role in the CRM | Title shown | Color dot |
|---|---|---|---|
| Harper Marlowe | Owner (also books clients) | Master stylist, colorist | plum #7c3aed |
| Bree Callahan | Front desk | Front desk | (not bookable) |
| Lena Ortiz | Staff | Master stylist | teal #0d9488 |
| Jade Mercer | Staff | Senior stylist | rose #db2777 |
| Tess Navarro | Staff | Junior stylist | amber #d97706 |
| Dani Fox | Booth renter | Booth renter | slate #64748b |
| Camila Reyes | Staff | Nail tech | coral #f97316 |
| Sofia Lind | Staff | Esthetician | sky #0284c7 |
| Rafael Ochoa | Staff | Massage therapist | olive #65a30d |

Clients (all fictional, 555 numbers): Olivia Grant (469) 555-0182, Ava Linden (469) 555-0340, Brooke Adler, Tara Quinn, Eli Vance, Ryan Feld, Natalie Shore, Kayla Ross, Mei Chen, Holly Vance, Rachel Ames, Kim Abbott (214) 555-0147.

---

## 2. Roles and what they need first

**Owner (Harper), 7 AM on the couch, then between her own clients**
1. Is today full, person by person, and where are the open gaps?
2. Who hasn't confirmed for tomorrow?
3. Did yesterday's drawer match (day close)?
4. Who is past due to come back and hasn't booked?
5. What the booth renter owes or is owed, and that rent came in.
Trust: she sees each chair's day as a strip with color processing time shaded, the way she reads her book. Dismiss: home-service money tiles ("Still owed", "Quotes") or seeing her renter's clients (renters will leave over that).

**Front desk (Bree), phone ringing, client at the counter**
1. Who's next to arrive and who's already checked in.
2. Check out a visit fast: lines by person, deposit already applied, tip, card on file or reader.
3. Book the next visit before the client walks out.
4. Send the receipt by text.
5. Who's calling (caller's name and their next appointment).
Trust: the deposit is already on the ticket and the tip splits itself between the colorist and the assistant. Dismiss: an "invoice" flow or retyping services.

**Stylist (Jade), one hand, gloves on, between foils**
1. My next client and what time.
2. Last visit's formula, notes and before/after photos.
3. Is someone booked into my processing time?
4. Mark checked in / in chair / done.
5. An open hour I could fill.
Trust: the formula from last time is right there. Dismiss: seeing the whole salon's money, or a screen built for a desk.

**Client (on her phone at 9 PM)**
1. The service, how long, the price.
2. Pick her stylist (or any).
3. A real time that's free.
4. The deposit and the cancellation rule in plain words, before she pays.
5. A text reminder she can confirm with one letter, and a link to move it.
Trust: it looks like the salon, not an app, and the fee rule is said up front. Dismiss: surprise fees, or having to make an account.

---

## 3. Words

| Bone | Salon word |
|---|---|
| Customer | client ("Clients") |
| Visit | appointment; states "Booked", "Confirmed", "Checked in", "In chair", "Done", "No-show", "Cancelled" |
| Deal | not used (the kit turns Opportunities off; no pipeline) |
| Work item | ticket ("Ticket"); per-visit notes, formula and before/after photos on the client |
| Money | ticket, "Deposit", tip, "Tip split", "No-show fee", "Late cancel fee", "Owes", receipt, "Day close", "Takings", "Booth rent", "Payout", pay report |
| Team | Owner, Manager, Front desk, Stylist, Booth renter (titles: Master / Senior / Junior stylist, Nail tech, Esthetician, Massage therapist) |
| Place | the person's column (chair) |

**Nav, owner (desktop sidebar, kit order and groups):** Every day: Today, Calendar, Checkout, Contacts · Talk: Texts, Phone · Grow: Reputation, Campaigns · Setup: Automations, Pay, Settings.
**Nav, front desk:** Every day: Today, Calendar, Checkout, Contacts · Talk: Texts, Phone · Setup: Pay.
**Nav, stylist / renter (phone bottom tabs, kit):** Today, Calendar, Contacts, Texts, More (More holds Checkout, Pay, Phone).

**Must NOT appear:** job, work order, technician or "tech" on its own (only "Nail tech" as a title), dispatch, on my way, route, crew, truck, estimate, quote, invoice, proposal, lead, pipeline, deal, opportunity, customer, patient, member, membership, class, warranty, parts, diagnosis, treatment plan, chart, "Balance due", "Still owed", "Collected", "Bookings" (as nav), "Inbox", "Mail", "Commissions" (as nav), "Cash" (as nav), "In progress", "Completed", "Assigned to", gift card, package, waitlist, room booking, retail stock (phase 2, not built).

---

## 4. The 6 screens

Every image: bottom strip "Sample screens · sample data, not a real business". Staff screens use the emerald Top Shelf CRM kit. Screen 5 is styled as the salon.

### Screen 1. Owner home ("Today"), desktop 1440x900
Job: Harper sees every chair's day at a glance, then what needs her.

- **Sidebar (240px, emerald):** "Studio Marlowe Salon & Spa"; owner nav above with Today active; Texts badge "2"; footer avatar HM "Harper Marlowe · Owner".
- **Header band (emerald):** "Good morning, Harper" / "Friday, Dec 4 · 40 appointments · 4 open slots". Right: toggle "Mine | Whole team" (Whole team selected, kit control), search "Search contacts...".
- **Card A, full width: "Today's appointments" by person.** Hour axis 9 AM to 7 PM across the top. One row per person: color dot, name, title under it in small gray, count at right ("5 appointments"). Each row is a horizontal bar of blocks: solid color = booked; same color with diagonal stripes = processing time (labeled "Processing" when wide enough); gray hatched = break; dashed outline with label = open time. Blocks at 7 AM are all "Confirmed" (solid) or "Booked" (60% opacity solid).
  - No client names on these bars (the Calendar has them). Times only.
  - Harper Marlowe · Master stylist · 5: 9:00-12:00 (stripe 10:00-10:45), 10:00-10:30 drawn inside the stripe, break 12:00-12:30, 12:30-2:30, 3:00-4:15, 5:00-5:45.
  - Lena Ortiz · Master stylist · 6: 9:00-9:45, 10:00-11:45 (stripe 10:30-11:15), 12:00-1:00, break 1:00-1:30, 1:30-3:30, 4:00-4:45, 5:00-6:00.
  - Jade Mercer · Senior stylist · 6: 9:00-10:15, 10:30-12:15 (stripe 11:00-11:40), 11:05-11:35 inside the stripe, 12:30-1:15, open dashed 1:30-2:30 "1 hr open", 2:30-3:30, 4:00-5:45.
  - Tess Navarro · Junior stylist · 5: 9:30-10:15, 10:45-11:30, 11:45-12:15, open dashed 12:30-1:30 "1 hr open", 2:00-2:45, 4:00-4:45.
  - Dani Fox · Booth renter · 5: four slate blocks each labeled only "Booked" (9:00-10:00, 10:15-11:45, 12:00-12:45, 1:30-3:00, 3:30-4:30). No names anywhere on this row.
  - Camila Reyes · Nail tech · 6: 9:00-10:00, 10:00-11:15, 11:30-12:30, 1:00-2:00, open dashed 2:00-3:00 "1 hr open", 3:00-4:00, 4:30-5:30.
  - Sofia Lind · Esthetician · 4: 9:30-10:00, 11:00-12:00, 1:00-2:00, 3:00-3:30.
  - Rafael Ochoa · Massage therapist · 3: 10:00-11:30, 1:00-2:00, open dashed 3:00-4:00 "1 hr open", 4:00-5:30.
  - Card footer line: "Open today: Jade 1:30 · Tess 12:30 · Camila 2:00 · Rafael 3:00" each a link "Book".
- **Row B, three columns under Card A:**
  - **Col 1 "Waiting on you (4)"** (kit section name; rows are kit Today rows with Call / Text buttons):
    - "Not confirmed: Kayla Ross" / "Tomorrow 9:30 AM · Sofia Lind" [Call] [Text]
    - "Not confirmed: Denise Whitfield" / "Tomorrow 11:00 AM · Rafael Ochoa" [Call] [Text]
    - "Unpaid: Carla Benson" / "Owes $18.00" [Open ticket]
    - "Payout ready: Dani Fox" / "Nov 15 to Nov 28 · gross $1,532.00 · card fees $45.60 · net owed $1,486.40" [Open Pay]
    - small gray line under the list: "Couldn't book Ryan Feld's standing appointment on Fri 12/25" [Got it]
  - **Col 2 "Due back (3)"**, subtitle "Not booked and past their usual time":
    - Rachel Ames · Root touch-up · last in Oct 9 with Lena (8 weeks) [Text]
    - Jordan Lee · Men's cut · last in Oct 30 with Tess (5 weeks) [Text]
    - Tina Moss · Gel manicure · last in Nov 6 with Camila (4 weeks) [Text]
    - then "Birthdays (2)" (kit section): "Mei Chen · Sat 12/5" [Text], "Tara Quinn · Tue 12/8" [Text]
  - **Col 3 "Day close · Thu 12/3"** card:
    - "Takings $3,486.00" big, gray "By method, after refunds, tips included" (kit line)
    - Card reader $2,418.00 · Card on file $296.00 · Cash $412.00 · Online $360.00
    - "Tips $512.00"
    - "Expected in the drawer $412.00 · Counted $412.00" with an emerald check "Matches"
    - "Dani Fox (booth renter): cash $85.00, hers" (one line, kit rule)
    - link "Open day close"
    - below, small card "Booth rent": "Dani Fox · $325.00 weekly · Paid Mon 11/30"
    - below, small card "Reputation": "4.9 ★ · 212 reviews · 3 new this week · 1 to reply to"

### Screen 2. Signature: the day by chair ("Calendar"), desktop 1440x900
Job: the whole floor's day in columns per person, with color processing time other clients are booked into.

- **Sidebar collapsed to an icon rail (72px)**, Calendar icon active.
- **Page head (kit layout):** title "Appointments", sub-links "Services · Stylists". Controls row: [<] "Friday, Dec 4" [>] [Today] date field "12/04/2026". Right: emerald button "+ Book an appointment".
- **State legend chips** under the controls: Booked (outlined) · Confirmed (solid light) · Checked in (amber dot) · In chair (emerald dot) · Done (gray check) · No-show (none today; omit the chip).
- **Grid:** time gutter 9:00 to 3:00 down the left (about 110px per hour), a thin emerald now-line at 10:40 labeled "10:40". Six columns visible, header = color dot, name, title small, count. A chip at the right edge "Sofia, Rafael →" (scroll).
  - **Harper Marlowe · Master stylist · 5**
    - 9:00-12:00 Olivia Grant · Balayage & toner · "In chair" · small "$ Deposit $55" badge. Inside it, 10:00-10:45 is striped and labeled "Processing". This card is selected (emerald 2px outline).
    - 10:00-10:30 Ryan Feld · Men's cut · "Done" · repeat icon (standing, every 3 weeks). Drawn inside the striped band, offset right.
    - 12:00-12:30 gray hatched "Break".
    - 12:30-2:30 Natalie Shore · Bridal trial: updo · "Confirmed" · "$ Deposit $30".
  - **Lena Ortiz · Master stylist · 6**
    - 9:00-9:45 Holly Vance · Women's cut · "Done"
    - 10:00-11:45 Claire Bell · All-over color · "In chair" · stripe 10:30-11:15 "Processing"
    - 12:00-1:00 Grace Wynn · Women's cut & blowout · "Confirmed"
    - 1:00-1:30 "Break"
    - 1:30-3:00+ Sasha Bloom · Highlights · "Booked"
  - **Jade Mercer · Senior stylist · 6**
    - 9:00-10:15 Brooke Adler · Women's cut & blowout · "Done"
    - 10:30-12:15 Tara Quinn · Partial highlights · "In chair" · stripe 11:00-11:40
    - 11:05-11:35 Eli Vance · Men's cut · "Confirmed" (inside the stripe)
    - 12:30-1:15 Kim Abbott · Blowout · "Confirmed"
    - 1:30-2:30 empty with faint "+ 1 hr open"
    - 2:30-3:00+ Leah Stone · Women's cut · "Confirmed"
  - **Tess Navarro · Junior stylist · 5**
    - 9:30-10:15 Mila Shaw · Kids' cut · "Done"
    - 10:45-11:30 Jordan Pike · Men's cut · "Confirmed"
    - 11:45-12:15 Olivia Grant · Blowout finish · "Booked" (same visit as Harper's; tiny link icon)
    - 12:30-1:30 "+ 1 hr open"
    - 2:00-2:45 Nora Kett · Blowout · "Booked"
  - **Dani Fox · Booth renter · 5**: slate blocks with only "Booked" and the time (9:00-10:00, 10:15-11:45, 12:00-12:45, 1:30-3:00). No name, no service, no state.
  - **Camila Reyes · Nail tech · 6**
    - 9:00-10:00 Paige Turner · Gel manicure · "Done"
    - 10:00-11:15 Mei Chen · Spa pedicure · "In chair"
    - 11:30-12:30 Rosa Diaz · Gel manicure · "Confirmed"
    - 1:00-2:00 Joy Hale · Gel fill · "Booked"
    - 2:00-3:00 "+ 1 hr open"
- **Visit panel (right drawer, 400px, white)** for Olivia Grant:
  - Name "Olivia Grant", "(469) 555-0182", chips "In chair" and "Deposit $55 paid".
  - "Services": Balayage · Harper Marlowe · 9:00 · $185.00; Toner · Harper Marlowe · 10:45 · $35.00; Blowout finish · Tess Navarro · 11:45 · $40.00.
  - "Last visit": Sep 25 with Harper · Balayage & toner.
  - "Formula (Sep 25)": "Lightener + 20 vol, foils, 35 min · Toner 9V + 9P, 15 min".
  - "Notes": "Keep the money piece bright. Coffee, oat milk."
  - Two photo thumbnails "Before" / "After" (Sep 25).
  - Buttons: primary "Done", secondary "Hand to ▾" (kit), "Checkout", text link "Save notes".

### Screen 3. Front desk checkout ("Ticket"), desktop 1440x900
Job: Bree rings out a color visit with two people on it, deposit applied, tip split, next visit booked.

- **Sidebar:** front desk nav, Checkout active; footer "Bree Callahan · Front desk".
- **Header band:** "Checkout" / breadcrumb "Checkout › Olivia Grant · Fri 12/4". Time shown nowhere else; it's 12:18 PM.
- **Left column (60%), "Ticket" card:**
  - Top line: "Olivia Grant · (469) 555-0182" and chip "Open". Under it: "Appointment 9:00 AM to 12:15 PM with Harper Marlowe and Tess Navarro".
  - Table headers "What · Team member · Price":
    - Balayage · Harper Marlowe · $185.00
    - Toner · Harper Marlowe · $35.00
    - Bond treatment (add-on) · Harper Marlowe · $30.00
    - Blowout finish · Tess Navarro · $40.00
    - link "+ Add something else", link "Discount"
  - "Totals": Subtotal $290.00 · Tax $0.00 · Total $290.00
  - "Payments": "Deposit · Online · Tue 11/24 · -$55.00". Bold "Left to pay $235.00".
  - "Tips": chips 18% $52.20 · **20% $58.00** (selected) · 25% $72.50 · Other. Gray note "Tips aren't part of the total."
  - "Tip split": Harper Marlowe $50.00 · Tess Navarro $8.00 · link "Edit".
- **Right column (40%):**
  - **"Take a payment"** (kit pay sheet): "How they paid" segmented: Card reader ("Front desk reader · Ready") · **Card on file** (selected, "Visa •• 4417, saved 11/24") · Cash · Other. Amount $235.00, Tip $58.00. Big emerald button "Take $293.00".
  - **"Book next visit"** card: "Balayage & toner with Harper · usually every 10 weeks". Three time chips: "Tue 2/9 · 9:00 AM", "Fri 2/12 · 9:00 AM", "Sat 2/13 · 10:00 AM", link "Pick another time".
  - **"Send receipt"**: buttons "Text" and "Email", grayed with note "After it's paid". Gray line: "A review request goes to Olivia by text after it's paid."
- **Toast bottom right (incoming call):** phone icon "Incoming · Kim Abbott · (214) 555-0147" / "Next: Blowout today 12:30 PM with Jade" buttons [Answer] [Let the AI answer].

### Screen 4. Stylist on the floor ("Calendar", one column), phone 390x844
Job: Jade sees her client in the chair with last time's formula, and who's booked into her processing time.

- **Top bar:** "Calendar", picker "Jade Mercer ▾" (kit's one-column-at-a-time view), date "Fri, Dec 4", right "10:50 AM".
- **Summary line:** "6 appointments · open 1:30 to 2:30".
- **Now card (expanded, emerald left border):**
  - "10:30 · Tara Quinn" chip "In chair"; "Partial highlights"; band "Processing · 50 min left (until 11:40)".
  - "Last visit Oct 9 with you · Partial highlights · $145.00"
  - "Formula (Oct 9)": "Lightener + 20 vol, foils, 35 min · Gloss 9N + 9V, 20 min"
  - "Notes": "Face-framing pieces, no bangs. Likes it cool."
  - Two photo thumbs "Before" / "After" (Oct 9) and a "+ Photo" tile.
  - Buttons (44px tall): primary "Done", secondary "Hand to ▾".
- **Next card:** "11:05 · Eli Vance" chip "Checked in"; "Men's cut · 30 min"; amber note "In your processing time"; button "Start" (sets "In chair").
- **Compact list:** 9:00 Brooke Adler · Women's cut & blowout · Done ✓ · "Paid" / 12:30 Kim Abbott · Blowout · Confirmed / 1:30 "1 hr open" (dashed) / 2:30 Leah Stone · Women's cut · Confirmed / 4:00 Nina Ford · Root touch-up · Booked.
- **Bottom tabs (kit):** Today, **Calendar** (active), Contacts, Texts, More.

### Screen 5. Client booking page ("Book an appointment"), phone 390x844
Job: a new client picks a facial, her esthetician and a time, and sees the deposit and fee rule before paying.

Styled as the salon, not the CRM: off-white background #faf7f5, accent dusty rose #b76e79, serif headings. No emerald, no CRM nav.
- **Top:** "Studio Marlowe Salon & Spa" / "McKinney, TX · (469) 555-0118".
- **Title** "Book an appointment" / gray "Step 3 of 4" / "< Back".
- **Picked card:** "Signature facial · 60 min · $100.00" / "with Sofia Lind, Esthetician" / link "Change".
- **"Pick a day and time"**: date pills Tue 12/8 · Wed 12/9 · Thu 12/10 · Fri 12/11 · **Sat 12/12** (selected).
- **Times for Sofia, Sat 12/12:** 9:00 AM · **10:30 AM** (selected, rose fill) · 1:00 PM · 2:30 PM · 4:00 PM.
- **Policy box (light rose):** "A $25.00 deposit holds your time and comes off your bill. Cancel or move it free up to 48 hours before, from the link in your reminder. After that, or if you miss it, the fee is 50% ($50.00), and your deposit counts toward it."
- **Button (rose, full width):** "Next: your details".

### Screen 6. The text thread (Texts), phone 390x844
Job: an after-hours call the AI receptionist booked, the deposit hold, the reminder, "C" to confirm, and an add-on, all in one thread.

- **Header:** back arrow, "Ava Linden", "(469) 555-0340", call icon. Chips under it: "Next: Sat 12/5 · 10:00 AM · Lena" and "Deposit $30 paid".
- **Thread (oldest at top):**
  1. Gray day label "Tue 12/1".
  2. **AI receptionist card** (full-width, light emerald): "AI receptionist answered · 7:42 PM · 2 min" / "Ava wanted her root touch-up with Lena. Booked Sat 12/5 at 10:00 AM: Root touch-up & gloss, 1 hr 45 min, $120.00. Sent the deposit link." / links "Play" "Transcript".
  3. Outgoing 7:44 PM: "Studio Marlowe Salon & Spa: your appointment on Sat 12/5 at 10:00 AM is held until 8:44 PM. To keep it, pay the $30.00 deposit here: studio-marlowe.example/appt/7KQ2"
  4. Gray system line 7:51 PM: "Deposit paid $30.00".
  5. Gray day label "Fri 12/4".
  6. Outgoing 10:00 AM: "Hi Ava, this is Studio Marlowe Salon & Spa: your Root touch-up & gloss with Lena Ortiz is Sat 12/5 at 10:00 AM. Reply C to confirm, or change it here: studio-marlowe.example/m/7KQ2"
  7. Incoming 10:12 AM: "C! Could I add a brow wax too?"
  8. Outgoing 10:12 AM (small "auto" tag): "Thanks, Ava. You're confirmed for Sat 12/5 at 10:00 AM."
  9. Outgoing 10:20 AM (tag "Bree"): "Done! Brow wax with Sofia at 11:45, right after your color. See you tomorrow."
- **Composer:** paperclip, "Text message", send.

---

## 5. How it uses the bones

| Screen | Shared records it reads |
|---|---|
| 1 Owner home | Visit (by Team member, states, processing gaps), Customer (birthday, last visit, due back), Money (unpaid ticket, day close, payout, booth rent), Automation (standing skipped, due-back), Reputation counts |
| 2 Day by chair | Visit + its lines (staff, service, start, processing), Team (columns, titles, colors, renter flag), Customer (name, phone), Work item (formula, notes, photos), Money (deposit) |
| 3 Checkout | Work item (ticket lines by Team member), Money (deposit payment, tip, tip split, card on file, reader), Visit (book next), Automation (receipt, review request), Conversation (incoming call) |
| 4 Stylist phone | Visit (own column, states), Work item (formula, notes, photos), Customer (last visit) |
| 5 Booking page | Customer view, Visit (availability by Team member), Money (deposit, fee rule), Website link |
| 6 Text thread | Conversation (AI receptionist call, texts), Automation (hold text, reminder, reply-C confirm), Money (deposit paid), Visit |

---

## 6. Watch-outs

- **Renter privacy is the trust point.** The owner sees a booth renter's day only as slate "Booked" blocks with times: no client name, service, state or money. Renter money reaches the owner as one payout line (gross, card fees, net) and one day-close cash line. Never draw a renter's client anywhere the owner looks.
- **Fees are a staff tap, never automatic.** If a no-show is drawn anywhere, its button reads "Charge $X no-show fee" with a confirm. The fee rule on the booking page must say the deposit counts toward it.
- **Tips are separate from the total** and split by service share (Harper $50.00 / Tess $8.00 on a $58.00 tip). Don't add the tip into "Total".
- **Processing time is the signature detail.** Draw it striped inside the color visit, with another client booked into it in the same column. That is what makes a stylist believe it.
- **Use the kit's exact strings:** states "Booked / Confirmed / Checked in / In chair / Done / No-show", sections "Today's appointments / Waiting on you / Birthdays", "Not confirmed: {name}", "Unpaid: {name}", "Owes $X", "Book next visit", "Take a payment", "Left to pay", "Tip split", "Day close", "Expected in the drawer", "Hand to", "+ Book an appointment", the reminder and hold text wording, "Reply C to confirm".
- **Formula, notes and photos are staff-only.** Never on the booking page, receipt or texts. No health or body notes for massage or facials; skip the allergies field in the samples.
- **Not built, so don't show:** rooms booked with a visit, gift cards, packages or memberships, retail stock, intake forms, a waitlist, Reserve with Google, payroll paid out. Walk-ins (tablet check-in, "you're next") exist only on the Barbershop preset; leave them out of a salon & spa set.
- **Two kit gaps for Taylor (draw as written, but decide):** (1) the kit's nav label is "Contacts" although its words say "Clients"; a salon owner would expect "Clients". (2) The Hair salon preset has one staff word ("Stylist") and levels Junior / Senior / Master stylist, so a mixed salon & spa's "Stylists" tab also lists the nail tech, esthetician and massage therapist; the titles shown here assume editable level names.
- **Look:** real kit screenshots use the sample's dark gold theme; these samples use the emerald Top Shelf kit per BONES. The booking page uses the salon's own rose accent.
- **Don't repeat the rejected draft:** no money KPI tiles across the top, no week view, no Invoices / Quotes / Commissions / Cash in the nav, no "Quote approved, not booked", no "Balances due".
