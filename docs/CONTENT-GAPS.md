# Content gaps: guide pillars and certifications

**Last reviewed:** 2026-11-07

A gap review of the guide pillars (`learn/`, `work/`, `build/`, `tools/`, `safety/`, `careers/`) and the
certification guides on ai.noblerworks.com. Paper and explainer gaps stay in [GAPS.md](GAPS.md), which
remains the queue for those. The review listed the tree with `git ls-files` and searched it with
`git grep`. A topic is called missing only when the search found nothing (or one or two passing mentions).
The open items are tracked in `TODO.md` under "Content gaps (2026-11-07 review)".

## Where the site stands

| Pillar | Pages | Thin spot |
|---|---|---|
| learn | 33 concepts, 6 day-one, 7 start-here | No maths on-ramp; classic ML has 2 pages |
| work | 17 | No HR, legal, finance or product playbooks |
| build | 6 patterns, 12 projects | No tabular-ML or multi-agent project; 6 projects not yet run live |
| tools | 7 comparisons, 4 decisions | No image/video, speech, embedding-model or automation comparisons |
| safety | 13 | No AI privacy, AI incident response or deepfake pages |
| careers | 6 | The thinnest pillar |
| certifications | 34 guides | Several decks missing; NVIDIA rewrites pending |

The LLM half of the site is strong. The gaps are the **classic-ML foundations** a "zero" reader needs and
the **careers** pillar.

## Plan, in order

### Wave 1 - finish what is written (already in TODO)

Run the untested project code (chatbot, extraction, voice agent, red-team, coding-agent loop, agent eval),
the AI-103 notes and the GCP GenAI samples against the live APIs. A guide that fails when someone runs it
costs more than a missing guide.

### Wave 2 - foundations for the zero reader

- `learn/day-one/`: **maths for ML without fear** (vectors, matrices, probability, gradients: linear
  algebra has 2 passing mentions).
- `learn/concepts/`: **decision trees and gradient boosting** (3 mentions), **CNNs and computer vision
  basics** (3), **reinforcement learning basics** (mentioned often, never explained for beginners),
  **time-series forecasting**, **feature engineering and data prep**.
- `build/projects/`: a **tabular ML end to end** project in scikit-learn (train, evaluate, deploy), so
  the classic-ML pages have a hands-on partner.

### Wave 3 - careers (the thinnest pillar)

- Roles: ML engineer roadmap, data scientist in the LLM era, AI product manager, AI researcher (the
  learn path exists; the career page does not).
- **Building an AI portfolio** (2 passing mentions): what to build, how to show it.
- Interviews: AI product manager, and prompt / applied-AI take-home exercises.

### Wave 4 - work, tools and safety breadth

- `work/playbooks/`: HR, legal, finance, product and design.
- `work/use-cases/`: healthcare and education (2 mentions each, both regulated, so cite regulators).
- `tools/comparisons/`: image and video generation, speech (ASR/TTS) providers, embedding models,
  no-code AI automation (n8n, Zapier, Make: no hits).
- `build/patterns/`: multi-agent orchestration and guardrails as an architecture pattern.
- `safety/`: **privacy and data protection with AI**, **AI incident response** (one mention),
  **deepfakes and synthetic media** (one mention), **bias and fairness testing** in practice,
  US state AI laws (Colorado: one mention).

### Wave 5 - certifications (already in TODO)

- NVIDIA NCP-AIN rewritten to the blueprint 2026-11-07 (done); NCP-OUSD rewritten 2026-11-07 (done); NCA-GENM rewritten 2026-11-07 (done).
- Databricks ML Associate rebuilt on the 4-section outline, 2026-11-07 (done).
- Flashcard decks: generator ported 2026-11-07 (`scripts/build_flashcards.py`); CCDV-F and Databricks GenAI now have decks. Still no deck: NVIDIA ADS and GenAI LLMs Professional (waiting on the rewrite), Databricks ML Associate/Professional (add `Key terms` lines, then verify against the docs), retired AI-102 and DP-100, the prompt-engineering study track. Plus PMLE monitoring / Model Garden / Model Armor cards.
- New guides once codes are verified: AWS AI Business Strategist, NVIDIA NCA-ADS, NCP-ARI, MLA-C02 at GA.
  The AI governance certs (AIGP, AAISM) are planned for the security site with a link here.

## How to do each item

Guide pages use `templates/guide.md` with the three header lines; run `build_manifest.py`, `check_links.py`
and `check_counts.py` before committing. Prices and model names are cited to the vendor page with a date.
