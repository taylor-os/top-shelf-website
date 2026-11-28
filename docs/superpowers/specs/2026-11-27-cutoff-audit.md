# Cut-off audit: concepts A–D and the updated current-site pages (2026-11-27)

This was a read-only visual QA pass. No site file was edited.

Screenshots and scripts are in
`C:\Users\taylo\AppData\Local\Temp\claude\e8a30302c63b0c61\503746ae-8215-4629-8d24-dc2bfa57ce43\scratchpad\cutoff-audit\`
(below, `SP\` means that folder):

- `SP\audit.py` holds the measurement and scroll-frame script (`measure | shots | motion`). `SP\measure.json` and `SP\measure-cur_.json` hold the raw results.
- `SP\frames\<concept>-<page>-<width>[-motion]\NN_y<scrollY>.png` are viewport-sized frames taken while scrolling.
- `SP\sheets\*.png` are contact sheets of those frames, 181 in total, and are the images I actually reviewed.
- `SP\el\*.png` are crisp element crops used as evidence for the findings.

## Headline

- **No page has document-level horizontal overflow** at 390 or 1440 px, so nothing spills past the screen edge. Text never runs off the viewport or out of its section.
- **A fixed bar never permanently hides anything.** At maximum scroll, nothing sits under D's Call/Text bar, B's concept tag, the current site's Call/Text bar or the chat button.
- The "cut off" look comes from **device mockups whose bottoms are sliced by a card or section edge, and screens covered by another screen.** Each case below has one CSS root cause that repeats across many pages.

## Findings, ranked

### 1. HIGH: Concept B homepage hero. The phone and desktop mockups are sliced flat at the bottom.
- **Page:** `b/index.html`, both widths, and worse at 1440. Motion mode (what visitors see) and reduced-motion both show it.
- **Section:** `section.hero` → `.hero-stage` → `figure.hero-phone` and `.hero-desk`.
- **What is cut:**
  - At 1440, the phone loses about 51 px of its bottom. The tab bar and bottom bezel are gone and it ends in a hard horizontal edge.
  - The desktop frame is cut and faded at the same line.
  - The phone's label chip ("Sample screens · Inbox · 2 AM call") is **completely hidden**: 46 px are clipped, so it never shows.
  - At 390, about 12 px of the phone and its chip are clipped.
- **Screenshots:**
  - `SP\frames\b-index-1440-motion\02_y900.png`, the clearest view.
  - `SP\frames\b-index-1440\01_y810.png`
  - `SP\el\b-index-1440-hero.png`
- **Cause:** `scripts/concepts/b/style.css`, three rules together:
  - line 74 `.hero{…overflow:hidden}`
  - line 109 `.hero-phone{…bottom:-8%}` hangs the phone below the hero
  - line 110 `.hero::after` adds a 150 px fade over the bottom
  - In motion mode, `site.js` also starts the phone at `y:120`, which pushes it further into the clip.

### 2. HIGH: Concepts A and D industries hub. Every card's CRM window is sliced, and the website headline is covered mid-word.
- **Pages:** `a/industries.html` and `d/industries.html`, all 12 cards, both widths.
- **Section:** `.hub-card > .hub-pair` (contains `.hub-web` and `.hub-crm`).
- **What is cut:**
  - The "Sample CRM" window runs off the bottom of the grey panel. At 1440, 47 px (21 %) is clipped and the window has no bottom edge. At 390, it sits flush against the panel's bottom edge.
  - The CRM window also covers the website mockup's headline mid-word on every card: "Good used ca…", "Financing here…", "Dealer-leve…", "Detailing wit…", "Serious cou…".
- **Screenshots:**
  - `SP\el\a-industries-1440-hubpair-carlots.png`
  - `SP\el\d-industries-390-hubpair-carlots.png`
  - `SP\sheets\a-industries-1440-s00.png`
  - `SP\frames\a-industries-390\01_y759.png`
- **Cause:**
  - In `scripts/concepts/a/style.css`:
    - line 296 `.hub-pair{…overflow:hidden; height:300px}`
    - the rule after it `.hub-crm{position:absolute; width:66%; top:92px}`
    - mobile line 364 `.hub-pair{height:220px}` and `.hub-crm{top:64px}`
  - `d/style.css` repeats the same rules at lines 294–296 and 365–366.
  - The fixed height is shorter than the website plus the offset CRM.

### 3. HIGH: Concept A homepage bento. Phone and desktop screenshots are sliced at the bottom of each card, through the content that matters.
- **Page:** `a/index.html` (`section#crm .bento`), both widths. Concept D does not use the bento.
- **What is cut:**
  - **"Get paid from their phone":** the "Pay $204.09" button is cut in half at 1440, where 111 px (24 %) of the phone is clipped. At 390 the phone ends at "Card number" and the Pay button never appears.
  - **"Estimates by text":** cut through the "Brake fluid flush" line. 111 px are clipped at 1440 and 81 px at 390.
  - **"Answer every call":** the phone is cut mid-conversation at 390 (81 px). At 1440 only the tab bar is clipped.
  - **"Book and dispatch" and "More reviews":** the desktop shots lose 19–39 px at the bottom and bleed off the right edge.
