---
last-updated: 2026-10-22
difficulty: advanced
---

# NVIDIA Certified Professional - Accelerated Data Science (NCP-ADS) - Practice Questions

30 questions for NCP-ADS prep across the RAPIDS ecosystem: cuDF, cuML, cuGraph, GPU ETL with Spark and Dask, and performance work.

> **Cert page:** [exams/nvidia/accelerated-data-science-professional/](../nvidia/accelerated-data-science-professional/README.md)

---

### Question 1
**Scenario:** Which RAPIDS library provides a pandas-like DataFrame API on the GPU?

A. cuDF
B. cuML, the GPU library that mirrors scikit-learn estimators such as random forests and k-means
C. cuGraph, the GPU library for graph analytics such as PageRank
D. cuSpatial, the GPU library for geospatial and trajectory computations

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** cuDF mirrors the pandas API for GPU dataframes. cuML mirrors scikit-learn for machine learning, cuGraph handles graph analytics with a NetworkX-like surface, and cuSpatial covers geospatial operations. Knowing the mapping from CPU library to RAPIDS equivalent is core NCP-ADS material.
</details>

---

### Question 2
**Scenario:** An existing pandas script must be accelerated with minimal code change.

A. Convert to NumPy
B. Use `cudf.pandas` accelerator mode, which intercepts pandas calls and runs supported operations on the GPU with CPU fallback
C. Rewrite it in CUDA C++
D. Increase the CPU count

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The pandas accelerator lets unmodified code run on the GPU where operations are supported and fall back transparently where they are not, which removes the porting cost from the decision. Watch the fallback rate, because heavy fallback means you are paying transfer costs for little benefit.
</details>

---

### Question 3
**Scenario:** A dataset is larger than a single GPU's memory.

A. Downsample the data to a random 10 percent sample so that it fits in one GPU's memory, then treat the result as final
B. Switch to pandas
C. It cannot be processed
D. Use Dask-cuDF to partition across multiple GPUs or process in chunks, with out-of-core spilling where supported

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Dask-cuDF partitions the frame across workers so aggregate GPU memory becomes the ceiling, and unified virtual memory or spilling handles overflow at a performance cost. Downsampling changes the analysis rather than scaling it.
</details>

---

### Question 4
**Scenario:** A GPU pipeline is slower than the CPU version for a small dataset.

A. Fixed overheads (kernel launch, host-to-device transfer) dominate for small data; GPUs win once the work per transfer is large enough
B. Use more GPUs
C. cuDF is broken
D. The GPU is faulty

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Acceleration is a throughput story, so there is a crossover point below which the transfer and launch overhead exceeds the compute saved. Keeping data resident on the GPU across the whole pipeline, rather than bouncing to host between steps, is what moves that crossover in your favor.
</details>

---

### Question 5
**Scenario:** Which format should be read for the fastest GPU ingestion of columnar data?

A. JSON, since it is human-readable and parses quickly because every record is self-describing
B. CSV
C. Parquet, read with cuDF (optionally via GPUDirect Storage)
D. XML

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Parquet is columnar, compressed, and carries a schema, so only the needed columns are read and parsing is cheap. CSV parsing is expensive and type inference is error-prone, and row-oriented text formats waste bandwidth on columns you never use.
</details>

---

### Question 6
**Scenario:** cuML's `RandomForestClassifier` results differ slightly from scikit-learn's.

A. cuML is incorrect and should not be used for any model until it matches scikit-learn exactly on every run
B. Use CPU only
C. Implementation and floating-point ordering differences cause small variation; compare metrics
D. The data was corrupted when it was copied to the GPU, so the dataset has to be reloaded and retrained

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Parallel reductions do not sum in a fixed order, and algorithmic details differ between implementations, so bit-identical results are not the goal. Compare accuracy, AUC, or RMSE within a tolerance, which is the right acceptance test for a port anyway.
</details>

---

### Question 7
**Scenario:** Apache Spark jobs should use GPUs for SQL and dataframe operations.

