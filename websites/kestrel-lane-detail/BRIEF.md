# Kestrel Lane Detail Co. | Sample Site Brief

**Industry:** Auto (detailing) · **Slug:** `kestrel-lane-detail` · **Domain:** kestrellanedetail.com (the booking-link domain on the CRM screens)
**Phone:** 123-456-7890 · **Email:** contact@kestrellanedetail.com
**Built:** 2026-11-27 (ask: a 5-page sample site that pairs with the auto-detailing CRM screens, "same business, same look").

## Source of truth
- `renders-src/industry-crm/briefs/auto-detailing.md` (the business, cast, prices, words, watch-outs).
- `renders-src/industry-crm/screens/auto-detailing/*` (the rendered screens). Where the screens and the brief disagree on a surname, the screens win because they are what a prospect sees next to this site: **Paloma Rowley** (brief: Ruiz) and **Minh Talley** (brief: Tran).
- Price list = `DetailMenu::SAMPLE` in the CRM. Only Full detail changes by size; the other packages and the add-ons are one price for every size.

## Identity
- **Name:** Kestrel Lane Detail Co. · **Type:** drop-off auto detailing shop. One shop, 2 bays ("2 cars at a time"), open daily 8:00 AM to 5:00 PM. No mobile service.
- **Town:** Rowlett, TX (the CRM's town). No street address is shown; the site never names one.
- **Phone on the site:** 123-456-7890 per the program (the CRM screens use a 555 number, which stays on the screens only).
- **Fictional:** a sample business. Footer carries a visible "Sample website" note and every price is labelled a sample price.

## Team (from the CRM)
| Person | Role | What they do |
|---|---|---|
| Dee Hargrove | Owner | Prices the big jobs herself: ceramic coating and paint correction |
| Paloma Rowley | Front desk | Phones, check-in, deposits, pickups |
| Trey Ashford | Detailer | Full details, interiors |
| Minh Talley | Detailer | Paint correction, ceramic coating |

## Price list (sample prices, same as the CRM)
| Package | Car | SUV | Truck or van | Time |
|---|---|---|---|---|
| Full detail | $180 | $220 | $250 | 3 h |
| Interior shampoo | $120 | $120 | $120 | 2 h |
| Exterior wash and wax | $90 | $90 | $90 | 1.5 h |
| Ceramic coating, 3-year | $900 | $900 | $900 | 8 h |

Add-ons, one price: Pet hair removal $40 (30 min) · Headlight restore $60 (1 h) · Engine bay $50 (1 h).
Not on the booking page: Paint correction (1-step), priced by the hour at $75 an hour; Dee quotes it after seeing the car.
Deposit: 25% of the booking, rounded to the cent, comes off the bill. Rest due at pickup.

## How a visit goes (real CRM flow, no invented features)
1. Book online: pick size, package, add-ons, day and time; the price and the deposit show before you book. A text confirms it with a link to the booking.
2. Drop off: Paloma checks the car in; check-in photos record the car as it came in.
3. If the detailer finds something (dog hair in the cargo carpet), the shop texts the price and waits for your OK before doing it.
4. "Text it's ready": pay by link or at the counter; the tip is added by you on the pay link.
5. Rebook reminders by text if you want them (a reminder, not a plan you pay for).

## Must not appear
Invented reviews, ratings or review counts; warranty or guarantee claims; ceramic coating durability or performance claims (the package name "Ceramic coating, 3-year" is used as named on the price list, with no further claim); mobile service, wash clubs, memberships, gift cards, prepaid packs, fleet accounts, coating certificates; "call for a quote"; em dashes.

## Voice
Plain and specific, like the front desk on a good day: the price, the time, what happens next. Proud of the work, no hype.

## Theme / art direction
- **Palette (the CRM's):** gloss black `#07090d`, deep black `#030406`, panel `#0e131b`, ceramic blue `#3b8eff` (accent, dark ink on blue buttons for AA), light blue `#8fbfff` (links/eyebrows on black), chrome text `#e9eef5`, muted `#9ba7b7`.
- **Type:** Bricolage Grotesque (display, used with restraint), Figtree (body), JetBrains Mono (prices, times, labels: tabular numbers).
- **Signature:** the hero is a gloss-black paint panel drawn in SVG: a sky-blue reflection band with a crisp reflection line, water beads sitting on the panel, and a light streak that sweeps across (follows the pointer on desktop, static under reduced motion).
- **Visuals:** SVG/CSS only. No photos, no generated or downloaded images. Gallery before/afters are labelled illustrations.
- **Motion:** Lenis + GSAP hero entrance, reveal on scroll, before/after drag sliders. `prefers-reduced-motion` respected; everything readable with JS off.

## Pages (5)
1. **index.html:** hero panel → price by size picker (Full detail) → the four packages → how a visit goes → one before/after → the people → hours and visit info → CTA.
2. **packages.html:** size switcher + full price table (Car / SUV / Truck or van), package details, add-ons, paint correction by the hour, deposit note.
3. **gallery.html:** four before/after sliders drawn in SVG (headlight, cargo carpet pet hair, hood wash and wax, paint correction), labelled illustrations.
4. **about.html:** the shop, the four people, how a visit goes, hours.
5. **book.html:** the booking request form that feeds the CRM booking: size → package → add-ons → day and time → your details, with a live total and 25% deposit. Demo submit (nothing is sent).

## Assets
- `assets/logo-mark.svg`: hand-built mark (a kestrel wing drawn as three swept light streaks on a gloss-black tile, the leading one ceramic blue, a single water bead).
- `assets/styles.css`, `assets/app.js`. No raster images except the shared Top Shelf credit logo.