- **Screenshots:**
  - `SP\el\a-index-1440-bento.png`
  - `SP\el\a-index-390-bento.png`
  - `SP\el\a-index-1440-getpaid.png`
  - `SP\sheets\a-index-390-s00.png`
- **Cause:** `scripts/concepts/a/style.css`. The bleed is deliberate, but at these sizes it slices the screen's own key content.
  - line 127 `.bento-card{overflow:hidden}`
  - line 132 `.k-phone .bento-shot{margin:auto auto -120px}`
  - line 133 `.k-desktop .bento-shot{margin:auto -1px -40px auto}`
  - line 135 `.b0 … margin-bottom:-24px`
  - mobile line 354 `margin-bottom:-90px` and line 355 `-20px`

### 4. MEDIUM-HIGH: Current-site homepage CRM bento (`index.html`, `#cc .c-bento`). The phone screenshots are cut mid-row on mobile.
- **Width:** 390. Five tiles are affected: Answer every call, Book and dispatch, Estimates the same day, Reviews and Get paid.
- **What is cut:**
  - Each phone screenshot is clipped by 146 px (28 %) at a fixed 380 px height.
  - The cut runs through content rows: "Hannah Cole", a half-visible "JOB TOTAL $…" line, "Refrigerant recharge" and the invoice materials.
  - At 1440 the desktop shots are also clipped at the bottom; the Reviews tile, for example, ends mid-row on "Dana Whitfield". This is milder.
- **Screenshots:** `SP\el\cur-index-390-bento.png` and `SP\el\cur-index-1440-bento.png`.
- **Cause:** the inline `<style>` in `index.html`, **not** `assets/site.css`:
  - line 147 `#cc .c-shot.c-ph{height:380px;width:min(260px,70%)}`
  - line 142 `#cc .c-shot{…overflow:hidden}`
  - at 1440, line 144 `#cc .c-shot.c-d{aspect-ratio:var(--ar,16/9)}`

### 5. MEDIUM: Concept C. The right 17–18 % of every website and CRM screenshot is cropped.
- **Pages:**
  - all 24 `c/industries/*` pages, as `span.pb-img img`
  - `c/index.html` and `c/websites.html`, as `figure img` and `.site-card .frame img`
  - `c/industries.html`, as `figure.taped img`
  - both widths
- **What is cut:** 16:10 screenshots (1200×750 and 1440×900) are forced into a 4:3 box with `object-fit:cover; object-position:top left`.
  - Website shots lose the right end of the header: the nav CTA and part of the phone number.
  - CRM shots lose the right-hand column, such as "Needs attention".
  - It reads as a crop rather than a broken layout, but real UI is missing.
- **Screenshots:** `SP\el\c-hs-crm-1440-pbimg.png` and `SP\sheets\c-industries_home-services-crm-1440-s00.png`.
- **Cause:** `scripts/concepts/c/site.css` sets `aspect-ratio:4/3; object-fit:cover; object-position:top left` at:
  - line 145 `.pair-shots img`
  - line 210 `.spread img`
  - line 231 `.pb-img img`
  - line 241 `.site-card .frame img`

### 6. LOW-MEDIUM: Concepts A and D CRM page. The sticky jump nav's last chip is cut at the screen edge.
- **Pages:** `a/crm.html` and `d/crm.html` at 390.
- **What is cut:** the second chip reads "Get paid from the customer's ph…", sliced by the viewport. It is a horizontal scroller with its scrollbar hidden and no fade or "swipe" hint, so it looks cut off rather than scrollable. Concept D's industry rail got a fade mask; `.jump` did not.
- **Screenshots:** `SP\sheets\a-crm-390-s00.png` and `SP\sheets\d-crm-390-s00.png`.
- **Cause:** `scripts/concepts/a/style.css` line 253 `.jump-in{overflow-x:auto; scrollbar-width:none}` and line 254, with the same rules in `d/style.css`.

### 7. LOW: Device label tags and chips are truncated with an ellipsis.
- **Concept B:** on 13 pages (index, crm and every industry CRM page), `figcaption.chip` on phones loses up to 165 px of text at 390, for example "Sample screens · Technician · Ge…". The chip also sits over the phone's bottom tab bar. Cause: `b/style.css` line 99 `.chip{…white-space:nowrap; overflow:hidden; text-overflow:ellipsis}`.
- **Concepts A and D:** `.phone .tag` is truncated on `index` and `crm`, for example "Sample · Everline Home S…". On `crm` at 390 the "Sample · Bramlett Motor Co." tag on `figure.g-phone` also pokes 29 px out of its section. Cause: `a/style.css` and `d/style.css` line 104–105 `.phone .tag{…max-width:calc(100% - 12px); overflow:hidden; text-overflow:ellipsis}`.

### 8. LOW: Current-site page-hero photos are cropped hard on mobile.
- **Pages:** `solution-crm.html`, `solution-websites-seo.html` and `pricing.html`.
- **What is cut:** `section.page-hero .page-hero-photo img` is a 2400×1018 image under `object-fit:cover`. At 390, 78–86 % of its width is cut away; at 1440, 23–42 %.
- **Assessment:** it is a dimmed background, and the frames show no face or subject sliced, so this is noted rather than a defect.
- **Cause:** `assets/site.css` line 925 `.page-hero-photo{position:absolute; inset:0; overflow:hidden}` with its cover image.

### 9. LOW: Concept B anchor jumps without smooth scroll land headings under the sticky header and picker.
- **Where:** `b/industries.html` picker links at 390 and 1440. The skip link does the same on every B page at 390.
- **What happens:**
  - The section eyebrow lands 23–40 px under the sticky `.top` and `.picker`.
  - With motion on, Lenis's `offset:-150` hides it.
  - With reduced motion or no JS, it shows. Nothing sets `scroll-margin-top`.
- **Cause:** `b/style.css` line 256 `.picker{position:sticky; top:64px}`.

## Checked and cleared (false positives and deliberate)

- **B `section.price` overflow** (39 px at 390 and 140 px tall at 1440): it is only the decorative `.price-glow`. No content is clipped.
- **C `span.circled` wider than its parent:** this is the hand-drawn loop SVG around $99 and $499, which is meant to overflow. It renders fully.
- **Current site "See it" button overlapping the tile heading** (`button.c-plus` and `h3`): the boxes overlap, but `h3{padding-right:120px}` keeps the text clear. Not a visual collision.
- **B `span.wl` (3 px):** this is the headline's word-rise mask, and descenders are fine.
- **Current site, any page:** scrolling past 45 % opens the "See your business" pop-up (`assets/see-your-business.js`) over the whole page. It works as designed, and its card scrolls internally. On real phones its `max-height:100vh` can hide the bottom buttons behind the browser toolbar; using `dvh` would fix that. Popups were suppressed for every other measurement.
- **Mid-scroll overlays:** D's Call/Text bar, B's "Concept B · design preview" tag, and the current site's chat button plus "See your business" tab cover content only while it scrolls past. Body padding clears all of them at page end.
- **B pinned five-beat stage** at 1440×900 in motion mode: the phones and desktop fit inside the pin (`min(74vh,680px)`), and copy never overlaps between beats. Only the mid-transition frames are blurred, by design.

## Coverage: what was fully checked versus sampled

**Programmatic checks (a)–(f), fully checked:**
- Scope was all 117 pages: 4 concepts × 28 pages, plus the 5 current-site pages, each at 390×844 and 1440×900, for 234 page-loads.
- Pages ran with reduced motion, so B renders its stacked stage. On top of that I injected `animation/transition:none`, forced `.reveal` to be visible, set every image to eager and waited for it, killed ScrollTrigger and did a stepped pre-scroll.
- Check (e) looked at the page at maximum scroll.
- Check (f) compared text and button boxes against each other, excluding closed `<details>` and sticky or fixed elements.

**Visual review (scroll frames, looked at), sampled:**
- Per concept, at both widths: index, crm, websites and industries, plus 3 industry pages.
  - A: auto-repair-crm, salon-spa-website, legal-crm
  - B: restaurants-crm, medical-dental-website, car-lots-crm
  - C: home-services-crm, fitness-website, vet-crm
  - D: real-estate-crm, retail-website, auto-detailing-crm
- All 5 current-site pages at both widths.
- Concept B in real **motion mode** (GSAP, Lenis and pins live) for the same 7 pages at both widths.

**Not visually reviewed:** the other 21 industry pages per concept (84 in total).
- They were measured, not looked at.
- Each concept builds all its industry pages from one template, and their measured results match the siblings I reviewed. For example, B's chip truncation is measured on all 12 CRM pages and C's object-fit crop on all 24 pages.
- Content-specific crops on those pages would be missed, such as a screenshot whose own layout cuts badly.
