# Agents, the Copilot CLI and Customization

This note covers the parts of skill area 2, "Use GitHub Copilot features" (25-30%), that the 2026-08-07 outline added or expanded: agent mode, Copilot Edits, MCP, agent sessions and sub-agents, the Copilot CLI, Copilot code review, Spaces, Spark, pull request summaries, instructions files, prompt files, and the limits, feedback and commands of Copilot Chat. Inline suggestions and the basics of chat are in [note 02](02-code-completions-and-chat.md); organization policies, audit logs and the REST API are in [note 05](05-enterprise-administration.md).

**[📖 Customization cheat sheet](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)** - every customization file and where it works
**[📖 About Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)** - the terminal agent
**[📖 Copilot Spaces](https://docs.github.com/en/copilot/concepts/context/spaces)** - curated context

---

## From suggestions to agents

Copilot now works at three levels of autonomy, and the exam expects you to pick the right one for a task. **Inline suggestions** complete the line or block you are typing; you stay in full control and accept or reject each one. **Ask mode** in chat answers questions and proposes code you copy or apply yourself. **Agents** take a goal, plan the steps, read and edit files across the project, run commands and tests, observe the results and iterate until the task is done, asking for approval before risky actions. The agentic surfaces are agent mode in the IDE, the Copilot CLI in the terminal, and the Copilot coding agent, which works on GitHub in its own cloud environment and delivers a pull request.

## Agent mode and Copilot Edits

**Agent mode** in the IDE is the autonomous chat mode. You describe an outcome ("add input validation to the signup form and update the tests"), and Copilot works out which files are involved, makes the edits, runs the build or tests in the terminal, reads errors and fixes them. Because it executes commands, it asks for confirmation before running tools that change files or the system, and you review the changes before keeping them. Use it for multi-step tasks whose exact file list you do not know in advance.

**Copilot Edits** is the multi-file editing experience: you name the files in scope (the working set), describe the change, and Copilot proposes edits across those files as a reviewable diff that you accept or discard file by file. The distinction the exam draws is control. With Copilot Edits you decide the scope and review a proposed change set; with agent mode Copilot decides the scope and the steps itself. Pick Edits for a well-defined change to known files, and agent mode for open-ended tasks.

## MCP: giving Copilot tools

The Model Context Protocol (MCP) is the open standard for connecting AI assistants to external tools and data: issue trackers, databases, browsers, cloud APIs, internal services. An MCP server exposes tools; Copilot's agent calls them when a task needs them. In VS Code you configure servers in an `mcp.json` file (for a workspace, `.vscode/mcp.json`) or through the UI; the Copilot CLI has its own configuration and an `/mcp` command; the coding agent on GitHub is configured per repository. The GitHub MCP server, which lets the agent read issues, pull requests and repository data, is built in to several surfaces. Organizations can turn MCP use on or off through Copilot policy (see [note 05](05-enterprise-administration.md)). MCP is also what replaced GitHub App-based Copilot Extensions, which GitHub sunset in November 2025.

The reason MCP appears next to agent mode in the outline is that agents are only as capable as their tools. If a scenario asks how to let Copilot query the team's ticketing system or run browser checks while it works, the answer is an MCP server, not a longer prompt.

## Agent sessions and sub-agents

Long agent tasks consume context. Every file read, command output and intermediate idea stays in the conversation and competes for the model's limited context window, and quality drops when it fills with noise. The outline asks you to "manage Agent Sessions and delegate tasks to Sub-Agents for optimized context usage".

An **agent session** is one unit of agent work with its own history. Editors and GitHub list sessions so you can see what is running, check progress, switch between them, and hand work from one surface to another (for example, starting a task locally and delegating it to the coding agent in the cloud). Starting a fresh session for an unrelated task is itself a context-management technique.

A **sub-agent** is a helper the main agent starts for a self-contained piece of work, such as researching how a library is used across the codebase, comparing two approaches, or reviewing a change. The sub-agent works in its own isolated context and returns only its findings, so the main conversation receives a short answer instead of all the intermediate reading. In VS Code this happens through a `runSubagent` tool; you can ask for delegation in the prompt or let the main agent decide, and custom agents (described below) can serve as specialized sub-agents with their own instructions and tool limits. The exam point is the why: delegating keeps the main context small and focused, which keeps the main agent accurate on long tasks.

## The Copilot CLI

The Copilot CLI brings Copilot's agent into the terminal. It can answer questions, write and edit code, run commands, debug, generate scripts, manage files and work with GitHub.com, all from a shell session. It replaced the old `gh copilot suggest` and `gh copilot explain` extension, which stopped working on 2025-10-25, and it became generally available for Copilot subscribers in February 2026.

**Installing.** It needs an active Copilot subscription. Install it with npm (`npm install -g @github/copilot`, Node.js 22 or later), Homebrew (`brew install --cask copilot-cli`), WinGet (`winget install GitHub.Copilot`), or the install script; GitHub CLI users can also start it through `gh copilot`. On first run, authenticate with the `/login` slash command, or provide a fine-grained personal access token with the Copilot Requests permission in an environment variable for non-interactive use.

**Interactive and programmatic use.** Type `copilot` to start an interactive session, where you converse with the agent and steer it; Shift+Tab switches between the normal ask/execute mode and plan mode, in which Copilot proposes a plan before doing anything. For scripts and automation, pass a prompt with `-p` (or `--prompt`); Copilot completes the task and exits. Sessions keep their history, so you can resume earlier work.

**Approvals and safety.** Before using a tool that modifies or executes files, the CLI asks for approval, and you can approve once, approve for the session, or deny and redirect. Flags such as `--allow-tool` and `--deny-tool` pre-approve or block tools for unattended runs. Grant the minimum: an automation that only needs to read files should not be allowed to run arbitrary shell commands.

**Commands worth knowing.** Slash commands control the session: `/model` to choose a model, `/mcp` to manage MCP servers, `/context` to see what is using the context window, `/compact` to summarize the conversation and free context, `/login`, and `/feedback`. Expect questions that pair a need ("my session is running out of context") with the command (`/compact`).

**Typical uses.** Generating a script ("write a bash script that rotates these logs and test it"), bulk file operations ("rename these files to kebab-case and update the imports"), explaining an unfamiliar command or error, and working through a GitHub issue without leaving the terminal.

## The Copilot coding agent

The coding agent works on GitHub rather than on your machine. You assign it an issue (or start a task from the agents panel or chat), and it spins up its own development environment powered by GitHub Actions, makes the changes on a branch, runs tests, and opens a pull request for a human to review. It follows the repository's instructions files, can use MCP servers configured for the repository, and responds to review comments on its pull request. It is the right choice for well-scoped, low-to-medium complexity tasks you want done asynchronously: fixing a bug with a clear reproduction, adding tests, updating documentation. Its work is always reviewed through a pull request; it does not merge on its own.

## Copilot code review and pull request summaries

Copilot can review pull requests. A developer requests Copilot as a reviewer, or a repository or organization ruleset requests it automatically on every pull request. Copilot leaves review comments, often with suggested changes that can be applied in one click; it leaves a "Comment" review rather than an approval, so it never satisfies a required approval on its own. Review standards are customizable through instructions files: the repository's `.github/copilot-instructions.md` and path-specific `.instructions.md` files tell the reviewer what your team cares about (for example, "flag any SQL built by string concatenation"). Organizations control availability through Copilot code review policies (see [note 05](05-enterprise-administration.md)). You can also ask Copilot to review a selection or your uncommitted changes in the IDE before you open a pull request.

**Pull request summaries** are generated descriptions: in a pull request, Copilot drafts a summary of what changed and why from the diff, which the author then edits. They help reviewers start from an overview instead of reading every file cold.

## Spaces and Spark

**Copilot Spaces** organize the context Copilot uses to answer questions. A space can hold repositories, specific code files, pull requests, issues, free text such as transcripts or notes, images and uploaded files, plus instructions for how Copilot should respond. Ask questions inside the space and the answers are grounded in that curated material. Organization-owned spaces can be shared with members as admins, editors or viewers; personal spaces can be private, shared with specific people or public. Anyone with a Copilot licence, including Copilot Free, can create and use them. Spaces replaced Copilot knowledge bases, which were retired on 2025-11-01, so any question about "sharing a curated set of docs and code as context for a team" now points to a Space.

**GitHub Spark** turned a natural-language description into a small working web app, with hosting included. The outline still names it, but GitHub stopped accepting new Spark users and apps on 2026-08-04 and retired it for existing users on 2026-08-31 (deployed apps keep running), pointing builders to Copilot in VS Code, the Copilot CLI and the GitHub Copilot app instead. Know what it was for in case it appears, but do not plan around it.

## Instructions files, prompt files and other customization

Copilot reads several kinds of repository file. Knowing which one solves which problem is a reliable source of exam marks.

**Repository custom instructions** live in `.github/copilot-instructions.md`. They are standing guidance added to every request in that repository: coding standards, preferred libraries, how to build and test, what the reviewer should look for. Use them for "every answer should follow our conventions".

**Path-specific instructions** live in `.github/instructions/NAME.instructions.md`, with an `applyTo` glob in the front matter so they apply only to matching files (for example, `applyTo: "**/*.ts"` for TypeScript rules or a pattern for the `migrations/` folder). Use them when different parts of the codebase have different rules.

**Agent instruction files** such as `AGENTS.md` (and `CLAUDE.md` or `GEMINI.md`) are also read by Copilot's agents, so one file can guide several tools.

**Prompt files** live in `.github/prompts/NAME.prompt.md`. Each is a reusable, standalone prompt template, which can take input variables and reference files, that anyone in the repository can run by name in chat. Use them for "we keep typing the same long request": scaffold an endpoint in our style, write a release note, generate tests in our format. The outline phrases this as "prompt file reuse for consistent responses". The difference from instructions is that instructions apply automatically to everything, while a prompt file runs only when someone invokes it. Prompt files work in the IDEs (VS Code and Visual Studio), not on github.com.

**Custom agents** (`.github/agents/NAME.md`) define a specialist persona with its own instructions, tool restrictions and context, such as a "security reviewer" that can read but not edit. **Agent skills** (`.github/skills/NAME/SKILL.md`) package instructions, scripts and resources that Copilot loads only when relevant. **Hooks** (`.github/hooks/*.json`) run deterministic shell commands at points in the agent's work. These three are newer than the outline's wording, but they are how sub-agents and repeatable agent behaviour are configured in practice.

## Copilot Chat: limits, options, feedback and commands

The outline asks you to "understand the limits, options, feedback, and commands of GitHub Copilot Chat". The **limits** are those of any LLM plus Copilot's own: answers can be wrong or out of date, the context window is finite (long threads lose early detail), chat only knows what is in its context (open files, attachments, the repository index, a Space), and responses that match public code may be blocked by the filter. Usage of premium models also draws on the plan's monthly allowance.

The **options** are the modes (ask, edit, agent), model choice where the plan allows it, and the context you attach with `#` references (files, selections, the codebase) or chat participants with `@` (such as `@workspace` and `@terminal` in VS Code). The **commands** are slash commands such as `/explain`, `/fix`, `/tests`, `/doc`, `/new` and `/clear`, plus any prompt files the repository defines. **Feedback** is the thumbs up and thumbs down on each response (and in the CLI, `/feedback`), which is how users report poor or harmful answers; for a poor answer the practical fix is to refine the prompt, add context or start a new thread.

## Key Exam Facts

- Agent mode decides the scope and steps; Copilot Edits works on a working set you choose and shows a diff
- Sub-agents run in isolated context and return only results, keeping the main session's context small
- The Copilot CLI starts with `copilot`, installs with `npm install -g @github/copilot` (Node 22+), Homebrew, WinGet or a script, and runs non-interactively with `-p`
- The old `gh copilot suggest` and `gh copilot explain` extension stopped working on 2025-10-25
- The coding agent works in a GitHub Actions environment and delivers a pull request
- Copilot code review leaves comments, never an approval; customize it with instructions files
- Spaces replaced knowledge bases (2025-11-01); MCP replaced GitHub App-based Copilot Extensions (November 2025)
- Spark was retired on 2026-08-31 even though the outline still names it
- `.github/copilot-instructions.md` applies to everything; `.instructions.md` with `applyTo` applies to matching paths; `.prompt.md` runs only when invoked

## Study Checklist

- [ ] I can explain when to use inline suggestions, ask mode, Copilot Edits, agent mode, the CLI and the coding agent
- [ ] I have configured an MCP server and seen the agent call it
- [ ] I can explain why sub-agents help on long tasks
- [ ] I have installed the Copilot CLI and used it interactively and with `-p`
- [ ] I know where each customization file lives and what it does
- [ ] I have requested a Copilot code review on a pull request
- [ ] I have created a Copilot Space
