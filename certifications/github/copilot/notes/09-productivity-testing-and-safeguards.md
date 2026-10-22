# Productivity, Testing and Safeguards

This note covers skill area 6, "Improve developer productivity with GitHub Copilot" (10-15%), and the troubleshooting half of skill area 7, "Configure privacy, content exclusions, and safeguards" (10-15%). Configuration of exclusions, the public code filter and data retention is in [note 04](04-security-privacy-and-data-handling.md); prompting technique is in [note 06](06-prompt-engineering-for-copilot.md).

**[📖 Developer use cases for AI with GitHub Copilot](https://learn.microsoft.com/en-us/training/modules/developer-use-cases-for-ai-with-github-copilot/)** - official module
**[📖 Develop unit tests using GitHub Copilot tools](https://learn.microsoft.com/en-us/training/modules/develop-unit-tests-using-github-copilot-tools/)** - official module
**[📖 Exclude content from Copilot](https://docs.github.com/en/copilot/how-tos/configure-content-exclusion/exclude-content-from-copilot)** - setup and timing

---

## Generation, refactoring and documentation

The first productivity objective is to "use Copilot for code generation, refactoring, and documentation". For **generation**, the pattern that works is to state intent before asking: a function signature with types and a short comment saying what it must do, or a chat request that names inputs, outputs and constraints. Copilot fills in boilerplate fastest (data classes, API clients, configuration, CRUD handlers), which is where most of the time saving comes from. For **refactoring**, select the code and say what should change and what must stay the same ("extract the validation into its own function without changing behaviour"); for changes across several files, Copilot Edits or agent mode can apply them as one reviewable diff, and the existing tests are what prove behaviour did not change. For **documentation**, `/doc` writes doc comments for a selection, chat can draft a README or explain an architecture from the code, and pull request summaries draft the description of a change. In each case the developer checks accuracy: documentation that confidently describes behaviour the code does not have is worse than none.

## Learning and reducing context switching

"Accelerate learning and reduce context switching" is about staying in the editor. Instead of leaving to search the web, you can ask chat to explain an unfamiliar block (`/explain`), a language feature, a regular expression, a failing command or an error message, and follow up until it makes sense. Joining a new codebase becomes "how is authentication handled in this repository?" asked in chat with the codebase as context, or inside a Copilot Space built for onboarding. Learning a new language becomes writing in it with suggestions as a guide and asking why when a suggestion surprises you. The time saved is less about typing and more about not breaking concentration. The caution is that explanations can be wrong too, so check them against the code and the official documentation, especially for very new libraries.

## Sample data and legacy modernization

**Sample data.** Copilot is good at producing realistic test fixtures: a JSON array of fifty customers with varied names and addresses, a CSV with edge-case values, SQL insert statements matching a schema you show it. Give it the schema and the variety you need, and never paste real personal data into a prompt to get "realistic" output.

**Legacy modernization.** For old code, Copilot can explain what a COBOL paragraph or a dense legacy function does, propose a translation to a modern language, update deprecated APIs, and add the tests that make the change safe. The safe order is: understand the legacy code (ask Copilot to explain it), capture its current behaviour in tests, then migrate in small steps with those tests passing at each step. Agent mode or the coding agent can carry out a well-specified migration across many files, but a large rewrite in one shot is exactly where hallucinated behaviour slips through.

## Generating tests, edge cases and assertions

The testing group has three objectives. To **generate unit and integration tests**, select the code and use `/tests`, or describe the test in chat, naming the framework your project uses (pytest, Jest, JUnit) and any fixtures or mocks to reuse; Copilot follows the style of existing test files it can see, so keeping one open helps. Unit tests isolate one function with dependencies mocked; integration tests exercise several components together, such as an API handler with a real test database, and need you to describe the setup.

To **identify edge cases and write assertions**, ask directly: "what edge cases does this function not handle?" Copilot will typically suggest empty input, null or missing values, boundary numbers (zero, negative, maximum), very large inputs, invalid formats, duplicate entries, concurrency and error paths. Then ask for tests that assert specific expected outcomes, not just that the function runs. The trap to recognize is a generated test that asserts whatever the current code returns: if the code is wrong, the test enshrines the bug. Decide the expected value from the requirement, not from the implementation.

Agents can go further: in agent mode, Copilot can write the tests, run them, read the failures and fix either the test or the code, iterating until the suite passes. Review what it changed, because "make the tests pass" can be satisfied by weakening a test.

## Security improvements and performance optimizations

"Suggest security improvements and performance optimizations" means using Copilot as a reviewer. Ask it to look at a function for injection risks, missing input validation, hard-coded secrets, unsafe deserialization or weak cryptography, and to propose fixes; Copilot code review on pull requests does the same at merge time, steered by your instructions files. For performance, ask it to find inefficient loops, repeated queries (the N+1 pattern), unnecessary allocations or a better data structure, and to explain the trade-off. Copilot complements, and does not replace, dedicated tools: code scanning, secret scanning and dependency review catch classes of problems systematically, and a benchmark, not a confident explanation, proves an optimization.

## Troubleshooting suggestions and content exclusions

The safeguards area ends with "resolve issues with suggestions and content exclusions". Work through it in the order of the suggestion lifecycle ([note 08](08-data-architecture-and-lifecycle.md)).

**No suggestions at all.** Check that the user is signed in and has an assigned seat, that Copilot is enabled for the language and the file type in the editor settings, that the organization policy allows the feature, and that a network proxy or firewall is not blocking Copilot's endpoints. The editor's Copilot status indicator and its log output show which of these it is.

**No suggestions in one file or folder.** That is usually a content exclusion working as designed; the status indicator shows that the file is excluded. If the developer believes it should not be excluded, an administrator checks the repository and organization rules.

**An exclusion that does not seem to work.** GitHub documents that a new or changed exclusion can take **up to 30 minutes** to reach IDEs that have already loaded the settings. To apply it sooner, reload the window in VS Code (Command Palette, "Developer: Reload Window") or restart Visual Studio or a JetBrains IDE; Vim and Neovim fetch exclusions each time a file is opened. Also check the path pattern syntax and the scope (repository rules apply to that repository; organization rules can target other repositories). Remember the documented limits of exclusions too, because a "bug" is sometimes one of them: content exclusion is not supported in the Edit and Agent modes of Copilot Chat in VS Code and other editors; it does not apply to symbolic links or to repositories on remote filesystems; and it cannot stop the IDE from passing along semantic information from an excluded file indirectly, such as type information or hover definitions. It is available on Copilot Business and Enterprise.

**Suggestions that appear then disappear, or that are never offered for a familiar snippet.** The public code filter may be blocking a match; with code referencing enabled instead, the suggestion appears with a reference to the matching repository and licence.

**Poor or irrelevant suggestions.** Usually a context problem: open the related files, add a descriptive comment or signature, attach the right files in chat, start a fresh thread, or add repository instructions that state the conventions.

## Ownership and limitations of output

The privacy area also asks you to "describe ownership and limitations of outputs". GitHub does not claim ownership of the suggestions Copilot generates; the user is responsible for the code they accept, as with any code they write or copy. That responsibility is why the limitations matter: suggestions can be incorrect, insecure or similar to public code, and on Business and Enterprise plans GitHub's IP indemnity applies to unmodified suggestions only when the public code filter is set to block matches. The safeguard is the same throughout: review, test and scan before merging.

## Key Exam Facts

- State intent first (signature, comment, constraints) for generation; keep tests passing for refactors
- `/tests` and `/doc` handle tests and documentation; agent mode can write, run and fix tests
- Expected values come from requirements, not from what the current code returns
- Never paste real personal data to generate sample data
- Modernize legacy code by explaining it, capturing behaviour in tests, then migrating in small steps
- Exclusion changes can take up to 30 minutes to reach loaded IDEs; reload the window to apply sooner
- The user owns and is responsible for accepted suggestions

## Study Checklist

- [ ] I have generated unit tests with `/tests` and asked Copilot for missing edge cases
- [ ] I can explain why a test that asserts current behaviour can hide a bug
- [ ] I have used Copilot to explain and modernize a piece of legacy code
- [ ] I can troubleshoot "no suggestions" from seat to settings to policy to network
- [ ] I know the 30-minute exclusion delay and how to apply changes sooner
