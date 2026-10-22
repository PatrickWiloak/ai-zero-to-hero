---
last-updated: 2026-10-22
difficulty: intermediate
---

# Claude Certified Architect - Foundations (CCAR-F) - Practice Questions

30 questions for the Claude Certified Architect - Foundations (CCAR-F) exam, weighted toward agentic architecture (27%), Claude Code configuration (20%), prompt engineering and structured output (20%), tool design and MCP (18%), and context and reliability (15%).

These are original practice questions, not vendor exam questions. Verify API details against the current documentation.

> **Cert page:** [exams/anthropic/claude-certified-architect-foundations/](../anthropic/claude-certified-architect-foundations/README.md)

---

### Question 1
**Scenario:** A team wants to know whether their task warrants an agent.

A. Check four things: multi-step and hard to specify, worth the cost and latency, model capable at it, errors catchable
B. Always build an agent, since a model-driven loop handles every task at least as well as fixed code can and needs less engineering effort
C. Agents are for chat only, so a task with no human conversation partner is better built as a plain workflow with fixed steps
D. Build an agent if the task uses tools, because any task that calls tools needs the model to drive the loop

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Complexity, value, viability, and cost of error are the four gates. A "no" on any of them means staying at a simpler tier: a single call for classification or extraction, or a code-controlled workflow where you own the branching.
</details>

---

### Question 2
**Scenario:** Which describes the tiers from simplest to most complex?

A. Workflow, agent, single call, with each tier adding one more step of model-controlled decisions to the one before
B. They are equivalent, so the choice between them is a matter of the preferred framework and the team's habits
C. Single LLM call, code-controlled workflow, then a model-driven agent loop
D. Agent, workflow, single call, because an agent is the least complex and a single call needs the most code

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Default to the simplest tier that meets the need. The distinction between a workflow and an agent is who decides the next step: your code in a workflow, the model in an agent. Model-driven control flow is what buys adaptability and what costs predictability.
</details>

---

### Question 3
**Scenario:** A custom-tool agent is being built and the team is writing the request-execute-loop by hand.

A. The SDK's tool runner drives the loop and still exposes per-turn hooks for approval, error interception and retries
B. Hand-writing the loop gives more control in every case, because the runner hides each turn from the code and cannot be intercepted
C. That is the only option, since the API leaves the request, execute and respond steps for the application to write by hand
D. Loops are not needed, because the model runs each tool call itself and returns the final answer in one response to the first request

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** "I need control" is rarely a reason to hand-roll: the runner yields the assistant message before tools execute, so approval gating and interception fit inside it. Write the loop yourself only for control the runner genuinely does not expose.
</details>

---

### Question 4
**Scenario:** The team confuses the Tool Runner with the Claude Agent SDK.

A. The Tool Runner is a regular SDK helper that loops over your tools; the Agent SDK packages the Claude Code harness with its built-in tools
B. They are the same product under two names, and the Agent SDK is only the newer release of the Tool Runner helper in the regular SDK, with a longer name
C. The Agent SDK has no tools of its own, so you must define the file, bash and search tools before it can act on a repository
D. The Tool Runner hosts your compute, running each tool in an Anthropic-managed sandbox for the length of the session

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Both supply a harness and leave deployment to you; the difference is scope. The Tool Runner has no built-in tools and no filesystem access. Managed Agents is the third option, where Anthropic runs both the loop and a per-session sandbox.
</details>

---

### Question 5
**Scenario:** Should an action be a bash command or a dedicated tool?

A. Start with bash for breadth; promote an action to a dedicated tool when you need to gate, render, audit or parallelize it
B. Always bash for flexibility, since one string covers any command and the harness never needs to tell the different actions apart or gate them
C. Always dedicated tools, so that every action is a typed call and no shell ever runs inside the agent's environment, whatever the task
D. It makes no difference, because the harness sees the same request whichever way the action is described to the model

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A bash tool gives your harness one opaque string for every action, so it cannot tell a parallel-safe search from a destructive push. A dedicated tool gives typed arguments the harness can intercept, confirm, or run concurrently.
</details>

---

### Question 6
**Scenario:** A tool description is one vague sentence and its parameters have no descriptions.

