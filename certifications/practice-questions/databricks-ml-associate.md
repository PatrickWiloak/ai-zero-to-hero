---
last-updated: 2026-11-07
difficulty: intermediate
---

# Databricks Certified Machine Learning Associate - Practice Questions

30 original questions on the four sections of the current exam guide, in the guide's weights: Databricks Machine Learning (38%, 11 questions), Data Processing (19%, 6), Model Development (31%, 9) and Model Deployment (12%, 4). They are written for this guide and are not Databricks exam questions. Each answer explains why the other options are wrong.

> **Cert page:** [exams/databricks/ml-associate/](../databricks/ml-associate/README.md)

---

### Question 1
**Section 1. Scenario:** A team's inference job must start using a newly validated model version without anyone editing the job's code.

A. Hard-code the new version number in the job configuration and redeploy the job each time a version is approved, so every promotion is a reviewed change
B. Delete the old model version so the new one is the only one that remains
C. Load the model by alias (for example models:/main.ml.churn@champion) and move the alias to the new version
D. Set a tag named production on the new version and have the job search for it by hand

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An alias is a mutable named reference to one version, so jobs that load the alias pick up the new version automatically and rollback is just pointing the alias back. Hard-coding versions needs an edit each time, deletion destroys the rollback path, and tags are descriptive only.
</details>

---

### Question 2
**Section 1. Scenario:** A workspace has Unity Catalog enabled, and a team asks why they should register models there instead of in the workspace model registry.

A. The workspace registry cannot store more than one version of a model
B. Unity Catalog adds centralized access control, auditing, lineage and model discovery across workspaces
C. Unity Catalog registers models without needing a signature or any logging
D. The workspace registry is the only one that supports aliases, so teams that want to promote versions by pointing a name at them must stay in it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Databricks docs describe these governance benefits for models in Unity Catalog, and the workspace registry is the legacy option. Unity Catalog models do require a signature, and aliases are the Unity Catalog promotion mechanism.
</details>

---

### Question 3
**Section 1. Scenario:** A data scientist ran 40 MLflow runs in one experiment, each logging an f1 metric, and needs the run with the highest f1 in code.

A. Sort the runs table in the MLflow UI and copy the run id by hand
B. Take the run with the latest start time, since later runs are usually better
C. Call get_experiment, which returns the best run directly
D. Call search_runs on the experiment with order_by=["metrics.f1 DESC"] and take the first result

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** search_runs supports server-side ordering on a metric, so one call returns the best run. The UI is not the client API, the latest run is not necessarily the best, and get_experiment returns experiment metadata, not a ranked run.
</details>

---

### Question 4
**Section 1. Scenario:** Which statement best describes the main advantage of a Databricks Runtime for Machine Learning over building a cluster environment by hand?

A. It ships with ML and deep learning libraries pre-installed
B. It removes the need to choose evaluation metrics because it picks and applies the best metric for the task automatically
C. It guarantees every model trained on it will be accurate
D. It trains models without any cluster compute

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The ML runtime automates the creation of compute with pre-built ML and deep learning tooling. It does not choose metrics, guarantee accuracy or remove compute.
</details>

---

### Question 5
**Section 1. Scenario:** A team wants a fast baseline and a view into how it was built so the data scientists can keep improving it.

A. Run AutoML and treat the leaderboard as final because the code is hidden
B. Run AutoML, then open and edit the generated notebook of the best trial
C. Skip baselines and write a deep network first
D. Export the data to a spreadsheet and fit a trend line

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AutoML trains and tunes several algorithms and generates source code notebooks for the trials, which can be reviewed and modified. It is a glass box, not a hidden result.
</details>

---

### Question 6
**Section 1. Scenario:** A data scientist is creating a feature table in a Unity Catalog workspace. Which is the correct creation path?

A. Run CREATE FEATURE TABLE in SQL with a primary key constraint, which is the only supported way to create a feature table in Unity Catalog
B. Create any Delta table without a primary key and call it a feature table
C. Call create_table on FeatureEngineeringClient with a name, primary keys and a schema or DataFrame, then write data with write_table
D. Save a CSV in the workspace files and register it with register_table

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Feature tables are Delta tables with a primary key created through the FeatureEngineeringClient. There is no CREATE FEATURE TABLE statement, and a table without a primary key is not a valid feature table.
</details>

