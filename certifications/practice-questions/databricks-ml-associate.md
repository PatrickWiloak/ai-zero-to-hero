---
last-updated: 2026-10-22
difficulty: intermediate
---

# Databricks Certified Machine Learning Associate - Practice Questions

30 questions for the ML Associate exam, weighted toward ML workloads on Databricks (29%) and the ML workflow (29%), then Spark ML (17%), deep learning (13%), and scaling (12%).

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

### Question 16
**Scenario:** A batch scoring notebook must always load whichever version of `main.fraud.classifier` is currently marked as the production model in Unity Catalog, without editing the notebook on each promotion.

A. Load the model from the run ID of the training run that produced the current production version
B. Load `models:/main.fraud.classifier/latest`, which always returns the version in production use
C. Load `models:/main.fraud.classifier@champion`, and move the alias when a new version is promoted
D. Copy the model files to a fixed DBFS path on each promotion and load the files from that path

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An alias is a mutable pointer to a model version, so code that loads by alias picks up a promotion as soon as the alias moves. A run ID hard-codes one version. The newest version is not necessarily the approved one, and copying files outside the registry loses lineage and access control.
</details>

---

### Question 17
**Scenario:** A churn model uses customer features stored in a Unity Catalog feature table. The team wants batch scoring to look up the same features automatically, given only customer IDs.

A. Build the training set with `FeatureLookup` and log the model with the Feature Engineering client
B. Export the feature table to CSV after each training run and join it to the scoring data by hand
C. Recompute every feature inside the scoring notebook using a copy of the training notebook's code
D. Store the feature values inside the model artifact so that they travel with the model to scoring

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** When a model is trained on a training set built from feature lookups and logged through the Feature Engineering client, the model carries its feature metadata, so scoring can fetch features by key automatically. Manual joins and copied code are where training-serving skew creeps in, and features frozen in the artifact go stale.
</details>

---

### Question 18
**Scenario:** An experiment has 300 MLflow runs. A data scientist needs the run with the highest validation AUC programmatically, to register its model.

A. Open each run in the UI in turn and write down its AUC, then pick the highest one by hand
B. Register every run's model and keep the version that the serving endpoint scores best on
C. Rerun the training for every configuration so that the AUC values can be compared together
D. Use `mlflow.search_runs` on the experiment, ordered by `metrics.val_auc DESC`, and take the first

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `mlflow.search_runs` returns runs as a DataFrame and supports filters and ordering on metrics and parameters, so selecting the best run is one call. Checking 300 runs by hand is slow and error-prone, rerunning wastes compute, and registering every model clutters the registry.
</details>

---

### Question 19
**Scenario:** A model served from Unity Catalog accepts requests with misnamed or wrongly typed columns and returns nonsense instead of a clear error.

A. Add a try and except block in the client code that retries any request that returns odd values
B. Log the model with a signature and an input example so the expected schema is recorded
C. Write the expected column names in the model's description field in Unity Catalog
D. Retrain the model on a wider range of inputs so that it can handle wrongly typed columns

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An MLflow model signature records the expected input and output schema, so input that does not match can be checked and rejected, and the input example documents valid requests. Retries repeat the same bad input, a description is not enforced, and retraining does not make a model understand misnamed columns.
</details>

---

### Question 20
**Scenario:** A team has only 2,000 labeled rows. A single 80/20 train-test split gives accuracy that swings by several points depending on the random seed.

A. Use the same random seed every time so that the accuracy figure stays stable between runs
B. Train on all 2,000 rows and report training accuracy, since no data is wasted on a test set
C. Increase the test share to 50% so that the test set is large enough to give a stable estimate
D. Use k-fold cross-validation to average performance across folds for a more stable estimate

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cross-validation trains and evaluates on several splits and averages the results, which reduces the variance of the estimate on small datasets. Fixing the seed hides the variance rather than reducing it, training accuracy overstates performance, and a bigger test set leaves less data to train on.
</details>

