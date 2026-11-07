# Guardrails Architecture

**In one line:** Treat guardrails as layers around the model (input checks, a constrained model, output checks, tool permissions, human approval, monitoring), because no single filter stops every failure and some controls must live outside the prompt.
**Last reviewed:** 2026-11-07

---

## The short version

- A guardrail is any control that limits what an AI system can take in, say or do. The concept page is [guardrails and safety](../../learn/concepts/guardrails-and-safety.md); this page is about how to **arrange** them.
- Put controls at **five points**: before the model (input), in the model call (instructions and structure), after the model (output), around tools (permissions), and across time (monitoring and review).
- **Do not rely on the system prompt alone.** A prompt is an instruction, not an enforcement point. Hard limits belong in code and permissions. See [prompt injection defence](../../safety/security/prompt-injection-defense.md).
- OWASP's 2025 Top 10 for LLM applications lists, among others, prompt injection, sensitive information disclosure, improper output handling, excessive agency and unbounded consumption. Each maps to a layer below. (OWASP GenAI, read 2026-11-07)
- Test guardrails like code: a set of attacks and edge cases that must pass before every release.

## The layers

| Layer | Controls | Example |
|---|---|---|
| **1. Input** | Length limits, topic rules, PII detection or masking, prompt-attack detection, authentication and rate limits | Reject a 200,000-character paste; mask account numbers |
| **2. Model call** | Clear instructions, structured outputs, retrieval limited to what the user may see, low-privilege system identity | JSON schema output; per-user document filters in RAG |
| **3. Output** | Content filters, PII masking, grounding checks against sources, schema validation, refusal handling | Block unsupported claims in a RAG answer |
| **4. Tools and actions** | Allow-lists, scoped credentials, spending caps, read-only by default, **human approval for irreversible actions** | Agent can draft the email, a person sends it |
| **5. Monitoring** | Logging, alerts on blocked-rate spikes, sampled human review, an incident process | Weekly review of blocked and borderline cases |

## What a managed service gives you

Amazon Bedrock Guardrails, per AWS documentation read 2026-11-07, offers: content filters (Hate, Insults, Sexual, Violence, Misconduct, Prompt Attack), denied topics, word filters, sensitive information filters (block or mask PII, plus custom regex), contextual grounding checks to detect hallucinations in RAG, and Automated Reasoning checks against logical rules. It can be attached to a model call or used on its own through an `ApplyGuardrail` API, so it can check text from any model. Other clouds and open-source tools offer similar pieces; those were not fetched for this page.

## Design decisions

1. **Block, mask or warn?** Blocking is safest and most annoying; masking keeps the flow; warning relies on the user.
2. **Fail closed or open?** If a guardrail service is down, decide in advance. Money or safety actions should fail closed.
3. **Latency and cost.** Every check adds a call. See [cost and latency control](cost-and-latency-control.md); run cheap checks first and run independent checks in parallel.
4. **False positives.** Measure what legitimate requests you block, not only what attacks you stop.
5. **Who owns changes?** Treat guardrail configuration as versioned code with review.

## A worked flow

User question to a support bot: (1) input layer strips an account number and checks length; (2) the model answers from retrieved help articles only, in a schema; (3) an output check confirms every claim is grounded in a retrieved passage, otherwise it returns a safe fallback; (4) the bot can look up order status read-only, and refunds go to a person; (5) blocked and low-grounding cases are sampled weekly for review.

## Common mistakes

- One big "safety" prompt as the only layer.
- Guarding input but not output (or the reverse).
- Giving the agent broad credentials "so it works", then relying on a filter.
- Never testing with real attacks. See [LLM red teaming](../../safety/security/llm-red-teaming.md).
- No owner, so the filter drifts from the product.

## Next steps

- [OWASP LLM Top 10](../../safety/security/owasp-llm-top-10.md) and [agent security](../../safety/security/agent-security.md)
- [Multi-agent orchestration](multi-agent-orchestration.md)
- [Set up an eval harness](../projects/set-up-eval-harness.md)

## Sources

- Amazon Bedrock Guardrails user guide: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html (fetched 2026-11-07)
- OWASP GenAI, LLM Top 10: https://genai.owasp.org/llm-top-10/ (fetched 2026-11-07)
- Anthropic, Building effective agents (guardrails, stopping conditions, human checkpoints): https://www.anthropic.com/engineering/building-effective-agents (fetched 2026-11-07)
