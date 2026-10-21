---
last-updated: 2026-08-11
difficulty: beginner
---

# Claude Certified Associate - Foundations (CCAO-F) - Practice Questions

15 questions for the CCAO-F exam, weighted toward output evaluation and validation (21%), workflow integration and solution design (16%), governance, risk, and responsible use (15%), prompting and task execution (14%), product and model selection (12%), configuration and knowledge management (12%), and troubleshooting and optimization (10%).

> **Cert page:** [exams/anthropic/claude-certified-associate-foundations/](../anthropic/claude-certified-associate-foundations/README.md)

---

### Question 1
**Scenario:** Claude produces a fluent, confident summary containing several statistics and two named source reports. A consultant asks how much she can trust it.

A. Fluency is not accuracy: statistics, quotes, and citations are the high-risk elements and must be verified against real sources before external use
B. Trust it if the summary is internally consistent
C. Claude never invents sources, so only the statistics need checking
D. Confident, well-structured output indicates the facts are correct

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Claude can state false claims and cite non-existent reports with complete fluency. Names, numbers, quotes, and citations are the falsifiable "checkables" that verification targets first. Internal consistency and polish tell you nothing about factual accuracy.
</details>

---

### Question 2
**Scenario:** A team debates how thoroughly to verify Claude outputs: one member wants every output fully fact-checked, another wants no checking at all.

A. Checking is only needed for outputs longer than a page
B. Never check; that defeats the time savings
C. Scale verification to stakes: skim a private brainstorm, spot-check an internal summary, fully verify a client deliverable, and require expert human review for legal, financial, or people decisions
D. Fact-check everything, always

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Proportionality is the tested principle, and it cuts both ways: under-verifying a client deliverable is a risk failure, and audit-grade review of a throwaway brainstorm is a cost failure. Risk level, not length, drives the depth of review.
</details>

---

### Question 3
**Scenario:** An analyst wants Claude's answers about an uploaded contract to be reliably grounded in the document.

A. Instruct Claude to answer only from the document, say so when the answer is not in it, and quote the supporting passage for each claim, then spot-check the quotes
B. Ask Claude to be extra careful
C. Upload the contract twice for emphasis
D. Ask Claude to review its own answer afterward and treat that second pass as full verification, since it will catch any claim the contract does not actually support, so no human check is needed

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Grounding plus required citations creates a fast audit trail; a quoted passage that is not actually in the document flags the output immediately. Self-review is a useful first filter but shares the model's blind spots, so it never substitutes for checking against the source.
</details>

---

### Question 4
**Scenario:** A delivery lead is deciding which step of a proposal workflow Claude should own.

A. Claude should only be used for spell-checking
B. Claude should do the whole workflow end to end, including final approval
C. Alternate authorship randomly between Claude and the team
D. Pick the language-shaped steps (drafting, summarizing, tailoring boilerplate) for Claude, keep pricing and final approval with humans, and define an explicit review gate before anything leaves the team

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Good solution design is surgical: Claude accelerates the drafting-shaped steps while accountable decisions and external release keep a human checkpoint. "Claude drafts, human approves" is the default pattern for deliverables.
</details>

---

### Question 5
**Scenario:** An operations manager pilots a Claude-assisted reporting workflow and wants to know if it is working before rolling it out to 30 people.

A. Baseline first, pilot with a few users, measure time and edits per report, then expand
B. Roll out to the whole department immediately; measurement can come later once everyone is using it and there is real data to look at in the quarterly review
C. Compare the pilot results against a different team that does different work and uses other tools
D. Ask the pilot users whether it feels faster, and roll it out if most of them say that it does

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The rollout pattern the exam rewards is pilot, measure against a baseline with named metrics, improve, then expand. Feelings and mismatched comparisons cannot show whether the workflow actually saves time or maintains quality.
</details>

---

### Question 6
**Scenario:** Team members keep copy-pasting Slack threads into Claude to get discussion summaries and draft replies.

A. Keep copy-pasting indefinitely, because Claude cannot be connected to Slack or any other workplace tool
B. This signals an integration fit: Claude in Slack puts the capability where the work lives
C. Print the threads and retype them into Claude, so that the pasted text is cleaned of any formatting
D. Ban Slack

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** When the work and its context live in another tool and copy-paste is the recurring friction, an integration is the designed solution. Workflow design includes choosing the surface where Claude meets the work, not just the prompt.
</details>

---

### Question 7
**Scenario:** A consultant with a personal Claude Pro account and access to her firm's Enterprise workspace needs to analyze a client's confidential financials.

A. Use whichever is open in her browser
B. Use the personal account but delete the chat afterward
C. Use the personal account; the underlying model is the same, so the output quality and the handling of the client's data are identical to the firm's workspace
D. Use the firm's Enterprise workspace, confirm the engagement permits AI processing, and share only the portions of the data the analysis needs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Client-confidential data belongs in the organization's governed workspace under commercial terms, subject to the engagement's rules, and minimized to what the task requires. Identical model quality is irrelevant; the difference is data terms and governance, and after-the-fact deletion does not repair using the wrong workspace.
</details>

---

### Question 8
**Scenario:** Claude refuses a request that a manager believes is legitimate.

