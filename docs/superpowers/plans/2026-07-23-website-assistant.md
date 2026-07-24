# Top Shelf Website Assistant — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a bottom-right scripted chat concierge to topshelfsolutions.io — backed by the 83-service portfolio vault — that answers visitor questions and captures leads into the Top Shelf CRM + email.

**Architecture:** Pure client-side retrieval widget (no LLM) injected site-wide via the shared `assets/site.js` + `assets/site.css`, loading a committed `assets/services-vault.json`. Captured leads POST to a small public endpoint on the `top-shelf` Laravel app that creates a CRM Contact and emails the owner; Formspree is the no-lost-lead fallback.

**Tech Stack:** Static HTML/CSS/vanilla JS (no build step, Hostinger auto-deploy) for the website; Laravel 12 + PHPUnit for the app endpoint.

## Global Constraints

- **Two repos.** Website = `C:\Users\taylo\top-shelf-website` (static; push `main` → Hostinger `public_html`, ~15s, NO build step). App = `C:\Users\taylo\top-shelf` (Laravel on Railway). **Work each repo on a branch `feat/website-assistant`; do not push to `main` until verified** (website `main` auto-deploys live).
- **No LLM, no API key, no per-chat cost.** The chat brain is client-side keyword retrieval only.
- **No prices, ever.** Pricing questions → "every business is different; we do a quick free audit and build a custom plan" → capture.
- **Design tokens (website `assets/site.css`):** ground `#0B0906`, surface `#100C08`/`#15100B`, ink `#F4F0E8`/`#CFC7B8`/`#98907F`, gold `#C9A86A`/`#E4C98A`/`#A98A4E`, hairline `rgba(201,168,106,.16)`; serif `var(--serif)` (Cormorant Garamond), sans `var(--sans)` (Jost); radii `--r:3px`/`--r-lg:5px`; ease `var(--ease)`. The widget MUST use these variables — no new palette.
- **Site-wide, zero per-page HTML edits:** the widget injects its own markup from JS and its code/styles live in the already-global `site.js`/`site.css`. The vault is a separate fetched data file.
- **Respect `prefers-reduced-motion`** (the site already gates motion on it).
- **Owner email:** `contact@topshelfsolutions.io`. **Lead tag:** `website-chat`.
- App endpoint: public, **throttled**, **CORS-limited to `https://topshelfsolutions.io`**, creates a `Contact` in `WEBSITE_LEAD_LOCATION_ID` + emails the owner.

---

## Task 1 (website): Build the services vault data file

**Files:**
- Create: `assets/services-vault.json` (the vault, committed)
- Create: `assets/build-vault.py` (reproducible condensation script + doc)

**Interfaces:**
- Produces: `assets/services-vault.json` = `{ "sections": string[], "services": Array<{name, section, keywords: string[], blurb: string, great_for: string}> }`. Consumed by the widget engine (Task 4).

- [ ] **Step 1: Write the condensation script**

```python
# assets/build-vault.py — regenerate assets/services-vault.json from the Drive catalog.
# Run: python assets/build-vault.py
import json, re, pathlib

SRC = r"G:/My Drive/Taylor OS/Projects/Top Shelf/Portfolio/service-catalog-data.json"
OUT = pathlib.Path(__file__).with_name("services-vault.json")
STOP = set("the a an and or for of to your you with we our that so more into it is are on in".split())

def kw(*parts):
    words = re.findall(r"[a-z0-9]+", " ".join(p for p in parts if p).lower())
    seen, out = set(), []
    for w in words:
        if len(w) > 2 and w not in STOP and w not in seen:
            seen.add(w); out.append(w)
    return out[:14]

data = json.load(open(SRC, encoding="utf-8"))
services = []
for s in data:
    blurb = " ".join(x for x in [s.get("what_it_is",""), s.get("how_ts_solves",""), s.get("what_it_means","")] if x).strip()
    services.append({
        "name": s["name"],
        "section": s["section"],
        "keywords": kw(s["name"], s["section"], s.get("great_for",""), s.get("what_it_is","")),
        "blurb": blurb,
        "great_for": s.get("great_for",""),
    })
sections = sorted({s["section"] for s in services})
OUT.write_text(json.dumps({"sections": sections, "services": services}, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"wrote {OUT} — {len(services)} services, {len(sections)} sections")
```

- [ ] **Step 2: Generate the vault**

