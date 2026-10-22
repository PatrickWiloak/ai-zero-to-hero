---
last-updated: 2026-10-22
difficulty: beginner
---

# GitHub Copilot Certification - Practice Questions

30 questions for the GitHub Copilot exam (GH-300). Questions 16-30 follow the skills measured as of 2026-08-07: use GitHub Copilot features (25-30%), use Copilot responsibly (15-20%), then data and architecture, prompt engineering and context crafting, developer productivity, and privacy, content exclusions and safeguards (10-15% each).

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

### Question 16
**Scenario:** Copilot suggests a database query built by concatenating user input into a SQL string. The developer is in a hurry.

A. Accept it, since Copilot only suggests code that has passed a security review
B. Treat it as SQL injection risk and use parameterised queries
C. Accept it and add a comment saying Copilot wrote it
D. Reject Copilot entirely for the rest of the project

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Generative tools can reproduce insecure patterns, so suggestions get the same scrutiny as human code, and security tooling backs that up. Copilot does not guarantee secure output. A comment does not remove the risk. Dropping the tool over one bad suggestion overreacts; validation is the habit.
</details>

### Question 17
**Scenario:** A pull request contains code that was suggested by Copilot and accepted by a developer. A bug in it reaches production. Who is responsible for the code?

A. GitHub, because Copilot wrote it
B. The model provider, because the model generated it
C. Nobody, because AI-generated code has no owner
D. The developer and team who accepted, reviewed and merged it

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Copilot is an assistant; the people who accept and ship the code remain accountable for it, which is why review and testing still apply. Responsible use means humans stay in charge of what goes into the codebase.
</details>

### Question 18
**Scenario:** Copilot generates a regular expression to validate email addresses. It looks plausible.

A. Test it against valid, invalid and edge-case inputs
B. Accept it, since regular expressions are easy for models
C. Ask Copilot whether the regex is correct and accept a "yes"
D. Use it only in production, where real data will show whether it works

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** AI output must be validated, and tests with edge cases are how you validate a regex. Plausible-looking patterns often have gaps. Asking the same tool to grade itself is weak evidence. Testing in production lets users find the bugs.
</details>

### Question 19
**Scenario:** A developer needs a change across several files, including running the test suite and fixing failures until it passes, with the developer approving the steps.

A. Inline code completions in the open file
B. Copilot Chat in ask mode, copying each answer into the files by hand
C. Agent mode in the IDE
D. Pull request summaries

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Agent mode works across files, runs terminal commands such as tests, and iterates on the results, with the developer able to review and approve. Inline completions work at the cursor. Ask mode answers questions but does not apply and verify changes. PR summaries describe changes rather than making them.
</details>

### Question 20
**Scenario:** A developer spends most of the day in the terminal and wants Copilot's help to write shell scripts, explain commands and work with files without opening an IDE.

A. GitHub Copilot CLI
B. Copilot code review on github.com
C. Copilot inline suggestions in the IDE
D. GitHub Pages

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Copilot CLI brings Copilot into the terminal, where it can answer questions, generate scripts and work with files interactively. Code review runs on pull requests. Inline suggestions need an editor. GitHub Pages hosts websites.
</details>

### Question 21
**Scenario:** A team keeps typing the same long request to scaffold a new API endpoint in their style. They want one reusable prompt that everyone in the repository can run.

A. Paste the request into the README and copy it each time
B. Rely on chat history from a previous session
C. Turn on the public code filter
D. Save it as a prompt file in the repository

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Prompt files store reusable prompts in the repository so everyone gets consistent results. Custom instruction files are the related feature for standing guidance that applies to every request. Copying from a README is manual. Chat history is per session. The public code filter is unrelated.
</details>

### Question 22
**Scenario:** An organisation onboards and offboards hundreds of developers each month and wants Copilot seats assigned and removed automatically from its HR system.

A. Ask each developer to buy their own Copilot Pro plan
B. Use the Copilot user management REST API
C. Assign seats by hand in the settings page every Friday
D. Give every member a seat permanently, whether they still work there or not

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The REST API lets an organisation manage Copilot seat assignments programmatically, so the HR system can drive it. Personal plans bypass organisation policy. Weekly manual changes lag and cost money. Leaving seats for departed staff wastes licences and access control.
</details>

### Question 23
**Scenario:** An administrator asks where the filter that blocks suggestions matching public code is applied in Copilot's flow.

