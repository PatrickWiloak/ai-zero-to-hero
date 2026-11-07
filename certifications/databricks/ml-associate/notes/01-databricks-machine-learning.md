# Section 1: Databricks Machine Learning (38%)

**Last reviewed:** 2026-11-07

This is the biggest section of the exam, and it is the one that is least about machine learning and most about the Databricks platform around it. The questions ask what a tool is for, which API call does a job, and which of two similar-sounding options is the current one. Everything below follows the order of the official exam guide ([August 2026 guide](https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Machine-Learning-Associate-Exam-Guide-August-2026.pdf)): MLOps strategy and ML runtimes, AutoML, feature tables in Unity Catalog, MLflow tracking, the Unity Catalog model registry, and promotion with aliases.

**[📖 Machine learning on Databricks](https://docs.databricks.com/aws/en/machine-learning/)** - Entry point to the platform docs for this section

## MLOps strategy and best practices

MLOps is the practice of running machine learning the way a team runs any production software: versioned code, tested changes, controlled environments, monitoring. Databricks describes it as combining DevOps, DataOps and ModelOps, which is its way of saying that you manage three kinds of asset (code, data and models) and the platform gives you one place and one access-control system for all three.

**[📖 MLOps workflow on Databricks](https://docs.databricks.com/aws/en/machine-learning/mlops/mlops-workflow)** - The recommended environments, promotion approach and retraining advice

The guide's advice reduces to a handful of ideas the exam likes to test:

- **Separate environments by stage.** Development, staging and production are kept apart, with defined transitions between them. Data scientists experiment in development. Staging is where the pipeline *code* is tested (unit tests on pull requests, integration tests of the whole set of pipelines). Production is owned by ML engineers, and data scientists typically get read-only access there.
- **Everything lives in a governed home.** Code in Git, data as Delta tables under access control, experiments tracked in MLflow, and model lifecycle managed in Unity Catalog.
- **In most situations, promote code, not models.** The docs say this ensures all code in the ML process goes through the same review and integration testing, and that production models are trained by production code. We come back to the exceptions in the promotion section below.
- **Start with scheduled retraining.** The docs recommend beginning with scheduled, periodic retraining and moving to triggered retraining when needed.
- **Reference aliases, not version numbers.** Inference pipelines read the model that holds the Champion alias, so promoting a new version does not require editing the pipeline.

Notice the pattern: each of these is a trade between speed and safety, and the platform answer is almost always "the version that keeps a review and an audit trail".

## Advantages of ML runtimes

A Databricks Runtime for Machine Learning (ML runtime) is a cluster image with the machine learning and deep learning tooling already installed and kept compatible. The docs say it "automates the creation of a compute resource with pre-built machine learning and deep learning infrastructure". The advantage the exam wants is simple: you do not spend your time building and debugging a Python environment, and the libraries in it are versions Databricks has tested together. You can still add libraries at notebook, compute or init-script level.

**[📖 Databricks Runtime for Machine Learning](https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml)** - What the ML runtime is and what it adds

Three smaller facts from the same page that could appear as distractors or answers: selecting the machine learning option sets the access mode to Dedicated automatically; Photon (15.2 ML and above) speeds up Spark SQL, DataFrames and feature engineering but not Pandas UDFs or Python-only libraries; and for custom GPU deep learning the page now points to AI Runtime instead.

- **ML runtime** - a Databricks Runtime variant that comes with machine learning and deep learning libraries pre-installed and tested together, so a team does not build the environment itself.
- **Dedicated access mode** - the cluster access mode that is set automatically when you pick the machine learning runtime, and that Unity Catalog data access from ML compute requires.

## AutoML: model selection, feature selection and what it adds

AutoML takes a dataset and a target and does the repetitive part of model building for you. According to the docs it cleans and prepares the data, runs distributed training and hyperparameter tuning across multiple algorithms, and selects the best model using open source evaluation algorithms (scikit-learn, xgboost, LightGBM, Prophet and ARIMA), then presents the results. It supports classification, regression and forecasting, from either a low-code UI or the Python API.

**[📖 What is AutoML?](https://docs.databricks.com/aws/en/machine-learning/automl/)** - AutoML workflow, supported problem types and algorithms

The point the exam keeps returning to is *transparency*. AutoML generates a source code notebook for every trial, "allowing you to review, reproduce, and modify the code as needed", so it is not a black box: a data scientist can open the best trial's notebook and continue from there. For classification and regression, notebooks for data exploration and the best trial are imported to the workspace and the other trial notebooks are saved as MLflow artifacts. SHAP feature importance code is included but off by default (`shap_enabled = True` turns it on).

So the two advantages to remember:

1. **Selection:** it compares several algorithm families and hyperparameter settings for you and ranks them, so you start from a measured baseline instead of a guess.
2. **Development speed with editable code:** the baseline arrives as notebooks you can read and extend.

What AutoML is not: it does not remove the need for judgment about the metric, the leakage in your features, or whether the model should ship.

- **AutoML** - a Databricks capability that prepares data, trains and tunes models across several algorithms, picks the best, and generates editable notebooks for the trials.
- **Trial notebook** - the generated source code for a single AutoML trial, which you can review, reproduce and modify.

## Feature tables in Unity Catalog

A feature table is a Delta table with a primary key that holds precomputed features so training and inference read the same values. In a Unity Catalog workspace the table is a Unity Catalog object with a three-level name, `catalog.schema.table`, governed like any other table, and "accessible to all workspaces assigned to the table's Unity Catalog metastore". That is the exam's answer to *account level versus workspace level*: the workspace feature store is the legacy option confined to one workspace, while a Unity Catalog feature table is shared across every workspace on the metastore with Unity Catalog's access control, lineage and discovery.

**[📖 Work with feature tables in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc)** - Create, write, read and update feature tables

### Create and write

You use the `FeatureEngineeringClient` from `databricks.feature_engineering`. `create_table` takes a name, primary keys, a schema (or a DataFrame) and a description; `write_table` writes data and with `mode='merge'` upserts by primary key. This is the exact pattern of the guide's sample question: there is no `AS FEATURE STORE` SQL clause and no `register_table`; you use `create_table`, then write data.

```python
# Not run here: needs a Databricks workspace with Unity Catalog (from the Databricks docs)
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

fe.create_table(
    name='ml.recommender_system.customer_features',
    primary_keys='customer_id',
    schema=customer_features_df.schema,
    description='Customer features')

fe.write_table(
    name='ml.recommender_system.customer_features',
    df=customer_features_df,
    mode='merge')
```

Requirements worth remembering: feature tables must have a primary key, and they need Databricks Runtime 13.2 or above (the `TIMESERIES` keyword needs 13.3 LTS or above). With `mode='merge'`, rows whose keys are not in the DataFrame are left alone. Do not change the primary key or the name or type of an existing feature, because downstream pipelines can break.

### Train and score with features

Training uses a `FeatureLookup` for each table you want to join, `create_training_set` to build the dataset, and `fe.log_model` to save the model *together with its feature references*.

**[📖 Train models using feature tables](https://docs.databricks.com/aws/en/machine-learning/feature-store/train-models-with-feature-store)** - FeatureLookup, create_training_set, log_model, score_batch

```python
# Not run here: Databricks only (from the Databricks docs)
feature_lookups = [
    FeatureLookup(table_name='ml.recommender_system.customer_features',
                  feature_names=['total_purchases_30d', 'total_purchases_7d'],
                  lookup_key='customer_id')]
training_set = fe.create_training_set(df=training_df, feature_lookups=feature_lookups,
                                      label='rating', exclude_columns=['customer_id'])
training_df = training_set.load_df()          # train on THIS dataframe
fe.log_model(model=model, artifact_path="recommendation_model",
             flavor=mlflow.sklearn, training_set=training_set,
             registered_model_name="recommendation_model")

predictions = fe.score_batch(model_uri=model_uri, df=batch_df)   # keys only
```

Two details the exam can lean on. First, you must train on the DataFrame returned by `load_df`, and log with `fe.log_model` from the feature client, because that is what attaches the lookup information. Second, scoring with `fe.score_batch` needs only the primary keys: the model fetches its features itself, and columns you do supply override the stored values. A missing lookup returns `NaN` in batch scoring.

### Online versus offline feature tables

The offline table is the Delta table you just built: large, cheap, queried in bulk for training and batch scoring. An online store is a low-latency copy for real-time serving, where the model has milliseconds to fetch features by key. Databricks says that for real-time serving of feature values it recommends Databricks Online Feature Stores, or you can publish to a third-party low-latency database. With automatic feature lookup the client sends only the keys and values that exist at request time and the model looks up the rest.

**[📖 Online feature stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-stores)** - Real-time feature serving and automatic feature lookup

- **Feature table** - a Delta table with a primary key (and optionally a time series column) that stores computed features for reuse in training and inference.
- **FeatureEngineeringClient** - the Python client in `databricks.feature_engineering` used to create, write, read and tag feature tables and to build training sets.
- **FeatureLookup** - the object that tells a training set which table, which features and which lookup key to join in.
- **Offline feature table** - the governed Delta table used for training and batch scoring, queried in bulk.
- **Online feature store** - a low-latency store holding the latest feature values so a real-time endpoint can look features up by key.

## MLflow: finding the best run, logging, and the UI

MLflow tracking records what happened in each training execution. A *run* is one execution of model code, an *experiment* groups related runs, and on Databricks the hosted tracking server stores experiment data in your workspace with no setup. With no active experiment, runs land in the notebook's experiment. Autologging is the easiest way to start; the logging API gives control over which parameters and metrics are recorded and lets you attach artifacts such as plots or CSV files.

**[📖 MLflow experiment tracking](https://docs.databricks.com/aws/en/mlflow/tracking)** - Runs, experiments, autologging and querying runs programmatically

The docs name two ways to analyze runs in code: the Python client's `search_runs`, which returns a pandas DataFrame, and a Spark data source for reading experiments. "Identify the best run using the MLflow Client API" therefore means `search_runs` with an `order_by` on the metric. I ran this against MLflow OSS (3.18.0, SQLite backend, four Ridge runs with different `alpha`, each logging a parameter, a metric, a model and an artifact):

```python
client = MlflowClient()
best = client.search_runs([exp.experiment_id],
                          order_by=["metrics.validation_rmse ASC"], max_results=1)[0]
print("best run:", best.data.params, round(best.data.metrics["validation_rmse"], 3))
```

```
best run: {'alpha': '0.01'} 10.815
  params.alpha  metrics.validation_rmse
0         0.01                    10.81
1            1                    10.95
2          100                    42.78
3        10000                   120.32
```

Server-side ordering is the whole trick: you do not fetch every run and sort in Python, and you do not pick "the latest run", which is not necessarily the best. Manual logging inside a run is `mlflow.log_param`, `mlflow.log_metric`, `mlflow.log_artifact` and `mlflow.<flavor>.log_model`, all inside a `with mlflow.start_run():` block.

What the MLflow UI shows is the other half of this objective: for each run the parameters, metrics, tags and artifacts (including the logged model), and for an experiment a table where you compare and filter runs. The docs say you "can compare and filter runs to understand how your model performs".

- **MLflow run** - one execution of model training code, which records parameters, metrics, tags and artifacts.
- **MLflow experiment** - a named group of related runs that you can compare and filter.
- **search_runs** - the MLflow client call that queries runs, with `order_by` such as `metrics.rmse ASC`, and returns them (as a pandas DataFrame from `mlflow.search_runs`).
- **Autologging** - MLflow's automatic capture of parameters, metrics and the model for supported libraries, the easiest way to start tracking.

## The Unity Catalog model registry

Registering a model turns a run's logged model into a named, versioned, governed object. In Unity Catalog the name is three-level (`catalog.schema.model`), the client is pointed at it with `mlflow.set_registry_uri("databricks-uc")` where that is not the default, and `mlflow.register_model(model_uri, name)` creates a new version each time. New Unity Catalog model versions must have a model signature, which autologging or an input example provides.

**[📖 Manage model lifecycle in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/)** - Registering models, aliases, tags and loading by alias

**Why it beats the workspace registry.** Models in Unity Catalog extend the benefits of Unity Catalog to models: "centralized access control, auditing, lineage, and model discovery across workspaces". The workspace registry is the legacy option for workspaces without Unity Catalog.

**Promoting code versus promoting models.** The default recommendation is promote *code*: the training pipeline is reviewed, tested in staging and run in production, so the production model comes from production-tested code. Promoting a *model* (copying the artifact between catalogs) is the better choice when training is expensive or cannot be re-run, for example a very large model trained once, or when the production environment may not access the training data. (The docs say "in most situations" promote code and link to a separate discussion of trade-offs; the two examples here are my reading of that trade-off, not a quote.) The exam wording is "identify scenarios where X is preferred", so reason from the constraint: cannot re-train in prod means promote the model; can re-train and want review means promote code.

### Tags and aliases

Tags are key-value labels on a registered model or a model version, such as `validation_status` = `approved`. Aliases are "a mutable, named reference to a particular version of a registered model". The pattern: register the new version, give it the `challenger` alias while it is validated, and when it wins, point `champion` at it. Inference code loads `models:/catalog.schema.model@champion`, so nothing downstream changes. Stages (Staging, Production) are not supported for models in Unity Catalog: the docs say to use the three-level namespace for environments and aliases to promote models. That is why "transition to the Production stage" in the guide's sample question is wrong.

I ran the whole workflow on MLflow OSS (aliases and tags behave the same way; the Unity Catalog three-level name is the only difference here):

```python
client.set_registered_model_alias(name, "champion", v1.version)
client.set_registered_model_alias(name, "challenger", v2.version)
client.set_model_version_tag(name, v2.version, "validation_status", "approved")
# ... then
client.delete_model_version_tag(name, v2.version, "validation_status")
client.set_registered_model_alias(name, "champion", v2.version)   # promote
m = mlflow.pyfunc.load_model(f"models:/{name}@champion")
```

```
tags: {'validation_status': 'approved'}
tags after delete: {}
champion -> 1 | challenger -> 2
after promote champion -> 2
loaded by alias, predict: [ -64.9  -104.17]
```

Promotion is one call that *reassigns* the alias. Nothing is deleted, the old version is still there, and rolling back is the same call pointed at version 1. That is the property that makes aliases better than deleting the old version or editing tags (a tag is only descriptive metadata and does not change which version is served).

- **Unity Catalog model registry** - the registry that stores models as three-level named, versioned Unity Catalog objects with centralized access control, auditing, lineage and cross-workspace discovery.
- **Model alias** - a mutable, named reference (such as champion) to one version of a registered model, set with `set_registered_model_alias`.
- **Model tag** - a key-value label on a registered model or model version, set with `set_model_version_tag` and removed with `delete_model_version_tag`.
- **Champion and challenger** - the convention of giving the serving version the champion alias and the candidate the challenger alias, and promoting by moving champion to the winner.
- **Promote code versus promote models** - the two promotion strategies; code promotion is the usual recommendation, and model promotion fits cases where retraining in production is not possible.

## Check yourself against the objectives

Say what the MLOps recommendation is and where the exceptions come from; say what AutoML adds and why its notebooks matter; write the create, write, train and score sequence for a feature table from memory; explain online versus offline; name the call that finds the best run; and explain alias promotion and why stages are gone. Questions for this section are in the [Databricks ML Associate bank](../../../practice-questions/databricks-ml-associate.md).
