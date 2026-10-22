# GitHub Copilot Study Strategy

## Know what is being tested

The GH-300 skills outline as of 2026-08-07 has seven skill areas and a 100-minute exam. "Use GitHub Copilot features" (25-30%) is the biggest area by far, and it is where the outline changed most: agent mode, Copilot Edits, MCP, sub-agents, the Copilot CLI, code review, Spaces, instructions and prompt files, organization policies and the REST API. Responsible use (15-20%) is next. The remaining areas (data and architecture, prompt engineering, productivity, privacy and safeguards) are 10-15% each. A seventh line, "GitHub Copilot features (25-30%)", is listed with no objectives and appears to duplicate the features area, so do not hunt for separate content for it. Plan your hours around this: roughly a third on features, a fifth on responsible use, and the rest spread evenly.

The other thing to know is how fast the product moves. Several features that older courses teach are retired (knowledge bases, Copilot Extensions, Copilot Workspace, the old `gh copilot suggest` and `gh copilot explain` extension, and Spark since 2026-08-31). When a practice question offers one of them, it is usually a distractor, and when a study source is built around them, it predates the outline.

## Study Approach

### Phase 1: Product Foundations (Week 1)

**Goal:** Build a clear mental model of what Copilot is, what plans exist, and where it runs.

1. **Know the Product Family**
   - Free, Pro, Pro+, Business, Enterprise
   - Which are per-user vs per-org
   - Billing cycle basics and seat assignment

2. **Know the Surfaces**
   - IDE inline and chat (VS Code, JetBrains, Visual Studio, Neovim, Xcode, Eclipse)
   - GitHub.com chat and repo-aware chat
   - GitHub Mobile
   - The Copilot CLI (`copilot`), an agent in the terminal
   - Pull requests (summaries, review, commit messages)

