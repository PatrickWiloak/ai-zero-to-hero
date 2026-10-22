---
last-updated: 2026-10-22
difficulty: beginner
---

# Claude Certified Associate - Foundations (CCAO-F) - Practice Questions

30 questions for the CCAO-F exam, weighted toward output evaluation and validation (21%), workflow integration and solution design (16%), governance, risk, and responsible use (15%), prompting and task execution (14%), product and model selection (12%), configuration and knowledge management (12%), and troubleshooting and optimization (10%).

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

---

### Question 16
**Scenario:** Claude's summary of a 40-page supplier contract includes a sentence in quotation marks that it says is the exact termination clause. The summary will be pasted into a note to the client's legal team.

A. Accept it, since Claude was given the full contract and quotation marks show it copied the clause
B. Ask Claude in the same chat whether the quote is exact, and keep it if Claude confirms that it is
C. Search the contract for the quoted text and check the wording and the section before sending it
D. Remove the quotation marks so the sentence reads as a paraphrase and no longer needs checking

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Claude can paraphrase while presenting text as a direct quote, so anything that goes to a client as a verbatim quote should be checked against the source itself. Asking Claude to confirm its own output is not independent evidence. Dropping the quotation marks hides the problem instead of checking whether the clause says what the note claims.
</details>

---

### Question 17
**Scenario:** A manager asks Claude whether a proposed office move will save money. Claude's analysis concludes strongly in favor, which is exactly what the manager hoped to hear.

A. Present the analysis as is, since Claude has no stake in the outcome and so cannot be biased
B. Ask Claude for the strongest case against the move, then check the key figures it relied on
C. Ask Claude to rewrite the analysis in a more confident tone so the board finds it persuasive
D. Run the same prompt three more times and adopt the conclusion that appears most often

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A welcome conclusion deserves more scrutiny, not less, and the way a question is framed can steer the answer. Asking for the counter-case surfaces what the analysis left out, and the figures it rests on still need checking. Repeating the same prompt repeats the same framing, and a more confident tone adds persuasion without adding evidence.
</details>

---

### Question 18
**Scenario:** A marketing lead asks Claude which competitors changed their pricing last month. Web search is turned off for this chat.

A. Trust the answer, since Claude is trained on very large amounts of up-to-date information
B. Ask Claude to list the competitors' prices from memory and treat any gaps as no change
C. Rephrase the question to say "as of today" so Claude answers with the most recent information
D. Turn on web search, then check that the cited sources are recent and actually say this

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Claude's built-in knowledge stops at a training cutoff, so recent events need a live source such as web search, and the cited pages still need checking for date and content. Saying "as of today" does not give Claude new information, and treating gaps as "no change" turns missing knowledge into a false finding.
</details>

---

### Question 19
**Scenario:** An account team wants Claude to help with routine client update emails. The team lead worries about errors reaching clients.

A. Let Claude send the emails directly, since routine updates carry little risk for the account
B. Stop using Claude for client email, since any error in front of a client is too costly to risk
C. Have Claude draft each email and have the account owner review and send it themselves
D. Have Claude draft each email and send it automatically, with a weekly sample checked later

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A good workflow puts Claude on the drafting, where it saves the most time, and keeps a human checkpoint before anything leaves the firm, where an error costs the most. Sending without review moves the risk to the client, and a later sample catches mistakes only after they have been sent. Dropping Claude entirely gives up the time savings to avoid a risk that review already controls.
</details>

---

### Question 20
**Scenario:** A support director wants every one of 2,000 inbound emails a day to be read, tagged and given a draft reply automatically, with no one typing prompts.

A. Give every support agent a Claude Pro account and ask them to paste in each email as it arrives
B. Bring in the engineering team to build it on the Claude API, since it is an automated pipeline
C. Create a shared Project with the tagging rules and ask one person to process the emails in a single chat
D. Use Artifacts to build a form that agents fill in by hand with each email and its tag

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** High-volume, system-to-system processing with no human in the chat is an API job for a technical team, not a chat workflow. Pasting 2,000 emails by hand, in one chat or across many accounts, recreates the manual work the director wants to remove. An Artifact form still needs a person for each email.
</details>

---

### Question 21
**Scenario:** An HR analyst is approved to use the company's Enterprise workspace to find themes in 500 employee survey comments. The export also contains names, employee IDs and home addresses.

A. Upload the full export, since the Enterprise workspace is approved and so any data is fine to include
B. Upload the comments one at a time across several chats so that no single chat holds all the data
C. Ask Claude to ignore the names, IDs and addresses, and keep the export as it is
D. Remove the names, IDs and addresses first, since the theme analysis does not need them

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** An approved tool is necessary but not sufficient: responsible use also means sharing only the data the task needs. Theme analysis needs the comments, not identities. Telling Claude to ignore fields still puts them in the conversation, and splitting the upload across chats changes nothing about what was shared.
</details>

---

### Question 22
**Scenario:** A consultant used Claude heavily to draft a client report. Her firm's policy requires that AI-assisted work be disclosed to clients, and the client later finds an error in one table.

A. She remains accountable for the report, and should follow the disclosure policy and correct the error
B. The error is Claude's responsibility, since the table was generated by the model and not by her
C. She need not disclose the AI use, since the client is paying for the result rather than the method
D. She should regenerate the full report with a more capable model so the client sees a better version

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The person who delivers the work owns it, whatever tools helped produce it, and firm policy on disclosure applies whether or not anything goes wrong. Blaming the model does not transfer accountability. Skipping disclosure breaks policy, and a regenerated report is not a correction of the error the client found.
</details>

