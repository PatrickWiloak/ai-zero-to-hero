# AI Champions Program

**In one line:** Recruit one respected, curious person per team as an AI champion, give them a few hours a month, a clear job and a direct line to the rollout owner, and they will spread working habits faster than any central training team can.
**Last reviewed:** 2026-10-21

---

## The short version

- A champion is a peer in a team who uses AI well, helps colleagues, collects what works, and reports what does not. They are not an IT helpdesk and not a cheerleader.
- Aim for roughly one champion per team of 8-15 people, chosen for credibility in their own job, not for technical skill.
- Give them **protected time** (2-4 hours a month is a reasonable start), **early access** to new features, **a monthly meeting** with the rollout owner, and **recognition** that counts in their review.
- Their three outputs: a curated prompt library for their team, a monthly list of wins and failures, and quick answers to "can I use AI for this?"
- Programs fail when champions are unpaid volunteers with no time, or when leadership ignores what they report.

## Why peers work

People copy the colleague next to them more readily than a training video. When someone in your own role shows you how they cut a weekly report from an hour to fifteen minutes, on the same report you write, the use case is obviously relevant and obviously allowed.

Champions also solve a problem central teams cannot: the best AI use cases are specific. "Use AI for writing" is useless advice. "Paste the call transcript and our discovery template into the assistant and ask it to fill the template, then fix the budget line, which it always gets wrong" is a habit. Only someone who does that work can find and refine it.

There is supporting evidence from the customer support study by Brynjolfsson, Li and Raymond: the AI assistant helped novice agents most, and the authors suggest it worked partly by spreading the practices of the best agents to everyone. A champion program does the same thing deliberately, with people.

## Choosing champions

Look for:

- **Credibility in the day job.** A strong performer whose colleagues already ask them for help.
- **Curiosity, with healthy scepticism.** You want someone who will say "this doesn't work for X" as readily as "this is great".
- **Willingness to teach.** Patience with less confident colleagues.
- **Range.** Include people from non-technical teams, different seniority levels and different locations.

Avoid:

- Appointing only the most technical person in each team.
- Making it a manager's job by default. Managers should support champions, not be them.
- Forcing it on someone. Ask for volunteers, then pick.

## The champion's job description

Copy and adapt:

```markdown
## AI Champion - [Team]

Time: about [3] hours a month, agreed with your manager. Term: 6 months, renewable.

You will:
1. Use the approved AI tools in your own work and try new features early.
2. Maintain the [Team] prompt library: add prompts that work, retire ones that
   don't, and note the known failure modes for each.
3. Be the first port of call for "can I use AI for this?" questions in your
   team, and route anything unclear about data or policy to [owner].
4. Run or co-run a 20-minute show-and-tell in your team once a month.
5. Attend the monthly champions meeting and bring: two wins (with the time or
   quality change, if you can measure it), one failure, and any policy friction.
6. Report incidents (wrong data pasted, bad output reaching a customer) to
   [security contact] the same day.

You will get:
- Early access to new tools and features, and training before others.
- A direct line to [rollout owner].
- Recognition in [performance review / internal comms / certificate].
```

## Running the program, month by month

**Month 0 (during the pilot).** Recruit champions from the pilot cohort of the [adoption playbook](ai-adoption-playbook.md). They take the [starter training](training-your-team.md) first, plus a 60-minute "champion session" on running a show-and-tell, curating a prompt library and handling data-policy questions.

**Month 1.** Each champion builds their team's prompt library with at least five prompts for recurring tasks. A good entry looks like this:

```markdown
### Weekly client status report
Use when: Friday status emails for active projects.
Prompt:
  "Here are my notes from this week on project [name]: [paste notes].
   Write a client status update with sections: Done this week, Next week,
   Risks and decisions needed. Under 200 words. Plain language. Flag any
   item in my notes that is ambiguous instead of guessing."
Check: dates and owner names - it sometimes swaps them.
Owner: [champion]. Last tested: [date].
```

**Month 2.** Champions run their first show-and-tells. The rollout owner hosts the first monthly champions meeting: go round the room for wins, failures and friction. Turn repeated friction into fixes (policy clarification, a missing connector, a training gap).

**Month 3 onward.** Champions help onboard each new rollout wave. Rotate one or two champions each quarter so the role does not become a burden, and so new people gain the skill.

## What the rollout owner must do in return

The program only works if champions see their input change things.

- **Act on reports.** If three champions say the same thing is blocked, fix it or explain why not, within the month.
- **Share wins across teams.** A good finance prompt may help operations too. Publish a short monthly digest.
- **Escalate risk.** If champions see Restricted data going into tools, that is a policy or tooling problem, not a people problem. Fix the tool access or the training.
- **Protect their time.** Agree the hours with their manager in writing.

## Measuring the program

- Prompt library entries per team, and how many are used (ask in the monthly pulse).
- Weekly active users per team, compared between teams with an active champion and without.
- Questions answered by champions versus escalated (a rising share answered locally is good).
- Champion retention: if champions quit the role after one term, the role is too heavy or too thankless.

Feed these into [measuring AI ROI](measuring-ai-roi.md).

## Where champions cannot help

- They cannot make a poor tool good, or fix a data access problem that IT has not solved.
- They should not decide policy. They raise issues; the owner decides.
- They are not accountable for colleagues' output. Each person owns their own work.

## Common mistakes

- **No time allocation.** "Do this on top of your job" lasts about six weeks.
- **Champions as cheerleaders.** If they only report wins, leadership loses its best early warning system. Ask explicitly for failures.
- **Only technical champions.** Sales, finance and HR need champions who do that work.
- **No rotation.** The same five people forever become a bottleneck and burn out.
- **Ignoring them.** Nothing kills a champion network faster than reports that go nowhere.

## Next steps

- The rollout plan this sits inside: [AI adoption playbook](ai-adoption-playbook.md)
- The session champions help run: [training your team](training-your-team.md)
- Prompt starting points for team libraries: [for managers](../playbooks/for-managers.md), [for sales](../playbooks/for-sales.md), [for support and ops](../playbooks/for-support-and-ops.md)
- The policy they help explain: [acceptable use policy](acceptable-use-policy.md)

## Sources

- Brynjolfsson, Li and Raymond, *Generative AI at Work*, NBER Working Paper 31161: <https://www.nber.org/papers/w31161>
