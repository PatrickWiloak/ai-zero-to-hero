# AI for Support and Operations

**In one line:** Use AI to draft replies from your knowledge base, summarise long tickets and threads, write and update procedures, and triage incoming work - with a human sending every customer-facing answer until you have measured that the AI gets it right.
**Last reviewed:** 2026-10-21

---

## The short version

- Support and operations are among the best-studied places AI helps at work. In a study of customer support agents, an AI assistant raised issues resolved per hour by 14% on average, and by 34% for novice and low-skilled agents.
- Start with **agent assist** (AI drafts, a human sends), not with a fully automated chatbot. It is lower risk and builds the knowledge base you will need anyway.
- Your knowledge base quality is the ceiling. AI drafting from an outdated policy produces confident, outdated answers faster.
- Your company is responsible for what an AI tells customers. A Canadian tribunal held Air Canada liable for a refund policy its chatbot made up.
- In operations, AI is strong at writing and maintaining procedures, summarising incidents, and turning messy inputs (emails, forms) into structured records.

## Support: where it helps

| Task | AI does | Agent does |
|---|---|---|
| Reply drafting | Drafts a reply from the ticket plus relevant help articles | Checks facts and tone, sends |
| Ticket summary | Summarises a 40-message thread for handover | Reads the summary, skims the latest messages |
| Triage | Suggests category, priority, language, sentiment | Confirms or overrides |
| Translation | Drafts replies in the customer's language | Checks with a fluent colleague for sensitive cases |
| Knowledge base | Drafts new articles from resolved tickets | Approves, owns accuracy |
| QA | Flags tickets for review (policy mentions, angry tone) | Reviews |

## Copyable prompts for support

**Reply from policy**
```
You are drafting a reply for a support agent. Use ONLY the policy text below.
If the policy does not answer the question, say "Policy does not cover this"
and suggest what to ask a supervisor. Do not promise refunds, credits or
dates that the policy does not state.

Policy:
[paste relevant help article or policy section]

Customer message:
[paste, with card numbers and passwords removed]

Write a reply under 150 words, warm and direct, that answers the question
and states the next step. Then, separately, list the policy sentences you
relied on.
```

**Thread summary for handover**
```
Summarise this support thread for a colleague taking it over: [paste].
Include: the customer's actual problem in one sentence, what has been tried,
what was promised and by whom, current status, and the next action.
Quote any commitment we made exactly.
```

**Turn resolved tickets into a help article**
```
Here are 5 resolved tickets about the same issue: [paste, anonymised].
Draft a help article: title as the customer would search it, symptoms,
cause (only if stated in the tickets), step-by-step fix, and when to
contact support. Mark anything you are unsure about with [CHECK].
```

## Operations: where it helps

- **Procedures (SOPs).** Turning a recorded walkthrough or rough notes into a numbered procedure; spotting missing steps; keeping versions consistent.
- **Incident and shift handovers.** Summarising a chat channel or log of an incident into timeline, impact, actions and open items.
- **Intake.** Turning emails, forms and PDFs into structured records (vendor requests, purchase orders, onboarding forms). At volume, this becomes a [document processing](../use-cases/document-processing.md) pipeline.
- **Policy questions.** Answering "what's the process for X?" from your own documents, when the tool is connected to them.

**SOP from notes**
```
Turn these notes into a standard operating procedure: [paste notes or
transcript]. Format: Purpose, Scope, Roles, Prerequisites, numbered Steps
(one action per step, who does it), Checks, and What to do if it fails.
List any step that seems missing or ambiguous at the end as questions.
```

**Incident summary**
```
Here is the incident channel export: [paste]. Write a summary with: timeline
(UTC, from the timestamps only), customer impact, root cause if stated
(otherwise "not yet known"), actions taken, and open follow-ups with owners.
Do not speculate on cause.
```

## Before and after

**Before.** A new support agent handles a billing question by searching the help centre, reading three articles, asking a senior colleague in chat, and writing the reply. About 12 minutes, and the senior colleague is interrupted 20 times a day.

**After.** The agent's helpdesk shows an AI draft built from the two most relevant articles, with the policy sentences it used listed underneath. The agent reads both, fixes one sentence, and sends in about 5 minutes. When the draft says "policy does not cover this", the agent escalates. The senior colleague now spends that time updating the articles the AI keeps flagging as gaps.

This mirrors what the research found: the biggest gains went to newer agents, because the AI made the best agents' knowledge available to everyone.

## Moving to automation, carefully

Fully automated answers (a customer-facing chatbot or AI agent) are a bigger step. Klarna announced in February 2024 that its AI assistant was handling two-thirds of its customer service chats in its first month. In May 2025 its CEO said the company would make sure customers can always reach a human, and was investing in the quality of human support, after acknowledging lower quality from the AI-led approach. The lesson is not "never automate" but "measure quality, not just cost, and keep a human path".

Before automating any category of question, check:

1. Agents accept the AI draft with no or minimal edits for that category, measured over weeks.
2. There is a clear, fast route to a human.
3. The AI only answers from approved content and says when it does not know.
4. You tell customers they are talking to an AI.
5. You monitor a sample of conversations every week.

The full method is on [customer support automation](../use-cases/customer-support-automation.md).

## Where not to use it

- Refunds, credits, legal or safety commitments without human approval.
- Vulnerable customers, complaints with legal implications, or regulated advice (financial, medical) without a human.
- Card numbers, passwords or identity documents in any AI tool not approved for them.
- As a replacement for fixing the product problem that causes the tickets.

## Failure modes

- **Policy invention.** The AI produces a plausible policy that does not exist. The "use ONLY the policy" instruction plus listing the sentences relied on makes this easier to catch.
- **Stale knowledge.** Articles out of date means answers out of date. Assign owners and review dates to articles.
- **Tone mismatch.** Cheerful replies to angry customers. Add tone guidance and review.
- **Deskilling.** If new agents only edit drafts, they may not learn the product. Pair AI assist with real training.

## Common mistakes

- Starting with a public chatbot instead of agent assist.
- Measuring handle time only, not resolution, reopen rate and customer satisfaction.
- No feedback loop: agents fix the same AI mistake daily and nobody updates the knowledge base.
- Rolling out without the [acceptable use policy](../enablement/acceptable-use-policy.md) covering customer data.

## Next steps

- Automating support end to end: [customer support automation](../use-cases/customer-support-automation.md)
- Forms, invoices and emails at volume: [document processing](../use-cases/document-processing.md)
- How retrieval over your knowledge base works: [RAG explained](../../learn/concepts/rag-explained.md)
- Measuring the impact: [measuring AI ROI](../enablement/measuring-ai-roi.md)

## Sources

- Brynjolfsson, Li and Raymond, *Generative AI at Work*, NBER Working Paper 31161: <https://www.nber.org/papers/w31161>
- McCarthy Tetrault, *Moffatt v. Air Canada: A Misrepresentation by an AI Chatbot* (2024 BCCRT 149): <https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot>
- Klarna, *Klarna AI assistant handles two-thirds of customer service chats in its first month* (27 February 2024): <https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/>
- Entrepreneur, *Klarna Is Hiring Customer Service Agents After AI Couldn't Cut It on Calls* (May 2025, reporting Bloomberg interview): <https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396>
