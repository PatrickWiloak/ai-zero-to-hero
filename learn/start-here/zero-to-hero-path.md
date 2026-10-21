# The AI Zero to Hero Path

**In one line:** A seven-phase route from "I have used a chatbot" to "I can build, judge and ship AI systems", with time estimates, a hands-on checkpoint for each phase, and links to the exact pages to read along the way.
**Last reviewed:** 2026-10-21

---

## The short version

- You do not need a maths degree, and you do not need to train a model from scratch, to be useful with AI. Most AI work today is **using** models well: prompting them, feeding them the right context, giving them tools, measuring them, and running them in production without surprises.
- The path has seven phases. Phases 0 to 2 (about 2 to 3 weeks part time) make you a confident, informed user who can call a model from code. Phases 3 to 5 (about 6 to 8 weeks) make you someone who can build real applications. Phase 6 is ongoing: specialise.
- Each phase ends with a **checkpoint**: something concrete you can do. If you can do it, move on. If you cannot, the phase is not done, however many pages you have read.
- Build something small at the end of every phase. Reading about retrieval is not the same as watching your own retrieval return the wrong paragraph.
- If you are not technical and never plan to write code, do Phase 0 and Phase 1, then go to [AI for everyone](ai-for-everyone.md) or [AI for leaders](ai-for-leaders.md). That is a complete path, not a lesser one.

## How to use this page

Treat this as a map, not a syllabus. The time estimates assume about 5 to 8 hours a week, the pace of someone with a job. If you can study full time, divide them by three. If a phase covers something you already know, skim the checkpoint: if you can do it, skip ahead.

The phases are ordered so that each one explains the next. Embeddings make no sense until you know what a model sees; agents make no sense until you have called a model with a tool; evaluation makes no sense until you have built something that sometimes fails. You can jump around, but if a later page feels like jargon soup, the fix is usually one phase back.

Three kinds of pages on this site feed the path:

- **Guides** (the `learn/`, `build/`, `tools/`, `safety/`, `work/` and `careers/` sections) teach you to do something.
- **Explainers** describe how part of the field works, such as [tokenization](../../explainers/concepts/tokenization.md) or [reasoning models](../../explainers/concepts/reasoning-models.md).
- **Paper summaries** are the evidence: plain-language walk-throughs of the research the whole field rests on. You do not need to read papers to follow this path, but each phase names one or two that are worth your time once the ideas click.

## Phase 0: Orientation (2 to 4 hours)

**Goal:** know what the words mean and use a modern assistant well.

Most people start using AI by typing into a chat window and judging the result by vibes. That is a fine start. This phase turns it into an informed habit. Read [What is machine learning?](../concepts/what-is-machine-learning.md) for the big picture: a model is a function whose behaviour is learned from examples rather than written by hand. Then read [Neural networks in plain English](../concepts/neural-networks-plain-english.md), which explains weights, training and inference without calculus.

Then pick one assistant and use it seriously for a week. [Pick a chat assistant](../day-one/pick-a-chat-assistant.md) compares the main options. Use it for real tasks: summarising a long document, drafting an email you would actually send, explaining an error message, planning a trip. Notice where it is excellent and where it is confidently wrong.

That second observation leads straight to [Hallucinations](../concepts/hallucinations.md), the single most important idea for any AI user. Models produce fluent text whether or not it is true, and there are specific, learnable reasons why.

**Checkpoint:** you can explain to a friend, in two minutes and without the word "magic", what happens when you send a message to a chatbot, and you can name two kinds of task where you would not trust the answer without checking it.

## Phase 1: How language models work (1 week)

**Goal:** a working mental model of a large language model (LLM).

An LLM is a neural network trained to predict the next token (a chunk of text) given everything before it. That one sentence explains an enormous amount: why models are fluent, why they can be wrong, why they have context limits, and why they cost what they cost. Read, in order:

1. [LLM basics](../concepts/llm-basics.md): pretraining, instruction tuning, and what "parameters" are.
2. [Tokenization](../../explainers/concepts/tokenization.md): what the model actually reads, and why everything is priced in tokens.
3. [Transformer architecture](../concepts/transformer-architecture.md): the 2017 design almost every model still uses. Pair it with the [Attention Is All You Need summary](../../papers/architectures/01-attention-is-all-you-need/summary.md).
4. [Context windows](../../explainers/concepts/context-windows.md) and [sampling and decoding](../../explainers/concepts/sampling-and-decoding.md): how much the model can see at once, and what temperature actually does.
5. [Reasoning models](../../explainers/concepts/reasoning-models.md): why some models "think" before answering and when that is worth paying for.

If you want the story of how we got here, the [timeline of AI](../../explainers/history/timeline-of-ai.md) is a good evening's read, and the [GPT-3 summary](../../papers/language-models/04-gpt3-few-shot-learners/summary.md) and [InstructGPT summary](../../papers/language-models/05-instructgpt-rlhf/summary.md) explain the two jumps that made chat assistants possible: scale, then training on human feedback.

