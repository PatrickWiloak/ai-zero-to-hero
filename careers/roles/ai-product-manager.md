# AI Product Manager

**In one line:** What an AI product manager does differently from a general PM, the skills to build, and how to get evidence of them before you have the title.
**Last reviewed:** 2026-11-07

---

## The short version

- An **AI product manager** owns a product whose behaviour is probabilistic: the same input can give different outputs, and quality is a distribution, not a yes or no.
- The extra work compared with a general PM: define what "good" means, own the eval set, set cost and latency budgets, decide where a human stays in the loop, and handle risk.
- You do not need to train models. You do need to read an eval report, spot a bad metric and talk to engineers about trade-offs.
- This page is judgment, with no salary or market numbers (none sourced).

## What is different

| Area | What the AI PM adds |
|---|---|
| Quality | A written definition of good, plus an eval set that grows from real failures. See [evals for LLMs](../../learn/concepts/evals-for-llms.md). |
| Cost | Cost per task and a budget, not just a feature price. See [AI cost basics](../../learn/concepts/ai-cost-basics.md) and [measuring AI ROI](../../work/enablement/measuring-ai-roi.md). |
| Failure | Plan for wrong answers: [hallucinations](../../learn/concepts/hallucinations.md), [guardrails](../../learn/concepts/guardrails-and-safety.md), fallbacks and human review. |
| Build choice | Prompt, RAG, fine-tune or classic ML? See [fine-tuning vs RAG](../../learn/concepts/fine-tuning-vs-rag.md). |
| Risk | Privacy, security and regulation: [responsible AI basics](../../safety/governance/responsible-ai-basics.md), [EU AI Act](../../safety/governance/eu-ai-act-compliance.md), [NIST AI RMF](../../safety/governance/nist-ai-rmf.md), [AI risk assessment](../../safety/governance/ai-risk-assessment.md). |
| Trust | Show sources, express uncertainty, make errors easy to report. |

## Skills to build

1. **Technical fluency.** Read [LLM basics](../../learn/concepts/llm-basics.md), [RAG explained](../../learn/concepts/rag-explained.md), [agents explained](../../learn/concepts/agents-explained.md) and [prompt engineering](../../learn/concepts/prompt-engineering.md).
2. **Evaluation.** Build a small eval yourself with [set up an eval harness](../../build/projects/set-up-eval-harness.md).
3. **Rollout.** See the [AI adoption playbook](../../work/enablement/ai-adoption-playbook.md) and [choosing enterprise AI tools](../../work/enablement/choosing-enterprise-ai-tools.md).
4. **Leadership view.** [AI for leaders](../../learn/start-here/ai-for-leaders.md).

## Getting evidence without the title

- Ship a small AI feature or internal tool at your current job and write down the eval, the cost and what you cut.
- Build one prototype yourself ([chatbot in an afternoon](../../build/projects/chatbot-in-an-afternoon.md)) so you can speak from experience.
- Write a one-page product spec for an AI feature with success metrics, failure handling and risks.

## Common mistakes

- Promising accuracy before you have an eval set.
- Treating the model as the product. Data, UX and review flows usually decide whether it works.
- Ignoring cost until the invoice arrives.

## Next steps

- [AI product manager interview](../interviews/ai-product-manager-interview.md).
- [AI careers map](ai-careers-map.md) and [build an AI portfolio](build-an-ai-portfolio.md).
- Governance depth on the [security site](https://security.noblerworks.com/).

## Sources

- Judgment: the role description is this site's editorial view.
- Regulatory and framework detail lives in the linked safety pages, which cite their own sources.
