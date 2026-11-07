---
last-updated: 2026-11-07
---

# Databricks Machine Learning Associate - Fact Sheet

## Exam Overview

**Exam Name:** Databricks Certified Machine Learning Associate
**Duration:** 90 minutes
**Questions:** 48 scored multiple-choice and multiple-selection (up to 10 more unscored)
**Passing Score:** Not published by Databricks
**Cost:** $200 USD plus applicable taxes (stated by Databricks, checked 2026-11-07)
**Delivery:** Online proctored or test center
**Valid For:** 2 years

**[📖 Official Exam Page](https://www.databricks.com/learn/certification/machine-learning-associate)** - Registration and exam details
**[📖 Exam Guide PDF](https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Machine-Learning-Associate-Exam-Guide-August-2026.pdf)** - The four-section outline with objectives
**[📖 Databricks documentation](https://docs.databricks.com/)** - The authoritative, current source

## Target Audience

Individuals who use Databricks for basic ML tasks. Databricks recommends six months of hands-on experience with the platform areas in the outline. No prerequisite.

## Section 1: Databricks Machine Learning (38%)

Full teaching: [notes/01-databricks-machine-learning.md](notes/01-databricks-machine-learning.md).

**[📖 MLOps workflow](https://docs.databricks.com/aws/en/machine-learning/mlops/mlops-workflow)** - Environments, promote code, retraining
**[📖 Runtime for ML](https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml)** - ML runtime advantages
**[📖 AutoML](https://docs.databricks.com/aws/en/machine-learning/automl/)** - What AutoML does
**[📖 Feature tables in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc)** - Create and write
**[📖 Train with feature tables](https://docs.databricks.com/aws/en/machine-learning/feature-store/train-models-with-feature-store)** - Training sets and scoring
**[📖 Online feature stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-stores)** - Real-time features
**[📖 MLflow tracking](https://docs.databricks.com/aws/en/mlflow/tracking)** - Runs, experiments, search_runs
**[📖 Models in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/)** - Registry, aliases, tags

**Key Facts:**
- Promote code, not models, "in most situations" (MLOps docs); aliases let pipelines reference Champion without edits
- AutoML covers classification, regression and forecasting and generates a notebook per trial
- Feature tables need a primary key and Databricks Runtime 13.2+; create with `FeatureEngineeringClient.create_table`, write with `write_table` (`mode='merge'` upserts)
- Train on the DataFrame from `TrainingSet.load_df` and log with `fe.log_model`; `fe.score_batch` needs the primary keys (plus any external columns the model was trained with); supplied columns override stored values
- Best run: `search_runs` with `order_by=["metrics.<name> ASC"]`
- Unity Catalog models: three-level names, aliases, tags; stages are not supported
- Promote a challenger with `set_registered_model_alias(name, "champion", version)`

## Section 2: Data Processing (19%)

Full teaching: [notes/02-data-processing.md](notes/02-data-processing.md).

**[📖 dbutils.data.summarize](https://docs.databricks.com/aws/en/dev-tools/databricks-utils)** - Notebook data summaries
**[📖 Spark ML features](https://spark.apache.org/docs/latest/ml-features.html)** - StringIndexer, OneHotEncoder, Imputer

**Key Facts:**
- `df.summary()` returns count, mean, stddev, min, quartiles, max; counts skip nulls
- Outliers: standard deviation rule (assumes bell shape) or IQR rule (Q1 - 1.5 IQR, Q3 + 1.5 IQR; robust to skew)
- Impute: mean for symmetric continuous, median for skewed, mode for categorical
- One-hot encoding: nominal, low-cardinality, numeric models; not for ordinal or very high cardinality
- Log transform: right-skewed positive data across orders of magnitude

## Section 3: Model Development (31%)

Full teaching: [notes/03-model-development.md](notes/03-model-development.md).

**[📖 Hyperopt concepts](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/hyperopt-concepts)** - fmin, Trials, SparkTrials
**[📖 ML Pipelines](https://spark.apache.org/docs/latest/ml-pipeline.html)** - Transformer, Estimator, Pipeline
**[📖 ML Tuning](https://spark.apache.org/docs/latest/ml-tuning.html)** - CrossValidator, TrainValidationSplit
**[📖 Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html)** - F1, log loss, ROC AUC

**Key Facts:**
- Imbalance: cost-sensitive learning, resampling, better metrics, stratified splits
- Models trained by grid search with cross-validation = (grid combinations) x (folds); `TrainValidationSplit` = combinations x 1
- `SparkTrials` parallelizes single-machine models; use `Trials` with distributed algorithms
- Hyperopt is unmaintained and absent from Databricks Runtime ML after 16.4 LTS ML (Optuna or Ray Tune recommended)
- Exponentiate predictions from a log-trained model before computing RMSE or interpreting them
- Overfitting = low training error, high validation error; underfitting = both high

## Section 4: Model Deployment (12%)

Full teaching: [notes/04-model-deployment.md](notes/04-model-deployment.md).

**[📖 ML lifecycle](https://docs.databricks.com/aws/en/machine-learning/concepts/ml-lifecycle)** - Real-time versus batch
**[📖 Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/)** - Endpoints
**[📖 Create serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints)** - UI, REST, SDK
**[📖 Query custom model endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-custom-model-endpoints)** - Input formats
**[📖 Serve multiple models](https://docs.databricks.com/aws/en/machine-learning/model-serving/serve-multiple-models-to-serving-endpoint)** - Traffic split
**[📖 Pipelines transform](https://docs.databricks.com/en/delta-live-tables/transform.html)** - MLflow models in pipelines

**Key Facts:**
- Batch for scheduled bulk scoring, real time for per-request latency, streaming for continuous events
- `mlflow.pyfunc.load_model(...).predict(pandas_df)` for in-memory batch; `mlflow.pyfunc.spark_udf` for Spark
- Pipelines do not install MLflow by default
- Query formats: `dataframe_split` (recommended), `dataframe_records`, `instances`, `inputs`
- Traffic split: `traffic_config.routes` with `served_model_name` and `traffic_percentage`; not across model types
- Scale to zero is not recommended for production endpoints

## Exam Tips

1. Section 1 plus Section 3 are 69 percent of the exam: platform API names and metric choice
2. When two answers both "work", pick the one the current docs recommend (aliases over stages, `create_table` over any SQL shortcut)
3. Count models as combinations x folds
4. Match the metric to the cost of the mistake, not to habit
5. Choose the serving pattern from the latency requirement