3. **Phase 1 Resources**
   - **[Copilot Overview](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)**
   - **[Plans for Copilot](https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)**
   - **[Copilot Quickstart](https://docs.github.com/en/copilot/quickstart)**

### Phase 2: Daily Use (Weeks 2-3)

**Goal:** Become fluent in Copilot as a daily tool so the exam reflects muscle memory.

1. **Inline Completions Mastery**
   - Tab to accept, Alt+] / Alt+[ to cycle
   - Partial acceptance (next word) with Ctrl+Right
   - Open the suggestions panel with Ctrl+Enter
   - Use multiple open tabs to enrich context

2. **Chat Mastery**
   - Memorize every slash command and what it does
   - Memorize agents (`@workspace`, `@vscode`, `@terminal`, `@github`)
   - Memorize context variables (`#file`, `#selection`, `#codebase`)
   - Practice iterative refinement with follow-up messages

3. **Prompt Engineering**
   - The 4 S's (Single, Specific, Short, Surround)
   - Zero-shot, one-shot, few-shot
   - Use comments, types, and signatures to seed prompts

4. **Phase 2 Resources**
   - **[Chat Cheat Sheet](https://docs.github.com/en/copilot/reference/chat-cheat-sheet)**
   - **[Best Practices](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)**
   - **[Prompt Engineering](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)**

### Phase 2b: Agents and Customization (Week 3)

**Goal:** Cover the agentic objectives that dominate the features area.

1. **Agent mode and Copilot Edits** - when Copilot chooses the steps versus when you choose the files
2. **MCP** - configure a server and watch the agent use it
3. **Sessions and sub-agents** - why isolated context keeps long tasks accurate
4. **Copilot CLI** - install, interactive and `-p` use, approvals, `/compact` and `/context`
5. **Customization files** - `copilot-instructions.md`, `.instructions.md` with `applyTo`, `.prompt.md`, custom agents
6. **Code review, Spaces, PR summaries** - and the organization policies that control them
7. **Phase 2b Resources**
   - **[Notes 07](notes/07-agents-cli-and-customization.md)**
   - **[Customization cheat sheet](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)**
   - **[About Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)**

### Phase 3: Responsible Use, Data and Administration (Week 4)

**Goal:** Understand the policy, security, and privacy surface area.

1. **Responsible AI**
   - Model limitations (hallucinations, outdated APIs, bias, insecure code)
   - Verification workflow: review, test, scan

2. **Data Handling**
   - Business/Enterprise: prompts and suggestions are not retained or used for training
   - Individual: user opts in or out of training
   - Data in transit encrypted; proxy strips prompts after response

3. **Content Exclusions**
   - Path-based rules at repo, org, enterprise scope
   - Changes can take up to 30 minutes to reach loaded IDEs; reload to apply sooner
   - Not supported in Edit and Agent modes of Copilot Chat
   - Suppresses suggestions inside excluded files and prevents files from being used as context
   - Does not retroactively remove public or already-sent data

4. **Duplicate Detection and IP Indemnity**
   - Duplicate detection filter blocks suggestions that match ~150 chars of public code
   - IP indemnity requires Business/Enterprise plus duplicate detection enabled

5. **Phase 3 Resources**
   - **[Trust Center](https://resources.github.com/copilot-trust-center/)**
   - **[Content Exclusions](https://docs.github.com/en/copilot/how-tos/configure-content-exclusion/exclude-content-from-copilot)**
   - **[Notes 08](notes/08-data-architecture-and-lifecycle.md)** - data flow, proxy filtering, the suggestion lifecycle
   - **[Notes 09](notes/09-productivity-testing-and-safeguards.md)** - productivity, tests, troubleshooting exclusions
   - **[Responsible Use](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features)**

### Phase 4: Review and Exam (Week 5)

**Goal:** Consolidate, take mock exams, identify gaps, ship the exam.

1. Run full scenarios under timing
2. Drill the feature matrix in both directions (feature to plan, plan to features)
3. Re-read any low-confidence sections
4. Take Microsoft's free practice assessment from the certification page

## Study Resources

### Official GitHub Resources
- **[Copilot Documentation](https://docs.github.com/en/copilot)** - Complete docs
- **[Copilot Trust Center](https://resources.github.com/copilot-trust-center/)** - Security and privacy
- **[Copilot Learning Pathway](https://learn.github.com/learning-pathways)** - Curated path
- **[GitHub Blog - Copilot tag](https://github.blog/tag/github-copilot/)** - New features
- **[GitHub Skills](https://skills.github.com/)** - Hands-on courses

### Free Learning Resources
- **[Copilot Quickstart](https://docs.github.com/en/copilot/quickstart)** - 10-minute intro
- **[YouTube - GitHub](https://www.youtube.com/github)** - Demos and walkthroughs
- **[GitHub Universe talks](https://githubuniverse.com/)** - Deep-dive content

### Practice Platforms
- Your own repositories across multiple languages
- A sandbox org on GitHub Free where you can try Business settings (trial)
- Public open source issues for realistic chat practice

## Exam Tactics

### Question Strategy
1. **Read the full stem** - Many Copilot questions include constraints like plan type or IDE
2. **Identify the plan context** - Enterprise-only features are common distractors
3. **Eliminate retired features** - knowledge bases, Copilot Extensions, Workspace and `gh copilot suggest` / `explain` are gone
4. **Prefer official terminology** - Use exact names like "duplicate detection filter" and "content exclusions"
5. **Watch for responsible-use flags** - Questions often test whether you verify, test, or scan AI output

### Time Management
- **100 minutes**; Microsoft does not publish the question count, so check the count on the first screen and budget from it
- **First pass (about 65 minutes):** answer confident items, flag uncertain
- **Second pass (about 25 minutes):** revisit flagged
- **Final (about 10 minutes):** sanity-check, make sure nothing is blank
- Do not exceed 3 minutes on any single question on the first pass

### Question Types to Expect
- **Feature to plan mapping** - Which plan includes X?
- **Command recognition** - What does `/fix` do? What does `@workspace` do? What does `copilot -p` do?
- **Which mode or surface** - inline, ask, Copilot Edits, agent mode, CLI, or coding agent?
- **Which customization file** - instructions, path-specific instructions, or a prompt file?
- **Policy scenarios** - Where do you configure Y?
- **Responsible use** - Given situation X, what should the developer do?
- **Prompt patterns** - Which prompt will most likely produce correct code?

### Key Differentiators to Study

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| Duplicate detection filter | Content exclusions | Detection blocks matches to public code; exclusions block files from context |
| Copilot Edits | Agent mode | Edits works on files you choose; agent mode chooses its own steps |
| Instructions file | Prompt file | Instructions apply to every request; a prompt file runs when invoked |
| Spaces | Content exclusions | Spaces add curated context; exclusions remove files from context |
| `@workspace` | `@github` | Workspace is IDE repo context; github queries github.com data |
| Inline suggestion | Chat | Inline is ghost text; chat is conversational |
| Copilot Pro | Copilot Pro+ | Pro+ has higher premium request limits and all models |
| Content exclusions | Private repo | Exclusions affect Copilot context specifically; private repo affects visibility |
| IP indemnity | Responsible use | Indemnity is a contractual commitment; responsible use is a practice |

## Common Pitfalls

### Product Confusion
- **Studying retired features** - knowledge bases became Spaces, Extensions became MCP, `gh copilot suggest` / `explain` became the Copilot CLI
- **Assuming all chat features exist everywhere** - Some are IDE-only, some are github.com-only
- **Forgetting Copilot Free exists** - It has limited completions and chat per month

### Responsible Use
- **Thinking content exclusions protect already-sent data** - They only affect future requests
- **Expecting exclusions to apply instantly or everywhere** - up to 30 minutes to reach IDEs, and not in Edit or Agent modes
- **Assuming IP indemnity is automatic** - It requires duplicate detection to be enabled
- **Believing Copilot never sees private code** - It sees your current editor context by design

### Usage
- **Confusing slash commands with agents** - `/explain` vs `@workspace` are different surfaces
- **Not using context variables** - `#file` and `#selection` dramatically improve quality
- **Using vague prompts** - Ignoring the 4 S's is a common bad habit

### Administration
- **Not knowing scope hierarchy** - Enterprise > Organization > Repository for exclusions and policies
- **Ignoring audit logs** - Copilot emits events for seat management and policy changes
- **Confusing Copilot with GHAS** - They are separate products; do not mix features
