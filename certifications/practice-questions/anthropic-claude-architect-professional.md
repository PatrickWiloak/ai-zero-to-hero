---
last-updated: 2026-10-22
difficulty: advanced
---

# Claude Certified Architect - Professional (CCAR-P) - Practice Questions

30 questions for the Claude Certified Architect - Professional (CCAR-P) exam, weighted toward the heavier blueprint domains: Integration (19%), Solution Design and Architecture (17%), Evaluation, Testing and Optimization (16%), Governance, Safety and Risk Management (14%), Stakeholder Communication and Lifecycle Management (14%), Claude Models, Prompting and Context Engineering (13%), and Developer Productivity and Operational Enablement (7%).

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

### Question 16
**Scenario:** Claude returns three `tool_use` blocks in one assistant turn. The integration runs the tools concurrently, one of them fails, and the client sends each result back in its own user message, dropping the failed one. Over time the agent stops making parallel calls.

A. Retry the failed tool silently until it succeeds, then send all three results back in separate user messages
B. Disable parallel tool use for the whole agent, so each turn produces only one call and one result
C. Return only the two successful results in one message, and describe the failure in a text block
D. Send all three `tool_result` blocks in one user message, marking the failed one with `is_error: true`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Every `tool_use` needs a matching `tool_result`, and parallel results belong together in a single user message. Splitting them across messages teaches the model to stop calling in parallel, and dropping a result breaks the pairing. A failure is reported with `is_error: true` so Claude can react. Silent retries hide a real fault, and turning parallelism off throws away latency gains to fix a client bug.
</details>

---

### Question 17
**Scenario:** A platform team is publishing one MCP server for a ticketing system so that dozens of agents running in different services and regions can share it.

A. Expose it over the Streamable HTTP transport as a remote server with authentication
B. Ship it over the stdio transport and have each agent host connect to the team's copy across the network
C. Copy the server's tool definitions into every agent's tool array so no transport is needed at all
D. Run it over stdio inside the platform team's own laptop session and share the session with each agent

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The MCP specification defines stdio for a server launched as a local subprocess of the client, and Streamable HTTP for a server reached over the network. A shared, multi-consumer server is the remote case, so it needs HTTP with proper authorization. stdio cannot be reached across the network, and copying tool definitions duplicates the schemas without the server that executes them.
</details>

---

### Question 18
**Scenario:** Each night a compliance job must classify 200,000 archived emails. Results are needed by the next morning, and finance wants the run to cost as little as possible.

A. Send the requests through streaming calls so that the output arrives faster and is billed at a lower rate
B. Split the work across several API keys so that each key stays under its rate limit during the run
C. Submit them through the Message Batches API and match each result to its request by `custom_id`
D. Use the largest model at maximum effort so that no email ever needs a second pass in the morning

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Batch processing suits work that is not latency sensitive and is billed at half the standard rate. Results can come back in any order, so they must be joined on `custom_id`, never by position. Streaming changes delivery, not price. Spreading load over keys dodges limits without cutting cost, and maximum effort raises the bill on a task that rarely needs it.
</details>

---

### Question 19
**Scenario:** A pipeline parses Claude's JSON output into a typed object. About one response in 300 has a missing required field or a trailing comment, and the parser fails in production.

A. Add a second prompt that asks Claude to check its own JSON, and retry whenever the parser still fails
B. Use structured outputs with a JSON schema, or `strict: true` on the tool, so the response is constrained
C. Raise the temperature slightly so that the model is less likely to repeat the same broken output pattern
D. Write a regular expression that strips comments and fills in any missing fields with default values

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Structured outputs (`output_config.format`) and strict tool use constrain generation to the schema, which removes the parse failure class rather than catching it later. A self-check prompt and retries still fail some of the time and cost extra calls. Regex repair silently invents values for required fields, which is worse than an error.
</details>

---

### Question 20
**Scenario:** A SaaS vendor builds one RAG assistant that serves 400 customer tenants from a shared vector store. A security review asks how one tenant is kept from seeing another tenant's documents.

