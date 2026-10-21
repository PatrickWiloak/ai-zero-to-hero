---
last-updated: 2026-08-09
difficulty: intermediate
---

# Databricks Certified Machine Learning Associate - Practice Questions

15 questions for the ML Associate exam, weighted toward ML workloads on Databricks (29%) and the ML workflow (29%), then Spark ML (17%), deep learning (13%), and scaling (12%).

> **Cert page:** [exams/databricks/ml-associate/](../databricks/ml-associate/README.md)

---

### Question 1
**Scenario:** An experiment's parameters, metrics, and model artifact must be recorded automatically.

A. Print statements in the notebook that write each parameter and metric to the cell output after every run
B. MLflow autologging, or `mlflow.log_param` and `log_metric` calls within a run
C. A shared spreadsheet where each person pastes the parameters and scores after training finishes
D. Manual notes in the notebook markdown, listing the settings used and the final score of each attempt

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Autologging captures parameters, metrics, and the model for supported libraries with one line, which means tracking happens by default rather than when someone remembers. Runs are then comparable in the experiment UI without any bookkeeping discipline.
</details>

---

### Question 2
**Scenario:** A model must be promoted from development to production with a clear lifecycle.

A. Rename the model artifact with a version suffix such as `_prod` and point the application at that file name
B. Email the pickle file to the deployment team, who unpack it on the production cluster, test it there, and then replace the previous pickle file by hand
C. Register the model in Unity Catalog with model versions and aliases such as `champion`, and grant access through the catalog
D. Copy the model file from the development workspace folder into the production workspace folder

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The registry keeps lineage back to the producing run and makes promotion an explicit, auditable action. Aliases replaced the older named stages, so applications reference `@champion` and a promotion is an alias move rather than a redeployment.
</details>

---

### Question 3
**Scenario:** Hyperparameters must be tuned in parallel across a cluster.

A. Ray Tune, recommended over Hyperopt
B. Manual tuning, changing one setting at a time and re-running the notebook until the metric stops improving
C. A sequential loop over a parameter grid on the driver, which logs each result to MLflow in turn
D. One configuration chosen from the library defaults, which are tuned for the typical dataset by the maintainers

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Ray Tune runs trials in parallel across the cluster workers and supports smarter search than a grid. Open-source Hyperopt is no longer maintained and is not included in Databricks Runtime ML after 16.4 LTS, so its SparkTrials is no longer the recommended path. Results can still be logged to MLflow.

**Key Concept:** [Hyperparameter tuning on Databricks](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/hyperopt-concepts)
</details>

---

### Question 4
**Scenario:** Features used in training must match those used at inference.

A. Write the transformations twice, once in the training notebook and once in the serving code, and keep them aligned by review
B. Databricks Feature Store (Feature Engineering in Unity Catalog), serving the same definitions offline and online
C. A shared spreadsheet that lists each feature formula so that the training and serving teams can follow it
D. Copy the training code into the serving application and update the copy whenever the original changes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The feature store removes training-serving skew by making one definition authoritative, and it supports point-in-time joins so training does not accidentally use values that were not available at prediction time. Copied code diverges as soon as someone fixes a bug in one place.
</details>

---

### Question 5
**Scenario:** A scikit-learn model must be trained on data too large for one machine.

A. Use Spark ML for distributed training, or distribute single-node training across the cluster with `applyInPandas` for per-group models
B. It cannot be done, because scikit-learn trains only on data that fits in the memory of a single machine
C. Buy a bigger driver node with more memory until the full dataset fits, then train on it as normal
D. Sample the data down to what fits in memory and accept the loss of accuracy that comes from the sample

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Spark ML implements distributed versions of common algorithms. The per-group pattern is the other common case: thousands of small models, one per store or customer segment, each fitting comfortably on one worker and trained in parallel.
</details>

---

### Question 6
**Scenario:** A Spark ML pipeline includes indexing, assembling, and a classifier.

A. SQL only, with each transformation written as a view and the classifier called through a SQL function in each query
B. Separate notebooks for each stage, run in order by a job, with the intermediate data saved to files between them and re-read by the next notebook
C. Run each step manually in a notebook cell and keep the fitted objects in variables for later use
D. A `Pipeline` of stages, fit once, producing a `PipelineModel` with the same transformations at inference

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Wrapping the transformations and the estimator into one pipeline means the fitted preprocessing travels with the model, so serving cannot accidentally apply different encoding. This is the Spark ML answer to training-serving skew.
</details>

---

### Question 7
**Scenario:** A classification model on imbalanced data reports 98% accuracy.

A. Add features until the accuracy climbs past 98%, since more signal always helps the model on skewed labels
B. Ship it, because 98% accuracy is well over the usual bar for production classification models and further tuning is not worth the delay
C. Evaluate with precision, recall, F1, and PR-AUC, and consider class weights or resampling
D. Increase the training epochs so the model sees the rare class more often and its accuracy rises further

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** With 2% positives, predicting the majority class always scores 98%. Precision and recall on the minority class expose that immediately, and resampling should be applied only to the training split so the evaluation stays honest.
</details>

---

