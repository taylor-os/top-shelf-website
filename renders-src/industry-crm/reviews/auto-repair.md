# Auto repair: review of the 6 drawn screens

Reviewed as Ray (owner), Dana (service advisor), Marcus (technician) and Brenda (car owner). I looked at every .jpg and zoomed in on the drawn part photos in the .png files.

Overall: this reads as a repair shop, not a car lot or a plumber. I found no car-lot or home-services words (no Inventory, stock, recon, dispatch or "on my way"). The kit's board columns, approval chips, totals bar, job clock and authorization flow are all there. The numbers agree across screens except the one the builder flagged. The biggest problem a shop person would spot is the brake pad photo.

## Verdict per screen

| # | Screen | Verdict | Why |
|---|---|---|---|
| 1 | Owner home | **Fix** | Right things in the right order: next step, ready for pickup, money owed, waiting on OK, declined work to chase, then counts, rush, money, calls, team. "Approved today $1,342.00" has nothing behind it (fix 1). |
| 2 | Shop board | **Keep** (one nice-to-have) | The signature screen works: five kit columns, rush card on top, OK chips, parts ETAs, a paid/unpaid split in Done. The Waiting column order doesn't follow the active sort (fix 4). |
| 3 | Repair order | **Fix** | Layout and words are right, and the approval notice plus the per-job Approved/Declined chips are exactly what an advisor needs at the counter. The front pads photo shows the wrong part (fix 2). |
| 4 | Tech My jobs | **Keep** (nice-to-haves) | One big red Stop, Done, photo, notes, no prices, "Customer car" instead of a name. Belt photo reads well. Tensioner caption and icon are small fixes (fixes 6, 7, 8). |
| 5 | Customer estimate | **Fix** | Line-by-line choice, photos and a running total are the trust moment, and they're clear. But the pads photo is wrong here too (fix 2), and the selected Approve button is a red slab (fix 3). The form cut-off is acceptable (fix 9). |
| 6 | AI call thread | **Keep** | Plain, believable, shop-specific (wrecker, drop box, estimate before work). Nothing to change. |

## Ranked fixes (at most 12)

1. **MUST. Screen 1, Today's money card.** Replace "Approved today $1,342.00" with **"Approved today $615.00"**, and under it in small grey text: **"Brenda Ochoa, RO 2052 · 2 estimates still out"**. Leave "In today $1,504.95", "Owed $302.34" and "Average RO this week $418" as they are. Why: $615 is the only approval today that any screen shows (screens 1, 3 and 5), and "2 estimates still out" matches the "Waiting on the customer's OK · 2" card.

2. **MUST. Screens 3 and 5, the "Front pads, 2 mm left" photo (img/pads.svg).** What's drawn is a curved drum-brake shoe on an inch ruler. Any tech or owner sees that's the wrong part for "front brake pads and rotors". Redraw it as a **flat disc brake pad seen from the edge**: a dark steel backing plate with the two small mounting ears, and a very thin friction layer on top. Put a new pad beside it with a thick friction layer so the wear is obvious. Use a millimetre scale or no ruler, never inches. Keep the caption "Front pads, 2 mm left". The rotor photo (concentric grooves, rust lip, red caliper edge) reads well; keep it.

3. **MUST. Screen 5, the customer page's accent color.** The selected "✓ Approve" buttons and the "You are approving" box are dark red, so the customer's yes looks like a warning or stop button on a $420 repair. My brief asked for that red; it's my mistake. Change Turnbuckle's accent to a **deep navy (#1F3A5F)**: the shop initials badge, the phone number, the selected Approve buttons and the outline of the "You are approving" box. Leave the selected Decline as charcoal. It still looks like the shop's own page and not the emerald staff app.

4. **Nice-to-have. Screen 2, Waiting column order.** "Rush first" is the active sort, so after rush the column should run soonest Ready by first: **RO 2054 Ford Ranger (Today 4:00 PM), RO 2052 Camry (Today 5:00 PM), RO 2053 Tahoe (Wed 12:00 PM), RO 2055 Sorento (Wed 5:00 PM)**. Brenda's Camry stays fully visible as the second card, and the Sorento becomes the one that peeks. The other columns already follow this rule.

5. **Nice-to-have. Screen 1, "Ready for pickup" row for Priya.** "not texted yet" makes Dana look slow on the owner's home. Change it to **"Done 40 m ago · ready text not sent"** and give that row a small emerald **"Send ready text"** button in place of Text. It reads as an action, not a lapse, and it shows the ready-text automation.

6. **Nice-to-have. Screen 4, the tensioner photo caption.** A still photo can't show a wobble. Change "Tensioner pulley wobble" to **"Tensioner pulley, worn bearing"**. The belt photo ("Old belt, cracked") reads very well; keep it.

7. **Nice-to-have. Screen 4, icon on "Whole repair order: Waiting on parts".** It's a clock now. Use the **package/box icon** (the kit's icon for parts, and the same one the Parts line on this card uses), so it isn't confused with the job clock.

8. **Nice-to-have. Screen 4, show the second card's Start button.** Marcus's next job is cut off at its title, so the red Stop / emerald Start contrast never shows. Shrink the two photo tiles from about 125 px to **72 px tall squares** (in screen pixels, at 1x). If that's not enough room, also drop the extra "Ready by Today 12:00 PM" line on the rush card, since "needed by Today 12:00 PM" already says it. That should bring card 2's "RO 2052 · Waiting · Booked 1.8 h" and a full-width emerald **"▶ Start clock"** into view above the tab bar.

9. **Nice-to-have, leave as is unless it's cheap. Screen 5, the form below the fold.** The page stops at "Your full name: Brenda Ochoa", which reads as a page you scroll. The authorization sentence and "Send my answers" sit just below it. Don't make Send a sticky bar: the kit keeps the authorization sentence directly above Send and never hides it. If there's room to save, shorten the car card to one line, "2018 Toyota Camry · Silver · RO 2052 · 61,280 mi". The VIN can go on the customer page.

## Checks that passed

- **Counts:** 12 cars in the shop, 1 rush, column counts 4/3/2/1/3, and each tech's open ROs and jobs match the board. Owed $302.34 = $89.94 + $212.40. In today $1,504.95 = $1,148.20 + $356.75. Brenda's $615 / $0 / $83 match on screens 1, 3 and 5.
- **Words:** shop words throughout (RO, Ready by, Waiting on parts, Quality check, Move to..., bill, Shop board, How your shop runs). Nothing from car lots or home services.
- **Privacy and tone:** the tech screen shows no customer names, phone numbers or prices. Approval is a typed name, no signature pad. There are no demo or preview labels. Nothing looks overdue except one $212.40 balance, which is believable.
- **Departures from the brief:** the Waiting order is the only one worth changing (fix 4). The board header line "12 cars in the shop · 1 rush", the "Estimate 1 · rate $130/h" note on the totals bar, and the job icons in History are good additions; keep them.