A. Rewrite everything in cuDF so that Spark is no longer needed, then run the job as a plain Python script
B. The RAPIDS Accelerator for Apache Spark, which offloads supported operations to the GPU
C. Use Spark Streaming
D. Increase executor memory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The plugin intercepts the physical plan and replaces supported operators with GPU versions, falling back to CPU otherwise, so existing Spark SQL runs unchanged. Reading the explain output to see which stages actually ran on GPU is the standard tuning step.
</details>

---

### Question 8
**Scenario:** A graph analytics job must compute PageRank over 500 million edges.

A. A SQL query
B. cuGraph, optionally multi-GPU, using its GPU PageRank implementation
C. NetworkX on CPU, which handles graphs of this size well because its PageRank is multithreaded
D. Manual iteration in Python, one vertex at a time, over an adjacency list in memory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** cuGraph implements the standard graph algorithms on GPU with an interface close to NetworkX, and multi-GPU support extends it beyond a single device's memory. NetworkX is pure Python and does not reach this scale in practical time.
</details>

---

### Question 9
**Scenario:** A cuML model trained on GPU must be served in a CPU-only environment.

A. Export to ONNX or a Treelite model, or use a CPU inference library
B. Pickle the cuML model and load it in plain scikit-learn on the CPU host, which reads cuML pickles natively
C. It is impossible because GPU-trained cuML models use a binary format that no CPU-side library can read, so GPU hosts are required
D. Ship a GPU workstation to the site and run the model there instead of on CPUs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Training and inference hardware do not have to match. Forest models can be exported for CPU inference, and ONNX covers many other model types. Forest Inference Library is the reverse case: CPU-trained tree ensembles served fast on GPU.
</details>

---

### Question 10
**Scenario:** GPU memory fills during a long chain of cuDF operations.

A. Use smaller data types only, converting every column to int8 or float16 and leaving the memory pool settings and cached intermediates alone
B. Manage the RMM memory pool, delete intermediate frames, and drop references to intermediates
C. Add more CPUs
D. Restart the kernel after every single step, then reload all of the data from disk before the next operation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RAPIDS Memory Manager pools allocations to avoid the cost of repeated cudaMalloc, and configuring the pool is standard practice. The Python-side cause is usually intermediate frames still referenced by a notebook variable or output cell, so they are never freed.
</details>

---

### Question 11
**Scenario:** A feature engineering step uses a Python UDF applied row by row and is slow.

A. Keep the loop, because Python UDFs on cuDF automatically compile to GPU kernels with no performance penalty at any scale
B. Use pandas instead
C. Add more GPUs
D. Vectorize with cuDF column operations, or write a numba CUDA kernel if the logic cannot be expressed with them

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Row-wise Python defeats the parallelism entirely. Column operations run as GPU kernels over the whole array, and numba lets you compile custom element-wise logic when the built-in operations do not cover it.
</details>

---

### Question 12
**Scenario:** Which cuML algorithm family benefits most dramatically from GPU acceleration?

A. Compute-heavy algorithms over large data: k-nearest neighbors, DBSCAN, UMAP and t-SNE
B. String concatenation
C. Simple counting of rows in a table, which a single CPU thread already finishes in milliseconds
D. A single small decision tree trained on a few thousand rows, where kernel launch and transfer overhead dominate the run

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Algorithms dominated by pairwise distance computation or many independent tree builds map extremely well onto thousands of cores, which is where the largest speedups appear. Trivially cheap operations are dominated by overhead, which is question 4 again.
</details>

---

### Question 13
**Scenario:** Reproducibility is required across runs of a GPU pipeline.

A. Run on CPU only
B. Disable parallelism
C. Set random seeds, pin library and container versions, and accept documented floating-point tolerance where parallel reduction order varies
D. Reproducibility is impossible on GPU

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Seeds and pinned environments give reproducible pipelines; what you cannot generally promise is bit-identical floating-point results, because reduction order varies with scheduling. Stating the tolerance up front avoids arguments later about whether a difference is a bug.
</details>

---

