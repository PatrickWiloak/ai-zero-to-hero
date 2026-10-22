---
last-updated: 2026-10-22
difficulty: advanced
---

# Google Cloud Professional Machine Learning Engineer - Practice Questions

30 questions for the Professional ML Engineer exam, covering problem framing, data and model development on Agent Platform (formerly Vertex AI), pipeline automation, serving, and monitoring. Questions 16-30 are weighted by the six sections of the current exam guide: scaling prototypes (~21%), serving and scaling (~20%), pipelines (~18%), collaborating on data and models (~16%), low-code AI (~13%) and monitoring AI solutions (~13%).

> **Cert page:** [exams/gcp/machine-learning-engineer/](../gcp/machine-learning-engineer/README.md)

---

### Question 1
**Scenario:** A business wants to "use AI to improve retention." What is the first engineering step?

A. Choose a model architecture such as gradient-boosted trees or a deep network, then prototype it on whatever customer data is already available
B. Provision a GPU cluster and managed notebooks so that the data scientists can begin experimenting as soon as the business gives approval
C. Frame it as an ML problem: define the prediction target, the decision it informs, the label source, and the success metric
D. Collect more data from every system the company owns first, since more data always improves a model

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The exam consistently rewards framing before building. A churn model is useless unless someone acts on the score, so the decision and intervention define the label window, the prediction horizon, and the metric. Skipping this produces a technically fine model nobody uses.
</details>

---

### Question 2
**Scenario:** Features must be shared consistently between training and online serving.

A. Agent Platform Feature Store, serving the same feature values offline for training and online for inference
B. A shared spreadsheet documenting each feature's formula, which engineers then reimplement separately in training and serving code
C. Recompute them in each system from the raw data, using whatever library each team knows
D. Cache the computed values in the application's memory and read them back during training runs as well as serving

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A feature store exists to remove training-serving skew by making one definition the source for both paths, and it provides point-in-time correct historical retrieval so training does not accidentally use future values. Recomputing in two systems guarantees eventual divergence.
</details>

---

### Question 3
**Scenario:** Which Agent Platform capability trains a model with no code on tabular data?

A. Model Garden
B. Agent Platform Workbench
C. AutoML
D. Custom training with a container

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AutoML handles feature engineering, architecture search, and tuning for tabular, image, text, and video tasks. Custom training is the escape hatch when you need your own code, and Model Garden is the catalog of pretrained and foundation models.
</details>

---

### Question 4
**Scenario:** A training job needs to run reproducibly with data prep, training, evaluation, and conditional deployment.

A. Agent Platform Pipelines (Kubeflow Pipelines or TFX) with components and a conditional deploy step
B. A shell script on a VM that runs each step in order and is started by a cron entry every night, with logs kept on the disk
C. Cloud Functions chained together by Pub/Sub messages, each function running one step of the workflow
D. A notebook run manually by a data scientist, with results saved in a shared folder

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Pipelines give a versioned DAG with artifact lineage and caching, and the conditional step turns the evaluation into an enforced gate. Notebooks are for exploration; they do not produce the reproducibility or audit trail a production model needs.
</details>

---

### Question 5
**Scenario:** An online prediction endpoint must serve two model versions with traffic split.

A. Two endpoints, each serving one model version, with clients choosing which endpoint to call
B. A load balancer in front of two separate services that each host one of the model versions
C. One endpoint with multiple deployed models and a traffic split percentage
D. Batch prediction jobs that score a sample of requests with the new model version and compare the results

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Agent Platform endpoints support several deployed models with a traffic split, so canary rollout and rollback are configuration changes rather than client changes. Each deployed model has its own machine type and autoscaling settings.
</details>

---

### Question 6
**Scenario:** Predictions are needed for 100 million rows overnight.

A. Batch prediction reading from BigQuery or Cloud Storage and writing results back
B. A Cloud Function per row, invoked in parallel by a Pub/Sub message for each of the 100 million rows
C. Online prediction from a single endpoint, scaled out with a high maximum replica count overnight
D. One request per row sent in a loop from a script running on a single VM

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Batch prediction parallelizes across workers and avoids paying per-request overhead 100 million times. Online endpoints are for latency-sensitive single predictions, and using them for bulk scoring is both slow and disproportionately expensive.
</details>

---

### Question 7
**Scenario:** A deployed model's inputs are drifting from the training distribution.

A. Cloud Monitoring CPU and memory metrics on the endpoint, with an alert whenever utilization stays high for long
B. Model Monitoring on Agent Platform, comparing serving inputs to a training baseline to alert on skew and drift
C. Nothing can be detected until users complain about the quality
D. Manual sampling of predictions by an analyst each quarter, checked against later labels

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Model Monitoring distinguishes training-serving skew (serving data differs from training data) from prediction drift (serving data changes over time), and alerts per feature. Infrastructure metrics show a perfectly healthy endpoint serving increasingly wrong answers.
</details>

