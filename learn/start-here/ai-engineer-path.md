# The AI Engineer Path

**In one line:** A route for developers who want to build products on top of language models - prompts, retrieval, tools, agents, evals and production operations - in roughly twelve weeks of part-time work, with a project at each stage.
**Last reviewed:** 2026-10-21

---

## The short version

- An **AI engineer** builds software whose core behaviour comes from a model they did not train. The job is mostly software engineering plus a new set of skills: context design, evaluation, cost control, and defending against a new class of attacks.
- You need solid programming (Python or TypeScript), comfort with HTTP APIs and JSON, and basic cloud deployment. You do not need to derive backpropagation.
- The core loop of the job: **design the context, call the model, check the output, measure across many cases, ship, watch.** Every stage below adds one piece of that loop.
- Your portfolio matters more than certificates. Three small, finished, evaluated projects beat one ambitious unfinished one.
- The skill that most separates good AI engineers from the rest is **evaluation**: knowing, with a number, whether a change made things better.

## Who this is for

This path assumes you can already program. If you cannot, do [Python for AI](../day-one/python-for-ai.md) and Phase 2 of the [Zero to Hero path](zero-to-hero-path.md) first. If you are a backend, frontend, data or platform engineer, you are the target reader: most of what you know transfers, and this page shows you what is new.

If you are more interested in training and serving models than in building applications on them, the [ML engineer path](ml-engineer-path.md) is a better fit. The two overlap in the middle; many people do both.

## Stage 1: Foundations, fast (week 1)

You need an accurate mental model of what you are calling. Skim [LLM basics](../concepts/llm-basics.md), [Tokenization](../../explainers/concepts/tokenization.md), [Context windows](../../explainers/concepts/context-windows.md), [Sampling and decoding](../../explainers/concepts/sampling-and-decoding.md) and [Reasoning models](../../explainers/concepts/reasoning-models.md). Then [Hallucinations](../concepts/hallucinations.md), because designing around them is half your job.

Then get set up: [API keys and environment variables](../day-one/api-keys-and-env-vars.md), [Your first LLM API call](../day-one/first-llm-api-call.md) with at least two providers, and [Run a model locally](../day-one/run-a-model-locally.md). Knowing how to swap providers and run an open-weight model locally will save you later when a price or a policy changes.

Know the landscape at a glance: the [Claude](../../explainers/model-families/claude.md), [GPT](../../explainers/model-families/gpt.md), [Gemini](../../explainers/model-families/gemini.md), [Qwen](../../explainers/model-families/qwen.md) and [Llama](../../explainers/model-families/llama.md) family explainers, plus [open vs closed weights](../../explainers/concepts/open-vs-closed-weights.md). [Which model for which job](../../tools/decisions/which-model-for-which-job.md) turns that into choices.

**Project:** a command-line tool that takes a file and a task ("summarise", "extract action items", "translate to Spanish") and runs it against a model of your choice, printing the result, the token counts and the cost.

## Stage 2: Prompts and outputs (weeks 2 to 3)

Prompting is not a bag of tricks. It is writing a specification for a very capable, very literal colleague. Read [Prompt engineering](../concepts/prompt-engineering.md), then [Structured outputs](../concepts/structured-outputs.md): your code needs JSON that matches a schema, not prose. Learn [Prompt caching](../concepts/prompt-caching.md) early; for any application with a long, stable system prompt it cuts cost and latency substantially and is a few lines of code.

The research behind techniques you will use daily is worth an hour: [chain-of-thought](../../papers/techniques/09-chain-of-thought/summary.md), [self-consistency](../../papers/techniques/77-self-consistency/summary.md), and the [GPT-3 few-shot paper](../../papers/language-models/04-gpt3-few-shot-learners/summary.md), which is where "put examples in the prompt" comes from.

**Project:** [Structured extraction pipeline](../../build/projects/structured-extraction-pipeline.md). Take 50 real documents (invoices, job ads, support emails), extract fields into a schema, and measure accuracy against a hand-labelled sample. This is the single most common production AI task, and it teaches you evaluation from the first day.

## Stage 3: Retrieval (weeks 4 to 5)

Most business applications need the model to answer from information it was not trained on. Read [Embeddings and vector search](../concepts/embeddings-and-vector-search.md), [RAG explained](../concepts/rag-explained.md), [Context windows and management](../concepts/context-windows-and-management.md) and [Fine-tuning vs RAG](../concepts/fine-tuning-vs-rag.md). Then [Advanced RAG patterns](../../build/patterns/advanced-rag-patterns.md) for hybrid search, reranking and query rewriting, which is what turns a demo into something users trust.

Research to read: [RAG](../../papers/techniques/13-rag/summary.md), [dense retrieval](../../papers/techniques/87-dense-retrieval/summary.md), [GraphRAG](../../papers/techniques/60-graph-rag/summary.md), and [RULER](../../papers/techniques/132-ruler/summary.md), which shows that a model's advertised context length and its usable context length are different numbers.

**Project:** [Build a RAG pipeline](../../build/projects/build-rag-pipeline.md) over a document set you care about. Pick the store with [the vector database decision](../../tools/decisions/vector-database.md). Write 25 questions with known answers before you start tuning.

## Stage 4: Tools, agents and MCP (weeks 6 to 8)

Read [Tool use and function calling](../concepts/tool-use-and-function-calling.md), [Agents explained](../concepts/agents-explained.md), [Agentic loops](../concepts/agentic-loops.md) and [MCP explained](../concepts/mcp-explained.md). Then [Agent architectures](../../build/patterns/agent-architectures.md) for the patterns (router, orchestrator-worker, evaluator-optimiser) and the [agent frameworks comparison](../../tools/comparisons/agent-frameworks.md) for the libraries.

