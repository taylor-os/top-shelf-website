# Handoff — Top Shelf (umbrella: business audit)

> Save-state read FIRST on resume. GitHub holds the code; this holds the thinking.
> **This is the canonical handoff for the Top Shelf BUSINESS AUDIT** (registry `vault_slug: top-shelf`, covering CRM + Website + Outreach together).
> Sub-project handoffs still exist for engineering work: `top-shelf-crm.md` (also holds a separate, still-open UI-redesign thread) and `top-shelf-website.md`.

**Last updated:** 2026-08-09 · **By:** Claude Code (desktop, Opus 5) · **Continuing on:** Taylor OS, project "Top Shelf"

---

## 🔴 READ THIS FIRST — the agent layer is DOWN, and fixing it is step zero

**Nothing else in this handoff should be worked until this is resolved.** Owner instruction, verbatim: *"I need all of the council, agents, skills, judge, manager to work correctly before any work is done."*

**Symptom:** every subagent — council seats, leads, `judge-agent` — dies in <500ms with zero tokens:
> `400 output_config.effort 'xhigh' is not supported when thinking is disabled on this model. Use effort 'high' or below, or enable thinking.`

**Cause:** subagents inherit the session's *effort* but are spawned **without thinking**. On Opus that pair is illegal.

**Measured, all four dispatch forms:**

| `model` passed | Result |
|---|---|
| *(none — inherits Opus 5)* | **400** |
| `opus` | **400** |
| `sonnet` | runs |
| `fable` | runs |

⚠️ `sonnet` and `fable` "work" **only because they switch off Opus.** They are not fixes — they silently run every seat on a model the owner did not select, and report success. This fooled me twice and I recorded both as "fixed." Do not repeat it.

### The staged fix has NEVER been loaded

`alwaysThinkingEnabled: true` is set in `~/.claude/settings.json`. **It has never run.** Proof:
- claude process started **17:56:20**
- `settings.json` written **22:09:15** — four hours into an already-running process
- `$env:CLAUDE_CODE_SESSION_ID` never changed → **no restart ever occurred**

An earlier note in the brain claimed the setting "does not win." **That was wrong.** I had only tested that it doesn't apply *mid-session* and generalised that into "doesn't work." Settings.json is read at startup only.

### STEP 1 — test inheritance (do this before anything else)
Dispatch any agent with **no `model` parameter**:
> `Agent(subagent_type: "general-purpose", prompt: "Reply with one line: OK")`

- **Runs** → thinking inherits. Go to STEP 2.
- **400s** → confirmed product limitation, not a config error. Say so plainly, use the fallback, stop hunting.

### STEP 2 — only if STEP 1 passed: unpin the Judge
`~/.claude/agents/judge-agent.md` currently carries `model: sonnet` as a deliberate crutch. If inheritance works, that pin now **violates the owner's standing rule** by forcing the Judge onto Sonnet forever. Remove the `model: sonnet` line, re-test the Judge with no model param, commit.

### FALLBACK if STEP 1 fails
Pass `model` as a tool parameter per dispatch. Keep the Judge pinned. **Do NOT re-pin the other 105 agents** — commit `72a0f3f` unpinned them deliberately.

### Already ruled out — do not re-investigate
Fast mode is OFF (`epitaxyPrefs.fastMode = False` in `%APPDATA%\Claude\claude_desktop_config.json`) · no managed/policy settings · no HKLM/HKCU registry policy · no thinking/effort env vars · no thinking key in `.claude.json`, the desktop config, or the session record · Claude Code is current (2.1.226), so not an already-fixed upstream bug. There is **no way to force a settings reload mid-session** — no CLI, no tool; the Workflow tool spawns through the same path and hits the identical 400.

### Fixed along the way (`72a0f3f`)
**All 106 agents carried a hardcoded `model:` in frontmatter — 103 `sonnet`, 3 `opus`, zero inheriting.** That included `judge-agent`, so **every Judge verdict ever rendered in the Manager pipeline used Sonnet regardless of the selected model.** Pins removed. Side effect: agents now fail *loudly* instead of silently running on the wrong model. Note frontmatter pins are **cached at session start**, so editing them mid-session does nothing.

**⚠️ Also: this file's narrative gets clobbered.** Correction commit `c7b7f4d` was overwritten within the hour by another session and an autosync WIP snapshot. Durable lessons belong in `brain/_core/` memory, not here.

---

## OWNER'S GOAL — verbatim, do not re-ask

> Point Top Shelf CRM at a city → it reviews every business → builds a CSV of who to contact → creates the deliverables → sends them → auto-responds to text/email replies → keeps him notified throughout → sends onboarding docs for signature → delivers a welcome packet → auto-creates the client in the CRM with delivery templates and automations.

And: *"I want everything straightened up and correct before sending anything. I dont want a customer to reach out and we are not ready for their business."*

**Constraints (decided — do not re-litigate):**
- **Solo, a few hours a week.** The binding constraint on every decision.
- **Automate everything**; surface legal risks rather than avoid them — *"dont not do something because it might be illegal just make sure I know about it while fixing it."*
- Offer and pricing **fully in scope and changeable**.
- **Equal scrutiny on all 7 phases**, full council depth each.
- **Standing rule:** every seat always uses the effort and model selected at the prompt. Never pin frontmatter, never override, never put effort instructions in a skill or agent.

**⚠️ HOW HE WANTS ME TO WORK** — *"this is the whole reason I am auditing. I want you to evaluate what I already have, see if it's any good, and come up with solutions on your own and give them to me so I can review them."*
**Stop asking him to spec things. Evaluate → propose → he reviews.**

---

## THE FINDING THAT REFRAMED EVERYTHING

**The machine is fully built and has never been switched on.** Verified by hand, not agent-reported:
- **275 leads** (Highland Village 235 + Lewisville 40) — `outreach_status` **blank on all 275**
- **0 of 57** recommended leads have an `owner_email` or `owner_name`
- CAN-SPAM mailing address in `topshelf-lead-outreach/config.yaml` is still `<<NEED: real physical mailing address>>`
- **Zero customers, zero prospects contacted, ever**

Three independent blockers, any one of which halts all outbound.

**Also done:** paused auto-archive on all 8 cold-prospect sample sites (`top-shelf-website` @ `0bc1c66`). Luigi's was 19 days from deletion; the 60-day timer was counting down against prospects who don't know the samples exist.

---

## PHASE 0 — Offer & ICP — COMPLETE
Doc: `top-shelf-crm/docs/audit/2026-08-09-phase0-offer-and-icp.md` (`a5827ad`)

1. **🔴 Live homepage publishes 3 past-tense case studies under a "Real Results" header** (`top-shelf-website/index.html` L452–469) from a business with **zero customers**, plus 4 unsourced hero stats (L104–118). Found independently by two council seats, then verified by hand.
2. **Root cause: no `facts/topshelf.json`.** The platter fact gate validates claims about the *prospect*, so Top Shelf's claims about *itself* pass unchecked. Same gap that shipped the false "you own the sample site" line in August.
3. **Premium $1,599 is undeliverable solo** — three seats agreed independently (~15.9 hrs/mo recurring, 26.5% net margin, worst per-hour of the three tiers).
4. **Essential $499 does not break even until month 8–9 — after its own 6-month term ends.** No setup fee + blank kill fee ⇒ a month-2 churn costs ~$1,472 with zero recourse.
5. **The pitch targets the wrong segment.** The funnel is mostly high-review/weak-site businesses (Ousley Vision 1,298 reviews; Tangerine 939) who already get customers — "your website is dated" is not their felt pain.

**OWNER DECISIONS (do not re-ask):**
- **D1 — leave the "Real Results" section live**, fix it in the dedicated website session. **HARD BLOCKER: must be fixed before the first outreach send.** Bounded risk only while nobody has been contacted.
- **D2 — defer the Premium question to Phase 5**, since its contents depend on the delivery model. **Do not sell Premium before Phase 5 concludes.**

---

## PHASE 1 — Find & Qualify — PARTIAL
Doc: `top-shelf-crm/docs/audit/2026-08-09-phase1-find-and-qualify.md` (`23eaa98`)

⚠️ The five council seats ran **on the wrong model** (Fable 5 while the owner was on Opus 5 — my error, from misreading a cached picker menu as the active model). **Every finding below was therefore re-verified by hand and stands on that, not on the seats.**

**VERIFIED AND FINAL:**
- **The composite score is decorative.** 4 of 57 clear the 65 threshold; **53 ride the website override.** HV max 66; dataset-wide max 75.
- **Scores are NOT comparable across cities.** `reachability` fires in Lewisville (max 10, mean 3.0 among 20 recommended; all-row 1.5) and is 0 in Highland Village. An earlier claim of mine that it is "structurally dead" was HV-only presented as dataset-wide — **wrong, do not repeat.** `winner_boost` **is** structurally 0 everywhere (`winners.yaml` empty).
- **`years_est` is blank on all 235 rows**, so `longevity` is a constant. Third dead input.
- **Cross-file identity is broken both ways.** *Williams & Kunkel* excluded in HV as "out-of-city Flower Mound" *with* website+phone, yet live/recommended/queued in Lewisville with neither. *Hirji CPA* permanently suppressed by its own wrong-city exclusion record. Dedup keys on name + **search** city.
- **The Approved gate does not gate.** Strittmatter deployed with empty CSV URLs; Tangerine deployed but status still Not contacted; **Dove Creek deployed with no row in any CSV and no manifest entry**; Animal Medical Center **Approved since 2026-08-04 with nothing built.** Nothing reconciles CSV ↔ manifest ↔ deployed dirs.
- **55 rows stamped `confidence: high` on *derived* GBP status** ("claim status not verified") — understates the exact gap Top Shelf sells into, then feeds the audit as fact.
- **Geographic bleed is 112 of 176 exclusions (64%)** — nearly half of everything discovered. Flower Mound alone is 42. *(An earlier draft said "~90"; the Judge caught it — I had matched only `located in X` and missed `out-of-city X`.)*
- The "187/235 unknown website_quality" figure is **not** a scanner failure — 174 are Excluded pre-scan by design. Only **13 live rows** carry an unmeasured grade.

**§2a — Manager analysis on Opus 5, NOT an independent seat, NOT Judged:**
- **The owner's real selection criterion is invisible to the model.** All six Approved leads have **≥197 reviews** (median 396); 14 of 57 recommended have <15 reviews and he approved **none**. `traction = log10(reviews+1)/2` saturates at ~100 reviews, so a 100-review business and Onyx's 694 score **identically** — the scorer flatlines exactly where his decisions begin. Fix: desaturate (`/2.5`) + a traction floor (≥15 reviews OR top-5 map rank).
- **Weak website is the right gate, wrong ranker.** All 6 approvals have weak sites — but so do all 57 recommended, so it cannot separate within the pool.
- **Vertical: HV data says dental (62% survival) and salon (60%), NOT home services (roofing 21%).** The conflict with Phase 0 is *geographic*: trades are radius operators serving HV from neighbouring towns, so they appear as out-of-city exclusions. **A bedroom suburb contains storefronts.** If home services is strategically right, discovery must run **vertical-first across the metro**, not geography-first per suburb.

**JUDGE RECORD:** an independent Judge (pinned to Sonnet) returned REVISE with 3 objections; 2 fully correct (geographic count, unstated mean population — both fixed), 1 half-right (it called the two blank-`exclusion_reason` rows a defect; they are the two *modern-site* businesses, correctly scored and correctly not recommended — documented as correct so nobody "fixes" it). It confirmed §1.4 and §2a.2 are **proportionate, not inflated**, and that the verified/unverified labelling held. **Caveat: this is Sonnet grading Opus-produced work** — reliable on arithmetic and sourcing, may miss subtle reasoning flaws.

**STILL OWED:** independently Judge §2a; re-run the ICP/Targeting and Demand seats once agents work. Brief them with §1 as fact and §2 as corrections; **do NOT re-feed the "structurally dead" error.**

**BLOCKING ISSUES B1–B6 (owner decisions needed, in the doc §5):** B1 cross-file identity must key on place_id/address+domain **(blocks any second city)** · B2 add `business_city` (never re-key; row identity for every writeback is name+city) · B3 reconciliation job CSV ↔ manifest ↔ deployed dirs · B4 cap `confidence` mechanically on derived fields · B5 builders must refuse `website_quality=unknown` and empty-`website` rows · B6 resolve Animal Medical Center and Dove Creek; decide on Strittmatter/Tangerine.

---

## VERTICAL TARGETING — owner request, evaluated, proposal pending review

**What he asked for:** point the finder at **any US city** and filter by industry — keep all verticals, or narrow to only those with a proven pack.

**This already exists and was never used:** `topshelf-lead-finder/SKILL.md` L62 — `mode: city+industry | city-only | industry-only | flexible`, plus `metro_cities`. Highland Village ran `city-only` (widest geography, no industry filter), which is exactly why it surfaced salons/dentists and discarded ~112 out-of-area trades. **Configuration + workflow change, not a build.**

**His decisions:** all four pack components in scope · **success metric = reply rate of any kind** · scope = any US city, he picks city and filters industry · **build ONE vertical pack end-to-end first.**

**PACK EVALUATION (Manager analysis, not Judged):**

| Component | State | Verdict |
|---|---|---|
| Sample-site templates | 9 distinct HTML files, 30–40KB each, own vertical maps + design rationale | **Good — real designs, not reskins** |
| Proposal | 42 tokens, **zero** industry/vertical tokens | Not vertical-aware |
| Outreach copy | `gap_phrase()` keys on `website_quality` only | Not vertical-aware |
| CRM funnel per vertical | none built | Does not exist |

**The insight:** the expensive piece (9 industry designs) is DONE; the cheap pieces (industry-specific *words*) are missing. A roofer and an orthodontist both currently receive *"your site's looking a little dated."* His success metric is **reply rate**, which is driven by outreach copy — the least tailored component. Highest-leverage fix in the system.

**PROPOSED PACK (NOT yet approved):** 1) industry gap phrasing — `gap_phrase()` becomes `(website_quality × industry)`; 2) industry pain-set tokens in the proposal; 3) template-family mapping (mostly exists); 4) curated photo pack per industry (fixes the 2026-08-05 defect — construction/cleaning stock photos on an HVAC sample); 5) CRM funnel page — **defer**, only matters for inbound, none exists.

**PROPOSED FIRST VERTICAL: home services** — deliberately against the HV numbers, because **the owner runs GDR, a real home-services business** with a live site, review funnel, CRM and real customers. That is the case study Top Shelf lacks, and it answers the Skeptic's #1 kill risk ("who else have you done this for?"). Also fits the geography finding: trades need `industry-only`/city-list, not suburb sweeps.

---

## OPEN ENGINEERING THREAD — AI Employee 401 (from a Taylor OS session, 2026-08-09)

Carried here because it is unresolved and belongs to this project. Full detail in the secondary log `top-shelf-crm.md` and in `projects/top-shelf/context.md`.

**P10 AI Employee (chat-bubble reply drafting) will not authenticate.** Taylor minted a fresh `CLAUDE_CODE_OAUTH_TOKEN` via `claude setup-token` and pasted it into Railway → top-shelf → **web** *and* **worker** Variables. Result: `401 OAuth access token is invalid`. He then redid the entire OAuth flow from scratch — **same 401**, so it is not a bad copy/paste.

