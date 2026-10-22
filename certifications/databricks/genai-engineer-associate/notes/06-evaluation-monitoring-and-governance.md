# Evaluation, Monitoring and Governance - Databricks GenAI Engineer Associate

## Overview

This note covers **Section 6: Evaluation and Monitoring** (ten objectives) and **Section 5: Governance** (four objectives) of the exam guide live since 2026-03-18, building on note 03. Databricks publishes no weights for either section. The current outline is noticeably more specific than the old one: it names MLflow scoring and tracing, judges that need ground truth, AI Gateway inference and usage tables, rate limiting, custom scorers and SME feedback, so expect questions that turn on the exact tool.

**[📖 Built-in judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/)** - which judges need ground truth
**[📖 AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/)** - usage tracking, inference tables, rate limits, guardrails

---

## 1. Evaluation versus monitoring

The guide asks you to "compare the evaluation and monitoring phases of the Gen AI application life cycle". Evaluation happens before release, against a fixed evaluation set you chose, and answers "is this version good enough to ship, and better than the last one?". Monitoring happens after release, against live traffic you did not choose, and answers "is it still working, what is it costing, and are users hitting cases we never tested?". The same judges can serve both: in evaluation they score a curated dataset with known answers; in monitoring they score a sample of production traces, where no ground truth exists. That last point is why the next section matters.

## 2. Scoring with MLflow, and which judges need ground truth

On Databricks, agents are evaluated with `mlflow.genai.evaluate()`, which runs the agent (or reads existing traces) over an evaluation dataset and applies scorers to each record, logging the results to an MLflow run. MLflow tracing records every step the agent took (each retrieval, tool call and model call with inputs, outputs and timing), so a low score can be traced to the step that caused it. The objective "evaluate agent performance using MLflow scoring and tracing" is about using these together: the score tells you that something is wrong, the trace tells you where.

"Identify evaluation judges that require ground truth" is a direct recall question. Ground truth means an expected answer or expected facts supplied with each evaluation record. The built-in judges split like this:

| Needs ground truth | Does not need ground truth |
|---|---|
| `Correctness` (is the response correct against the expected answer or facts) | `RelevanceToQuery` (does the response address the request) |
| `RetrievalSufficiency` (does the retrieved context contain everything needed for the expected answer) | `RetrievalRelevance` (is each retrieved chunk relevant to the request) |
| `ToolCallCorrectness` (were the right tools called with the right arguments) | `RetrievalGroundedness` (is the response supported by the retrieved context, the hallucination check) |
| | `Safety`, `Guidelines`, `ToolCallEfficiency` |

The reasoning to remember: a judge needs ground truth when it compares against what the answer *should* have been. Relevance, groundedness and safety can be judged from the request, the context and the response alone, which is why they are the ones you can run on production traffic. `ExpectationsGuidelines` sits in between: it needs per-record guidelines passed as expectations, but not a reference answer.

## 3. Custom scorers and SME feedback

Built-in judges cover common qualities. When a requirement is domain-specific ("every answer must cite a policy number", "never quote a price older than 30 days"), the guide asks you to "use Databricks custom Scorers". You can write a code-based scorer, a Python function decorated as a scorer that inspects inputs, outputs or the trace and returns a value, which is best when the check is deterministic. Or you can write a custom LLM judge with your own natural-language criteria, which is best when the check needs judgment. Prefer code when code can decide; it is cheaper and does not vary.

"Incorporate SME feedback to improve agent performance" is about domain experts. MLflow provides a review app and labeling sessions where experts read sampled answers and record ratings and corrections. The guide's sample shows the trap: four experts whose ratings disagree produce unreliable data. The fix is to define clear rubrics, calibrate the experts on them, and feed the aligned judgments into `mlflow.genai.evaluate()`. Replacing the experts with an LLM judge, averaging conflicting scores, or dropping every disputed case are all wrong, because each discards the signal instead of making it consistent. Expert corrections also become ground truth for future evaluation sets, and can be used to align a custom judge with how the experts actually decide.

## 4. Choosing an LLM from quantitative metrics

"Select an LLM choice (size and architecture) based on a set of quantitative evaluation metrics" and "select the best model for a given task based on common metrics generated in experiments" both ask you to read a results table. The habit is to identify the metric the scenario cares about first (accuracy on the task, latency, cost per request, groundedness), filter out models that miss a hard constraint, and only then pick the best of the rest. A larger model that scores two points higher but triples latency is the wrong choice for a latency-bound chatbot; a small model that fails the quality bar is wrong however cheap it is.

## 5. Monitoring a live endpoint

Several objectives describe the same production toolkit from different angles. **Inference tables** log each request and response sent to a serving endpoint into a Unity Catalog Delta table, which is how you "use inference logging to assess deployed RAG application performance": you can query real questions, find the ones that failed, and add them to the evaluation set. **Usage tracking** records requests, tokens and latency per endpoint in system tables, which is how you see who is using what and what it costs. **Rate limiting** caps consumption on an endpoint so one user or application cannot exhaust capacity or budget. These three are features of **AI Gateway**, which the guide names together ("Inference Tables, Usage Tables, and rate limiting") for tracking an LLM or an agent deployed with Agent Framework; AI Gateway also provides guardrails, traffic splitting and fallbacks to another model.

**Agent Monitoring** (production monitoring in MLflow) runs your scorers automatically on a sample of live traces, so quality metrics such as groundedness, relevance and safety keep updating after launch without anyone running a job. Combine it with inference tables: monitoring tells you that quality dropped, the logged requests show you which questions caused it.

"Select key metrics to monitor for a specific LLM deployment scenario" asks for judgment. A customer-facing assistant cares about safety, groundedness, latency percentiles and error rate. An internal batch summarizer cares about throughput, cost per row and failure count. A RAG system should also watch retrieval quality, because a stale or broken index shows up first as falling retrieval relevance.

## 6. Controlling cost

"Use Databricks features to control LLM costs" draws on most of the above. Pick the smallest model that meets the quality bar, using evaluation results rather than intuition. Use pay-per-token for low or spiky traffic and provisioned throughput only when steady volume justifies it. Allow endpoints to scale to zero where cold starts are acceptable. Move batch work to `ai_query()` instead of interactive endpoints. Cap usage with AI Gateway rate limits and watch the usage tables. Keep prompts and retrieved context tight, since every token sent is paid for.

## 7. Governance: guardrails, masking, licensing and problematic text

Section 5 has four objectives, each a judgment call.

"Use masking techniques as guard rails to meet a performance objective" means removing or replacing sensitive values (names, account numbers, emails) before they reach the model or the logs, so the application can use a capable model without exposing protected data. Masking keeps the request useful (the model still sees that there *is* an account number) while removing the value itself. In Unity Catalog, column masks and row filters apply the same idea at the data layer, and AI Gateway guardrails can detect or block PII in requests and responses.

"Select guardrail techniques to protect against malicious user inputs" is about prompt injection and abuse. Layer the defences: validate and constrain input, keep system instructions separate from user text, filter inputs and outputs with safety guardrails, limit what tools the agent can call and with what permissions, and rate-limit to blunt automated attacks. No single filter is enough, and the answer that relies on "tell the model to ignore malicious instructions" alone is the weak one.

"Use legal/licensing requirements for data sources to avoid legal risk" asks you to check that you may use a data source for your purpose before you index it. If a site's terms forbid commercial reuse, the compliant answer is not to use that data (or to obtain a licence), not to scrape it and hope. The same applies to model licences, which can restrict commercial use or require attribution.

"Recommend an alternative for problematic text mitigation in a data source feeding a GenAI application" covers sources that contain toxic, biased, outdated or sensitive passages. Options include filtering or cleaning the text before chunking, excluding the offending documents, replacing the source with a cleaner one, and adding output guardrails as a second line of defence. Cleaning the data is generally better than trusting the model to ignore what it retrieves.

## Exam tips for this section

Memorize which judges need ground truth (`Correctness`, `RetrievalSufficiency`, `ToolCallCorrectness`). Know that inference tables, usage tables and rate limits are AI Gateway features. Calibrate SMEs with rubrics rather than averaging or replacing them. Prefer code scorers when a rule is deterministic. For governance, mask before the model, layer guardrails, and respect licences.

## Documentation Links Summary

| Topic | Link |
|-------|------|
| Built-in judges | [Judges and ground truth](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/) |
| AI Gateway | [AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/) |
| Evaluation | [MLflow GenAI evaluation](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/) |
| Tracing | [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/overview) |
