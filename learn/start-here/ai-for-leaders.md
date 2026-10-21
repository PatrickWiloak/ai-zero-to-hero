# AI for Leaders

**In one line:** For executives and managers: what AI can and cannot do for your organisation today, how to pick where to start, the risks you own, and which parts of the noise you can safely ignore.
**Last reviewed:** 2026-10-21

---

## The short version

- Today's AI is very good at **language work**: reading, summarising, drafting, classifying, extracting, answering questions over documents, writing and reviewing code. If a task is mostly reading and writing text, there is probably a real gain available.
- It is unreliable at **unsupervised judgement on facts that matter**. Every serious deployment keeps a human, a check, or a narrow scope between the model and anything consequential.
- Start with **use, not build**. Give staff an approved assistant with clear rules, measure what happens, and only then fund custom systems for the few workflows where the data says it pays.
- You own three risks whether or not you have a strategy: **data leaving the building** through unapproved tools, **wrong outputs** reaching customers, and **regulation** that already applies to some uses (hiring, credit, health, education).
- Measure time saved and quality on real tasks, not licences issued or "AI initiatives launched".
- You can ignore most model launch announcements, most benchmark leaderboards, and most claims about what AI will do in five years. They rarely change what you should do this quarter.

## What changed, in one paragraph

Until about 2022, using machine learning in a business meant collecting labelled data and training a model for one narrow task, such as fraud scoring or demand forecasting. That still matters, and [What is machine learning?](../concepts/what-is-machine-learning.md) explains it. What changed is that **general-purpose language models** became good enough to do thousands of different language tasks from a plain-English instruction, with no training project. The cost of trying an AI idea fell from a six-month project to an afternoon. That is why AI is now a leadership question rather than only a data-science one: every department can use it, so every department will, with or without a plan.

## What AI is good for today

Think in terms of task shapes, not job titles.

| Task shape | Examples | Typical result |
|---|---|---|
| Long text to short text | Summarising reports, contracts, tickets, calls | Large time savings; needs spot checks |
| Rough to polished | Drafting emails, proposals, job ads, policies | Faster first drafts; human edits and owns the final |
| Unstructured to structured | Pulling fields from invoices, forms, emails into a system | Strong when paired with validation rules |
| Question over your documents | Internal help desks, policy questions, sales enablement | Works when the documents are good and answers cite sources |
| Classify and route | Ticket triage, lead scoring, sentiment, intent | Reliable, cheap, easy to measure |
| Code | Writing, reviewing and explaining software | The most mature use; widely adopted by engineering teams |

The use-case guides go into each: [document processing](../../work/use-cases/document-processing.md), [customer support automation](../../work/use-cases/customer-support-automation.md), [meetings and summaries](../../work/use-cases/meetings-and-summaries.md), [research and analysis](../../work/use-cases/research-and-analysis.md), and [coding assistants in practice](../../work/use-cases/coding-assistants-in-practice.md).

## What it is not good for (yet)

**Unsupervised facts.** Language models generate plausible text, which is usually but not always true, and they state errors in the same confident tone as facts. [Hallucinations](../concepts/hallucinations.md) explains why this is structural, not a bug that will be patched next quarter. Design so that a person, a database lookup, or a validation rule checks anything a customer, regulator or court will rely on.

**Long autonomous chains of action.** "Agents" that plan and act over many steps are improving quickly and are useful in narrow, well-instrumented settings such as software engineering. Outside those, each extra autonomous step is another chance for an error to compound. Ask vendors how their agent fails and how you would know.

**Replacing judgement you cannot describe.** If your best people cannot explain what makes a decision good, a model cannot learn it from a prompt, and you cannot evaluate whether it got it right.

## Where to start: a three-stage pattern

The organisations that get value tend to follow the same sequence. The [AI adoption playbook](../../work/enablement/ai-adoption-playbook.md) covers it in detail; here is the shape.

**Stage 1: safe access and literacy (first 1 to 3 months).** Choose an enterprise assistant with a data-processing agreement ([choosing enterprise AI tools](../../work/enablement/choosing-enterprise-ai-tools.md) compares the main ones). Publish a short [acceptable use policy](../../work/enablement/acceptable-use-policy.md). Train people on how to brief a model and how to check its work ([training your team](../../work/enablement/training-your-team.md)). Recruit a handful of enthusiasts as [AI champions](../../work/enablement/ai-champions-program.md). The goal is to replace shadow use of personal accounts with sanctioned use, and to find out where the value actually is.

**Stage 2: measured workflows (months 3 to 9).** Pick the two or three workflows where Stage 1 showed real gains. Redesign them around AI deliberately: who checks what, what gets logged, what the fallback is. Measure before and after on time, quality and error rate ([measuring AI ROI](../../work/enablement/measuring-ai-roi.md)).

**Stage 3: build where it pays (months 6 onward).** Only now fund custom systems: retrieval over your own knowledge base, automation inside your products, agents for specific internal processes. [Build vs buy](../../tools/decisions/build-vs-buy.md) helps with that call.

Skipping straight to Stage 3 is the most common and most expensive mistake. Teams build a custom chatbot before anyone knows which questions people actually ask.

## The risks you own

**Data leakage.** If you have not provided an approved tool, assume some of your staff are using personal accounts anyway, because the tools are free and a browser tab away. The fix is not a ban (bans push use underground); it is an approved tool with a contract that covers data retention and training use, plus clear rules.

