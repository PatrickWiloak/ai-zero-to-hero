---
last-updated: 2026-08-09
difficulty: advanced
---

# NVIDIA Certified Professional - Accelerated Data Science (NCP-ADS) - Practice Questions

15 questions for NCP-ADS prep across the RAPIDS ecosystem: cuDF, cuML, cuGraph, GPU ETL with Spark and Dask, and performance work.

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

## Where to go deeper

- [NCP-ADS cert page](../nvidia/accelerated-data-science-professional/README.md) - notes, practice plan, strategy
- [NCP-AII practice questions](nvidia-ai-infrastructure-professional.md) - the infrastructure underneath
- [GPUs for AI](../../learn/concepts/gpus-for-ai.md) - why GPUs are fast at this
- [Databricks Data Engineer Associate practice questions](https://data.noblerworks.com/resources/practice-questions/databricks-data-engineer-associate/) - the Spark counterpart
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
