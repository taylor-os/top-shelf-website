# Task for each screen builder: draw your industry's 6 screens

Scratch work only. Do not edit any git repo, do not commit, do not push.

Folder root: `C:\Users\taylo\AppData\Local\Temp\claude\e8a30302c63b0c61\503746ae-8215-4629-8d24-dc2bfa57ce43\scratchpad\industry-v2\` (call it V2).

Read, in order:
1. `V2\BONES.md`: the owner's direction (verbatim at the top), the shared records, visual bones, screen set and sample-data rules.
2. `V2\briefs\<industry>.md`: your industry's brief. It is the spec: draw exactly what it says (layout, widgets, words, sample content). Where it is silent, choose what a person in that industry would expect.
3. `V2\kit\README.md`, `V2\kit\kit.css`, and the pages in `V2\kit\examples\` (look at their .jpg renders): every screen must be built from the kit so all industries look like the same product. Copy a template, keep the kit's classes, add page-specific CSS only in a `<style>` block on the page when the kit lacks something (e.g. a hold-shelf grid, a deal step strip). Never edit kit.css or render.py.

Build in `V2\screens\<industry>\`:
- six pages named `1-<short-name>-d.html` / `-m.html` (d = desktop 1440x900, m = phone 390x844) following the brief's screen order, linking `../../kit/kit.css` and `../../kit/icons.js`.
- render each with `python V2\kit\render.py <page> <same-name>.jpg d|m` (or `--all V2\screens\<industry>`).

The layout must be designed for this industry, not the home-services Today screen with new words. Home screens differ in structure, not just labels: the widgets, their order and their shape come from what this industry's owner checks first (per the brief). Staff screens show only what that role needs. Customer-facing screens use `body.cx` with the business's own accent and name, and no "Top Shelf" branding on them.

Quality bar (check every render by opening the .jpg and looking at it):
- Everything the screen is about is visible above the fold; nothing clipped, overlapping, or cut mid-word; no empty half-screens; phone screens readable at phone size.
- Numbers agree across the six screens and add up (totals, counts, balances).
- No word from the brief's banned list appears (write a quick check over your HTML), no em dashes in visible text, no real business or person names, 555 numbers only, the bottom "Sample screens" strip present.
- It should look like a real, busy, well-run business on a normal day.

Report back, short: the folder, the six screens (file, role, one line each), anything in the brief you could not draw or changed and why, and any open question.