A. Add urgent capitalized instructions to the description so the model always calls the tool
B. Shorter is always better, since a long description uses up context and the model picks tools by name
C. Fine, the schema is enough, since the model can infer each parameter's purpose from its name and type
D. Under-described: write several sentences covering what the tool does, when to use it, when not to, and what each parameter means

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Under-description is the more common failure than over-description, and being prescriptive about *when* to call a tool measurably improves selection. What does not belong in a description is behavioral steering or worked examples; those go in the system prompt or a skill.
</details>

---

### Question 7
**Scenario:** MCP in one sentence.

A. A prompt format for combining tool results and system instructions in one message
B. An open protocol for exposing tools, prompts and resources to a model through a standard server interface
C. A model architecture that routes each request among experts during inference
D. A hosting platform where a provider runs your tools so models can reach them online

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MCP standardizes the integration surface so a tool written once works across clients. The API's MCP connector requires two halves together: `mcp_servers` declaring the connection, and a matching `mcp_toolset` entry in `tools` referencing it by name.
</details>

---

### Question 8
**Scenario:** A prompt must produce guaranteed-valid JSON.

A. Prefill the assistant turn with an opening brace, so the model continues the object and cannot start with prose
B. Structured outputs with a JSON schema
C. A stop sequence at the closing brace, which ends the response as soon as the object is complete and valid
D. Ask politely for JSON only and retry on parse failure up to three times, then fall back to a default value

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Prefilling was the older technique and now returns a 400 on current models. When migrating a prompt off it, the surrounding machinery goes too: the stop sequences, the regex extraction, and the retry-on-parse-failure loop all existed to serve the old mechanism.
</details>

---

### Question 9
**Scenario:** A system prompt carried over from an older model is full of "CRITICAL: You MUST" instructions and the model now overtriggers a tool.

A. Lower the temperature to zero, which stops the model overweighting any instruction
B. Add more emphasis to the tool's description, so that the model learns the exact conditions under which it must not call the tool at all
C. Dial the language back to plain statements; current models follow the system prompt closely, so emphasis over-applies
D. Remove the tool from the request, since a model cannot call a tool it was never given

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** When every instruction is marked critical, the markers stop carrying information, and an anxious prompt produces a hedging model. Emphasis is a tested fix for one demonstrably underweighted instruction, not a default register.
</details>

---

### Question 10
**Scenario:** Where should thinking depth be controlled?

A. By instructing "think step by step" in the prompt, which sets the depth the model reasons to before it answers
B. By raising `max_tokens`, since a higher cap makes the model reason for longer on every request that it receives
C. Through configuration: adaptive thinking plus the effort parameter
D. It cannot be controlled, because the model decides its own thinking depth for each request without any setting

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** On thinking models the prose incantation is redundant, and instructions to think or not to think are prompt cruft worth deleting. Effort is the configured control, and it also affects tool-use rate and how far the model scopes its work.
</details>

---

### Question 11
**Scenario:** A long-running agent's context window fills with old tool results.

A. Restart the conversation with only the latest user message, so that the context starts empty on every task and the old results are gone
B. Delete the oldest messages arbitrarily until the window has room, keeping the most recent turns intact and the system prompt in place
C. Raise `max_tokens` so that the model has more room in the window to hold the old tool results
D. Context editing to clear stale tool results, compaction near the limit, and memory for state that outlives a session

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The three operate at different scopes: editing prunes within a session, compaction summarizes within a session, memory persists across sessions. Many long-running agents use all three. Arbitrary truncation breaks tool-use pairing and thinking-block ordering.
</details>

---

### Question 12
**Scenario:** An agent's prompt cache keeps missing after the team added a mode switch that edits the system prompt mid-session.

A. Accept the cost, since a cache miss on each mode switch is simply part of using a system prompt that is changed in the middle of a session
B. Editing the system prompt invalidates the cached prefix; on supporting models, append a system-role message to `messages` instead
C. Disable caching, since a prompt that changes during a session cannot benefit from caching of any part of the request
D. Add more breakpoints, so that the changed system prompt is cached again at each of the new positions in the request

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Render order is tools, then system, then messages, so anything appended after the cached history leaves it intact. Changing the tool set or the model invalidates the cache in the same way; use tool search or a subagent respectively to avoid it.
</details>