---

### Question 8
**Scenario:** A model must explain individual predictions for a regulated decision.

A. Model size, since a smaller model has fewer parameters and is therefore easier to explain to a regulator
B. Agent Platform Explainable AI with feature attributions (integrated gradients, sampled Shapley, or XRAI)
C. The training loss curve, which shows how well the model fit the data it saw during training
D. The confusion matrix, which shows true and false prediction counts for each class

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Explainable AI attributes a specific prediction to input features, which is what an adverse-decision explanation requires. The method depends on the model type: gradient-based for differentiable models, sampled Shapley for non-differentiable ones.
</details>

---

### Question 9
**Scenario:** Training data in BigQuery must be prepared for a TensorFlow model at scale.

A. Export to CSV and load it all into pandas on a large notebook instance, then convert the rows to tensors
B. Process each row one at a time in a Python loop that reads from BigQuery through the client library
C. BigQuery for aggregation, then Dataflow (Apache Beam) or TFX for distributed transformation, writing TFRecords
D. Use a single large VM with as much memory as possible and run the preprocessing script there

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Pushing aggregation into BigQuery and heavy transformation into Dataflow keeps the work distributed, and TFX Transform has the important property that the same transformation graph is applied at serving time, which prevents skew.
</details>

---

### Question 10
**Scenario:** Hyperparameter tuning must be efficient on an expensive training job.

A. Random search over the full space with no stopping, running every trial to the end of training
B. Grid search over every combination of the parameter values, which tests the whole space exhaustively
C. One configuration chosen by the team's most experienced engineer and trained for a long time
D. Agent Platform hyperparameter tuning with Bayesian optimization and early stopping

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Bayesian search conditions each trial on previous results, so it converges in far fewer runs than grid search when each run is expensive. Early stopping of underperforming trials is where the rest of the savings comes from.
</details>

---

### Question 11
**Scenario:** A team wants a foundation model grounded in their own documents on Google Cloud.

A. Fine-tune on the documents so that the model memorizes every fact they contain
B. Paste the documents into every prompt, even past the context window
C. Train a new LLM from scratch on the documents so that it knows the content natively, with no retrieval step
D. Agent Search and grounding, or a RAG pipeline with embeddings and Vector Search for retrieval

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Grounding keeps answers tied to retrievable sources with citations and updates as the documents update. Fine-tuning would encode a snapshot of the knowledge into weights, which is both expensive to refresh and impossible to cite.
</details>

---

### Question 12
**Scenario:** A training job must use preemptible or Spot VMs safely.

A. Checkpoint to Cloud Storage often and resume from the last checkpoint after preemption
B. Never checkpoint, because writing to Cloud Storage slows training more than a restart would cost
C. Use only on-demand VMs, since Spot capacity cannot run training workloads that last longer than an hour
D. Restart from scratch each time, because a checkpoint written before a preemption is always corrupted

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Spot capacity cuts cost substantially, and checkpointing is what converts a preemption from a lost run into a short delay. The checkpoint interval is a trade-off between storage writes and the work you are willing to lose.
</details>

---

### Question 13
**Scenario:** A model must not be trained on personally identifiable information.

A. Trust the data, because the source system's owners already agreed that it contains no personal data at all, in writing
B. Use Cloud DLP to inspect and de-identify (mask, tokenize, or bucket) before training, and document it
C. Encrypt the training job and disks with a customer-managed key
D. Delete the model after training, because a deleted model can no longer reveal anything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Models memorize training data, so PII in the corpus can resurface in outputs and in membership inference attacks. Inspecting and de-identifying before training addresses it at the source, and documenting the transformation is what makes the claim auditable.
</details>

---

### Question 14
**Scenario:** An ML system must retrain automatically when performance drops.

A. Retrain manually when a stakeholder notices that the predictions look worse than they used to, then redeploy
B. Trigger retraining from monitoring signals (drift or degraded metrics) through a pipeline with an evaluation gate
C. Retrain on a fixed schedule regardless of whether the data or the model performance has changed since
D. Never retrain, because a model validated once at launch keeps its accuracy as the incoming data changes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Event-driven retraining responds to the actual condition rather than the calendar, and the evaluation gate is what prevents automatically deploying a model trained on a bad data batch. Fixed schedules are a reasonable fallback when a good trigger signal does not exist.
</details>

---

### Question 15
**Scenario:** Which best describes the responsible AI step before launching a model that affects people?