A. Tell the model in the system prompt which tenant it is serving and to ignore other tenants' content
B. Give each tenant a different model so that its answers can only come from its own fine-tuned weights
C. Rely on embedding similarity, since documents from other tenants will rarely be close to the question
D. Apply the tenant ID as a mandatory filter in the retrieval layer, set from the authenticated session

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Isolation has to happen before content reaches the model: the retrieval query is filtered by a tenant ID taken from the verified session, not from anything the user or model can change. A prompt instruction is not an access control, since the leaked text is already in context. Similarity is a ranking signal, not a boundary, and per-tenant models do not address the shared store at all.
</details>

---

### Question 21
**Scenario:** A European bank using the first-party Claude API requires that model inference for a specific workload run only in the United States, and that it can prove where each request ran.

A. Add a system prompt line that tells Claude it is operating under US data rules for that workload
B. Deploy the client SDK on servers in a US region, since inference runs wherever the caller is hosted
C. Set the `inference_geo` request parameter, then confirm the location in `usage.inference_geo`
D. Use a model alias without a version, since aliases are routed to US capacity by default

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `inference_geo` is a top-level Messages API parameter that controls where inference runs, and the response usage block reports the geography actually used, which gives the evidence the bank needs. Where the client runs does not decide where the model runs. A prompt line changes wording, not infrastructure, and aliases say nothing about location.
</details>

---

### Question 22
**Scenario:** A team wants to use Claude as an LLM judge to grade 10,000 support answers per week against a rubric, replacing most human review.

A. First grade a sample with both humans and the judge, measure agreement, and fix the rubric until it holds
B. Ask the judge to give a score from 1 to 100 so that its ratings have finer detail than a pass or fail
C. Use the same prompt that produced the answers, so the judge shares the context the writer had
D. Trust the judge from the start, since a capable model grades more consistently than people do

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A judge is a measuring instrument, so it must be calibrated against human labels before its numbers drive decisions, and rechecked when the rubric or model changes. Fine-grained scales usually reduce agreement rather than add precision; clear criteria with discrete outcomes grade more reliably. Reusing the writer's prompt invites the judge to share its blind spots.
</details>

---

### Question 23
**Scenario:** An agent sends the same 30,000-token system prompt and tool set on every request with a cache breakpoint, yet `usage.cache_read_input_tokens` is zero on every call. The system prompt starts with the current time.

A. Add more cache breakpoints throughout the system prompt so that at least one of them is always matched
B. Switch to a model with a larger context window, since the cache only works on smaller prompts
C. Increase the cache time-to-live so that the cached prefix survives until the next request arrives
D. Move the timestamp after the last breakpoint, because any change in the prefix invalidates the cache

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Caching is an exact prefix match over tools, then system, then messages. A value that changes every call at the top of the system prompt means no request ever shares a prefix with the one before. Volatile content goes after the last breakpoint. Extra breakpoints and longer TTLs cannot help when the bytes differ, and context size has nothing to do with it.
</details>

---

### Question 24
**Scenario:** To cut cost, an architect proposes a cascade: a small model answers first, and a larger model retries whenever the small one seems unsure. The workload is long multi-turn sessions with a large cached system prompt.

A. Build the cascade, since a cheaper first attempt always lowers the cost per completed task
B. Measure the larger model at a lower effort setting first, since caches are model-scoped
C. Send every request to both models and keep whichever answer is shorter, to save output tokens
D. Use the smallest model for every turn and accept a lower success rate as the price of savings

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lower effort on a capable model often holds quality at a fraction of the token spend, and a single model keeps one cache namespace. A cascade loses cache reuse across models, and retries add turns, so it can cost more per completed task even when each request is cheaper. Calling both models doubles the bill, and accepting lower success is a quality decision, not an optimization.
</details>

---

### Question 25
**Scenario:** A finance agent can call a `send_payment` tool. Policy says no payment above $10,000 may leave without a named human approving it.

A. Add a sentence to the system prompt telling the agent to ask for approval before large payments
B. Lower the agent's effort for payment tasks, so it is more cautious with high-value transfers
C. Gate the tool in code: pause above the threshold until an approver confirms, and log the decision
D. Ask the agent to describe each payment in its final answer so a reviewer can reverse it later

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A hard policy needs a hard control at the tool boundary, where code can refuse regardless of what the model was persuaded to do. The approval and its result go into the audit trail. A prompt instruction can be skipped or injected around, effort does not create caution, and after-the-fact review cannot recall money already sent.
</details>

---

### Question 26
**Scenario:** A customer of a Claude-based assistant files a GDPR erasure request. The assistant stores conversation logs, embeds user notes in a vector index, and lets the agent write memory files.

A. Delete the user's account record, since the logs and other stores point to it and become anonymous
B. Ask Anthropic to retrain the model without this user's data, since the model has learned from it
C. Wait for the log retention window to expire, since that satisfies erasure for every store in time
D. Use a data map to find and delete the user's data in logs, vector index and memory, then record it

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Erasure applies to every place the application stored personal data, so the design needs a map of those stores and a way to delete from each, including derived data like embeddings and memory files. API traffic is not used to train the model by default, so retraining is not the issue. Deleting only the account leaves identifiable content behind, and waiting does not meet the response deadline.
</details>

---

### Question 27
**Scenario:** A CFO asks whether a Claude-based contract review tool is worth renewing. The team's dashboard shows cost per million tokens and total tokens used.

A. Report cost per completed review against the current cost of human review, with quality and error rates
B. Report total token usage for the year, since a high number shows that the tool was used heavily
C. Report the model's public benchmark scores, since a higher score shows the tool is good value
D. Report the per-token price trend, since falling prices show the tool is becoming cheaper each quarter

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Executives decide on business outcomes: what a unit of work costs, what it replaces, and whether quality holds. Token counts and per-token prices are inputs, not results, and heavy usage can mean waste as easily as value. Benchmarks describe the model in general, not this workflow's accuracy.
</details>

---

### Question 28
**Scenario:** A sales lead promises a client that the Claude-based claims assistant will "never make a mistake." The architect is asked to support that statement in the proposal.

A. Support it, since a well-tested prompt makes the model's behavior fixed and fully predictable
B. Replace it with the measured error rate, the review steps that catch errors, and how they escalate
C. Remove all mention of errors from the proposal, so the client is not alarmed during the sale
D. Support it but add a footnote saying that the model's outputs are the client's responsibility

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Model output is probabilistic, so honest expectation setting gives the measured error rate from evals and describes the controls that catch the remainder. An absolute promise sets up a breach of trust the first time an error ships. Silence and fine-print disclaimers hide the risk instead of managing it.
</details>

---

### Question 29
**Scenario:** A prompt includes three long policy documents (about 60,000 tokens in total) and one question. The question and instructions currently sit at the top, before the documents, and answers miss details.

A. Shorten each document to its first page, since the model reads only the start of long inputs
B. Repeat the question before each document, so that each one is read with the question in mind
C. Put the documents first in tags with metadata, and the question and instructions at the end
D. Move the documents into separate API calls and merge the three answers with a fourth call

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Anthropic's long-context guidance is to place long material at the top, wrapped in tags with source metadata, and to put the query at the end, which measurably improves answer quality. Truncating loses the detail that was missing. Splitting into separate calls removes the cross-document view, and repeating the question adds noise without fixing the order.
</details>

---

### Question 30
**Scenario:** A team adopting Claude Code wants every agent edit to be run through the code formatter, with no exceptions, across all developers' machines.

A. Write the rule in CLAUDE.md in capital letters so that the agent treats it as a strict requirement
B. Ask each developer to remind Claude to format files at the start of every session they open
C. Add a line to the README asking contributors to run the formatter before they open a pull request
D. Configure a hook in the shared project settings that runs the formatter after each file edit

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Hooks run deterministically on lifecycle events, so they are the tool for things that must always happen; checked-in project settings share them with the whole team. CLAUDE.md is guidance the model reads and usually follows, which is right for conventions but not for guarantees. Reminders and README notes depend on people remembering.
</details>

---

## Where to go deeper

- [Claude Certified Architect - Professional cert page](../anthropic/claude-certified-architect-professional/README.md) - notes, practice plan, strategy
- [Claude Architect Foundations practice questions](anthropic-claude-architect-foundations.md) - the level below
- [Agent and tool security](../../safety/security/agent-security.md) - question 7 in depth
- [Prompt injection defense](../../safety/security/prompt-injection-defense.md) - the attack and the controls
- **[📖 Claude agents and tools documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)** - primary source