Run: `cd "C:/Users/taylo/top-shelf-website" && python assets/build-vault.py`
Expected: `wrote .../services-vault.json — 83 services, 12 sections`

- [ ] **Step 3: Validate the output**

Run: `python -c "import json;d=json.load(open('assets/services-vault.json',encoding='utf-8'));assert len(d['services'])==83;assert all(x['name'] and x['keywords'] and x['blurb'] for x in d['services']);print('ok',len(d['sections']),'sections')"`
Expected: `ok 12 sections`

- [ ] **Step 4: Commit**

```bash
git add assets/services-vault.json assets/build-vault.py
git commit -m "feat(assistant): services vault data (83 services) + build script"
```

---

## Task 2 (app): Public lead-intake endpoint

**Repo:** `C:\Users\taylo\top-shelf` (branch `feat/website-assistant`).

**Files:**
- Create: `config/website_lead.php`, `app/Http/Controllers/PublicWebsiteLeadController.php`, `app/Mail/WebsiteLeadMail.php`, `resources/views/emails/website-lead.blade.php`
- Modify: `routes/web.php` (add the public route), `config/cors.php` (allow the site origin + expose the path)
- Test: `tests/Feature/WebsiteLeadTest.php`

**Interfaces:**
- Produces: `POST /api/website-lead` accepting JSON `{ name, business?, email?, phone?, need?, page? }` (at least one of email/phone required) → creates a `Contact` in `config('website_lead.location_id')` tagged `website-chat` + queues `WebsiteLeadMail` to `config('website_lead.notify_email')`; returns `{ "ok": true }` (422 on validation failure). Consumed by the website submit (Task 5).

- [ ] **Step 1: Add config**

```php
<?php // config/website_lead.php
return [
    'location_id' => env('WEBSITE_LEAD_LOCATION_ID'),      // null => controller falls back to first location
    'notify_email' => env('WEBSITE_LEAD_NOTIFY_EMAIL', 'contact@topshelfsolutions.io'),
];
```

- [ ] **Step 2: Write the failing feature test**

```php
<?php // tests/Feature/WebsiteLeadTest.php
namespace Tests\Feature;

use App\Models\Contact;
use App\Models\Location;
use App\Mail\WebsiteLeadMail;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Mail;
use Tests\TestCase;

class WebsiteLeadTest extends TestCase
{
    use RefreshDatabase;

    public function test_valid_lead_creates_contact_and_emails_owner(): void
    {
        Mail::fake();
        $location = Location::factory()->create();
        config(['website_lead.location_id' => $location->id, 'website_lead.notify_email' => 'contact@topshelfsolutions.io']);

        $res = $this->postJson('/api/website-lead', [
            'name' => 'Jane Owner', 'business' => 'Jane Plumbing', 'email' => 'jane@example.com',
            'phone' => '(940) 555-1212', 'need' => 'want more calls', 'page' => 'https://topshelfsolutions.io/solution-marketing.html',
        ]);

        $res->assertOk()->assertJson(['ok' => true]);
        $this->assertDatabaseHas('contacts', ['location_id' => $location->id, 'email' => 'jane@example.com']);
        $contact = Contact::withoutGlobalScopes()->where('email', 'jane@example.com')->first();
        $this->assertTrue($contact->tags()->where('name', 'website-chat')->exists());
        Mail::assertQueued(WebsiteLeadMail::class);
    }

    public function test_lead_without_any_contact_method_is_rejected(): void
    {
        $location = Location::factory()->create();
        config(['website_lead.location_id' => $location->id]);
        $this->postJson('/api/website-lead', ['name' => 'No Contact'])->assertStatus(422);
    }
}
```

- [ ] **Step 3: Run it (fails — route/controller missing)**

Run: `php artisan test --filter=WebsiteLeadTest`
Expected: FAIL (404/500 — route not defined).

- [ ] **Step 4: Add the route** (in `routes/web.php`, in the public section near the other public routes)

```php
use App\Http\Controllers\PublicWebsiteLeadController;
Route::post('api/website-lead', [PublicWebsiteLeadController::class, 'store'])
    ->middleware('throttle:10,1')->name('website.lead');
```

- [ ] **Step 5: Write the controller**