A. Before the prompt is built, by removing the open files from context
B. Inside the developer's compiler at build time
C. After the model generates a suggestion, as part of post-processing before it is shown
D. In the git pre-commit hook on the developer's machine

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Copilot's pipeline builds a prompt from context, passes it through the proxy to the model, then post-processes the response, which is where suggestions matching public code can be filtered. The filter does not remove context, run in the compiler or depend on git hooks.
</details>

### Question 24
**Scenario:** A developer is surprised that a completion ignores a helper function defined in a file that is not open anywhere in the editor.

A. Completions only see limited context, mainly open files
B. Copilot reads every file in the repository for every completion
C. The helper function must be written in a different language
D. Copilot only works in files under 100 lines

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Context for completions is limited and comes mainly from the cursor position, the current file and open or related files. Opening the relevant file, or referencing it in chat, improves results. Copilot does not read the whole repository for each completion, and language and file length are not the cause.
</details>

### Question 25
**Scenario:** A developer wants Copilot Chat to write new unit tests in exactly the structure the team uses, and includes two existing tests in the prompt as examples.

A. Zero-shot prompting
B. Role prompting with no examples
C. Prompt chaining across separate tools
D. Few-shot prompting

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Giving the model a few examples of the desired output is few-shot prompting, and it is effective for matching an existing style. Zero-shot means no examples. A role alone does not show the structure. Prompt chaining splits a task into steps, which is not what is happening here.
</details>

### Question 26
**Scenario:** After a long chat about a payment module, the developer asks about an unrelated logging library and gets answers mixed with payment details.

A. Lower the temperature in the IDE settings so answers stay focused
B. Start a new chat thread for the new topic
C. Ask the same question five more times
D. Uninstall and reinstall the extension

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Chat history becomes part of the prompt, so earlier turns about a different topic can pull the answer off course. A fresh thread gives clean context. Repeating the question keeps the same history. Reinstalling changes nothing, and temperature is not the issue.
</details>

### Question 27
**Scenario:** A team must convert a legacy module from an old language to a modern one and cannot afford behaviour changes.

A. Ask Copilot to translate the whole module at once and deploy the result
B. Rewrite it by hand without looking at the old code
C. Explain it, pin behaviour with tests, then translate in parts
D. Ask Copilot for a summary and delete the old code

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Modernising with Copilot works best when the existing behaviour is understood and pinned down by tests before translating, so each step can be verified. A one-shot translation deployed untested risks silent changes. Ignoring the old code loses its rules. A summary is not a replacement.
</details>

### Question 28
**Scenario:** Copilot generated tests for a date-range function, but they only check one ordinary case.

A. Ask for edge-case tests and review the assertions
B. Accept the tests, since any test that passes is enough to show the function works
C. Delete the tests and ship the function untested
D. Increase the test timeout

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Copilot can help identify and test edge cases if asked, and the developer still checks that the assertions are meaningful. One happy-path test misses the bugs that matter. No tests is worse. A timeout setting has nothing to do with coverage.
</details>

### Question 29
**Scenario:** An administrator adds a content exclusion for `secrets/**`. A few minutes later a developer still gets suggestions in an excluded file.

A. Content exclusions only apply to public repositories
B. Exclusions have to be added again by every developer
C. The exclusion syntax requires listing every file by name
D. Settings take time to reach IDEs; reload the editor

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** GitHub documents that a new or changed exclusion can take up to 30 minutes to reach IDEs that have already loaded the settings; reloading the window in VS Code, or restarting Visual Studio or a JetBrains IDE, picks it up sooner (Vim and Neovim fetch exclusions each time a file opens). Exclusions work for private repositories, are set centrally by administrators, and accept path patterns.
</details>

### Question 30
**Scenario:** An organisation allows suggestions that match public code, but wants developers to see where the code came from and under what licence.

A. Block all suggestions, since public code can never be used
B. Turn off Copilot for every repository that uses open source
C. Allow matches and use code referencing
D. Add a note in the README asking developers to search GitHub by hand

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** When matches are allowed, code referencing reports matching public code with details such as the repository and licence, so developers can decide how to use it. Blocking everything or disabling Copilot goes beyond the stated policy. Manual searching is unreliable.
</details>

---

## Where to go deeper

- [GitHub Copilot cert page](../github/copilot/README.md) - notes, practice plan, strategy
- [GitHub Foundations practice questions](https://cloud.noblerworks.com/resources/practice-questions/github-foundations/) - the platform fundamentals
- [Prompt engineering](../../learn/concepts/prompt-engineering.md) - the general skill
- [AI security topic index](../../safety/README.md) - responsible use in a wider frame
- **[📖 GitHub Certifications](https://learn.github.com/certifications)** - official exam pages
