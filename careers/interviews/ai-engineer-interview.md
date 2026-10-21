# AI Engineer Interview Guide

**In one line:** AI engineer interviews test whether you can build reliable products on top of models; prepare for five rounds (LLM fundamentals, RAG and retrieval, evals and quality, agents and production, and a practical build) using the sample questions and strong-answer outlines below.
**Last reviewed:** 2026-10-21

---

## The short version

- Expect a mix of **normal software engineering** (coding, system design, behavioural) and **AI-specific** rounds. Companies weight them differently; startups often add a take-home or live build.
- Interviewers look for four things: you understand **how models behave** (not just API syntax), you **measure** instead of guessing, you think about **cost, latency and failure**, and you can **ship**.
- The most common differentiator is **evals**. Candidates who can explain how they would know a system works, and how they would catch regressions, stand out.
- Prepare two or three **projects you can talk about in depth**: architecture, numbers, what failed, what you would change.
- Questions below come with outlines of a strong answer. Practise saying them out loud in two to three minutes each.

## What the loop usually looks like

| Round | What they test | How to prepare |
|---|---|---|
| Recruiter / hiring manager | Motivation, relevant experience | A crisp story of what you built and its impact |
| Coding | General programming, often Python | Normal coding practice; data structures, APIs, async |
| LLM fundamentals and applied knowledge | Tokens, context, sampling, prompting, RAG, tools | This page; the concept pages linked below |
| AI system design | Design an LLM-powered system end to end | [AI system design interview](ai-system-design-interview.md) |
| Practical build or take-home | Build a small LLM feature with evals | Rehearse with the projects in [build/](../../build/projects/chatbot-in-an-afternoon.md) |
| Behavioural | Collaboration, judgement, ownership | Stories in STAR form (situation, task, action, result) |

## Round 1: LLM fundamentals

**Q: What happens, step by step, when you send a prompt to an LLM API?**

Strong answer outline:
- Text is split into tokens by the model's tokenizer; the system prompt, history, tools and user message are all part of the input.
- The model processes the whole input in parallel (prefill), building a KV cache, then generates output tokens one at a time, each sampled from a probability distribution over the vocabulary.
- Sampling settings (temperature, top-p) shape randomness; generation stops on an end token, a stop sequence or `max_tokens`.
- You pay per input and output token; output is usually priced higher and dominates latency.
- Bonus: reasoning models generate hidden thinking tokens first, billed as output.
- Read: [tokenization](../../explainers/concepts/tokenization.md), [KV cache](../../explainers/concepts/kv-cache.md), [sampling and decoding](../../explainers/concepts/sampling-and-decoding.md), [reasoning models](../../explainers/concepts/reasoning-models.md).

**Q: Why do models hallucinate, and what do you do about it in a product?**

- Models are trained to produce plausible continuations; training and evaluation have historically rewarded guessing over saying "I don't know".
- Mitigations: ground answers in retrieved sources; require citations; allow and reward abstention; constrain outputs with schemas; verify critical facts with code or a second check; tell users the limits.
- Measure the hallucination rate on an eval set rather than claiming it is solved.
- Read: [hallucinations](../../learn/concepts/hallucinations.md), [Why language models hallucinate](../../papers/techniques/149-why-language-models-hallucinate/summary.md).

**Q: When would you use temperature 0, and does it make outputs deterministic?**

- Use low temperature for extraction, classification and code where you want the most likely answer; higher for brainstorming.
- It does not guarantee identical outputs: batching, floating-point non-determinism and infrastructure changes can still vary results. Some newer models and settings do not expose temperature at all; effort or other controls replace it.
- For reproducibility, rely on evals over many cases, not single runs.

**Q: Fine-tuning vs RAG vs prompting: how do you choose?**

- Prompting first: cheapest, fastest to change.
- RAG when the model needs knowledge it does not have, especially private or changing data; easy to update and cite.
- Fine-tuning for behaviour, format or style at scale, or to make a small model do a narrow task well; not a good way to add facts that change.
- Often combined. Decide with an eval, not opinion.
- Read: [fine-tuning vs RAG](../../learn/concepts/fine-tuning-vs-rag.md), [LoRA](../../papers/techniques/10-lora/summary.md).

