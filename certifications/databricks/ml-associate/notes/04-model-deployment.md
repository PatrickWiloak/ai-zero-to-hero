# Section 4: Model Deployment (12%)

**Last reviewed:** 2026-11-07

The smallest section, but it has the sharpest "which one" questions. A trained model is only useful when something calls it, and the first decision is *when* predictions are needed: on a schedule over many rows (batch), in milliseconds per request (real time), or continuously as data arrives (streaming). The objectives follow the [official exam guide (August 2026)](https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Machine-Learning-Associate-Exam-Guide-August-2026.pdf). Batch and streaming scoring below were run locally (MLflow 3.18.0, PySpark 4.3.0, scikit-learn); anything that needs a Databricks serving endpoint is marked not run.

## Batch, real-time and streaming: differences and advantages

**[📖 Machine learning lifecycle on Databricks](https://docs.databricks.com/aws/en/machine-learning/concepts/ml-lifecycle)** - The two serving patterns and the shared model artifact

| Approach | What it is | Choose it when | Cost shape |
|---|---|---|---|
| Batch | Score many rows on a schedule and write predictions to a Delta table | Predictions can be computed ahead and stored: nightly recommendations, daily forecasts | Compute only while the job runs; cheapest per prediction |
| Real time | A low-latency REST endpoint scores one request (or a few) at a time | A decision is needed at request time: fraud at checkout, live personalization | An always-available endpoint (autoscaling helps, but you pay for readiness) |
| Streaming | A continuously running pipeline scores events as they arrive | Events flow constantly and results are needed within seconds or minutes, without a per-event API call | A pipeline that runs continuously; scales with event volume |

The docs describe real-time serving as the fit for "fraud interception at transaction time, live personalization, or dynamic pricing", and batch inference as what "handles daily forecasts, nightly recommendation refreshes, and other periodic jobs". They also state that "Both patterns use the same trained model artifact", which is the important design point: you register the model once and choose the serving pattern separately, without retraining or changing governance. The decision rule for the exam: ask what latency the consumer needs. If the answer is "tomorrow morning" it is batch; "while the user waits" is real time; "as events happen, in volume" is streaming.

- **Batch inference** - scoring a whole dataset on a schedule and storing the predictions, which is the simplest and cheapest pattern when no per-request latency is required.
- **Real-time inference** - scoring individual requests through a low-latency REST endpoint such as a Model Serving endpoint.
- **Streaming inference** - scoring records continuously as they arrive in a streaming pipeline.

## Batch inference with pandas

For data that fits in memory on one machine, "use pandas to perform batch inference" is the plain version: load the registered model as a Python function with `mlflow.pyfunc.load_model`, then call `predict` on a pandas DataFrame. MLflow's `pyfunc` flavor is the generic loader that works for any logged model flavor.

**[📖 Log, load and register MLflow models](https://docs.databricks.com/aws/en/mlflow/models)** - `load_model`, `predict` and `spark_udf`

```python
# Run locally (MLflow 3.18.0): a logged scikit-learn model, loaded as a pyfunc and scored on a pandas DataFrame
m = mlflow.pyfunc.load_model(uri)          # on Databricks: "models:/catalog.schema.model@champion"
pred = m.predict(df)
print("pandas batch:", pred.shape, np.round(pred[:3], 2))
```

```
pandas batch: (100,) [-28.6   -4.29 -81.69]
```

When the data is too big for one machine, the same model becomes a Spark UDF with `mlflow.pyfunc.spark_udf` and the scoring runs distributed across the cluster. The docs example is `model_udf = mlflow.pyfunc.spark_udf(spark, model_path)` followed by `input_data.withColumn("prediction", model_udf())`. I ran the same pattern in local Spark; the prediction column matches the pandas predictions row for row (for example -28.5989 for the first row, -28.6 above):

```
|                 f0|                 f1|                 f2|         prediction|
|-1.0930615087305058|-1.4912575927056055| 0.3960067126616453|-28.598888203301765|
|  -0.65240858238702|-0.3909533751876011|0.39009332268792646|  -4.29447837152718|
```

For custom models on serving endpoints, the lifecycle page also lists `ai_query` as an efficient batch option. Databricks documents these batch tools: `ai_query`, Spark UDFs and `mlflow.pyfunc`.

- **mlflow.pyfunc.load_model** - the MLflow call that loads any logged model as a generic Python function with a `predict` method.
- **mlflow.pyfunc.spark_udf** - the MLflow call that wraps a logged model as a Spark UDF so it can score a Spark DataFrame on a cluster, in batch or streaming.

## Streaming inference with Delta Live Tables

A streaming job scores records as they land. The same Spark UDF works on a streaming DataFrame; I ran it against Spark's built-in `rate` source (5 rows a second for about 8 seconds) and it scored 35 rows:

```
streamed rows scored: 35
```

On Databricks the managed way to run this is a Delta Live Tables pipeline (the product is now named Lakeflow Spark Declarative Pipelines; the exam guide still says Delta Live Tables). The docs give three steps: get the MLflow model's run ID and model name to form the model URI, define a Spark UDF from that URI, and call the UDF in your table definition. One gotcha: "Pipelines do not install MLflow by default", so you must install the MLflow library in the pipeline yourself.

**[📖 Transform data with pipelines](https://docs.databricks.com/en/delta-live-tables/transform.html)** - The "Use MLflow models in pipelines" section

```python
# Not run here: needs a Databricks pipeline (core line from the Databricks docs)
loaded_model_udf = mlflow.pyfunc.spark_udf(spark, model_uri=model_uri)
# then use loaded_model_udf(...) inside a table definition in the pipeline
```

Why DLT rather than a plain Structured Streaming job in the guide's sample question? The pipeline is managed: it handles compute and can resize it as event volume changes, which is the requirement in the scenario (tens of thousands of events per second, fluctuating through the day). Applying the model as a UDF inside the pipeline also avoids a network hop to a serving endpoint for every event. Both of these reasons come from the guide's own answer explanation, not from a separate docs page, so treat the autoscaling claim as the exam's framing and check the pipelines docs for your runtime.

- **Delta Live Tables** - the Databricks declarative pipeline framework (now Lakeflow Spark Declarative Pipelines) for managed batch and streaming data pipelines, including model inference through a Spark UDF.
- **Structured Streaming** - Spark's streaming engine, which scores arriving records with the same DataFrame operations and UDFs as batch.

## Deploying a custom model to a model endpoint

Databricks Model Serving is the managed real-time option. The docs describe it as "highly available and low-latency", with endpoints that scale up or down with demand on serverless compute; each served model is a REST API. A *custom model* is a Python model in MLflow format (scikit-learn, XGBoost, PyTorch, Hugging Face transformers and so on) registered in Unity Catalog or the workspace registry.

**[📖 Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/)** - Capabilities and model types
**[📖 Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints)** - UI, REST API and SDK creation

You can create an endpoint in the Serving UI, with the REST API, or with the MLflow Deployments SDK. The shape of the request names a *served entity* (a Unity Catalog model and version), plus optional concurrency and scale-to-zero settings:

```python
# Not run here: needs a Databricks workspace (from the Databricks docs)
import mlflow
from mlflow.deployments import get_deploy_client
mlflow.set_registry_uri("databricks-uc")
client = get_deploy_client("databricks")
endpoint = client.create_endpoint(
    name="unity-catalog-model-endpoint",
    config={"served_entities": [{
        "name": "ads-entity",
        "entity_name": "catalog.schema.my-ads-model",
        "entity_version": "3",
        "min_provisioned_concurrency": 4,
        "max_provisioned_concurrency": 12,
        "scale_to_zero_enabled": False}]})
```

Permissions matter: the endpoint creator needs `USE CATALOG`, `USE SCHEMA` and `EXECUTE` on the Unity Catalog model. Scale to zero saves money when idle, but the docs say it is not recommended for production endpoints because capacity is not guaranteed and scaling back up adds a cold-start delay. While you update an endpoint, the old configuration keeps serving traffic until the new one is ready.

- **Served entity** - the model (a Unity Catalog model name and version) that a Model Serving endpoint serves, with its compute settings.
- **Scale to zero** - an endpoint setting that releases compute when idle; not recommended for production because capacity is not guaranteed and the first request is slow.

## Querying a model for real-time inference

You can query a custom model endpoint from the Serving UI, the `ai_query` SQL function, the REST API or the MLflow Deployments SDK. The request is a JSON payload, and for tabular models the docs recommend `dataframe_split`; `dataframe_records` does not guarantee column order, and the tensor formats are `instances` and `inputs`. The response is JSON with the output under `predictions`. Production clients should use machine-to-machine OAuth tokens.

**[📖 Query serving endpoints for custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-custom-model-endpoints)** - Input formats, REST and SDK examples

```python
# Not run here: needs a live endpoint (from the Databricks docs)
import mlflow.deployments
client = mlflow.deployments.get_deploy_client("databricks")
response = client.predict(
    endpoint="test-model-endpoint",
    inputs={"dataframe_split": {
        "index": [0, 1],
        "columns": ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
        "data": [[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2]]}})
```

- **dataframe_split** - the recommended JSON input format for tabular models, a pandas DataFrame in split orientation with `columns` and `data`.
- **ai_query** - a Databricks SQL function that calls a Model Serving endpoint from a query, used for batch scoring and in pipelines.

## Splitting data between endpoints

"Split data between endpoints for real-time inference" is the A/B-test or canary pattern. In Databricks you do not need two endpoints for it: one endpoint can serve several models, and `traffic_config` routes a percentage of requests to each served entity. The docs example gives 90 percent to a model named `current` and 10 percent to a `challenger`:

**[📖 Serve multiple models to a Model Serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/serve-multiple-models-to-serving-endpoint)** - Traffic split between served entities

```json
"traffic_config": {
  "routes": [
    { "served_model_name": "current", "traffic_percentage": "90" },
    { "served_model_name": "challenger", "traffic_percentage": "10" }
  ]
}
```

Rules from the same page: you cannot serve different model types on one endpoint (a custom model and an external model cannot share it); you change the split later by sending a `PUT` to `/api/2.0/serving-endpoints/{name}/config` with the new `traffic_config` (or in the UI); and querying a served model directly through its own `/served-models/{name}/invocations` URL ignores the traffic settings. This connects to Section 1: the model with the `challenger` alias is a natural candidate for the small slice of traffic, and once it proves itself you promote it to `champion`.

- **traffic_config** - the endpoint setting that lists routes, each pairing a served model name with a traffic percentage.
- **Traffic split** - sending a chosen share of requests to each model behind one endpoint, used for A/B tests and gradual rollouts.

## Check yourself against the objectives

State the one-line rule for choosing batch, real time or streaming; show where pandas scoring stops and `spark_udf` begins; explain why a pipeline-managed streaming job fits fluctuating event volume; list the ways to create and to query a custom model endpoint; and write the shape of a 90/10 traffic split. Questions for this section are in the [Databricks ML Associate bank](../../../practice-questions/databricks-ml-associate.md).