**Checkpoint:** you can read a model provider's pricing page and turn "$X per million input tokens" into "this task costs about Y cents", and you can explain why asking a model to count the letters in a word is harder than it looks.

## Phase 2: Your first code (1 to 2 weeks)

**Goal:** call a model from a program, safely.

This is where you cross from user to builder. If you have never programmed, budget the full two weeks and start with [Python for AI](../day-one/python-for-ai.md), which teaches only the Python you need for this path. Then work through the rest of the day-one set in order:

1. [Notebooks and Colab](../day-one/notebooks-and-colab.md): a place to run code with nothing to install.
2. [API keys and environment variables](../day-one/api-keys-and-env-vars.md): how to hold a secret without leaking it. Do not skip this one; leaked keys cost real money.
3. [Your first LLM API call](../day-one/first-llm-api-call.md): the same request with the Anthropic SDK, the OpenAI SDK and raw curl.
4. [Run a model locally](../day-one/run-a-model-locally.md): an open-weight model on your own laptop, free and private.

Then learn to ask well. [Prompt engineering](../concepts/prompt-engineering.md) covers system prompts, examples, and asking for a format, and [structured outputs](../concepts/structured-outputs.md) shows how to get JSON you can parse instead of prose you have to scrape.

**Build:** a 30-line script that reads a text file, sends it to a model with a clear instruction ("summarise this for a busy manager in five bullets"), and prints the result. Then add one improvement: stream the output, or count the tokens and print the cost, or run it against a local model too. [Chatbot in an afternoon](../../build/projects/chatbot-in-an-afternoon.md) is a guided version.

**Checkpoint:** you can write, from memory or close to it, a program that sends a prompt to a hosted model and prints the answer, with the key read from an environment variable and never pasted into the code.

## Phase 3: Context, retrieval and embeddings (2 weeks)

**Goal:** give a model knowledge it was not trained on.

A model knows what was in its training data, up to its cutoff date, and nothing about your company handbook. The fix is to put the relevant text into the prompt at question time. Doing that at scale is **retrieval-augmented generation (RAG)**, and it is the most common pattern in industry AI.

Read [Embeddings and vector search](../concepts/embeddings-and-vector-search.md) first: an embedding turns text into a list of numbers so that similar meanings land close together. Then [RAG explained](../concepts/rag-explained.md), and the original [RAG paper summary](../../papers/techniques/13-rag/summary.md) and [dense retrieval summary](../../papers/techniques/87-dense-retrieval/summary.md) if you want the research. [Fine-tuning vs RAG](../concepts/fine-tuning-vs-rag.md) answers the question everyone asks next, and [context windows and management](../concepts/context-windows-and-management.md) explains when you do not need retrieval at all because the documents fit in the prompt.

**Build:** [Build a RAG pipeline](../../build/projects/build-rag-pipeline.md). Index one long PDF, ask ten questions, and look at which chunks came back for each. You will learn more from the bad retrievals than from the good answers. When you are ready to choose a database, [vector database decision](../../tools/decisions/vector-database.md) helps.

**Checkpoint:** you can explain why your RAG system gave a wrong answer to a specific question, and say whether the fault was in chunking, retrieval or generation.

## Phase 4: Tools and agents (2 weeks)

**Goal:** let a model take actions, and know when not to.

Tool use (also called function calling) is the step that turns a model from a writer into a worker. You describe functions to the model; it replies with a request to call one; your code runs it and sends the result back. Repeat that in a loop and you have an **agent**.

Read [Tool use and function calling](../concepts/tool-use-and-function-calling.md), then [Agents explained](../concepts/agents-explained.md) and [Agentic loops](../concepts/agentic-loops.md). [MCP explained](../concepts/mcp-explained.md) covers the Model Context Protocol, the open standard for plugging tools into models, and [agent protocols](../../explainers/ecosystem/agent-protocols.md) puts it in context. For the research lineage, the [ReAct summary](../../papers/techniques/21-react/summary.md), the [Toolformer summary](../../papers/techniques/24-toolformer/summary.md) and Anthropic's [Building Effective Agents essay summary](../../papers/essays/115-building-effective-agents/summary.md) are the three to read. The last one is the most practical: most problems that look like they need an agent are better solved with a fixed workflow.

Agents also open a new class of security problem. Read [Prompt injection explained](../../safety/security/prompt-injection-explained.md) now, before you give anything write access.

**Build:** [Build a Claude agent with MCP](../../build/projects/build-claude-agent-with-mcp.md). Give it two tools, ask it to do a small research task, and log every model call. Count them, and add up the tokens. The number will surprise you.

**Checkpoint:** you can sketch an agent for a task on a whiteboard, estimate how many model calls it makes and what it costs per run, and point at the tool that would do the most damage if an attacker controlled its input.

## Phase 5: Evaluate, secure and ship (2 to 3 weeks)

**Goal:** turn a demo into something you can run for real users.

Everything up to here produces demos. The gap between a demo and a product is measurement and operations. Start with [Evals for LLMs](../concepts/evals-for-llms.md): a small set of real inputs with known good properties, run automatically, so that every prompt or model change is a measured decision instead of a guess. The [LLM-as-a-judge summary](../../papers/techniques/85-llm-as-judge/summary.md) explains when one model can grade another, and the [benchmark contamination explainer](../../explainers/benchmarks/contamination-and-saturation.md) explains why public leaderboards are not a substitute for your own tests.

Then safety: [Guardrails and safety](../concepts/guardrails-and-safety.md), the [OWASP LLM Top 10](../../safety/security/owasp-llm-top-10.md), and [Prompt injection defense](../../safety/security/prompt-injection-defense.md). Then operations: [Prompt caching](../concepts/prompt-caching.md), [Cost and latency control](../../build/patterns/cost-and-latency-control.md) and [LLMOps and observability](../../build/patterns/llmops-observability.md).

**Build:** [Set up an eval harness](../../build/projects/set-up-eval-harness.md) for the RAG or agent project from earlier. Twenty test cases is enough to start. Change the prompt, rerun, and see whether the score moved. Then add logging of tokens, cost and latency per request.

**Checkpoint:** for one thing you have built, you can show a number that says how good it is, a number that says what it costs per user per day, and a list of the failure cases you know about.

## Phase 6: Specialise (ongoing)

By now you have the shared foundation. Where you go next depends on what you want to do:

| You want to... | Go to | Then |
|---|---|---|
| Build AI features into products | [AI engineer path](ai-engineer-path.md) | [AI engineer roadmap](../../careers/roles/ai-engineer-roadmap.md) |
| Train, fine-tune and serve models | [ML engineer path](ml-engineer-path.md) | [Fine-tune with LoRA](../../build/projects/fine-tune-with-lora.md) |
| Understand the research frontier | [Researcher path](researcher-path.md) | [docs/ROADMAP.md](../../docs/ROADMAP.md) |
| Roll AI out across a team | [AI adoption playbook](../../work/enablement/ai-adoption-playbook.md) | [Measuring AI ROI](../../work/enablement/measuring-ai-roi.md) |
| Lead or govern AI in an organisation | [AI for leaders](ai-for-leaders.md) | [AI governance program](../../safety/governance/ai-governance-program.md) |
| Get certified | [AI certifications guide](../../careers/certifications/ai-certifications-guide.md) | [Anthropic certification guides](../../certifications/anthropic/README.md) or [NVIDIA tracks](../../certifications/nvidia/README.md) |

## A realistic schedule

At 5 to 8 hours a week:

| Weeks | Phase | You can now... |
|---|---|---|
| 1 | 0 and 1 | Use assistants critically; explain tokens, context and hallucination |
| 2 to 3 | 2 | Call any major model from Python; run one locally |
| 4 to 5 | 3 | Build question answering over your own documents |
| 6 to 7 | 4 | Build a small agent with tools and estimate its cost |
| 8 to 10 | 5 | Measure quality, defend against injection, log cost and latency |
| 11+ | 6 | Go deep in one direction |

Ten weeks is not long to go from zero to building evaluated, tool-using AI applications. It is enough because you are standing on models that other people spent hundreds of millions of dollars training. Your job is to learn to use them well.

## Common mistakes

- **Reading without building.** If you finish a phase without having written and run code (from Phase 2 on), you have not finished it. The checkpoints are written to be impossible to pass from reading alone.
- **Starting with the maths.** Linear algebra and backpropagation are worth learning eventually, especially on the ML engineer or researcher paths, but they are not a prerequisite for building with models. Start with the system; add the theory when you hit a question it answers.
- **Chasing every release.** New models arrive monthly. If you rewrite your learning plan every time, you never finish one. The foundations in Phases 1 to 5 have been stable for years; new models make them more useful, not obsolete.
- **Jumping to agents.** Agents are exciting and expensive. Most real problems are solved by one good prompt, a retrieval step, or a short fixed workflow. Learn those first so you can tell when an agent is actually needed.
- **Skipping evaluation.** "It worked when I tried it" is how every broken AI feature shipped. If you take one habit from this path, make it writing down test cases before you change a prompt.

## Next steps

- Start Phase 0: [What is machine learning?](../concepts/what-is-machine-learning.md)
- Not technical? [AI for everyone](ai-for-everyone.md)
- Already a developer? Skim Phases 0 and 1, then start at [Your first LLM API call](../day-one/first-llm-api-call.md)
- The paper-first route: [docs/ROADMAP.md](../../docs/ROADMAP.md) and the [glossary](../../docs/GLOSSARY.md)

## Sources

- This path is adapted and expanded from the AI From Scratch path on the original combined Zero to Hero site, before it split into the four subject sites on 2026-10-21.
- Vaswani et al., "Attention Is All You Need" (2017): https://arxiv.org/abs/1706.03762
- Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (2020): https://arxiv.org/abs/2005.11401
- Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models" (2022): https://arxiv.org/abs/2210.03629
- Anthropic, "Building Effective Agents" (December 2024): https://www.anthropic.com/engineering/building-effective-agents
- Model Context Protocol documentation: https://modelcontextprotocol.io/