### Question 8
**Scenario:** A deep learning model must train on multiple GPUs.

A. CPU training with a larger instance type and more cores, which avoids the need to coordinate between devices
B. A single GPU only, with a smaller batch size so the model fits
C. Distributed training with TorchDistributor (or Ray on Databricks), scaling from one node to several
D. Reduce the model size by pruning layers until it trains on one device

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** TorchDistributor runs PyTorch distributed training on a Databricks cluster, handling process launch and coordination. Start single-node multi-GPU and move to multi-node only when the model or data genuinely requires it, since inter-node communication adds real cost.
</details>

---

### Question 9
**Scenario:** A model must serve real-time predictions with autoscaling.

A. A notebook on an always-on cluster, called from the app through a REST request
B. A cron script on a virtual machine that loads the model and reads requests
C. A batch job that scores pending requests every few minutes
D. Mosaic AI Model Serving with a registered model version, scaling on request volume and latency

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Model Serving provides an HTTPS endpoint with authentication, autoscaling, and optional scale-to-zero, backed by a registered model version. Batch scoring remains the right answer for high-volume offline work where latency does not matter.
</details>

---

### Question 10
**Scenario:** Data leakage is suspected because validation performance is suspiciously high.

A. Accept the result, since a high validation score is expected from a tuned model
B. Use a smaller model, since fewer parameters cannot memorize leaked rows
C. Increase regularization until the validation score drops to a believable level, then keep that setting and treat the problem as solved
D. Check for target leakage: features built after the label, or preprocessing fitted before the split

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Fitting a scaler or an encoder on the full dataset before splitting leaks distributional information into validation. The other classic is a feature that only exists because the outcome already happened. Both produce excellent offline numbers and a useless production model.
</details>

---

### Question 11
**Scenario:** Model training must be reproducible months later.

A. Save only the metrics, since the final scores are what the team compares and the settings are recorded in them
B. Log the model with signature and environment, pin the runtime version, and version the input data
C. Remember the settings, and write them in the wiki at handover
D. Save the notebook, which holds the code and parameters, and rely on the latest data in the source table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Code, data, and environment all have to be pinned. Delta time travel supplies the data version, MLflow captures the conda or pip environment and model signature, and the runtime version pins the libraries the notebook assumed.
</details>

---

### Question 12
**Scenario:** A batch scoring job must run nightly on new data.

A. Manual runs by an engineer each evening, started from the notebook once the new data has landed in the table
B. A notebook someone opens each night and runs, with the results written to a table by hand
C. A scheduled Databricks job loading the registered model and writing predictions to a Delta table
D. Real-time serving for all rows, sending each record to the endpoint in a loop from a scheduled job each night

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Batch scoring through `mlflow.pyfunc.spark_udf` parallelizes across the cluster and writes results transactionally. Pushing millions of rows through a real-time endpoint pays per-request overhead for every record.
</details>

---

### Question 13
**Scenario:** Two models must be compared on the same evaluation data.

A. Run them at different times, on whatever data is current at each run, and compare the final numbers they report
B. Log each model as an MLflow run in one experiment with the same metrics, and compare them in the run UI
C. Compare the file sizes of the two saved models, since the larger one holds more learned detail and so must perform better on the data
D. Ask the team which model they prefer, based on the notebooks and what each author remembers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Comparison requires the same metric names on the same data, which is exactly what an experiment groups. Logging the evaluation dataset version alongside the metrics is what makes the comparison defensible later.
</details>

---

### Question 14
**Scenario:** AutoML is used on a tabular dataset.

A. It produces baseline models plus generated notebooks showing the code, which serve as a starting point for refinement
B. It only reports metrics for the best model it found and keeps the code and the feature handling hidden
C. It cannot be inspected, because the trained pipelines are stored in a format that only AutoML can read
D. It replaces the data scientist, since the best model is selected and deployed with no human review

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The generated notebook is the distinguishing feature: nothing is hidden, so you can see the preprocessing and modeling choices and take over from there. What AutoML cannot do is tell you the label is wrong or the problem is badly framed.
</details>

---

### Question 15
**Scenario:** A cluster for ML work must have the right libraries.

A. The Databricks Runtime for Machine Learning, with common ML libraries and GPU support
B. Build the cluster image from scratch, installing every library and driver by hand with an init script
C. Install packages in every notebook with `%pip`, so that each notebook carries its own library versions
D. The standard runtime, which has Spark and Delta Lake but ships without the common ML libraries

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The ML runtime ships with tested versions of scikit-learn, PyTorch, TensorFlow, XGBoost, MLflow, and CUDA where applicable. Installing ad hoc on the standard runtime produces version conflicts and cluster start times that grow with every added package.
</details>

---

## Where to go deeper

- [ML Associate cert page](../databricks/ml-associate/README.md) - notes, practice plan, strategy
- [ML Professional practice questions](databricks-ml-professional.md) - the next level up
- [Data Engineer Associate practice questions](https://data.noblerworks.com/resources/practice-questions/databricks-data-engineer-associate/) - the data platform beneath
- [AI/ML systems topic index](../../build/README.md) - MLOps across the repo
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides
