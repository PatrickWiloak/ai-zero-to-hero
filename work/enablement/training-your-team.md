# Training Your Team to Use AI

**In one line:** Teach AI as a work skill, not a tool tour - a 90-minute hands-on starter session on people's own tasks, then short weekly practice and a shared prompt library - and you will get far more use than from any slide deck.
**Last reviewed:** 2026-10-21

---

## The short version

- Most people try AI once on a vague question, get a vague answer, and conclude it is overrated or magic. Training exists to get them past that first bad experience.
- Teach four things: **what it is good and bad at**, **how to give it context**, **how to check its work**, and **what data never goes in**.
- Do it hands-on with each person's real work. People learn in the moment they see it save them 20 minutes on something they do every week.
- Follow the starter session with four weeks of short practice and a shared library of prompts that work for your team.
- Under the EU AI Act, organisations deploying AI must take measures to ensure a sufficient level of AI literacy among staff who use it (Article 4, applicable since 2 February 2025). Training plus a policy is the practical way to show that.

## What people actually need to learn

Skip the history of neural networks. Non-technical staff need a mental model that predicts behaviour:

1. **It predicts plausible text.** A language model writes what is likely to come next given everything in the conversation. That makes it excellent at drafting, rewording, summarising and structuring, and it means it will produce fluent, confident text even when it does not know the answer. That is a [hallucination](../../learn/concepts/hallucinations.md), and it is normal behaviour, not a malfunction.
2. **It only knows what is in front of it** plus what it absorbed in training. It does not know your company, your customer, or last week's decision unless you paste or connect it. More relevant context beats cleverer wording.
3. **It is uneven.** The same tool can be brilliant at one task and quietly wrong at a similar-looking one. In the Harvard/BCG field experiment, consultants using AI did markedly better on tasks within its capability but were 19 percentage points less likely to be correct on a task outside it. People need to learn their own task-by-task map.
4. **You are the editor.** Treat output as a first draft from a fast, well-read intern who has never met your customers.

## The 90-minute starter session

Run it for groups of 8-15, ideally from one team so examples are shared. Everyone needs a laptop logged into the approved tool. Ask each person to bring two real tasks from the past week that contain no Restricted data.

**0-10 min: why and the rules.** What the company is rolling out and why. The three data buckets from the [acceptable use policy](acceptable-use-policy.md), with real examples: "this is fine to paste, this is not". Who owns the output (you do).

**10-25 min: live demo, bad prompt versus good prompt.** The facilitator shows the same task twice.

Bad:
```
Write an email about the project delay.
```

Good:
```
You are helping me write to a client. Context: we are 2 weeks late on the
data migration for Acme because their IT team gave us database access 10 days
after the agreed date. We have a new go-live of 14 November. The client
contact is Priya, the CFO, who is direct and dislikes long emails.

Write a short email (under 150 words) that: states the new date, explains the
cause factually without blaming Acme's IT team, says what we are doing to
avoid further slips, and asks for a 20-minute call this week. Plain tone,
no apologies beyond one sentence.
```

Point out what made the difference: role, audience, facts, constraints, format, tone. Then show iterating: "Shorter. Remove the second paragraph. Make the ask clearer."

**25-35 min: the anatomy of a useful prompt.** Put this on a slide and in the handout:

```
1. Task      - what you want, in one sentence
2. Context   - the facts, the background, paste the source material
3. Audience  - who will read it and what they care about
4. Format    - length, structure, bullets or prose, table
5. Examples  - a sample of what good looks like, if you have one
6. Check     - "list any facts you are unsure of" / "quote the source for each claim"
```

**35-70 min: hands-on with their own tasks.** Each person works on their two tasks. Facilitator and a champion walk the room. The goal is one real win per person. Common coaching moments: "paste the actual document", "tell it who the reader is", "ask it to ask you questions first", "it's wrong about that - tell it so and why".

**70-80 min: checking output.** A short exercise: give everyone the same AI-generated summary of a document, with two planted errors (a wrong number and an invented quote). Ask them to find them using the source. Most groups miss at least one. That lands the point better than any warning.

