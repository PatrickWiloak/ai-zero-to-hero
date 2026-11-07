# Data Scientist in the LLM Era

**In one line:** What changes and what stays the same for data scientists now that LLMs can write queries and draft analyses, and how to adjust your skills and portfolio.
**Last reviewed:** 2026-11-07

---

## The short version

- The core of the job, framing a question, getting trustworthy data, choosing a method and communicating uncertainty, is not automated by LLMs. Assistants speed up the typing around it.
- What shifts: more time on evaluation and checking, because generated code and summaries can be wrong in confident ways. See [hallucinations](../../learn/concepts/hallucinations.md).
- New useful skills: structured extraction from text, embeddings for search and clustering, and building evals. Classical skills (statistics, experiment design, gradient boosting) stay valuable.
- This page is judgment, not labour-market data. No hiring or salary figures are given because none were sourced.

## What stays the same

- Statistics, causal thinking and experiment design. No LLM tells you your A/B test was underpowered unless you ask the right question.
- Feature work on tabular data: [feature engineering](../../learn/concepts/feature-engineering-and-data-prep.md), [trees and boosting](../../learn/concepts/decision-trees-and-gradient-boosting.md), [time series](../../learn/concepts/time-series-forecasting.md).
- Telling a story a decision-maker can act on. See [research and analysis with AI](../../work/use-cases/research-and-analysis.md).

## What changes

- **You work with an assistant.** Use it for boilerplate, SQL drafts and plotting code, then verify. See [AI coding agents explained](../../learn/concepts/ai-coding-agents-explained.md) and [for analysts](../../work/playbooks/for-analysts.md).
- **Text becomes data.** Unstructured documents can be turned into rows: [structured outputs](../../learn/concepts/structured-outputs.md) and the [structured extraction project](../../build/projects/structured-extraction-pipeline.md).
- **Semantic tools.** [Embeddings and vector search](../../learn/concepts/embeddings-and-vector-search.md) give clustering and similarity search on text.
- **Evaluation of generated output** is a data science problem: sampling, labelling, agreement, metrics. See [evals for LLMs](../../learn/concepts/evals-for-llms.md) and [set up an eval harness](../../build/projects/set-up-eval-harness.md).

## A practical skill plan

1. Keep your statistics and SQL sharp. The [data site](https://data.noblerworks.com/) is the deeper home for this.
2. Add one LLM workflow end to end: extract fields from messy text, validate them, and measure accuracy against a hand-labelled sample.
3. Learn when not to use an LLM: a gradient-boosted model on clean tabular data is usually cheaper and easier to audit ([tabular ML end to end](../../build/projects/tabular-ml-end-to-end.md)).
4. Learn the cost side: [AI cost basics](../../learn/concepts/ai-cost-basics.md).

## Data scientist or ML engineer?

If you enjoy the question and the story, stay on the data scientist side. If you enjoy shipping the model, follow the [ML engineer roadmap](ml-engineer-roadmap.md). Many teams blur the two.

## Common mistakes

- Pasting data into a public assistant without checking your employer's rules. See the [acceptable use policy guide](../../work/enablement/acceptable-use-policy.md).
- Trusting a generated number without recomputing it.
- Dropping statistics to chase prompts.

## Next steps

- [Build an AI portfolio](build-an-ai-portfolio.md) and the [AI careers map](ai-careers-map.md).
- [Machine learning basics](../../learn/concepts/what-is-machine-learning.md).

## Sources

- Judgment: the shifts above are this site's editorial view.
- Linked pages on this site hold sourced detail.
