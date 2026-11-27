# Home services: review of the 6 rendered screens

Reviewed `screens/home-services/*.jpg` as the owner (Travis), the dispatcher (Brandi), the tech (Kyle) and the homeowners (Gloria, Hannah). Overall the set reads like a real HVAC shop on a cold Wednesday. Each person sees what they check first, in their own words. The numbers agree across screens: Gloria is 1:00–3:00 PM with Kyle on screens 1, 2 and 6; Dale Pruitt is done and paid at $389.00; the job total is $406.17 and the tips add up; the estimate options are $289.26, $10,405.85 and $12,827.55; and "5 awaiting" matches the Awaiting tab. The cast is as decided, Marcus Reed stays.

## Verdict per screen

| # | Screen | Verdict | Why |
|---|---|---|---|
| 1 | Owner Today, desktop | **Keep** | The 7:50 AM view is right: the overnight call is unassigned, the missed-call "YES" reply is waiting, and there's one unpaid invoice and one signed estimate. It matches the brief. |
| 2 | Dispatch board, desktop | **Fix** | It's the strongest screen and only home services has it. But Kyle's first block (Dale Pruitt, 7:00–7:45) is too narrow and reads as a broken tile: "7:00–7:…", "Dale P…", "No hea…", "1409 As…". |
| 3 | Tech get paid, phone | **Keep** (small polish) | One-hand payment at the door with tip and the "Charge card · $446.79" button. It's exactly what a tech does at 2:40 PM. |
| 4 | Owner estimate chase list, phone | **Keep** (small polish) | This is the "estimates go cold" problem from the page, made concrete: days waiting, last contact, and Call/Text buttons. |
| 5 | Homeowner estimate, phone | **Keep** (small polish) | It reads as the HVAC company's own page, not the software. Repair vs replace is clear, and the price spread is believable. |
| 6 | AI call + texts, phone | **Fix** | The story works. But the "Sent automatically" tag on the 8:02 AM confirmation isn't true to the story: Brandi assigned Kyle and sent it. |

The builder departed from the brief in two places, and both are OK:
- **Screen 6, AI summary card:** drawn as labeled rows (Address / Problem / Booked) with "AI receptionist answered" instead of a plain paragraph. It's easier to scan and the facts are the same. Keep it.
- **Screen 1, owner sidebar:** drops Inventory and Automations, so it's cleaner than the homepage hero. Fine (see fix 9 if exact parity matters).

## Ranked fixes (max 12, most important first)

1. **MUST, Screen 2: Dale Pruitt block is unreadable.** Change the visit to **7:00–8:00 AM** so the block is a full hour wide. Put the "Done" pill on the same row as the time, right-aligned (the time may truncate; the pill must not wrap to its own line). The block should then read: row 1 "7:00–8:00 AM" + "Done"; row 2 **"Dale Pruitt"** in full; row 3 "No heat, furnace…"; row 4 "1409 Ashwood Ct, Al…". Keep Carla Mendez at 8:00–10:00 AM, butted against it. Screen 1 already says 7:00 AM, so nothing else changes.
2. **MUST, Screen 6: wrong tag on the confirmation text.** Replace "**Sent automatically** · 8:02 AM" with "**Confirmation** · 8:02 AM" (same green tag style as "On my way · 12:41 PM"). In the story, Brandi assigned Kyle and sent the confirmation from the board. Nothing in the app sends it on its own after the AI call.
3. **MUST, Screen 6: "Assign to me" pill says nobody owns this thread.** By 12:43 PM Brandi has handled it. In the app, an assigned conversation shows the assignee's name in that pill. Change it to **person icon + "Brandi Kessler"**, keeping "+ Book job" and "View client".
4. **Nice-to-have, Screen 2: let the Done blocks breathe.** Raymond Ochoa ("Upstairs bedroom w…", "815 Kingsbridge Dr, …") and Bev Halloran ("Fall tune-up, two sys…") truncate hard while dimmed. Optional: keep the dim at 60% opacity but use the darker grey text for the client name so the finished stops can still be read at a glance.
5. **Nice-to-have, Screen 3: the job header behind the sheet doesn't match the app.** Behind the dim, the title area shows as a light grey card. In the app (and in homepage `s2-job-m.jpg`) it sits inside the emerald band with white text. Draw it as the emerald band, white "No heat, upstairs and down", white "Gloria Banks", white address, with the amber "Working" pill. Then dim the whole band at 50%.
6. **Nice-to-have, Screen 5: the long material line wraps its price onto a second line.** Change the option 2 material line to **"3-ton heat pump + air handler · 1 × $6,980.00"**; the SEER rating is already in the option name. Do the same for option 3: "3-ton variable-speed heat pump + air handler · 1 × $8,940.00". Totals don't change.
7. **Nice-to-have, Screen 4: subtitle orphan.** "Quote your clients for upcoming work." wraps and leaves "work." alone on a line. Give the subtitle the full width by moving "+ New estimate" up beside the title "Estimates" (same height as the title), or shrink the button to "+ New". The words stay.
8. **Nice-to-have, Screen 3: method buttons have icons the app doesn't have.** The app's method grid is text only. Either remove the icons (truer to the app) or keep them (harmless). If kept, give Cash App and Venmo different icons; right now both are the same phone glyph.
9. **Nice-to-have, Screen 1: sidebar parity with the homepage hero.** The hero shows "Inventory" under Reviews (half cut off by Settings). If Taylor wants the industry page's owner screen to match the homepage exactly, add "Inventory" under Reviews. Otherwise leave it, since the shorter nav is cleaner.

Nothing on any screen feels foreign to the trade. No words from other industries, no alarming counts, no overlaps on the board. The amounts are plausible for DFW HVAC.
