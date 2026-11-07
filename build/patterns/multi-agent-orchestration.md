# Multi-Agent Orchestration

**In one line:** Use several cooperating agents only when one agent cannot do the job (parallel breadth, separate tool sets, or context that will not fit); otherwise a single agent or a fixed workflow is cheaper, faster and easier to debug.
**Last reviewed:** 2026-11-07

---

## The short version

- Start with the simplest thing that works. Anthropic's guidance says agents trade latency and cost for better performance, so add complexity only when it clearly improves outcomes. (Building effective agents, read 2026-11-07)
- Multi-agent systems cost a lot more. Anthropic reported that agents use about 4 times the tokens of chat, and multi-agent systems about 15 times, so the approach only pays off on high-value tasks. (Multi-agent research system post, read 2026-11-07)
- They fit **breadth-first work that splits into independent directions** (research, large searches). They fit poorly where agents depend on each other's results, such as most coding tasks, per the same post.
- The most common shape is **orchestrator-worker**: one lead agent plans, workers run in parallel, the lead merges.
- You need evals and tracing before you add agents, or you cannot tell whether the extra agents help. See [evals for LLMs](../../learn/concepts/evals-for-llms.md).

## The patterns

| Pattern | How it works | Use when |
|---|---|---|
| **Prompt chain** | Fixed steps, each feeding the next | Task splits cleanly into stages |
| **Routing** | A classifier sends the input to a specialised handler | Different inputs need different prompts or models |
| **Parallelization** | Run sub-tasks at once (sectioning) or run the same task several times and vote | Speed, or confidence from agreement |
| **Orchestrator-workers** | A lead LLM breaks the task down, delegates, and synthesises | Sub-tasks cannot be known in advance |
| **Evaluator-optimizer** | One model drafts, another critiques, loop | You have clear quality criteria |
| **Handoff / swarm** | An agent passes the conversation to a specialist | Support, triage and escalation flows |

The first five are the workflow patterns named in Anthropic's guide. Handoff is common in agent frameworks; see [agent frameworks compared](../../tools/comparisons/agent-frameworks.md). For single-agent designs, see [agent architectures](agent-architectures.md).

## What worked and failed in a published system

Anthropic's description of its Research feature (read 2026-11-07):

- A lead agent plans and spawns subagents that search in parallel; a separate citation agent attributes claims to sources. The lead saves its plan to memory because context beyond 200,000 tokens is truncated.
- On their internal research eval, a Claude Opus 4 lead with Claude Sonnet 4 subagents beat single-agent Claude Opus 4 by 90.2%. This is one vendor's internal result, not a general law.
- Token use alone explained about 80% of performance variance on the BrowseComp evaluation.
- Early failures: spawning 50 subagents for simple queries, endless searching for sources that did not exist, and agents flooding each other with updates.
- Fixes: detailed task descriptions for each subagent (objective, output format, tool guidance, boundaries), effort-scaling rules written into the prompt, and clear tool descriptions.
- Operations: resume from checkpoints instead of restarting, tell agents when a tool fails, and deploy gradually so running agents are not disrupted.

## Design checklist

1. **Why more than one?** Write the reason (parallel breadth, context separation, different permissions). If you cannot, use one agent.
2. **Contracts**: give every worker a written objective, output format and boundary, and validate what comes back. See [structured outputs](../../learn/concepts/structured-outputs.md).
3. **Budgets**: cap the number of agents, steps and tokens. Add stopping conditions such as a maximum number of iterations.
4. **Least privilege**: workers get only the tools they need. See [agent security](../../safety/security/agent-security.md).
5. **Human checkpoints** for irreversible actions.
6. **Tracing**: log every agent's inputs, tool calls and outputs. See [LLMOps and observability](llmops-observability.md).
7. **Evaluate against a single-agent baseline.** Keep the extra agents only if the numbers justify the cost.

## Common mistakes

- Using many agents because it looks sophisticated.
- Vague delegation ("research this"), producing duplicated work.
- No cap on spawned agents or loops.
- Letting a worker read untrusted content and also hold powerful tools: one prompt injection reaches everything.
- Testing only the final answer, not each agent's step.

## Next steps

- [Agents explained](../../learn/concepts/agents-explained.md) and [agentic loops](../../learn/concepts/agentic-loops.md)
- [Guardrails architecture](guardrails-architecture.md)
- [Evaluate an agent end to end](../projects/evaluate-an-agent-end-to-end.md)

## Sources

- Anthropic, Building effective agents: https://www.anthropic.com/engineering/building-effective-agents (fetched 2026-11-07)
- Anthropic, How we built our multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system (fetched 2026-11-07)
