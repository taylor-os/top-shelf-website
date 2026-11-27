# Fitness screens: review (owner, front desk, coach, member)

Reviewed all 6 renders in `screens/fitness/`. Overall: this reads like a gym, not a home-services app with the words swapped. The schedule, capacity bars, waitlist, check-in and roster all ring true, and the numbers mostly agree across screens. Only small fixes are needed.

Cross-screen checks that pass: the 88 of 120 spots booked today add up from the 8 classes. The per-class counts are the same on the dashboard, the week grid, the check-in "Next class" card and the member app's "spots left" (20-7=13, 16-11=5, 12-9=3, 16-12=4). The 5:30 PM class shows "16 of 16 · 3 waiting" everywhere, and Deja is on that roster. Brianna's declines (Nov 22, 25, 29) match the real retry schedule and the dashboard line. Intro 3 of 8 matches the 3 first-timers named at the desk. Caleb's "running 5 min late" text matches his 6:36 AM check-in. Ethan's "last in Nov 14" matches the desk task. Luis carries no billing badge on the coach's screen. Tasks "3" matches the desk's Tasks card.

## Verdict per screen

| # | Screen | Verdict | Why |
|---|---|---|---|
| 1 | Owner dashboard | **Fix** | Right content in the right order (classes, payments, who to win back, overnight, reviews). The title is still serif, and the overnight counts don't match the rows shown. |
| 2 | Classes week | **Keep** (font fix only) | The signature screen works: capacity bars, Full and waiting chips, a No coach flag, faded past days, and a roster panel with the waitlist. The builder put different names on the 5:30 PM roster than on the 6:30 AM one. That's a good change: my brief had double-booked Jerome and Kira. |
| 3 | Front desk check-in | **Fix** (small) | Exactly what the desk needs: scan box, a past-due card with Collect / Let in anyway / Text her, and today's list with Undo. The Tasks card the builder added is a good change. The "Phones" line contradicts the dashboard. Serif title. |
| 4 | Coach roster | **Keep** | Big Here / No-show buttons, the first-timer flagged, "7 here", Undo toast with a countdown, no billing. A coach would use this. |
| 5 | Member app Today | **Keep** | It's the gym's own app with its own color, next class, check-in code, and spots left that match the schedule. Paid through date at the bottom. |
| 6 | AI intro text thread | **Keep** (one wording fix) | The call card laid out as Asked / Booked / Told her beats the paragraph I specced. Automatic and staff texts look different. The reminder chip is clear. |

## Fixes, ranked (most important first)

1. **MUST. Screens 1, 2, 3: page titles in the kit font.** "Larkspur Strength Club", "Classes" and "Check-in" are drawn in a Georgia-style serif. Use Figtree, same weight as other industries' H1 (already decided).

2. **MUST. Screen 1: overnight counts must match the rows.** The tile says "4" calls and "AI receptionist booked 2", and the card header says "4 calls · 1 text". But the card lists 2 calls (Jasmine, one missed call) and 1 text, with only 1 booking. Change the tile to **"Overnight calls" / "2" / "AI receptionist booked 1 · 1 texted back"**. Change the card header to **"2 calls · 1 text"**. Leave the rows as they are.

3. **MUST. Screen 3: the "Phones" card contradicts screen 1.** "Today: 2 calls answered, 1 class booked" at 7:04 AM implies calls after midnight. Change it to **"Overnight: 2 calls, 1 intro booked"**.

4. **NICE (high). Screen 6: the AI receptionist must quote the full price.** In "Told her", change the text to **"Monthly is $59 plus a $25 sign-up fee, and Unlimited classes is $119"**. An owner will check that the AI didn't leave off the sign-up fee. It's also the plan as specced.

5. **NICE. Screen 2: drop the redundant "· on".** In "Texts for this class", the toggles already show on. Make the labels **"Booking confirmation"** and **"Reminder 2 hours before"**.

6. **NICE. Screen 5: keep "spots left" on one line.** "13 spots / left" wraps onto two lines in every row. Narrow the coach column or the Book button so **"13 spots left"** fits on one line, right-aligned before Book. Keep the amber color on "3 spots left".

Nothing foreign or alarming: no job, invoice or customer words, no minors, no body data, no "CrossFit". There are 3 payment issues and 3 lapsed members out of 412, so it looks like a healthy, busy gym.