**Wrong outputs.** Someone will send a customer an AI-drafted answer with a wrong number in it. Decide in advance where human review is mandatory, and make the reviewer accountable for the result, not the tool.

**Security.** AI systems that read external content (email, web pages, uploaded files) can be manipulated by instructions hidden in that content. This is called **prompt injection**, and it is not fully solved by any vendor. It matters most when the AI can also take actions or see sensitive data. Your technical teams should know [prompt injection](../../safety/security/prompt-injection-explained.md) and the [OWASP LLM Top 10](../../safety/security/owasp-llm-top-10.md); you should know to ask about it.

**Regulation.** Some AI uses are regulated now. The EU AI Act bans a short list of practices (since 2 February 2025), places duties on providers of general-purpose models (since 2 August 2025), and imposes heavy requirements on "high-risk" uses such as hiring, credit and education; as of 2026-10 those high-risk duties are scheduled to apply from 2 December 2027 for stand-alone systems, after the 2026 "AI Omnibus" delay. If you sell into or operate in the EU, read the [EU AI Act explainer](../../explainers/policy/eu-ai-act.md) and [EU AI Act compliance](../../safety/governance/eu-ai-act-compliance.md). In the US, the picture is a mix of federal guidance and state laws ([US AI policy](../../explainers/policy/us-ai-policy.md)). Existing law on discrimination, consumer protection and privacy applies to AI decisions everywhere.

**Governance.** You need a named owner, an inventory of where AI is used, and a risk review for new uses. That does not need to be heavy. [AI governance program](../../safety/governance/ai-governance-program.md) and [AI risk assessment](../../safety/governance/ai-risk-assessment.md) show a proportionate version; the [NIST AI RMF](../../safety/governance/nist-ai-rmf.md) and [ISO/IEC 42001](../../safety/governance/iso-42001.md) are the frameworks auditors will recognise.

## What to measure

Avoid vanity metrics. Licences assigned and "number of AI use cases" tell you nothing. Useful measures:

- **Time per task** on a specific workflow, before and after, on a sample of real work.
- **Quality** on the same sample, judged by the people who would normally review it.
- **Error and escalation rate:** how often AI-assisted work had to be corrected, and how serious the corrections were.
- **Adoption depth:** weekly active users and what they use it for, not just logins.
- **Cost per completed task**, including licence and the review time it creates.

A 30% time saving on a task that takes 10% of someone's week is a 3% productivity gain for that person. That is real, but it is not the transformation in the press release. Be honest about the arithmetic.

## What you can safely ignore

- **Each new model launch.** Leading models from the major labs leapfrog each other every few months. For most business tasks several of them are good enough, and the difference between them is smaller than the difference between a good and a bad workflow design. Revisit your choice once or twice a year, not every month.
- **Benchmark leaderboards.** Public benchmarks measure narrow skills, are often partly memorised by the models, and saturate quickly ([contamination and saturation](../../explainers/benchmarks/contamination-and-saturation.md)). Test on your own tasks.
- **Timelines for general AI.** Serious people disagree by decades. Plan for the capability you can test today plus steady improvement. If you want the debate, [scaling limits](../../explainers/open-questions/scaling-limits.md) and the [Situational Awareness essay summary](../../papers/essays/113-situational-awareness/summary.md) are good starting points, but they should not change this quarter's plan.
- **"AI-powered" labels.** Ask what the model does, what data it sees, how it fails, and how you would measure whether it works.

## Questions to ask your team or a vendor

1. What exactly does the model do in this workflow, and what does a person still do?
2. What data does it see, where is it processed, and is it retained or used for training?
3. How do we know it is working? Show me the test set and the number.
4. What happens when it is wrong? Who notices, and how fast?
5. What does it cost per transaction at our volume, and what happens to that cost if usage triples?
6. If this vendor or model disappeared tomorrow, how hard is it to switch?

If the answers are vague, the project is not ready.

## Common mistakes

- **Building before using.** Custom systems built before anyone used an off-the-shelf assistant usually solve the wrong problem.
- **Banning instead of providing.** Bans move use to personal phones, where you have no visibility.
- **Counting pilots instead of outcomes.** Ten pilots with no measurement are worse than one workflow with a before-and-after number.
- **Delegating it entirely to IT.** The value is in redesigning work, which is a business decision. IT can provide tools and controls; the business has to own the workflow change.
- **Treating it as one-off.** Models, prices and rules change every few months. Assign an owner and review quarterly.

## Next steps

- [AI adoption playbook](../../work/enablement/ai-adoption-playbook.md): the staged rollout in detail
- [Choosing enterprise AI tools](../../work/enablement/choosing-enterprise-ai-tools.md)
- [Playbook for managers](../../work/playbooks/for-managers.md)
- [Responsible AI basics](../../safety/governance/responsible-ai-basics.md)
- [AI for everyone](ai-for-everyone.md): share this with your team
- [Labs landscape](../../explainers/ecosystem/labs-landscape.md): who makes the models you are buying

## Sources

- European Commission, AI Act regulatory framework (risk tiers, timeline, AI Omnibus dates): https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- Regulation (EU) 2024/1689 (AI Act), EUR-Lex: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- NIST, AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001:2023, Artificial intelligence management system: https://www.iso.org/standard/81230.html
- OWASP Top 10 for LLM Applications: https://genai.owasp.org/llm-top-10/
- Kalai et al., "Why Language Models Hallucinate" (2025): https://arxiv.org/abs/2509.04664
