---
last-updated: 2026-08-11
difficulty: advanced
---

# Claude Certified Architect - Professional (CCAR-P) - Practice Questions

15 questions for the Claude Certified Architect - Professional (CCAR-P) exam, weighted toward the heavier blueprint domains: Integration (19%), Solution Design and Architecture (17%), Evaluation, Testing and Optimization (16%), Governance, Safety and Risk Management (14%), Stakeholder Communication and Lifecycle Management (14%), Claude Models, Prompting and Context Engineering (13%), and Developer Productivity and Operational Enablement (7%).

These are practice questions written for this repo, not real exam items. Verify API details against the current documentation.

> **Cert page:** [exams/anthropic/claude-certified-architect-professional/](../anthropic/claude-certified-architect-professional/README.md)

---

### Question 1
**Scenario:** A research task splits into six independent sub-questions, each requiring heavy reading.

A. Delegate each sub-question to a subagent, so each gets a fresh context and only its report returns
B. Increase the context window so that all six sub-questions and their source material fit in one conversation
C. Run six separate applications, each with its own prompt and its own copy of the sources, and merge by hand
D. One long single-threaded loop that reads the sources for each sub-question in turn and keeps every note in context

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Fan-out is the case delegation is for: parallel threads, independent contexts, and a coordinator whose context stays small because it reads reports rather than raw material. The cost is a round trip and a re-briefing per delegation, so it is wrong for a task you could finish in a few tool calls.
</details>

---

### Question 2
**Scenario:** A production claims agent is pinned to a dated model snapshot. The provider announces that snapshot's deprecation with a six-month window. An engineer proposes switching to an auto-updating model alias so migrations stop being necessary.

A. Move to a cloud platform where snapshots are never retired and keep the dated snapshot
B. Wait until the deprecation date, then fix whatever prompts break once users report them
C. Keep pinning; eval and red-team the successor, fix regressions, phase it in with rollback, and tell stakeholders
D. Accept the proposal: an auto-updating alias eliminates migration work, and the team can spend the six months on features

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A model version change is a behavior change to the product, so it goes through the same gate as a code release: eval diff, phased rollout, rollback path, stakeholder notice. An auto-updating alias trades scheduled migrations for silent, unreviewed behavior changes, and cloud platforms retire model versions on their own schedules too.
</details>

---

### Question 3
**Scenario:** A healthcare enterprise requires that prompts and completions are never retained after the response is served, and that the deployment is covered for PHI under HIPAA.

A. Sign a BAA, use a HIPAA-eligible endpoint, and arrange contractual ZDR; verify each path separately
B. Strip PHI client-side with a redaction step before each call; then retention and the BAA no longer matter for the deployment
C. Retention is already zero by default on every endpoint, so only a BAA is needed
D. Set a retention flag on each API request so that the prompt and completion are discarded as soon as the response has been served to the user

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** ZDR is a contractual arrangement for qualified customers, not a request-time flag, and default handling permits short-term retention for abuse detection. HIPAA coverage requires a signed BAA on a HIPAA-eligible endpoint. Minimization (B) is good practice but does not satisfy a hard requirement on its own, since PHI can still reach the model in a clinical workload.
</details>

---

### Question 4
**Scenario:** Prompt caching is designed for an agent whose model must change mid-session for a cheap sub-task.

A. Add a cache breakpoint before the switch, so the cached prefix is reused by the cheaper model for the sub-task
B. Caches are model-scoped, so a switch invalidates them; use a subagent on the cheaper model
C. Switch the model on the same conversation and rely on the cache to carry the cached prefix across to the new model for the sub-task and back again
D. Use a longer cache TTL, so the cached prefix is still available when the cheaper model takes over the sub-task

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Three things invalidate the whole prefix: changing the tool set, changing the model, and editing the system prompt. Each has a workaround: tool search appends rather than swaps, a subagent isolates the model change, and a system-role message in `messages` leaves the cached history intact.
</details>

---

### Question 5
**Scenario:** An agent has 200 tools available but only a few are relevant per request.

A. Load every schema on every request, which keeps the tool array stable but puts all 200 definitions into context each time
B. Tool search with deferred loading, so only relevant schemas enter context and are appended rather than swapped
C. Shorten the descriptions of all 200 tools to save room
D. Split the tools into 200 agents, one per tool, with a router

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The appended-not-swapped property is what preserves the prompt cache, which is why tool search is the scaling answer rather than rebuilding the tool array per request. Note the search tool itself must not be deferred, and at least one tool must remain non-deferred.
</details>

---

### Question 6
**Scenario:** Claude chains five tool calls, each returning a large payload that is filtered and discarded.

A. Batch the calls into one request, so the five payloads are returned together and all stay in context for later turns
B. Programmatic tool calling: Claude scripts the tool calls in the code execution container and returns only the final output
C. Accept the token cost, since each intermediate payload is needed in context so that the model can reason about the next call in the chain
D. Use a bigger context window, so that the five large payloads fit without any change to how the tools are called

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** With standard tool use every intermediate result lands in context and costs tokens forever after. PTC keeps the intermediate data in the running script, so token cost scales with the final output rather than with everything the tools returned.
</details>

---

### Question 7
**Scenario:** An indirect prompt injection arrives in a document the agent retrieved.

A. Assume it may succeed: scope each credential narrowly, check authorization in code at the tool boundary, confirm irreversible actions, and treat output as untrusted
B. Filter the retrieved input for suspicious phrases such as 'ignore previous instructions' before it reaches the model's context
C. Use a larger model, since larger models are better at telling an instruction from the data that surrounds it
D. Instruct the model in the system prompt to ignore any instructions that appear inside retrieved documents

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** No classifier reliably separates instructions from data in natural language, so the design goal is bounding the consequence. The tool boundary is the last non-model control that can refuse, which is why authorization belongs there rather than in the prompt.
</details>

---

### Question 8
**Scenario:** An agent's behavior must be debuggable three days after a bad run.

A. Application logs only, with request IDs and status codes, which show that each call finished but not what it contained
B. Ask the model to explain what happened, then store its explanation with the run
C. The final output, saved with a timestamp for each run, which the reviewers can compare with the expected answer later
D. Full tracing: each prompt, tool call with arguments, observation, and decision, tied together by a trace ID

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A wrong answer is usually a retrieval or observation problem, invisible from the output. A post-hoc explanation from the model is a plausible narrative reconstructed from the same context, not a record of what happened.
</details>

---

### Question 9
**Scenario:** An agent must be evaluated before production.

A. Final-answer accuracy measured on a held-out set of questions, reported as the percentage of answers that match the reference
B. Published benchmark scores for the model, since a strong result on public tasks predicts behavior in production
C. Trajectory-level evaluation (task success, tool calls, steps, cost) plus adversarial cases, rerun often
D. Latency only, measured at the 95th percentile, since fast agents keep users

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Final-answer accuracy hides agents that reach the right answer through unsafe or wasteful paths. Running the suite on prompt edits as well as model upgrades matters because both change behavior, and injection resistance in particular regresses silently.
</details>

---

### Question 10
**Scenario:** A pilot's exit gate requires a 90% task-success score before general rollout. The pilot lands at 84%, and the executive sponsor pushes to launch anyway because a competitor just shipped.

A. Lower the gate to 84% so that the pilot passes, and record the new threshold as the standard for later launches
B. Hold the pre-agreed gate: show the evidence, diagnose top failures, propose bounded remediation with a re-test date, and allow a narrow interim launch only for a segment that clears it
C. Launch, because the gate was only a guideline and the competitor's release changes the value of waiting
D. Escalate to the sponsor's manager, asking them to rule on whether the launch can go ahead on the 84% result

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Go/no-go gates exist precisely for the moment pressure and sunk cost argue for launching; agreeing on thresholds before the phase is what makes the decision evidence-based rather than political. Moving the goalposts (C, A) destroys the gate's value for every future launch. Offering a scoped alternative keeps the conversation constructive without shipping a known-failing experience.
</details>

