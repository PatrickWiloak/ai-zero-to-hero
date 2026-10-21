---
last-updated: 2026-08-09
difficulty: beginner
---

# GitHub Copilot Certification - Practice Questions

15 questions for the GitHub Copilot exam, weighted toward using Copilot (25%), introduction (20%), then plans and features, developer use cases, responsible use, and prompt engineering.

> **Cert page:** [exams/github/copilot/](../github/copilot/README.md)

---

### Question 1
**Scenario:** What does Copilot use to generate a suggestion?

A. A search of public repositories at request time, with the closest match pasted in verbatim
B. A large language model given context from your open files and prompt
C. Your git history and commit messages only, searched for the most similar earlier changes
D. A fixed library of code snippets that is matched to what you type by keyword

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Suggestions are generated, not retrieved, which is why they are novel and also why they can be confidently wrong. The context sent includes the current file and related open tabs, which is why keeping relevant files open improves suggestions noticeably.
</details>

---

### Question 2
**Scenario:** A suggestion compiles and looks correct.

A. Accept it without review, since the model was trained on high-quality code and has already checked it for errors and unsafe patterns
B. Trust it because it compiles
C. Review it as you would a colleague's code: correctness, security, performance, and whether it fits the codebase
D. Run it in production to test

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The developer who commits the code is responsible for it. Generated code compiles far more reliably than it is correct, and the plausible-but-subtly-wrong case is the one that costs the most to find later.
</details>

---

### Question 3
**Scenario:** An organization is concerned Copilot might suggest code matching public repositories.

A. Rely on the repository's LICENSE file, since Copilot reads it and never suggests code under other licenses
B. Enable the duplication detection filter, which blocks suggestions matching public code
C. Nothing can be done
D. Disable Copilot

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The filter suppresses suggestions that match public code above a length threshold, which addresses the licensing concern most legal teams raise. Copilot Business and Enterprise also carry IP indemnification when the filter is enabled, which is examinable.
</details>

---

### Question 4
**Scenario:** Copilot must not use an organization's code to train models.

A. Training cannot be controlled
B. Only individual plans are safe
C. It always trains on your code
D. Copilot Business and Enterprise do not use customer code for model training, and admins control telemetry and data retention settings

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The data handling difference between individual and business plans is a standard exam and procurement question. Knowing that prompts and suggestions are not retained for training on business plans is usually what unblocks adoption.
</details>

---

### Question 5
**Scenario:** A developer wants Copilot to write a function matching a specific behavior.

A. An empty file
B. A specific comment stating inputs, outputs and edge cases, with a descriptive function name
C. Random keystrokes typed into the file, so that the model has plenty of text to work from when it guesses
D. A vague one-line comment such as 'make it work', with no names, types or examples nearby to give context

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Copilot infers intent from context, so specificity in names, signatures, and comments is the main quality lever. Existing similar code in an open file acts as an implicit style example, which is why suggestions improve as a file develops.
</details>

---

### Question 6
**Scenario:** Copilot Chat is asked to explain unfamiliar code.

A. Select the code and ask, using slash commands such as `/explain`, `/fix`, and `/tests` for common tasks
B. Only inline completion exists, so unfamiliar code can be understood only by reading it line by line yourself
C. It cannot explain code
D. Copy the code to a web search

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Chat with a selection is the fastest way into unfamiliar code, and the slash commands wrap the common intents. Onboarding to a new codebase is one of the strongest documented use cases, ahead of writing brand-new code.
</details>

---

### Question 7
**Scenario:** Which Copilot capability reviews a pull request?

A. Copilot code review, which suggests changes on a pull request
B. Secret scanning, which flags committed credentials and token patterns in the repository and its pull requests
C. Dependabot, which opens pull requests to update vulnerable or outdated dependencies
D. There is none; pull requests can only be reviewed by people on the team

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Copilot can review a pull request and leave suggestions, which catches straightforward issues before a human reviewer spends attention on them. It supplements human review rather than replacing the judgment about design and intent.
</details>

---

### Question 8
**Scenario:** Tests must be generated for existing code.

A. Ask Copilot to generate tests, then review that they assert meaningful behavior and cover edge cases rather than just passing
B. Tests are always correct
C. Only the developer can write tests
D. Copilot cannot write tests

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Test generation is a strong use case because the surrounding code supplies clear context. The review that matters is whether the assertions are meaningful: tests generated from an implementation can encode the current behavior, including its bugs.
</details>

