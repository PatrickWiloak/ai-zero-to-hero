# GitHub Copilot Certification Exam Guide (GH-300)

## Exam Overview

The GitHub Copilot certification (exam GH-300) validates that you can use GitHub Copilot to improve software development productivity, quality and security. Microsoft's audience profile names responsible AI use, prompt engineering, Copilot features across the plans, and privacy safeguards, and expects familiarity with GitHub fundamentals and at least one programming language. The current skills outline, **as of 2026-08-07**, has moved well beyond ghost text and chat: agent mode, the Copilot CLI, MCP, sub-agents, instructions and prompt files, Copilot code review policies and subscription management through the REST API are all named objectives.

### Exam Details
- **Exam code:** GH-300
- **Duration:** 100 minutes (it was 90 before the current outline)
- **Format:** Multiple choice and multiple response; may include interactive components
- **Number of questions:** Not published by Microsoft
- **Passing score:** 700 on a 1-1000 scale
- **Cost:** Set by the country where the exam is proctored (around USD 99 in the US)
- **Delivery:** Pearson VUE (online proctored or test centre)
- **Languages:** English, Spanish, Portuguese (Brazil), Korean, Japanese
- **Prerequisites:** None required; Git, GitHub and IDE familiarity recommended
- **Validity:** 2 years; GitHub is moving to Microsoft's recertification process
- **Retake policy:** 24 hours after the first attempt; longer for later attempts
- **Skills outline checked:** 2026-10-22 against the [GH-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300)