```php
<?php // app/Http/Controllers/PublicWebsiteLeadController.php
namespace App\Http\Controllers;

use App\Mail\WebsiteLeadMail;
use App\Models\Contact;
use App\Models\Location;
use App\Models\Tag;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Mail;

class PublicWebsiteLeadController extends Controller
{
    public function store(Request $request): JsonResponse
    {
        $data = $request->validate([
            'name' => ['required', 'string', 'max:120'],
            'business' => ['nullable', 'string', 'max:160'],
            'email' => ['nullable', 'email', 'max:160'],
            'phone' => ['nullable', 'string', 'max:40'],
            'need' => ['nullable', 'string', 'max:1000'],
            'page' => ['nullable', 'string', 'max:300'],
        ]);
        if (empty($data['email']) && empty($data['phone'])) {
            return response()->json(['ok' => false, 'error' => 'contact_required'], 422);
        }

        $locationId = config('website_lead.location_id') ?: optional(Location::withoutGlobalScopes()->orderBy('id')->first())->id;
        abort_if(! $locationId, 500, 'No location configured');

        $parts = preg_split('/\s+/', trim($data['name']), 2);
        $contact = Contact::withoutGlobalScopes()->create([
            'location_id' => $locationId,
            'first_name' => $parts[0] ?? $data['name'],
            'last_name' => $parts[1] ?? '',
            'email' => $data['email'] ?? null,
            'phone' => $data['phone'] ?? null,
            'company_name' => $data['business'] ?? null,
        ]);
        $tag = Tag::withoutGlobalScopes()->firstOrCreate(['location_id' => $locationId, 'name' => 'website-chat']);
        $contact->tags()->syncWithoutDetaching([$tag->id]);

        Mail::to(config('website_lead.notify_email'))->queue(new WebsiteLeadMail($data));

        return response()->json(['ok' => true]);
    }
}
```

> Verify against the real models: confirm `Contact` fillable includes `first_name/last_name/email/phone/company_name/location_id` and `tags()` is a many-to-many with a `location_id`+`name` `Tag` (mirror the funnel-submit path in `PublicFunnelController`). Adjust field/tag calls to the real API if they differ; keep the behavior (contact in the location, tagged `website-chat`).

- [ ] **Step 6: Write the Mailable + view**

```php
<?php // app/Mail/WebsiteLeadMail.php
namespace App\Mail;

use Illuminate\Bus\Queueable;
use Illuminate\Mail\Mailable;
use Illuminate\Mail\Mailables\Content;
use Illuminate\Mail\Mailables\Envelope;
use Illuminate\Queue\SerializesModels;

class WebsiteLeadMail extends Mailable
{
    use Queueable, SerializesModels;

    /** @param array<string,mixed> $lead */
    public function __construct(public array $lead) {}

    public function envelope(): Envelope
    {
        return new Envelope(subject: 'New website lead: '.($this->lead['name'] ?? 'Unknown'));
    }

    public function content(): Content
    {
        return new Content(view: 'emails.website-lead', with: ['lead' => $this->lead]);
    }
}
```

```blade
{{-- resources/views/emails/website-lead.blade.php --}}
<h2>New website lead</h2>
<ul>
    <li><strong>Name:</strong> {{ $lead['name'] ?? '' }}</li>
    <li><strong>Business:</strong> {{ $lead['business'] ?? '—' }}</li>
    <li><strong>Email:</strong> {{ $lead['email'] ?? '—' }}</li>
    <li><strong>Phone:</strong> {{ $lead['phone'] ?? '—' }}</li>
    <li><strong>Need:</strong> {{ $lead['need'] ?? '—' }}</li>
    <li><strong>Page:</strong> {{ $lead['page'] ?? '—' }}</li>
</ul>
```

- [ ] **Step 7: Allow CORS for the site origin** — in `config/cors.php`, ensure `paths` includes `api/*` (or add `'api/website-lead'`) and `allowed_origins` includes `https://topshelfsolutions.io` (and `https://www.topshelfsolutions.io`). If the file uses `['*']` already, leave paths and just confirm the origin is allowed.

- [ ] **Step 8: Run the test (passes)**

Run: `php artisan test --filter=WebsiteLeadTest`
Expected: PASS (2 tests). If `Location`/`Contact` factories need fields, supply them.

- [ ] **Step 9: Commit**

```bash
git add config/website_lead.php app/Http/Controllers/PublicWebsiteLeadController.php app/Mail/WebsiteLeadMail.php resources/views/emails/website-lead.blade.php routes/web.php config/cors.php tests/Feature/WebsiteLeadTest.php
git commit -m "feat(website-lead): public intake endpoint -> CRM contact + owner email"
```

