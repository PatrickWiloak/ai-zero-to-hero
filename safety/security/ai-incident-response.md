# AI Incident Response

**In one line:** Prepare for AI failures the way you prepare for security incidents: define what counts as an incident, who decides, how to stop the system fast, how to investigate prompts and model behaviour, who must be told, and what you change afterwards.
**Last reviewed:** 2026-11-07

---

## The short version

- AI incidents are wider than breaches: a chatbot gives harmful advice, an agent takes a wrong action, a model leaks data, outputs show bias, a deepfake impersonates your executive, or a vendor model changes behaviour overnight.
- You need a **kill switch** before you need a plan: a way to disable a feature, a tool, a model version or an agent's write access in minutes without a deploy.
- Use your existing incident process and extend it. NIST's SP 800-61 Rev. 3 (April 2025) explains how to build incident response into cybersecurity risk management using Cybersecurity Framework 2.0, and supersedes Rev. 2 from 2012. (NIST CSRC, read 2026-11-07)
- Public learning matters: the AI Incident Database, run by the nonprofit Responsible AI Collaborative, indexes real-world harms and near harms from deployed AI systems and accepts submissions. (read 2026-11-07)
- Judgment page: severity levels and notification duties below are suggestions. Legal notification rules (privacy, sector, contract) need counsel.

## What to log so you can investigate

Prompts and outputs (redacted as policy allows), model and version, system prompt and config version, retrieved documents, tool calls and results, user or session ID, guardrail decisions and timestamps. Without these you cannot reconstruct what happened. See [LLMOps and observability](../../build/patterns/llmops-observability.md) and balance with [privacy](../governance/privacy-and-data-protection-with-ai.md).

## The lifecycle

| Phase | AI-specific actions |
|---|---|
| **Prepare** | Inventory AI systems and owners; kill switches; logging; severity scale; on-call; vendor contacts; a tested [runbook](#a-starter-severity-scale) |
| **Detect** | User reports, support tickets, alert on blocked-rate and refusal spikes, eval regressions, sampled review, security monitoring |
| **Contain** | Disable the feature or tool, roll back the prompt or model version, revoke credentials, pause the agent, rate-limit |
| **Investigate** | Reproduce with logged inputs; was it prompt injection, data leak, model change, bad retrieval, bad data, misuse? |
| **Notify** | Internal leadership, legal, affected users, vendors, regulators where required |
| **Recover** | Fix, add the case to your eval set, re-test, restore gradually |
| **Learn** | Blameless review within a week; update guardrails, policy, training; consider sharing a lesson publicly |

## A starter severity scale

| Level | Example | Response |
|---|---|---|
| 1 | Wrong or odd answer, no harm | Log, add to eval set |
| 2 | Harmful or embarrassing output seen by a few users | Fix this week, review |
| 3 | Personal data exposed, or real-world action taken wrongly | Contain now, involve legal and privacy |
| 4 | Safety harm, widespread leak, or regulatory trigger | Executive incident, kill switch, external notifications |

## Practice

Run a tabletop exercise each half year: pick a scenario (agent emailed a customer list to the wrong address; chatbot told a user something dangerous), and walk through who does what. Time how long it takes to disable the feature. Fix whatever blocked you. See also [agent security](agent-security.md) and [LLM red teaming](llm-red-teaming.md).

## Common mistakes

- No way to switch a feature off without a release.
- No logs, so the review is guesswork.
- Treating a "just a bad answer" report as not an incident when it is a pattern.
- Not telling the vendor, who may be able to see it elsewhere.
- Skipping the step of adding the failure to your tests.

## Next steps

- [AI governance program](../governance/ai-governance-program.md)
- [Guardrails architecture](../../build/patterns/guardrails-architecture.md)

## Sources

- NIST SP 800-61 Rev. 3: https://csrc.nist.gov/pubs/sp/800/61/r3/final (fetched 2026-11-07)
- AI Incident Database: https://incidentdatabase.ai/ (fetched 2026-11-07)
