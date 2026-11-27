# Theme pass for each builder

Taylor approved all the layouts. New direction (verbatim): "I like them all but make sure they all have their own theme that matches the industry, can be dark or light depending on what you think it should be based on the industry. Please adjust those and have the customer facing theme match the CRM theme for that industry."

The kit now has a theme system. Read `V2\kit\README.md` section "Industry themes" (V2 = `C:\Users\taylo\AppData\Local\Temp\claude\e8a30302c63b0c61\503746ae-8215-4629-8d24-dc2bfa57ce43\scratchpad\industry-v2`), and look at `V2\kit\examples\themes-preview\contact-sheet.jpg` plus your industry's `<industry>-home-d.jpg` and `<industry>-booking-m.jpg` in that folder: that is your target look. Never edit kit.css, themes.css or make_themes.py.

For each of your six pages in `V2\screens\<industry>\`:
1. Add `<link rel="stylesheet" href="../../kit/themes.css">` right after kit.css, and `class="t-<industry>"` on `<body>` (customer-facing page: `class="cx t-<industry>"`).
2. Customer-facing page: delete any inline `style="--accent:..."` (or other inline color vars) on body so the theme wins; drop page-local fonts/colors that fight the theme. It should read as the business's own page, in the same palette and light/dark mode as the CRM screens. Keep the business's name and wordmark.
3. Convert every hard-coded color in your page `<style>` blocks and inline styles to kit tokens (README lists them): white backgrounds → `var(--panel)` (or `var(--cx-card)` on customer pages); grays → `--ink/--ink-2/--muted/--line`; status colors → `--green/--amber/--red/--blue/--violet` and their `-soft` fills; text on accent fills → `var(--on-accent)` / `var(--accent-ink)`, never #fff. Map your own page variables (`--navy`, `--brass`, ...) to tokens or remove them. Drawn images (SVG photos, cars, parts) stay as they are.
4. Re-render (`python V2\kit\render.py --all V2\screens\<industry>`), open every .jpg and check: nothing left white or light-gray on a dark theme (or dark-on-dark), all text readable, chips/pills/buttons readable, the sample strip present, layout unchanged. Also grep your HTML for `#fff`, `#ffffff`, `white`, `rgb(255` and fixed hex colors left in page styles; anything remaining must be deliberate (say why).

Reply short: theme applied, what you converted, anything that still looks off and why.
