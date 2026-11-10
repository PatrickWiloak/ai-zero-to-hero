# TODO

Working task list for **ai-zero-to-hero**. Read this at the start of a work session and keep it current as work completes - check items off with a date, add follow-ups as they surface. Stale TODOs are worse than none. Security debt (if any) is tracked separately in `SECURITY-DEBT.md`.

---

## Refactor audit (2026-10-01) - found, not started

Read-only fleet audit (9 agents, nothing changed). Each line: effort S (<half day) / M (1-3 days) / L, and the risk of making the fix. 🔴 = a live bug or safety hole.

- [x] 🟡 Delete the AI-session leftovers `FINAL_SUMMARY.md` + `ORGANIZATION_SUMMARY.md` from the public root. S, low. ✅ 2026-10-01 73ad0db
- [ ] 🟡 `scripts/check-ci-local.mjs` is a 321-line fork of the 975-line fleet gate - restamp, or mark it an intentional MkDocs variant; `scripts/site_hooks.py` drift with zero-to-hero (see its TODO). S, low.

## Audit findings (2026-10-02)

- [x] 2026-10-02 🟡 medium - Bio said "18x multi-cloud certified" (`.github/site/home.md:161`): number removed. Live on the next push to main (Pages workflow).
- [x] 2026-10-02 🟢 low - README Nobler banner hotlinked from `Noblerworks/IRONSIGHT`: vendored to `assets/brand/nobler-works-banner.jpg`.
- [ ] 🟢 low - No site analytics and no plan for it (`mkdocs.yml` extra): reuse the zero-to-hero GA4-behind-consent + Cloudflare beacon plan once Patrick unblocks it there, so one set of steps covers both. The 2026-10-30 judge relies on GitHub referrers only until then.

## AI Zero to Hero (2026-10-21)

- [x] 2026-11-07 Cross-site learning paths (7 routes, `learn/start-here/learning-paths.md`, byte-identical in all four repos, linked from which-site, learn hub and home). Not pushed or deployed: ships with the train.
- [ ] 2026-12-07 re-verify every link in `learn/start-here/learning-paths.md` against each repo's `git ls-files` (script: loop the URLs through the four trees) and the matching certs against current exam codes.
- [x] 2026-10-21 Six guide pillars shipped (98 pages: learn, work, build, tools, safety, careers); site renamed "AI Zero to Hero". Plan: `~/.cache/ai-z2h/PLAN.md`.
- [x] 2026-10-21 Repo renamed `ai-zero-to-hero`; site on `ai.noblerworks.com` (Route 53 CNAME, NW) + robots.txt; no redirects from older names.
- [x] ✅ 2026-10-31 sitemap submitted via API (read, 712 URLs, 0 errors; Request indexing skipped, UI only); 2026-11-01 Patrick (moved from 10-28): Search Console `sc-domain:noblerworks.com` (add if missing) -> submit `https://ai.noblerworks.com/sitemap.xml`, Request indexing on `/`. Replaces the old URL-prefix steps below.
- [x] 2026-10-27 (custom preview set) Patrick: upload `assets/brand/social-preview-1280x640.png` at GitHub Settings > General > Social preview (no API). Card is the shared Zero to Hero template (`assets/brand/social-preview.html`, 2026-10-21).
- [ ] 2026-12-01 verify ChatGPT Business prices in `work/enablement/choosing-enterprise-ai-tools.md`: openai.com 403s curl and a headless browser (11-06). M365 Copilot prices, Cursor and Promptfoo deals verified at primary sources 11-06.
- [ ] 2026-11-08: run the untested code in `build/projects/{chatbot-in-an-afternoon,structured-extraction-pipeline,voice-agent,prompt-injection-red-team}.md`.
- [ ] run `build/projects/{build-a-coding-agent-loop,evaluate-an-agent-end-to-end}.md` against the live API (tested with a scripted stand-in model only) and replace the illustrative output.
- [x] 2026-10-21 Refreshed the gen-AI table, prices and SDK samples in `tools/comparisons/cloud-ai-ml-services.md` from vendor pages.
- [ ] 2026-12-01: re-check prices in `learn/concepts/ai-cost-basics.md` + `tools/comparisons/cloud-ai-ml-services.md` (Gemini 4 Argon promo ends 11-30, 3.8 Flash 12-31). Also `certifications/gcp/genai/` (states both promo and later rates).
- [ ] Run `certifications/gcp/genai/` code samples against the live API: migrated by script to google-genai, checked for syntax and SDK shape only (2026-11-06).
- [ ] Add PMLE flashcards for monitoring, Model Garden and Model Armor (`certifications/gcp/machine-learning-engineer/flashcards.csv`).
- [x] 2026-10-22 OSWorld-Verified top scores confirmed on the official leaderboard; `computer-use-agents.md` now cites them.
- [x] 2026-10-21 Ten new concept pages in `learn/concepts/` (classic ML, overfitting/metrics, LLM training, coding/computer-use agents, agent memory, speech, SLMs, recommenders, cost) and two agent projects in `build/projects/`.
- [ ] Next pillar page: AI news digest + RSS. (Paper lineage graph skipped 2026-10-21: `papers.json` has no builds-on/citation field, so it could only be hand-typed; add that field first.)
- [x] 2026-10-21 Split from cloud-data-ai-security-zero-to-hero on 2026-10-21; AI cert guides wired in as `certifications/` (index `certs.json`, generated hub + nav, flashcard pages).
- [x] 2026-11-07 Flashcard generator ported (`scripts/build_flashcards.py`, runs in `build_manifest.py`); decks added for CCDV-F (35) and Databricks GenAI Associate (20).
- [ ] 2026-11-22 Flashcards still missing (hub shows "-"): add `- **Term** - definition` Key terms to Databricks ML Professional notes (ML Associate done 2026-11-07) (verify vs docs), NVIDIA ADS + GenAI LLMs Professional after the rewrite; `python3 scripts/build_flashcards.py --report` lists them.
- [x] 2026-11-07 "Check yourself" quiz (3-4 questions, collapsed answers) added to all 38 `learn/concepts/` pages; strict build verified. When a concepts page changes, re-check its quiz still matches the text.
- [ ] 2027-04-19: re-review every guide page (180-day stale warning starts).

## Certifications (moved in from the old cloud repo TODO, 2026-10-21)

- [x] 2026-10-21 AI-901 guide built (`certifications/azure/ai-901/`, notes, plan, 20-question bank, flashcards).
- [x] 2026-10-22 AI-103 guide built (`certifications/azure/ai-103/`: 5 notes, plan, 51 flashcards, 30-question bank); AI-102 points at it.
- [ ] 2026-12-01: re-check the AI-103 study guide change log (skills as of 2026-04-16) and preview status of agentic mode, memory, workflows in `certifications/azure/ai-103/`.
- [ ] 2026-11-08: run the AI-103 note code (`certifications/azure/ai-103/notes/*.md`) against a Foundry project; samples are copied from Microsoft docs, not executed here.
- [x] 2026-10-22 AI-901 duration added (45 min, Microsoft's Fundamentals figure); question count is not published by Microsoft.
- [x] 2026-10-22 NVIDIA codes confirmed on nvidia.com: NCP-NET -> NCP-AIN, NCP-USD -> NCP-OUSD, NCA-MMGA -> NCA-GENM; names, logistics, blueprints and dirs fixed.
- [x] 2026-11-07 NCP-AIN rewritten to the 6-section blueprint (notes 01-06, bank 30, generated flashcards).
- [x] 2026-11-07 NCP-OUSD rewritten to the 8-section blueprint and NVIDIA's study guide v1.1.0 (notes 01-08 with real `usd-core` 0.26.11 output, bank 30, generated flashcards).
- [x] 2026-11-07 NCA-GENM rewritten to the 7-section blueprint (notes 01-07 with CPU PyTorch, scikit-learn and spaCy output, bank 30, generated flashcards; $125, 1 hour, 50 questions confirmed on nvidia.com).
- [ ] 2026-12-01: NCA-GENM: fetch the unread reading-list items (Prompt Engineering Guide, Molnar, FID paper, HF Evaluate, data augmentation), run a CLIP-conditioned diffusion example on a GPU, recheck the 50 versus 50-60 question count.
- [ ] 2026-12-01: NCP-OUSD gaps: fetch the Conceptual Data Mapping, ASWF asset structure and Scalable Asset Structure references, the file format plug-in page, SceneIndex plug-ins, build configuration; run `usdchecker`/`usdcat` from a full USD build.
- [ ] 2026-12-01: NCP-AIN gaps to fill from NVIDIA docs: DSX Air user guide, ibdiagnet manual, SuperNIC congestion control, OpenSM SM priority, PFC watchdog, cl-resource-query sample output (`certifications/nvidia/ai-networking-professional/README.md` lists them); recheck exam page for price and lab detail.
- [x] 2026-11-07 NCP-AIN price ($500) and lab ("Hands-on lab: Yes") confirmed on the nvidia.com exam page (https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/); README, fact sheet, flashcards, careers guide updated.
- [x] 2026-10-22 MLA-C01 guide: real logistics (130 min, 65 q) and verified MLA-C02 beta facts (ME1-C02, $75, 170 min, 85 q, GA TBD).
- [ ] 2026-12-01: MLA-C02 GA date on aws.amazon.com? Rechecked 2026-11-07: still "TBD: GA registration opens / GA delivery begins" (beta ME1-C02, $75, 170 min, 85 q; exam guide at docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/). If announced, build `aws/associate/ml-engineer-mla-c02` from that guide [H].
- [x] 2026-10-22 Anthropic: CPES confirmed not an exam (study track, invented logistics removed); CCAO-F and CCAR-P weights match the v1.0 exam guide PDFs.
- [ ] New-guide candidates (verify codes): AWS AI Business Strategist (beta), NVIDIA NCA-ADS, NCP-ARI.
- [x] 2026-10-22 Vertex AI -> Agent Platform names swept in `certifications/gcp/` (PMLE + GAL exam guides use only new names); PMLE domains set to the 2026-06-01 guide.
- [x] 2026-11-06 PMLE on the June 2026 guide: README, fact sheet, notes (new `ml-monitoring-ai-solutions`, `ml-foundation-models-and-tuning`), bank re-mapped to 6 sections, 36 questions.
- [x] 2026-10-22 Banks for CCAR-F, CCDV-F, AIP-C01, GAL, Databricks GenAI, DP-100, Copilot, PMLE expanded to 30 questions (new ones weighted by current guides).
- [x] 2026-10-22 Copilot page rebuilt to GH-300 skills 2026-08-07 (7 areas, 100 min, Pearson VUE); notes 07-09 added (`certifications/github/copilot/`).
- [x] 2026-10-22 Databricks GenAI page mapped to the 6-section guide (no official weights, objective counts instead); notes 04-06 added.
- [x] 2026-10-22 DP-100 page on the final outline (LM optimization 25-30%), retired banner; `notes/language-model-optimization.md` added.
- [x] 2026-10-22 GAL README, strategy, notes 04 and fact sheet now give the guide's 30/35/20/15 weights.
- [x] 2026-11-06 Databricks ML Associate README + fact-sheet header on the official 4 sections (48 scored, pass mark unpublished); genai README aligned with its fact sheet, old service names fixed.
- [x] 2026-11-07 Databricks ML Associate rebuilt on the 4-section outline (notes 01-04 run locally with real output, fact sheet, plan, scenarios, strategy, 30-question bank at 11/6/9/4, 76 generated flashcards). Unity Catalog feature table and serving code is marked not run.
- [ ] 2026-12-01: re-check Databricks ML Associate exam guide (its update table still says March 1, 2025 while the title says August 2026) and Hyperopt status (gone from Runtime ML after 16.4 LTS ML).
- [ ] 2027-02-01: re-check GH-300 outline (Spark retired 2026-08-31 but listed; duplicate "GitHub Copilot features" line) and Databricks guide (KA, Supervisor now legacy).
- [x] ✅ 2026-11-06 spot-check: LUIS notes moved to CLU; PaLM + AutoML banners added (Microsoft/Google pages). Rewrite below.
- [x] 2026-11-06 rewrote `certifications/gcp/genai` off PaLM/Codey onto Gemini 3.8 Flash and `google-genai`; banners removed; PaLM/Codey kept as one history note.
- [ ] Distribution: submit to awesome-llm-security.

## Open

- [x] 2026-11-10 Freshness workflow on main; dispatched run 42795046085 green: 137 pages, 7 over 120 days (all `last-updated: 2026-05-03`, 191 d), 21 undated READMEs, none near the 365-day fail.
- [ ] 2026-12-15 Re-verify the 7 fact-sheets (AIF-C01, MLS-C01, AIP-C01, Azure GenAI, Databricks ML Pro, NVIDIA x2) (2026-05-03) on vendor pages, bump `last-updated` (365-d fail: 2027-05-03); date or exempt the 21 undated READMEs. `python3 scripts/check_freshness.py --days 120`.

### 🟠 Discoverability (added 2026-08-31)

- [x] ~~Update the GitHub repo description and topics for the broader scope~~ ✅ done 2026-09-30:
      description now "Everything AI, summarized: 144 papers and landmark essays plus 31 dated
      explainers..."; topics `ai-policy`, `robotics`, `explainers` added. **Patrick:** the old
      description was "For folks who don't have time to read 220,000+ words of research 📚" - restore
      your voice with `gh repo edit --description` if you prefer it.
- [x] ~~Set GitHub topics~~ ✅ done 2026-08-31 (15 topics: llm, generative-ai, research-papers, rag, ...)
- [x] ~~Commit and push the rewritten `LICENSE` + new `NOTICE`~~ ✅ done - on `main` since
      2026-08-31 (commit "Replace the hand-written CC BY summary with the canonical legal text").

### Search (added 2026-09-30)

- [x] ~~Per-page descriptions and search titles, Open Graph/Twitter cards, JSON-LD, noindex on
      templates, IndexNow on deploy, Search Console URL-prefix property + sitemap~~ ✅ done 2026-09-30
      (ported from zero-to-hero). Baseline to judge against: GitHub referrers for this repo on 2026-09-30
      (`gh api repos/PatrickWiloak/ai-zero-to-hero/traffic/popular/referrers`):
      Google 5 referrals / 5 uniques in 14 days, no other search engine; repo views 43 / 42 uniques.
- [x] ~~IndexNow first submission~~ ✅ done 2026-09-30: the deploy step's first run was accepted
      (HTTP 202, all 189 URLs). If a later run 403s, check `<site>/<key>.txt` is served
      (key in `.github/site/indexnow-key.txt`) and rerun `python3 scripts/notify_indexnow.py --all`.
- [ ] 2026-11-21 check: GSC URL Inspection on https://ai.noblerworks.com/ (`sc-domain:noblerworks.com`) reads "Submitted and indexed"; 11-07 it was "Crawled - currently not indexed". If still not, Pat: Request indexing (UI only).
- [x] ✅ 2026-11-07 PASS (sitemap read 11-06, 712 URLs, 0 errors; 380 pages with impressions, `sc-domain:noblerworks.com`) **2026-11-01 check** (re-dated 2026-10-15 after the FAIL below; was 2026-10-14): Search Console -> Sitemaps shows `sitemap.xml` as read with ~190 URLs and
      Pages -> Indexed above zero (old URL-prefix property for the github.io URL, retired,
      owners pat@noblerworks.com and the `nobler-reporting` service account).
      ✏️ 2026-10-15 judged: 🔴 FAIL - the sitemap (submitted 2026-09-30) is still `isPending: true`, never
      downloaded, 0 errors; URL Inspection says the home page and `/INDEX/` are "URL is unknown to Google"; 0
      impressions 09-15..10-14. The sitemap itself is fine (200, `application/xml`, 189 `<loc>`). Read via the GSC
      API as `nobler-reporting` (WIF, gitgood.dev `scripts/analytics/wif-auth.ts`). Next (Pat, 2026-10-28, browser):
      URL Inspection -> Request indexing on the home page, and resubmit the sitemap; then re-check 2026-11-01.
- [ ] **2026-11-15 judge**: re-pull the referrers above; target Google + Bing referrals up versus the ✏️ 2026-11-07 re-dated 2026-11-15: Search Console/Bing referrer pull is Patrick's console step
      2026-09-30 baseline, and search queries appearing in Search Console -> Performance.
      ✏️ 2026-10-30 (todo-sweep): re-dated 2026-11-06 - `gh api` (GitHub referrers) is blocked by this
      loop's Bash permissions, and Search Console Performance needs the GSC WIF script (node), which
      this loop can't run; needs a session with `gh`/node access, or Patrick.
- [ ] **Patrick: Bing Webmaster Tools** -> Import from Google Search Console (IndexNow already pings Bing;
      Webmaster Tools shows what it did with them).
- [x] 2026-10-21 Custom domain decided: `ai.noblerworks.com`; zero-to-hero moved to `cloud.noblerworks.com` the same day.

### Content
- [x] 2026-10-16 SEO internal-link pass: home page now links 12 classic papers plus a generated "Recently added"
      list (`{{recent_papers}}` token, newest 8 by number); the new papers are in 10 explainers' "Read next", the
      ROADMAP and READING_GUIDE; six weak search titles fixed via `SEO_SHORT` in `scripts/site_hooks.py`.
      Whether it moves anything is judged by the existing 2026-10-30 / 2026-11-01 checks (indexing is the blocker, not links).
- [x] 2026-10-16 added papers 145-150 (METR time horizons, Christiano 2017, Stiennon 2020, Tulu 3,
      Why LMs Hallucinate, Stochastic Parrots) from the new gap pass. **Re-run
      `python3 scripts/measure_sources.py && python3 scripts/build_manifest.py`** (network + `pdftotext`)
      so the landing page word totals include them. Unverified details are listed in each file's
      claims; facts read from secondary sources: Stochastic Parrots controversy (Wikipedia only).
- [x] 2026-10-16 added papers 151-156 (circuit tracing, CoT faithfulness, Emergent Misalignment, s1, DAPO,
      Mamba-3). Still **re-run `scripts/measure_sources.py`** once for 145-156. 151 and 152 read only the first
      ~100k chars of long web pages.
- [ ] 🟡 Next batch from `docs/GAPS.md` "Queued: recent work": Kimi k1.5/K2, LLaDA, then the classics list
      (Greshake prompt injection, watermarking, model merging, AI 2027). More 2026 papers need a human-curated
      source - web search returned no reliable ranking.

- [ ] 🟡 Work through the (new) high-priority queue in [`docs/GAPS.md`](./docs/GAPS.md): SWE-agent,
      AlphaCode, Toy Models of Superposition, Alignment Faking, Constitutional Classifiers, Ring
      Attention, Medusa/EAGLE, HELM/BIG-Bench. Code generation is the one area still marked Thin.
- [ ] 🟡 Explainer queue in `docs/GAPS.md`: xAI Grok / Phi / Kimi families, MoE routing in practice,
      multimodal tokenization, AI for code, jailbreaks and prompt injection, AI and jobs, copyright.
- [ ] **2027-03-29: re-review every explainer** - that is when all 31 cross the 180-day line and
      `build_manifest.py` starts printing `WARN explainers not reviewed in 180 days`. Model families,
      benchmarks, compute prices and policy go stale first; bump each page's `Last reviewed` as you go.
- [ ] **2026-12-31: re-check the three fastest-moving explainers** - `explainers/model-families/gpt.md`,
      `claude.md`, `gemini.md` - and the dated scores in `explainers/benchmarks/*.md` and
      `papers/techniques/139-osworld/summary.md` ("What Happened Next"). These were current on
      2026-09-30 and will be wrong within a quarter.
- [x] ~~Spot-check the salvaged 88-107 summaries~~ ✅ done 2026-09-30 - a read-only verifier checked
      all 20 against their papers; about 60 corrections applied (one wrong cross-reference, several
      "connections" that misdescribed the cited paper, and numeric tables in Mistral 7B, Llama Guard,
      Self-Refine, KTO, Voyager, PaLM, MAE and STaR rebuilt from the papers). Unverified and left as
      is: CICERO's headline numbers (Science paywall), ESM-2's contact-precision table.
- [ ] 🟡 `docs/READING_GUIDE.md`, `docs/ROADMAP.md` and `docs/COMPARISONS.md` now reference the
      whole collection but still curate rather than enumerate. That is deliberate, but it means a
      new paper does not automatically appear in them - check whether it belongs on a learning path
      or changes a comparison when adding one.


### Tooling
- [ ] 🟡 24 of the 144 papers have no retrievable PDF, so they are excluded from the "1.8M words in"
      figure on the landing page (which is therefore a floor). New since 2026-09-30: the nine essays
      (web pages), 126-induction-heads (transformer-circuits), 140-model-collapse (Nature). Nature paywalls: `68-alphafold`,
      `61-alphageometry`, `101-alphafold3`. DOI redirects: `106-esm`, `107-cicero`. Published as web
      pages: the Anthropic, OpenAI, Meta, Google and transformer-circuits entries. `39-rlvr` now links
      to DeepSeek-R1 but is deliberately excluded via `SHARED_SOURCE` in `measure_sources.py`, since
      that PDF is already counted under `26-deepseek-r1`. If any gain an open PDF, re-run
      `scripts/measure_sources.py`.

---

## Done

- [x] ~~**Broaden to "Everything AI"** (2026-09-30): site renamed "Everything AI, Summarized" (repo name
      and Pages URL deliberately unchanged - a rename breaks the Pages URL with no redirect). New
      `explainers/` content type (31 pages, 8 sections, generated `EXPLAINERS.md` hub, `Last reviewed`
      dates enforced by `check_counts.py`, 180-day staleness warning in the build). New paper
      categories `robotics` and `essays`. Papers 108-144 added (9 essays, 3 robotics, 3D, audio
      generation, safety/interpretability, long context, data, optimisers, evaluation). GAPS queue
      closed and rewritten; glossary 117 -> 144 terms; ROADMAP Path 6 (no-maths Big Picture);
      COMPARISONS and READING_GUIDE updated. All explainers and essays fact-checked against primary
      sources by a separate verification pass before publishing~~ ✅ done 2026-09-30
- [x] ~~Fix gitGood promo copy: trial is 7 days (was "10 days free") and price $8/$64 (was $5/$40),
      here and in the zero-to-hero sibling~~ ✅ done 2026-09-30
- [x] ~~Fix four factual errors found while fact-checking: 26-deepseek-r1 distilled-model table
      (wrong scores and base models throughout), 54-rope (Llama 3 does not use YaRN), 43-claude4
      (May not June 2025), 47-gemini3 (November not December 2025)~~ ✅ done 2026-09-30
- [x] ~~Documentation sweep: `BROWSE.md` completed to all 107 cards (was 54) and reorganised by
      category with corrected per-category and badge tallies; `docs/QUICK_REFERENCE.md` rebuilt with
      a row per paper (was 24); `docs/READING_GUIDE.md` rewritten for the current collection (was 15
      papers); `docs/COMPARISONS.md` gained reasoning, diffusion-sampling, control, tokenizer,
      serving, retrieval, agent, evaluation and beyond-language sections; `docs/ROADMAP.md` gained a
      Reasoning & Agents path and a production sprint~~ ✅ done 2026-08-20
- [x] ~~Add `scripts/check_counts.py` and wire it into CI - verifies BROWSE's per-category and badge
      tallies, the glossary term count in `GLOSSARY.md` and `README.md`, and that `docs/GAPS.md`'s
      coverage map accounts for every paper. Verified it fails on injected drift~~ ✅ done 2026-08-20
- [x] ~~Fix false counts: README footer claimed 460,000+ words (actual 219,000+ including guides),
      README and `GLOSSARY.md` claimed 250+/150+ glossary terms (actual 117), BROWSE's Quick Stats
      per-category rows were stale on four of five categories, and `docs/GAPS.md` still said 87
      papers and listed Imagen and AlphaZero as gaps after both were added~~ ✅ done 2026-08-20
- [x] ~~Give `39-rlvr` a source link (DeepSeek-R1) so the build no longer warns, and exclude it from
      the source-word measurement via `SHARED_SOURCE` so that PDF is not counted twice~~ ✅ done 2026-08-20

- [x] ~~Ship the site rebuild and the 88-107 salvage to `main` (`a559e1e`). CI and the Docs site workflow both green; verified live on the old github.io URL - amber palette, new landing page, 107 papers, and the salvaged summaries all serving 200~~ ✅ done 2026-08-19
- [x] ~~Delete `claude/expand-paper-collection-Rif7n` after confirming all 20 salvaged summaries are on `origin/main`; recovery SHA `592be71` if ever needed~~ ✅ done 2026-08-19
- [x] ~~Delete the `claude/content-gaps-ads-ylbmrr` remote branch - fully merged into `main` (zero commits ahead, zero diff); recovery SHA `aa97fa8` if ever needed~~ ✅ done 2026-08-19
- [x] ~~Set the repo homepage to the Pages URL so GitHub links the site from the repo header~~ ✅ done 2026-08-19
- [x] ~~Confirm GitHub Pages is already wired to GitHub Actions and deploying (it is, since June 2026) - no manual setup needed~~ ✅ done 2026-08-19
- [x] ~~Rebuild the docs site to match the zero-to-hero repo: hand-maintained `mkdocs.yml` with the nav generated into a git-ignored `mkdocs.generated.yml`, a site-only landing page and stylesheet under `.github/site/`, near-black palette with an amber accent, Geist fonts, `toc.integrate`, pinned toolchain, and a `--strict` build as a blocking gate on every PR~~ ✅ done 2026-08-18
- [x] ~~Salvage the 20 genuinely-new summaries from the stale `claude/expand-paper-collection-Rif7n` branch as papers 88-107, dropping its 5 duplicate papers (Word2Vec, DDPM, Mixtral, AlphaFold 2, GPT-2) and its stale README/guide rewrites~~ ✅ done 2026-08-18
- [x] ~~Generate README's By Year block from `papers.json` instead of maintaining it by hand while claiming it was generated~~ ✅ done 2026-08-18
- [x] ~~Replace README's exhaustive per-paper directory tree with a category-level tree, removing a guaranteed drift source~~ ✅ done 2026-08-18
- [x] ~~Add Nobler Works + gitGood.dev promo block to the README, matching the zero-to-hero repo~~ ✅ done 2026-08-18
- [x] ~~Gap analysis pass: 19 summaries added (69-87) covering the modern diffusion pipeline, ResNet/U-Net/GQA, training systems, instruction tuning, retrieval, evaluation, interpretability and safety~~ ✅ done 2026-08-18
- [x] ~~Publish `docs/GAPS.md` so the collection's boundaries and queue are explicit~~ ✅ done 2026-08-18
- [x] 2026-10-27 CODE_OF_CONDUCT.md + PR template added (community health was 71%).

## Content gaps (2026-11-07 review)

Plan: [docs/CONTENT-GAPS.md](docs/CONTENT-GAPS.md) (pillars + certs; papers stay in GAPS.md). Wave 1 (run untested code) and the cert items are already listed above.

- [x] 2026-11-07 Wave 2: maths-for-ML day-one page; concept pages for trees/boosting, CNNs, RL basics, forecasting, feature engineering; tabular scikit-learn project (code run in a venv, output pasted; deploy step described, not run).
- [x] 2026-11-07 Wave 3: careers - ML engineer, data scientist, AI PM, researcher roles; AI portfolio guide; AI PM interview (judgment pages, no market stats).
- [x] 2026-11-07 Wave 3 remainder: applied-AI take-home exercises interview page.
- [x] 2026-11-07 Wave 4: playbooks, use cases, comparisons, patterns. Still unverified (pages 403): HHS HIPAA, ED AI pages, ABA Op. 512 text, ICO, Midjourney, CA SB 53/243 statute. See page Sources.
- [x] 2026-11-07 Wave 4: safety - AI privacy, AI incident response, deepfakes, bias testing, US state AI laws.
- [x] 2026-11-07 Wave 4 fact pass done: see docs/VERIFICATION-2026-11-07.md (Colorado repealed and replaced by SB26-189; unverifiable list there).
- [ ] 2026-12-07 Recheck Wave 4 dated facts (docs/VERIFICATION-2026-11-07.md): Colorado SB26-189 AG rules (due 2027-01-01), California AI bills and SB 53 effective date, vendor model names in image/speech/embeddings pages.
