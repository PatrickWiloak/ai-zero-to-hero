# Applied AI Take-Home Exercises

**In one line:** Treat a take-home as a small product: state the problem and assumptions, build the simplest thing that works, evaluate it on a test set you made, show where it fails, and write a short, honest README, because reviewers grade judgment more than polish.
**Last reviewed:** 2026-11-07

---

## The short version

- This page is a **judgment guide from common practice**, not a survey of what companies ask. Ask the recruiter for the time limit, allowed tools and grading criteria.
- Respect the time box. If they say 3 hours, do not submit 12 hours of work; say what you would do next.
- The usual hidden rubric: Did you understand the problem? Did you measure quality? Did you handle failure? Can you explain trade-offs? Is it readable?
- Using an AI assistant: follow the stated rules. If allowed, say so and show you checked the output. If not stated, ask.
- Never put the company's confidential data or your keys in a public repo.

## Typical exercise types

| Type | Example | What they look for |
|---|---|---|
| Prompt and eval | Write prompts to classify support tickets; show accuracy | A labelled test set, error analysis, prompt iteration with evidence |
| RAG | Answer questions over supplied documents | Chunking choices, retrieval check, citations, "I don't know" behaviour |
| Extraction | Pull fields from messy documents into JSON | Schema, validation, failure handling |
| Agent / tool use | Build a small agent with two tools | Loop limits, tool errors, logging, safety |
| Classic ML | Predict churn from a CSV | Leakage awareness, baseline, proper split |
| Review / debug | Find why a pipeline's answers are wrong | Systematic diagnosis, not guesses |
| Written | Design memo for an AI feature | Risks, cost, rollout |

## A 6-step approach

1. **Read twice, list assumptions.** Write 3 to 5 assumptions and any question you would ask. If you may email the company, ask one or two sharp questions.
2. **Baseline first.** A rule, a simple prompt or a keyword search. You need something to beat.
3. **Build the smallest end-to-end version** before improving any part.
4. **Make a test set.** Even 20 to 30 hand-labelled examples let you compare changes. Note that it is small and what that means for confidence. See [set up an eval harness](../../build/projects/set-up-eval-harness.md) and [evals for LLMs](../../learn/concepts/evals-for-llms.md).
5. **Analyse failures.** Show 5 real errors, why they happened, and what you tried.
6. **Write the README** (below), then re-run everything from a clean checkout.

## README outline

- Problem and your assumptions
- How to run it (exact commands, versions, where to put keys)
- Approach and why you chose it over alternatives
- Results: the numbers, how you measured, test set size, a table of baseline vs final
- Failure cases and limits
- Cost and latency estimate per request (say how you estimated it)
- What you would do with another day
- Use of AI tools, if any

## Worked mini-example

Task: "Classify these 200 tickets into 6 categories." A strong submission: hand-label 40, keyword baseline (say it scores X), an LLM prompt with a fixed output schema, accuracy per category, confusion between two categories explained, a rule to send low-confidence tickets to a human, and a note that 40 examples gives only a rough estimate. A weak one: one prompt, "works well" with no numbers.

## Common mistakes

- No evaluation, just a demo.
- Over-engineering (a vector database for 10 documents).
- Hidden secrets or a broken run command.
- Claiming accuracy without saying how it was measured.
- Ignoring safety and cost for a feature that touches users.
- Not saying where you used an AI assistant when the rules ask.

## Next steps

- [AI engineer interview](ai-engineer-interview.md) and [AI system design interview](ai-system-design-interview.md)
- [Build a RAG pipeline](../../build/projects/build-rag-pipeline.md) and [structured extraction pipeline](../../build/projects/structured-extraction-pipeline.md)
- [Build an AI portfolio](../roles/build-an-ai-portfolio.md)

## Sources

- No external sources: this is a judgment page based on common practice.
