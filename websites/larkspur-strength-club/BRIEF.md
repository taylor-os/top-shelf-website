# Larkspur Strength Club: Sample Site Brief

**Industry:** Salon, Spa &amp; Fitness (gym half) · **Slug:** `larkspur-strength-club` · **Domain:** larkspurstrengthclub.com
**Phone:** 123-456-7890 · **Email:** contact@larkspurstrengthclub.com
**Pairs with:** the fitness CRM screens in `renders-src/industry-crm/screens/fitness/` (brief: `renders-src/industry-crm/briefs/fitness.md`). Same business, same look.

## Identity
- **Name:** Larkspur Strength Club · **Type:** group strength classes plus open gym, one location.
- **Town:** Rowlett, TX. Address from the CRM brief (made up): 4410 Bayside Commons Dr, Rowlett, TX 75088.
- **One-liner:** Coached strength classes and open gym in Rowlett.
- **Hours (CRM brief):** open 5:00 AM to 10:00 PM weekdays; front desk staffed 6:00 AM to 9:00 PM. The CRM states no weekend opening hours, only weekend classes, so the site lists weekends as "Class times only" and points to the schedule rather than inventing hours.
- **Positioning:** A coached gym that is easy to start at. Your first class is Intro / Foundations, capped at 8 people. After that, book any class from the member app and get a text reminder.

## Cast (names exactly as the CRM screens show them)
- **Graham Paxton**, owner (the screens say Paxton; the written CRM brief says Pruitt; the screens win).
- **Malik Odom**, head coach; teaches the morning Strength &amp; Conditioning, Barbell Club and Intro / Foundations.
- **Dez Fuller**, coach; evening Strength &amp; Conditioning and HIIT 45, Saturday 10:00 AM S&amp;C.
- **Erin Sato**, coach; Mobility, morning and midday HIIT 45, Friday 5:30 AM S&amp;C.
- **Hannah Strickland**, personal trainer (one-on-one; no schedule shown).
- **Tessa Villanueva**, front desk.
- No credentials, years of experience or backstory are invented for anyone.

## Classes (capacity from the CRM brief)
Strength &amp; Conditioning (16, 60 min) · HIIT 45 (16) · Barbell Club (12) · Mobility (20) · Intro / Foundations (8).
Weekly schedule copied from the CRM "Classes" week screen:
- Mon/Wed: 5:30 AM S&amp;C (Malik), 6:30 AM S&amp;C (Malik), 9:00 AM HIIT 45 (Erin), 12:00 PM HIIT 45 (Erin), 4:30 PM Barbell Club (Malik), 5:30 PM S&amp;C (Dez), 6:30 PM HIIT 45 (Dez).
- Tue/Thu: as above but 9:00 AM Mobility (Erin), plus 7:30 PM Intro / Foundations (Malik).
- Fri: 5:30 AM S&amp;C (Erin), then as Mon.
- Sat: 8:00 AM Barbell Club (coach to be announced; the CRM flags it "No coach"), 9:00 AM Intro / Foundations (Malik), 10:00 AM S&amp;C (Dez).
- Sun: 9:00 AM Mobility (Erin).

## Memberships (sample prices are the CRM screens' own, labelled "sample")
- **Monthly** (open gym): $59/mo plus a $25 sign-up fee.
- **Unlimited classes**: $119/mo, no sign-up fee, 30 days' notice to cancel.
- **Personal training** with Hannah: no price on the screens, so none shown ("ask at the desk").
- How billing works, in the CRM's words: card on file, monthly charge, "paid through" date in the app, a text if a card is declined and a retry.

## Voice
Plain, direct, a coach talking at the front desk. Short sentences. No hype, no "transform your life". Uses the CRM's words: member, class, booking, check-in, membership, plan. Never: customer, client (except PT), appointment, subscription, CrossFit, WOD.

## Theme / art direction
- **Palette (fixed by the CRM):** ink `#0e0f10`, charcoal `#161719`, slab `#202226`, chalk `#ECE7DF` (text), steel `#9A9DA3` (muted text), orange `#e0702e` (accent; buttons carry ink text for AA).
- **Type:** Big Shoulders Display (condensed, industrial, plate-stamp feel) for display; Archivo for body; IBM Plex Mono for times and capacities.
- **Signature:** a side-on loaded barbell drawn in SVG across the home hero; plates slide onto the sleeves on load. Knurl-texture rules (CSS crosshatch) divide sections, like the grip on a bar.
- **Logo:** hand-built SVG. A vertical bar with stacked plates that shrink toward the top: a plate tree that also reads as a larkspur flower spike. Wordmark in Big Shoulders.
- **Art:** SVG/CSS only. Bold geometric plates, bars and rings. No photography, no paid generation, no downloads.
- **Motion:** Lenis + GSAP (program stack), hero plate load-in, soft reveals. `prefers-reduced-motion` turns all of it off.

## Proof
None invented. No reviews, ratings, member counts or stats on the site.

## Pages (5)
1. **index.html, Home:** hero (barbell, headline, Try a class, hours/address strip) → the five classes with capacity → how starting works (a real 4-step sequence) → member app (a sample screen copied from the CRM's member app) → the two plans → three coaches → CTA.
2. **classes.html, Classes:** class types with times, coaches and capacity → weekly schedule with a class-type filter (Sat 8:00 AM Barbell Club shows "Coach to be announced") → when a class is full / your first class → CTA.
3. **memberships.html, Memberships:** two plans (sample prices) → personal training → how billing works → questions → CTA.
4. **coaches.html, Coaches:** coaches with what they teach → owner and front desk → CTA.
5. **visit.html, Visit / Try a class:** intro-class request form (feeds the CRM's Leads + booking) beside what to bring, address and parking, hours, and phone/email. The form is the page's CTA.

**Global:** sticky header (logo, Home · Classes · Memberships · Coaches · Visit, phone, "Try a class"). Footer: explore, visit, contact, and a visible "Sample website" note with the Top Shelf credit.

## Assets
- `assets/logo-mark.svg` (hand-built), `assets/styles.css`, `assets/app.js`, `assets/topshelf-logo.png` (copied from another sample site).
