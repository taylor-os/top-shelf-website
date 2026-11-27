# Task: make each approved CRM screen set the same business as its sample website

Taylor approved the 66 CRM screens (layouts and words) and then chose "same business, same look": each industry's CRM and its sample website are ONE fictional business. A guest books on the website and lands in that business's CRM. The CRM palettes are already regenerated from the websites in `renders-src/industry-crm/kit/themes.css` (via `make_themes.py`, done; don't edit those).

Worktree `C:\Users\taylo\top-shelf-website-focus`. Don't commit or push. Edit only the industries named in your prompt.

For each industry (`renders-src/industry-crm/pairs.json` gives `business`, `old_business`, `locale`, `website_dir`, fonts):
1. **Study the website.** Read `websites/<dir>/BRIEF.md` and all its pages (team/attorneys/about pages especially). Note its name, locale, logo (`websites/<dir>/assets/*.svg` or the logo markup), owner and staff names, services, hours, and the way it names things.
2. **Rename** in every `renders-src/industry-crm/screens/<slug>/*.html`:
   - `old_business` becomes `business`.
   - The business's town or area becomes the website's `locale`. Customer street addresses can stay as plausible DFW-style addresses, but the business's own address and town must match the website if the website shows them.
   - Where the website names people (owner, doctor, attorneys, stylists, chef), use those names for the matching CRM roles everywhere they appear, with matching initials in avatars.
   - Keep the customer cast, unless a name collides with a surname used in another industry's screens. Check with a grep across `renders-src/industry-crm/screens/*/`.
3. **Fit the trade** where the website's focus differs from the screen data:
   - Make the smallest data edits so the screens fit that focus.
   - Keep every number consistent across the six screens.
   - Don't add features or claims.
4. **Customer-facing screens** (`body.cx`) must read as pages of that website:
   - Use the website's logo (inline the SVG, or reference it by relative path from the screen HTML) and the business name in the website's wordmark style.
   - Fonts come from the theme automatically. Remove any page-level font or color overrides that fight the theme.
   - The staff screens keep the kit look with the new theme. The company tile in the sidebar shows the website's logo mark if it reads at that size, otherwise the initials.
5. **Re-render**: `python renders-src/industry-crm/kit/render.py --all renders-src/industry-crm/screens/<slug>`. Open every .jpg and check:
   - nothing is clipped
   - text is readable in the new theme
   - no old business name, town or person remains (grep `old_business` and the old owner names)
   - no em dashes
   - only 555 numbers
   - the Sample strip is present
   Delete the raw .png files `render.py` leaves.

Report briefly, for each industry:
- what you renamed (people, places)
- any data edits made for fit
- any screen that still looks off
