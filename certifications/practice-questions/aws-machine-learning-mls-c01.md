---
last-updated: 2026-08-09
difficulty: advanced
---

# AWS Certified Machine Learning - Specialty (MLS-C01) - Practice Questions

15 questions for MLS-C01 prep, weighted toward modeling (36%), exploratory data analysis (24%), then data engineering and ML implementation and operations (20% each).

MLS-C01 has been superseded for many candidates by the Machine Learning Engineer Associate (MLA-C01). Check which exam is current before booking.

> **Cert page:** [exams/aws/specialty/machine-learning-mls-c01/](../aws/specialty/machine-learning-mls-c01/README.md)

---

### Question 1
**Scenario:** A binary classifier must catch as many fraudulent transactions as possible, accepting some false alarms.

A. Optimize training speed, since fraud models must be retrained often on fresh transactions
B. Optimize precision, so that nearly every flagged transaction turns out to be real fraud
C. Optimize accuracy, which counts every correct prediction and so reflects fraud detection well
D. Optimize recall, and tune the decision threshold accordingly

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Recall is the fraction of actual fraud you catch, which is what "miss as few as possible" means. Precision is the cost you are choosing to pay in false positives. Accuracy is meaningless at 0.1% fraud, where predicting "not fraud" always scores 99.9%.
</details>

---

### Question 2
**Scenario:** Training accuracy is 99% and validation accuracy is 70%.

A. Underfitting; use a larger model with more layers so it can fit the validation set better
B. Overfitting; add regularization, dropout, more data, or early stopping
C. The learning rate is too low, so training has not converged
D. The data is corrupt, since the validation labels must have been shuffled during upload

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A large train-validation gap is the definition of overfitting: the model memorized the training set. Regularization, more data, simpler models, and early stopping all attack it. Underfitting shows as poor performance on both sets.
</details>

---

### Question 3
**Scenario:** A categorical feature has 10,000 distinct values.

A. One-hot encode it into 10,000 binary columns, which keeps every category separate and works for every model
B. Drop it, since a feature with that many values cannot carry useful signal for any model
C. Use target encoding, hashing, or a learned embedding, depending on the model and how it is trained
D. Label encode it for a linear model, treating each integer as a magnitude

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** One-hot at that cardinality creates a huge sparse matrix. Hashing bounds the dimension, target encoding compresses to a statistic (with care to avoid leakage, using out-of-fold encoding), and embeddings learn a dense representation. Label encoding imposes a false ordinal relationship on a linear model.
</details>

---

### Question 4
**Scenario:** SageMaker must serve a model with variable, spiky traffic and scale to zero between bursts.

A. An EC2 instance running the model container behind a load balancer sized for the peak
B. Serverless Inference, which scales with traffic and down to zero
C. A real-time endpoint with a fixed instance count
D. Batch Transform, started on a schedule to process the requests that accumulated since the last run

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Serverless Inference scales with traffic and to zero, at the cost of cold starts. Real-time endpoints give consistent latency but bill continuously. Asynchronous Inference is the third option, suited to large payloads and long processing where a queue is acceptable.
</details>

---

### Question 5
**Scenario:** Two model versions must be compared on live traffic without risking full exposure.

A. Deploy the versions behind one endpoint as production variants with weighted traffic, or use a shadow variant
B. Two separate endpoints, with manual switching of the client's URL between them during the test
C. Offline evaluation only, using a held-out test set, since live traffic cannot be sampled safely
D. Deploy the new one fully, then roll back if the error rate rises over the old model's baseline

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Production variants split traffic by weight behind a single endpoint, so rollback is a weight change. Shadow testing sends a copy of traffic to the new variant without returning its responses, which measures behavior with zero user risk.
</details>

---

### Question 6
**Scenario:** A dataset is highly imbalanced at 100:1.

A. Combine resampling (SMOTE or undersampling), class weights, and precision-recall evaluation rather than accuracy
B. Do nothing, since a sufficiently large dataset lets the model learn the minority class unaided
C. Use a bigger model, because more capacity lets it fit the rare class without any other change
D. Collect more of the majority class, which rebalances the ratio once the data volume doubles

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Imbalance affects both training and evaluation, so it needs handling in both places. Apply resampling only to the training split, never to validation or test, or your measured performance will be optimistic and wrong.
</details>

---

### Question 7
**Scenario:** Hyperparameter tuning must find good values efficiently on an expensive training job.

A. Random guessing of values within the documented ranges, repeated until the metric looks fine
B. Manual tuning by an engineer, who edits the hyperparameters after reading each job's logs
C. Grid search over every combination of values, which is exhaustive and so finds the best result quickly and cheaply
D. SageMaker automatic model tuning with Bayesian search, early stopping, and a limit on parallel jobs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Bayesian optimization uses the results of previous trials to choose the next configuration, which finds good values in far fewer runs than grid search on an expensive objective. Early stopping kills unpromising trials, which is where the remaining savings come from.
</details>

---

### Question 8
**Scenario:** Feature values computed at training time differ from those computed at inference time.

