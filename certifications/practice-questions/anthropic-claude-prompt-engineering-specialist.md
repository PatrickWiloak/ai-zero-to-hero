---
last-updated: 2026-10-22
difficulty: intermediate
---

# Claude Prompt Engineering Specialist (Self-Directed Track) - Practice Questions

30 questions for the Claude Prompt Engineering Specialist track, weighted toward prompt fundamentals (18%), system prompts and role (16%), reasoning elicitation (16%), then structure, examples, evaluation, and cache-aware prompt design.

This is a self-directed study track rather than an Anthropic exam. Prompting guidance shifts between model generations, so verify against current documentation.

> **Cert page:** [exams/anthropic/claude-prompt-engineering-specialist/](../anthropic/claude-prompt-engineering-specialist/README.md)

---

### Question 1
**Scenario:** What belongs in a prompt, in one principle?

A. What only you know: the audience, the product, environment facts, the quality bar, constraints and their reasons
B. Everything that might be relevant, including background the model already knows, so that nothing is left out and no later guesswork is needed
C. As few words as possible, because short prompts are cheaper and the model fills in any missing details sensibly and reliably
D. Restatements of good behavior, such as being accurate, helpful, and careful, which the model already follows without being told

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Context is never cruft; restating trained defaults is. "Be accurate and helpful" adds nothing, while "this goes to compliance reviewers who need the source cited" changes the output. Too-short prompts produce generic results because the model fills gaps with safe defaults.
</details>

---

### Question 2
**Scenario:** A prompt reads "CRITICAL: You MUST ALWAYS verify before answering. NEVER guess. IMPORTANT: be thorough."

A. Over-emphasized: when everything is marked critical the markers carry no information, and an anxious prompt produces a hedging, over-cautious model
B. Needs more emphasis, such as capital letters and repeated warnings throughout, so that the model treats every instruction as the highest priority and stops cutting corners
C. Correct for all models, because strong wording is a reliable way to get compliance and has no downside on current models
D. Well-calibrated emphasis, since each rule carries a marker that tells the model exactly how seriously to take it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Forcefulness was genuinely needed on older, less steerable models. Current models follow the system prompt closely, so the same text over-applies. Emphasis is a tested, scoped fix for one demonstrably underweighted instruction, not a default register.
</details>

---

### Question 3
**Scenario:** A prompt says "try to include a summary if possible" for a summary that is actually required.

A. Repeat the line three times in different places, so that the model sees the requirement often enough to treat it as mandatory
B. Hedges are now read literally as permission to skip; state the requirement plainly
C. Fine as written, because a polite request is the best way to ask and current models understand that it is actually required
D. Add emphasis with capital letters and an exclamation mark, which shouts louder but leaves the hedged wording of the requirement

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Over-emphasis and under-emphasis are the same defect from opposite directions, and both come from writing for a model with different steerability. Say exactly what you mean at normal volume.
</details>

---

### Question 4
**Scenario:** A prompt contains "think step by step" and instructions to use `<scratchpad>` tags.

A. Add more reasoning instructions, such as asking for a longer chain of thought and a final check, to improve accuracy further
B. They improve output on every model and should be kept in all prompts, because explicit reasoning cues are always helpful
C. Keep them for reliability, since removing reasoning instructions makes the model skip steps and produce lower quality answers, especially on multi-step tasks with many conditions
D. On thinking models these are redundant; control reasoning with adaptive thinking and the effort parameter

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** These are idioms from an era before reasoning was natively trained and configurable. Instructions telling the model *not* to reason are worse still: they can increase leakage of internal markup into the visible response rather than suppressing it.
</details>

---

### Question 5
**Scenario:** A prompt uses XML tags to delimit a document and the instructions.

A. Useful: explicit delimiters make it unambiguous which text is data and which is instruction, especially with long inputs
B. Only JSON works for separating data from instructions, so XML tags confuse the model and should be replaced with JSON keys everywhere
C. Unnecessary, since the model can always tell where a long document ends
D. XML tags are deprecated, and current models ignore them, so plain headings are the only supported way to separate text from instructions

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Structural delimiting remains sound practice for separating content from instruction. What has been superseded is using tags to *force output shape*, which structured outputs now handles as a decoding constraint rather than a prompting convention.
</details>

---

### Question 6
**Scenario:** A prompt embeds one gold-standard output example.

