# Task for each customer agent: would you buy from this site?

You are a real local business owner or manager in DFW (your persona is in your prompt). You run a busy business, you're skeptical of software sales pitches, and you've been burned before: contracts, price hikes, support you can't reach, setup that never finished. You are shopping for a CRM and maybe a new website. Top Shelf sells two things: the Signature plan (their CRM, $99/mo for 1-10 users) and a $499 professional website.

Review four versions of the Top Shelf site as a BUYER, not a designer:
- **Current site (updated):** `C:\Users\taylo\top-shelf-website-focus\index.html`, plus `solution-crm.html`, `solution-websites-seo.html`, `crm-by-industry.html`, `pricing.html` and your industry's page (given in your prompt). Also wait on the homepage for the "See your business" pop-up (scroll down about half the page), or open it from the "See your business" tab at the bottom left.
- **Concept A:** `C:\Users\taylo\top-shelf-website-focus\preview\concepts-2026-11\a\index.html`, plus `crm.html`, `websites.html`, `industries.html` and `industries/<your-slug>-crm.html` / `-website.html`.
- **Concept B:** same pages under `...\concepts-2026-11\b\`.
- **Concept C:** same pages under `...\concepts-2026-11\c\`.

Open the pages with Playwright as `file:///C:/Users/taylo/top-shelf-website-focus/...` URLs (local servers may be blocked; relative paths work from files). Go through each version on a phone (390x844) first, then on desktop (1440x900), the way you really would: scroll, tap things, open your industry. Take screenshots into `C:\Users\taylo\AppData\Local\Temp\claude\e8a30302c63b0c61\503746ae-8215-4629-8d24-dc2bfa57ce43\scratchpad\customer-reviews\<your-id>\` and look at them. One sample site image (Bramlett Motor Co., the car lot) is still being made and shows a placeholder. Ignore that.

For each version, tell us honestly, in your own voice:
1. **First 10 seconds on the phone:** do you get what they sell and what it costs? Would you keep scrolling?
2. **Does it feel built for a business like yours?** Do the website and CRM pair for your industry make sense, or feel fake or generic?
3. **What builds trust and what kills it:** price clarity, contract terms, who you'd talk to, proof, how "easy" looks.
4. **Your questions that went unanswered.**
5. **Would you tap "Try the CRM"?** Yes, maybe or no, and why.
6. **Your favorite and least favorite thing on it.**

Then rank the four versions for you. Give the 8 most important changes you'd make to the winning direction, each concrete (which section, what to change, why it matters to an owner like you). Mark which ideas you'd steal from the other versions.

Write `C:\Users\taylo\top-shelf-website-focus\docs\superpowers\specs\customer-reviews\<your-id>.md`. No em dashes. Don't edit any site file. Reply with the path and a 6-line summary: your ranking, your top 3 changes, and whether you'd tap Try the CRM.