---

## Task 3 (website): Widget shell — FAB, panel, open/close, greeting

**Files:**
- Modify: `assets/site.css` (append the widget styles), `assets/site.js` (append a widget IIFE that injects markup + wires open/close/greeting)

**Interfaces:**
- Produces: a global `window.__tsChat` object with `open()` / `close()` and DOM ids `tsChatFab`, `tsChatPanel`. The engine (Task 4) attaches to the same panel. Any element with `[data-open-chat]` opens it.

- [ ] **Step 1: Append widget styles to `assets/site.css`**

```css
/* ===== Website assistant (concierge) ===== */
.tsc-fab{position:fixed;right:clamp(1rem,3vw,2rem);bottom:clamp(1rem,3vw,2rem);z-index:200;
  width:60px;height:60px;border-radius:50%;display:grid;place-items:center;cursor:pointer;
  background:var(--gold);color:#1a1408;border:1px solid var(--gold-bright);
  box-shadow:0 10px 30px rgba(0,0,0,.45),0 0 0 6px var(--gold-glow);transition:transform .2s var(--ease)}
.tsc-fab:hover{transform:translateY(-2px) scale(1.03)}
.tsc-panel{position:fixed;right:clamp(1rem,3vw,2rem);bottom:calc(clamp(1rem,3vw,2rem) + 74px);z-index:201;
  width:min(380px,calc(100vw - 2rem));height:min(560px,calc(100vh - 130px));display:none;flex-direction:column;
  background:var(--surface);border:1px solid var(--hairline);border-radius:var(--r-lg);overflow:hidden;
  box-shadow:0 24px 60px rgba(0,0,0,.55);font-family:var(--sans)}
.tsc-panel.open{display:flex}
.tsc-head{display:flex;align-items:center;gap:.7rem;padding:1rem 1.1rem;background:var(--surface-2);border-bottom:1px solid var(--hairline)}
.tsc-head .tsc-av{width:34px;height:34px;border-radius:50%;display:grid;place-items:center;background:var(--gold);color:#1a1408}
.tsc-head b{font-family:var(--serif);color:var(--ink);font-weight:600;font-size:1.02rem;display:block;line-height:1.1}
.tsc-head span{color:var(--ink-3);font-size:.74rem}
.tsc-head button{margin-left:auto;background:none;border:none;color:var(--ink-3);cursor:pointer;font-size:1.3rem;line-height:1}
.tsc-body{flex:1;overflow-y:auto;padding:1rem;display:flex;flex-direction:column;gap:.6rem}
.tsc-msg{max-width:85%;padding:.6rem .8rem;border-radius:var(--r-lg);font-size:.9rem;line-height:1.5}
.tsc-msg--bot{background:var(--surface-2);color:var(--ink-2);border:1px solid var(--hairline-soft);align-self:flex-start}
.tsc-msg--user{background:var(--gold);color:#1a1408;align-self:flex-end}
.tsc-msg a{color:var(--gold-bright)}
.tsc-msg--user a{color:#1a1408;text-decoration:underline}
.tsc-typing span{display:inline-block;width:6px;height:6px;margin:0 1px;border-radius:50%;background:var(--ink-3);animation:tsc-blink 1.2s infinite}
.tsc-typing span:nth-child(2){animation-delay:.2s}.tsc-typing span:nth-child(3){animation-delay:.4s}
@keyframes tsc-blink{0%,60%,100%{opacity:.25}30%{opacity:1}}
.tsc-quick{display:flex;flex-wrap:wrap;gap:.4rem;padding:0 1rem .6rem}
.tsc-quick button{background:transparent;border:1px solid var(--hairline-strong);color:var(--ink-2);
  border-radius:99px;padding:.35rem .7rem;font-size:.76rem;cursor:pointer;font-family:var(--sans)}
.tsc-quick button:hover{border-color:var(--gold);color:var(--gold-bright)}
.tsc-foot{display:flex;gap:.5rem;padding:.8rem;border-top:1px solid var(--hairline);background:var(--surface-2)}
.tsc-foot input{flex:1;background:var(--ground);border:1px solid var(--hairline);border-radius:var(--r);
  color:var(--ink);padding:.6rem .7rem;font-family:var(--sans);font-size:.9rem}
.tsc-foot button{background:var(--gold);color:#1a1408;border:none;border-radius:var(--r);padding:0 .9rem;cursor:pointer;font-weight:500}
@media (prefers-reduced-motion: reduce){.tsc-fab,.tsc-typing span{transition:none;animation:none}}
```

- [ ] **Step 2: Append the widget-shell IIFE to `assets/site.js`** (at end of file)

```javascript
/* ===== Website assistant (concierge) — shell (markup + open/close) ===== */
(function () {
  if (document.getElementById('tsChatFab')) return;
  var fab = document.createElement('button');
  fab.className = 'tsc-fab'; fab.id = 'tsChatFab'; fab.setAttribute('aria-label', 'Chat with Top Shelf');
  fab.innerHTML = '<svg viewBox="0 0 24 24" width="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-8.5 8.5 8.5 8.5 0 0 1-3.8-.9L3 21l1.9-5.7A8.5 8.5 0 1 1 21 11.5z"/></svg>';
  var panel = document.createElement('section');
  panel.className = 'tsc-panel'; panel.id = 'tsChatPanel'; panel.setAttribute('aria-label', 'Top Shelf assistant');
  panel.innerHTML =
    '<div class="tsc-head"><div class="tsc-av"><svg viewBox="0 0 24 24" width="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2 3 7l9 5 9-5-9-5zM3 12l9 5 9-5M3 17l9 5 9-5"/></svg></div>'
    + '<div><b>Top Shelf Concierge</b><span>Typically replies instantly</span></div>'
    + '<button type="button" aria-label="Close">×</button></div>'
    + '<div class="tsc-body"></div>'
    + '<div class="tsc-quick"></div>'
    + '<form class="tsc-foot"><input type="text" placeholder="Ask about our services…" aria-label="Message" autocomplete="off"><button type="submit">Send</button></form>';
  document.body.appendChild(fab); document.body.appendChild(panel);

  var greeted = false;
  var api = {
    open: function () {
      panel.classList.add('open'); fab.style.display = 'none';
      if (!greeted && window.__tsChatGreet) { greeted = true; window.__tsChatGreet(); }
      setTimeout(function () { var i = panel.querySelector('.tsc-foot input'); if (i) i.focus(); }, 250);
    },
    close: function () { panel.classList.remove('open'); fab.style.display = 'grid'; }
  };
  fab.addEventListener('click', api.open);
  panel.querySelector('.tsc-head button').addEventListener('click', api.close);
  document.querySelectorAll('[data-open-chat]').forEach(function (el) {
    el.addEventListener('click', function (e) { e.preventDefault(); api.open(); });
  });
  window.__tsChat = api;
})();
```

- [ ] **Step 3: Verify in the browser preview**

Start the site with the preview tool (serve `C:/Users/taylo/top-shelf-website` over http) and open `index.html`. Confirm: a gold circular button sits bottom-right; clicking it opens an espresso panel with the header + input; the × closes it; layout is clean on a narrow (mobile) viewport. (Greeting appears once Task 4 defines `__tsChatGreet` — not yet.)

- [ ] **Step 4: Commit**

```bash
git add assets/site.css assets/site.js
git commit -m "feat(assistant): concierge widget shell (FAB + panel, espresso/gold)"
```

---

## Task 4 (website): Retrieval engine over the vault + intents + quick chips

**Files:**
- Modify: `assets/site.js` (append the engine IIFE)

**Interfaces:**
- Consumes: the panel from Task 3 (`#tsChatPanel`), `assets/services-vault.json` (Task 1). Defines `window.__tsChatGreet` and message helpers. Produces `window.__tsChatRespond(text)` used by Task 5's capture flow.

- [ ] **Step 1: Append the engine IIFE to `assets/site.js`**

```javascript
/* ===== Website assistant — retrieval engine ===== */
(function () {
  var panel = document.getElementById('tsChatPanel');
  if (!panel) return;
  var body = panel.querySelector('.tsc-body');
  var quick = panel.querySelector('.tsc-quick');
  var form = panel.querySelector('.tsc-foot');
  var input = form.querySelector('input');

  var VAULT = { services: [], sections: [] };
  fetch('assets/services-vault.json').then(function (r) { return r.json(); })
    .then(function (d) { VAULT = d; }).catch(function () {});

  var STOP = ' the a an and or for of to your you with we our is are on in do does can '; 
  function score(text, keywords) {
    var t = ' ' + text.toLowerCase() + ' ', s = 0;
    keywords.forEach(function (k) { if (t.indexOf(k) !== -1) s += k.length; });
    return s;
  }

  // Site-level intents (checked before the vault)
  var INTENTS = [
    { k: ['hello','hi','hey','help','start'], a: function () { return "Hi! I'm the Top Shelf concierge. I can walk you through what we do — websites, marketing, CRM, AI phone answering, payments and a lot more — and help you get a free audit. What kind of business do you run?"; } },
    { k: ['price','pricing','cost','how much','quote','rate','fee','afford','budget'], a: function () { return "Every business is different, so we don’t do one-size-fits-all pricing — we run a quick <strong>free audit</strong> of your business and build you a custom plan that fits. Want me to set that up? I’ll just grab your details."; } },
    { k: ['who are you','what is top shelf','about','why you','why top shelf','trust'], a: function () { return "Top Shelf Business Solutions is your all-in-one growth partner — we handle the tech and marketing that get you more customers, so you can run your business. We tailor everything to your trade and you keep what we build for you."; } },
    { k: ['how does it work','how it works','process','get started','start','next step'], a: function () { return "Simple: we do a free audit of where you’re losing customers, show you exactly what we’d fix, and build a custom plan — no guesswork. Want me to get you on the list for an audit?"; } },
    { k: ['contact','talk','human','call','phone','reach','speak','email'], a: function () { return "Happy to connect you with a real person. Drop your info and we’ll reach out fast — what’s your name?"; } },
    { k: ['services','what do you offer','what do you do','offerings','list','everything'], a: function () { return "We cover a lot — grouped into: " + (VAULT.sections.join(', ') || 'web presence, marketing, CRM, phone & communications, payments, and more') + ". Which area is on your mind? Or tell me your biggest headache and I’ll point you to the fix."; } },
  ];

  function findAnswer(text) {
    var best = null, bs = 0;
    INTENTS.forEach(function (it) { var s = score(text, it.k); if (s > bs) { bs = s; best = { a: it.a(), cta: /audit|reach out|on the list|your name|your details/i.test(it.a()) }; } });
    VAULT.services.forEach(function (sv) {
      var s = score(text, sv.keywords) + score(text, [sv.name.toLowerCase()]) * 1.5;
      if (s > bs) { bs = s; best = { a: '<strong>' + sv.name + '.</strong> ' + sv.blurb + (sv.great_for ? ' <em>Great for ' + sv.great_for + '.</em>' : '') + ' Want a free audit to see what this looks like for your business?', cta: true }; }
    });
    if (!best) return { a: "Great question — the fastest way to a solid answer is a quick free audit tailored to your business. Want me to grab your info so a Top Shelf specialist can follow up?", cta: true };
    return best;
  }

  function el(html, cls) { var d = document.createElement('div'); d.className = cls; d.innerHTML = html; body.appendChild(d); body.scrollTop = body.scrollHeight; return d; }
  function botTyping() { return el('<div class="tsc-typing"><span></span><span></span><span></span></div>', 'tsc-msg tsc-msg--bot'); }
  function botReply(html, delay) { var t = botTyping(); setTimeout(function () { t.innerHTML = html; body.scrollTop = body.scrollHeight; }, delay || 650); }
  function userMsg(text) { el(escapeHtml(text), 'tsc-msg tsc-msg--user'); }
  function escapeHtml(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  window.__tsChatBotReply = botReply; window.__tsChatUserMsg = userMsg; window.__tsChatEscape = escapeHtml;

  window.__tsChatGreet = function () {
    botReply("Hi! I’m the <strong>Top Shelf concierge</strong>. Ask me anything about how we help businesses grow — or tell me your trade and I’ll point you to the right fix. 👋", 400);
    setQuick(['What do you offer?', 'Help me get more customers', 'Book a free audit']);
  };

  function setQuick(items) {
    quick.innerHTML = '';
    items.forEach(function (label) {
      var b = document.createElement('button'); b.type = 'button'; b.textContent = label;
      b.addEventListener('click', function () { handle(label); });
      quick.appendChild(b);
    });
  }
  window.__tsChatSetQuick = setQuick;

  // Base responder — Task 5 wraps this to add lead capture.
  window.__tsChatRespond = function (text) {
    var res = findAnswer(text);
    botReply(res.a, 700);
    return res; // { a, cta }
  };

  function handle(text) {
    if (!text || !text.trim()) return;
    userMsg(text);
    (window.__tsChatHandle || window.__tsChatRespond)(text);
  }
  window.__tsChatHandleInput = handle;

  form.addEventListener('submit', function (e) { e.preventDefault(); var v = input.value; input.value = ''; handle(v); });
})();
```

