---
last-updated: 2026-08-11
difficulty: intermediate
---

# Claude Certified Architect - Foundations (CCAR-F) - Practice Questions

15 questions for the Claude Certified Architect - Foundations (CCAR-F) exam, weighted toward agentic architecture (27%), Claude Code configuration (20%), prompt engineering and structured output (20%), tool design and MCP (18%), and context and reliability (15%).

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

---

## Where to go deeper

- [Claude Architect Foundations track page](../anthropic/claude-certified-architect-foundations/README.md) - notes, practice plan, strategy
- [Claude Certified Architect - Professional practice questions](anthropic-claude-architect-professional.md) - the next level
- [Agentic loops](../../learn/concepts/agentic-loops.md) - the loop in plain English
- [MCP explained](../../learn/concepts/mcp-explained.md) - the protocol
- **[📖 Claude agents and tools documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)** - primary source
