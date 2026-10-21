# AI for Managers

**In one line:** Use AI to cut the writing and synthesis load of managing - updates, meeting prep, plans, first drafts of documents - while keeping it well away from judgments about people, and set clear expectations so your team uses it well too.
**Last reviewed:** 2026-10-21

---

## The short version

- Managers write a lot: status updates, plans, emails, meeting agendas, decision memos. AI is good at first drafts and at turning messy notes into structure. Start there.
- Use it as a thinking partner: "what am I missing?", "argue the other side", "what questions will my VP ask?"
- **Do not** use it to write performance reviews from scratch, decide promotions or pay, or assess individuals. Those decisions need your judgment and carry legal and fairness risk.
- Your second job is your team's use: model good habits, protect time to learn, review AI-assisted work by its quality not its origin, and follow the [acceptable use policy](../enablement/acceptable-use-policy.md).
- Expect the biggest wins where the work is repetitive writing and the smallest where it depends on relationships or facts the AI does not have.

## Where AI helps a manager most

| Task | How AI helps | What you still do |
|---|---|---|
| Weekly status update | Turns bullet notes into a clean update for your audience | Decide what matters and what to flag |
| Meeting prep | Builds an agenda, pre-reads summary, likely questions | Choose the outcome you need |
| Meeting follow-up | Turns notes or a transcript into decisions and actions | Check owners and dates |
| Plans and proposals | First draft from your outline; structure; risks list | The actual plan and trade-offs |
| Hard emails | Drafts in a calm tone; checks for unintended tone | Send it, own it |
| Decision memos | Lays out options, pros, cons, open questions | Make the decision |
| Learning a new area | Explains concepts, suggests what to read | Verify against real sources |

## Copyable prompts

Replace the bracketed parts. Paste real context; it matters more than wording.

**Status update from notes**
```
Here are my rough notes from this week for [team/project]:
[paste notes]

Write a status update for [audience, e.g. my director, who reads on mobile and
cares about risks and dates]. Sections: Progress, Risks (with what I need
from them), Next week. Under 200 words. Do not invent anything not in my
notes; if something is unclear, list it at the end as "Questions for me".
```

**Meeting prep**
```
I have a 30-minute meeting with [who, role] about [topic]. My goal is
[decision or outcome]. Background: [paste context].

Give me: a 4-item agenda with timings, the 5 questions they are most likely
to ask and a short answer for each based only on the background, and the
one thing most likely to derail the meeting.
```

**Pressure-test a plan**
```
Here is my plan for [goal]: [paste plan].
Act as a sceptical senior leader. List the 5 strongest objections, what
evidence would answer each, and which assumption, if wrong, breaks the plan.
Be direct. Do not rewrite the plan.
```

**Turn a transcript into actions**
```
Here is a meeting transcript: [paste].
Extract: decisions made (quote the line that shows it), action items as a
table (action, owner, due date - write "not stated" rather than guessing),
and open questions. Then write a 5-line follow-up email to attendees.
```

**Difficult email, tone check**
```
Here is a draft email to [who] about [situation]: [paste draft].
I want it to be [firm but respectful]. Point out any sentence that could
read as [defensive / blaming / vague], and suggest a rewrite of only those
sentences.
```

## Before and after

**Before.** A team lead spends Friday afternoon writing three versions of the same week: a detailed update for the team, a short one for her director, and a client-safe one. About 90 minutes.

**After.** She keeps a running notes file during the week. On Friday she pastes it with the status-update prompt three times, once per audience, then edits each for 5-10 minutes, checking every date and name against her notes. About 30 minutes. The director version gets better because she uses the time saved to add one paragraph of actual judgment about a risk.

The point is not that the AI wrote it. The point is that she spent her time on the part only she can do.

## Leading your team's AI use

- **Say clearly what is expected.** "Use the approved tool for drafts and summaries. You own what you send. Never paste customer personal data." Ambiguity makes careful people avoid it and careless people misuse it.
- **Use it visibly yourself**, and share both a win and a failure in a team meeting.
- **Protect learning time.** An hour a week for the first month. See [training your team](../enablement/training-your-team.md).
- **Review the work, not the tool.** Do not penalise AI-assisted work that is good, and do not accept poor work because "the AI wrote it".
- **Redesign the workflow, not only the task.** If drafts now take minutes, perhaps review becomes the bottleneck. Adjust who reviews what.
- **Support a champion** in your team, and give them the time. See [AI champions program](../enablement/ai-champions-program.md).
- **Watch for uneven effects.** Research on support agents found the largest gains for novices. Your newer staff may speed up most; make sure they are also learning the underlying skill, not only producing output.

## Where not to use it

- **Performance reviews and feedback.** You can use AI to improve the clarity of feedback you have already written, with names and identifying details removed. Do not ask it to assess someone, and do not paste HR records. Decisions about people's employment are treated as high-risk under the EU AI Act, and bias in such systems is a known problem. See [responsible AI basics](../../safety/governance/responsible-ai-basics.md).
- **Hiring decisions.** Screening and ranking candidates with a general chatbot is a fairness and legal risk. If your company uses AI in hiring, it should go through a formal [AI risk assessment](../../safety/governance/ai-risk-assessment.md).
- **Anything confidential** about restructures, pay, or individuals, unless your approved tool and policy explicitly cover that data.
- **Facts it cannot know.** Your org's numbers, last week's decision, the customer's history. If you did not paste it, do not trust it.

## Failure modes to watch for

- **Fluent but empty.** AI-written updates can sound complete and say nothing. If you cannot point to a decision, a risk or a number in it, rewrite it.
- **Invented specifics.** Dates, owners and figures that were not in your notes. The "do not invent; list questions" line in the prompts above reduces this but does not remove it.
- **Homogenised voice.** If every message from you sounds the same, people stop reading. Edit for your own voice on anything important.
- **Over-reliance in new managers.** AI can draft the hard email; it cannot have the hard conversation.

## Common mistakes

- Asking vague questions ("help me with my team") and concluding it is useless.
- Sending a draft without reading it closely.
- Banning AI on your team out of caution while people use personal accounts anyway.
- Measuring your team's AI use instead of their results.

## Next steps

- Lead the wider rollout: [AI adoption playbook](../enablement/ai-adoption-playbook.md)
- Measure what changes: [measuring AI ROI](../enablement/measuring-ai-roi.md)
- Meetings specifically: [meetings and summaries](../use-cases/meetings-and-summaries.md)
- The leader's view: [AI for leaders](../../learn/start-here/ai-for-leaders.md)

## Sources

- Brynjolfsson, Li and Raymond, *Generative AI at Work*, NBER Working Paper 31161: <https://www.nber.org/papers/w31161>
- EU AI Act, Annex III (high-risk systems, including employment and worker management): <https://artificialintelligenceact.eu/annex/3/>
