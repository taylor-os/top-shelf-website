# Restaurants & Bars: screen review

Reviewed all 6 renders in `screens/restaurants/` as the owner/GM, host, events coordinator, server and guest. Overall: this now reads like a restaurant, not a home-services app. There are no POS words and no home-services words on any screen. The covers, party sizes, tables, allergies and event money agree across screens. Two must-fixes, both small.

## Verdict per screen

| # | Screen | Verdict | Why |
|---|---|---|---|
| 1 | Owner home "Tonight" | **Fix** | The order is right for Marisol at 3:40: covers, confirmations, pacing, who matters, events, reviews, phone. But the Larder stacked on the 7:00 bar makes it 40 tall, well over the booking limit line, so 7:00 reads as overbooked while 7:30 is the bar flagged "at the limit". An owner would stop and frown. |
| 2 | Floor plan (host) | **Fix (small)** | Strong signature screen: sections, table states, waitlist with "Text: table ready", and the T9 suggestion. One allergy dot is missing and one header count is confusing. |
| 3 | Events board | **Keep** (nice-to-haves only) | Right stages, right money, and the event sheet adds up. The builder's header ("9 events · $2,050 in deposits in hand") is a better number than my brief's: it matches the cards (750 + 400 + 400 + 500). Keep it. The "Due this week" strip is a good addition. |
| 4 | Server "My tables" | **Keep** | It's exactly what a server checks: the allergy band can't be missed, the occasion and regular notes are there, and it shows no money or phone numbers. |
| 5 | Guest reserve page | **Keep** | It looks like the restaurant, not the CRM. The time grid, the waitlist link, one allergy field and the "Plan an event" link are all right. |
| 6 | AI receptionist call | **Keep** (one nice-to-have) | The table for 6 at 7 becomes 7:30, the allergy is flagged and the guest confirms, with no staff time. Matches screens 1, 2 and 4 (party of 6, T16, Confirmed). |

**On the builder's departures from the brief:**
- **Events header:** fine, keep it (see screen 3 above).
- **H2 "Clearing" instead of Open:** fine, keep it. It adds realism, and the "3 tables open now" count stays correct (T3, T9, T15).
- **Larder stacked on the pacing chart:** draw it separately (fix 1). A private room event isn't paced against the dining room's booking limit, and stacking it puts a bar far above the line.

## Fixes, ranked (most impact first)

1. **MUST: Screen 1, pacing chart.** Take the Larder off the 7:00 bar so 7:00 shows 18 only, with the same green as the other bars. Remove "The Larder (private event)" from the legend. Add one small pill above the 7:00 bar, or at the right end of the legend row: "The Larder · 22 at 7:00 · private room, not counted in the limit". Delete the "40" label. 7:30 stays the only bar at the line.
2. **MUST: Screen 2, T6.** Add the red allergy dot after "Raman (6)" on T6. Priya's party has a gluten free guest: it's red on screen 1 and red in the Arriving next rail, and the legend says a red dot means "Allergy on the reservation". T5 and T16 have the dot; T6 must too.
3. **Nice: Screen 2, Arriving next rail header.** "5 parties · 32 covers by 7:22" sits above a list of 7 parties, so the count contradicts what's under it. Change it to: "Through 7:30 · 7 parties · 44 covers". Leave the top band as "5 parties · 32 covers / Arriving next 30 min".
4. **Nice: Screen 3, cramped chips in narrow columns.** Shorten the chip text so it fits on one line:
   - "Balance invoice sent $1,140" becomes "Balance sent · $1,140"
   - "Final count due today" (on the board card) becomes "Count due today"
   - "From website chat, 2h ago" becomes "Web chat · 2h ago"

   If there's room, also take about 40px from the event sheet panel and give it to the five columns, so "Amberly-Ross rehearsal dinner" wraps to two lines instead of three.
5. **Nice: Screen 3, "Calendar" appears twice** (sidebar nav and a tab). My brief caused this. Change the sidebar to: Events · Reservations · Guests · Inbox · Payments. Keep the Board · Calendar · Rooms tabs.
6. **Nice: Screen 6, reminder text.** Start it with the business name like the first text does, so the guest knows who's texting: "Wrenfield Kitchen & Bar: See you tonight at 7:30, Nate. Running late or need to change the party size? Just reply here."
7. **Nice: Screen 5, reminder checkbox.** Screen 6 sends the reminder the morning of, because Nate booked the night before. Change the label from "Text me a reminder the day before" to "Text me a reminder before my reservation", so the two screens don't disagree.
8. **Nice: Screen 2, popover placement.** The Weller popover sits on top of the upper part of The Larder block. Anchor it to open left of T12, over the empty space beside T15 and T16, so the Larder block shows whole.
9. **Nice: Screen 4, T15 card.** The open table card has only a dashed left edge, which looks cut off. Give it a full 1px dashed border, matching how open tables look on the floor plan.

Words check: nothing to remove. No job, tech, dispatch, estimate, appointment, check, tab, ticket, tips, comps or sales anywhere. "On the house (Marisol)" in the Weller note is an owner's instruction, not a POS comp. Keep it.

Numbers check: these agree across screens:
- 164 covers, 41 reservations, Larder 22, 33 of 41 confirmed.
- Inbox 2 (screen 1 badge and "2 waiting").
- Whitlock 6 at 7:30 on T16 (screens 1, 2, 4, 6); Weller 7:00 on T12; Kim 7:15 on T5; Raman 7:30 on T6.
- Waitlist 4, longest 18 min.
- Amberly-Ross: $3,117.60 total, $2,367.60 balance.
