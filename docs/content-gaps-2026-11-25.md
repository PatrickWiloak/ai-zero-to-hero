# Content gaps: verified review, 2026-11-25

**Last reviewed:** 2026-11-25

**Scope:** the six guide pillars, the certification guides and the one waiting draft on ai.noblerworks.com.
Papers and explainers stay in [GAPS.md](GAPS.md), which remains their queue; this doc only points at it.
The earlier review is [CONTENT-GAPS.md](CONTENT-GAPS.md) (2026-11-07; its waves 2 to 4 are built).

**Method:** a Gemini (Antigravity CLI) audit, pasted by Patrick, was treated as leads only. Every figure
below was re-measured on 2026-11-25 with `git ls-files`, `git grep`, a word count over `notes/*.md`,
`python3 scripts/build_flashcards.py --report` and `papers.json`. Every exam fact was read from the
vendor's own exam page that day (URLs given in each item). A topic is called a gap only when the grep
found no page for it; where pages cover part of it, the item names them and says what is left.

## Gemini claims checked

18 claims: 11 confirmed, 5 overstated, 2 false. Gemini also missed the largest problem found (Wave 1).

| # | Claim | Verdict | Measured figure |
|---|---|---|---|
| 1 | `papers.json` has 1 paper from 2026 and 18 from 2025 (34 in 2023, 30 in 2024) | confirmed | 2026: 1 (156 Mamba-3), 2025: 18, 2024: 30, 2023: 34; 156 papers |
| 2 | GAPS.md high-priority papers unbuilt: SWE-agent, Toy Models, Alignment Faking, Constitutional Classifiers, Ring Attention, Medusa/EAGLE, Greshake, Kimi k1.5/K2, LLaDA | confirmed | none has a `papers/**/summary.md`; each appears only in passing in other summaries or explainers, or in GAPS.md/TODO.md (Greshake and LLaDA: GAPS.md and TODO.md only) |
| 3 | No Grok, Phi or Kimi family explainers | confirmed | `explainers/model-families/` has claude, deepseek, gemini, gpt, llama, mistral, qwen only |
| 4 | No "AI for code" explainer | **false** | `learn/concepts/ai-coding-agents-explained.md`, `tools/comparisons/coding-assistants.md`, `work/use-cases/coding-assistants-in-practice.md` |
| 5 | No jailbreaks explainer | overstated | prompt injection has two pages (`safety/security/prompt-injection-explained.md`, `prompt-injection-defense.md`); "jailbreak" has 27 hits in 13 files (red teaming, OWASP, paper 127 GCG) but no page of its own |
| 6 | No hallucination explainer | **false** | `learn/concepts/hallucinations.md` (11 sections) plus paper 149 |
| 7 | No AI and jobs page | confirmed | 0 hits for "labor market", "displace", "job loss", "unemploy" in the pillars and explainers |
| 8 | No AI energy page | overstated | `explainers/compute/cost-of-training.md` has a section "Energy and the data centre build-out" (IEA, 415 TWh in 2024) |
| 9 | `build-a-coding-agent-loop.md` and `evaluate-an-agent-end-to-end.md` not run live | confirmed | "Tested on 2026-10-21 ... scripted stand-in" (lines 254 and 241) |
| 10 | `certifications/gcp/genai/` code samples not run | confirmed | 141 `python` blocks in 3 notes pages, and unlike AI-103 the pages do not say they were not run |
| 11 | Draft `drafts/safety/governance/ai-copyright-training-data-and-licenses.md` unpublished | confirmed | in `drafts/`, not built (commit `4ffcc6c`); verdict at the end |
| 12 | 4 active certs without `flashcards.csv` (NCP-ADS, NCP-GENL, Databricks ML Pro, prompt-engineering specialist) plus retired AI-102, DP-100 | confirmed | `--report` lists exactly these 6; note the prompt-engineering one is a study track, not an exam |
| 13 | 12 certs have under 5,000 words of notes | confirmed | 12 of 34 (NCA-AIIO 2,706 to MLS-C01 4,630; 2 of them retired). Word count is not the gap; wrong blueprints are (Wave 1) |
| 14 | 7 fact sheets stamped 2026-05-03 / 05-08 | confirmed | AIF-C01, MLS-C01, AIP-C01 (05-08), Azure GenAI, Databricks ML Pro, NCA-AIIO, NCP-AII; already TODO line "2026-12-15 Re-verify the 7 fact-sheets" |
| 15 | No labs-by-cert mapping (the other 3 sites have one) | confirmed | cloud, data and security each have `resources/hands-on-projects/labs-by-cert.md` + `.github/scripts/build-lab-map.py`; this repo has neither |
| 16 | Pending certs: AWS AI Business Strategist, NVIDIA NCA-ADS and NCP-ARI, AWS MLA-C02 | overstated | all four are real, but NCA-ADS and NCP-ARI are **already live** (not pending); AIB-C01 and MLA-C02 are in beta with no GA date |
| 17 | No troubleshooting playbooks (RAG retrieval, eval regressions, agent loops, GPU OOM / vLLM latency) | overstated | RAG: symptom table in `build/patterns/advanced-rag-patterns.md` and "When RAG fails" in `learn/concepts/rag-explained.md`. Agent loops: "Failure modes and controls" in `build/patterns/agent-architectures.md`. Real gaps: GPU OOM / latency and diagnosing an eval regression |
| 18 | No AI incident case studies (Air Canada, Chevrolet/DPD, Samsung) | overstated | Air Canada is cited on 3 work pages, Samsung on `work/enablement/acceptable-use-policy.md`; Chevrolet and DPD have 0 hits; no case-study page exists |

