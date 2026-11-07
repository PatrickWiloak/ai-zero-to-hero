# Build an AI Portfolio

**In one line:** Choose three or four projects that show different skills, present each with a clear README, numbers and an honest limitations section, and link to hands-on projects on this site to start.
**Last reviewed:** 2026-11-07

---

## The short version

- A portfolio is evidence that you can finish things. Three or four good projects beat ten half-built ones.
- Cover different skills: one that retrieves, one that evaluates, one that ships, and one that shows judgment about risk.
- Every project needs a README that says what it does, how it was measured, what failed and what it costs to run.
- This is judgment from this site's editors. No hiring-survey data is cited.

## What to build

| Project type | Starting point here | What it proves |
|---|---|---|
| RAG over real documents | [Build a RAG pipeline](../../build/projects/build-rag-pipeline.md) | Retrieval, chunking, citations |
| Structured extraction | [Structured extraction pipeline](../../build/projects/structured-extraction-pipeline.md) | Schemas, validation, error handling |
| Agent with tools | [Claude agent with MCP](../../build/projects/build-claude-agent-with-mcp.md), [coding agent loop](../../build/projects/build-a-coding-agent-loop.md) | Tool use, loops, limits |
| Evaluation | [Set up an eval harness](../../build/projects/set-up-eval-harness.md), [evaluate an agent end to end](../../build/projects/evaluate-an-agent-end-to-end.md) | Measuring quality |
| Classical ML | [Tabular ML end to end](../../build/projects/tabular-ml-end-to-end.md), [deploy an ML model](../../build/projects/deploy-ml-model.md) | Baselines, deployment |
| Fine-tuning and serving | [Fine-tune with LoRA](../../build/projects/fine-tune-with-lora.md), [Llama on one GPU](../../build/projects/run-llama-on-single-gpu.md) | Training and inference |
| Security | [Prompt injection red team](../../build/projects/prompt-injection-red-team.md) | Risk awareness |
| Voice or chat product | [Voice agent](../../build/projects/voice-agent.md), [chatbot in an afternoon](../../build/projects/chatbot-in-an-afternoon.md) | Product thinking |

Do not publish an unchanged tutorial result as your own. Change the data, the question or the evaluation so the work is clearly yours.

## How to present each project

1. **One-line summary and a screenshot or short demo.**
2. **Problem and users.** Who needs this and why.
3. **Design.** One diagram, the main choices and the alternatives you rejected.
4. **Results.** Numbers from an eval set you built, compared with a simple baseline. Say how large the set was.
5. **Failures and limits.** What it gets wrong, with examples. This is where reviewers learn to trust you.
6. **Cost and latency.** What one task costs and how long it takes.
7. **How to run it.** One command, a `.env.example`, and no committed secrets.

## Make it safe to publish

- Use data you are allowed to share. Never publish an employer's or client's material.
- Keep keys out of git. See [API keys and env vars](../../learn/day-one/api-keys-and-env-vars.md).
- Note any security work you did: [prompt injection defense](../../safety/security/prompt-injection-defense.md), [OWASP LLM Top 10](../../safety/security/owasp-llm-top-10.md).

## Where to put it

A public GitHub repository per project, a short personal page that links to them, and a pinned profile README. Keep it current; remove broken demos.

## Match the portfolio to the role

- [AI engineer](ai-engineer-roadmap.md): RAG, agent, eval, plus one deployed app.
- [ML engineer](ml-engineer-roadmap.md): tabular model, deployed model, fine-tune.
- [Data scientist](data-scientist-in-the-llm-era.md): extraction plus a statistical analysis with honest uncertainty.
- [AI product manager](ai-product-manager.md): a spec, an eval you built and a working prototype.
- [Researcher](ai-researcher-path.md): a reproduction with a write-up.

## Common mistakes

- Only chatbot wrappers with no evaluation.
- No baseline, so nobody can tell if the AI helped.
- Hiding failures. Reviewers find them anyway.
- Demos that die because an API key expired.

## Next steps

- Practise explaining a project with the [AI engineer interview](../interviews/ai-engineer-interview.md) and [AI system design interview](../interviews/ai-system-design-interview.md).
- [AI certifications guide](../certifications/ai-certifications-guide.md) for when a credential adds to a portfolio.

## Sources

- Judgment: what to include is editorial, based on the projects on this site.
- Project pages linked above hold the runnable detail.