A. Get legal sign-off only, since the legal team is responsible for every risk that the model creates for people
B. Check overall accuracy only, on a held-out test set that matches the training distribution closely
C. Add a disclaimer to the product page saying that predictions may be wrong and are not guaranteed
D. Evaluate disaggregated performance across affected groups, document intended use and limits, and define a human review path

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Aggregate accuracy hides subgroup failure, so disaggregated evaluation is the measurement that matters. Model cards document intended use and limits, and a human path handles the cases the model gets wrong, which is the part that determines real-world harm.
</details>

### Question 16
**Scenario:** Analysts keep customer data in BigQuery and know SQL but not Python. They need a first churn model within a week.

A. Export the data to CSV and build a custom TensorFlow model on a GPU cluster
B. BigQuery ML, training with SQL where the data lives
C. Build a Kubeflow pipeline with custom containers before training anything
D. Wait until the team has learned Python

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** BigQuery ML trains models with SQL inside BigQuery, which fits the team's skills, avoids moving data and delivers a baseline fast. Custom TensorFlow and a full pipeline are heavier than a first model needs. Waiting delays value for no technical reason.
</details>

### Question 17
**Scenario:** A product team wants a feature that summarises customer reviews. There is no labelled data and the deadline is close.

A. Collect and label 100,000 reviews, then train a summarisation model from scratch
B. Train an AutoML tabular model on review star ratings
C. Fine-tune a model before testing any prompts
D. Prompt a Gemini model from Model Garden, tuning only if needed

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Summarisation is a strength of foundation models, so a prompt-based solution is the low-code first step; tuning comes later if measured quality falls short. Training from scratch is slow and costly. AutoML tabular predicts a column, not a summary. Fine-tuning before trying prompts skips the cheapest option.
</details>

### Question 18
**Scenario:** Five data scientists train variants of a model and keep results in personal notebooks. Nobody can say which settings produced the model now in production.

A. Agent Platform Experiments plus Model Registry versions
B. Ask everyone to email their results to a shared inbox
C. Keep the best model file in a shared folder named "final"
D. Use only one data scientist so there is less to track

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Experiment tracking records parameters and metrics per run, and the Model Registry versions models, so the team can compare work and trace what is deployed. Email and a "final" folder have no lineage or versioning. Reducing the team does not fix the process.
</details>

### Question 19
**Scenario:** A team wants managed Jupyter notebooks with BigQuery and Cloud Storage integration, idle shutdown, and the option to run notebooks on a schedule.

A. Compute Engine VMs with Jupyter installed by hand
B. Cloud Functions
C. Agent Platform Workbench
D. App Engine

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Workbench provides managed notebook instances integrated with Google Cloud data services, with idle shutdown and scheduled execution. Hand-built VMs need the team to manage everything. Cloud Functions and App Engine run application code, not interactive notebooks.
</details>

### Question 20
**Scenario:** A prototype trains in 30 hours on one GPU. The full dataset is ten times larger and results are needed within a day.

A. Keep one GPU and wait ten days
B. Reduce the dataset to the prototype size permanently, since more data rarely changes results
C. Distributed training on Agent Platform Managed Training
D. Switch to a larger CPU-only machine

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Distributing training across multiple accelerators or workers is how a prototype scales to full data within a deadline. Waiting misses the deadline. Throwing away data lowers quality. CPUs are slower than GPUs for this kind of training.
</details>

### Question 21
**Scenario:** A large model built in TensorFlow (or JAX) is dominated by big matrix multiplications and trains with very large batches for weeks.

A. TPUs, which are designed for large matrix workloads at scale
B. A single small CPU VM
C. Cloud Functions running in parallel
D. Preemptible CPU VMs only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** TPUs are Google's accelerators for large-scale training dominated by matrix operations, and they work with TensorFlow and JAX. CPUs and serverless functions are not suited to weeks of heavy training. Preemptible CPUs save money but lack the needed acceleration.
</details>

### Question 22
**Scenario:** A prototype reaches 99% accuracy on training data and 70% on validation data.

A. Train for more epochs to raise validation accuracy
B. Deploy it, since training accuracy is high
C. Remove the validation set and report training accuracy
D. Treat it as overfitting and regularise

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A large gap between training and validation scores is the classic sign of overfitting, and these are the standard remedies. More epochs usually make it worse. Training accuracy does not predict real-world performance. Dropping validation hides the problem.
</details>

### Question 23
**Scenario:** An online endpoint's p99 latency spikes every morning when traffic jumps, because new replicas take minutes to start.

