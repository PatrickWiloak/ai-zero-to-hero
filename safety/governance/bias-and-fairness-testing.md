# Bias and Fairness Testing in Practice

**In one line:** Test an AI system for unequal outcomes the way you test for bugs: define who could be harmed, build test sets across groups, measure outcomes and error rates by group, decide an acceptable gap in writing, and re-test after every change.
**Last reviewed:** 2026-11-07

---

> Judgment guide, not legal advice. What counts as unlawful discrimination depends on the law and the setting.

## The short version

- Bias is not only a data problem. NIST notes that biases "remain endemic across technology processes and can lead to harmful impacts regardless of intent" (NIST SP 1270 abstract, read 2026-11-07). Intent is not a defence in practice; measure outcomes.
- Fairness has no single definition. You must **choose** what to measure (for example, selection rates, error rates, or calibration by group) and be able to justify the choice for your use case.
- You usually cannot fix what you cannot measure. That means sometimes needing group data to test, collected and handled lawfully. See [privacy and data protection](privacy-and-data-protection-with-ai.md).
- Regulators already expect it for consequential decisions. The EEOC said in 2021 that AI tools in employment decisions may perpetuate bias and that anti-discrimination laws still apply (read 2026-11-07). Colorado's AI act requires developers and deployers of high-risk systems to use reasonable care against algorithmic discrimination (see [US state AI laws](us-state-ai-laws.md)).
- Test generative systems too: chat answers, summaries, and image output can differ in quality or tone by name, dialect, gender or language.

## The method

1. **Scope the harm.** Who is affected, what decision or output matters, what is the worst realistic outcome.
2. **Pick groups** that matter for the use and the law (for example protected classes in hiring, language or dialect in support).
3. **Build a test set.** Real data where lawful, plus synthetic paired examples that differ only in a group signal (a name, a pronoun, a dialect).
4. **Choose metrics**:

| Metric | Question it answers |
|---|---|
| Selection or approval rate by group | Does one group get favourable outcomes more often? |
| False positive / false negative rate by group | Are mistakes spread unevenly? |
| Score or quality gap on paired prompts | Does the output change when only the group signal changes? |
| Refusal or toxicity rate by group | Does the system treat some groups' requests differently? |

5. **Set thresholds in advance.** In US employment practice, a common screening heuristic compares group selection rates (the "four-fifths" or 80 percent rule). The regulation page for it could not be fetched, so confirm the rule with counsel before using it. A heuristic is a flag to investigate, not a pass or fail.
6. **Investigate gaps**: data coverage, labels, features that act as proxies (such as postcode), prompt wording, thresholds.
7. **Mitigate and re-test**: rebalance data, change features, adjust thresholds, add human review, or decide not to automate.
8. **Document and monitor.** Keep results, decisions and owners. Re-test on every model, prompt or data change, and on a schedule.

## A worked example (paired prompts)

You run a resume-summary tool. Take 100 resumes, create two copies of each that differ only in the candidate's first name (chosen to signal different backgrounds), run both, and compare: summary length, strength of language, and recommended-to-interview rate. If the rate differs materially, you have a flag to investigate before launch. Use an LLM or human rater with a fixed rubric, and have people spot-check.

## Common mistakes

- Testing only overall accuracy. A 95% average can hide a 70% group.
- "Removing" the sensitive column and calling it done; proxies remain.
- One audit at launch, never repeated.
- Treating a vendor's fairness claim as your evidence.
- Measuring only the model, not the whole process with humans in it.

## Next steps

- [AI risk assessment](ai-risk-assessment.md)
- [Evals for LLMs](../../learn/concepts/evals-for-llms.md) and [set up an eval harness](../../build/projects/set-up-eval-harness.md)
- [AI for HR](../../work/playbooks/for-hr.md)

## Sources

- NIST, Towards a Standard for Identifying and Managing Bias in AI (SP 1270): https://www.nist.gov/publications/towards-standard-identifying-and-managing-bias-artificial-intelligence (fetched 2026-11-07; abstract only, the page did not give the bias categories)
- EEOC, AI and Algorithmic Fairness initiative: https://www.eeoc.gov/newsroom/eeoc-launches-initiative-artificial-intelligence-and-algorithmic-fairness (fetched 2026-11-07)
- Colorado SB24-205: https://leg.colorado.gov/bills/sb24-205 (fetched 2026-11-07)
