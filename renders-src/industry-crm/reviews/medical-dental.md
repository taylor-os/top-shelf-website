# Medical & Dental: review of the 6 screens

Reviewed as Dr. Fairchild (owner), Lupe (front desk), Kendra (hygienist) and Megan (patient), from the six .jpg renders. Overall these read as a dental office: the day is organized by chair, the words are dental, and there are no charting, claims or home-services words anywhere. The practice looks healthy, not struggling. Texts and the patient page keep to the HIPAA promise: no visit reasons in any message. Every count I checked agrees across screens: Op 1 has 9, Op 2 has 7 and Op 3 has 8 patients, recall is 31 of 52, 2 fit the 1:00 ASAP slot, 2 cleanings are done before Hector, the estimates total $2,460, and the 3 replies match the inbox badge of 3.

## Verdict per screen

| # | Screen | Verdict | Why |
|---|---|---|---|
| 1 | Owner home | **Keep** (small fixes) | Shows what she checks at 7 AM, in the right order: chairs, confirmations, money, new patients, recall. The "Today by chair" lanes are the best owner widget in the set. |
| 2 | Schedule by chair | **Fix** | It's the right signature screen, but the red "now" line runs through the text of Hector's and Mason's blocks, so they read as struck through or cancelled. The 9:58 cancellation also doesn't name who cancelled. |
| 3 | Front desk | **Keep** (one fix) | It's what Lupe needs: the call bar with name, visit and Unconfirmed, then the counter, tomorrow's confirmations and recall. The subtitle's "25 patients" needs one line of explanation (see fix 2). |
| 4 | Hygienist "My chair" | **Keep** | Right priorities: the rebook is booked, family member due, "Ready for checkout" as the big button, and no money on the screen. "2 done this morning" is correct; my brief's "3" was wrong. |
| 5 | Patient page | **Keep** (one fix) | It's family-first, there's no reason for the visit anywhere, it's styled as the practice, and paying is one tap. The card icons look like broken placeholders. |
| 6 | AI receptionist | **Keep** (wording) | The lunch call, two bookings, an auto-text with no PHI, the confirmation, then a human reply: exactly the page's story. Two labels read oddly. |

## The 24 vs 25 count: is it clear?

The builder's story holds together:
- At 7:10, the owner screen shows 25 patients with Lowry at 10:30.
- Lowry cancels at 9:58, so the schedule at 10:20 shows 24 patients and 2 open hours.
- June Whitaker takes the 10:30, so the front desk at 10:58 shows 25 patients and 1 open hour.

**It isn't clear enough as drawn.** Lowry is named only as a tiny tile on screen 1, the schedule never says who cancelled, and the front desk never says the 10:30 got filled. A prospect looking at screens 1, 2 and 3 side by side will see 25, 24, 25 and assume it's a mistake. Fixes 2 and 3 tie it together with two short text changes, without changing any number.

## Ranked fixes (at most 12)

1. **MUST. Screen 2: the "now" line strikes through appointments.** At 10:20 the red line crosses the "Cleaning & exam" text in Hector Ruiz's and Mason Pike's In chair blocks, so they look cancelled. Draw the line behind the blocks (z-index under the cards) and show it only in the gaps and the time rail, with a small red dot and "10:20" label in the rail. Or move it 10px so it clears the text. It must never cross a patient's text.
2. **MUST. Screen 3: explain the 25.** Change the subtitle from "Tue, Dec 1 · 10:58 AM · 25 patients today · 1 open hour, Op 2 at 1:00" to "Tue, Dec 1 · 10:58 AM · 25 patients today · June Whitaker took the 10:30 opening · 1 open hour, Op 2 at 1:00".
3. **MUST. Screen 2: name the cancellation.** In the Op 1 10:30 open block, change "10:30 Open · cancelled 9:58 AM" to "10:30 Open · Lowry cancelled 9:58 AM". Use the same surname on screen 1's tile, and give Lowry a first name on screen 2 if there's room (e.g. "Dana Lowry").
4. **MUST. Screen 5: replace the blank card icons.** The three empty grey rectangles look like a broken page, which is the last thing a patient should see next to "Pay". Replace them with the plain text "Visa · Mastercard · Amex · Discover · Apple Pay", or remove the row and keep "Paid securely by card" with the lock.
5. **Nice. Screen 2: take Megan Brennan off the ASAP list.** The front desk books Liam "Dec 10, 3:30 next to Mom", and the patient page shows both on Dec 10. Megan wanting a sooner slot works against that family block. Replace the row with "Nell Archer · Cleaning & exam · has Dec 15, wants sooner · afternoons · fits Op 2 1:00".
6. **Nice. Screen 6: fix the summary labels.** Change "Callers" to "Caller" and the value to "Grace Oyelaran, new patient, booking for herself and daughter Zoe, 6". Change "Asked" to "Reminded" and the value to "Bring insurance card and photo ID". As drawn, "Asked" reads as if Grace asked something.
7. **Nice. Screen 1: say which review is waiting.** The card shows Kurt Bauer's 5-star review next to "1 waiting for a reply", so it's unclear whether his is the one waiting. Put the chip on his review row as "Not replied yet", or change the chip to "Kurt's review is waiting for a reply".
8. **Nice. Screen 1: put real names on the lane tiles.** "AL", "MS", "SR" and "IS" read like codes, not patients. Use surnames like the other tiles: Lindqvist, Santos, Reyes, Shah. Shrink the font one step if the 30-minute tiles are too narrow, and keep the NEW tag on Santos and Reyes.
9. **Nice. Screen 3: "Text 4 again" doesn't match the rows.** Three rows say "Text again" and Cole Barrett's says "Call". Change the button to "Text 3 again", or change Cole's button to "Text again" so there are 4.
10. **Nice. Screen 4: the review request shouldn't look like a to-do.** A ticked checkbox for something that happens on its own is confusing. Swap the checkbox for a small clock icon and keep "Review request · sends automatically at 1:00 PM" as plain info. Checkboxes stay only on what Kendra does herself.

Departures from my brief that I agree with (keep them): the Lowry patient, which makes the 9:58 cancellation real; "2 fit" instead of 3 for the 1:00 slot (the list really has 2); "2 done this morning"; the "Replies waiting" card on the front desk; "Patient since 2019" on the call bar; "AI receptionist answers the phones" in the lunch block; and the "Booked by AI" chip on screen 6.

No privacy slips found. No appointment types or reasons appear in any patient-facing text or on the patient page, and the balance shows only a visit date. The one compliance claim (the HIPAA setup chip on screen 1) matches the page.