---

### Question 7
**Section 1. Scenario:** A model was trained with fe.log_model using a training set built from feature lookups. A batch job has only the customer ids. How does it score?

A. Join every feature table by hand first, because the logged model stores only feature names and keeps no record of where each feature came from
B. Call fe.score_batch with the model uri and a DataFrame of the keys, and the model looks up its own features
C. Retrain the model with the keys as the only inputs
D. Load the offline table into memory and replace the ids with random values

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Logging with the feature client stores the feature references, and score_batch uses the primary keys to fetch features. Columns you supply override stored values.
</details>

---

### Question 8
**Section 1. Scenario:** A fraud model needs customer features at single-digit millisecond latency inside a real-time endpoint. Which data structure supports this?

A. An online feature store holding the latest values for lookup by key
B. The offline Delta feature table, queried with a full scan on each request, since Delta reads are fast enough for real-time serving
C. A CSV file loaded on every request
D. A tag on the registered model

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Online feature stores are the low-latency store Databricks recommends for real-time serving. The offline table is for training and bulk scoring.
</details>

---

### Question 9
**Section 1. Scenario:** An ML platform lead is deciding how to move work from development to production. Which is the usual Databricks recommendation, and a reason for it?

A. Promote code, so the same review and integration tests apply and production models are trained by production code
B. Always copy trained models by hand, because retraining in production is forbidden
C. Train in production from scratch notebooks that are not under version control
D. Give data scientists write access in production so they can fix quickly

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The MLOps docs recommend promoting code in most situations. Models are promoted instead when retraining in the target environment is not possible, and data scientists typically do not have write access in production.
</details>

---

### Question 10
**Section 1. Scenario:** The model registry choice matters for lifecycle. A team still calls transition_model_version_stage to move a Unity Catalog model to Production. What is the issue?

A. Nothing, stages are the recommended Unity Catalog approach and the call is the standard way to move a model version to Production
B. Stages are not supported for models in Unity Catalog; use aliases and three-level names for environments
C. The call works only for tag-based models
D. The call is correct but must be run twice

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The docs state that stages are not supported for Unity Catalog models and recommend the three-level namespace for environments and aliases for promotion.
</details>

---

### Question 11
**Section 1. Scenario:** After a registered model version passes review, the team wants a note on it that a downstream process reads as 'validation approved', without changing what is served. What do they set?

A. The champion alias on that version
B. A new registered model with a different name
C. A model version tag such as validation_status=approved
D. A stage transition to Staging

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Tags are key-value labels for classification. They carry information but do not change which version an alias resolves to. Using an alias would change what production reads.
</details>

---

### Question 12
**Section 2. Scenario:** A Spark DataFrame column shows count 9,200 for 10,000 rows, a mean of 480, a median of 55 and a max of 99,000. What does summary() tell you?

A. The column is symmetric and ready to use, because the mean and median are both reported and the count is close to the number of rows
B. There are no missing values because count is positive
C. The standard deviation must be zero
D. There are about 800 nulls and the column is strongly right-skewed with extreme values

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Count excludes nulls, so 9,200 of 10,000 means 800 missing. A mean far above the median and a max far above the 75th percentile signal right skew and outliers.
</details>

---

### Question 13
**Section 2. Scenario:** A sensor feature is approximately normally distributed with two obvious glitches. Which outlier rule is suitable, and why?

A. Remove points more than about three standard deviations from the mean, because the data is roughly bell-shaped
B. Remove every point above the median
C. Remove points outside the 40th and 60th percentiles
D. Never remove anything, since outliers cannot be identified

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** On roughly normal data the standard deviation rule is gentle and appropriate. Heavily skewed data is the case where the IQR rule is the better choice.
</details>

---

### Question 14
**Section 2. Scenario:** A numeric feature has a long right tail with some very large values and 5 percent nulls. Which fill is the most defensible?

A. The median, because it is not pulled by the extreme values
B. The mean, because it uses every observation and therefore always represents the typical value of a numeric feature
C. The mode, because the feature is numeric
D. Zero, since zero never affects a model

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** With skew and outliers the mean is distorted; the median stays near the typical value. Zero changes the distribution and mode is mostly for categories.
</details>

---

### Question 15
**Section 2. Scenario:** A text column 'plan' with three values (basic, plus, pro) and no order is fed to logistic regression. Which preprocessing is appropriate?