---

### Question 21
**Scenario:** A fraud dataset has 1% positive labels. After a random split, one validation set contains almost no fraud cases.

A. Use a stratified split so each split keeps roughly the same share of fraud cases
B. Drop the validation set and judge the model only on its training metrics instead
C. Remove most of the non-fraud rows from the validation set so it has more fraud cases
D. Shuffle the data again and keep re-splitting until the validation set looks balanced

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Stratified splitting preserves the class proportions in each split, so validation reflects the real class mix and contains enough positives to measure. Training metrics overstate performance, rebalancing the validation set distorts the metrics, and re-splitting until it looks right is an unprincipled version of stratification.
</details>

---

### Question 22
**Scenario:** A Spark ML pipeline fails because a numeric column has nulls. The column is skewed, and the team wants a fill value that is not distorted by outliers.

A. Use `VectorAssembler` with `handleInvalid` set to keep, which fills each null with zero
B. Drop the column from the pipeline, since columns with nulls cannot be used in Spark ML
C. Add an `Imputer` stage with `strategy` set to `median` before assembling the features
D. Use `StringIndexer` on the column so that the nulls become their own category index

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Spark ML's `Imputer` fills missing numeric values with the mean, median or mode, and the median is robust to skew. Placing it in the pipeline means the same fill values are learned on training data and reapplied at inference. Dropping the column loses information, and `StringIndexer` is for categorical strings, not numeric columns.
</details>

---

### Question 23
**Scenario:** A gradient-boosted model has eight hyperparameters to tune, and each training run takes 20 minutes. A full grid search would need thousands of runs.

A. Run the full grid search anyway, since only a grid is certain to find the best combination
B. Use random or Bayesian search (for example Optuna), which explores the space in fewer trials
C. Tune one hyperparameter at a time and keep the others at their default values throughout
D. Skip tuning and use the defaults, since boosted trees do not benefit from hyperparameter tuning

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** With many hyperparameters, random search and Bayesian optimization such as Optuna find good regions with far fewer trials than a grid, and can run trials in parallel. A full grid is impractical here, one-at-a-time tuning misses interactions, and boosted trees are sensitive to settings like depth and learning rate.
</details>

---

### Question 24
**Scenario:** A new team member asks what `LogisticRegression().fit(train_df)` returns in Spark ML, and how it is then used.

A. It returns a DataFrame of predictions for the training data, which is then written to a Delta table
B. It returns nothing, and the estimator object itself is updated in place with the learned weights
C. It returns a Pipeline, which must be fitted a second time before it can be used for predictions
D. It returns a fitted model, which is a Transformer that adds predictions with `transform()`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** In Spark ML an Estimator's `fit()` returns a Model, and that Model is a Transformer whose `transform()` adds prediction columns to a DataFrame. Estimators are not modified in place, `fit()` does not return predictions, and a Pipeline is something you build from stages, not the output of fitting one.
</details>

---

### Question 25
**Scenario:** A Spark ML regression fails with an error that the input column `features` does not exist. The DataFrame has twelve separate numeric columns.

A. Combine the columns into a single vector column with `VectorAssembler` before the estimator
B. Rename one of the numeric columns to `features`, since the estimator needs only one column
C. Convert the DataFrame to pandas, since Spark ML estimators cannot read numeric columns
D. Set the estimator's `featuresCol` to a comma-separated list of the twelve column names

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Spark ML estimators expect all features in one vector column, which `VectorAssembler` builds from the individual columns. Renaming one column would train on one feature only, `featuresCol` takes a single column name, and converting to pandas gives up distributed training.
</details>

---

### Question 26
**Scenario:** A team tunes a Spark ML pipeline with `CrossValidator` over a parameter grid of 24 combinations and 3 folds. The cluster sits mostly idle while models train one after another.