A. File a bug report with the vendor straight away, because a refusal of a legitimate business request is always an error
B. Claim the request is for a work of fiction, so that the refusal no longer applies to the conversation, and proceed
C. Rephrase deceptively or split the task into innocent-looking pieces until it complies, since the refusal is only a keyword filter that a clever prompt can always get around
D. If the intent was misread, restate the purpose honestly; if policy forbids it, accept the refusal

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Honest clarification resolves most misunderstanding-refusals, and that is fine. Deceptive rephrasing, task-splitting, and fake framing are policy violations even when the underlying goal is legitimate - and a refusal of a genuinely prohibited task is the system working correctly.
</details>

---

### Question 9
**Scenario:** A consultant's prompt "write a proposal for the client" produced generic boilerplate.

A. Add the words 'be creative and specific' to the end of the prompt and keep everything else the same, then resubmit
B. Regenerate until something better appears
C. Rebuild the prompt with audience, scope, win themes, format and length limits, and a past proposal as example
D. Switch to the most capable model and keep the same one-line prompt, since a stronger model can infer the audience, scope, and win themes without being told

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Generic output is the signature of a context-free prompt. Role, task, context, constraints, format, and an example of what good looks like supply the information specificity requires. Regeneration re-rolls the same gap, and a stronger model just writes more eloquent boilerplate.
</details>

---

### Question 10
**Scenario:** A project lead needs Claude to produce a complete 20-page strategy document.

A. Ask for the document 20 times and pick the best
B. One giant prompt requesting all 20 pages at once, with every section's requirements listed up front in the first message so nothing is missed
C. Work stepwise: agree an outline first, draft section by section with review between steps, then run a final consistency pass
D. Large documents are impossible with Claude

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Decomposing big tasks with human checkpoints between steps produces better structure and lets you steer early, which is cheaper than repairing a monolithic draft. This is the core task-execution pattern for substantial deliverables.
</details>

---

### Question 11
**Scenario:** A manager must handle two jobs: a one-time deep analysis of a dense 90-page regulatory filing for the board, and 2-line summaries of 300 short routine meeting notes.

A. Most capable tier for the 90-page analysis; fastest, cheapest tier for the high-volume summaries
B. Use the most capable tier for the 90-page filing and for the high-volume simple summaries as well, since quality always outranks cost and speed
C. Use the fastest and cheapest tier for the filing and the high-volume summaries alike, since model choice only affects response speed
D. Model choice never affects the outcome, so the team should simply use whichever tier the first chat defaults to

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Tier matching is the tested skill: step up from the balanced default when quality dominates a hard one-off task, step down when volume and speed dominate simple tasks. Flagship-for-everything and cheapest-for-everything are both standard distractors.
</details>

---

### Question 12
**Scenario:** A team on client work is choosing between individual Free accounts and a Team plan.

A. Free accounts; the models answer the same questions, and data terms are the same on every plan, so there is no reason to pay for seats
B. A Team plan: commercial data terms, shared Projects, and collaboration are the point when business use involves client data
C. Plans differ only in usage limits
D. Personal Pro accounts with reimbursement

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Plan selection is a governance choice as much as a feature choice. Client work needs the commercial terms and shared, admin-manageable workspace that business plans provide; personal accounts for business data is the recurring wrong answer.
</details>

---

### Question 13
**Scenario:** A user retypes the same role, tone rules, and report template into every new chat for a weekly workstream.

A. Move the durable context into a Project: rules into instructions, the template into knowledge
B. Make the chats longer instead
C. Keep retyping it each time, because the repetition reminds the model what matters and improves results
D. Put the template into account-wide personal preferences so it applies to every chat, including unrelated ones

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Anything repeatedly retyped belongs in configuration at the right scope: workstream rules in project instructions, reference material in project knowledge. Account-wide preferences are the wrong scope; they drag workstream-specific rules into every unrelated chat.
</details>

---

### Question 14
**Scenario:** A shared Project's answers started citing outdated prices for every team member after a price change.

A. Delete the Project and have every team member rebuild their own copy from scratch over the next week
B. Curate the Project's knowledge: remove the stale rate card, upload the current one, and re-test
C. Switch the team to a more capable model, which will recognise on its own that the stored prices are out of date
D. Everyone adds "use the new prices" to each prompt

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A failure that hits every user of a Project regardless of prompt phrasing is a configuration problem, and stale knowledge files are the classic cause. Curation at the root fixes it permanently; per-prompt patches fight the configuration forever, and model capability cannot correct wrong reference data.
</details>

---

### Question 15
**Scenario:** After two weeks in one very long chat with several re-scopes and abandoned drafts, Claude keeps mixing old draft content into new sections.

A. Complain in the chat about the mistakes and tell Claude firmly to stop using any of the old draft content
B. Summarize the agreed decisions, verify the summary, and continue in a fresh chat seeded with it
C. Continue in the same chat and simply hope that it corrects itself once more of the new sections are written
D. Start completely blank and rebuild all of the context from memory at the start of every single session

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Long conversations accumulate contradictions and superseded drafts that degrade attention. The standard reset is distill, verify, restart warm; a Project holds the durable context for ongoing work. Complaints add tokens without removing the contaminated history, and a blank restart throws away signal along with noise.
</details>
