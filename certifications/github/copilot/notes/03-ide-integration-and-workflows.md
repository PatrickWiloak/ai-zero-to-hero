# IDE Integration and Workflows

## Supported Editors

Copilot ships official extensions or plugins for the following environments.

| Editor | Extension/Plugin | Notes |
|--------|------------------|-------|
| Visual Studio Code | GitHub Copilot and GitHub Copilot Chat | First-class; gets features earliest |
| Visual Studio 2022+ | GitHub Copilot | Installed via VS Installer |
| JetBrains IDEs | GitHub Copilot plugin | IntelliJ, PyCharm, GoLand, WebStorm, Rider, etc. |
| Neovim | copilot.vim and CopilotChat.nvim | Completions and chat |
| Xcode | GitHub Copilot for Xcode | Completions and chat |
| Eclipse | GitHub Copilot | Completions and chat |
| Azure Data Studio | GitHub Copilot | Completions for SQL |

**[Setup in your IDE](https://docs.github.com/en/copilot/configuring-github-copilot/installing-the-github-copilot-extension-in-your-environment)** - Installation guide

## Installation Flow

General steps (VS Code shown):

1. Install the **GitHub Copilot** extension
2. Install the **GitHub Copilot Chat** extension
3. Sign in to GitHub in the editor
4. Authorize the extension to access your GitHub account
5. Verify a seat is assigned (Free, Pro, Business, or Enterprise)

## VS Code Feature Map

- **Ghost text** for completions in any supported language
- **Chat view** in the primary side bar
- **Inline chat** at the cursor (Ctrl+I)
- **Terminal chat** in the integrated terminal (Ctrl+I)
- **Quick chat** - Ctrl+Shift+I
- **Agents** - `@workspace`, `@vscode`, `@terminal`, `@github`
- **Context variables** - `#file`, `#selection`, `#codebase`, `#web`
- **Commands** via Command Palette: "Copilot: ..."
- **Source Control** - generate commit message icon

## JetBrains Feature Map

- Completions while typing
- Chat tool window
- Inline chat via editor context menu
- Slash commands and agents similar to VS Code (subset may vary)

## Copilot in Visual Studio 2022+

- Completions and chat
- Chat pane integrated with the solution
- Context includes open documents and solution files

## Copilot in GitHub Mobile

- Conversational chat with access to GitHub.com data
- Ask about notifications, issues, PRs, and repo summaries
- Useful for reviewing on the go

## Copilot CLI

The current Copilot CLI is an agent in the terminal, started with `copilot`. It replaced the `gh copilot suggest` / `gh copilot explain` extension, which stopped working on 2025-10-25.

```bash
npm install -g @github/copilot      # Node.js 22 or later; or Homebrew, WinGet, the install script, or `gh copilot`
copilot                              # interactive session; use /login on first run
copilot -p "list files changed in the last 24 hours and summarize them"   # programmatic: run and exit
```

Inside a session, Shift+Tab toggles plan mode, and slash commands such as `/model`, `/mcp`, `/context` and `/compact` manage the session. Tools that modify or execute files need approval. Full detail is in [note 07](07-agents-cli-and-customization.md).

**[About Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)** - CLI docs

## Copilot on GitHub.com

### Global Chat

Click the Copilot button in the header to open chat. Ask general questions, or reference a specific repo.

### Repo Chat

On a repository page, chat is scoped to that repo and can reason about its structure, docs, and code.

### Issues and PRs

- Summarize a long issue thread
- Draft a PR description based on the diff (pull request summaries)
- Comment on PRs where Copilot is requested as a reviewer (Copilot code review)

## Retired: Copilot Extensions and Copilot Workspace

Older study material describes **Copilot Extensions** (chat agents such as `@sentry` installed from the Marketplace as GitHub Apps) and **Copilot Workspace** (a task-centric issue-to-PR environment). GitHub sunset GitHub App-based Copilot Extensions in November 2025 in favour of MCP servers, and Copilot Workspace ended as a technical preview in 2025; its issue-to-pull-request role is now filled by the Copilot coding agent. Neither appears in the 2026-08-07 skills outline. See [note 07](07-agents-cli-and-customization.md) for MCP and the coding agent.

## Typical Workflows

### Feature Development

1. Create an issue
2. Open the repo in your IDE; open key files in tabs for context
3. Write a function signature; let Copilot ghost text fill the body
4. Ask chat `/tests` to generate tests for the selection
5. Run tests; if red, run `/fix`
6. Use Copilot to draft a PR summary (Enterprise)
7. Request Copilot as a reviewer (Enterprise)

### Debugging

1. Select the failing function
2. `/explain` to understand it
3. `/fix` to propose a correction
4. Run tests; iterate

### Documentation

1. Select an API module
2. `/doc` to generate docstrings
3. Ask chat to generate a README section with examples

### DevOps

1. Ask chat to generate a GitHub Actions workflow for CI
2. Ask for a multi-stage Dockerfile
3. Ask for Terraform for a specific cloud resource
4. Explain complex shell pipelines with the Copilot CLI (`copilot`)

## MCP (Model Context Protocol) Support

Copilot Chat supports the Model Context Protocol, letting local MCP servers provide tools to chat. Admins can enable or disable MCP via policy in Business and Enterprise.

## Key Exam Facts

- Install order: Copilot extension, then Copilot Chat extension, then sign in
- The Copilot CLI starts with `copilot`; the old `gh-copilot` extension is retired
- Copilot on GitHub.com has global, repo, issue, and PR contexts
- MCP servers replaced GitHub App-based Copilot Extensions (November 2025)
- MCP is policy-controlled in Business and Enterprise

## Study Checklist

- [ ] I can install Copilot in VS Code end to end
- [ ] I can install the Copilot CLI and use it interactively and with `-p`
- [ ] I can describe the chat surfaces on github.com
- [ ] I know which older features (Extensions, Workspace, knowledge bases) are retired and what replaced them
- [ ] I can run a full feature workflow (issue to PR) using Copilot
