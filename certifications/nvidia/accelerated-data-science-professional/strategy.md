# NCP-ADS Accelerated Data Science Professional Study Strategy

## Study Approach

### Phase 1: Foundation (1-2 weeks)
1. **RAPIDS Ecosystem** - Components, installation, CPU equivalents
2. **cuDF** - Data loading, transformations, pandas differences
3. **cuML** - Algorithms, API patterns, model evaluation
- **[📖 RAPIDS Docs (now docs.nvidia.com/datascience)](https://docs.nvidia.com/datascience/)**

### Phase 2: Advanced (2-3 weeks)
1. **cuGraph** - Graph construction, algorithms, integration with cuDF
2. **Dask-cuDF** - Multi-GPU scaling patterns
3. **cuDF plugin for Apache Spark** (formerly the RAPIDS Accelerator for Apache Spark, often called Spark RAPIDS) - Configuration, supported operations, tuning
- **[📖 cuDF plugin for Apache Spark Docs](https://docs.nvidia.com/cudf-spark/latest/)**

### Phase 3: Exam Prep (1-2 weeks)
1. Practice code-based questions
2. Review API patterns and algorithm selection
3. Focus on performance optimization scenarios

## Recommended Resources
- **[RAPIDS Documentation](https://docs.nvidia.com/datascience/)** - Complete reference (moved from docs.rapids.ai to docs.nvidia.com)
- **[cuDF API](https://docs.nvidia.com/cudf/latest/)** - DataFrame reference
- **[cuML API](https://docs.nvidia.com/cuml/latest/)** - ML algorithm reference
- **[cuGraph API](https://docs.nvidia.com/cugraph/latest/)** - Graph analytics reference
- **[cuDF plugin for Apache Spark](https://docs.nvidia.com/cudf-spark/latest/)** - Spark integration
- **[NVIDIA DLI Courses](https://www.nvidia.com/en-us/training/)** - Official training
- **[RAPIDS GitHub](https://github.com/rapidsai)** - Source code and examples

## Exam Tactics

### Keywords
- "DataFrame" or "tabular" - cuDF
- "Classification/clustering/regression" - cuML
- "Graph" or "network" - cuGraph
- "Large dataset" or "multi-GPU" - Dask-cuDF
- "Spark" or "existing pipeline" - cuDF plugin for Spark (the exam may still say RAPIDS Accelerator)
- "Memory" - RMM, managed memory, chunking
- "Fastest format" - Parquet

### Common Pitfalls
- cuDF is not 100% pandas-compatible - custom .apply() needs Numba
- cuML API mirrors scikit-learn but input should be cuDF/cuPy
- cuGraph requires integer vertex IDs for best performance
- Dask-cuDF operations are lazy - need .compute() to execute
- The cuDF plugin for Spark is a plugin, not a code rewrite
- Parquet is always faster than CSV for GPU loading

## Self-Assessment Questions
- Can I map each data science task to the correct RAPIDS component?
- Do I know cuDF API for loading, filtering, groupby, and merge?
- Can I select the right cuML algorithm for a given problem?
- Do I understand cuGraph construction and key algorithms?
- Can I configure the cuDF plugin for Spark for GPU acceleration?
- Do I know when to use cuDF vs Dask-cuDF vs the cuDF plugin for Spark?
