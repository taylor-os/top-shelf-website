# Bramlett Motor Co. - Sample Site Brief

**Industry:** Auto (independent used-car lot, buy here pay here friendly) · **Slug:** `bramlett-motor-co` · **Domain:** bramlettmotorco.com
**Phone:** 123-456-7890 · **Email:** contact@bramlettmotorco.com
**Pairs with:** the car-lot CRM screens in `renders-src/industry-crm/screens/car-lots/` (same business, same look).

## Identity
- **Name:** Bramlett Motor Co. · **Type:** one independent used-car lot. Sells cash, through an outside lender, or on its own in-house loans (buy here pay here).
- **Town:** Garland, TX. No street address anywhere (matches the CRM brief); the Visit page says "call or text and we'll send you a pin".
- **Hours:** Monday to Saturday, 9 am to 7 pm. Closed Sunday.
- **Tagline:** *Good used cars. Financing here at the lot.*
- **Positioning:** A family-run lot where the price is on every car, the numbers get explained across a desk before anyone signs, and you deal with the same people after you drive away.
- **Cars:** priced $7,995 to $15,900 (from the CRM brief).

## People (names match the CRM)
- **Curtis Bramlett**, owner. Gives the OK on deals, backs up collections.
- **Yolanda Pierce**, finance manager. Writes the loans, takes payments, does title work.
- **Andre Warrick**, sales. (CRM screens use "Andre Warrick".)
- **Luis Cantú**, sales.

## Voice
Plain, warm, specific. Talks like the person behind the desk. No hype, no pressure words. No em dashes.
Never says: guaranteed approval, everyone approved, no credit check, buy now pay later, any lender name, "dealership experience". No advertised payment, APR or down-payment amounts (Truth in Lending triggers). No reviews, ratings, star counts, years in business or sales numbers.

## Theme / art direction
- **World:** the lot after dark under a string of bulbs. Graphite ground, warm gold light. Same palette as the CRM.
- **Palette:** graphite `#09090a` (page) / `#111113` (chrome) / `#18181b` (raised), line `#2a2a2e`; **gold** `#c9a34e` (light `#dcbd72`); ink `#f1ede4`, muted `#a9a59c`.
- **Type:** Archivo, variable width at ~112%, weight 750, for display headings; Figtree (the CRM's face) for body, 400 to 800.
- **Rebuild (2026-11-27):** photo-led. Full-bleed photo heroes on every page (`assets/img/*.webp` + `-sm` 900px), each listing has its own photo (`car-<model>.webp`, matching body style and paint, no badges or plates, uncropped 3:2), noted on the page as sample photos. The SVG car art below is retired.
- **Shape rule:** buttons and inputs 10px radius, cards 16px, chips full pill.
- **Visuals:** hand-built SVG only. Side-profile vector cars (sedan, SUV, truck, box hatch) tinted per listing, no badges, no logos, no plates (profile view). Hero is the lot at night under bulb strings.
- **Motion:** Lenis smooth scroll, GSAP hero parallax, IntersectionObserver reveals, gentle bulb glow. All off under `prefers-reduced-motion`.

## Pages (5)
1. **index.html: Home:** split hero (headline, short sub, "See the cars" + "Set up a test drive", lot-at-night SVG) -> facts band (hours / we finance here / trade-ins) -> sample cars scroll row -> how buying here works (4 stops, like the CRM step strip) -> three ways to pay (segmented control: Cash / We finance it / Your bank or credit union) -> after-hours text band (missed call gets a text back) -> Curtis in his own words + team -> visit CTA.
2. **inventory.html: Inventory:** 10 sample listings, each marked "Sample listing", filter by Cars / SUVs / Trucks / Under $10k, each card links to the test-drive form with the car preselected. One car shows "On hold" (the Equinox from the CRM deal jacket).
3. **financing.html: Financing:** how buying here works in plain words, what to bring, three ways to pay, paying your loan (counter or texted pay link, receipt by text), honest FAQ, CTA.
4. **about.html: About:** Curtis's story, how the lot works (price on every car, numbers explained, same people after), the four staff, towns nearby, hours.
5. **contact.html: Visit:** the test-drive request form (feeds the CRM: name, phone, email, car, day, time, how they're paying, trade-in, note, text consent) + hours, phone, text, email, what to bring.

**Global:** sticky dark header (key-tag mark + "Bramlett Motor Co." / "Garland, Texas"; Home · Inventory · Financing · About · Visit; phone + "Test drive" button; mobile drawer). Footer with links, visit info and a visible "Sample website" note.

## Sample cars (all labelled sample listings)
| Car | Body | Stock # | Miles | Price | Paint |
|---|---|---|---|---|---|
| 2018 Honda CR-V EX | SUV | 26-0229 | 98,700 | $15,900 | White |
| 2013 Chevrolet Silverado 1500 LT | Truck | 26-0226 | 162,400 | $14,750 | Dark gray |
| 2017 Nissan Rogue SV | SUV | 26-0198 | 96,210 | $12,850 | Gray |
| 2018 Toyota Corolla LE | Car | 26-0224 | 88,340 | $12,495 | Blue |
| 2016 Chevrolet Equinox LT | SUV | 26-0214 | 118,400 | $11,995 | Silver (On hold) |
| 2019 Kia Soul LX | Car | 26-0207 | 71,020 | $11,450 | Red |
| 2016 Honda Accord LX | Car | 26-0219 | 109,870 | $11,250 | Black |
| 2015 Ford Escape SE | SUV | 26-0211 | 124,600 | $8,995 | Green |
| 2014 Toyota Camry SE | Car | 26-0221 | 151,300 | $8,495 | Burgundy |
| 2012 Honda Civic LX | Car | 26-0203 | 158,200 | $7,995 | Tan |

Rogue, Soul, Camry and Equinox carry the CRM's stock numbers, miles and prices.

## Assets
- **Logo:** hand-built SVG key-tag mark (gold tag, graphite "B") `assets/logo-mark.svg` + HTML wordmark.
- **Art:** inline SVG car symbols and the hero lot scene. No photography, no paid generation, no downloads.

## Known gaps / decisions
- Phone is the program's 123-456-7890, not the CRM's (972) 555-0148 lot line.
- No street address, by design.
