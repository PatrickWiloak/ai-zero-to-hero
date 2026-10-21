# AI for Engineers

**In one line:** Use AI across the whole engineering job - not just autocomplete, but understanding unfamiliar code, writing tests, debugging, design docs, reviews and on-call - while keeping your review bar, your tests and your secrets hygiene exactly where they were.
**Last reviewed:** 2026-10-21

---

## The short version

- AI help for engineers now spans three modes: **inline completion**, **chat** about code and design, and **agents** that edit files, run commands and iterate on tests. Each needs a different level of supervision.
- The evidence on speed is mixed and task-dependent. A 2023 controlled study found developers using Copilot finished a small greenfield task 55.8% faster; a 2025 randomised trial found experienced developers working in their own large repositories were 19% slower with AI tools, while believing they were faster.
- Developers use it widely but trust it cautiously: in Stack Overflow's 2025 survey, 84% used or planned to use AI tools, and more distrusted the accuracy of the output (46%) than trusted it (33%).
- The habits that make it pay: give it context, keep tasks small and verifiable, let tests be the judge, and review AI code as carefully as a new colleague's.
- Never paste secrets, and treat AI agents with tool access as a new security boundary.

## Where it helps most

| Work | Good fit | Watch out |
|---|---|---|
| Understanding code | "Explain this module", "trace where this value comes from" | It may describe what the code *should* do |
| Boilerplate | CRUD handlers, config, migrations, serializers | Outdated library APIs |
| Tests | Generating cases, edge cases, fixtures | Tests that assert current (buggy) behaviour |
| Debugging | Reading stack traces, suggesting hypotheses | Confident wrong root causes |
| Refactors | Mechanical, well-tested changes across files | Subtle behaviour changes |
| Learning | New language, framework or API | Hallucinated functions and flags |
| Docs | Design docs, READMEs, ADRs, PR descriptions | Docs that drift from code |
| Ops | Log analysis, runbook drafting, query writing | Running suggested commands blindly |

It helps least on deeply novel design, performance-critical code you cannot measure, and large codebases where the relevant context does not fit or is not provided. That last point is a plausible part of why the METR result differed from the greenfield studies.

## Copyable prompts

**Understand before changing**
```
I need to change how [feature] handles [case]. Here are the relevant files:
[paste or reference]. Before suggesting any change: explain the current flow
step by step, list every place that would need to change, and list what
could break. Do not write code yet.
```

**Tests first**
```
Here is a function and its current tests: [paste]. Write additional tests
for edge cases that are not covered: empty input, boundaries, invalid types,
concurrency if relevant. Use [framework]. For each test, one line on what it
protects against. Do not modify the function.
```

**Debugging**
```
Error and stack trace: [paste]. Relevant code: [paste]. What I've tried:
[list]. Give me the 3 most likely causes ranked, and for each the fastest
experiment to confirm or rule it out. Do not propose a fix until we know
the cause.
```

**Design doc critique**
```
Here is my design doc: [paste]. Review it as a senior engineer focused on
[reliability / security / cost]. List concrete risks, missing failure modes,
unstated assumptions, and questions a reviewer will ask. No praise.
```

**PR self-review**
```
Here is my diff: [paste]. Review it for bugs, missing error handling,
security issues (injection, authz, secrets), and missing tests. Reference
line numbers. Separate "must fix" from "nit".
```

## Working with coding agents

Agentic tools can now take a task, read the codebase, edit many files, run tests and iterate. They are powerful and need structure:

- **Small, well-specified tasks.** "Add pagination to the /orders endpoint following the pattern in /customers, with tests" beats "improve the orders API".
- **Tests as the contract.** Agents iterate toward passing checks. Make sure the checks mean something, and watch for agents that weaken or delete tests to pass.
- **Project instructions.** Most tools read a project file of conventions (build commands, style, do-not-touch areas). Write one.
- **Review the diff like a stranger's PR.** Read it all. Run it.
- **Least privilege.** Do not give an agent production credentials, broad cloud permissions, or unattended shell access on a machine with secrets. Text in a file, issue or web page the agent reads can contain instructions (prompt injection). See [agent security](../../safety/security/agent-security.md).