A. Replace the values with 1, 2 and 3 and use them as one number, since logistic regression handles numeric codes for categories natively
B. One-hot encode it, so the model does not read a false numeric order into the plans
C. Drop the column because text cannot be used
D. Take the log of the string length

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** One-hot encoding creates one binary column per category for a nominal feature in a linear model. Mapping to 1, 2, 3 would tell the model that pro is three times basic.
</details>

---

### Question 16
**Section 2. Scenario:** For which feature is one-hot encoding a poor choice?

A. A country field with six values used in a neural network
B. A boolean field stored as yes or no
C. A user id with two million distinct values
D. A product category with four values used in a logistic regression

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** High-cardinality features create millions of sparse columns. Use hashing, target encoding or embeddings instead. The other three are small nominal features that one-hot encoding handles well.
</details>

---

### Question 17
**Section 2. Scenario:** A target that spans several orders of magnitude and is right-skewed, such as sale price, is being fitted by linear regression. Which transformation is typically useful?

A. Replacing the target with its rank, which removes the skew but discards the original units and the size of differences between values
B. Subtracting the minimum from every value
C. One-hot encoding the target
D. A log transformation of the target, then exponentiate predictions to return to the original units

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A log transform compresses the long tail and makes the distribution more symmetric. Predictions must be exponentiated afterwards to interpret them in original units.
</details>

---

### Question 18
**Section 3. Scenario:** A churn dataset has a 4 percent positive class and the first model has 96 percent accuracy and almost no recall on churners. What is the most direct fix?

A. Weight the minority class more or resample, and judge with recall or F1
B. Standardize every feature to zero mean and unit variance
C. Double the number of majority-class rows
D. Switch the metric to accuracy at a higher threshold, so the model is rewarded for the 96 percent of predictions it already gets right

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cost-sensitive learning or resampling acts on the imbalance, and accuracy hides it. Scaling, adding majority data and chasing accuracy do not.
</details>

---

### Question 19
**Section 3. Scenario:** In Spark ML, which statement about estimators and transformers is correct?

A. An estimator's fit() produces a model that is itself a transformer
B. A transformer learns parameters from data by calling fit(), and an estimator only applies those learned parameters to new data
C. A pipeline is a transformer that cannot be fitted
D. Estimators and transformers are the same, only the name differs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Spark ML docs define an estimator as an algorithm that can be fit on a DataFrame to produce a transformer, and a Pipeline is an estimator whose fit returns a PipelineModel.
</details>

---

### Question 20
**Section 3. Scenario:** A tuning job uses scikit-learn models on a Databricks cluster and wants to run trials in parallel with Hyperopt. Which trials object fits?

A. Trials, because it automatically distributes work to every worker
B. SparkTrials is only for MLlib models
C. No trials object exists; Hyperopt cannot run in parallel
D. SparkTrials, because the models are single-machine and each trial can run as a Spark task

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SparkTrials distributes single-machine models. Trials is used when the objective itself uses distributed training such as MLlib. One more fact: Hyperopt is no longer maintained upstream, and Databricks recommends Optuna or Ray Tune.
</details>

---

### Question 21
**Section 3. Scenario:** A team tunes a model with 4 values of learning rate, 3 values of depth and 5-fold cross-validation. How many models are trained during the search (not counting a final refit)?

A. 12
B. 20
C. 60
D. 15

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** 4 x 3 = 12 hyperparameter combinations, and each is trained once per fold: 12 x 5 = 60.
</details>

---

### Question 22
**Section 3. Scenario:** What is a real downside of k-fold cross-validation compared with a single train-validation split?

A. It cannot be used with a grid of parameters
B. It gives a less reliable estimate on small data
C. It requires labels to be removed
D. It trains the model k times per parameter setting, so it costs about k times as much

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Spark docs note that TrainValidationSplit evaluates each combination once rather than k times, so it is cheaper but less reliable on small data. Cross-validation is the more reliable but more expensive option.
</details>

---

### Question 23
**Section 3. Scenario:** A lender needs a classifier whose predicted probabilities are well calibrated, because they will be used directly to price risk. Which metric focuses on that?