### Question 14
**Scenario:** A profiling exercise must show where a RAPIDS pipeline spends its time.

A. Count the lines of code in each stage and assume that the stage with the most code is the slowest one
B. Read the GPU temperature and fan speed from nvidia-smi while the full script runs, then compare runs
C. NVTX ranges in Nsight Systems plus per-stage timing, separating transfer, compute and CPU work
D. Wall-clock timing of the whole script with time.time(), which shows the total runtime but not which stage is slow

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A total runtime number does not distinguish a slow kernel from a pipeline stalled on host-to-device copies or on Python. NVTX ranges make your own stages visible in the Nsight timeline alongside CUDA activity, which is what localizes the cost.
</details>

---

### Question 15
**Scenario:** Which describes the ideal RAPIDS pipeline shape?

A. Move data between host and device at every step, so that each stage can use whichever library it prefers
B. Convert the frames to pandas between steps so that each stage can use the CPU libraries the team knows
C. Use the GPU only for the model training step, and run all of the ETL and feature engineering on the CPU
D. Read straight into GPU memory, keep data resident through all stages, and copy out the result

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Each host-device round trip costs PCIe bandwidth and synchronization, so a pipeline that bounces between cuDF and pandas can spend more time transferring than computing. Keeping data resident end to end is the single largest architectural lever in accelerated data science.
</details>

---

### Question 16
**Scenario:** A notebook runs under `cudf.pandas`, yet a few cells are barely faster than plain pandas. The team wants to know which pandas calls are not running on the GPU.

A. Rewrite every cell with `import cudf` directly, since `cudf.pandas` never reports where an operation ran
B. Run the slow cells with `%%cudf.pandas.profile` to see which calls fell back to CPU pandas
C. Set the pandas option `compute.use_gpu` to true so that every remaining operation is forced onto the GPU
D. Restart the kernel with more GPU memory, because a fallback to CPU only happens when the GPU runs out of memory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `cudf.pandas` runs operations on the GPU when cuDF supports them and transparently falls back to pandas on the CPU when it does not, and the profiler reports which calls took which path. Rewriting everything by hand throws away the zero-code-change benefit before you know where the problem is. There is no pandas option that forces GPU execution, and fallback is usually caused by an unsupported operation, not by memory pressure.

**Key Concept:** [cudf.pandas](https://docs.nvidia.com/cudf/latest/cudf_pandas/)
</details>

---

### Question 17
**Scenario:** An analytics team writes its pipelines as Polars lazy queries and wants GPU acceleration without rewriting them in another API.

A. Convert each LazyFrame to a cuDF DataFrame with `cudf.from_polars()` before any filter or join runs
B. Run the script with `python -m cudf.pandas`, which also intercepts Polars calls and moves them to the GPU
C. Install the GPU engine and call `.collect(engine="gpu")`, which falls back to CPU for unsupported queries
D. Replace the lazy queries with Spark SQL, because Polars has no GPU execution path in the RAPIDS ecosystem

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Polars GPU engine is built on cuDF and is selected at collect time, so existing lazy queries run on the GPU and fall back to the CPU engine for anything the GPU engine does not support. `cudf.pandas` accelerates the pandas API, not Polars, and there is no `cudf.from_polars` conversion step in the documented workflow. Moving to Spark is a rewrite, not an acceleration.

**Key Concept:** [Polars GPU engine](https://docs.nvidia.com/cudf/latest/cudf_polars/)
</details>

---

### Question 18
**Scenario:** A data scientist has a working scikit-learn training script with UMAP and HDBSCAN steps and wants to test GPU speedups without editing the script.

A. Run it as `python -m cuml.accel train.py`, which swaps in cuML where supported and falls back otherwise
B. Change every `from sklearn` import to `from cuml` and fix any estimator that has a different signature
C. Set `n_jobs=-1` on each estimator, which offloads the scikit-learn work to every GPU on the node
D. Wrap the script in `dask_cuda.LocalCUDACluster`, which moves scikit-learn estimators to the GPU automatically

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `cuml.accel` is cuML's zero-code-change mode: it intercepts scikit-learn, UMAP and HDBSCAN calls, runs supported estimators on the GPU and transparently falls back to the CPU implementation for the rest. Editing imports works but is the opposite of "without editing the script". `n_jobs` controls CPU parallelism, and a Dask CUDA cluster does not change which library an estimator comes from.

**Key Concept:** [cuml.accel overview](https://docs.nvidia.com/cuml/latest/cuml-accel/)
</details>

---

### Question 19
**Scenario:** A fraud team has thousands of lines of NetworkX code computing betweenness centrality and wants it on the GPU with no change to the code or imports.

A. Convert each graph with `cugraph.from_networkx()` and call the cuGraph function by its new name
B. Rebuild the graphs in cuDF edge lists, since NetworkX graphs cannot be passed to any GPU backend
C. Install a GPU build of NetworkX, which replaces the pure-Python package and runs every algorithm on CUDA
D. Install nx-cugraph and set `NX_CUGRAPH_AUTOCONFIG=True` so that NetworkX dispatches to the GPU backend

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** nx-cugraph is a NetworkX backend: NetworkX dispatches supported algorithms to it, and the environment variable turns that on without touching imports or calls. Converting graphs and calling cuGraph directly works but is a code change. There is no separate GPU build of NetworkX, and NetworkX graphs do not need to be rebuilt by hand to use the backend.

**Key Concept:** [nx-cugraph](https://docs.nvidia.com/cugraph/latest/nx_cugraph/)
</details>

---

### Question 20
**Scenario:** A platform team runs 400 Spark jobs on CPU clusters and must decide which ones are worth moving to GPUs before buying hardware.

A. Move all 400 jobs to a GPU cluster for a week and compare the monthly cloud bill with the previous month
B. Pick the jobs with the largest input size, since data volume alone decides whether a GPU helps a Spark job
C. Run the Qualification tool on the CPU jobs' event logs to estimate which ones are likely to speed up
D. Run the Profiling tool on the CPU event logs, because it is the tool that ranks jobs for GPU migration

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Qualification tool reads event logs from CPU runs and estimates which applications are good candidates for GPU acceleration, which is exactly the pre-purchase question. Input size alone ignores unsupported operators and shuffle patterns, and a blind week-long migration is expensive. The Profiling tool analyzes and tunes jobs that already ran on GPUs.

**Key Concept:** [Qualification tool overview](https://docs.nvidia.com/cudf-spark/latest/qualification/overview.html)
</details>

---

### Question 21
**Scenario:** After enabling the cuDF plugin for Apache Spark (formerly the RAPIDS Accelerator), a query is only slightly faster. The engineer suspects some operators are still running on the CPU.

A. Set `spark.rapids.sql.enabled=false` and compare, since the plugin logs nothing about where operators run
B. Set `spark.rapids.sql.explain=NOT_ON_GPU` and read the driver log for the operators that stayed on CPU
C. Increase `spark.executor.cores`, because operators fall back to CPU only when there are too few cores
D. Disable adaptive query execution, because AQE always forces every operator back to the CPU path

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The plugin can explain its placement decisions, and `NOT_ON_GPU` logs just the parts of the plan that could not be placed on the GPU and why, which points at the expressions or data types to change. Disabling the plugin tells you the total speedup but not where it was lost. CPU core count does not drive placement, and the plugin supports adaptive query execution.

**Key Concept:** [cuDF plugin for Apache Spark user guide](https://docs.nvidia.com/cudf-spark/latest/index.html)
</details>

---

### Question 22
**Scenario:** A cuDF workload creates and frees thousands of small intermediate columns, and profiling shows a large share of time in CUDA memory allocation calls.

A. Call `gc.collect()` after every operation so Python frees GPU memory sooner
B. Convert every column to `float64` so that each allocation is the same size
C. Move the intermediate columns to host memory with `.to_pandas()` between steps
D. Initialize an RMM pool allocator so that allocations come from a pre-reserved pool

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** RAPIDS Memory Manager (RMM) provides a pool memory resource that reserves GPU memory up front and sub-allocates from it, removing the cost of repeated `cudaMalloc` and `cudaFree` calls. Forcing garbage collection adds overhead without changing the allocator. Widening data types uses more memory, and copying to host memory adds PCIe transfers that are slower than the allocations.

**Key Concept:** [RAPIDS Memory Manager (RMM)](https://docs.nvidia.com/rmm/latest/)
</details>

---

### Question 23
**Scenario:** Features prepared in cuDF must be handed to a PyTorch model on the same GPU, and the team wants to avoid copying the data through host memory.

A. Pass the data through DLPack or the CUDA array interface, which share device memory without a host copy
B. Write the DataFrame to Parquet and read it back with PyTorch, because GPU libraries cannot share buffers
C. Call `.to_pandas()` and then `torch.tensor()`, since PyTorch accepts only host-resident NumPy arrays
D. Serialize the columns with pickle and load them in PyTorch, which keeps the buffers on the device

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RAPIDS libraries support standard GPU interchange protocols such as DLPack and `__cuda_array_interface__`, so a tensor can be built over the same device memory without a round trip. Writing files and converting to pandas both move the data through the host. Pickling does not create a shared device view.

**Key Concept:** [cuDF interoperability](https://docs.nvidia.com/cudf/latest/)
</details>

---

### Question 24
**Scenario:** A k-means model must be trained on a dataset spread across all four GPUs of one node, using cuML.

A. Train one single-GPU model per GPU on a quarter of the data and average the four sets of centroids
B. Set `CUDA_VISIBLE_DEVICES=0,1,2,3`, which makes single-GPU cuML estimators span every listed GPU
C. Start a `LocalCUDACluster` with Dask-CUDA and use the multi-node, multi-GPU estimators in `cuml.dask`
D. Use the scikit-learn estimator with `n_jobs=4`, which assigns one partition to each of the four GPUs

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Dask-CUDA starts one worker per GPU, and the `cuml.dask` estimators train one model across the distributed partitions. Averaging independently trained centroids is not equivalent to k-means on the full data. Making devices visible does not make a single-GPU estimator multi-GPU, and scikit-learn's `n_jobs` is CPU parallelism.

**Key Concept:** [Dask-CUDA](https://docs.nvidia.com/dask-cuda/latest/)
</details>

---

### Question 25
**Scenario:** A 300-million-row cuDF table has a `country` string column with about 200 distinct values, and it takes a large share of GPU memory.

A. Split the table into one file per country and load each file only when a query needs it
B. Store the column as a Python object dtype, which keeps the strings in host memory instead
C. Hash each country name into a 64-bit integer and drop the original column from the table
D. Convert the column to the `category` dtype so each row stores a small code into a dictionary

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Low-cardinality strings are a textbook case for categorical encoding: the distinct values are stored once and each row holds a small integer code, which cuts memory sharply and speeds up group-bys and joins. Splitting files changes the workload, not the representation. cuDF does not keep object columns in host memory, and hashing loses the readable values and risks collisions.

**Key Concept:** [cuDF user guide](https://docs.nvidia.com/cudf/latest/cudf/)
</details>

---

### Question 26
**Scenario:** A gradient-boosted tree model trained with XGBoost on a 50-million-row table must use the GPU.

A. Install cuML, since XGBoost has no GPU support and cuML provides the only GPU tree booster
B. Set `device="cuda"` with the `hist` tree method so that XGBoost trains on the GPU
C. Set `nthread` to the number of GPU streaming multiprocessors so the CPU booster is offloaded
D. Wrap the training call in `cudf.pandas`, which redirects XGBoost to the GPU through pandas

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Current XGBoost selects GPU training through the `device` parameter, and its histogram tree method runs on CUDA; it also accepts cuDF and CuPy inputs directly. XGBoost has had GPU support for years. `nthread` controls CPU threads, and `cudf.pandas` accelerates pandas calls, not the XGBoost booster.

**Key Concept:** [XGBoost GPU support](https://xgboost.readthedocs.io/en/stable/gpu/index.html)
</details>

---

### Question 27
**Scenario:** A new workstation has a recent NVIDIA driver, and a developer installs RAPIDS with pip. Imports fail with CUDA errors.

A. Install the RAPIDS wheels built for the CUDA major version that the installed driver supports
B. Downgrade the driver to the oldest version listed, because RAPIDS only supports legacy drivers
C. Install the CUDA toolkit from source, since pip wheels never include the CUDA runtime libraries
D. Install the CPU-only pandas and scikit-learn first, because RAPIDS wheels require them as GPU drivers

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RAPIDS publishes wheels per CUDA major version (package names carry a suffix such as `-cu12`), and the wheel must match a CUDA version the driver supports. The NGC RAPIDS container avoids the issue entirely. Downgrading to the oldest driver is backwards, a source-built toolkit is unnecessary, and pandas is not a GPU driver.

**Key Concept:** [RAPIDS installation guide](https://docs.rapids.ai/install/)
</details>

---

### Question 28
**Scenario:** Community detection on a large customer graph returned some communities that are internally disconnected, and analysts want every community to be well connected.

A. Run PageRank and group the vertices by score
B. Run weakly connected components on the whole graph
C. Run Louvain again with a different random seed
D. Run Leiden, which guarantees connected communities

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Leiden refines Louvain's partitions so every community is guaranteed to be connected, which is the defect described, and cuGraph provides it on the GPU. Rerunning Louvain with another seed can still produce disconnected communities. PageRank measures importance, not community membership, and connected components only finds pieces with no links between them.

**Key Concept:** [cuGraph documentation](https://docs.nvidia.com/cugraph/latest/)
</details>

---

### Question 29
**Scenario:** A Spark job already runs on GPUs with the cuDF plugin, but executors sit idle at times and the team does not know which settings to change.

A. Run the Qualification tool again, since it produces the tuning settings for jobs that already run on GPUs
B. Raise `spark.sql.shuffle.partitions` to 10,000, because more partitions always keep each GPU busy
C. Run the Profiling tool on the GPU event logs and apply the AutoTuner's recommended settings
D. Set `spark.task.resource.gpu.amount` to 1.0 so that only one task at a time can use each GPU

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Profiling tool analyzes GPU runs and its AutoTuner recommends settings such as concurrent GPU tasks, partition counts and memory, grounded in what the job actually did. Qualification is for CPU jobs being considered for migration. A huge partition count adds scheduling overhead, and allowing only one task per GPU usually lowers utilization.

**Key Concept:** [cuDF plugin for Apache Spark user guide](https://docs.nvidia.com/cudf-spark/latest/index.html)
</details>

---

### Question 30
**Scenario:** cuML predictions feed a plotting library that accepts only NumPy arrays, and the code breaks because cuML returns device arrays.

A. Retrain the model on pandas data, since cuML always returns the same type that the training data had
B. Set cuML's output type to `numpy`, globally or per estimator, so that results come back as host arrays
C. Disable the GPU for prediction only, because cuML can only return NumPy arrays when it runs on CPU
D. Patch the plotting library to read CUDA device memory, because cuML has no option for output types

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** cuML lets you set the output type globally or per estimator, so predictions can be returned as NumPy arrays where downstream code needs them. By default cuML mirrors the input type of each call, so the fix is configuration, not retraining. Turning off the GPU throws away the speedup, and patching a third-party library is unnecessary.

**Key Concept:** [cuML documentation](https://docs.nvidia.com/cuml/latest/)
</details>

---

## Where to go deeper

- [NCP-ADS cert page](../nvidia/accelerated-data-science-professional/README.md) - notes, practice plan, strategy
- [NCP-AII practice questions](nvidia-ai-infrastructure-professional.md) - the infrastructure underneath
- [GPUs for AI](../../learn/concepts/gpus-for-ai.md) - why GPUs are fast at this
- [Databricks Data Engineer Associate practice questions](https://data.noblerworks.com/resources/practice-questions/databricks-data-engineer-associate/) - the Spark counterpart
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