---

### Question 13
**Scenario:** An agent loop must not run forever.

A. Increase the context window, so the loop has enough room to keep running until the model decides on its own that the task is finished
B. Bound it: maximum iterations, a wall-clock timeout, a token budget, and detection of repeated states
C. Trust the model to stop once it judges the task done
D. Use a larger model, which finishes in fewer iterations

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Non-termination is the default failure mode of an agent loop, and the model's own judgment about being finished is not a control. Server-side tool loops add a related case: a turn can stop with `pause_turn`, which you resume by re-sending rather than treating as complete.
</details>

---

### Question 14
**Scenario:** A repository uses a `CLAUDE.md` and skill files.

A. Longer is always better, because more instructions give the model more guidance for every task it is given
B. They replace the system prompt, so the API call no longer needs one once the files are in the repository, and the model reads them first
C. They are documentation for humans only, and the model never reads them when it works in the repository, so they cost nothing in context
D. They are context loaded into the working set, so each paragraph is paid for on use and should hold what only the author knows

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The deletion test is whether the model could already know it. Keep the audience, environment facts, quality bar, and tool contracts; remove restatements of trained defaults and workarounds for failures the current model no longer has.
</details>

---

### Question 15
**Scenario:** A tool with side effects, such as sending email, is exposed to an agent.

A. Trust the loop, since the model asks before sending anything the user may not want sent
B. Log the calls and review them later, alerting on email to addresses outside the company domain
C. Validate inputs and gate destructive or irreversible actions behind confirmation, with the runner or a manual loop
D. Add a line to the system prompt telling the model never to send email without explicit approval

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The tool executes automatically whenever the model requests it, so the gate has to be in code. With the runner you gate inside the tool function or intervene on the yielded message before it executes; the system prompt is advisory and injected content can compete with it.
</details>

### Question 16
**Scenario:** A support system receives refund requests, technical questions and sales enquiries. Each type is handled best by a different prompt and tool set, and the type can be identified reliably from the message.

A. One large prompt that covers all three types, with every tool attached to every request
B. Routing: classify the input first, then send it to a prompt and tools specialised for that type
C. An autonomous agent that decides its own plan for every message, with no classification step
D. Fine-tune one model on all three types so that it learns to handle each without separate prompts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Routing fits when inputs fall into distinct categories that are better handled separately and the classification is reliable. One giant prompt makes each type compete for attention and exposes tools that do not apply. A fully autonomous agent adds cost and unpredictability where a fixed split works. Fine-tuning is a heavy fix for what is a prompt-and-tools design problem.
</details>

### Question 17
**Scenario:** A research assistant gets open-ended questions. How many sources it must search, and which ones, cannot be known until it starts reading.

A. Parallelization with a fixed set of three searches that always run at the same time
B. Prompt chaining with a hard-coded sequence of five steps
C. A single model call with a very large max_tokens setting
D. Orchestrator-workers, where a lead model plans the subtasks at run time

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The deciding detail is that the subtasks cannot be predicted in advance, which is exactly when an orchestrator plans them at run time. Parallelization and chaining both need the subtasks fixed ahead of time. One long call cannot search sources it has not been given.
</details>

### Question 18
**Scenario:** Marketing copy is translated into French. Reviewers have clear, written criteria (tone, length, terminology), and a second pass that critiques the draft against them measurably improves it.

A. Evaluator-optimizer: one call drafts, another critiques it against the criteria, in a loop
B. Routing between two translation prompts based on the length of the source text
C. A single call at temperature 0, since lower temperature gives the best translation
D. Orchestrator-workers, with one worker per paragraph running in parallel and no separate review step at the end

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Evaluator-optimizer suits tasks with clear evaluation criteria where iterative feedback demonstrably helps, and the loop needs an exit (criteria met or a maximum number of rounds). Routing by length does not apply the criteria. Temperature changes randomness, not adherence to a style guide. Splitting by paragraph without review drops the step that adds the quality.
</details>

### Question 19
**Scenario:** An agent handles account changes for a bank. Most requests are routine, but some involve suspected fraud or amounts above a limit, and those must reach a person.