A. Risky: examples are the strongest signal in a prompt, so one example freezes its length, tone, and structure; use several deliberately varied examples labeled illustrative
B. Add more examples of the same shape, which reinforces the pattern and gives the model a strong template for each output, so every response matches the sample closely in length and tone
C. Examples never matter, because the model follows the written instructions alone and ignores any sample outputs in the prompt
D. Ideal, because one gold-standard example shows the model precisely what is wanted and avoids ambiguity about the format

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The model matches what it sees, so a single example becomes a template rather than an illustration. Examples written for an older model are worse: they freeze that model's behavior into the new one. Keep examples that pin a genuinely format-sensitive output.
</details>

---

### Question 7
**Scenario:** A prompt has fifteen "do not" lines.

A. Add more prohibitions covering every failure seen so far, so that the model has a complete list of behaviors it must avoid
B. Describing success beats enumerating failure, and a prohibition can anchor the model toward that failure
C. Prohibitions are always wrong, and a prompt should never state what the model must not do
D. Comprehensive coverage, since a long list of explicit rules is the safest way to prevent each known failure from recurring, and every incident should add one more line to the list

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The test for each line is provenance: does it encode a real constraint with a reason, or is it a workaround for an older model's habit? Keep prohibitions whose failure reproduces on the current model; rewrite the rest as positive statements.
</details>

---

### Question 8
**Scenario:** A system prompt runs to 4,000 words of numbered steps for a judgment task.

A. Convert it to bullets, which makes it easier to read but leaves the same prescriptive structure and the same word count
B. More detail is better, so keep adding steps for each case the model gets wrong until every situation is covered
C. Over-prescriptive: prompts written for prior models are often too prescriptive for current ones and reduce output quality; state outcomes, constraints, and how to verify, keeping numbered steps only where order truly matters
D. Split it into two prompts of 2,000 words each, which divides the length but keeps the over-prescriptive steps in each part

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Prompting effort should scale with how far the task is from what the model does naturally. Fragile operations where exactly one sequence is safe keep their exact scripts; open-ended judgment work does better with the goal and the constraints.
</details>

---

### Question 9
**Scenario:** A prompt says "you will be graded on completeness; there are hidden tests."

A. Add the rubric to the prompt as a hidden section, so that the model knows which items will be scored and can plan its answer
B. Effective motivation, since telling the model that it is being evaluated makes it try harder and check its work more carefully
C. It describes the scoring apparatus instead of the requirement, and pushes effort toward appearing watched; state every requirement the grader checks and never describe the grader
D. Remove all quality language from the prompt, including the stated requirements, so that the model is not pushed by any pressure

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** If a requirement matters, say it as a requirement. Grader vocabulary is a proxy that the model optimizes toward instead of the underlying goal, which is exactly the substitution you do not want.
</details>

---

### Question 10
**Scenario:** How should a prompt change be validated?

A. Ship it and watch for complaints from users, then revise the prompt if people report that the quality has dropped
B. Read the new output and judge it, using your impression of a few examples to decide if the change was an improvement
C. Ask the model whether the prompt is good, and apply any changes it recommends, since it knows what it responds best to
D. An evaluation set with defined metrics, run before and after, ideally changing one thing at a time

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Prompting is empirical and intuitions about what helps are unreliable. Asking the model to assess its own prompt is self-report, not measurement. Changing one thing at a time is what lets a regression be attributed to its cause.
</details>

---

### Question 11
**Scenario:** A prompt embeds "current date: {today}" at the top of the system prompt.

A. Dates cannot be provided to the model in a prompt, because it has no clock and any date text would be ignored
B. It sits at the front of the cached prefix and invalidates everything after it on every request; inject dynamic context later in the messages instead
C. Move it to the end of the system prompt, which still sits inside the cached prefix and changes the cache key each day
D. Good practice for temporal grounding, since placing the date first helps the model anchor all later content to the correct day, and the cost of a changing prefix is small compared with the benefit

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Caching is a prefix match, and the render order is tools, then system, then messages. Anything varying per request belongs after the last breakpoint. A message at turn five invalidates nothing before turn five.
</details>

---

### Question 12
**Scenario:** A prompt contains lines nobody can justify, added after specific incidents on a retired model.

A. Keep them, they are harmless, because extra instructions never reduce quality and may protect against a failure that returns, so deleting any of them adds risk with no benefit
B. Rewrite them more forcefully so that the model gives them clear priority over the rest of the instructions in the prompt
C. Treat them as removal candidates: prompts accumulate the union of every generation's workarounds, and specific outdated instructions actively degrade behavior
D. Add a comment explaining each, which documents the history for readers but leaves the outdated instructions in the model's context

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The question for every emphatic line is which failure, on which model, it prevented, and whether that failure still reproduces. Removal is a hypothesis to test, not a conclusion: probe behavior before and after, and re-add in minimal form if a cut regresses.
</details>

---

### Question 13
**Scenario:** A skill's frontmatter description carries urgent language about when to invoke it.

A. All urgency should be removed from every part of a prompt, including skill descriptions, because strong wording harms any model
B. Descriptions should be one word long, since a short name is enough for the model to decide whether to invoke the skill
C. Same problem as an over-emphatic system prompt, because urgent wording in any text always causes over-triggering and rigid behavior
D. Different: text whose job is routing may legitimately carry calibrated urgency, since skills currently under-trigger; text whose job is behavior should explain rather than shout

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Trigger text and behavioral text look identical to a search, so classify by function before editing. Ideally the trigger wording is tuned against a trigger evaluation rather than intuition.
</details>

---

### Question 14
**Scenario:** A response is longer than the product wants.

A. Add "be concise" and hope, which is vague, leaves the model to guess what to cut and how short the response should be, and gives different lengths on different runs
B. Give a concrete instruction about what to include and what to drop, and prefer positive examples of the desired concision over telling the model what not to do
C. Lower the effort setting, which changes how much the model reasons and does not directly control the length of the final answer
D. Cap the output tokens at a small limit, which truncates the answer mid-sentence instead of teaching the model what to include and what to leave out, and so harms quality

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Numeric output caps tuned against an older model's verbosity starve reasoning on hard problems, and truncate rather than shorten. Lowering effort changes reasoning depth without reliably changing visible length. Selectivity is the lever: drop what would not change what the reader does next.
</details>

---

### Question 15
**Scenario:** A prompt is being written for a new model generation.

A. Reuse the old prompt unchanged, because a prompt that worked well on the previous model will also work on its successor, and rewriting it only adds the risk of new errors
B. Re-baseline from the old prompt: remove workarounds the new model no longer needs, and add guidance for its new behaviors, since prompts are per-model artifacts
C. Always shorten it, because newer models need fewer instructions and any extra text will lower the quality of the output, so every migration should cut the prompt by half or more
D. Always lengthen it, because newer models can use more detail, and adding extra guidance can only improve what they produce

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Matching a prompt to a new model sometimes means adding text, not only cutting it. A line that is load-bearing on one generation is cruft on the next, and the reverse, which is why each model release is a trigger to re-audit rather than a reason to reuse.
</details>

---

### Question 16
**Scenario:** A voice assistant's prompt says "Never use ellipses." Claude follows it most of the time, but still uses other symbols that the text-to-speech engine reads aloud badly.

A. Repeat the rule three times in capital letters so that it carries more weight in the prompt
B. Add a list of every symbol that should not appear, and update the list after each new failure
C. Explain why: the output is read aloud by a speech engine, so it should avoid symbols it cannot say
D. Move the rule to the very end of the prompt, since the last instruction is the one followed most

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Giving the reason behind an instruction lets Claude generalize to cases the rule did not name, here any symbol a speech engine handles badly. Capitals and repetition add emphasis, not understanding, and can cause overreaction elsewhere. A growing blocklist only covers failures already seen, and position alone does not supply the missing context.
</details>

---

### Question 17
**Scenario:** A data-cleaning prompt describes five operations in one long paragraph. Claude sometimes runs them in the wrong order, and the order matters.

A. Write the operations as a numbered list in the order they must run, and say that order matters
B. Put the most important operation first in the paragraph and leave the rest of it unchanged
C. Split the paragraph into five separate requests sent in parallel and merge the results afterwards
D. Ask Claude to choose the best order itself, since it can see which operations depend on others

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** When sequence matters, numbered steps make the order explicit instead of leaving it to be inferred from prose. Moving one operation forward leaves the rest ambiguous. Parallel requests cannot respect an order, and handing the ordering decision to Claude reintroduces the guess that caused the problem.
</details>

---

### Question 18
**Scenario:** A legal-review prompt asks Claude to flag risky clauses in vendor contracts. The flags are generic and miss issues that an experienced lawyer would raise.

A. Ask for a longer answer, since a longer review covers more clauses and so catches more problems
B. Lower the effort setting, so that Claude focuses only on the clauses that matter most
C. Add "be accurate" and "be thorough" to the end of the prompt, so Claude takes the task seriously
D. Give Claude a specific role in the system prompt, such as general counsel reviewing for a buyer

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A specific role in the system prompt sets the perspective, priorities and domain vocabulary Claude applies, which is what generic flags lack. Length does not add expertise. "Be accurate" is a wish rather than guidance, and lowering effort trades depth away on a task that needs it.
</details>

---

### Question 19
**Scenario:** An app sends one long user message on each call that mixes the assistant's standing rules with the specific customer question for that call.

A. Move everything into the system prompt, including the customer question, so all text has the same weight
B. Keep the standing rules in the system prompt and put each call's question and data in the user turn
C. Put the rules after the customer question in the user turn, so Claude reads them most recently
D. Send the rules in a separate request first, then send the question in a second request

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The system prompt is the place for stable operator instructions such as role, rules and format, while the user turn carries what varies per call. That split is clearer for the model and keeps the stable prefix identical between calls, which also makes it cacheable. Separate requests share no context, so rules sent earlier are simply gone.
</details>

---

### Question 20
**Scenario:** A team enables adaptive thinking for a hard planning task, then adds a 30-line script telling Claude exactly which steps to think through and in what order. Quality goes down.

A. Lengthen the script with more steps, since the model needs more guidance when it is thinking
B. Turn thinking off and keep the script, since scripts and thinking are not meant to be combined
C. Replace the script with a high-level instruction to think carefully, then read the thinking to refine it
D. Move the script into the user message, since thinking only reads instructions from the user turn

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Anthropic's guidance is that with thinking enabled, Claude usually does better with a high-level instruction to think deeply than with prescriptive step-by-step direction, and that you can then steer from what the thinking shows. A longer script tightens the constraint that hurt quality. Turning thinking off removes the capability the task needs, and where the script sits is not the issue.
</details>

---

### Question 21
**Scenario:** A coding prompt asks Claude to write a date-parsing function. The functions look right but sometimes fail on edge cases that would have been caught by simply running a few inputs.

A. Ask Claude to verify its work before finishing, for example by writing and running test cases
B. Tell Claude that the function will be reviewed by a senior engineer, so that it writes more carefully
C. Ask Claude to explain each line of the function in comments, so mistakes are easier to see later
D. Ask Claude to produce three versions of the function and choose the longest one to use

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Asking Claude to check its own work against concrete tests before finishing catches errors in the same turn, and is a documented technique for coding and analysis. Mentioning a reviewer is pressure, not a check. Comments document the code without testing it, and length has no relation to correctness.
</details>

---

### Question 22
**Scenario:** A prompt includes a contract and a policy, each in its own XML tags. The instructions say "check the document against the rules," and Claude sometimes treats the policy as the document.

A. Remove the tags so that both texts read as one continuous section and Claude sees the whole picture
B. Rename both tags to `<document>` so that Claude treats them the same and compares them evenly
C. Put both texts inside one `<data>` tag, so that Claude knows the contents are not instructions
D. Refer to each by its tag name, such as "check the contract in `<contract>` against `<policy>`"

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Tags work best when they have clear, distinct names and the instructions refer to them by name, which removes any doubt about which text plays which part. Removing tags, giving both the same name, or merging them under one tag all make the two inputs harder to tell apart.
</details>

---

### Question 23
**Scenario:** An old prompt gets JSON back by prefilling the assistant turn with an opening brace. After moving to a current Claude model, those requests return a 400 error.

A. Prefill the assistant turn with a longer partial object instead of only the opening brace
B. Move the opening brace into the system prompt, so that the model starts its response with it
C. Remove the prefill and use structured outputs with a JSON schema to get the format reliably
D. Add the opening brace to the end of the user message, so that the model carries it on as JSON

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Prefilling the last assistant turn is not supported on current models, so any prefill, long or short, still fails. Structured outputs replace the technique and constrain the response to a schema rather than nudging it. Moving a brace into the system or user text is only a hint and gives no format guarantee.
</details>

---

### Question 24
**Scenario:** A support-ticket prompt includes four examples, all short password-reset tickets. Claude now answers billing disputes with the same short, password-focused style.

A. Remove all examples, since examples always cause the model to copy their content too closely
B. Use varied examples that cover different ticket types and lengths, including tricky edge cases
C. Add ten more password-reset examples, since more examples make the pattern easier to follow
D. Move the examples to the end of the prompt, since examples placed last have less influence

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Claude picks up patterns from examples, including ones you did not intend, so examples should be relevant and diverse enough that the intended pattern is the only consistent one. More of the same strengthens the wrong pattern. Removing examples loses the format guidance, and moving them does not change what they teach.
</details>

---

### Question 25
**Scenario:** A prompt mixes three sample answers into the middle of its instructions with no markers. Claude sometimes treats lines from the samples as rules to follow.