- [ ] **Step 2: Verify in the browser preview**

Reload `index.html`, open the widget. Confirm: greeting + 3 quick chips appear. Type "I need more customers" → a marketing/SEO-type service blurb. Type "how much does it cost" → the no-price/audit line. Type "what do you offer" → the sections list. Type gibberish → the fallback-to-audit line. Each ends by inviting the audit.

- [ ] **Step 3: Commit**

```bash
git add assets/site.js
git commit -m "feat(assistant): vault retrieval engine + site intents + quick chips"
```

---

## Task 5 (website): Lead capture flow + submit (CRM endpoint + Formspree fallback)

**Files:**
- Modify: `assets/site.js` (append the capture IIFE; wraps `__tsChatRespond`)

**Interfaces:**
- Consumes: `window.__tsChatRespond`, `__tsChatBotReply`, `__tsChatSetQuick`, `__tsChatEscape` (Task 4). Sets `window.__tsChatHandle` (the capture-aware responder the input/chips call).

- [ ] **Step 1: Append the capture IIFE to `assets/site.js`**

```javascript
/* ===== Website assistant — lead capture + submit ===== */
(function () {
  if (!window.__tsChatRespond) return;
  var LEAD_ENDPOINT = 'https://app-or-domain-of-top-shelf/api/website-lead'; // set to the app's public URL
  var FORMSPREE = 'https://formspree.io/f/FORMSPREE_ID'; // fallback (same id as the contact form)
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  var PHONE_RE = /(\d[\s\-().]*){10,}/;

  var lead = { active: false, step: 0, name: '', business: '', contact: '', need: '' };

  function ask(q, delay) { window.__tsChatBotReply(q, delay || 450); }

  function start(need) {
    lead = { active: true, step: 1, name: '', business: '', contact: '', need: need || '' };
    window.__tsChatSetQuick([]);
    ask("Love it — let’s get you a free audit. First, what’s your name?");
  }
  window.__tsChatStartCapture = start;

  function submit() {
    var payload = { name: lead.name, business: lead.business, need: lead.need, page: location.href };
    if (EMAIL_RE.test(lead.contact)) payload.email = lead.contact; else payload.phone = lead.contact;
    var done = function () {
      ask("You’re all set, " + window.__tsChatEscape(lead.name.split(' ')[0]) + "! ✅ A Top Shelf specialist will reach out shortly about your free audit. Prefer email? <a href='mailto:contact@topshelfsolutions.io'>contact@topshelfsolutions.io</a>.", 500);
      lead.active = false;
    };
    fetch(LEAD_ENDPOINT, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
      .then(function (r) { if (!r.ok) throw new Error('bad'); return r.json(); })
      .then(done)
      .catch(function () {
        // Fallback so a lead is never lost.
        fetch(FORMSPREE, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
          .then(done).catch(done);
      });
  }

  function step(text) {
    if (lead.step === 1) { lead.name = text.trim(); lead.step = 2; ask("Thanks, " + window.__tsChatEscape(lead.name.split(' ')[0]) + "! What’s your business or trade?"); return; }
    if (lead.step === 2) { lead.business = text.trim(); lead.step = 3; ask("Got it. What’s the best email or phone to reach you?"); return; }
    if (lead.step === 3) {
      if (!EMAIL_RE.test(text) && !PHONE_RE.test(text)) { ask("Hmm, that doesn’t look like an email or a full phone number — mind sending one so we can reach you?"); return; }
      lead.contact = text.trim(); lead.step = 4;
      ask("Perfect. Anything specific you’re hoping to fix or grow? (Optional — you can say ‘not sure’.)"); return;
    }
    if (lead.step === 4) { if (!lead.need) lead.need = text.trim(); lead.step = 0; submit(); return; }
  }

  var wantsCapture = /(call me|reach out|contact me|leave|my (name|number|info)|get (an )?audit|book|sign me up|yes|get started|interested)/i;

  window.__tsChatHandle = function (text) {
    if (lead.active) { step(text); return; }
    var res = window.__tsChatRespond(text); // renders the answer
    if (res && (res.cta || wantsCapture.test(text))) { setTimeout(function () { if (!lead.active) start(text); }, 1500); }
  };
})();
```

