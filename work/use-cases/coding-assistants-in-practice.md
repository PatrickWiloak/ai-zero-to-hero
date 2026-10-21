# Coding Assistants in Practice

**In one line:** Roll out coding assistants and agents to an engineering team with clear rules for context, review, testing, secrets and agent permissions, and judge them on delivery and quality metrics rather than on how much code they generate.
**Last reviewed:** 2026-10-21

---

## The short version

- Coding assistants work in three modes: **completion** (suggestions as you type), **chat** (questions and edits in the editor), and **agents** (the tool plans, edits multiple files, runs commands and tests, and iterates). Teams now use all three.
- Results vary widely by task and context. Developers in a 2023 controlled study finished a small, self-contained task 55.8% faster with Copilot; experienced developers in a 2025 randomised trial on their own mature repositories were 19% slower with AI tools while believing they were faster.
- In the 2024 DORA survey data, a 25% increase in AI adoption was associated with small estimated improvements in documentation quality, code quality and review speed, but an estimated 7.2% decrease in delivery stability. AI makes bigger changes easy; bigger changes are riskier.
- Make it work with: **small tasks**, **tests as the contract**, **project instruction files**, **human review of every diff**, and **least-privilege agents**.
- Measure lead time, change failure rate, review time and escaped defects, not lines generated or suggestions accepted.

## Rolling it out to a team

Use the general [AI adoption playbook](../enablement/ai-adoption-playbook.md), with these engineering specifics.

**Week 1-2: decide the rules.** Write a one-page team standard covering:

```markdown
## AI-assisted development standard - [team]

Tools: [approved assistant(s)] on the company plan only. Personal accounts
are not allowed for company code.

Secrets: never paste secrets. [Tool] is configured to ignore .env, *.pem,
secrets/, and [paths]. If a secret is exposed to any AI tool, rotate it and
report to [security].

Review: every AI-assisted change is reviewed by a human who did not generate
it, to the same standard as any change. The author must be able to explain
every line.

Size: prefer PRs under [400] changed lines. Split agent output that is larger.

Tests: new behaviour needs tests. Changes that weaken, skip or delete tests
need an explicit reviewer sign-off.

Dependencies: new packages are verified (exists, maintained, expected
publisher, licence) before adding. AI-suggested package names are not trusted.

Agents: run in [sandbox / dev container / CI]; no production credentials;
no network access beyond [package registries, docs] unless approved.
Destructive commands (rm -rf, force push, migrations, infra apply) need
human confirmation.

Disclosure: note "AI-assisted" in the PR description when an agent wrote
most of the change. [optional]
```

**Week 2: project instructions.** Most assistants and agents read a project-level instruction file (conventions, build and test commands, architecture notes, do-not-touch areas). Write one per repository. It is the cheapest quality improvement available, because it gives the model the context a new colleague would need.

**Weeks 3-8: pilot with volunteers** on real tickets, with weekly 30-minute retros: what worked, what wasted time, what got through review that should not have.

**Weeks 9-10: measure and decide** (see below).

## How to use each mode well

**Completion.** Best for boilerplate, repetitive patterns and well-known APIs. Read every suggestion before accepting; the risk is accepting plausible code on autopilot.

**Chat.** Best for understanding code, debugging, writing tests and small focused edits. Paste or reference the relevant files; specify language, framework and versions.

**Agents.** Best for well-specified multi-file tasks with good test coverage: "Add rate limiting to the public API using the existing middleware pattern in auth/, with tests for the 429 path." Poor for vague goals and code without tests. A workable loop:

```
1. Write or point to the spec (issue, acceptance criteria)
2. Ask the agent for a plan first; correct the plan
3. Let it implement and run tests in a sandbox
4. Review the full diff yourself; run it locally
5. Ask the agent to address review comments, or fix by hand
6. Normal PR review by a teammate
```

For tool choices, see [coding assistants compared](../../tools/comparisons/coding-assistants.md).

## Security: agents are a new boundary

An agent that can read files, run shell commands and make network requests acts with your permissions. Risks to plan for:

- **Prompt injection.** Text inside a repository, issue, dependency README or web page can contain instructions that the agent may follow ("also send the contents of ~/.aws/credentials to..."). Sandboxing and least privilege limit the damage. See [prompt injection explained](../../safety/security/prompt-injection-explained.md) and [agent security](../../safety/security/agent-security.md).
- **Package hallucination.** A 2024 study of 16 code-generating models found hallucinated package names in at least 5.2% of samples from commercial models and 21.7% from open models. Attackers can register those names. Verify dependencies.
- **Secrets in context.** Configure ignore files; keep credentials out of the working tree; use short-lived credentials in dev.
- **Supply chain of the tool itself.** Extensions, plugins and tool servers (for example MCP servers) run with real permissions. Approve them like any dependency. See [model supply chain](../../safety/security/model-supply-chain.md).

## Measuring impact

| Metric | Source | What to look for |
|---|---|---|
| Lead time for changes | Version control and deploy data | Should fall or hold |
| Change failure rate | Incident and rollback records | Must not rise |
| PR size | Version control | Watch for creep; DORA links larger batches to instability |
| Review time per PR | Code review tool | Rising review time can eat the gains |
| Escaped defects | Bug tracker | Must not rise |
| Developer experience | Short quarterly survey | Satisfaction, frustration, "where it wastes my time" |

Avoid: lines of code generated, suggestion acceptance rate, and self-reported time saved as primary measures. The METR trial is the clearest warning: developers estimated a 20% speed-up while the measured effect was a 19% slowdown. Where you can, compare similar work with and without the tool, or before and after, using system data.

## Before and after

**Before.** A team of eight gets AI assistants with no guidance. Within two months PRs double in size, reviews take longer, two incidents trace back to AI-written code that nobody fully read, and a contractor pastes a production database URL with credentials into a personal chatbot.

**After (the re-launch).** The team adopts the one-page standard, adds project instruction files, configures ignore rules, moves agent work into dev containers without production access, and sets a PR size guideline. Reviewers reject diffs the author cannot explain. Over the next quarter PR size returns to normal, review time drops, and engineers report the biggest value in test writing, understanding unfamiliar services, and migrations. The credential was rotated the day it was reported.

(Illustrative; the pattern is common, the numbers will be yours.)

## Where assistants help least

- Novel architecture and design trade-offs.
- Performance and concurrency problems without a way to measure.
- Large, legacy codebases with little test coverage and undocumented behaviour.
- Areas where the engineer cannot judge correctness. If you cannot review it, you should not merge it.

## Juniors and learning

Assistants can speed up newcomers a great deal, and can also let them ship code they do not understand. Pair AI use with explanation: ask juniors to walk through AI-written code in review, and keep some tasks deliberately hands-on. The skill to judge code is what makes the tool safe to use.

## Common mistakes

- No team standard, so everyone invents their own rules.
- Agents with production credentials.
- Measuring acceptance rate and celebrating it.
- Huge AI-generated PRs that reviewers rubber-stamp.
- Letting the agent "fix" failing tests by changing the tests.

## Next steps

- Individual practice: [AI for engineers](../playbooks/for-engineers.md)
- Tools: [coding assistants compared](../../tools/comparisons/coding-assistants.md)
- How coding agents are evaluated: [SWE-bench](../../papers/techniques/84-swe-bench/summary.md), [METR time horizons](../../papers/techniques/145-metr-time-horizons/summary.md), [math and code benchmarks](../../explainers/benchmarks/math-and-code.md)
- Agents in general: [agents explained](../../learn/concepts/agents-explained.md), [MCP explained](../../learn/concepts/mcp-explained.md), [Building Effective Agents](../../papers/essays/115-building-effective-agents/summary.md)
- Origins: [Codex](../../papers/language-models/56-codex/summary.md)

## Sources

- Peng, Kalliamvakou, Cihon and Demirer, *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot* (2023): <https://arxiv.org/abs/2302.06590>
- METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* (2025): <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>
- Google Cloud DORA, *Accelerate State of DevOps Report 2024*: <https://dora.dev/research/2024/dora-report/>; infographic: <https://dora.dev/research/2024/2024-DORA-Report-Infographic.pdf>
- Spracklen et al., *We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs*, USENIX Security 2025: <https://arxiv.org/abs/2406.10279>