### Official Resources
- **[GH-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300)** - the skills measured; study against this
- **[GitHub Copilot certification page](https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/)** - registration, duration, free practice assessment
- **[GitHub Copilot Documentation](https://docs.github.com/en/copilot)** - complete product docs
- **[GitHub Copilot Fundamentals Part 1](https://learn.microsoft.com/en-us/training/paths/copilot/)** and **[Part 2](https://learn.microsoft.com/en-us/training/paths/gh-copilot-2/)** - the official learning paths
- **[GitHub Trust Center](https://github.com/trust-center)** - how Copilot handles data

## Skills Measured (as of 2026-08-07)

The outline lists **seven skill areas**. One of them needs a warning: the published "skills at a glance" contains both "Use GitHub Copilot features (25-30%)" and a second line, "GitHub Copilot features (25-30%)", that has no objectives of its own anywhere in the study guide. It reads as a duplicate of the first. Counting it, the ranges add up to well over 100%; leaving it out, they bracket 100% the way Microsoft outlines normally do. Study the six areas that have objectives, and treat "Use GitHub Copilot features" as the single biggest area on the exam.

| # | Skill area | Weight | Notes in this repo |
|---|---|---|---|
| 1 | Use GitHub Copilot responsibly | 15-20% | [04](notes/04-security-privacy-and-data-handling.md), [08](notes/08-data-architecture-and-lifecycle.md) |
| 2 | Use GitHub Copilot features | 25-30% | [02](notes/02-code-completions-and-chat.md), [03](notes/03-ide-integration-and-workflows.md), [05](notes/05-enterprise-administration.md), [07](notes/07-agents-cli-and-customization.md) |
| 3 | GitHub Copilot features | 25-30% | Listed in the outline with no objectives; see above |
| 4 | Understand GitHub Copilot data and architecture | 10-15% | [08](notes/08-data-architecture-and-lifecycle.md) |
| 5 | Apply prompt engineering and context crafting | 10-15% | [06](notes/06-prompt-engineering-for-copilot.md) |
| 6 | Improve developer productivity with GitHub Copilot | 10-15% | [09](notes/09-productivity-testing-and-safeguards.md) |
| 7 | Configure privacy, content exclusions, and safeguards | 10-15% | [04](notes/04-security-privacy-and-data-handling.md), [09](notes/09-productivity-testing-and-safeguards.md) |

### What changed from the older outline

Older guides (and older versions of this page) described six domains with fixed percentages and a 90-minute exam: introduction, responsible use, plans and features, using Copilot, prompt engineering and developer use cases. The current outline regroups that content and adds a great deal. New or much expanded: agent mode, Copilot Edits and MCP; managing agent sessions and delegating to sub-agents; the Copilot CLI as a full objective group; Copilot code review and organization policies for it; Spaces, Spark and pull request summaries; instructions files and prompt files; audit log events; subscription management through the REST API; and a separate area on data flow, prompt building, proxy filtering and the suggestion lifecycle. Several products named in older material have since been retired (Copilot Workspace, knowledge bases, GitHub App-based Copilot Extensions and the old `gh-copilot` extension), so treat any study source that leans on them as out of date.

### 1. Use GitHub Copilot responsibly (15-20%)

This area is about judgment rather than features. You need to describe the risks and limitations of generative AI tools (confident but wrong code, insecure patterns, outdated APIs, bias, suggestions that match public code), describe what ethical and responsible use looks like, and identify harms with their mitigations. The second objective group, "validate and operate AI tools", is the practical core: explain why every piece of AI output must be validated (read it, test it, scan it, review it like a colleague's code) and how to operate Copilot responsibly day to day, which means the developer stays accountable for what gets committed. Expect scenario questions where the right answer is "review and test before merging" rather than any product setting.

### 2. Use GitHub Copilot features (25-30%)

The largest area, with four objective groups.

**Copilot in the IDE.** Enable Copilot in the editor, trigger it through inline suggestions, chat, the CLI and agent mode, and configure content exclusions for specific files or repositories from the application's point of view (what a developer sees when a file is excluded).

**Copilot CLI.** Define what the Copilot CLI is and why developers use it, install it, describe its key features and commands, use it interactively and in sessions, and use it to generate scripts and manage files. This is the current agentic CLI started with `copilot`, not the retired `gh copilot suggest` and `gh copilot explain` extension.

**Features and capabilities.** Use agent mode, Copilot Edits and MCP; manage agent sessions and delegate tasks to sub-agents to keep context focused; use Copilot for code review and coding help; use Spaces, Spark, pull request summaries and review standards set through instructions files; and know the limits, options, feedback mechanisms and commands of Copilot Chat, including reusing prompt files for consistent responses.

**Organization settings and policies.** Configure organization-wide policies (including Copilot code review policies and which features are available in IDEs and on github.com), use audit log events, and manage subscriptions through the REST API.

### 3. GitHub Copilot features (25-30%)

Listed in the skills at a glance and on the certification page, but with no objectives in the study guide. Prepare for it by covering area 2 thoroughly.

### 4. Understand GitHub Copilot data and architecture (10-15%)

How a request travels. You need to explain how data is used, where it flows and with whom it is shared; how Copilot processes input and builds a prompt from the code around the cursor, open files and chat history; and how the proxy filters requests and post-processes responses (content exclusions, harmful-content filtering, the public code filter). The second group asks you to describe the lifecycle of a code suggestion from keystroke to accepted code, and to describe the limitations of LLMs and of Copilot specifically.

### 5. Apply prompt engineering and context crafting (10-15%)

Describe how a prompt is structured and how Copilot decides what context to include, use zero-shot and few-shot prompting, and apply prompt-crafting best practice (clear goal, specific detail, examples, breaking work into steps). The second group covers the principles behind prompt engineering and the prompt process flow, including how chat history is carried into later turns and why a fresh thread helps when a conversation drifts.

### 6. Improve developer productivity with GitHub Copilot (10-15%)

Use Copilot to generate, refactor and document code; accelerate learning and reduce context switching; generate sample data; and modernize legacy code. The testing and security group asks you to generate unit and integration tests, identify edge cases and write assertions, and have Copilot suggest security improvements and performance optimizations, always with the developer checking the result.

### 7. Configure privacy, content exclusions, and safeguards (10-15%)

Configure content exclusions and editor settings, and describe who owns Copilot's output and what its limits are. Then apply safeguards: enable the filter that blocks suggestions matching public code, and resolve problems with suggestions and with content exclusions (for example, an exclusion that has not reached an IDE yet; changes can take up to 30 minutes and a window reload applies them sooner).

## Study Approach

### Recommended Path
1. **Week 1:** Responsible use, data flow and the suggestion lifecycle (areas 1 and 4)
2. **Week 2:** The IDE, chat, agent mode, Copilot Edits and MCP (area 2)
3. **Week 3:** The Copilot CLI, customization files, Spaces, code review and organization policies (area 2)
4. **Week 4:** Prompt engineering and productivity, including tests and security (areas 5 and 6)
5. **Week 5:** Privacy, content exclusions and safeguards, then review and the free practice assessment (area 7)

### Hands-On Practice
- Use Copilot daily in VS Code plus one other IDE, in ask, edit and agent modes
- Install the Copilot CLI, run an interactive session, then a programmatic one with `-p`
- Add a `.github/copilot-instructions.md`, one path-specific `.instructions.md` and one `.prompt.md` to a test repository
- Configure an MCP server in the IDE and in the CLI
- Create a Copilot Space from a repository and some notes
- Request a Copilot code review on a pull request
- Configure a content exclusion on a test repository and watch it take effect
- Call the Copilot seat management REST endpoints against a test organization if you have one

### Study Materials
- **[GH-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300)** - the authoritative outline
- **[Copilot Docs](https://docs.github.com/en/copilot)** - primary reference
- **[Copilot customization cheat sheet](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)** - instructions, prompt files, agents, skills, hooks, MCP
- **[About Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)** - the CLI objective group
- **[Content exclusions](https://docs.github.com/en/copilot/how-tos/configure-content-exclusion/exclude-content-from-copilot)** - configuration and troubleshooting
- **[GitHub Changelog - Copilot](https://github.blog/changelog/label/copilot/)** - features move fast; check what has been retired

### Tips for Success
- Spend the most time on area 2; it is the largest by weight and the most changed
- Know the agentic features by name: agent mode, Copilot Edits, coding agent, sub-agents, MCP
- Know where each customization file lives and what it does
- Separate content exclusions (keep files out of context) from the public code filter (block suggestions that match public code)
- Check every study source's date; anything built around `gh copilot suggest`, knowledge bases or Copilot Extensions predates the current outline
- Take Microsoft's free practice assessment on the certification page