A. Training-serving skew: use a feature store or shared transformation code so each path computes features identically
B. Increase model size so it can learn to compensate for the differences in feature values
C. Retrain more often on fresher data, since every new training run will bring the two feature computations back into line and fix the gap
D. Ignore it, because small differences in feature values average out over many predictions and rarely move the results by much

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Skew produces a model that performs well offline and badly in production, and it is one of the most common causes of that gap. SageMaker Feature Store, or at minimum a single shared transformation library, removes the possibility of the two paths diverging.
</details>

---

### Question 9
**Scenario:** Which SageMaker capability detects data drift on a deployed endpoint?

A. CloudWatch alarms on CPU and memory utilization, which rise whenever the input data distribution shifts
B. Clarify only, run once at deployment time to compare the live feature statistics with the training set
C. Batch Transform jobs that re-score the endpoint's recent traffic and report any change in the predictions
D. Model Monitor with a baseline from the training data

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Model Monitor captures endpoint traffic, compares statistics against a baseline, and reports violations for data quality, model quality, bias drift, and feature attribution drift. Clarify computes bias and explainability, and its outputs feed two of those monitor types.
</details>

---

### Question 10
**Scenario:** A time series must be split for validation.

A. Chronological split, training on earlier data and validating on later data, or rolling-origin cross-validation
B. Random shuffle split, so both sets contain examples from every period of the series
C. Stratified split on the target, so that each set keeps the same share of high and low values
D. K-fold with shuffling, repeated five times so every record is used for validation once

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Random splitting on time series lets the model see the future, which produces excellent validation scores and a useless model. Chronological splitting and rolling-origin cross-validation preserve the causal order, and lag features must be computed with the same care.
</details>

---

### Question 11
**Scenario:** Large training data lives in S3 and the job spends most of its time downloading.

A. Use a bigger instance with more vCPUs, since download time scales down with compute
B. Compress with gzip only, then keep File mode so that the job still copies every object at the start
C. Use Pipe or FastFile mode to stream from S3, or FSx for Lustre for repeated access to the data
D. Reduce the dataset by dropping older partitions, accepting a smaller training set

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** File mode copies the whole dataset before training starts, which dominates the wall clock for large data. Streaming modes overlap download with compute, and FSx for Lustre is the right answer when many jobs repeatedly read the same dataset.
</details>

---

### Question 12
**Scenario:** A model must explain individual predictions to satisfy a regulator.

A. SageMaker Clarify with SHAP values for feature attribution
B. Model size, reported as the parameter count, which shows regulators how complex each decision was
C. The confusion matrix on the test set, which lists the true and false predictions for each applicant
D. Training loss curves, which show the reasons behind each prediction over the training epochs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SHAP attributes a prediction to its input features in a locally accurate way, which is what "why did this application get declined" requires. Aggregate performance metrics describe the model overall and say nothing about an individual decision.
</details>

---

### Question 13
**Scenario:** Which algorithm suits anomaly detection on streaming numeric data?

A. Linear Learner, a supervised algorithm for regression and classification
B. Random Cut Forest, an unsupervised anomaly detector
C. Seq2Seq, a sequence-to-sequence model for translation and text summarization
D. XGBoost, a gradient boosted tree algorithm that needs labeled examples

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Random Cut Forest is the built-in unsupervised anomaly detection algorithm and is available both in SageMaker and in Kinesis Data Analytics for streaming. The supervised algorithms need labeled anomalies, which is precisely what you usually lack.
</details>

---

### Question 14
**Scenario:** Training must use spot capacity without losing progress on interruption.

A. Restart from scratch on interruption, accepting that a long job may never finish
B. On-demand only, at a higher price
C. Managed spot training with checkpointing to S3
D. Reserved instances, which guarantee capacity for a one-year term and so need no checkpoints

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Managed spot training can cut costs substantially, and checkpointing is what makes interruption survivable: the job resumes from the last checkpoint rather than the beginning. Without checkpoints, a long job on spot is a gamble that gets worse the longer it runs.
</details>

---

### Question 15
**Scenario:** An ML pipeline must run data prep, training, evaluation, and conditional registration.

A. A shell script run by cron that calls each stage in order and emails the log to the team
B. SageMaker Pipelines with steps and a condition step that gates model registration on the metric
C. A single notebook with all four stages in separate cells, re-run by hand after every data update by whoever is on call
D. Manual steps in a runbook, with a reviewer approving each stage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Pipelines gives a versioned DAG with lineage tracking and caching, and the condition step is what turns "we evaluated it" into an enforced quality gate. Notebooks are for exploration; they do not give reproducibility or auditability.
</details>

---

## Where to go deeper

- [MLS-C01 cert page](../aws/specialty/machine-learning-mls-c01/README.md) - notes, practice plan, strategy
- [ML Engineer Associate practice questions](aws-ml-engineer-associate.md) - the current-generation exam
- [DP-100 practice questions](azure-data-scientist-dp-100.md) - the Azure counterpart
- [AI/ML systems topic index](../../build/README.md) - MLOps across the repo
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides
