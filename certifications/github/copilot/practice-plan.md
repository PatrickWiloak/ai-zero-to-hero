# GitHub Copilot Study Plan

## 5-Week Study Schedule

### Week 1: Foundations, Plans, and Setup

#### Day 1-2: What Copilot Is
- [ ] Read the Copilot product overview and feature map
- [ ] List the Copilot SKUs: Free, Pro, Pro+, Business, Enterprise
- [ ] Identify which LLMs Copilot uses and when model selection is available
- [ ] Review Notes: `notes/01-copilot-fundamentals.md`
- [ ] Read: [What is Copilot](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)

#### Day 3-4: Plan and Feature Matrix
- [ ] Build a feature matrix comparing Free, Pro, Business, Enterprise
- [ ] Read the [GH-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300) end to end and note the seven skill areas
- [ ] Note which older features are retired (knowledge bases, Extensions, Workspace, `gh copilot suggest` / `explain`, Spark)
- [ ] Note which controls are user-level vs admin-level
- [ ] Read: [Plans for Copilot](https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)

#### Day 5-6: Install and Trial
- [ ] Start a Copilot Free or Individual trial
- [ ] Install Copilot in VS Code and at least one JetBrains IDE
- [ ] Install the Copilot CLI: `npm install -g @github/copilot` (or Homebrew / WinGet), run `copilot`, sign in with `/login`
- [ ] Accept and decline suggestions; try all keyboard shortcuts
- [ ] Review Notes: `notes/01-copilot-fundamentals.md`

#### Day 7: Week 1 Review
- [ ] Quiz yourself on plan differences
- [ ] Re-read the feature matrix
- [ ] Build a one-page summary of which features need which plan

### Week 2: Using Copilot in the IDE and Chat

#### Day 8-9: Inline Completions
- [ ] Practice Tab-to-accept, Alt+] / Alt+[ to cycle
- [ ] Use the suggestions panel (Ctrl+Enter in VS Code)
- [ ] Write a descriptive function signature and observe suggestions
- [ ] Review Notes: `notes/02-code-completions-and-chat.md`

#### Day 10-11: Copilot Chat
- [ ] Try inline chat (Ctrl+I), chat panel, and quick chat
- [ ] Use every slash command: `/explain`, `/fix`, `/tests`, `/doc`, `/new`, `/clear`
- [ ] Use agents: `@workspace`, `@vscode`, `@terminal`, `@github`
- [ ] Attach files and selections with `#file`, `#selection`, `#codebase`
- [ ] Read: [Chat Cheat Sheet](https://docs.github.com/en/copilot/reference/chat-cheat-sheet)

#### Day 12-13: Other Surfaces
- [ ] Try Copilot Chat on github.com (repo-level and general)
- [ ] Use the Copilot CLI interactively, then run one task with `copilot -p "..."`
- [ ] Try agent mode and Copilot Edits on the same small change and compare
- [ ] Configure one MCP server; read [notes 07](notes/07-agents-cli-and-customization.md)
- [ ] Explore Copilot in GitHub Mobile
- [ ] Generate a commit message with IDE source control
- [ ] Review Notes: `notes/03-ide-integration-and-workflows.md`

#### Day 14: Week 2 Review
- [ ] Recreate the slash command and agent table from memory
- [ ] Pair each keyboard shortcut with the correct action
- [ ] Identify which surfaces require Business or Enterprise

### Week 3: Prompt Engineering and Developer Use Cases

#### Day 15-16: Prompt Fundamentals
- [ ] Memorize the 4 S's: Single, Specific, Short, Surround
- [ ] Practice zero-shot, one-shot, and few-shot prompts in chat
- [ ] Write before/after refactor prompts and compare outputs
- [ ] Review Notes: `notes/06-prompt-engineering-for-copilot.md`
- [ ] Read: [Prompt Engineering](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)

#### Day 17-18: Code Use Cases
- [ ] Generate unit tests for an existing module using `/tests`
- [ ] Refactor a long function in two steps: explain, then refactor
- [ ] Add docstrings and README sections using `/doc`
- [ ] Ask Copilot to learn a new framework by generating examples

#### Day 19-20: DevOps and Platform Use Cases
- [ ] Generate a GitHub Actions workflow for CI with Copilot Chat
- [ ] Generate a multi-stage Dockerfile
- [ ] Generate Terraform for a simple AWS resource
- [ ] Explain a complex shell pipeline with the Copilot CLI

#### Day 21: Week 3 Review
- [ ] Review your strongest and weakest prompt patterns
- [ ] Practice chat follow-ups and iterative refinement
- [ ] Review Notes: `notes/06-prompt-engineering-for-copilot.md`

### Week 4: Responsible Use and Enterprise Administration

#### Day 22-23: Responsible Use
- [ ] Read the Copilot Trust Center materials
- [ ] Understand duplicate detection filter behavior
- [ ] Understand content exclusions and their scopes
- [ ] Review IP indemnity requirements (Business/Enterprise + duplicate detection)
- [ ] Review Notes: `notes/04-security-privacy-and-data-handling.md`
- [ ] Read: [Responsible Use](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features)

#### Day 24-25: Policies and Content Exclusions
- [ ] In a sandbox org, configure content exclusions at repo level
- [ ] Configure duplicate detection policy at org level
- [ ] Disable or enable chat, network, or MCP policies
- [ ] Review audit log events for Copilot

#### Day 26-27: Enterprise Features
- [ ] Create a Copilot Space from a repository and some notes
- [ ] Study PR summaries and Copilot code review
- [ ] Add `.github/copilot-instructions.md`, a path-specific `.instructions.md` and a `.prompt.md` to a test repository
- [ ] Request a Copilot code review on a pull request
- [ ] Read the Copilot seat management REST endpoints in [notes 05](notes/05-enterprise-administration.md)
- [ ] Read [notes 08](notes/08-data-architecture-and-lifecycle.md) and [notes 09](notes/09-productivity-testing-and-safeguards.md)
- [ ] Review Notes: `notes/05-enterprise-administration.md`

#### Day 28: Week 4 Review
- [ ] Walk through the full seat assignment workflow
- [ ] Enumerate every admin policy that affects Copilot behavior
- [ ] Summarize what each plan retains and does not retain

### Week 5: Review and Mock Exams

#### Day 29-30: Comprehensive Review
- [ ] Re-read fact-sheet.md top to bottom
- [ ] Review all six notes files
- [ ] Create flashcards for plan differences and slash commands

#### Day 31-32: Scenarios
- [ ] Work through scenarios.md end-to-end
- [ ] For every wrong answer, re-read the relevant doc section

#### Day 33-34: Mock Exams
- [ ] Take any available practice exam
- [ ] Time yourself to 100 minutes
- [ ] Take Microsoft's free practice assessment
- [ ] Log weak areas and revisit specific notes

#### Day 35: Exam Day
- [ ] Light fact-sheet review in the morning
- [ ] Confirm ID, webcam, quiet room
- [ ] Close unnecessary apps; confirm stable network
- [ ] Take the exam with confidence

## Study Tips

### Time Allocation by Skill Area Weight

| Skill area (2026-08-07) | Weight | Suggested Hours |
|--------|--------|----------------|
| Use GitHub Copilot features | 25-30% | 12-14 hours |
| Use GitHub Copilot responsibly | 15-20% | 6-8 hours |
| Data and architecture | 10-15% | 4-6 hours |
| Prompt engineering and context crafting | 10-15% | 4-6 hours |
| Developer productivity | 10-15% | 4-6 hours |
| Privacy, content exclusions and safeguards | 10-15% | 4-6 hours |

The outline also lists "GitHub Copilot features (25-30%)" with no objectives; it appears to duplicate the first row.

### Recommended Daily Schedule
- **20 min** reading Copilot docs or notes
- **40 min** hands-on practice in IDE, chat, and CLI
- **15 min** flashcards for plans, commands, and policies
- **Total: ~1.25 hours/day**

### Hands-On Labs
1. Build a REST API (Python or Node) using only Copilot Chat and inline
2. Generate a full test suite for an existing small repo
3. Configure content exclusions on a sandbox org and verify behavior
4. Create a GitHub Actions workflow by prompting Copilot
5. Use the Copilot CLI to build 10 shell one-liners from natural language
