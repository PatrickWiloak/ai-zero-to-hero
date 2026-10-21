# AI Adoption Playbook

**In one line:** Roll AI out to a team or company in four phases over about twelve weeks - set guardrails, pilot with volunteers on real tasks, measure, then scale what worked - instead of buying licences for everyone and hoping.
**Last reviewed:** 2026-10-21

---

## The short version

- Your people are probably already using AI, on personal accounts you cannot see. Microsoft's 2024 survey of 31,000 knowledge workers found 75% used AI at work and 78% of those brought their own tools. The first job of a rollout is to give them a safe, sanctioned option, not to start from zero.
- Run it in four phases: **Guardrails** (weeks 1-2), **Pilot** (weeks 3-8), **Measure and decide** (weeks 9-10), **Scale** (weeks 11-12 and beyond).
- Pick pilot use cases from real, repeated work that people already find tedious, where a wrong answer is cheap to catch. Not from a vendor demo.
- Gains are uneven. Controlled studies find big improvements on some tasks and worse results on others, so measure task by task and do not promise a blanket number.
- A rollout succeeds when people change how they work, so most of your effort goes into training, champions and shared prompts, not into the tool.

## Why a plan beats "everyone gets a licence"

The two common failure patterns are opposite. One company bans AI, and staff paste customer data into free consumer chatbots anyway, out of sight. Another buys a licence for every employee, sends one launch email, and six months later finds a fifth of seats in active use and nobody able to say what changed.

The evidence explains why neither works. In a field experiment with 758 Boston Consulting Group consultants, people using GPT-4 on tasks inside the model's capability finished 12.2% more tasks, 25.1% faster, at over 40% higher quality. On a task the researchers deliberately chose to sit outside that capability, consultants with AI were 19 percentage points less likely to get the right answer than those without it. The authors called this the "jagged frontier": AI is very good at some tasks and confidently wrong at others that look just as hard. A large customer support study found a 14% average gain in issues resolved per hour, but 34% for novices and close to nothing for the most experienced.

So the job of an adoption program is to help each team find where its own work sits on that frontier, and to make the good uses repeatable.

## Phase 1: Guardrails (weeks 1-2)

You cannot run a pilot until people know what they are allowed to do.

**Week 1**

