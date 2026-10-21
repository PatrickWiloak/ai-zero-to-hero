# Measuring AI ROI

**In one line:** Measure AI's value task by task against a baseline - time, quality, errors and adoption - using timestamps and blind review rather than self-reported feelings, and turn hours saved into money only when they actually go somewhere.
**Last reviewed:** 2026-10-21

---

## The short version

- "We have 400 active users" is not ROI. ROI is "proposal drafting takes 3 hours instead of 6 at the same quality, for 25 people, and we used the time to send more proposals".
- Always take a **baseline before** rollout, for the specific tasks you expect AI to help.
- Measure four things per task: **time**, **quality**, **errors**, and **adoption**. Add one business outcome where you can (tickets resolved, deals progressed, cycle time).
- Do not trust self-reported time savings alone. In a 2025 randomised trial, experienced developers were 19% slower with AI tools yet believed they were about 20% faster.
- Hours saved are only worth money if they are reinvested in something valuable or reduce a real cost. Say which.

## Why this is harder than it looks

Published studies show the range you should expect, and why "AI makes people X% more productive" is not a number you can borrow:

| Study | Who and what | Result |
|---|---|---|
| Noy and Zhang, *Science* (2023) | 453 college-educated professionals on writing tasks | Time down 40%, quality up 18% |
| Brynjolfsson, Li and Raymond (NBER) | Customer support agents | Issues resolved per hour up 14% on average, 34% for novice and low-skilled workers, little effect for the most experienced |
| Dell'Acqua et al. (Harvard/BCG, 2023) | 758 consultants, 18 realistic tasks | Inside AI's capability: 12.2% more tasks, 25.1% faster, over 40% higher quality. On a task outside it: 19 percentage points less likely to be correct |
| Peng et al. (2023) | Developers writing an HTTP server in JavaScript | Copilot group finished 55.8% faster |
| METR (2025) | 16 experienced open-source developers, 246 tasks in their own repositories | 19% slower with AI tools, while believing they were faster |

The lesson is not that AI does or does not work. It is that the effect depends on the task, the person's experience, and the quality of the tool and workflow. You have to measure your own.

## Step 1: Choose the tasks and the metrics

For each use case in your pilot, fill in one row before anyone starts:

| Use case | Volume per week | Baseline time | Quality measure | Error measure | Business outcome |
|---|---|---|---|---|---|
| Proposal first drafts | 12 | median 6.5 h | Blind reviewer score 1-5 | Factual errors found in review | Proposals sent per month |
| Support reply drafts | 900 | 7.5 min handle time | QA score on sampled tickets | Escalations, reopened tickets | CSAT, backlog |
| Monthly variance commentary | 1 per BU | 2 days | Finance lead score | Numbers that do not tie | Days to close |

Rules of thumb:

- Pick tasks that happen often enough to measure in weeks, not months.
- Use the closest thing to a system timestamp you have: ticket handle time, document created-to-sent, pull request open-to-merge. Self-logs are a fallback.
- Choose the quality measure before you see results.

## Step 2: Take the baseline

Two weeks of data before AI access, for the pilot group, on those tasks. If people already use AI informally (likely), ask them not to during the baseline, or compare against a similar team that has not started.

If you can, keep a **comparison group**: a similar team or a random half of the pilot that starts four weeks later. It is the single best protection against fooling yourself, because many things change in a month besides AI.

## Step 3: Measure during the pilot

**Time.** Pull the same timestamps. For tasks without system data, use a short log: task, start, end, "used AI? yes/no". A sample of two weeks is enough.

**Quality.** Blind review. Take 20-30 outputs from before and after, strip anything that reveals which is which, and have a qualified reviewer score them on a fixed rubric. This catches the most common hidden cost: faster, but worse.

**Errors.** Count errors that reached a customer, a manager, or a published document, per 100 outputs. Pay special attention to the error types AI introduces: invented facts, wrong numbers, outdated policy, confident tone on wrong answers.

**Adoption.** Weekly active users / licensed users, and which use cases are used. Your tool's admin console usually gives the first number. The second needs a pulse survey.

**Sentiment.** Two questions monthly: "How disappointed would you be if we removed this tool?" (very / somewhat / not) and "Name one task it helped with this week." The named tasks are your evidence and your next prompt-library entries.

## Step 4: Turn it into money, honestly

```
Gross monthly value  = hours saved per task x tasks per month x loaded hourly cost
Net monthly value    = gross value - (licence cost + usage cost + support/training time)
Cost per active user = total monthly cost / weekly active users
```

Worked example (illustrative numbers):

- 25 people draft proposals. Median drafting time fell from 6.5 to 4.0 hours in the pilot, with blind quality scores unchanged.
- They write 50 proposals a month in total, so 125 hours saved.
- Loaded cost $70/hour gives a gross $8,750 a month.
- 25 seats at $30 is $750, plus about 10 hours a month of champion and admin time ($700): $1,450.
- Net: about $7,300 a month on this one use case.

Then the honest question: **where did the 125 hours go?** If the team sent more proposals and won more work, show that. If they absorbed it into other work, say "capacity freed", which is real but softer. If nothing changed, the saving is theoretical. Leaders who have seen inflated ROI decks will respect the distinction.

Also count the costs people forget: the time to review AI output, rework when it was wrong, the risk cost of an error reaching a customer, and seats nobody uses.

## Step 5: Report it

A one-page monthly report per rollout wave:

1. Adoption: weekly active / licensed, trend.
2. Top three use cases by measured value, with before and after.
3. Use cases stopped and why.
4. Quality and error trend.
5. Incidents (data, customer impact).
6. Cost per active user.
7. Decision needed: expand, hold, cut seats.

## What not to measure

- **Number of prompts or messages.** More messages can mean confusion, not value.
- **"Hours saved" from a vendor's calculator.** These assume every suggestion is used and every minute saved is productive.
- **Lines of code generated** for engineering teams. See [for engineers](../playbooks/for-engineers.md) and [coding assistants in practice](../use-cases/coding-assistants-in-practice.md) for better measures.

## Common mistakes

- **No baseline.** The most common and most fatal.
- **Relying on surveys of perceived speed.** Use them for sentiment, not for time.
- **Measuring speed without quality.** Faster wrong work is negative ROI.
- **Averaging across everyone.** Gains concentrate in certain tasks and, often, among less experienced staff. Report by use case and by group.
- **Claiming headcount savings you will not take.** If no role changes, do not put it in the business case.

## Next steps

- Where this fits in the rollout: [AI adoption playbook](ai-adoption-playbook.md)
- Cost side of the equation: [choosing enterprise AI tools](choosing-enterprise-ai-tools.md)
- For engineering teams and AI applications, the equivalent is evaluation: [evals for LLMs](../../learn/concepts/evals-for-llms.md)
- What AI can and cannot do on long tasks: [METR time horizons](../../papers/techniques/145-metr-time-horizons/summary.md)

## Sources

- Noy and Zhang, *Experimental evidence on the productivity effects of generative artificial intelligence*, Science 381 (2023): <https://www.science.org/doi/10.1126/science.adh2586> (working paper: <https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1_0.pdf>)
- Brynjolfsson, Li and Raymond, *Generative AI at Work*, NBER Working Paper 31161: <https://www.nber.org/papers/w31161>
- Dell'Acqua et al., *Navigating the Jagged Technological Frontier*, Harvard Business School Working Paper 24-013 (2023): <https://www.hbs.edu/faculty/Pages/item.aspx?num=64700>
- Peng, Kalliamvakou, Cihon and Demirer, *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot* (2023): <https://arxiv.org/abs/2302.06590>
- METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* (2025): <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>