- [ ] **Step 2: Set the real endpoint URL** — replace `https://app-or-domain-of-top-shelf` with the Top Shelf app's real public base URL (the Railway domain or `app.` host) and `FORMSPREE_ID` with the real Formspree id (same one used by `contact.html`). If the app URL isn't known yet, leave the Formspree fallback working and note it as a follow-up.

- [ ] **Step 3: Verify in the browser preview**

Reload, open the widget, click "Book a free audit" (or type "I'm interested"). Confirm the capture flow: name → business → email/phone (rejects a bad value) → optional need → a success message. In the browser devtools Network tab, confirm a `POST` fires to the endpoint (it may 404/CORS-fail locally — the Formspree fallback then fires; both are acceptable locally, the point is the flow completes and a request is attempted).

- [ ] **Step 4: Commit**

```bash
git add assets/site.js
git commit -m "feat(assistant): guided lead capture + submit to CRM endpoint (Formspree fallback)"
```

---

## Task 6 (both): Keep docs private, end-to-end verify, deploy

**Files:**
- Modify: website `.htaccess` (deny `/docs`)

- [ ] **Step 1: Deny the docs folder on the live site** — append to website `.htaccess`:

```apache
# Keep internal planning docs out of the public site
RedirectMatch 404 ^/docs/
```

- [ ] **Step 2: Full end-to-end check (browser preview)** — with the app endpoint deployed (or a local `php artisan serve` of the app), run the whole path against the live-style config: open the widget on `index.html`, ask 3 varied service questions (expect correct blurbs), ask a price question (expect the audit line), complete a capture, and confirm the lead lands (Contact created in the app + owner email queued, or the Formspree fallback delivered). Screenshot the open widget + a captured-lead confirmation.

- [ ] **Step 3: App suite green** — in `top-shelf`: `php artisan test --filter=WebsiteLeadTest` (and a quick `php artisan test` smoke) pass; Pint clean on the new files.

- [ ] **Step 4: Deploy** — merge each repo's `feat/website-assistant` to `main` and push:
  - App (`top-shelf`) first (so the endpoint exists): `git checkout main && git merge --no-ff feat/website-assistant && git push` → Railway deploys; set `WEBSITE_LEAD_LOCATION_ID` + confirm CORS live.
  - Website (`top-shelf-website`): `git checkout main && git merge --no-ff feat/website-assistant && git push` → Hostinger auto-deploys (~15s). Verify the widget on the live topshelfsolutions.io and that `/docs` returns 404.

- [ ] **Step 5: Update HANDOFF + memory** — website repo `HANDOFF.md`: what shipped, the vault file + how to regenerate it, the app endpoint + config to set, the Formspree id follow-up.

---

## Self-Review (author)

- **Spec coverage:** vault (Task 1), CRM+email intake (Task 2), site-wide FAB/panel espresso+gold (Task 3), vault retrieval + no-price/audit guardrails + intents (Task 4), guided capture + CRM-endpoint submit + Formspree fallback (Task 5), docs-deny + e2e + deploy (Task 6). All spec sections map to a task.
- **Placeholder scan:** two intentional real-value placeholders remain and are called out as explicit steps to fill with the owner's real values — the app endpoint base URL and the Formspree id (Task 5 Steps 2). Not logic placeholders. No "TODO/handle edge cases" left.
- **Type/name consistency:** widget globals (`__tsChat`, `__tsChatGreet`, `__tsChatRespond`, `__tsChatBotReply`, `__tsChatSetQuick`, `__tsChatEscape`, `__tsChatHandle`, `__tsChatStartCapture`) are defined and consumed consistently across Tasks 3–5; DOM ids `tsChatFab`/`tsChatPanel` and CSS classes `tsc-*` match between CSS (Task 3) and JS (Tasks 3–5); the endpoint contract `{name,business,email|phone,need,page} → {ok:true}` matches between the controller (Task 2) and the submit (Task 5).
- **Implementer verifies (flagged inline):** the app's real `Contact`/`Tag` create API + own-location id (Task 2 Step 5 note); the app's CORS config shape (Task 2 Step 7); the real app base URL + Formspree id (Task 5 Step 2).