**Q: What is prompt caching and how do you design for it?**

- Providers reuse a processed prompt prefix, billing cached tokens at a fraction of the normal rate and reducing latency.
- It is a prefix match: put stable content (system prompt, tools, reference docs) first and variable content last; avoid timestamps or IDs early in the prompt.
- Verify with the cached-token counts in usage data.
- Read: [prompt caching](../../learn/concepts/prompt-caching.md).

## Round 2: RAG and retrieval

**Q: Walk me through building a RAG system over 50,000 internal documents.**

- Ingestion: parse formats, clean, chunk by structure with metadata (source, date, permissions).
- Index: embeddings in a vector store plus a keyword index for hybrid search.
- Query: rewrite conversational queries, retrieve wide, rerank, keep the top few, filter by user permissions.
- Generate: grounded prompt, citations, abstain when unsupported.
- Evaluate retrieval (recall@k) and answers (faithfulness, correctness) separately; build the test set from real questions.
- Operate: incremental re-indexing, deletion, monitoring, feedback loop.
- Read: [RAG explained](../../learn/concepts/rag-explained.md), [advanced RAG patterns](../../build/patterns/advanced-rag-patterns.md).

**Q: Users say the bot "can't find" things that are definitely in the docs. How do you debug?**

- Collect failing questions; for each, find the passage that should answer it.
- Check whether it was retrieved at all, and at what rank. If not retrieved: chunking, embedding mismatch with exact terms (add hybrid search), missing metadata, stale index, or a permissions filter. If retrieved but ranked low: add a reranker. If retrieved and still wrong: a generation problem.
- Fix one thing, re-measure on the set.

**Q: How do you stop the bot showing documents a user is not allowed to see?**

- Enforce access control at retrieval time with filters tied to the user's identity, never by asking the model to withhold.
- Test with cases where a user lacks access and assert those chunks never appear in context.

## Round 3: evals and quality

**Q: How would you know your new prompt is better than the old one?**

- A fixed test set of representative and hard cases with expected outputs or rubrics.
- Automatic metrics where possible (exact match, schema validity, tests passing), LLM-as-judge with a rubric where not, calibrated against human labels.
- Run both versions, compare overall and by slice, check cost and latency too, and look at the actual differences, not just the score.
- Then a canary or A/B in production with online metrics.
- Read: [evals for LLMs](../../learn/concepts/evals-for-llms.md), [set up an eval harness](../../build/projects/set-up-eval-harness.md), [LLM-as-a-judge](../../papers/techniques/85-llm-as-judge/summary.md).

**Q: What are the risks of LLM-as-a-judge?**

- Position bias, verbosity bias, self-preference, inconsistency.
- Mitigate with clear rubrics, pairwise comparisons in both orders, a different model family as judge where possible, and agreement checks against human labels.

**Q: Public benchmark scores say model A beats model B. Do you switch?**

- Not on that alone. Benchmarks can be contaminated or saturated and rarely match your task. Run your own evals, include cost and latency, then decide.
- Read: [contamination and saturation](../../explainers/benchmarks/contamination-and-saturation.md).

## Round 4: agents and production

**Q: When should you build an agent rather than a workflow?**

- Workflow when the steps can be written down; agent when the next step depends on results in ways you cannot predict.
- Agents cost more, are slower and less predictable, and widen the security surface.
- Start simple; add autonomy where evals show it helps.
- Read: [agent architectures](../../build/patterns/agent-architectures.md), [Building Effective Agents](../../papers/essays/115-building-effective-agents/summary.md).

**Q: An agent sometimes loops forever and burns money. What do you do?**

- Immediate: step limits, token or dollar budgets per task, detection of repeated identical tool calls.
- Root cause: inspect traces; usually unclear tool errors, missing information, or a goal with no clear completion check.
- Improve tool error messages, add an explicit done condition verified in code, and add these cases to the eval set.

**Q: How do you defend an agent that reads emails and can send emails?**