---

### Question 11
**Scenario:** A long conversation approaches the context window limit.

A. Increase `max_tokens`, which raises the limit on the length of the reply and so leaves more room for history
B. Truncate the oldest messages until the conversation fits, keeping the most recent turns and the system prompt
C. Server-side compaction, appending the full response content each turn so compaction blocks are kept
D. Start a new conversation and paste a short summary of the old one in as the first user message

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The trap is appending only the extracted text: the compaction block is what the API uses to replace the compacted history on the next request, so dropping it silently loses the state. Arbitrary truncation additionally breaks tool-use pairing.
</details>

---

### Question 12
**Scenario:** An enterprise requires that model inference run on their cloud provider's infrastructure.

A. All platforms are identical, so any client class and any model ID works the same way on every one of them
B. Only the first-party API is available, so inference cannot run on the enterprise's own cloud provider's infrastructure at all
C. Only Bedrock exists as a third-party platform, so the design must be built on Amazon's infrastructure
D. Claude is on Amazon Bedrock, Google Agent Platform (formerly Vertex AI), and Microsoft Foundry, each with its own client class and feature set

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Availability differs per feature and per platform, so the architecture question is which capabilities the design depends on. Model IDs also differ: Bedrock prefixes them, Vertex uses bare IDs with its own version separator for dated snapshots.
</details>

---

### Question 13
**Scenario:** An agent should persist learnings across sessions.

A. A memory surface it can read and write, with guidance on what to record and what not to duplicate
B. Longer context windows, so that everything learned in one session is still in context when the next one begins
C. Compaction, which summarizes earlier turns in a session so the agent keeps its learnings as the conversation grows
D. A larger system prompt that the team edits after each session to add the notes that the agent should keep

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Memory is the cross-session mechanism; context editing and compaction operate within one. The design detail that matters is telling it *when* to consult and write memory: agents under-reach for capabilities that need an explicit decision to use them.
</details>

---

### Question 14
**Scenario:** The team wants Anthropic to run the agent loop and host the tool-execution sandbox.

A. That is not offered, so the team must run the loop and the sandbox on its own infrastructure
B. The Agent SDK does this, hosting the loop and the sandbox on Anthropic's servers
C. Managed Agents: a versioned agent config plus sessions that each get a container, driven through an event stream
D. The Tool Runner does this, running the loop and executing tools in an Anthropic-hosted sandbox

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Tool Runner and the Agent SDK both supply a harness and leave hosting to you; Managed Agents supplies both. The versioning is the reason agents are separate objects: sessions pin to a version, so you can iterate without breaking runs in flight.
</details>

---

### Question 15
**Scenario:** A safety layer must constrain what the agent will do.

A. A word blocklist covering the terms and phrases that the agent must never produce or act on
B. Layered controls, measuring violation rate and also false refusal rate
C. Lower temperature, so the agent's outputs are more predictable and less likely to drift into unsafe territory
D. Shorter responses, since a brief reply gives the agent less room to produce anything that breaks the policy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Safety is a trade-off curve, so measuring only violations optimizes toward an over-blocking product that fails a different way. Blocklists sit badly on both axes: trivially evaded, and prone to catching benign text.
</details>

---

## Where to go deeper

- [Claude Certified Architect - Professional cert page](../anthropic/claude-certified-architect-professional/README.md) - notes, practice plan, strategy
- [Claude Architect Foundations practice questions](anthropic-claude-architect-foundations.md) - the level below
- [Agent and tool security](../../safety/security/agent-security.md) - question 7 in depth
- [Prompt injection defense](../../safety/security/prompt-injection-defense.md) - the attack and the controls
- **[📖 Claude agents and tools documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)** - primary source