A. Lower the model's accuracy so it serves faster
B. Raise the minimum replica count and tune autoscaling
C. Move all predictions to batch inference
D. Turn off autoscaling and run one large replica, so there is never a cold start to wait for

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Keeping enough warm replicas and scaling on the right signal avoids waiting for cold replicas during the jump. Cutting accuracy is unrelated to start-up time. Batch inference does not serve live requests. One replica guarantees overload at peak.
</details>

### Question 24
**Scenario:** At training time, features are normalised with statistics computed in a Python preprocessing step. At serving time, the app sends raw values and predictions are poor.

A. Package the same preprocessing with the model
B. Ask each client application to reimplement the normalisation in its own language
C. Retrain the model on raw values without telling anyone
D. Add more replicas to the endpoint

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The problem is training-serving skew caused by different preprocessing paths. Shipping one preprocessing implementation with the model removes it. Reimplementing in each client creates more skew. Silent retraining changes the model without fixing the cause. Replicas affect capacity, not correctness.
</details>

### Question 25
**Scenario:** A model must run on handheld devices in warehouses with unreliable network connections.

A. Serve it only from an online endpoint and retry when the network fails
B. Run batch inference once a day and print the results
C. Export an optimised edge format (for example TensorFlow Lite) and run inference on the device
D. Host the model in a Cloud Function

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** On-device inference works without connectivity, and edge formats are optimised for small hardware. Online endpoints and Cloud Functions need the network the devices often lack. Daily batch output cannot react to what happens on the floor.
</details>

### Question 26
**Scenario:** A pipeline reruns an expensive data preparation step every time, even when its inputs and code have not changed.

A. Remove the data preparation step from the pipeline
B. Run the pipeline less often
C. Use a bigger machine for the step
D. Enable execution caching

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** With caching, a step whose inputs and definition are unchanged reuses its previous outputs, saving time and money. Removing the step breaks the pipeline. Running less often delays models. A bigger machine still repeats wasted work.
</details>

### Question 27
**Scenario:** A team wants every merge to main to test pipeline code, compile the pipeline and run it, with a new model promoted only if it beats the current one on evaluation.

A. Have a data scientist run the notebook manually after each merge
B. CI/CD (for example Cloud Build) with an evaluation gate
C. Deploy every newly trained model straight to production
D. Run the pipeline once and never change it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CI/CD automates testing and running the pipeline on code changes, and a conditional step compares the candidate with the current model before promotion. Manual runs are not repeatable. Deploying every model removes the quality gate. A frozen pipeline cannot improve.
</details>

### Question 28
**Scenario:** An auditor asks which dataset version and pipeline run produced the model currently deployed.

A. Pipelines and ML Metadata lineage
B. Search team chat history for the deployment date
C. Ask the person who deployed it
D. Retrain the model and assume the result matches

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Pipelines record metadata linking datasets, runs and resulting models, which answers lineage questions reliably. Chat history and memory are incomplete. Retraining produces a different model and proves nothing about the deployed one.
</details>

### Question 29
**Scenario:** Monitoring should alert when the distribution of features arriving at a production endpoint differs from the distribution in the training data.

A. Prediction drift detection, which compares recent serving data with earlier serving data
B. CPU utilisation alerts on the endpoint
C. Training-serving skew detection, which compares serving data with the training baseline
D. Cloud Logging of HTTP status codes

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Skew is the gap between training data and serving data, so a training baseline is the comparison point. Drift compares serving data over time; it is related but answers a different question. CPU and HTTP status tell you about the infrastructure, not data distributions.
</details>

### Question 30
**Scenario:** Before launch, a team must check a Gemini-based summariser for groundedness, fluency and safety on a set of test inputs, and repeat the check after each prompt change.

A. Ask the developers to read ten outputs and approve them
B. Compare outputs with exact string matching against reference summaries
C. Track only the endpoint's latency
D. The Gen AI evaluation service on a fixed dataset

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The evaluation service scores generative output against criteria such as groundedness, fluency and safety, and a fixed dataset makes results comparable between versions. Ten manual reads do not repeat reliably. Exact match fails for free-form summaries. Latency says nothing about quality.
</details>

---

## Where to go deeper

- [Professional ML Engineer cert page](../gcp/machine-learning-engineer/README.md) - notes, practice plan, strategy
- [GCP Data Engineer practice questions](https://data.noblerworks.com/resources/practice-questions/gcp-data-engineer/) - the data platform beneath this
- [DP-100 practice questions](azure-data-scientist-dp-100.md) - the Azure counterpart
- [AI/ML systems topic index](../../build/README.md) - MLOps across the repo
- **[📖 Google Cloud certification](https://cloud.google.com/learn/certification)** - official exam guides
