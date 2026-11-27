# Top Shelf CRM screen kit

This kit is plain HTML and CSS that reproduces the emerald FieldPro look from the homepage captures, and adds a light or dark theme for each industry (see Industry themes below). Each industry can lay its screens out differently and they will still read as one product. The font is Figtree 400/500/600, the same faces FieldPro loads, pulled from Google Fonts. The icons are the Heroicons v2 outline set, which is what FieldPro uses. All 324 of them live in `icons.js`. Everything renders offline except the font.

## Start a screen
1. Copy the example closest to what you need into your folder and give it a name ending in `-d.html` (desktop) or `-m.html` (phone):
   - desktop staff screen: `examples/home-today-d.html` (sidebar + band + dock), or `kanban-d`, `resource-day-d`, `detail-d`
   - phone staff screen: `examples/home-today-m.html` (band + bottom tabs) or `chat-m` (top bar + thread)
   - customer-facing page: `examples/booking-m.html`
2. Fix the `../kit.css` and `../icons.js` paths so they point at the kit folder. `icons.js` has to be the first thing inside `<body>`. Add `themes.css` and your industry's `t-` class.
3. Change the nav items, the words and the data. Keep the classes. `examples/parts-d.html` shows every part that the other examples leave out.
4. Icons: `<svg class="i"><use href="#wrench-screwdriver"/></svg>`. The name is any Heroicon outline name. Sizes: default 20, `s3` 12, `s35` 14, `s4` 16, `s6` 24, `s8` 32.

## Industry themes
Each industry has its own palette in `themes.css`. Some are light and some are dark, and every theme keeps the same layout and components. Each palette is taken from that industry's paired sample website (`../pairs.json` names it), so the CRM and the site read as the same business. The customer pages for an industry use that industry's CRM palette and, where the theme sets them, the website's fonts.

**Opt in.** Load the stylesheet after kit.css, then add the theme class to `<body>`:
```html
<link rel="stylesheet" href="../../kit/kit.css">
<link rel="stylesheet" href="../../kit/themes.css">
<body class="t-restaurants">              <!-- staff screen -->
<body class="cx t-restaurants">           <!-- customer page: booking, hub, pay link -->
```
The themes are `t-home-services`, `t-real-estate`, `t-salon-spa`, `t-medical-dental`, `t-legal`, `t-retail` and `t-vet` (light), plus `t-car-lots`, `t-auto-repair`, `t-auto-detailing`, `t-fitness` and `t-restaurants` (dark). A page with no theme class renders the original emerald look. To see every palette at once, open `examples/themes-preview/contact-sheet.jpg`.

**Rule: page styles never hard-code a color.** That includes `<style>` blocks and `style=""` attributes: no `#fff`, no `#1c1917`, no `rgb(245 158 11 / .1)`. Use the tokens below so the theme reaches your page:
- Surfaces:
  - `--canvas`: page background
  - `--panel`: cards, tables, calendar, tiles. Replace every white background with this
  - `--panel-2`: insets on a card
  - `--head`: group rows and headers
  - `--hatch`: blocked-time stripes
  - `--tint`: neutral chip fill
  - `--well`: inputs
  - `--sink`: deep background
- Text:
  - `--ink`: main text
  - `--ink-2`: secondary text
  - `--muted` / `--muted-2`: labels and meta (both AA on `--panel`)
  - `--faint`: icons and disabled text only, never body text
- Lines: `--line`, `--line-soft`, `--line-strong`
- Brand:
  - `rgb(var(--b-500))`: the accent
  - `rgb(var(--b-500) / .12)`: accent tints
  - `rgb(var(--b-600))` or `rgb(var(--b-700))`: accent-colored text (AA on `--panel` in every theme)
  - `rgb(var(--b-50))`: a tinted background
- Buttons and solid accent fills:
  - `--grad-1`, `--grad-2`, `--grad-3`: the primary button gradient
  - `--on-accent`: text on those fills. It is dark in the amber, gold and orange themes (home-services, car-lots, fitness, restaurants) and cream in others, so never put `#fff` on `--b-500` or `--grad-*`
  - `--focus`: focus ring
- Chrome (sidebar, band, bars, tab bar):
  - `--side`, `--band`, `--bar`, `--tabbar`: chrome backgrounds
  - `--on-em`, `--on-em-dim`, `--on-em-faint`: text on chrome
  - `--em-line`: lines on chrome
  - `--nav-on-bg`, `--nav-on-ink`: the active nav item
  - `--band-edge`: hairline under the band
  - `--band-btn-bg`, `--band-btn-ink`: solid buttons on the band
  - Chrome is dark with light text in every theme, so `rgba(255,255,255,.x)` overlays are allowed on chrome only
- Status colors:
  - `--green`, `--amber`, `--red`, `--blue`, `--violet`: dots, borders, big numbers
  - `--green-ink`, `--amber-ink`, `--blue-ink`: chip text (use `--red` as the red chip text)
  - `--*-soft`: chip and tile fills
  - `--rose`: rose events
  - `--badge`, `--badge-ink`: count badges
- Chat: `--bubble-out`, `--bubble-out-ink`
- Shadows: `--shadow`, `--shadow-sm`
- Customer pages (`.cx`):
  - `--cx-bg`, `--cx-card`, `--cx-ink`, `--cx-ink-2`, `--cx-muted`, `--cx-faint`, `--cx-line`: page, cards, text and lines
  - `--accent`, `--accent-ink`, `--accent-soft`: the business color, the text on it, and its tint. It is also used as text, so it can differ from the staff accent (home-services uses the website's navy, not its amber)
  - `--cx-logo`, `--cx-logo-ink`: optional logo-tile colors; they fall back to `--accent` and `--accent-ink`
  - `--font`, `--font-head`: the website's body and heading fonts, set on `body.cx` only when the theme has them. `--font` reaches body text and buttons; `h1`, `h2`, `h3` and `.cx-name` use `--font-head`. Write `font-family: var(--font)` or `var(--font-head)`, never a font name. Staff pages keep Figtree so every industry reads as the same product

**Converting an existing page:**
- **Inline accents on customer pages.** Delete any `--accent` / `--accent-soft` / `--accent-ink` written in `style=""` on `<body class="cx">`. An inline style beats the theme, so the page would keep its old color.
- **White backgrounds.** `background:#fff` becomes `var(--panel)`. On a customer page it becomes `var(--cx-card)`.
- **Text on accent fills.** `color:#fff` on an accent fill becomes `var(--on-accent)`. On chrome, `#fff` is fine, but `var(--on-em)` is better.
- **Fixed status hues.** `#f59e0b`, `#10b981` and the like become `var(--amber)`, `var(--green)` and so on. Their tinted fills become `var(--amber-soft)` and the other `--*-soft` tokens.
- **Your own color variables.** Map any variable you defined yourself (for example `--navy` or `--brass`) to kit tokens, or drop it.
- **Placeholder photos.** A gradient you drew for a photo placeholder should use `rgb(var(--b-200))` through `rgb(var(--b-600))`.
- **Check both modes.** Render the page in a dark theme and confirm nothing is still white.

**Changing a palette:** edit `PALETTES` in `make_themes.py`, then run `python make_themes.py`. Two optional keys: `fonts=("Heading", "Body")` gives the customer pages that theme's Google Fonts (copy them from the website's entry in `pairs.json`; `themes.css` loads every family named in one `@import`), and `deep=(...)` darkens `b-600`..`b-950` further in a light theme whose accent is bright (amber, teal), so accent text stays AA. It rewrites `themes.css` and re-checks WCAG AA contrast for text, chips, buttons, the active nav, chat bubbles and customer pages. It exits with an error if any check fails. Never hand-edit `themes.css`.

## Render
```
python render.py examples/kanban-d.html out/kanban-d.jpg d     # desktop: 1440x900 @2x -> 1440x900 JPEG q85
python render.py my-screen-m.html out/my-screen-m.jpg m         # phone: 390x844 @3x -> 585x1266 JPEG q85
python render.py --all <folder>                                 # every *-d.html / *-m.html, .jpg written beside each
```
The raw PNG is saved next to each JPEG. The script adds a dark strip at the bottom that says "Sample screens · sample data, not a real business". The viewport is shortened by the strip's height, so the strip covers nothing. `--no-strip` turns the strip off; it is only for side-by-side checks against the real captures in `compare/`. The script needs Playwright Chromium and Pillow.

## Components
**Desktop shell**
- `.app` (add `.has-dock` for the right phone rail, `.collapsed` for the 72px icon rail): the page grid
- `.side`: the emerald sidebar. Inside it go `.brand` (the company name, plus an optional `.mark` square), `.nav` (links; `a.on` = active, `.lbl` = label, `.sec` = group heading, `.badge` = red count), `.side-foot` (Settings + `.toggle`), `.side-user` (avatar, name, role) and `.side-co` (company switcher)
- `.main` > `.band` + `.page`: the content column, with the header band on top and padded content below it
- `.dock` > `.ph`: the 52px emerald phone rail with its call button and badge

**Header band** `.band`: `h1`, `.sub` (wrap emphasis in `b`), `.right` (actions), `.avatar-ring`, `.back` (back link), `.meta` (an icon row), `.chip` (turns translucent on the band), `.btn` (white outline on the band; `.btn.primary` is solid white), `.band-tabs` (tabs that sit on the band, active one in the canvas color)

**Phone shell**
- `.phone`: a 390px screen
- `.statusbar`: optional fake status bar
- `.band`: same as desktop, with tighter padding
- `.m-bar`: emerald top bar with back, title + `small`, and actions
- `.seg`: segmented tabs on emerald (Recent / Contacts / ...)
- `.tabs`: fixed emerald bottom bar. Use 5 `a`; `.on` = active; put the icon in `.ic`; add `.badge` for a count
- `.fab`: round action button
- `.list-card`: white list box

**Cards and numbers**
- `.tiles` (`--n` = columns; `.wide-last` stretches the last tile) > `.tile`, containing `.l` label, `.v` value (`.green` / `.amber` / `.red`, `small` for "of 4") and `.s` sub
- `.card` (`.pad`, `.pad5`, `.clip`): white surface
- `.card-h`: emerald title strip at the top of a card (`.r` sits on the right, `.count` is a pill). Pair it with `.card-b` for the body
- `.bar` (`.tall`): standalone emerald section bar like TODAY'S JOBS. It holds `h2`, `.count`, `.note` and `.r`
- `.attn`: needs-attention card with `.hd`, `.ic-box`, `.t`, `.count-pill` and `.it` rows. `.attn-m` is the compact phone version
- `.notice`: light info banner

**Rows**
- `.rows` > `.row` (`.done` greys it out): a list row containing `.time` (`b` time, `small` AM/PM; `.hot` = emerald), `.main-col` (with `.name`, `.line` (icon + text) and `.what` (green job title)), `.meta-strip` and `.end` (chips over buttons)
- `.hero`: the "Next up" card with `.top`, `.kicker`, `.body`, `.title`, `.who`, `.line` and `.link-sm`

**Chips, pills, avatars**
- `.chip`: neutral by default. Variants: `.user`, `.muted`, `.green`, `.amber`, `.red`, `.blue`, `.brand`; `.lg` makes it bigger. Wrap a group in `.chips`
- `.count-pill`: `.red`, `.amber`, `.green` or `.gray`
- `.dot`: color variants
- `.av`: initials avatar (`.sm`, `.lg`, `.sq`)
- `.ic-box`: tinted icon square (`.sm`, `.red`, `.amber`, `.green`, `.brand`)

**Buttons**
- `.btn` with `.primary` (emerald gradient), `.outline`, `.ghost` or `.danger`. Sizes: `.sm`, `.big`, `.block`
- `.icon-btn` (`.sm`): call and map style buttons. Group them in `.icon-btns`
- `.qa`: quick-action tiles (Call / Text / Directions)

