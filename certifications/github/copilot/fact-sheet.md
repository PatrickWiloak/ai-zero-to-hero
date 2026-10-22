---
last-updated: 2026-10-22
---

# GitHub Copilot Certification Fact Sheet

## Exam Overview

**Exam Name:** GitHub Copilot (GH-300)
**Duration:** 100 minutes
**Questions:** Not published; multiple choice and multiple response, possibly interactive items
**Passing Score:** 700 (scale 1-1000)
**Cost:** Set by country (around USD 99 in the US)
**Delivery:** Pearson VUE, online or test centre
**Prerequisites:** None (Git and IDE familiarity recommended)
**Validity:** 2 years
**Skills outline:** as of 2026-08-07, seven skill areas (one listed without objectives)

**[GH-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300)** - Skills measured
**[Certification page](https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/)** - Registration and free practice assessment
**[GitHub Copilot Documentation](https://docs.github.com/en/copilot)** - Product docs
**[Copilot Trust Center](https://resources.github.com/copilot-trust-center/)** - Privacy and security

## Skills Measured at a Glance

| Skill area | Weight |
|---|---|
| Use GitHub Copilot responsibly | 15-20% |
| Use GitHub Copilot features | 25-30% |
| GitHub Copilot features (listed with no objectives; appears to duplicate the line above) | 25-30% |
| Understand GitHub Copilot data and architecture | 10-15% |
| Apply prompt engineering and context crafting | 10-15% |
| Improve developer productivity with GitHub Copilot | 10-15% |
| Configure privacy, content exclusions, and safeguards | 10-15% |

The sections below follow these areas. Older material (fundamentals, plans) is kept as background.

## Target Audience

- Software developers using AI-assisted coding tools
- Team leads evaluating Copilot for adoption
- DevOps and platform engineers integrating Copilot into workflows
- Administrators responsible for Copilot Business or Enterprise rollout
- Technical consultants advising clients on AI tooling

## Background: Copilot Fundamentals

### What Copilot Is

GitHub Copilot is an AI pair programmer that provides code completions, chat-based assistance, pull request support, and CLI help. It is built on large language models hosted by GitHub on Azure, routed through a GitHub-owned proxy service.

**Models in use:** models from several providers (OpenAI, Anthropic, Google and others) are offered; the list changes often, and plan and organization policy decide which a user can pick. Check the supported models page rather than memorizing names.

**[About Copilot](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)** - Product introduction
**[Copilot Features](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features)** - Feature map

### Copilot Product Family

| Product | Audience | Key Features |
|---------|----------|--------------|
| Copilot Free | Individual users, trial | Limited completions and chat per month |
| Copilot Pro (Individual) | Individual paid users | Unlimited completions, chat, model choice |
| Copilot Pro+ | Power users | Higher premium request limits, all models |
| Copilot Business | Organizations | Policy controls, content exclusions, audit logs, IP indemnity |
| Copilot Enterprise | Large orgs on Enterprise Cloud | Everything in Business plus a larger premium allowance and enterprise features |

As of 2026-10 GitHub also lists Copilot Student and Copilot Max, and premium model usage is metered against a monthly allowance. Plans change often; check the plans page.

**[Copilot Plans](https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)** - Plan comparison

### Supported Languages and IDEs

- Best quality on languages with large public training corpora: Python, JavaScript, TypeScript, Go, Ruby, Java, C#, C, C++, Rust, PHP
- First-class IDE support: VS Code, Visual Studio, JetBrains family, Neovim, Xcode, Eclipse, Azure Data Studio
- Surfaces: IDE inline, IDE chat and agent mode, GitHub.com chat, GitHub Mobile, the Copilot CLI (`copilot`), the coding agent, PR review

## Skill Area 1: Use GitHub Copilot Responsibly (15-20%)

### Limitations to Communicate

- Suggestions can be incorrect, outdated, insecure, or biased
- Training data has a cutoff; very new APIs may be missing or wrong
- Copilot does not know private code unless it is part of the current context (or a Copilot Space)
- Suggestions can match public code; the duplicate detection filter mitigates this

**[Responsible Use](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features)** - Official guidance

### Duplicate Detection Filter

- Blocks suggestions that match ~150 characters of public code on GitHub
- Configurable at org/enterprise (Business and Enterprise plans)
- Required to be enabled for IP indemnification to apply
- Available to Individual users as a personal setting

### Content Exclusions

- Path-based rules that prevent files from being used as context and suppress suggestions inside excluded files
- Scoped at repository, organization, or enterprise level
- Applied to inline completions and chat in ask mode; not supported in Edit and Agent modes of Copilot Chat
- Do not apply to symlinks, remote filesystems, or code already submitted to Copilot
- Changes can take up to 30 minutes to reach IDEs that already loaded settings; reload the window to apply sooner
- Available on Business and Enterprise

**[Content Exclusions](https://docs.github.com/en/copilot/how-tos/configure-content-exclusion/exclude-content-from-copilot)** - Exclusion setup

### Data Handling

- Prompts, suggestions, and telemetry behavior depends on plan and settings
- Business and Enterprise: prompts and suggestions are not retained or used to train models
- Individual: user can opt in or out of training on prompts
- Data is encrypted in transit; the proxy strips prompts after response in Business/Enterprise

## Background: Plans and Features

### Feature Matrix

| Feature | Free | Pro | Business | Enterprise |
|---------|------|-----|----------|------------|
| Code completions | Limited | Unlimited | Unlimited | Unlimited |
| Chat in IDE | Limited | Yes | Yes | Yes |
| Chat on GitHub.com | Limited | Yes | Yes | Yes |
| Model selection | No | Yes | Yes | Yes |
| Duplicate detection policy | User | User | Admin | Admin |
| Content exclusions | No | No | Yes | Yes |
| IP indemnification | No | No | Yes | Yes |
| Audit logs | No | No | Yes | Yes |
| PR summaries | No | No | No | Yes |
| Copilot Spaces | Yes | Yes | Yes | Yes |

**[Plans for Copilot](https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)** - Detailed comparison

### Billing and Seats

- Seats are assigned per user by org or enterprise admins
- Unassigning mid-cycle may or may not refund depending on billing cycle
- Seat utilization can be tracked via API and org insights
- Enterprise accounts can enable Copilot for specific orgs or all orgs

## Skill Area 2: Use GitHub Copilot Features (25-30%)

### Agentic Features (new in the 2026 outline)

| Feature | What it does |
|---|---|
| Agent mode (IDE) | Plans, edits files, runs commands and tests, iterates; asks before risky actions |
| Copilot Edits | Multi-file edits on a working set you choose, shown as a reviewable diff |
| MCP servers | Give agents tools and data (issue trackers, databases, browsers); replaced Copilot Extensions |
| Agent sessions | Units of agent work you can list, monitor, resume and hand off |
| Sub-agents | Helpers with isolated context that return only results, keeping the main context small |
| Coding agent | Works in a GitHub Actions environment from an assigned issue and opens a pull request |
| Copilot code review | Comments (never approves) on PRs; standards from instructions files; enabled by policy |
| Spaces | Curated context (repos, code, issues, notes, files); replaced knowledge bases 2025-11-01 |
| Spark | Natural-language micro apps; retired 2026-08-31 though still named in the outline |

### Customization Files

| File | Applies |
|---|---|
| `.github/copilot-instructions.md` | Every request in the repository |
| `.github/instructions/NAME.instructions.md` (`applyTo` glob) | Requests touching matching paths |
| `.github/prompts/NAME.prompt.md` | Only when someone runs that prompt (IDE) |
| `.github/agents/NAME.md` | A custom agent persona with its own tools and instructions |
| `AGENTS.md` | Agent instructions read by several tools |

### Inline Completions (Ghost Text)

| Action | Shortcut (VS Code) |
|--------|--------------------|
| Accept full suggestion | Tab |
| Accept next word | Ctrl+Right (Cmd+Right) |
| Next suggestion | Alt+] |
| Previous suggestion | Alt+[ |
| Dismiss | Esc |
| Open suggestions panel | Ctrl+Enter |

### Copilot Chat Surfaces

- **Inline chat** - Invoked at the cursor (Ctrl+I)
- **Chat view/panel** - Persistent side panel
- **Quick chat** - Floating input for quick questions
- **Chat on GitHub.com** - Repo-aware chat on github.com
- **Chat in Mobile** - Conversational on iOS and Android

### Slash Commands (Chat)

| Command | Purpose |
|---------|---------|
| `/explain` | Explain selected code or concept |
| `/fix` | Propose a fix for a problem |
| `/tests` | Generate tests for selection |
| `/doc` | Generate documentation comments |
| `/new` | Scaffold a new project or workspace |
| `/clear` | Clear chat context |
| `/help` | List chat commands |

**[Chat Cheat Sheet](https://docs.github.com/en/copilot/reference/chat-cheat-sheet)** - Chat reference

### Agents and Context Variables

| Agent / Variable | Purpose |
|------------------|---------|
| `@workspace` | Whole repo context (VS Code) |
| `@vscode` | Questions about VS Code itself |
| `@terminal` | Shell/terminal help |
| `@github` | GitHub-hosted data (issues, PRs, repo) |
| `#file` | Attach a file as context |
| `#selection` | Use current selection |
| `#codebase` | Broad codebase search |
| `#terminalLastCommand` | Reference last terminal command |

### Copilot in the CLI

- Install: `npm install -g @github/copilot` (Node 22+), `brew install --cask copilot-cli`, `winget install GitHub.Copilot`, or the install script
- Start: `copilot` (interactive; `/login` on first run); `copilot -p "..."` runs one task and exits
- Shift+Tab toggles plan mode; `/model`, `/mcp`, `/context`, `/compact`, `/feedback`
- Tool approvals: once, for the session, or deny; `--allow-tool` / `--deny-tool` for automation
- The old `gh copilot suggest` / `explain` extension stopped working on 2025-10-25

### Organization Policies and the REST API

- Policies control feature availability across IDEs and github.com, Copilot code review, MCP, models and previews
- Audit log events record seat assignment and policy changes
- Seats: `GET /orgs/{org}/copilot/billing/seats`; add with `POST .../selected_users` or `.../selected_teams`; remove with `DELETE` (pending cancellation until cycle end)

### Pull Requests

- **PR summaries** - Auto-generated PR descriptions
- **Code review** - Copilot can be requested as a reviewer, or requested automatically by a ruleset
- **Commit message generation** - From IDE source control

## Skill Area 4: Understand GitHub Copilot Data and Architecture (10-15%)

- Client gathers context (code at cursor, neighbouring tabs, attachments, instructions, chat history), skipping excluded files
- Proxy: authenticates, enforces policy, screens prompts (toxicity, prompt hacking, off-topic), routes to the model
- Post-processing: harmful-content screening, security checks, public code filter (about 150 characters)
- Lifecycle: trigger, gather, build prompt, proxy in, inference, proxy out, display, accept or dismiss, telemetry
- Limitations: hallucination, staleness, insecure patterns, bias, limited context, non-determinism, uneven language quality

## Skill Area 5: Apply Prompt Engineering and Context Crafting (10-15%)

### The 4 S's

1. **Single** - One intent per prompt
2. **Specific** - Clear names, types, signatures, inputs, outputs
3. **Short** - Concise prompts; refine iteratively
4. **Surround** - Use neighboring code, open tabs, and comments as context

### Prompt Patterns

- **Zero-shot** - Ask once with clear intent
- **One-shot** - Include one example of the desired output
- **Few-shot** - Provide several examples
- **Chain prompting** - Build up context with follow-ups in chat

### Practical Techniques

- Write a descriptive function signature and docstring before asking for the body
- Keep related files open in tabs so Copilot can draw context
- Use types, schemas, and imports to anchor the prompt
- For refactors, explain the current behavior and the desired behavior

**[Prompt Engineering for Copilot](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)** - Official guide

## Skill Area 6: Improve Developer Productivity (10-15%)

### Core Use Cases

- New code generation from comments and signatures
- Test generation (unit, integration, property)
- Refactoring and rename suggestions
- Documentation (README, inline, API)
- Learning unfamiliar frameworks (ask Copilot to explain)
- Code review assistance and PR summaries
- DevOps: Dockerfile, GitHub Actions YAML, Terraform, Bash

### Testing and Security

- `/tests` for unit tests; describe setup for integration tests
- Ask for missing edge cases: empty, null, boundaries, large input, invalid format, error paths
- Take expected values from requirements, not from current behaviour
- Ask for security fixes (injection, validation, secrets) and performance improvements; verify with scanners and benchmarks

## Skill Area 7: Configure Privacy, Content Exclusions, and Safeguards (10-15%)

- Configure content exclusions (repo, org, enterprise) and editor settings
- Users own and are responsible for accepted suggestions
- Enable the public code filter (block) or code referencing (allow with references)
- Troubleshoot: seat, editor settings, policy, network; exclusions take up to 30 minutes, reload to apply

### Regulated and Sensitive Scenarios

- Use content exclusions for secrets, license-sensitive code, regulated data
- Enable duplicate detection to reduce public code matches
- Turn off Copilot in repos where prohibited by policy via org settings

## Exam Tips

### High-Priority Topics (by weight)
1. Use Copilot features (25-30%) - agent mode, Edits, MCP, sub-agents, CLI, code review, Spaces, customization files, policies, REST API
2. Use Copilot responsibly (15-20%) - limitations, validation, human accountability
3. Data and architecture (10-15%) - prompt building, proxy filtering, lifecycle
4. Prompt engineering and context crafting (10-15%) - context, zero and few-shot, chat history
5. Developer productivity (10-15%) - generation, refactoring, tests, edge cases, security
6. Privacy, exclusions and safeguards (10-15%) - exclusions, public code filter, troubleshooting

### Key Differentiators to Remember
- Content exclusions act on input; the public code filter acts on output
- Copilot Edits uses your working set; agent mode chooses its own steps
- Instructions files apply automatically; prompt files run when invoked
- Spaces replaced knowledge bases; MCP replaced Copilot Extensions; the Copilot CLI replaced `gh copilot suggest` and `explain`
- Copilot code review comments but never approves
- Business and Enterprise prompts are not used for training