- Assume prompt injection will happen. Treat all external content as data.
- Least privilege: recipient allowlists, read-only by default, separate reader and sender components.
- Human confirmation for external or irreversible actions.
- Injection screening and monitoring as extra layers, not the main defence.
- Read: [prompt injection defense](../../safety/security/prompt-injection-defense.md), [agent security](../../safety/security/agent-security.md), [prompt injection red team](../../build/projects/prompt-injection-red-team.md).

**Q: Your LLM feature costs three times the budget. Where do you look?**

- Measure cost per completed task by feature; find the biggest contributors.
- Free wins: prompt caching, trimming history and retrieved context, shorter outputs, batching non-urgent work.
- Trade-offs: smaller model or lower reasoning effort on routes where evals hold; routing.
- Guardrails: per-user budgets; anomaly alerts.
- Read: [cost and latency control](../../build/patterns/cost-and-latency-control.md).

**Q: What do you log and monitor for an LLM feature in production?**

- Traces per request with every model, retrieval and tool span; tokens, latency, cost; prompt and model versions.
- Error, refusal and fallback rates; p95 latency; quality signals (feedback, guardrail triggers, sampled judge scores).
- Privacy controls on what is logged and who can read it.
- Read: [LLMOps and observability](../../build/patterns/llmops-observability.md).

## Round 5: practical build

Common formats: "Build an endpoint that extracts fields from these 20 documents" or "Add a question-answering feature over this folder", in 60 to 120 minutes, or a take-home.

How to do well:

1. **Clarify** the inputs, outputs, quality bar and constraints before coding.
2. **Get an end-to-end slice working early**, even if crude.
3. **Add a tiny eval**: 10 cases with expected outputs and a score. This is the step most candidates skip.
4. **Handle failures**: retries, invalid outputs, empty results.
5. **Explain trade-offs** as you go: model choice, cost, what you would do with more time.

Practice with [structured extraction pipeline](../../build/projects/structured-extraction-pipeline.md) and [build a RAG pipeline](../../build/projects/build-rag-pipeline.md) under a timer.

## Behavioural questions with an AI twist

- "Tell me about an AI feature that did not work as expected." Show how you found out (metrics, users), what you changed, and what you learned.
- "How did you decide not to use AI for something?" Shows judgement.
- "How do you keep up with the field?" Mention concrete habits: reading papers and release notes, re-running your evals on new models. This site's [papers](../../docs/ROADMAP.md) are a good source.
- "Describe a disagreement about model or vendor choice." Show you resolved it with data.

## Questions to ask them

- How do you evaluate quality today, and who owns the eval sets?
- How do you handle model upgrades and deprecations?
- What is the split between building new features and maintaining existing ones?
- What does the AI security review process look like?

## Common mistakes

- **API trivia without understanding.** Knowing parameter names is less important than knowing what they do to behaviour and cost.
- **No numbers.** "It worked well" is weak; "faithfulness went from 82% to 94% on 120 cases" is strong.
- **Ignoring cost and latency.** Every design answer should mention them.
- **Overselling agents.** Interviewers like candidates who choose the simplest solution that works.
- **Not admitting uncertainty.** "I'd test that" is a good answer when it is true.

## Next steps

- [AI system design interview](ai-system-design-interview.md) and [ML engineer interview](ml-engineer-interview.md)
- [AI engineer roadmap](../roles/ai-engineer-roadmap.md)
- Projects to talk about: [chatbot](../../build/projects/chatbot-in-an-afternoon.md), [RAG pipeline](../../build/projects/build-rag-pipeline.md), [eval harness](../../build/projects/set-up-eval-harness.md), [agent with MCP](../../build/projects/build-claude-agent-with-mcp.md)

## Sources

- Anthropic, "Building effective agents" (Dec 2024): https://www.anthropic.com/engineering/building-effective-agents
- Kalai et al., "Why Language Models Hallucinate" (OpenAI, 2025): https://arxiv.org/abs/2509.04664
- Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (2023): https://arxiv.org/abs/2306.05685
- Anthropic, Prompt caching docs: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- OWASP, Top 10 for LLM Applications: https://genai.owasp.org/llm-top-10/