**Next steps, in order (do these instead of re-minting again):**
1. `railway ssh --service web` (and `worker`) on **top-shelf**, run `claude -p "hi"` with `CLAUDE_CODE_OAUTH_TOKEN` in env — reproduce outside the app to see the real error rather than the wrapped 401.
2. Check `claude --version` in the deployed image. The Dockerfile does `npm install -g @anthropic-ai/claude-code` **unpinned**, so a stale CLI could reject a token minted by a newer `setup-token`. Consider pinning.
3. Confirm the variable actually landed and triggered a **real redeploy** on both services — Railway sometimes needs an explicit trigger, not just a Variables save.
4. If still stuck, test the fresh token locally (`CLAUDE_CODE_OAUTH_TOKEN=… claude -p "hi"`) to separate "token is bad" from "container cannot use it."

Note both services must be set: chat works from `web`, but workflow-driven AI drafting runs on `worker` — set only one and automations silently do nothing.

---

## THE 7 PHASES
0 Offer & ICP ✅ · 1 Find & Qualify 🟡 partial · 2 The approach (deliverables, outreach, send-automation decision) · 3 Convert (MSA risk, contract) · 4 Onboard · 5 Keep & deliver *(Premium decision lands here)* · 6 The autonomous loop *(must be last; do not switch on while D1 is open)* · then a switch-on scorecard.

---

## TRAPS
- **Lead CSVs are on Google Drive, NOT in any repo:** `G:\My Drive\Taylor OS\Projects\Top Shelf\Outreach\Prospects\Leads\`. A Judge false-flagged them as missing by searching the repo. **Cite absolute paths.**
- **There is no Denton.csv.** Agent scans reported a "Denton run, 503 researched" — not on disk. Treat as lost. Only HV + Lewisville exist.
- `top-shelf-crm` local clone was **22 commits behind** origin. `git fetch` before any work.
- PowerShell 5.1: `2>&1` on git makes `$?` false even on success. Do not redirect.
- **Never infer the active model from `~/.claude.json`** — it is not there. `additionalModelOptionsCache` is a cached *picker menu*. The session record at `%APPDATA%\Claude\claude-code-sessions\…\local_*.json` has the real `"model"` field; the system prompt is also authoritative.
- **Before concluding a settings change "doesn't work," check whether the process ever restarted** — compare `(Get-Process claude*).StartTime` to the file's `LastWriteTime` and whether `$env:CLAUDE_CODE_SESSION_ID` changed.

---

## NEXT 3 STEPS
1. **Fix the agent layer** (top of this file). Nothing else until council/leads/Judge/Manager all run correctly on the selected model and effort.
2. **Get owner review** of the proposed vertical pack + home-services first vertical. Then build that pack end-to-end.
3. **Close Phase 1:** independently Judge §2a, re-run the two judgement seats, present B1–B6 for decision. **B1 blocks pointing the finder at any second city — and he wants any US city.**

## FILE MAP
- Audit docs → `top-shelf-crm/docs/audit/2026-08-09-phase{0,1}-*.md`
- Lead data → `G:\My Drive\Taylor OS\Projects\Top Shelf\Outreach\Prospects\Leads\*.csv`
- Skills → `~/.claude/skills/topshelf-{lead-finder,lead-audit,sample-site,lead-outreach,seo-audit}`
- Facts files → `C:\Users\taylo\Agentic-OS\vault\platter\facts\` (19; **none for Top Shelf itself** — that is finding #2 of Phase 0)
- Demo estate → `top-shelf-website/demo/` + `demo/manifest.json`
- Durable lessons → `vault/brain/_core/subagent-400-name-the-active-model.md`

<!-- AUTO:STATE — rewritten by brain-handoff.cjs. Edit above this line, not below. -->

**Repo state** — C:\Users\taylo\top-shelf-crm

- branch: `main`
- last commit: `eaec924 2026-08-09 docs(handoff): point to the canonical business-audit handoff in the vault`
- uncommitted files: 1 — HANDOFF.md
- commits not yet pushed: 0

**Repo state** — C:\Users\taylo\top-shelf-website

- branch: `main`
- last commit: `0bc1c66 2026-08-09 chore(demo): pause auto-archive on all 8 prospect sample sites`
- uncommitted files: 1 — HANDOFF.md
- commits not yet pushed: 0

<!-- /AUTO:STATE -->
