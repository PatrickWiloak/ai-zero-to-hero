# Databricks ML Associate - Exam Strategy

**Last reviewed:** 2026-11-07

## What the exam rewards

The exam has 48 scored questions in 90 minutes, which is about 1 minute 52 seconds each, with some extra time already built in for unscored items. Sections 1 and 3 hold 69 percent of the weight. Section 1 questions are mostly about *which Databricks feature or API call* does a job; Section 3 questions are mostly *judgment*: which metric, how many models, what the error pattern means.

## Tactics

1. **Prefer the current recommended path.** Aliases rather than stages in Unity Catalog, `FeatureEngineeringClient.create_table` rather than SQL tricks, the Unity Catalog registry rather than the workspace registry. When one answer uses a deprecated route, it is the distractor.
2. **Do the arithmetic.** For model counts, multiply grid combinations by folds and stop. For the 5-fold, 3 x 2 x 3 grid, 18 x 5 = 90.
3. **Translate scenarios into a cost of error.** "Missing a fraud case" points to recall; "too many false alarms" to precision; "imbalanced, both matter" to F1 or AUC; "probabilities must be calibrated" to log loss.
4. **Read the latency requirement.** Nightly means batch, per request means real time, continuous events means streaming.
5. **Multiple-selection questions** say how many to pick. Eliminate the clearly wrong ones first, then check each remaining option on its own.
6. **Do not over-read distractors that sound smart.** In the guide's sample questions, the wrong options are plausible-sounding inventions (an `AS FEATURE STORE` SQL clause, a SimpleImputer that auto-selects). If you cannot recall the feature existing, treat it with suspicion.
7. **Flag and move.** Mark a question you are unsure of and come back; do not spend four minutes on a 12 percent topic.

## Known traps from the exam guide's own samples

- A model trained on a log target must be exponentiated before RMSE is computed in original units.
- A tag is descriptive; only an alias changes which version production reads.
- Cost-sensitive learning, not feature scaling or a simpler model, answers class imbalance.
- Sorting runs in the MLflow UI is not the Client API: "using the Client API" means `search_runs` in code.

## Logistics reminders

Online proctored or test center, no test aids, two-year validity, USD 200 plus taxes at last check (2026-11-07). The pass mark is not published, so there is no safe score to aim for below "as high as you can".