A. Log loss, which scores the probability estimates directly
B. Accuracy at a threshold of 0.5, because it checks that the predicted class matches the label for every borrower
C. Recall alone
D. The number of features used

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Log loss (cross-entropy) is defined on probability estimates. Accuracy and recall depend on a threshold and ignore how confident the probabilities are.
</details>

---

### Question 24
**Section 3. Scenario:** A regression model for delivery times has a few very large mistakes that are especially costly. Which metric is most sensitive to those?

A. MAE, since it squares the errors before averaging and so weights large misses most heavily
B. RMSE, since squaring the errors penalizes large misses more heavily than MAE
C. R-squared, since it equals the largest error
D. Accuracy, since it counts every error equally

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RMSE squares errors before averaging, so large errors dominate. MAE treats errors in proportion to size and is more robust to outliers.
</details>

---

### Question 25
**Section 3. Scenario:** A model predicts log(price). The team computes RMSE directly between its output and the raw price column and gets a huge value. What should they do?

A. Apply log to the predictions a second time so that both sides of the comparison are on the same scale
B. Delete the largest prices
C. Switch to accuracy
D. Apply exp to the predictions before calculating RMSE against raw price

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The model's output is on the log scale. It must be exponentiated before comparing with raw values or interpreting predictions in original units.
</details>

---

### Question 26
**Section 3. Scenario:** A model has a training RMSE of 0.5 and a validation RMSE of 3.8. What does the bias-variance tradeoff suggest?

A. High bias (underfitting); add more layers or depth, because a model this far from its training targets is too simple
B. The model is ideal because training error is low
C. High variance (overfitting); reduce complexity, add regularization or get more data
D. The validation set is too small to say anything, so nothing can be concluded

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A large gap between low training error and high validation error is the signature of overfitting. High bias shows high error on both sets.
</details>

---

### Question 27
**Section 4. Scenario:** A bank scores a risk model once each night across all accounts and writes the results to a table that analysts read the next morning. Which approach fits?

A. A low-latency real-time endpoint called once per account, so each score is returned within milliseconds as the account is processed
B. A streaming pipeline that never stops
C. A GPU endpoint sized for the lowest latency
D. Batch inference on a schedule, writing predictions to a Delta table

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Without a per-request latency need, scheduled batch inference is the simplest and cheapest pattern. The docs describe batch for nightly refreshes and real time for decisions at transaction time.
</details>

---

### Question 28
**Section 4. Scenario:** A scientist has a registered model and a 50,000-row pandas DataFrame that fits in driver memory. What is the straightforward batch route?

A. Create a serving endpoint for the single call
B. Convert the model to a streaming query
C. Load the model with mlflow.pyfunc.load_model and call predict on the DataFrame
D. Retrain the model on the DataFrame first

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** pyfunc.load_model loads any logged flavor as a Python function, and predict scores a pandas DataFrame. If the data no longer fits, mlflow.pyfunc.spark_udf distributes the same model over Spark.
</details>

---

### Question 29
**Section 4. Scenario:** A client sends feature rows to a custom model endpoint as JSON. Which input format does Databricks recommend for tabular data?

A. dataframe_records, because it guarantees column order and is the format Databricks recommends for tabular data
B. dataframe_split, a pandas DataFrame in split orientation with columns and data
C. A CSV string in the URL
D. A pickled file in the request body

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The docs recommend dataframe_split; dataframe_records does not guarantee column order. Responses come back under a predictions key.
</details>

---

### Question 30
**Section 4. Scenario:** A team wants 10 percent of live requests to go to a candidate model and 90 percent to the current one, from a single URL. What do they configure?

A. Two separate endpoints and a client that flips a coin
B. A tag with the value 10 on the model version
C. Scale to zero on the current model
D. One endpoint with two served entities and traffic_config routes of 90 and 10 percent

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** One Model Serving endpoint can serve several models of the same kind and split traffic by percentage with traffic_config routes. Calling a served model directly bypasses the split.
</details>

---

## Where to go deeper

- [ML Associate cert page](../databricks/ml-associate/README.md) - notes, practice plan, strategy
- [ML Professional practice questions](databricks-ml-professional.md) - the next level up
- [Data Engineer Associate practice questions](https://data.noblerworks.com/resources/practice-questions/databricks-data-engineer-associate/) - the data platform beneath
- [AI/ML systems topic index](../../build/README.md) - MLOps across the repo
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides
