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

- California SB 53 and SB 243 statute text and effective dates, and the 2026 status of automated decision rules (leginfo returns HTTP 403, also in a browser); the effective dates rest on secondary summaries.
- NCSL claim that Colorado S 288 (intimate depictions) was enacted.
- HIPAA obligations (hhs.gov HTTP 403, also in a browser; page already declines to summarise); ICO guidance (HTTP 403); Department of Education AI pages (HTTP 403); ABA Formal Opinion 512 full text (ABA news page HTTP 403 on refetch); CFPB Circular 2022-03 withdrawal (Federal Register redirects to an unblock page); whether the FTC extended its impersonation rule to individuals (search found no final action; a September 2026 ANPRM exists on platform liability).
- Midjourney facts (docs HTTP 403 in fetch and browser, none claimed); Stability AI licensing; n8n software licence terms; Make's modules and agents; Zapier user counts.
- Time-series and library defaults beyond the scikit-learn docs sections cited: `TimeSeriesSplit` described, not run. The pages state Python 3.14 for their runs; the re-run here used Python 3.12 and reproduced every number.
- Genie space definition (Databricks note 04) was not fetched; "Python 3.14" run environment claims.
- Body text of the CCDV-F note 03 still shows forced tool choice in a worked example (line 149) and in the exam-topic list; the example is valid on models that allow it, but it needs the same model caveat if reworked.

## Settled 2026-11-07 (second pass)

Public pages only, no logins. Page, old, new, source.

| Page | Old | New | Source |
|---|---|---|---|
| us-state-ai-laws.md (Colorado) | exact SB26-189 operative dates and cure terms unconfirmed | act takes effect January 1, 2027 (effective-date clause and a few sections on passage), applies to decisions on or after January 1, 2027, AG rules on or before January 1, 2027; 60-day cure after notice of violation, none for knowing or repeated violations, cure repealed January 1, 2030. The legislature summary page's "effective May 14, 2026" does not match the act text and was not used | https://leg.colorado.gov/laws/session-laws/SB26-189/131/download |
| us-state-ai-laws.md, for-hr.md (NYC) | Local Law 144 page unreachable, not checked | bias audit within one year before use, public audit information, notice 10 business days before use, enforced from July 5, 2023 | https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page |
| us-state-ai-laws.md (California SB 53) | signing date from secondary summaries | signed September 29, 2025 confirmed by the Governor's release, which gives no effective date | https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/ |
| deepfakes-and-synthetic-media.md | TAKE IT DOWN terms not described | Public Law 119-12, approved May 19, 2025; 48-hour removal after a valid request; platform process due within one year; FTC enforces | https://www.govinfo.gov/content/pkg/PLAW-119publ12/html/PLAW-119publ12.htm |
| privacy-and-data-protection-with-ai.md | EDPB page unreachable | Opinion 28/2024 adopted 18 December 2024: anonymity case by case, legitimate interest three-step test, unlawfully processed data may affect deployment; ICO still HTTP 403 | https://www.edpb.europa.eu/news/news/2024/edpb-opinion-ai-models-gdpr-principles-support-responsible-ai_en |
| for-finance.md | CFPB page returned 404, not cited | Circular 2022-03 (May 26, 2022) cited with its quoted conclusion; withdrawal on May 12, 2025 reported only by secondary sources, flagged | https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/ |
| image-and-video-generation.md | model names due for recheck | refetched: OpenAI `gpt-image-2.5-sunburst`, `-flare`, `gpt-image-2.6-sunburst`, `-flare`; Google Nano Banana 2.1, 2 Lite, 2, Pro and legacy, 14 reference images, SynthID statement; Stability lists Stable Diffusion 3.5, Stable Image, Stable Audio; no page change needed | https://developers.openai.com/api/docs/guides/image-generation , https://aistudio.google.com/docs/image-generation , https://docs.stability.ai/ |
| bias-and-fairness-testing.md | 29 CFR 1607.4(D) quote | already checked in the first pass; eCFR redirected to an unblock page on refetch, so not rechecked | https://www.ecfr.gov/current/title-29/part-1607/section-1607.4 |

## Cert guides pass

Second pass over the cert guides rebuilt on 2026-11-07: exam logistics re-fetched from the vendor pages, every bank question decided against vendor docs, and the claim-dense notes checked. Counts are of items examined. Logistics, questions and claims are shown as checked / fixed (claims: verified / fixed / unverifiable).

| Guide | Logistics (checked / fixed) | Questions (checked / wrong keys) | Claims (verified / fixed / unverifiable) |
|---|---|---|---|
| databricks/ml-associate | 13 / 0 | 30 / 0 | 52 / 3 / 0 |
| nvidia/ai-networking-professional (NCP-AIN) | 12 / 0 | 30 / 0 | 22 / 3 / 5 |
| nvidia/openusd-development-professional (NCP-OUSD) | 12 / 0 | 30 / 0 | 38 / 5 / 6 |
| nvidia/generative-ai-multimodal-associate (NCA-GENM) | 13 / 0 | 30 / 0 | 24 / 3 / 3 |
| azure/ai-103 | 17 / 3 | 30 / 0 | about 55 / 8 / 7 |
| azure/ai-901 | 10 / 0 | 20 / 0 | about 24 / 6 / 2 |

No keyed answer was wrong in any bank, so nothing was re-lettered and the balancer check still passes. Distractor and explanation fixes: AI-901 Q9 (two distractors and the explanation), AI-103 Q22 and Q28, NCP-AIN Q7, Databricks Q6.

### Cert guide fixes

| Page | Old | New | Source |
|---|---|---|---|
| Databricks fact-sheet, note 01, scenarios | `fe.score_batch` needs only the keys | needs primary keys plus any external columns the model was trained with | https://docs.databricks.com/aws/en/machine-learning/feature-store/train-models-with-feature-store |
| Databricks note 01, bank Q6 | `create_table` implied the only route | any Unity Catalog Delta table with a primary key constraint can be a feature table | https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc |
| NCP-AIN note 02, bank Q7 | Cumulus does not support L3 VNI on the default VRF | one L3 VNI per tenant VRF; default-VRF claim marked unverified | https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing/ |
| NCP-AIN note 05 | cl-resource-query sample not reproduced | sample lines and NVUE forwarding-profile commands added | https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-59/Monitoring-and-Troubleshooting/Resource-Diagnostics-Using-cl-resource-query/ |
| NCP-AIN note 03 | SM priority rule not covered | priority 0 (default) to 15, master chosen by priority and GUID; tie-break marked unverified | https://www.mankier.com/8/opensm |
| NCP-OUSD notes 01, 02 | misquoted instancing, glossary and Kind page text | actual page wording or unquoted paraphrase | https://openusd.org/release/api/_usd__page__scenegraph_instancing.html |
| NCP-OUSD note 08 | UsdPreviewSurface spec 2.5 | page header 2.5, changelog lists 2.6 | https://openusd.org/release/spec_usdpreviewsurface.html |
| NCA-GENM note 01 | CLIP misquote | "predicting which caption goes with which image", 400M pairs | https://arxiv.org/abs/2103.00020 |
| NCA-GENM note 07, flashcard | NeMo Guardrails "accurate, on topic and secure"; confidential computing "protects data during processing" | "accurate, appropriate, on topic and secure"; confidential computing only listed as a security feature | https://www.nvidia.com/en-us/ai-data-science/trustworthy-ai/ |
| AI-103 fact-sheet, README | "Microsoft says most exams have 40-60 questions" | not published for AI-103, marked unverified | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103 |
| AI-103 fact-sheet, note 03, flashcard | DALL-E 3 retired 2026-03-04 | retired, date unverified | https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule |
| AI-103 note 03 | Sora 2 with no caveat | schedule lists sora-2 retirements 2026-07-15 and 2026-10-15 | same |
| AI-103 bank Q22, Q28 | confidence claimed for image analyzers; unfound quote | scenario reworded, hedged explanation; verified quote | https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-query |
| AI-901 bank Q9 C, D | Standard "no pooled capacity"; provisioned "any region" | Standard stays in one Azure geography; Global Provisioned may process anywhere | https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types |
| AI-901 note 01, flashcard | Data Zone "within a geography" | Data Zone is a Microsoft-defined zone (US/EU/APAC) | same |
| AI-901 notes 01, 03 | Face identification and verification limited | whole Face service is access-limited | https://learn.microsoft.com/en-us/azure/ai-services/face/overview-identity |
| AI-901 notes 02, 03, 04, fact-sheet | Claude via Marketplace; phrase list without limit; CU as successor to Document Intelligence; Foundry IQ "built on" AI Search | partner models incl. Anthropic; phrase lists need real-time or fast transcription; CU Studio transition path; AI Search provides indexing and retrieval | https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview |

### Still unverifiable

- NCA-GENM: 50 versus 50-60 questions (the exam page states both); the unread reading-list items; the CLIP-in-diffusion sentence (OpenAI page 403).
- NCP-OUSD: file-format plug-in, ASWF and Scalable Asset Structure pages (404), SceneIndex plug-ins, in-memory resolvers, Conceptual Data Mapping; "Certiverse account" is not on the fetched page; hands-on lab not stated.
- NCP-AIN: limited-PKey rule (InfiniBand spec, not NVIDIA pages), OpenSM tie-break, L3 VNI on default VRF, ibdiagnet, SuperNIC congestion control, DSX Air, PFC watchdog.
- AI-103: DALL-E 3 date, question count, price, image-analyzer confidence, Custom Translator with document translation, azure-ai-projects 2.x vs 1.x, Q7/Q18/Q24 rest on design practice.
- AI-901: lab yes/no (not stated), Azure OpenAI and Agent Service renames, speech WER and diarisation claims.
- Databricks: promote-code-versus-model exceptions are labelled "my reading" in note 01 (the MLOps page lists none).
