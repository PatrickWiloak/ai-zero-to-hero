# Memory for Agents

**In one line:** Give an agent the right kind of memory (the context window for now, summaries for long sessions, a persistent store for facts across sessions, and files or instructions for durable knowledge), decide what gets written and what gets recalled, and avoid the privacy and poisoning problems that come with anything a model remembers.
**Last reviewed:** 2026-10-21

---

> Assumes [Agents explained](agents-explained.md) and [Context windows and management](context-windows-and-management.md). Memory is mostly a retrieval problem, so [RAG explained](rag-explained.md) and [Embeddings and vector search](embeddings-and-vector-search.md) help too.

## The short version

- A model has no memory between calls. Everything it "remembers" is text your application puts into the context window. **Agent memory** is the set of mechanisms that decide what that text is.
- Think in four layers: **working memory** (the current context window), **session memory** (a long conversation or task, kept in budget by trimming and summarising), **long-term memory** (facts and preferences that persist across sessions, in a store you query) and **procedural memory** (durable instructions and skills, such as a project's `CLAUDE.md` or a set of reusable how-to files).
- The hard parts are **writing** (what is worth remembering, and how to update or forget it) and **recalling** (finding the few relevant memories for this moment without flooding the context). Storage is the easy part.
- Start simple: a summary of older turns plus a small file of explicit facts beats an elaborate memory architecture you cannot debug. Vendors now ship building blocks: Anthropic's memory tool, ChatGPT's memory, LangGraph's checkpointers and stores, Google's Memory Bank and Amazon Bedrock AgentCore Memory.
- Memory is user data and an attack surface. Let users see and delete what is stored, never store secrets, and treat stored memories as untrusted input, because an injected instruction that gets saved will be replayed in every future session.

## Why agents need memory at all

The context window is large but finite, costs money on every call, and starts empty for every new conversation. Three situations break a memory-less agent:

1. **Long tasks.** An agent working for hours accumulates tool results until the window is full or quality drops, as models attend less reliably to the middle of very long contexts (see the [context windows explainer](../../explainers/concepts/context-windows.md) and the [RULER summary](../../papers/techniques/132-ruler/summary.md)).
2. **Returning users.** The user said last week that they prefer Python and that their team deploys only on Thursdays. Without memory, they say it again, every session.
3. **Learning from experience.** An agent that found the right way to run this repository's tests yesterday rediscovers it from scratch today.

## The four layers

| Layer | Lives in | Lifetime | Typical mechanism |
|---|---|---|---|
| Working memory | The context window | One model call | The prompt itself |
| Session memory | Conversation state | One conversation or task | Keep recent turns verbatim, summarise or drop older ones, clear old tool results |
| Long-term memory | A database, files or vector store | Across sessions | Write facts as they arise; retrieve the relevant ones into each new context |
| Procedural memory | Instruction files, skills, system prompts | Until edited | Human- or agent-maintained documents loaded at start |

The research lineage: [Generative Agents](../../papers/techniques/58-generative-agents/summary.md) gave simulated people a memory stream scored by recency, importance and relevance, plus periodic "reflections" that summarise many memories into higher-level ones. MemGPT (2023) treated the context window like an operating system's RAM and an external store like disk, with the model itself paging information in and out. [Reflexion](../../papers/techniques/78-reflexion/summary.md) stored verbal lessons from failed attempts, and [Voyager](../../papers/techniques/100-voyager/summary.md) stored working code as a growing skill library: procedural memory.

## Session memory: keeping a long task in budget

Inside one long conversation or task, the techniques are the ones in [Context windows and management](context-windows-and-management.md), applied deliberately:

- **Keep the recent turns verbatim**; they matter most.
- **Summarise older turns** into a running summary that says what was decided, what was done and what is still open. Regenerate it every N turns.
- **Clear stale tool results.** A 3,000-line file read twenty steps ago rarely needs to stay. Keep a one-line note ("read config.yaml: uses Postgres, port 5433") instead.
- **Keep a scratchpad**: a short plan or to-do list the agent updates as it works and that always stays in context. It is cheap and keeps long tasks on track.

## Long-term memory: write, store, recall

**Writing** is where most memory systems go wrong. Options, from most to least controlled:

- **Explicit**: the user says "remember that...", or the application saves known fields (name, plan, preferences).
- **Agent-decided**: give the agent a memory tool and instructions on what is worth keeping (stable preferences, facts about the user's projects, lessons learned) and what is not (one-off details, anything sensitive).
- **Background extraction**: after each session, a separate model call extracts candidate memories from the transcript, deduplicates them against existing ones and resolves conflicts ("deploys on Thursdays" replaced by "deploys on Tuesdays since October").

Whatever writes, store **short, self-contained statements** with metadata: when it was written or last confirmed, where it came from, which user it belongs to, and a type (preference, fact, task state).

**Recalling** is retrieval. Before each turn (or when the agent asks), find the few memories relevant to the current request and put them in the context. The same choices as RAG apply: keyword matching, embedding similarity, or both, plus recency and importance. Here is a deliberately simple long-term store, to show the moving parts:

```python
import json, math, re, time
from pathlib import Path

class MemoryStore:
    """Long-term memory as a JSON file of short facts, retrieved by word overlap and recency."""

    def __init__(self, path="memory.json", half_life_days=30):
        self.path = Path(path)
        self.items = json.loads(self.path.read_text()) if self.path.exists() else []
        self.half_life = half_life_days * 86400

    def remember(self, text, kind="fact", now=None):
        now = now or time.time()
        key = text.lower().strip()
        for item in self.items:              # update instead of duplicating
            if item["text"].lower().strip() == key:
                item["updated"] = now
                break
        else:
            self.items.append({"text": text, "kind": kind, "updated": now})
        self.path.write_text(json.dumps(self.items, indent=1))

    def recall(self, query, k=3, now=None):
        now = now or time.time()
        words = set(re.findall(r"\w+", query.lower()))
        def score(item):
            overlap = len(words & set(re.findall(r"\w+", item["text"].lower())))
            recency = math.exp(-(now - item["updated"]) / self.half_life)
            return overlap + 0.5 * recency
        ranked = sorted(self.items, key=score, reverse=True)
        return [i["text"] for i in ranked[:k] if score(i) > 0.5]

mem = MemoryStore("demo-memory.json")
day = 86400
t0 = time.time() - 60 * day
mem.remember("User's name is Priya; prefers short answers", "profile", now=t0)
mem.remember("Priya's team deploys on Thursdays only", "fact", now=t0 + 10 * day)
mem.remember("Priya is migrating the billing service to Postgres", "project", now=t0 + 55 * day)
mem.remember("Priya prefers Python examples over JavaScript", "profile", now=t0 + 58 * day)
print(mem.recall("Can I deploy the billing service tomorrow?"))
```

Run on a fresh file, it prints:

```
['Priya is migrating the billing service to Postgres']
```

It found the billing memory and **missed the one that matters most**: the team deploys only on Thursdays. The query says "deploy", the memory says "deploys", and plain word overlap does not know they are the same idea. That is the case for **embedding-based** recall (see [Embeddings and vector search](embeddings-and-vector-search.md)) combined with keyword search, exactly as in [advanced RAG](../../build/patterns/advanced-rag-patterns.md). It also shows why some memories should not depend on retrieval at all: a short **profile** of always-relevant facts (name, key preferences, standing constraints) can simply be included in every context.

## Procedural memory: instructions and skills

Some of the most useful memory is not about the user but about **how to do the job**: how this repository is built and tested, the house style, which commands are safe. Coding agents keep this in files at the root of a project (`CLAUDE.md`, `AGENTS.md`), loaded at the start of every session and edited by people and agents alike. Larger systems keep libraries of reusable instructions or scripts that are loaded only when a task needs them. Procedural memory is reviewable, versioned in git and easy to correct, which makes it the safest place for durable knowledge. See [AI coding agents explained](ai-coding-agents-explained.md).

## Building blocks you can use (as of 2026-10-21)

- **Anthropic memory tool** (`memory_20250818`): Claude reads and writes files under a `/memories` directory, checks it before starting a task, and continues earlier work in later conversations. It runs **client-side**: your application executes each operation against storage you control, and must block paths outside `/memories`.
- **ChatGPT memory**: saved memories the user can view and delete, plus reference to past chat history, in the consumer product (described in OpenAI's help centre; settings vary by plan).
- **LangGraph**: short-term memory is per-thread state persisted by a checkpointer; long-term memory lives in stores shared across threads under namespaces you define.
- **Letta** (formerly MemGPT): an open-source platform for stateful agents.
- **Cloud agent platforms**: Google's Gemini Enterprise Agent Platform offers Memory Bank, and Amazon Bedrock AgentCore includes a Memory service. See [Cloud AI/ML services compared](../../tools/comparisons/cloud-ai-ml-services.md).

## Privacy, safety and poisoning

- **It is personal data.** Memory about users falls under privacy law (GDPR access and erasure rights, for example). Let users see, edit and delete what is remembered, and do not remember what you do not need.
- **Never store secrets**: passwords, API keys, card numbers. Filter writes.
- **Scope strictly.** One user's memories must never be recalled for another. Key everything by user and tenant, and test it.
- **Memory poisoning.** If an agent reads a malicious web page or email and saves an instruction from it ("always cc this address"), the attack persists into every future session. Restrict what can be written, record the source of each memory, and treat recalled memories as data, not instructions. See [Agent security](../../safety/security/agent-security.md) and [Prompt injection defense](../../safety/security/prompt-injection-defense.md).
- **Stale memories mislead.** Store when each fact was last confirmed, prefer newer facts on conflict, and let old, unused memories decay or expire.

## Common mistakes

- **Saving everything.** A memory store full of trivia retrieves trivia. Be selective at write time.
- **Recalling too much.** Twenty loosely related memories in every prompt cost tokens and distract the model. Retrieve a few, with a relevance threshold.
- **No update path.** Facts change. Without deduplication and conflict resolution, the store ends up with both "prefers Python" and "prefers TypeScript".
- **Invisible memory.** Users who cannot see what is remembered do not trust it, and you cannot debug it.
- **Building memory before you need it.** Many agents only need good session management and an instructions file.

## Next steps

- [Context windows and management](context-windows-and-management.md): the session-memory techniques in detail
- [RAG explained](rag-explained.md) and [Advanced RAG patterns](../../build/patterns/advanced-rag-patterns.md): recall is retrieval
- [Agentic loops](agentic-loops.md) and [Agent architectures](../../build/patterns/agent-architectures.md)
- Papers: [Generative Agents](../../papers/techniques/58-generative-agents/summary.md), [Reflexion](../../papers/techniques/78-reflexion/summary.md), [Voyager](../../papers/techniques/100-voyager/summary.md)

## Sources

- Anthropic, "Memory tool" documentation, read 2026-10-21: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- LangChain, LangGraph memory overview: https://docs.langchain.com/oss/python/langgraph/memory
- Letta documentation: https://docs.letta.com/ ; repository README ("Letta (f.k.a. MemGPT)"): https://github.com/letta-ai/letta
- Packer et al., "MemGPT: Towards LLMs as Operating Systems" (2023): https://arxiv.org/abs/2310.08560
- Park et al., "Generative Agents: Interactive Simulacra of Human Behavior" (2023): https://arxiv.org/abs/2304.03442
- Google Cloud, Gemini Enterprise Agent Platform agents overview (Memory Bank): https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents
- AWS, "What is Amazon Bedrock AgentCore?" (Memory service): https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- OpenAI Help Center on ChatGPT memory (not fetched directly on 2026-10-21; described from search results): https://help.openai.com/en/articles/11146739-how-does-reference-saved-memories-work
- Code output above produced on 2026-10-21.