More on team practice, review policy and measurement: [coding assistants in practice](../use-cases/coding-assistants-in-practice.md). Tool comparison: [coding assistants compared](../../tools/comparisons/coding-assistants.md).

## Before and after

**Before.** An engineer joins a team and is asked to add a retry policy to a payments client in an unfamiliar service. They spend most of a day reading code to find where requests are built, how errors are classified, and how tests mock the network.

**After.** They ask the assistant to explain the request flow and error handling with file references, then verify the explanation by reading the three files it names. They ask for tests describing the desired retry behaviour first, review them, then have the assistant implement until the tests pass. They review the diff, notice the retry also applies to a non-idempotent POST, and fix that by hand. The change takes a couple of hours, and the bug they caught is exactly the kind an unreviewed agent change would have shipped.

## Security and data

- **Secrets.** Never paste API keys, tokens, private keys or `.env` contents. Many tools can be configured to ignore files; use that.
- **Code confidentiality.** Use your company's approved tool on a business plan with training on your code turned off. See [choosing enterprise AI tools](../enablement/choosing-enterprise-ai-tools.md).
- **Suggested dependencies.** Models sometimes suggest packages that do not exist. A 2024 study of 16 code-generating models found hallucinated package names in at least 5.2% of samples from commercial models and 21.7% from open models, which attackers can exploit by registering those names. Verify every new dependency.
- **Generated code is your code.** Same review, same static analysis, same licence scrutiny.
- **LLM features you build** have their own risks: [OWASP LLM Top 10](../../safety/security/owasp-llm-top-10.md).

## What to measure on a team

Delivery and quality, not volume. In the 2024 DORA survey data, a 25% increase in AI adoption was associated with modest estimated gains in documentation quality (7.5%), code quality (3.4%) and code review speed (3.1%), but also an estimated 1.5% decrease in delivery throughput and 7.2% decrease in delivery stability. DORA's reading was that AI makes larger changes easier, and larger batches are riskier. Watch lead time, change failure rate, review time, and escaped defects before and after rollout. "Lines of code accepted" rewards the wrong thing.

## Common mistakes

- Asking for a large change in one go, then struggling to review it.
- Not giving context (the relevant files, versions, conventions) and blaming the model.
- Trusting explanations of code without reading the code.
- Letting AI write the tests and the implementation, then approving both without thinking about what should be tested.
- Skipping fundamentals early in a career. You need to be able to spot wrong code.

## Next steps

- Team-level practice: [coding assistants in practice](../use-cases/coding-assistants-in-practice.md)
- Build with LLMs instead of just using them: [first LLM API call](../../learn/day-one/first-llm-api-call.md), [LLM app architecture](../../build/patterns/llm-app-architecture.md)
- How coding ability is measured: [SWE-bench](../../papers/techniques/84-swe-bench/summary.md), [math and code benchmarks](../../explainers/benchmarks/math-and-code.md)
- How long tasks agents can do: [METR time horizons](../../papers/techniques/145-metr-time-horizons/summary.md)
- Agent design: [Building Effective Agents](../../papers/essays/115-building-effective-agents/summary.md)

## Sources

- Peng, Kalliamvakou, Cihon and Demirer, *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot* (2023): <https://arxiv.org/abs/2302.06590>
- METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* (2025): <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>
- Stack Overflow, *2025 Developer Survey: AI*: <https://survey.stackoverflow.co/2025/ai>
- Google Cloud DORA, *Accelerate State of DevOps Report 2024*: <https://dora.dev/research/2024/dora-report/>; report infographic: <https://dora.dev/research/2024/2024-DORA-Report-Infographic.pdf>; summary of the AI findings in InfoQ: <https://www.infoq.com/news/2024/11/2024-dora-report/>
- Spracklen et al., *We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs*, USENIX Security 2025: <https://arxiv.org/abs/2406.10279>