A. Wrap each sample in `<example>` tags, grouped in `<examples>`, so they are clearly marked as samples
B. Rewrite the samples as instructions, so that every line in the prompt is a rule Claude must follow
C. Delete the samples and describe the desired output in a single long sentence instead of showing it
D. Put each sample in bold so that it stands out visually from the surrounding instruction text

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Anthropic recommends wrapping examples in `<example>` tags (with several grouped in `<examples>`) so they are distinct from instructions. Turning samples into rules changes their meaning, deleting them loses the demonstration, and bold text is formatting, not structure.
</details>

---

### Question 26
**Scenario:** A product manager asks a prompt engineer to "make the summaries better" and wants to start editing the prompt straight away.

A. Start with small wording changes and ask the product manager whether each version looks better
B. Switch to a more capable model first, since a stronger model is the fastest way to improve quality
C. First agree measurable success criteria, such as required facts and a length limit, and a test set
D. Copy a published summarization prompt from the prompt library, since it was already tested

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Prompt work starts with defining success in specific, measurable terms and building tests against them; without that, "better" is opinion and changes cannot be compared. A library prompt was not tested on this product's criteria. A model switch may help, but there is still no way to tell.
</details>

---

### Question 27
**Scenario:** A team builds its prompt test set from 20 inputs it wrote by hand. The prompt scores well, but users still report failures on real messages.

A. Lower the pass mark on the test set until it reflects how often users report failures in production
B. Rewrite the 20 hand-written inputs so that they are harder and test the prompt more strictly
C. Ask Claude to generate 200 more synthetic inputs in the same style as the original 20
D. Add a sample of real production inputs, including the reported failures, to the test set

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A test set only predicts production if it looks like production, so real traffic and known failures belong in it. Synthetic inputs in the same style repeat the same blind spots, harder hand-written cases still come from the authors' assumptions, and moving the pass mark hides the gap instead of measuring it.
</details>

---

### Question 28
**Scenario:** A prompt has a 6,000-token block of reference material that never changes, followed by a short user question that changes on every call. The team wants to use prompt caching.

A. Put the user question first so that it is cached, and the reference material after it
B. Keep the reference material first and place the cache breakpoint at the end of it
C. Cache only the user question, since the reference material is already short enough
D. Place a cache breakpoint inside the user question so that its common words are reused

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Caching reuses an exact prefix, so stable content goes first and the breakpoint marks the end of the part that never changes. Anything that varies, like the question, comes after it. Putting the question first, or inside the cached part, makes every prefix different, so nothing is ever reused.
</details>

---

### Question 29
**Scenario:** To keep outputs fresh, a prompt picks five few-shot examples at random from a pool of 50 on every call. The examples sit in the system prompt, and cache hits are near zero.

A. Move the examples into a separate request so that they no longer count toward the prompt's tokens
B. Increase the cache time-to-live so that each random set of examples stays cached for longer
C. Use a fixed set and order of examples in the cached prefix, and add variety elsewhere if needed
D. Add a cache breakpoint before each example so that at least some of them are reused on each call

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Any change in the prefix invalidates everything after it, so randomly chosen examples in the system prompt make each request unique. A fixed, ordered example set keeps the prefix stable. A longer TTL or more breakpoints cannot help when the content differs, and examples in a separate request are not in the conversation at all.
</details>

---

### Question 30
**Scenario:** A prompt passes a 150-page annual report and asks one detailed question. Answers are often vague and mix up figures from different sections.

A. Ask Claude to first pull the relevant passages into `<quotes>` tags, then answer from those quotes
B. Ask the question twice in the same prompt, once before and once after the report text
C. Lower the effort setting so that Claude spends less time reading parts of the report that do not matter
D. Ask Claude to answer in one sentence so that it has less room to mix up the figures

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** For long documents, asking Claude to extract the relevant quotes first helps it cut through the rest of the text and grounds the answer in specific passages, which can also be checked. Repeating the question adds nothing new, lowering effort reduces the attention the task needs, and a one-sentence limit hides errors rather than preventing them.
</details>

---

## Where to go deeper

- [Claude Prompt Engineering Specialist track page](../anthropic/claude-prompt-engineering-specialist/README.md) - notes, practice plan, strategy
- [Claude Architect Foundations practice questions](anthropic-claude-architect-foundations.md) - the architecture track
- [Prompt engineering](../../learn/concepts/prompt-engineering.md) - plain-English primer
- [Structured outputs](../../learn/concepts/structured-outputs.md) - the replacement for format-forcing prompts
- **[📖 Claude prompt engineering documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)** - primary source