---

### Question 9
**Scenario:** Copilot suggests code using a deprecated API.

A. Report it as a bug to GitHub support and wait for the model to be corrected before using any suggestion from it
B. Verify against current documentation, because the model's knowledge has a cutoff
C. Use it anyway
D. Assume it is current, because Copilot only ever suggests APIs that are still supported today

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Training data has a cutoff, and API deprecation is exactly the kind of change that lands after it. Copilot Chat with repository or web context can help, but the documentation remains the authority for what is current.
</details>

---

### Question 10
**Scenario:** An organization wants Copilot to understand its internal codebase and standards.

A. Fine-tune the underlying model yourself by uploading the organization's repositories to the model vendor
B. Paste the standards into every prompt by hand, which the model remembers permanently across all later chat sessions
C. Copilot Spaces holding the key repositories and docs, plus repository custom instructions
D. Not possible

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Custom instructions in the repository apply automatically to Copilot's context, and Copilot Spaces group repositories, files, issues and notes so chat answers from internal sources. Both remove the need to restate context on every request. Spaces replaced knowledge bases, which GitHub retired on 1 November 2025.

**Key Concept:** [Copilot Spaces](https://docs.github.com/en/copilot/concepts/context/spaces)
</details>

---

### Question 11
**Scenario:** Which describes a limitation developers should know?

A. It cannot generate code
B. Copilot is always correct because it checks each suggestion against the compiler, so no review or security scanning is needed by the team
C. It only works on Python and JavaScript projects and cannot be used with any other programming language
D. It can produce buggy, insecure or unlicensed code, and it does not know your requirements

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Being able to state the limitations is explicitly part of the responsible use domain. The one people underweight is that Copilot cannot know your requirements: it produces plausible code for the context, not correct code for your intent.
</details>

---

### Question 12
**Scenario:** Copilot must be disabled for specific file types containing secrets.

A. Delete the files from the repository and rewrite the git history to remove every copy of them
B. It is not configurable, so the sensitive files have to be moved into a separate repository
C. Content exclusions at repository or organization level, naming the paths to ignore
D. Disable Copilot entirely for every user in the organization, accepting the loss of all completions and chat

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Content exclusions stop configured paths being used as context or receiving completions, which is how you keep `.env` files and key material out of the request. It is a per-repository or organization admin setting rather than a per-developer choice.
</details>

---

### Question 13
**Scenario:** Where can Copilot be used?

A. One IDE only
B. Only on Windows desktops, because the extension depends on a Windows-only runtime and the service is hosted there too
C. Only in the browser
D. In IDEs (VS Code, Visual Studio, JetBrains, Neovim), on GitHub.com, in the CLI, and in mobile, depending on plan

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Surface coverage differs by plan, and the CLI integration for shell commands plus chat on GitHub.com for pull requests and issues are the two people most often do not realize exist.
</details>

---

### Question 14
**Scenario:** A team wants to measure whether Copilot is helping.

A. Lines of code generated
B. Count suggestions
C. Adoption and acceptance metrics from the Copilot metrics API, alongside outcome measures such as cycle time and developer survey results
D. It cannot be measured

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Lines of code is a famously poor proxy that rewards verbosity. Usage metrics tell you whether people are using it; delivery and satisfaction measures tell you whether it is helping, and only the pair is meaningful.
</details>

---

### Question 15
**Scenario:** Prompt engineering for Copilot in one principle.

A. Give it context and specificity: clear names, a stated goal, relevant open files, and iteration
B. Prompting does not matter, because the model ignores the comments and names and reads only the file name
C. Use single letters for variable and function names, so that the model is free to choose what they all mean
D. Write less: keep every comment to two or three words, so the model is not distracted by extra detail

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Context and specificity are the levers. Treating a poor suggestion as a signal to add detail, rather than as a failure, is the working habit that separates productive use from frustration.
</details>

---

## Where to go deeper

- [GitHub Copilot cert page](../github/copilot/README.md) - notes, practice plan, strategy
- [GitHub Foundations practice questions](https://cloud.noblerworks.com/resources/practice-questions/github-foundations/) - the platform fundamentals
- [Prompt engineering](../../learn/concepts/prompt-engineering.md) - the general skill
- [AI security topic index](../../safety/README.md) - responsible use in a wider frame
- **[📖 GitHub Certifications](https://learn.github.com/certifications)** - official exam pages