A. Reduce the folds to one so that each combination trains only a single model on the cluster
B. Set the `parallelism` parameter on `CrossValidator` so several models train at the same time
C. Replace `CrossValidator` with a loop on the driver that trains each combination in pandas
D. Increase the number of partitions in the data so that each single model trains faster

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `CrossValidator` and `TrainValidationSplit` have a `parallelism` setting that fits multiple models concurrently, which uses idle cluster capacity. One fold is no longer cross-validation, a driver loop in pandas abandons the cluster, and repartitioning does not change the one-at-a-time evaluation order.
</details>

---

### Question 27
**Scenario:** A manufacturer has 3,000 labeled images of product defects and wants an image classifier. Training a deep network from scratch overfits badly.

A. Train a much deeper network from scratch, since a bigger model learns more from small data
B. Convert the images to tabular pixel columns and train a linear model with Spark ML
C. Start from a pretrained image model and fine-tune it, at first training only the top layers
D. Duplicate each image ten times so that the training set has 30,000 images to learn from

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Transfer learning reuses features learned on a large dataset, so a small labeled set is enough to adapt the final layers, and more layers can be unfrozen later. A deeper model from scratch overfits more, raw pixels in a linear model lose spatial structure, and exact duplicates add no new information.
</details>

---

### Question 28
**Scenario:** During deep learning training, validation loss starts rising after epoch 12 while training loss keeps falling. The job is set to run 100 epochs.

A. Increase the learning rate after epoch 12 so that the model escapes the rising validation loss
B. Remove the validation set, since rising validation loss means the validation data is noisy
C. Keep training for all 100 epochs, since training loss is still falling and the model is improving
D. Use early stopping on validation loss and keep the best checkpoint, logged to MLflow

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Diverging training and validation loss is overfitting, and early stopping halts training when validation loss stops improving while keeping the best weights. Continuing to 100 epochs makes it worse, a higher learning rate does not fix overfitting, and the validation set is what detected the problem.
</details>

---

### Question 29
**Scenario:** A scikit-learn model logged with MLflow must score 2 billion rows in a Delta table each night. A single-node loop takes far too long.

A. Collect the table to the driver in chunks and call `model.predict` on each chunk in turn
B. Load the model with `mlflow.pyfunc.spark_udf` and apply it to the Spark DataFrame in parallel
C. Retrain the model in Spark ML from scratch, since scikit-learn models cannot be used on Spark
D. Deploy the model to a serving endpoint and send it 2 billion requests from a notebook loop

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `mlflow.pyfunc.spark_udf` wraps any MLflow model as a Spark UDF, so scoring runs in parallel across the cluster's workers. Collecting to the driver keeps the bottleneck, a real-time endpoint is the wrong tool for bulk scoring, and retraining in another library is unnecessary.
</details>

---

### Question 30
**Scenario:** A retailer needs a separate demand-forecast model for each of 5,000 stores, using a single-node Python library. Training them one by one on the driver takes days.

A. Group by store and use `applyInPandas` so each store's model trains in parallel on the workers
B. Train one global model on all stores together, since per-store models cannot be parallelized
C. Start 5,000 separate jobs at once, each on its own cluster, to train one store per job
D. Increase the driver's memory so that the loop runs faster when training each store's model

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `groupBy(...).applyInPandas(...)` hands each group's data to a pandas function on the workers, which is the standard pattern for training many independent single-node models in parallel. A global model changes the requirement, 5,000 clusters waste startup time and cost, and more driver memory does not parallelize a loop.
</details>

---

## Where to go deeper

- [ML Associate cert page](../databricks/ml-associate/README.md) - notes, practice plan, strategy
- [ML Professional practice questions](databricks-ml-professional.md) - the next level up
- [Data Engineer Associate practice questions](https://data.noblerworks.com/resources/practice-questions/databricks-data-engineer-associate/) - the data platform beneath
- [AI/ML systems topic index](../../build/README.md) - MLOps across the repo
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides
