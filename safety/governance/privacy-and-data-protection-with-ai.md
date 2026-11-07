# Privacy and Data Protection with AI

**In one line:** Know what personal data goes into an AI system, where it goes, who keeps it and for how long, then minimise it, mask it, contract for it and log it, because privacy failures with AI mostly come from careless inputs, not clever attacks.
**Last reviewed:** 2026-11-07

---

> Judgment guide, not legal advice. Privacy law varies by country, state and sector. Talk to your privacy officer or counsel.

## The short version

- Start with a **data map**: what personal data enters prompts, retrieval stores, logs, fine-tuning sets and outputs.
- **Minimise first.** The safest personal data is data you never sent. Remove names, IDs and free-text details the task does not need.
- **Check the vendor terms**: is your data retained, who can see it, is it used for training, where is it stored, which subprocessors touch it. Consumer apps and enterprise APIs often differ; read the actual terms.
- **Mask before sending** where you can. Managed tools exist: Amazon Bedrock Guardrails sensitive information filters can block or mask PII (SSN, date of birth, address and custom regex patterns, per the Guardrails overview page) in inputs and model responses; detection is probabilistic, so it reduces risk and does not remove it. (AWS docs, read 2026-11-07)
- Sector rules still apply: health data, student records and financial data have their own laws. See [healthcare](../../work/use-cases/healthcare-ai.md), [education](../../work/use-cases/education-ai.md) and [finance](../../work/playbooks/for-finance.md).

## Where personal data leaks in AI systems

| Place | Risk | Control |
|---|---|---|
| Prompts | Staff paste customer or employee data into unapproved tools | Approved tools, an [acceptable use policy](../../work/enablement/acceptable-use-policy.md), training |
| Logs and traces | Prompts and outputs stored for debugging, kept forever | Redact before logging, short retention, access controls |
| Retrieval stores | Documents indexed without access control; a user retrieves another person's data | Per-user filters on every query |
| Fine-tuning data | Personal data baked into model weights | Scrub, document lawful basis, avoid when RAG suffices |
| Outputs | Model reveals data from the prompt or context | Output filters, tests. OWASP lists sensitive information disclosure as LLM02 in its 2025 Top 10 (read 2026-11-07) |
| Vendors | Subprocessors, regions, retention | Contracts, data-processing terms, vendor review |

## A practical program

1. **Inventory** every AI use that touches personal data.
2. **Assess** risk before launch. For high-risk uses, do a formal impact assessment. See [AI risk assessment](ai-risk-assessment.md).
3. **Decide the basis**: consent, contract, legitimate interest or whichever your law requires. This needs counsel; this page does not decide it.
4. **Set retention** for prompts, outputs and embeddings, and honour deletion requests (embeddings and fine-tuned weights are the hard cases).
5. **Be transparent**: tell people when AI processes their data or talks to them.
6. **Train staff** on what not to paste.
7. **Prepare for incidents**: a leak into a prompt log is a data incident. See [AI incident response](../security/ai-incident-response.md).

## Frameworks to lean on

The NIST Privacy Framework is a voluntary tool to identify and manage privacy risk; its page links Version 1.0 and shows a PF 1.1 initial public draft (publication date not stated on the page). NIST also published the AI RMF in January 2023 and a Generative AI Profile (AI 600-1) in July 2024. See [NIST AI RMF](nist-ai-rmf.md). The European Data Protection Board adopted Opinion 28/2024 on AI models on 18 December 2024: whether a model is anonymous is judged case by case; legitimate interest as a legal basis for developing or deploying AI needs a three-step test; and unlawfully processed training data can affect whether the model can lawfully be deployed unless it was properly anonymised ([EDPB news item](https://www.edpb.europa.eu/news/news/2024/edpb-opinion-ai-models-gdpr-principles-support-responsible-ai_en), fetched 2026-11-07). The UK ICO's AI guidance pages returned HTTP 403, so read them directly at ico.org.uk if UK GDPR applies to you.

## Common mistakes

- Treating "we use an API" as meaning "no data is kept". Read the terms.
- Putting personal data in embeddings and assuming it is anonymous.
- Logging full prompts forever.
- Having no way to delete a person's data from the AI stack.

## Next steps

- [AI governance program](ai-governance-program.md)
- [Guardrails architecture](../../build/patterns/guardrails-architecture.md)
- [Responsible AI basics](responsible-ai-basics.md)

## Sources

- Amazon Bedrock Guardrails: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html (fetched 2026-11-07)
- OWASP GenAI LLM Top 10: https://genai.owasp.org/llm-top-10/ (fetched 2026-11-07)
- EDPB, Opinion 28/2024: https://www.edpb.europa.eu/news/news/2024/edpb-opinion-ai-models-gdpr-principles-support-responsible-ai_en (fetched 2026-11-07)
- NIST Privacy Framework: https://www.nist.gov/privacy-framework (fetched 2026-11-07)
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework (fetched 2026-11-07)