## Waves, ranked

### Wave 1 - NVIDIA and Databricks guides teach the wrong blueprint (fix first)

Seven NVIDIA guides and the Databricks ML Professional guide list exam domains that do not exist on the
vendor's exam page. The NVIDIA ones all use a templated "5 domains x 20%" (or similar) outline; the three
NVIDIA guides rewritten on 2026-11-07 (NCP-AIN, NCP-OUSD, NCA-GENM) are the only ones that match. A
reader studying these guides studies the wrong exam. This is worse than any missing page. Each line is
one queue item: re-map `README.md` and `fact-sheet.md` (and the notes headings) to the vendor blueprint
and logistics, cite the URL with the date, then re-map any practice-question bank. Copy the shape of
`certifications/nvidia/ai-networking-professional/README.md` ("## Exam Blueprint").

| Cert | Guide says (README / fact sheet) | Vendor page says (read 2026-11-25) |
|---|---|---|
| NCA-AIIO `certifications/nvidia/ai-infrastructure-operations-associate/` | 5 domains (GPU Fundamentals 25%, Container 25%, Kubernetes 20%, Infrastructure Mgmt 15%, Troubleshooting 15%); 50-60 q; $135 (README lines 9-11, 17-45) | 3 areas: AI Infrastructure 40%, Essential AI Knowledge 38%, AI Operations 22%; 1 hour, 50 q, $125. https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate/ |
| NCP-AII `certifications/nvidia/ai-infrastructure-professional/` | 5 x 20% (DGX, Cluster Design, Kubernetes, Scheduling, Tuning); 60-70 q; $200 | Cluster Test and Verification 33%, System and Server Bring-Up 31%, Control Plane 19%, Troubleshooting 12%, Physical Layer 5%; 2 h, 70-75 q, $400. https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-professional/ |
| NCP-AIO `certifications/nvidia/ai-operations-professional/` | 5 x 20% (MLOps, Serving, DCGM, Fleet, Incident); 60-70 q; $200 | Install and Deploy 31%, Administration 23%, Workload Management 23%, Troubleshooting and Optimization 23%; 30 multiple-choice + 3 hands-on labs, 120 min, $500. https://www.nvidia.com/en-us/learn/certification/ai-operations-professional/ |
| NCP-AAI `certifications/nvidia/agentic-ai-professional/` | 5 x 20% | 10 areas, from Agent Architecture and Design 15% to Human-AI Interaction 5%; registration "Coming soon". https://www.nvidia.com/en-us/learn/certification/agentic-ai-professional/ |
| NCP-GENL `certifications/nvidia/genai-llms-professional/` | 5 x 20% | 10 areas, from Model Optimization 17% to Safety 5%; registration "Coming soon". https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-professional/ |
| NCA-GENL `certifications/nvidia/genai-llms-associate/` | 6 domains (LLM Fundamentals 25%, Prompt Eng 20%, RAG 20%, Fine-Tuning 15%, Deployment 10%, Ethics 10%) | Core ML and AI Knowledge 30%, Software Development 24%, Experimentation 22%, Data Analysis 14%, Trustworthy AI 10%. https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/ |
| NCP-ADS `certifications/nvidia/accelerated-data-science-professional/` | 5 domains (RAPIDS 15%, cuDF 25%, cuML 25%, cuGraph 15%, Spark ETL 20%) | Data analysis 14%, Data manipulation and software literacy 19%, Data preparation 17%, GPU and cloud computing 16%, Machine learning 15%, MLOps 19%; 120 min, 60-70 q, $200. https://www.nvidia.com/en-us/learn/certification/accelerated-data-science-professional/ |
| Databricks ML Professional `certifications/databricks/ml-professional/` | 5 domains (Feature Eng 20%, MLOps 30%, Advanced ML 25%, Serving 15%, Monitoring 10%); 60 q; $300 (README lines 9-11, 19) | Model Development 44%, ML Ops 44%, Model Deployment 12%; 59 scored q, 120 min, $200. https://www.databricks.com/learn/certification/machine-learning-professional |

Covered elsewhere: none of these guides has a correct blueprint anywhere in the repo (searched each
vendor topic name, e.g. `git grep -n "Cluster Test and Verification"`, `"Essential AI Knowledge"`,
`"Model Development"`: 0 hits). The TODO line "NVIDIA ADS + GenAI LLMs Professional after the rewrite"
already expects two of these rewrites; the other six are new. The fact-sheet re-verify line (2026-12-15)
covers NCA-AIIO, NCP-AII and Databricks ML Pro dates but not their domains.

Not checked: Oracle 1Z0-1127-25 (the Oracle page timed out); the loop should fetch it before trusting
`certifications/oracle/*/README.md`.

### Wave 2 - live exams with no guide

- **NVIDIA NCA-ADS** (Associate: Accelerated Data Science): live, 60 min, 50-60 q, $125; exam guide PDF linked
  from https://www.nvidia.com/en-us/learn/certification/accelerated-data-science-associate/ (weights:
  Data Manipulation and Preparation 23%, Machine Learning with RAPIDS 16%, and others). Target
  `certifications/nvidia/accelerated-data-science-associate/` + `certs.json`. Not on any sibling site
  (`git grep NCA-ADS` in data-zero-to-hero: 0 hits).
- **NVIDIA NCP-ARI** (AI Rack and Interconnect): live, 2 h, 70 q, $400, 7 weighted areas (High-Density
  Cabling 30%, AI Infrastructure Basics 20%, and others).
  https://www.nvidia.com/en-gb/learn/certification/ai-rack-and-interconnect-professional/ . Target
  `certifications/nvidia/ai-rack-and-interconnect-professional/`.
- **AWS AIB-C01** (AI Business Strategist): beta only (beta delivery from 2026-09-29, 85 q, 170 min, $50
  beta / $100 standard, no GA date). https://aws.amazon.com/certification/certified-ai-business-strategist/ ,
  guide https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01.html . Patrick's
  call whether a beta exam gets a guide now; the existing TODO line "New-guide candidates (verify codes)"
  can now name the code.
- **AWS MLA-C02**: still beta, GA "TBD" on https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/
  (2026-11-25). Third-party sites say 2027-01-14; not on the AWS page. Already covered by the TODO line
  "2026-12-01: MLA-C02 GA date"; no new item.

### Wave 3 - cheap honesty fixes

- **GCP GenAI notes need the "not run here" note.** `certifications/gcp/genai/notes/{generative-ai-fundamentals,vertex-ai,mlops-production-genai}.md`
  carry 141 Python blocks that were migrated by script and never executed (TODO line "Run
  `certifications/gcp/genai/` code samples"). The AI-103 notes carry this note at line 10 of each page:
  "The code on this page is adapted from Microsoft's documentation and has not been run against a live
  Azure AI Foundry project here." `git grep -n "has not been run" -- certifications/gcp` finds nothing.
  Add the same admonition, worded for Google's docs.
- **Flashcard decks** for NCP-ADS, NCP-GENL and Databricks ML Pro: already TODO (2026-11-22 line). Do
  them **after** Wave 1, or the deck repeats the wrong blueprint.
- **GAPS.md explainer queue is stale**: it still queues "hallucination" and "AI for code", which exist
  (claims 4 and 6), and "copyright", which is the waiting draft. Remove the first two; mark copyright
  as drafted.

### Wave 4 - labs by cert

The sibling sites map each hands-on project to the certs it backs (`resources/hands-on-projects/labs-by-cert.md`,
generated by `.github/scripts/build-lab-map.py` from a `certs:` list per project). Here, 9 files under
`certifications/` link to `build/projects/`, but no page lists which of the 13 projects serve which of
the 34 guides. Target: a page beside the projects (or a section in `careers/certifications/ai-certifications-guide.md`)
mapping, for example, `build/projects/run-llama-on-single-gpu.md` to NCP-GENL and NCA-AIIO, and
`build/projects/build-rag-pipeline.md` to AIP-C01 and Databricks GenAI. Porting the generator needs
`.github/` and build changes, so that part is Patrick's call; a hand-kept page is loop work.

### Wave 5 - new pages the grep proves missing

- **AI incident case studies** (`safety/security/ai-incident-case-studies.md`): Air Canada and Samsung
  are one-paragraph mentions (`work/enablement/acceptable-use-policy.md` lines 19 and 134); Chevrolet
  dealer chatbot and DPD have 0 hits; `safety/security/ai-incident-response.md` cites the AI Incident
  Database but walks through no real case. Each case: what happened, the failure class, the control that
  would have stopped it, linked to the incident-response lifecycle. Primary sources only (the tribunal
  decision 2024 BCCRT 149 is already cited).
- **Debugging self-hosted inference: out of memory and latency** (`build/patterns/` or a "Troubleshooting"
  section on `build/projects/run-llama-on-single-gpu.md`): the only OOM mentions are three lines
  (`learn/concepts/inference-servers.md:111,114`, `build/projects/fine-tune-with-lora.md:282`); the
  vLLM flags are listed in Step 6 of the Llama project without a symptom-to-cause table. Cite vLLM docs.
- **Diagnosing an eval regression** (deepen `build/projects/set-up-eval-harness.md` Step 5, which only
  detects one): run-to-run variance, a changed judge, a model version change. "Nondeterministic" or
  "flaky" appears in 3 files, none of them the harness page.
- **Jailbreaks as their own page** (claim 5): only if the prompt-injection pages cannot take a
  "Jailbreaks versus prompt injection" section; prefer the section.
- **AI and jobs** and the **Grok / Phi / Kimi** families are already in GAPS.md "Queued: explainers"
  (with the GPTs-are-GPTs anchor paper queued there too). Build from that queue; do not re-queue here.

### For Patrick, not the loop

- 2026-11-25 The two agent projects (`build/projects/build-a-coding-agent-loop.md`,
  `evaluate-an-agent-end-to-end.md`) can no longer be "run against the live API" from here: since
  2026-11-21 our own validation never runs on Bedrock or the Anthropic API. Choose: keep the honest
  "scripted stand-in" label for good, or test them against a local OpenAI-compatible model (Ollama or
  vLLM) and say so on the page. The open TODO line "run ... against the live API" should change with
  that decision.

## Draft verdict: publish after listed fixes

`drafts/safety/governance/ai-copyright-training-data-and-licenses.md` (2,205 words, loop draft
2026-11-15). The topic is a real gap: copyright appears only in passing on 6 pages
(`explainers/concepts/open-vs-closed-weights.md` has the licences table it links to). The four-bucket
frame, the checklist and the internal links are sound, and every link resolves once the file moves to
`safety/governance/`. No em dashes. But it was written "from memory, not re-fetched", and four court
facts were already out of date on the day it was drafted.

Checked against sources on 2026-11-25:

| Claim in the draft | Verdict | Source |
|---|---|---|
| Copyright Office copyrightability report, January 2025; prompts alone do not make the user the author; selection, arrangement and edits can be protected | correct (Part 2, 2025-01-29) | https://www.copyright.gov/ai/ , https://www.copyright.gov/newsnet/2025/1060.html |
| Thaler v. Perlmutter (D.C. Cir. 2025): no human author, no registration | correct, but incomplete: the Supreme Court denied review on 2026-03-02 (No. 25-449) | https://www.supremecourt.gov/docket/docketfiles/html/public/25-449.html |
| Bartz and Kadrey "both went in the defendants' favour" | overstated: in Bartz, training on bought books was fair use but the pirate-library copies were not and went toward trial; settled for $1.5 billion, final approval 2026-07-20 | Bloomberg Law / Jurist reports of the final approval order (N.D. Cal. 3:24-cv-05417) |
| Thomson Reuters v. Ross: "appeals ... were pending" | **out of date**: the Third Circuit affirmed on 2026-09-29, the first appellate ruling on AI training and fair use (non-generative tool, headnotes) | https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/third-circuit-finds-ai-training-use-of-westlaw-headnotes-is-not-fair-use-thomson-reuters-enterprise-centre-gmbh-v-ross-intelligence-inc |
| Getty v. Stability AI (UK High Court 2025): the model is not an infringing copy | correct (2025-11-04), but incomplete: Getty dropped its training claims before judgment, and the Court of Appeal heard the appeal in 2026 (judgment not yet given) | https://www.judiciary.uk/ (CA-2026-000007 skeletons); CMS case tracker |
| EU: DSM Directive Art. 4 opt-out; AI Act Art. 53(1)(c) copyright policy and (d) training summary | correct | https://artificialintelligenceact.eu/article/53/ |
| (missing) | **omission**: GEMA v. OpenAI, Munich Regional Court I, 2025-11-11 (42 O 14139/24): memorised lyrics in the model are a reproduction and the TDM exception does not cover them. It is the opposite answer to Getty on the same question, so the "differs by place" point needs it | https://merlin.obs.coe.int/article/10428 |
| (missing) | omission: Copyright Office Part 3 (training), pre-publication 2025-05-09, the US agency's view on bucket 1 | https://www.copyright.gov/ai/ |

Fixes before publishing (all in the draft file, then `git mv` per `drafts/README.md`):

1. Replace "Appeals and further cases were pending" for Ross with the 2026-09-29 Third Circuit affirmance and its narrow scope.
2. Rewrite the Bartz sentence: fair use for training on bought books, not for the pirate-library copies, $1.5 billion settlement approved 2026-07-20.
3. Add GEMA v. OpenAI to the EU bullet, and the pending Getty appeal to the UK bullet (and that Getty dropped the training claim).
4. Add the 2026-03-02 cert denial to Thaler, and Allen v. Perlmutter as the open "how much human input" case.
5. Add the Copyright Office Part 3 report to bucket 1.
6. Sources: give every case a URL and a "read YYYY-MM-DD" date, and delete "Checked from memory ... not re-fetched".
7. Set `**Last reviewed:**` to the day it is published.

Publishing stays Patrick's call (TODO line "2026-11-15 Pat: review 1 loop-drafted guide page(s)").