**80-90 min: what next.** Show the shared prompt library and the help channel. Each person writes down one task they will use AI for every day this week.

## Weeks 2-5: practice that sticks

One-off training fades. Habits form from repeated use on real work.

- **Weekly 20-minute "show and tell"** per team: two people show something that worked, one person shows something that failed. Failures are as valuable as wins.
- **Weekly challenge**, posted in the team channel. Week 2: summarise a long document and verify three facts against it. Week 3: ask the AI to critique your own draft before you send it. Week 4: turn a messy set of notes into a structured table. Week 5: build a reusable prompt for one recurring task and add it to the library.
- **Prompt library.** A shared document or wiki page per team: task name, the prompt, an example input and output, who owns it, and a warning line ("always check the dates"). Champions curate it. See [AI champions program](ai-champions-program.md).

## Tailor by audience

| Group | Extra focus |
|---|---|
| Everyone | Data rules, checking output, the prompt anatomy |
| Managers | Where AI changes workflow and expectations; how to review AI-assisted work; not using AI for decisions about people. See [for managers](../playbooks/for-managers.md) |
| Customer-facing roles | Never send unreviewed output; tone; when to disclose AI use. See [for sales](../playbooks/for-sales.md), [for support and ops](../playbooks/for-support-and-ops.md) |
| Analysts | Asking for formulas and code instead of numbers; reproducibility. See [for analysts](../playbooks/for-analysts.md) |
| Engineers | Coding assistants, code review, secrets, tests. See [for engineers](../playbooks/for-engineers.md) |
| Leaders | Strategy, risk, what to measure. See [AI for leaders](../../learn/start-here/ai-for-leaders.md) |

## How to tell training worked

- **Weekly active use** among trained staff at weeks 2, 4 and 8. A drop after week 2 means people did not find a daily use; go back to their tasks.
- **Prompt library growth**: new entries per week from outside the champion group.
- **Quiz on the data rules** (five questions, scenario-based) one month later.
- **Two-question pulse**: "Did AI save you time this week on a real task? Which one?" The named tasks are the evidence.
- **Incidents**: data pasted into unapproved tools, unreviewed output reaching customers. These should go down, not up, as people learn.

See [measuring AI ROI](measuring-ai-roi.md) for turning this into a business case.

## Where training does not help

- If the tool is not approved or not available, training creates frustration.
- If managers do not allow time to experiment, people will not change how they work. Protect an hour a week during the first month.
- If a job is mostly relationship, negotiation, or hands-on physical work, the gains are smaller. Be honest about that rather than forcing use cases.
- Some people will not like it. That is fine. Make it available and useful, not compulsory theatre.

## Common mistakes

- **Teaching the tool's buttons instead of the skill.** Interfaces change monthly; the prompt anatomy and checking habits do not.
- **Generic examples.** "Write a poem about our company" teaches nothing. Use their real tasks.
- **Skipping verification practice.** Telling people "it can be wrong" does not work. Letting them catch it being wrong does.
- **One session and done.** Without the follow-up weeks, usage typically fades.
- **Shaming mistakes.** If someone pasted the wrong thing, you want them to report it, not hide it.

## Next steps

- Build the network that keeps learning going: [AI champions program](ai-champions-program.md)
- Role-specific prompts to hand out: [for managers](../playbooks/for-managers.md), [for marketing](../playbooks/for-marketing.md), [for analysts](../playbooks/for-analysts.md)
- Deeper prompting for curious learners: [prompt engineering](../../learn/concepts/prompt-engineering.md)
- The non-technical starting path: [AI for everyone](../../learn/start-here/ai-for-everyone.md)
- Why models get facts wrong: [Why Language Models Hallucinate](../../papers/techniques/149-why-language-models-hallucinate/summary.md)

## Sources

- EU AI Act, Article 4 (AI literacy): <https://artificialintelligenceact.eu/article/4/>
- Dell'Acqua et al., *Navigating the Jagged Technological Frontier*, Harvard Business School Working Paper 24-013 (2023): <https://www.hbs.edu/faculty/Pages/item.aspx?num=64700>