---

### Question 23
**Scenario:** A partner keeps rewriting Claude's draft client emails because they never sound like her: too formal and too long.

A. Tell Claude to "sound more natural" at the end of each request and hope the tone improves
B. Switch to the most capable model, since a stronger model will pick up her style without help
C. Give Claude two or three of her past emails as examples of the tone, length and structure she wants
D. Ask Claude to write in a casual tone, since any informal style will be closer to the one she uses

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Examples show style more precisely than adjectives can, so a few real samples of the target voice are the most direct fix. "Sound more natural" and "casual" are vague, and Claude has to guess what they mean. A bigger model still has no idea what her emails look like.
</details>

---

### Question 24
**Scenario:** A director asks Claude to "put together a plan for the offsite." Claude produces a detailed agenda for a two-day event, but the offsite is one afternoon for six people.

A. Accept the agenda and cut it down by hand, since Claude cannot know such details anyway
B. Ask Claude to try again with the same request, since a second attempt often comes out shorter
C. Ask Claude for a shorter plan, without saying how short or what it should leave out
D. Give the key facts up front, or ask Claude to list what it needs to know before it starts

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Claude fills missing details with reasonable guesses, and the guesses can be far off. Stating the constraints, or inviting Claude to ask clarifying questions first, fixes the cause. Retrying the same vague request leaves the guess in place, "shorter" is still vague, and trimming by hand does the work Claude should have done.
</details>

---

### Question 25
**Scenario:** A finance lead wants Claude to build a small interactive savings calculator she can adjust and refine over several rounds, then share with her team.

A. Ask for the calculator logic as plain text in the chat and rebuild it in a spreadsheet by hand
B. Use Artifacts, where Claude builds the calculator as a standalone piece she can iterate on and share
C. Use Claude Code, since anything interactive needs a developer tool and a code repository
D. Upload a spreadsheet to a Project and ask Claude to describe how a calculator would work

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Artifacts are built for substantial outputs that a user views, edits through further prompts, and shares, including small interactive pages. Plain text and a description both leave the building to her. Claude Code targets software engineering in a codebase, which is far more than this task needs.
</details>

---

### Question 26
**Scenario:** A project team re-uploads the same planning documents to Claude every few days because the files change often, and answers keep coming from stale versions.

A. Upload the files to a new chat each morning and delete the older chats so that they cannot be used
B. Paste the full text of every document into each request so that Claude always has the latest copy
C. Connect Claude to the document store with a connector so that it reads the current files
D. Switch to a more capable model, since it will notice which uploaded version is the newest one

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Connectors let Claude read live sources, which suits information that changes often and keeps getting re-uploaded. Daily re-uploads and pasting are the manual work that causes stale answers. Model choice does not help when the newest information was never provided.
</details>

---

### Question 27
**Scenario:** An Enterprise admin learns that staff could connect Claude to personal cloud drives. Company policy allows only the approved document system.

A. Use the organization's admin settings to allow only the approved connectors for all members
B. Email staff asking them not to use personal drives and check a few chats each month for misuse
C. Add a line to each Project's instructions telling Claude not to read from personal cloud drives
D. Remove Claude access for anyone who has connected a personal drive at any point in the past

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** On organization plans, admins control which connectors and integrations members can enable, so the policy can be enforced in configuration. An email and spot checks rely on people complying. A Project instruction is guidance to the model, not an access control, and removing access punishes users instead of fixing the setting.
</details>

---

### Question 28
**Scenario:** A consultant uses Claude's memory across chats for her regular work. She now needs a one-off chat about a sensitive personnel matter that she does not want saved to her history or carried into future chats.

A. Use her usual chat and ask Claude at the end to forget what was discussed in that conversation
B. Start the chat inside a Project, since Projects keep their contents out of history entirely
C. Use the chat as normal and then delete her whole account history once the matter is closed
D. Use an incognito chat, which is not saved to her chat history or used for memory

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Incognito chats are designed for exactly this: they are not saved to chat history and do not feed memory. Asking Claude to forget does not change what was stored. Projects keep their own context and history rather than hiding it, and wiping all history to protect one chat destroys unrelated work.
</details>

---

### Question 29
**Scenario:** A user pastes a link to a report on the company intranet, which needs a login, and asks Claude to summarize it. Claude replies that it cannot open the page.

A. Ask again with "please try harder", since the page may load on a second attempt
B. Download the report or copy its text and give that to Claude, or use an approved connector
C. Send Claude the login details for the intranet so that it can sign in and read the page
D. Ask Claude to summarize the report from the title in the link, since that is usually enough

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Pages behind a login are not reachable from Claude's web tools, so the content has to be provided directly or through a connector the organization has approved. Retrying does not change access. Sharing credentials breaks security policy, and a summary built from a title is invented content.
</details>

---

### Question 30
**Scenario:** A team lead complains that Claude's meeting summaries run to a full page when she wants five bullet points she can paste into a status email.

A. Switch to the most capable model, since stronger models write more concisely without being asked
B. Ask Claude to be brief, since one word is enough for it to understand the length she has in mind
C. Say exactly what is wanted: five bullets, one line each, covering decisions and owners
D. Shorten each summary by hand, since Claude cannot reliably follow a length instruction

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A precise description of the output (count, length, content) removes the guesswork that produces long summaries. "Be brief" is vague. A bigger model has the same missing information, and editing by hand gives up on a fix that a clearer instruction provides.
</details>
