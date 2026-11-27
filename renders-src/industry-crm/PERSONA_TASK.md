# Task for each industry agent: write the screen brief for your industry

You are the voice of one industry: its owner, its staff and its customers. Taylor (who runs Top Shelf) is putting sample CRM screens for your industry on his website so an owner in your industry looks at them and thinks "that's built for a business like mine." Right now every industry's screens share one home-services layout with the words swapped, and Taylor rejected that. Your job is to say, concretely, what each person in your industry needs to see, and to spec the 6 screens a builder will draw.

Read first:
1. `C:\Users\taylo\AppData\Local\Temp\claude\e8a30302c63b0c61\503746ae-8215-4629-8d24-dc2bfa57ce43\scratchpad\industry-v2\BONES.md`: the shared records, visual kit, screen set and sample-data rules. Stay inside it.
2. The industry page on the Top Shelf site that sells to your industry (path given in your prompt), so the screens prove what that page promises.
3. Any real Top Shelf CRM kit already built for your industry (paths given in your prompt). Where a real kit exists, its screens and words are the truth: follow what it actually shows and how it's organised, because Taylor is building these for real and the samples must match.
4. The current draft screens for your industry, if any (path given), to see what NOT to repeat.

Think like the people, not like a designer: what does the owner open the app to check at 7 AM? What does the front desk need while the phone rings? What does the employee on the floor / in the field / in the chair need with one hand? What does the customer want from a text or a link? What would feel wrong or foreign in your industry (words, widgets, numbers)?

Write `C:\Users\taylo\AppData\Local\Temp\claude\e8a30302c63b0c61\503746ae-8215-4629-8d24-dc2bfa57ce43\scratchpad\industry-v2\briefs\<industry>.md` with:

1. **Business and cast.** One made-up DFW business (name, city, size: staff count, locations), and the named people who appear: owner, 1-3 staff roles, 4-10 customers. All fictional; check names against your sense of real DFW businesses and avoid lookalikes.
2. **Roles and what they need first.** For owner, each staff role, and the customer: the top 5 things they look for, in order, and the one thing that would make them trust or dismiss the app.
3. **Words.** The industry's own names for the bones (Customer, Visit, Deal, Work item, Money, Team...), the nav labels in order for the owner and for each staff role, and a list of words that must NOT appear (they belong to other industries).
4. **The 6 screens** (follow the screen set in BONES.md; you may swap which role gets screens 3-4 if that serves your industry better). For each: role, device (desktop 1440x900 or phone 390x844), the screen's job in one line, then a layout spec a builder can follow without guessing: regions top to bottom / left to right, each widget, and the exact sample content in it (names, times, amounts, statuses, message text). Make the signature screen (2) unmistakably your industry (a floor plan, a chair-by-chair day, a matter page with deadlines, a listings grid with website status, a shop board, a class schedule with capacity...).
5. **How it uses the bones.** One short table: each screen → which shared records it reads (so the backend stays common).
6. **Watch-outs.** Compliance or tone issues (e.g. no diagnoses, no case facts, no alarming numbers), and anything from the real kit the builder must keep.

Be specific and short; the builder draws exactly what you write. No marketing copy, no em dashes. Do not open or run any app, do not edit any repo, do not commit. Reply with the brief's path and a 5-line summary of what makes your industry's screens different from home services.