A. Tell the model in the system prompt to be careful with large amounts and trust it to handle them
B. Let the agent finish every request and have staff review a random 5% sample each week
C. Define explicit escalation criteria, give the agent an escalation tool, enforce the hard limits in code, and pass a summary of the case to the human
D. Remove the agent from the workflow entirely, since no part of it can be automated safely

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Human oversight works when the triggers are explicit, the hard limits are enforced outside the model, and the person receiving the case gets enough context to act without starting over. A prompt-only rule is advisory. Random sampling finds problems after the money has moved. Dropping the agent throws away the routine work it does well.
</details>

### Question 20
**Scenario:** Security requires that Claude Code can never read `.env` files on any developer's machine, even if a developer adds an allow rule in their own settings.

A. A note in the project `CLAUDE.md` asking Claude not to open `.env` files
B. A deny rule in the managed policy settings
C. A deny rule in each developer's `.claude/settings.local.json`
D. A custom slash command that reminds developers to keep secrets out of `.env` files

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Managed policy settings sit at the top of the settings hierarchy and cannot be overridden by user or project files, so the rule holds on every machine. `CLAUDE.md` is guidance the model reads, not an enforced permission. A local settings file is personal and editable by the developer it is meant to constrain. A slash command enforces nothing.
</details>

### Question 21
**Scenario:** A team wants the project formatter to run automatically after every file Claude Code edits, every time, without relying on the model remembering to do it.

A. Add "always run the formatter after editing" to `CLAUDE.md`
B. Create a custom slash command that runs the formatter, and ask developers to type it after each edit
C. Add the formatter to the allow list so the model never needs permission to run it
D. Configure a PostToolUse hook that matches the edit and write tools and runs the formatter

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Hooks are deterministic: they run on the lifecycle event whether or not the model thinks of it, and PostToolUse fires after a tool such as an edit completes. A `CLAUDE.md` line is a suggestion the model may skip. A slash command depends on a person remembering. An allow rule removes a prompt but does not make anything run.
</details>

### Question 22
**Scenario:** A team wants Claude Code to review each pull request in CI and emit a result that a later pipeline step can parse.

A. Run `claude -p` (print mode) with JSON output and a restricted tool list
B. Start an interactive Claude Code session on the CI runner and have a script type into it
C. Copy the diff into the Claude.ai chat interface and paste the answer back into the PR
D. Give the CI job a user account with full permissions so that no prompt can block it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Print mode is the headless way to run Claude Code in scripts and CI, a structured output format makes the result machine-readable, and limiting tools keeps an unattended run within bounds. Driving an interactive session from a script is fragile. Manual copy and paste is not automation. Broad permissions on an unattended job are the opposite of least privilege.
</details>

### Question 23
**Scenario:** A prompt includes three long contracts (about 40,000 tokens) and asks one question about them. Answers sometimes mix up which contract a clause came from.

A. Put the question first and the contracts after it, with no separators between documents
B. Summarise each contract to one paragraph first and send only the summaries, whatever the question asks
C. Put the contracts at the top, each in its own tagged block with its source name, and the question at the end
D. Split the question into three separate calls that each see only the first contract

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Anthropic's long-context guidance is to place long documents near the top and the query at the end, and to wrap each document in tags with metadata such as its source so the model can tell them apart. Untagged documents invite the mix-up described. Summaries may drop the clause in question. Sending only the first contract cannot answer a question about the others.
</details>

### Question 24
**Scenario:** An extraction prompt pulls invoice fields into JSON. When an invoice has no purchase order number, the model sometimes invents a plausible one.

A. Raise the temperature so that the model explores more options before answering
B. Make the field nullable and say to return null when it is absent
C. Remove the purchase order field so that it can never be wrong
D. Add a second call that asks the model whether it invented anything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A required field with no permitted "absent" value pushes the model to fill it. Allowing null, and saying when to use it, gives an honest way out. Higher temperature makes fabrication more likely, not less. Dropping the field loses data the business needs. A self-check call adds cost and is less reliable than removing the pressure to invent.
</details>

### Question 25
**Scenario:** A prompt has three few-shot examples, all short, all positive and all about the same product. Outputs now copy their length and tone even for long, negative inputs.

A. Delete the examples and rely on instructions alone, since examples always cause overfitting
B. Add ten more examples that are just like the existing three
C. Move the examples into the user turn so that they carry less weight
D. Use varied examples that cover edge cases, wrapped in example tags

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Models follow examples closely, so examples should be relevant, diverse and clearly marked. Three near-identical ones teach an unintended pattern. More of the same makes it worse. Removing examples throws away a strong tool. Moving them does not fix the lack of variety.
</details>

### Question 26
**Scenario:** A `get_order` tool sometimes fails because the order ID does not exist. Today the code raises an exception and the whole agent run crashes.

A. Return a tool_result with `is_error: true` and an actionable message
B. Return an empty tool_result with no content, so the model carries on as if nothing happened
C. Catch the exception and retry the same call five times with the same ID
D. Stop the agent and ask the user to restart the conversation from the beginning

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Reporting the failure as an error result with an actionable message lets Claude recover, for example by asking the user for the correct ID. An empty result hides the failure and invites a made-up answer. Retrying a call that cannot succeed wastes time. Ending the run throws away the conversation over a recoverable error.
</details>

### Question 27
**Scenario:** An MCP server must expose a read-only database schema that the host application can attach to the context, and a separate action that runs approved queries.

A. Expose both as prompts, since prompts are the only primitive the host can attach
B. Expose both as tools, since MCP has no other primitive
C. Expose the schema as a resource and the query action as a tool
D. Expose the schema as a tool and the query action as a resource

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** MCP has three server primitives. Resources are data that the application controls and attaches as context; tools are actions the model decides to call; prompts are templates a user chooses. The schema is context and the query is an action. Option D swaps the two, and the other options ignore the primitives that exist.
</details>

### Question 28
**Scenario:** An agent has 40 tools, many with overlapping names such as `search`, `find_records` and `lookup`. It often picks the wrong one.

A. Raise max_tokens so that the model has more room to think about which tool to use
B. Consolidate overlapping tools, with distinct names and "use this when" descriptions
C. Add more tools that cover the same ground, so that any choice the model makes is a reasonable one
D. Set tool_choice to force the first tool in the list on every request

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Tool selection depends on the names and descriptions. Overlap creates ambiguity, so fewer, clearly separated tools with "use this when" guidance fix the root cause. Output length does not resolve ambiguity. More overlapping tools make it worse. Forcing one tool breaks every request that needs another.
</details>

### Question 29
**Scenario:** A coding agent works on a migration that takes several hours and far more tokens than one context window holds.

A. Pick the model with the largest context window and hope the task fits
B. Restart the agent from scratch each time the context fills, with no record of earlier work
C. Keep every tool result in full, since deleting anything risks losing a detail
D. Have the agent keep structured progress notes outside the context (for example a progress file and git commits) and use compaction or a fresh context that resumes from them

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Long-running work survives context limits when state lives outside the window: a progress file, a task list and version control let a compacted or fresh context pick up where it left off. A larger window only delays the problem. Starting over with no notes repeats work. Keeping every tool result is what fills the window in the first place.
</details>

### Question 30
**Scenario:** The main agent must answer a question that requires searching a large codebase. The search returns thousands of lines, most irrelevant, and they crowd out the agent's working context.

A. Delegate the search to a subagent that returns only a short summary
B. Paste the full search output into the main context and ask the agent to ignore what does not matter
C. Turn off the search tool and ask the user to find the code themselves
D. Lower the temperature so that the agent pays more attention to the relevant lines

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Subagents isolate context: the noisy exploration happens in their window and only the condensed result returns to the main agent. Pasting everything in is the problem being solved. Removing the tool removes the capability. Temperature does not change what is in the context.
</details>

---

## Where to go deeper

- [Claude Architect Foundations track page](../anthropic/claude-certified-architect-foundations/README.md) - notes, practice plan, strategy
- [Claude Certified Architect - Professional practice questions](anthropic-claude-architect-professional.md) - the next level
- [Agentic loops](../../learn/concepts/agentic-loops.md) - the loop in plain English
- [MCP explained](../../learn/concepts/mcp-explained.md) - the protocol
- **[📖 Claude agents and tools documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)** - primary source