- Name an owner. One accountable person (often in operations, IT or a COO's office) plus a small working group: IT/security, legal or privacy, HR, and two or three managers from the business.
- Find out what is already happening. Send a short anonymous survey: which AI tools do you use, for what, on which account, and have you ever pasted customer or confidential data in? Anonymity gets you honest answers.
- Classify your data into three buckets: public, internal, and restricted (customer personal data, health, financial, legal privileged, trade secrets, anything under contract). This classification drives every later rule.

**Week 2**

- Publish a one-page acceptable-use policy. Start from the template on the [acceptable use policy](acceptable-use-policy.md) page.
- Choose a sanctioned tool for the pilot on a business or enterprise plan, where the vendor contractually does not train on your data. See [choosing enterprise AI tools](choosing-enterprise-ai-tools.md) for the comparison.
- Decide what you will measure before anyone starts (see Phase 3), and capture a baseline for those tasks now. Without a "before" you cannot show an "after".

## Phase 2: Pilot (weeks 3-8)

**Pick the cohort.** 15 to 40 volunteers across two to four teams is enough to learn from without being expensive. Include sceptics, not only enthusiasts, and include at least one manager per team so that changes to workflow can actually be approved.

**Pick the use cases.** Ask each team to list tasks that are frequent, tedious, text-heavy, and easy to check. Score them:

| Question | Score 0-2 |
|---|---|
| How often does this task happen? (weekly or more = 2) | |
| How much time does it take each time? | |
| Can a person check the output quickly? | |
| If the AI is wrong and nobody notices, is the damage small? | |
| Can it be done without restricted data, or on the sanctioned tool? | |

Pick the two or three highest per team. Typical winners: first drafts of routine emails and documents, summarising long threads or documents, turning meeting notes into action lists, reformatting and cleaning data, and drafting answers from an existing knowledge base. Typical losers for a first pilot: anything where the output goes directly to a customer or regulator without review, and anything needing facts the model does not have.

**Weeks 3-4: train and start.** Run the 90-minute starter session from [training your team](training-your-team.md). Give every pilot member a shared prompt library for their use cases (the role pages, such as [for managers](../playbooks/for-managers.md) or [for sales](../playbooks/for-sales.md), have copyable ones). Set up a chat channel for questions and wins.

**Weeks 5-6: weekly check-ins.** 30 minutes per team. Three questions: what worked, what failed, what did you stop using it for? Collect the prompts that work into the shared library. Collect failures too, they are your training material.

**Weeks 7-8: tighten.** Drop use cases that are not paying off. Write a one-paragraph "how we do X with AI" note for each one that is. This is where champions emerge; see [AI champions program](ai-champions-program.md).

## Phase 3: Measure and decide (weeks 9-10)

Measure the tasks, not the tool. "Number of prompts sent" tells you nothing about value. For each pilot use case, compare to the week-2 baseline:

- **Time per task**, from a short self-reported log or, better, from system timestamps (ticket handle time, document turnaround).
- **Quality**, by blind review of a sample of before-and-after outputs by someone who does not know which is which.
- **Error rate**, especially errors that reached a customer.
- **Adoption**, as weekly active users among the pilot cohort, and which use cases they actually use.
- **Sentiment**, from a two-question survey: "Would you be upset if we took this away?" and "What would you need to use it more?"

The full method, including how to turn time saved into a cost case without inflating it, is on [measuring AI ROI](measuring-ai-roi.md).

Be careful with self-reported time savings. In METR's 2025 randomised trial, 16 experienced open-source developers took 19% longer with AI tools on their own repositories, yet afterwards estimated that AI had made them about 20% faster. People are bad at sensing their own speed. Use timestamps or a controlled comparison wherever you can.

Then decide, per use case: scale, keep testing, or stop. Write it down.

## Phase 4: Scale (weeks 11-12 and ongoing)

- **Expand in waves**, team by team, each wave led by a champion from the pilot. Do not switch everyone on at once.
- **Ship the playbook with the licence.** Each new team gets the policy, the training session, their role page, and the use-case notes from the pilot.
- **Integrate where it pays.** Once a use case is proven in chat, consider building it into the workflow (a template in the support desk, a document-processing pipeline). See the [use cases](../use-cases/document-processing.md) section.
- **Review quarterly.** Licence utilisation, new use cases, incidents, and policy updates. Tools change monthly; the policy and the tool choice should be revisited at least every six months.
- **Connect to governance.** As usage grows, AI needs an owner and a risk process like any other system. See [AI governance program](../../safety/governance/ai-governance-program.md).

## A worked example: a 60-person professional services firm

- Week 1: the COO owns it. The anonymous survey finds 38 of 60 people using free chatbots, 9 of whom have pasted client documents in.
- Week 2: a one-page policy goes out. The firm picks a business-tier chat assistant whose admin console allows single sign-on and turns off data sharing. Baseline: proposals take a median 6.5 hours to draft; weekly client status reports take 40 minutes each.
- Weeks 3-8: 20 volunteers from consulting and finance pilot three use cases: proposal first drafts from a template and past proposals, weekly status reports from project notes, and summarising contracts for key terms (with a lawyer reviewing every summary).
- Weeks 9-10: proposal drafting time drops noticeably and reviewers rate quality the same; status reports get faster; contract summaries miss an unusual indemnity clause twice in 30 samples, so that use case stays "assist only, never rely".
- Weeks 11-12: rollout to the whole firm, proposals and status reports first. The contract-summary use case is kept but the policy now says the lawyer reads the full clause list every time.

(The firm is illustrative; the method is the point.)

## What AI will not do for you

- It will not fix a broken process. If nobody knows who approves a proposal, AI just produces unapproved proposals faster.
- It will not replace judgment, relationships or accountability. Someone still owns every output.
- It will not save time on work that is mostly waiting, meetings, or negotiation.
- It does not know your company's facts unless you give them to it, and even then it can invent details. See [hallucinations](../../learn/concepts/hallucinations.md).

## Common mistakes

- **Licences first, use cases later.** If you cannot name three tasks per team before you buy, you are not ready to buy.
- **Banning without an alternative.** People route around it. Give them a sanctioned tool the same week you restrict the others.
- **Measuring logins.** Usage is a leading indicator, not value.
- **Only enthusiasts in the pilot.** You learn more from a sceptic who finds the one thing that genuinely helps them.
- **No baseline.** Without a "before", every result is an anecdote.
- **Treating it as an IT project.** The tool is the easy part. Habits, training and manager support are where rollouts succeed or fail.

## Next steps

- Write the rules: [acceptable use policy](acceptable-use-policy.md)
- Pick the tool: [choosing enterprise AI tools](choosing-enterprise-ai-tools.md)
- Teach it: [training your team](training-your-team.md) and [AI champions program](ai-champions-program.md)
- Prove it: [measuring AI ROI](measuring-ai-roi.md)
- For the leader's view of strategy and risk: [AI for leaders](../../learn/start-here/ai-for-leaders.md)

## Sources

- Microsoft and LinkedIn, *2024 Work Trend Index: AI at Work Is Here. Now Comes the Hard Part* (31,000 respondents, 31 markets): <https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part>
- Dell'Acqua et al., *Navigating the Jagged Technological Frontier*, Harvard Business School Working Paper 24-013 (2023): <https://www.hbs.edu/faculty/Pages/item.aspx?num=64700>
- Brynjolfsson, Li and Raymond, *Generative AI at Work*, NBER Working Paper 31161: <https://www.nber.org/papers/w31161>
- METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* (2025): <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>