The essential reading is short: the [Building Effective Agents summary](../../papers/essays/115-building-effective-agents/summary.md) (start with the simplest thing that works), [ReAct](../../papers/techniques/21-react/summary.md), [Reflexion](../../papers/techniques/78-reflexion/summary.md), the [MCP summary](../../papers/techniques/59-model-context-protocol/summary.md), and [SWE-bench](../../papers/techniques/84-swe-bench/summary.md) and [METR time horizons](../../papers/techniques/145-metr-time-horizons/summary.md) to calibrate what agents can actually do. The [agent benchmarks explainer](../../explainers/benchmarks/agents-and-computer-use.md) ties these together.

Security becomes urgent here, because an agent with tools can do damage. Read [Prompt injection explained](../../safety/security/prompt-injection-explained.md) and [Agent security](../../safety/security/agent-security.md) before you give an agent write access to anything.

**Project:** [Build a Claude agent with MCP](../../build/projects/build-claude-agent-with-mcp.md). Then try to break it with [Prompt injection red team](../../build/projects/prompt-injection-red-team.md).

## Stage 5: Evaluation (weeks 9 to 10)

If you only get good at one thing on this path, make it this. Read [Evals for LLMs](../concepts/evals-for-llms.md), the [LLM-as-a-judge summary](../../papers/techniques/85-llm-as-judge/summary.md), and [Contamination and saturation](../../explainers/benchmarks/contamination-and-saturation.md) for why public leaderboards are not your eval.

The practical pattern: a versioned set of test inputs drawn from real usage, a mix of deterministic checks (does it parse, does it contain the required field, is the number right) and model-graded checks (is the tone right, is the answer supported by the retrieved text), run on every change. Start with 20 cases. Add every production failure as a new case.

**Project:** [Set up an eval harness](../../build/projects/set-up-eval-harness.md) for your RAG or agent project. Make one prompt change that you believe helps, and prove or disprove it with the harness.

## Stage 6: Production (weeks 11 to 12)

Read [LLM app architecture](../../build/patterns/llm-app-architecture.md), [Cost and latency control](../../build/patterns/cost-and-latency-control.md) and [LLMOps and observability](../../build/patterns/llmops-observability.md). Look at the [LLM observability comparison](../../tools/comparisons/llm-observability.md) and the [GenAI platforms comparison](../../tools/comparisons/genai-platforms.md). Read [Guardrails and safety](../concepts/guardrails-and-safety.md) and the [OWASP LLM Top 10](../../safety/security/owasp-llm-top-10.md).

The production concerns are the ones every other software system has, plus a few new ones: model versions get deprecated, outputs drift when a provider updates a model, a single user can run up a large bill, and costs scale with the length of conversations, not just their number. [Inference economics](../../explainers/compute/inference-economics.md) explains where the cost comes from.

**Project:** deploy one of your earlier projects behind an API with authentication, rate limiting per user, logging of tokens, cost and latency per request, and a dashboard. Run your eval suite in CI.

## What employers look for

AI engineer job descriptions vary, but most ask for some version of the same core: production experience with LLM APIs, retrieval systems, agent or tool-calling work, evaluation, and the usual backend skills (APIs, databases, cloud, CI/CD). The [AI careers map](../../careers/roles/ai-careers-map.md) and [AI engineer roadmap](../../careers/roles/ai-engineer-roadmap.md) go deeper, and the [AI engineer interview](../../careers/interviews/ai-engineer-interview.md) and [AI system design interview](../../careers/interviews/ai-system-design-interview.md) guides cover what you will be asked.

For portfolio projects, write a short README for each that states the problem, the design, the eval set, the score, and what you would do next. That README is what a hiring manager reads.

If you want certifications, the [AI certifications guide](../../careers/certifications/ai-certifications-guide.md) lists them, and the sibling site has study guides for the [Anthropic Claude certifications](../../certifications/anthropic/README.md) and [NVIDIA tracks](../../certifications/nvidia/README.md).

## Common mistakes

- **Framework first.** Learning an agent framework before you have written the raw API loop yourself means you cannot debug it. Write it by hand once.
- **No eval set.** Tuning prompts by trying three examples and eyeballing the output. You will make things worse without knowing.
- **Agents for everything.** A fixed pipeline of two model calls is cheaper, faster and easier to test than an agent that decides its own steps. Use agents when the steps genuinely cannot be known in advance.
- **Ignoring cost until the bill.** Log tokens per request from day one. Long conversations and agent loops multiply cost in ways that are invisible in a demo.
- **Trusting tool inputs.** Anything the model reads from outside (web pages, emails, files) can contain instructions. Treat it as untrusted input, like any other.

## Next steps

- Start Stage 1: [Your first LLM API call](../day-one/first-llm-api-call.md)
- [AI engineer roadmap](../../careers/roles/ai-engineer-roadmap.md)
- [Playbook for engineers](../../work/playbooks/for-engineers.md): using AI in your own engineering work
- [ML engineer path](ml-engineer-path.md) if you want to go below the API

## Sources

- Anthropic, "Building Effective Agents" (December 2024): https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, "Prompt caching" documentation: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- OpenAI, Structured Outputs guide: https://developers.openai.com/api/docs/guides/structured-outputs
- Hsieh et al., "RULER: What's the Real Context Size of Your Long-Context Language Models?" (2024): https://arxiv.org/abs/2404.06654
- Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (2023): https://arxiv.org/abs/2306.05685
- OWASP Top 10 for LLM Applications: https://genai.owasp.org/llm-top-10/