**Data**
- `.tbl`: table with `th`, `.num` (right-aligned), `.grp` (group row, `small` for a note), `.sub` (second line in a cell) and `.act` (row link)
- `.kv`: key/value list (`dt`/`dd`). `.lbl-up` is an uppercase label
- `.sum-row` (`.total`): money summary lines
- `.timeline` > `.tl`: history entries with `.pin` (icon), `.t`, `.s` and `.w` (when)
- `.steps` > `.st`: a progress stepper (`.done`, `.cur`)

**Boards and calendars**
- `.kanban` > `.col`: board columns (`--kcol` = minimum column width). Columns hold `.col-h` (`b` title, `.count-pill`, `.sum`) and `.kcard` (`.t`, `.s`, `.ft`, `.amt`; `.hot` adds an amber edge)
- `.cal` (`--cols`, `--slots`, `--slot` row height): one grid covers both the week calendar and the day-by-resource view (a column per staff member / chair / room / table / bay)
  - Row 1 is the header: `.corner` plus a `.ch` for each column (`.today` highlights one). Then come `.lines`, `.vl` column rules and `.hr` hour labels
  - Each row is 30 minutes. Place an event with `<div class="ev" style="grid-column:3; grid-row:4 / span 3">`. Event colors: `.amber`, `.blue`, `.violet`, `.rose`, `.gray`, `.block` (lunch/blocked), `.done`
  - `.now` is the red current-time line
- `.legend`: color key for a calendar or floor plan. Swatches are `<i class="brand|amber|blue|violet|red|free|reserved">`

**Floor plan, listings, chat**
- `.floor` (`--cols`, `--cell`) > `.ftable`: table/room tiles. Status: `.free`, `.seated`, `.ordered`, `.check`, `.reserved`, `.dirty`; `.round` makes a round table. `.zone` labels an area such as the bar or patio
- `.lgrid` (`--n`) > `.lcard`: photo/listing cards. `.ph` is the photo (put an `<img>` in it or leave the gradient placeholder; it takes a status `.chip` and a photo `.count`), then the body: `.price`, `.t`, `.s`, `.ft`
- `.chat`: a text thread
  - `.day-sep` separates days. Bubbles are `.msg.in` (customer), `.msg.out` (staff, emerald) and `.msg.auto` (automatic text); `.msg-t` (`.l` or `.r`, `.tag`) is the timestamp line
  - `.missed`: missed-call pill
  - `.ai-card`: AI receptionist call summary with `.hd`, `.bd .k` rows and `.ft` buttons
  - `.composer`: the message box
- `.detail-cols` (2fr / 1fr), `.utabs` (underline tabs): detail page layout. The band handles the header, with `.back`, `.meta`, actions and `.band-tabs`

**Customer-facing pages** (booking page, customer hub, pay link)
- `body.cx t-<industry>`: the business's own page in its industry palette, with no app chrome. Don't set `--accent` inline; the theme sets it
- Header: `.cx-top`, `.cx-logo`, `.cx-name`
- Body: `.cx-body`, `.cx-step`, `h2`, `.lead`
- Choices: `.cx-card` (`.sel`), `.cx-opt` (`.t`, `.s`, `.p`), `.cx-radio`, `.days`, `.slots` (`a.on`, `a.off`)
- Actions and money: `.cx-btn` (`.ghost`), `.cx-pay` (big amount), `.cx-line` (invoice lines), `.cx-chip`
- `.cx-foot`: small print at the bottom

**Helpers**
- Layout: `.dash-grid` (2fr/1fr), `.grid2`, `.stack`, `.flex`, `.grow`, `.sp` (pushes to the right)
- Text: `.trunc`, `.tnum`, `.xs`, `.sm`, `.muted`, `.t-green`, `.t-amber`, `.t-red`, `.t-brand`
- Spacing: `.mt-8`, `.mt-12`, `.mt-16`, `.mt-24`, `.mb-12`
