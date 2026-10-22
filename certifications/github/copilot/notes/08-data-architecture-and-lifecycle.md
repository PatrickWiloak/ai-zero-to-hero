# Data, Architecture and the Suggestion Lifecycle

This note covers skill area 4, "Understand GitHub Copilot data and architecture" (10-15%), and the limitations material that skill area 1, "Use GitHub Copilot responsibly" (15-20%), shares with it. The outline's objectives are: explain data usage, flow and sharing; describe input processing and prompt building; explain proxy filtering and post-processing; visualize the code suggestion lifecycle; and describe the limitations of LLMs and of Copilot. Retention by plan, the public code filter and content exclusion rules are in [note 04](04-security-privacy-and-data-handling.md).

**[📖 GitHub Trust Center](https://github.com/trust-center)** - how Copilot handles data
**[📖 How GitHub Copilot handles data (Microsoft Learn module)](https://learn.microsoft.com/en-us/training/paths/copilot/)** - part of the official learning path

---

## The big picture

Copilot is not a model running inside your editor. The editor extension (or the CLI, or github.com) is a client. It gathers context, builds a prompt and sends it over an encrypted connection to a GitHub-operated service, often called the Copilot proxy. The proxy authenticates the user, applies filters and policies, and forwards the prompt to a large language model hosted for GitHub (models from several providers are offered, and the plan and organization policy decide which ones a user may pick). The response comes back through the proxy, which applies its own checks, and then to the client, which may filter further before showing anything. Every exam question in this area is a question about one stage of that round trip.

## Input processing and prompt building

The model only knows what is in the prompt, so the client's first job is to assemble the most useful context within a limited token budget. For an inline suggestion, that context starts with the code before and after the cursor in the current file, which matters most. It adds the file's language and path, and snippets from other files that are likely related, especially files open in neighbouring editor tabs. This is why opening the relevant files improves suggestions and why a descriptive comment or function signature just above the cursor is such a strong signal.

For chat, the prompt also carries the conversation history (earlier questions and answers in the thread, trimmed as the thread grows), anything you explicitly attach with `#` references (a file, a selection, the codebase), results from tools or the repository index, the contents of a Copilot Space when you ask inside one, and the repository's custom instructions, which are added to every request automatically. Content excluded by an administrator is never gathered into the prompt in the first place.

The practical lessons the exam draws from this are simple. Copilot cannot use what it cannot see, so give it the right files and a clear statement of intent. Long, drifting chat threads carry stale context, so start a new thread when the topic changes. And the order of importance is roughly: the code at the cursor, what you explicitly attach, then everything gathered implicitly.

## Proxy filtering and post-processing

On the way in, the proxy does more than route. It checks that the user has an active seat and that the requested feature and model are allowed by policy. It screens prompts for problems such as toxic or hateful language, attempts to manipulate the system (prompt hacking or jailbreak attempts), and requests unrelated to software development, and it can refuse rather than forward them.

On the way back, post-processing checks the model's output before you see it. Responses are screened for harmful or offensive content. Code suggestions can be checked for common insecure patterns. If the organization (or the individual, on a personal plan) has set suggestions matching public code to "blocked", suggestions that match public code on GitHub, compared over a window of roughly 150 characters, are dropped; if set to "allowed", Copilot can instead show code references that identify the matching public repositories and their licences. Finally the client decides what to display, for example discarding a suggestion that is empty, duplicates existing code or would not fit at the cursor.

Keep the two privacy controls distinct, because exam distractors swap them. Content exclusions act on the **input**: excluded files are not used as context and do not receive inline suggestions. The public code filter acts on the **output**: it blocks or annotates suggestions that match public code.

## Data usage, flow and sharing

What happens to prompts and suggestions depends on the surface and the plan, and GitHub's Trust Center is the authoritative, current source. The principles to know are these. Data travels encrypted in transit. For organizations on Copilot Business and Enterprise, prompts and suggestions are not used to train models; GitHub's published terms state that IDE code completions and chat prompts are not retained after the response, while some surfaces outside the IDE keep prompts and suggestions for a short period (published as 28 days) to provide features such as conversation history. User engagement data, meaning events such as whether a suggestion was shown, accepted or dismissed, plus errors and latency, is kept longer to run and improve the service. Individual users on personal plans control in their settings whether GitHub may use their data for product improvement. Data is shared with the model providers that serve the request under agreements that prevent them from training on it or keeping it beyond processing. Agents add one more flow: work done by the coding agent or the CLI produces session logs, branches and pull requests, which live in the repository like any other work.

## The code suggestion lifecycle

The outline asks you to "visualize" the lifecycle, so be able to walk through it in order:

1. **Trigger.** You type, pause, write a comment, or invoke chat or an agent.
2. **Context gathering.** The client collects code around the cursor, related files, attachments, instructions and history, skipping anything excluded.
3. **Prompt building.** The client ranks and trims that context to fit the token budget and assembles the prompt.
4. **Inbound proxy.** Authentication, policy checks and prompt screening.
5. **Model inference.** The selected model generates one or more candidate completions or a chat response.
6. **Outbound post-processing.** Harmful-content screening, security checks and the public code filter.
7. **Client display.** The editor shows ghost text, a chat answer or a proposed diff.
8. **Developer decision.** You accept, partially accept, edit, cycle to another suggestion or dismiss it; agents ask for approval before risky actions.
9. **Telemetry.** Engagement data (accepted or dismissed, not the code itself on business plans) is recorded for service quality and for organization usage metrics.

Most troubleshooting questions map to a stage: no suggestions in one file usually means an exclusion (stage 2); a suggestion that appears and vanishes may have been filtered (stage 6); poor suggestions usually mean poor context (stages 2 and 3).

## Limitations of LLMs and of Copilot

Large language models predict likely text from patterns in their training data. They do not run your code, look anything up unless given a tool, or know when they are wrong. That produces the limitations the exam lists. **Hallucination**: plausible APIs, parameters or packages that do not exist. **Staleness**: training data has a cutoff, so new library versions and deprecations are missed. **Insecure or low-quality patterns** learned from public code. **Bias**, including in generated names, examples and comments. **Limited context**: the model sees only what fits in the prompt, so it can contradict code it was never shown. **Non-determinism**: the same request can produce different answers. **Uneven quality across languages**: strongest in widely used languages, weaker in niche languages and internal frameworks.

Copilot adds its own boundaries: it does not know your private code unless it is in the context or a Space; it cannot guarantee that a suggestion is free of licence obligations, even with the filter on; agents can take wrong actions quickly, which is why they ask for approval; and premium models draw on a monthly allowance. Every limitation leads to the same mitigation the responsible-use area teaches: the developer reviews, tests and scans everything before it ships, and owns the result.

## Key Exam Facts

- The client builds the prompt; the proxy authenticates, applies policy and filters both ways; the model generates; the client displays
- Code at the cursor is the strongest context; open tabs, attachments, instructions and chat history add to it
- Content exclusions act on input; the public code filter acts on output
- Business and Enterprise prompts and suggestions are not used for training; check the Trust Center for current retention
- Engagement data records acceptance and dismissal, not your code, on business plans
- Every LLM limitation is mitigated by human review, testing and scanning

## Study Checklist

- [ ] I can draw the request path from editor to model and back, naming what happens at the proxy
- [ ] I can list what goes into an inline prompt and a chat prompt
- [ ] I can walk through the nine stages of the suggestion lifecycle
- [ ] I can explain the difference between content exclusions and the public code filter
- [ ] I can name at least six LLM limitations and their mitigations
