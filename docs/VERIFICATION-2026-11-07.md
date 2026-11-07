# Fact verification pass, 2026-11-07

**In one line:** A claim-by-claim check of the guide pages written on 2026-11-07 against primary sources: which claims held, which were wrong and were fixed, and which could not be verified.
**Last reviewed:** 2026-11-07

---

Method: for each page the checkable claims (statutes and dates, product behaviour, defaults, limits, names, API signatures, versions) were compared with the fetched primary page, or, for code, re-run locally (scikit-learn 1.9.1, pandas 3.1.1 in `~/.cache/sk-venv`). Counts are of claims examined, not of sentences. Pages with no checkable external claims are listed as judgment pages.

## Per-page counts

| Page | Verified | Fixed | Unverifiable |
|---|---|---|---|
| safety/governance/us-state-ai-laws.md | 5 | 2 | 3 |
| safety/governance/bias-and-fairness-testing.md | 3 | 2 | 0 |
| safety/governance/privacy-and-data-protection-with-ai.md | 5 | 0 | 2 |
| safety/security/ai-incident-response.md | 4 | 0 | 0 |
| safety/security/deepfakes-and-synthetic-media.md | 5 | 0 | 3 |
| work/use-cases/healthcare-ai.md | 5 | 0 | 1 |
| work/use-cases/education-ai.md | 3 | 0 | 0 |
| work/playbooks/for-hr.md | 2 | 0 | 1 |
| work/playbooks/for-legal.md | 1 | 1 | 0 |
| work/playbooks/for-finance.md | 2 | 0 | 0 |
| work/playbooks/for-product-and-design.md | judgment page, no external claims | 0 | 0 |
| tools/comparisons/speech-asr-tts-providers.md | 14 | 1 | 1 |
| tools/comparisons/embedding-models.md | 10 | 2 | 0 |
| tools/comparisons/image-and-video-generation.md | 8 | 1 | 1 |
| tools/comparisons/no-code-ai-automation.md | 4 | 0 | 1 |
| build/patterns/guardrails-architecture.md | 4 | 0 | 0 |
| build/patterns/multi-agent-orchestration.md | 8 | 0 | 0 |
| build/projects/tabular-ml-end-to-end.md | 12 | 0 | 1 |
| learn/concepts/decision-trees-and-gradient-boosting.md | 8 | 0 | 1 |
| learn/concepts/feature-engineering-and-data-prep.md | 4 | 0 | 0 |
| learn/concepts/time-series-forecasting.md | 3 | 0 | 2 |
| learn/day-one/maths-for-ml-without-fear.md | 6 | 0 | 1 |
| learn/concepts/convolutional-networks-and-computer-vision.md | 5 | 0 | 0 |
| learn/concepts/reinforcement-learning-basics.md | 6 | 0 | 0 |
| careers/interviews/ai-product-manager-interview.md, applied-ai-take-home-exercises.md | judgment, labelled | 0 | 0 |
| careers/roles/ai-product-manager.md, ai-researcher-path.md, build-an-ai-portfolio.md, data-scientist-in-the-llm-era.md, ml-engineer-roadmap.md | judgment, labelled, no statistics | 0 | 0 |
| certifications/anthropic/claude-certified-developer-foundations (Key terms, 10 notes) | 20 | 3 | 1 |
| certifications/databricks/genai-engineer-associate (Key terms, 3 notes) | 11 | 5 | 1 |

## Fixes

| Page | Old | New | Source |
|---|---|---|---|
| us-state-ai-laws.md | Colorado SB24-205 duties begin February 1, 2026, with deployer duties, impact assessments and an affirmative defence | SB24-205 was repealed and reenacted as SB26-189 (Automated Decision-Making Technology), signed May 14, 2026; developer documentation duties start January 1, 2027; old duty list marked as no longer current | https://leg.colorado.gov/bills/sb26-189 |
| us-state-ai-laws.md | California: SB 53 status unknown (page 403) | SB 53 signed September 29, 2025, effective January 1, 2026; SB 243 signed October 2025, main provisions January 1, 2026 (secondary sources, flagged) | https://epic.org/california-tech-legislation-roundup-numerous-privacy-and-ai-laws-enacted-and-six-vetoed/ |
| bias-and-fairness-testing.md | Colorado's AI act requires reasonable care against algorithmic discrimination | Colorado replaced the 2024 act with SB26-189 in May 2026 | https://leg.colorado.gov/bills/sb26-189 |
| bias-and-fairness-testing.md | Four-fifths rule regulation "could not be fetched" | Quoted 29 CFR 1607.4(D) | https://www.ecfr.gov/current/title-29/part-1607/section-1607.4 |
| for-legal.md | ABA guidance page could not be fetched | ABA Formal Opinion 512, July 29, 2024, applies existing Model Rules, not binding | https://www.americanbar.org/news/abanews/aba-news-archives/2024/07/aba-issues-first-ethics-guidance-ai-tools/ |
| speech-asr-tts-providers.md | Deepgram Flux "English and 10 languages" | `flux-general-en` (English) and `flux-general-multi` (10 languages including English) | https://developers.deepgram.com/docs/models-languages-overview |
| embedding-models.md | Cohere context "not stated" | 128k tokens for v5 and v4, 512 for v3 | https://docs.cohere.com/docs/cohere-embed |
| embedding-models.md | Voyage "4-series models are mutually compatible" (incl. code) | Compatibility stated for voyage-4, -large, -lite, -nano; voyage-code-4 not stated | https://docs.voyageai.com/docs/embeddings |
| image-and-video-generation.md | "Two names on the Google video page were already shut down" | The three Veo 3.1 preview model names are retired | https://aistudio.google.com/docs/video |
| CCDV-F note 01 | stop_reason list ends "or refusal" | adds model_context_window_exceeded | https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons |
| CCDV-F note 03 | Forced tool choice is "the cleanest way" to extract structured data | any/tool return a 400 on Opus 5.5, Sonnet 5.5, Fable 5.1, Mythos 5.1; use auto with strict tool use or structured outputs | https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools |
| CCDV-F note 06 (term and line 53) | retry-after sent on 429 and 529 | honored when present; a spend-cap 429 has none; 529 not documented as sending it | https://platform.claude.com/docs/en/api/errors |
| Databricks note 04 | Knowledge Assistant and Multiagent Supervisor presented as current | FAQ lists both as legacy (Genie Agents for new low-code agents) | https://docs.databricks.com/aws/en/agents/concepts/faq |
| Databricks note 05 | Vector Search endpoint | docs now say AI Search endpoint, formerly Vector Search endpoint | https://docs.databricks.com/aws/en/vector-search/vector-search |
| Databricks note 05 | Delta Sync "embeddings computed for you"; Direct Access "write the vectors" | computed by Databricks or self-managed; Direct Access index is not synced and updated through the REST API | https://docs.databricks.com/aws/en/vector-search/vector-search |
| Databricks note 05 | Managed MCP exposes Databricks SQL and Genie | managed servers listed: Genie One, Databricks SQL, GitHub, Slack | https://docs.databricks.com/aws/en/generative-ai/mcp/ |
| Databricks note 06 | "Agent Monitoring" as the docs' name | docs term is production monitoring | https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/ |

## Still unverifiable

- California SB 53 and SB 243 statute text and the 2026 status of automated decision rules (leginfo returned HTTP 403); the two items rest on secondary summaries.
- Colorado SB26-189 exact operative dates, notice-and-cure terms (legislature summary only); NCSL claim that Colorado S 288 (intimate depictions) was enacted; TAKE IT DOWN Act terms (congress.gov HTTP 403); NYC Local Law 144 (not on the pages).
- HIPAA obligations (hhs.gov HTTP 403, page already declines to summarise); EDPB and ICO guidance (pages unreachable); whether the FTC extended its impersonation rule to individuals (search found no final action; a September 2026 ANPRM exists on platform liability).
- Midjourney facts (page blocked, none claimed); Stability AI licensing; n8n software licence terms; Make's modules and agents; Zapier user counts.
- Time-series and library defaults beyond the scikit-learn docs sections cited: `TimeSeriesSplit` described, not run. The pages state Python 3.14 for their runs; the re-run here used Python 3.12 and reproduced every number.
- Genie space definition (Databricks note 04) was not fetched; "Python 3.14" run environment claims.
- Body text of the CCDV-F note 03 still shows forced tool choice in a worked example (line 149) and in the exam-topic list; the example is valid on models that allow it, but it needs the same model caveat if reworked.
