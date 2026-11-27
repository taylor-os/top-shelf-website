# Veterinary: screen brief (slug `vet`)

Business is fixed: **Wellspring Animal Hospital**, the sample site at `websites/wellspring-animal-hospital/`. The screens use its team, services, hours, address, voice and look (customer view only). No real Top Shelf vet kit exists, so this brief sets the standard.

Sample day for every screen: **Wednesday, Dec 2, 2026** (dental uses Tue Dec 1, salon Fri Dec 4).

---

## 1. Business and cast

**Wellspring Animal Hospital**, full-service small-animal hospital (dogs and cats), Cedar Hollow neighborhood (placed in Flower Mound, TX for the sample; the site never names a city, so the screens only ever show "24 Cedar Hollow Road"). One location, since 2015. 3 exam rooms (Exam 3 is the **Cat room**, the site promises separate cat and dog spaces), 1 surgery suite. 5 staff on the screens.
Phone on screens: **(972) 555-0153** (the site's 123-456-7890 is a placeholder; never show it). Hours: Mon-Fri 8 AM-6 PM, Sat 8 AM-2 PM, closed Sun. Lunch 12:30-1:30 (AI receptionist answers).

Team (the first three are the site's own team page; the last two are added because the site mentions "the wider care team" without names)
| Name | Role in CRM | Title shown | Where they work today | Color dot |
|---|---|---|---|---|
| Dr. Elena Cho, DVM | Owner | Lead veterinarian | Exam 1 + Cat room | forest #1E6B54 |
| Dr. Marcus Reed, DVM | Veterinarian | Associate vet, surgery & dentistry | Surgery suite AM, Exam 2 PM | indigo #4F46E5 |
| Priya Shah | Manager | Practice manager & lead tech | everywhere, curbside | (not bookable) |
| Jesse Kimbrough, LVT | Staff | Vet tech | Exam 2 AM (tech visits), drop-offs | amber #D97706 |
| Callie Dunaway | Front desk | Front desk | front desk | (not bookable) |

Clients (the person is the **client**, the pet is the **patient**; always show pet first, owner second)
| Pet | Client | Story | Screens |
|---|---|---|---|
| Hazel (dog, 9) and Tofu (cat, 3) | Joanna Pruneda, (972) 555-0181 | Hazel's dental drop-off Dec 10 with deposit paid; Tofu due for annual wellness | 1, 3, 5 |
| Pepper (dog, 2) | Lacey Arbuckle, (940) 555-0174 | Chocolate call, AI transfers to a human, same-day sick visit 10:45 | 2, 3, 6 |
| Bandit (dog, 1) | Teo Villarreal | Neuter drop-off, ready for pickup, pay link | 1, 2, 4 |
| Waffles (cat, 6) | Grant Eckhart | Dental cleaning drop-off | 1, 2, 4 |
| Mabel (dog, 7 mo) | Sheila Driscoll | Spay drop-off | 1, 2, 4 |
| Clementine (puppy, 10 wks) | Hannah Stroud | NEW, booked by AI receptionist Sunday | 1, 2, 3 |
| Sir Pounce (cat, 4) | Omar Belhadj | NEW, booked by website chat; records from old clinic received | 1, 2, 3 |
| Duke (dog, 13) | Wendell Quarles | Senior wellness, checked out this morning | 2 |
| Biscotti (dog, 5) | Marguerite Dowell | In Exam 1 at 10:40, checking out at 10:47 | 2, 3 |
| Ziggy and Lulu (cats) | Nora Tibbetts | Two cats, one appointment, Family badge | 2, 3 |

Filler (schedule rows only; pet · client): Gus · Teresa Gentry, Miso · Yuki Nakamura, Nala · Sabrina Hutchins, Maple · Jerome Abernathy, Rufus · Paul Dempsey, Pixel · Ana Escobedo, Moose · Vince Mancuso, Bear · Lindsey Yancey, Tank · Mitch Hightower, Lola · Gina Cantu, Finn · Kyle Spurlock, Coco · Lorena Ruelas, Peanut and Pumpkin · Laura Kemper, Koda · Ben Sheffield, Bruno · Rosa Zamora, Roxie · Dana Gaskins, Ollie · Ray Pickens, Daisy · Tim Ostrander, Lady · Celeste Thibodeaux, Bodie · Kara Yoakum, Sully · Paige Whitcomb, Winnie · Courtney Lattimore, Juno · Felix Ambrose, Buster · Arlo Kincannon, Cleo · Nolan Fitzhugh, Sadie · Joy Vanderpool.
Every client surname above was checked against `screens/*/*.html` and `briefs/*.md`: none is used by another industry. Do not reuse the site's testimonial pets (Biscuit, Mochi, Willow) as clients.

Emergency hospital used for after-hours routing (fictional): **Wrenfield Animal ER, (972) 555-0199**.

---

## 2. Roles and what they need first

**Owner, Dr. Elena Cho** (in exam rooms all day; looks at 7:15 AM and at lunch)
1. Today by doctor: how full, where the same-day sick slots are held.
2. Drop-offs: who is coming in for surgery and dental, are estimates approved and deposits paid.
3. Who hasn't confirmed, so a slot doesn't go empty.
4. New clients this week and whether the after-hours and lunch calls got booked; any urgent after-hours call routed to the ER and followed up.
5. Money left on the table: approved estimates not booked, open pay links, reminders due this month not booked; reviews to reply to.
Trust: it shows her day the way she thinks about it (rooms, doctors, held sick slots, morning drop-offs) and urgent calls go to a person or the ER, never to a robot giving advice. Dismiss: it looks like it wants to replace her practice software (records, labs, prescriptions), or it talks about "jobs", "customers" and "techs on the way".

**Front desk, Callie Dunaway** (phone ringing, a dog at the counter, a cat carrier on the bench)
1. Who is calling: client, pets, next appointment, anything open.
2. Who is here, who is waiting in the car (curbside), who is checking out and what they owe.
3. New clients: intake form back, old clinic records requested, welcome kit ready.
4. Reminders due this month to work in quiet minutes.
5. Tomorrow's unconfirmed, one tap to text again.
Trust: one screen for the counter, the phone and curbside texts. Dismiss: retyping what the client already put in the website form.

**Vet tech, Jesse Kimbrough, LVT** (gloves on, phone in a scrub pocket)
1. My drop-offs today: pet, owner, doctor, pickup time.
2. Mark where each one is: dropped off, with the team, ready for pickup, picked up.
3. Text the owner "ready for pickup" in one tap.
4. Send the pay link so pickup is fast.
5. My tech visits (nail trims, vaccine visits) and who's next.
Trust: big taps, the owner's text reply shows right there. Dismiss: typing, or medical fields he'd expect in the practice software.

**Client, Joanna Pruneda** (from a reminder text, on her phone)
1. Which of my pets is due, and a time to book it now.
2. What's coming up, confirmed or not, drop-off and pickup times.
3. The estimate and deposit: what I approved and what I already paid.
4. How payment works (site: due at time of service).
5. Address, parking, curbside, hours, what to do if it's urgent.
Trust: it looks like Wellspring, it knows both pets by name, no account or app. Dismiss: a login wall, surprise fees, or a generic "customer portal".

---

## 3. Words

| Bone | Vet word |
|---|---|
| Customer | **Client** (the person) with **Pets** (each pet is the patient). Nav label "Clients & pets". |
| Visit | **Appointment**, placed in a room (Exam 1, Exam 2, Cat room, Surgery suite) with a doctor or the vet tech; surgery and dental are **Drop-offs** (drop-off window, pickup time) |
| Deal | **Estimate** (stages: Sent, Approved, Deposit paid, Scheduled). Shown as a range, e.g. "$540 to $710" |
| Work item | **Drop-off sheet** (status steps, deposit, pickup time, ready text) and **checkout** (next reminder set, review request). No clinical content. |
| Money | Estimate, deposit, invoice total, **pay link**, card payment, balance |
| Conversation | Inbox (calls, texts, website chat) |
| Automation | Reminders (wellness & vaccines due), confirmations, "ready for pickup" text, "come on in" curbside text, review requests, estimate follow-up |
| Team | Veterinarian, Vet tech (LVT), Practice manager, Front desk |
| Customer view | Client page ("Your pets") |
| Website link | Website "Request appointment" form, website chat, online booking |

Appointment types allowed (the only ones): Wellness exam, Senior wellness exam, Puppy visit, Kitten visit, New-client exam, Vaccine visit (tech), Nail trim (tech), Sick visit (same day), Recheck, Surgery consult. Drop-off types: Dental cleaning, Spay, Neuter, Soft-tissue surgery.

Status chips: Unconfirmed (amber), Confirmed (green check), Checked in (blue), Waiting in car (teal, car icon), In room (solid emerald), Checked out (gray). Drop-off steps: Dropped off · With the team · Ready for pickup · Picked up. Badges: NEW, AI (booked by AI receptionist), Same-day (amber), Family (multi-pet household), $ (pay link open), species icon (dog / cat) on every pet.

Nav, owner desktop (also practice manager): Today · Schedule · Drop-offs · Clients & pets · Inbox · Reminders · Estimates · Payments · Reviews · Team · Settings
Nav, front desk desktop: Front desk · Schedule · Drop-offs · Inbox · Clients & pets · Reminders · Estimates · Payments
Nav, vet tech phone (bottom tabs): Today · Drop-offs · Pets · Inbox
Nav, practice manager phone (bottom tabs): Today · Schedule · Inbox · More

Must NOT appear: job, work order, service call, dispatch, route, crew, truck, on my way, customer, lead (say "new client"), deal, pipeline, quote, guest, member, class, stylist, chair, operatory, Op 1, hygienist, patient (as the person), recall (vets say "reminders"), POS, register, payroll, ledger. Not offered by this hospital: boarding, grooming, daycare, kennel booking, pharmacy or food sales, refills. Clinical words, never on any screen: diagnosis, medical record, chart, SOAP, notes from the exam, lab results, bloodwork, x-ray or imaging results, prescription, Rx, medication or vaccine names (rabies, DHPP, Bordetella, FeLV, etc.), weight, test results, anesthesia, sedation, post-op, recovery, fasting instructions, microchip or tag numbers, euthanasia, deceased.

---

## 4. The 6 screens

Visual kit per BONES: emerald sidebar and header band, light canvas, white cards, emerald phone tab bar. Screen 5 is styled as Wellspring. Every image carries the bottom strip "Sample screens · sample data, not a real business".

### Screen 1: Owner home ("Today"), desktop 1440x900
Job: at 7:15 AM Dr. Cho sees today by doctor, the morning drop-offs, what came in overnight, and what's waiting on her.

- **Sidebar**: owner nav, Today active, Inbox badge "3". Top: paw icon + "Wellspring Animal Hospital". Footer: avatar EC "Elena Cho · Owner".
- **Header band**: "Good morning, Elena" / "Wed, Dec 2 · 25 appointments · 3 drop-offs · doors open 8:00 AM". Right: search "Search clients or pets...", avatar.
- **KPI row (5 cards)**:
  1. Today: "25 appointments" / "Dr. Cho 12 · Dr. Reed 7 · Jesse 6"
  2. Drop-offs: "3" / "Bandit, Waffles, Mabel · deposits paid · arriving 7:30 to 8:00"
  3. Confirmed: "22 of 25" / "Waiting: Rufus, Moose, Bear"
  4. New clients this week: "6" / "4 booked by the AI receptionist or website chat"
  5. Reminders, December: "64 of 118 booked" with a thin progress bar (54%)
- **Left column (about 62%)**
  - **"Today by doctor"** card: three horizontal lanes, 8 AM to 6 PM, lunch 12:30-1:30 hatched. Blocks show pet name + species icon only.
    - Dr. Cho: blocks 8:00-12:30 and 1:30-5:45; two dashed amber blocks labeled "Held · same-day sick" at 10:45 and 12:00; Rufus 2:15, Moose 4:45 and Bear 5:15 drawn amber-outlined (unconfirmed); open white gap 3:00-3:30.
    - Dr. Reed: solid indigo "Surgery suite" band 8:30-12:30 split into Bandit · Waffles · Mabel; afternoon blocks 1:30-3:00; dashed amber "Held · same-day sick" 3:00; three thin "Pickup" ticks 3:30, 4:00, 4:30; Coco 5:00.
    - Jesse (tech visits): six short blocks 8:15-11:45.
    - Link at right: "Open schedule".
  - **"Booked while you were busy"** card, 4 rows: pet · client · what · booked for · how it came in:
    - Clementine (puppy) · Hannah Stroud · NEW · New-client exam · Today 3:30 PM · AI receptionist, Sun 4:18 PM (closed)
    - Sir Pounce (cat) · Omar Belhadj · NEW · New-client exam · Today 1:30 PM · Website chat, Mon 10:52 PM
    - Winnie (dog) · Courtney Lattimore · NEW · New-client exam · Fri Dec 4, 9:00 AM · Missed call, texted back, Tue 5:52 PM
    - Tank (dog) · Mitch Hightower · Surgery consult · Today 1:30 PM · AI receptionist, Mon 7:40 AM (before open)
    - Footer line: "AI receptionist answered 61 calls this week · 19 after hours"
  - **"Urgent calls after hours (2)"** small card, subtitle "Sent to Wrenfield Animal ER, number texted to the caller":
    - Cleo (cat) · Nolan Fitzhugh · Sun 8:14 PM · "Priya called back Mon 8:10 AM ✓"
    - Sadie (dog) · Joy Vanderpool · Mon 11:02 PM · "Priya called back Tue 8:05 AM ✓"
- **Right column (about 38%)**
  - **"Estimates"** card: stage chips "Sent 4 · Approved, not booked 2 · Scheduled with deposit 5". Rows:
    - Bodie · Kara Yoakum · Dental cleaning · $480 to $640 · Approved Nov 30 · button "Text to book"
    - Sully · Paige Whitcomb · Dental cleaning · $520 to $680 · Sent Nov 27 · opened, no reply · button "Text"
    - Tank · Mitch Hightower · Soft-tissue surgery · $1,180 to $1,460 · Sent Nov 25 · "Consult today 1:30"
  - **"Payments"** card: "Collected yesterday $7,860" / "Deposits for today's drop-offs: $450 paid (3 × $150)". Sub-heading "Pay links open · 3 · $642.80": Lady · Celeste Thibodeaux $404.30 · Nov 24 · Lola · Gina Cantu $142.00 · Nov 28 · opened · Rufus · Paul Dempsey $96.50 · Nov 20 · in today 2:15. Button "Resend links".
  - **"Reviews"** card: "4.9 ★ · 264 Google reviews · 11 new in November". Latest: Sabrina Hutchins ★★★★★ "Nala's first puppy visit was so calm. Callie remembered her name at the door." Chip "1 waiting for a reply" + button "Reply".

### Screen 2 (signature): Schedule, today by room, desktop 1440x900
Job: run the day room by room (dog rooms, Cat room, Surgery suite), see each doctor by color, protect the same-day sick slots, and track the morning drop-offs to pickup.
Signed in as Priya Shah (owner nav, Schedule active). Time 10:40 AM.

- **Header band**: "Schedule" / toggles "Rooms | Doctors | Week" (Rooms on), arrows, "Today", date "Wed, Dec 2". Right: emerald button "+ Book appointment".
- **Summary strip**: "27 appointments · 25 confirmed · 2 unconfirmed · 3 drop-offs · Same-day sick: 3 held, 2 filled, 1 left (3:00 Dr. Reed)". Doctor legend chips with color dots: Dr. Cho · Dr. Reed · Jesse (tech).
- **Main grid (about 72%)**: four columns: "Exam 1", "Exam 2", "Exam 3 · Cat room" (small cat icon in header, column tinted faint sage), "Surgery suite". Time rail 8 AM-6 PM, red now-line at 10:40, lunch 12:30-1:30 hatched across all. Each block: time · pet name + species icon · client surname · type · doctor color bar on the left edge with initials (EC / MR / JK) · status chip · badges.
  - Exam 1: 8:00 Gus · Gentry · Wellness exam · EC · Checked out | 9:00 Nala · Hutchins · Puppy visit · EC · Checked out | 9:30-10:15 Duke, 13 · Quarles · Senior wellness exam · EC · Checked out | 10:15-10:45 Biscotti · Dowell · Wellness exam · EC · In room | **10:45-11:15 Pepper · Arbuckle · Sick visit (same day) · EC · amber "Same-day" chip · "On the way, ETA 10:44" · small line "AI transfer 10:22 · booked by Callie"** | 12:00 Maple · Abernathy · Sick visit (same day) · EC · Confirmed · Same-day | 2:15-3:00 Rufus · Dempsey · Senior wellness exam · EC · Unconfirmed · $ | 3:00-3:30 empty "+ Open" | 3:30-4:15 Clementine, 10 wks · Stroud · New-client exam · EC · Confirmed · NEW · AI | 4:45 Moose · Mancuso · Wellness exam · EC · Unconfirmed | 5:15 Bear · Yancey · Wellness exam · EC · Confirmed
  - Exam 2: tech visits, 15 min each, JK: 8:15 Peanut · Kemper · Nail trim · Checked out | 8:45 Koda · Sheffield · Vaccine visit · Checked out | 9:30 Bruno · Zamora · Vaccine visit · Checked out | 10:30 Roxie · Gaskins · Nail trim · In room | 11:00 Ollie · Pickens · Nail trim · Waiting in car | 11:30 Daisy · Ostrander · Vaccine visit · Confirmed. Afternoon, MR: 1:30 Tank · Hightower · Surgery consult · Confirmed | 2:00 Lola · Cantu · Recheck · Confirmed · $ | 2:30 Finn · Spurlock · Wellness exam · Confirmed | **3:00-3:30 dashed amber "Held · same-day sick · Dr. Reed"** | 3:30, 4:00, 4:30 thin gray blocks "Pickup · Bandit", "Pickup · Waffles", "Pickup · Mabel" | 5:00 Coco · Ruelas · Wellness exam · Confirmed
  - Exam 3 · Cat room (EC): 8:30 Miso · Nakamura · Wellness exam · Checked out | 11:15-12:00 Ziggy + Lulu · Tibbetts · Wellness exam ×2 · Confirmed · Family | 1:30-2:15 Sir Pounce · Belhadj · New-client exam · Confirmed · NEW | 4:15 Pixel · Escobedo · Kitten visit · Confirmed
  - Surgery suite (MR): 8:30-10:00 Bandit · Villarreal · Neuter · gray "Done" | 10:00-11:30 Waffles · Eckhart · Dental cleaning · solid indigo "In suite" | 11:30-12:30 Mabel · Driscoll · Spay · "Next"
- **Right rail (about 28%)**
  - **"Drop-offs today"** card, 3 rows (pet + species · client · drop-off time · pickup · step · deposit):
    - Bandit · Villarreal · in 7:36 AM · pickup 3:30 PM · "With the team" · Deposit $150 ✓
    - Waffles · Eckhart · in 7:48 AM · pickup 4:00 PM · "With the team" · Deposit $150 ✓
    - Mabel · Driscoll · in 7:55 AM · pickup 4:30 PM · "Dropped off" · Deposit $150 ✓
    Link "Open drop-offs".
  - **"Same-day sick slots"** card: three rows: 10:45 Dr. Cho · Pepper (filled 10:23 by Callie) · 12:00 Dr. Cho · Maple (filled 8:05) · 3:00 Dr. Reed · open, chip "Held until 2:00 PM, then opens to online booking".
  - **"Tomorrow · Thu, Dec 3"** card: "27 booked · 22 confirmed · 5 waiting · 2 drop-offs", button "Text the 5 again".

### Screen 3: Front desk, desktop 1440x900
Job: Callie handles the ringing phone, the counter, curbside and new-client intake from one screen. Time 10:47 AM.

- **Sidebar**: front desk nav, "Front desk" active. Footer "Callie Dunaway · Front desk".
- **Incoming call bar** (full width, dark emerald): pulsing phone icon · "Incoming call · (972) 555-0181 · Joanna Pruneda" · pets chips "Hazel (dog) · Tofu (cat)" · "Hazel: Dental cleaning drop-off Thu Dec 10 · Confirmed · Tofu: reminder link opened 10:31 AM" · buttons "Answer" and "Let the AI receptionist take it".
- **Three columns below**
  - **"Counter and curbside"** (left)
    - Checking out: Biscotti · Marguerite Dowell · Exam 1 · Dr. Cho · "Total $164.20" buttons "Take card" / "Text pay link" · "Next wellness reminder set: Dec 2027" · "Review request goes out at 2:00 PM".
    - Checked out: Roxie · Dana Gaskins · Nail trim · "$22.00 paid · card on file ✓".
    - Checked in: Pepper · Lacey Arbuckle · Same-day · Exam 1 · Dr. Cho · "In 10:45 · Priya brought her in from curbside".
    - Waiting in car: Ollie · Ray Pickens · 11:00 Nail trim · Jesse · button "Text: come on in" (preview "We're ready for Ollie. Come on in!").
    - Next: Ziggy + Lulu · Nora Tibbetts · 11:15 Cat room · Family · "Cat waiting area".
  - **"New clients"** (middle): header "6 this week · 2 already seen". Rows (pet · client · first visit · chips):
    - Clementine (puppy) · Hannah Stroud · Today 3:30 PM · AI · chips "Intake form ✓" "First vet visit, no records" "Welcome kit + free nail trim ready ✓"
    - Sir Pounce (cat) · Omar Belhadj · Today 1:30 PM · chips "Intake form ✓" "Records from previous clinic received Dec 1 ✓" "Welcome kit ready ✓"
    - Winnie (dog) · Courtney Lattimore · Fri Dec 4, 9:00 AM · chips "Intake form not back" (amber) "Records requested Nov 30" · button "Text form link"
    - Juno (cat) · Felix Ambrose · not booked · "Website request, Tue 9:14 PM · New patient / wellness exam · prefers Sat morning" · buttons "Text times" / "Call"
  - **"Reminders due · December"** (right): header "118 due · 64 booked · 54 to reach". Chips: Not texted yet (21) · Texted, no reply (25) · Call later (8). Rows (pet · client · due for · note · action):
    - Tofu (cat) · Joanna Pruneda · Annual wellness & vaccines · "Opened link 10:31 AM · Hazel in Dec 10" · "Book with Hazel's drop-off"
    - Pumpkin (cat) · Laura Kemper · Annual wellness & vaccines · "Peanut was in at 8:15" · "Text"
    - Buster (dog) · Arlo Kincannon · Senior wellness exam · texted Nov 20 · "Text again"
    - Bodie (dog) · Kara Yoakum · Annual wellness & vaccines · "Dental estimate approved, not booked" · "Book both"
    - Link at bottom: "View all 54".

### Screen 4: Vet tech "Drop-offs", phone 390x844
Job: Jesse moves each surgery/dental pet to "ready for pickup", texts the owner and sends the pay link so pickup takes two minutes. Time 3:05 PM.

- **Top bar**: "Drop-offs" / "Jesse Kimbrough · Wed, Dec 2" · chip "3 today · 1 ready".
- **Card 1, expanded (emerald edge)**: dog icon · **Bandit**, 1 · Teo Villarreal · Neuter · Dr. Reed · "Dropped off 7:36 AM · Pickup 3:30 PM".
  - Step bar: Dropped off ✓ · With the team ✓ · **Ready for pickup ✓ (texted 2:58 PM)** · Picked up ○
  - Money row: "Estimate $310 to $380 · Deposit $150.00 paid · Due at pickup $198.40".
  - Mini thread inside the card:
    - Wellspring, 2:58 PM: "Hi Teo, Bandit is ready to go home! Pick up anytime after 3:30 PM at 24 Cedar Hollow Road. Dr. Reed will go over everything with you at pickup."
    - Teo, 3:02 PM: "Great, be there at 3:45. Can I pay before I get there?"
    - Wellspring, 3:04 PM: "Sure, here's your link: Pay $198.40" (link chip) · status under it "Sent ✓"
  - Buttons: "Mark picked up" (primary), "Call Teo".
- **Card 2, collapsed**: cat icon · **Waffles**, 6 · Grant Eckhart · Dental cleaning · Dr. Reed · pickup 4:00 PM · step chip "With the team" · button "Text: ready for pickup" · "Deposit $150 ✓".
- **Card 3, collapsed**: dog icon · **Mabel**, 7 mo · Sheila Driscoll · Spay · Dr. Reed · pickup 4:30 PM · "With the team" · button "Text: ready for pickup" · "Deposit $150 ✓".
- Collapsed row under the cards: "Tech visits · 6 done today".
- **Bottom tabs**: Today · Drop-offs (active) · Pets · Inbox.

### Screen 5: Client page, phone 390x844 (styled as Wellspring, not the staff app)
Job: Joanna opens the link from Tofu's reminder text, books Tofu, and sees Hazel's drop-off is confirmed and the deposit is paid.

- Wellspring styling from the site: cream ground #FBF8F3, forest green #1E6B54 primary, coral #EE7256 accent, sage mist #EAF1EA cards, Quicksand headings, Nunito Sans body, large soft radii. Rounded paw mark (forest pads, one coral toe bean, `assets/logo-mark.svg`) + "Wellspring Animal Hospital". No emerald staff chrome, no sidebar.
- Header: logo, small lock "Secure page". "Hi Joanna". Pet row: two round avatars "Hazel · dog, 9" and "Tofu · cat, 3".
- **"Due now"** card (coral left edge): "Tofu · Annual wellness & vaccines · due in December". Toggle "Any doctor | Dr. Cho" (Dr. Cho on). Time chips: "Thu, Dec 10 · 8:30 AM" (selected, tag "Same morning as Hazel's drop-off"), "Sat, Dec 12 · 9:30 AM", "Tue, Dec 15 · 4:45 PM". Small line "Cats wait in our separate cat area." Button "Book Tofu · Thu, Dec 10 at 8:30 AM".
- **"Coming up"** card: "Hazel · Dental cleaning (drop-off) · Thu, Dec 10" · "Drop off 7:30 to 8:00 AM · Pickup after 3:30 PM, we'll text you" · "Confirmed ✓". Under it: "Estimate approved Nov 24 · $540 to $710 · Deposit $150.00 paid ✓" · link "View estimate". Links "Add to calendar" · "Reschedule".
- **"How payment works"** line: "Payment is due at the time of service. At pickup we'll text you a link, or pay at the desk."
- **Visit us** card: 24 Cedar Hollow Road · "Free parking, easy curbside drop-off" · (972) 555-0153 · Mon-Fri 8-6, Sat 8-2, closed Sun · coral note "Is it urgent? Call us now. After hours, we'll give you the nearest emergency hospital."
- Footer small: "Wellspring Animal Hospital · Powered by Top Shelf".

### Screen 6: AI receptionist, urgent call, phone 390x844 (practice manager inbox)
Job: show a "my dog ate chocolate" call: the AI gives no advice, gets a human on the line in seconds, the human books the held same-day slot, and the texts get the dog in the door.
Signed in as Priya Shah on her phone.

- **Top bar**: back arrow · "Lacey Arbuckle" · "(940) 555-0174" · chip "Pepper (dog, 2)" · phone icon.
- **Call card** (top of thread, light amber tint, amber chip "Urgent"): "AI receptionist · Wed, Dec 2 · 10:22 AM · 1:06 · Transferred to Callie at 0:41" · play button "Listen".
  - One transcript quote, small italic: AI: "I'm not able to give medical advice, but I'm getting someone from our team on the line right now. Please stay with me."
  - Summary bullets:
    - Caller says Pepper got into chocolate about 20 minutes ago
    - No advice given; flagged urgent
    - Warm transfer to Callie Dunaway, picked up in 9 sec
    - Callie booked: Sick visit (same day) · today 10:45 AM · Dr. Cho · Exam 1 (held slot)
  - Gray rule line under the bullets: "If no one picks up in 30 sec, the AI gives Wrenfield Animal ER, (972) 555-0199, and texts the number."
  - Chip row: "Added to schedule" · "Dr. Cho notified".
- **Text thread**:
  - Wellspring, 10:26 AM: "Hi Lacey, this is Wellspring Animal Hospital. We're expecting you and Pepper at 10:45 at 24 Cedar Hollow Road. Pull into a curbside spot and text us when you're here."
  - Lacey, 10:27 AM: "On our way, about 15 minutes."
  - Lacey, 10:44 AM: "Here, white SUV by the door."
  - Priya, 10:44 AM: "Coming out to get you both now."
  - System line: "Checked in 10:45 AM · Exam 1"
- **Composer**: "Text message", attach, send.
- **Bottom tabs**: Today · Schedule · Inbox (active) · More.

---

## 5. How it uses the bones

| Screen | Records read |
|---|---|
| 1 Owner home | Visit (by doctor, held slots, status), Deal (estimates by stage), Money (collected, deposits, pay links), Customer (new clients, source), Conversation (AI calls, website chat, missed-call text-back, after-hours urgent routing), Automation (reminders), reviews via Automation |
| 2 Schedule by room | Visit (room, doctor, type, status, held same-day slots, drop-off/pickup), Customer (pets, NEW, Family), Money (deposit, $ flag), Team (doctor colors), Conversation (AI transfer note) |
| 3 Front desk | Conversation (incoming call, curbside texts, website request), Visit (check-in/out, waiting in car), Money (card, pay link), Customer (intake form, records-requested flag, welcome kit), Automation (reminders, review request), Website link (request form) |
| 4 Vet tech drop-offs | Visit (drop-off, pickup), Work item (drop-off steps), Money (estimate, deposit, pay link), Conversation (ready text, reply), Automation (ready-for-pickup text) |
| 5 Client page | Customer view (hub), Customer (pets), Visit (upcoming, online booking slots), Deal (approved estimate), Money (deposit paid), Automation (reminder that sent the link) |
| 6 AI receptionist | Conversation (call summary, transfer, texts), Visit (same-day booking), Customer (client + pet), Team (transfer to Callie, Dr. Cho notified), Automation (ER fallback text) |

---

## 6. Watch-outs

- **The AI never gives medical advice.** Screen 6 must show it saying so and handing off to a person within seconds; the ER fallback is the only other path. No AI line or summary that assesses danger, amount, symptoms or what to do at home. Same on screen 1's after-hours card: "sent to Wrenfield Animal ER" plus a human follow-up, nothing more.
- **Stay beside the practice software, not instead of it.** No records, exam notes, lab or imaging results, prescriptions, vaccine names or dates given, weights, or diagnoses. "Sick visit" and "Recheck" are appointment types; never show the reason or symptom (the one exception is the chocolate call summary line, which is what the caller said). The drop-off steps are where the pet is, not how it's doing: no "recovering", "under anesthesia", "post-op".
- **Records from the old clinic** appear only as a status ("requested", "received"), never their contents.
- **Calm, not clinical.** The site's voice is warm and plain. Texts use the pet's name and a friendly line ("Bandit is ready to go home!"); no medical detail in any text. One amber "Urgent" chip on screen 6 and amber "Same-day" chips are the only urgency on the set. No euthanasia, deceased pets or grief anywhere.
- **Not home services, not dental.** No jobs, techs on the way or dispatch. The vet versions of "on my way / ready" are the curbside "Come on in" text and the "Ready for pickup" text. The person is a client, the pet is the patient; say "Reminders", not "Recall"; rooms, not chairs.
- **Only what the site offers.** No boarding, grooming or daycare (the site doesn't offer them); the only grooming-like item is the tech Nail trim and the new-client free nail trim from the site.
- **Payment matches the site:** "due at the time of service", written estimate before treatment, shown as a range, with a $150 deposit for drop-offs. Keep balances small; this practice collects at checkout.
- **Site facts used:** team (Dr. Elena Cho, Dr. Marcus Reed, Priya Shah), services, hours, 24 Cedar Hollow Road, curbside, separate cat area, new-client welcome kit + free nail trim, 4.9 rating. The site disagrees with itself on review count (brief "800+", hero "300+ pet families", stats "260+ reviews"); the screens use **264 Google reviews** to match the stats band. If Taylor fixes the site, update this one number.
- **Surname collision, flag for Taylor.** The site's own team surnames Cho, Reed and Shah already appear in other industries' screens (e.g. dental's filler "Eli Cho" and "Ivan Shah"). The business and team are fixed, so this brief keeps them; every client and added staff surname I cast is unique. If the rule must be absolute, rename the filler in the other sets, not Wellspring's team.
- **Numbers check:** 25 appointments at 7:15 AM becomes 27 by 10:40 (Maple booked 8:05, Pepper 10:23); unconfirmed 3 then 2 (Bear confirmed by text at 9:12). Reminders 21 + 25 + 8 = 54 to reach. Pay links $404.30 + $142.00 + $96.50 = $642.80. Bandit $348.40 final minus $150 deposit = $198.40. Dec 2, 2026 is a Wednesday; Dec 10 Thursday, Dec 12 Saturday, Dec 15 Tuesday.
- **Name check.** Wrenfield Animal ER and all client names are made up; search "Wrenfield Animal ER" once before publishing. All phones are 555-01xx and unused by other industries.
