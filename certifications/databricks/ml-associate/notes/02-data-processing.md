# Section 2: Data Processing (19%)

**Last reviewed:** 2026-11-07

The exam page calls this section "ML Workflows" while the exam guide calls it "Data Processing"; the guide is the authority and the objectives below are copied from it, in its order. This is the section where plain data-science judgment is tested: which summary to run, how to define an outlier, what to do with missing values and categorical columns, and when a log transform is the right tool. The Databricks-specific parts are small (`dbutils.data.summarize`, Spark DataFrame methods and Spark ML's `Imputer` and `OneHotEncoder`).

Every number below comes from code I ran in a throwaway virtual environment: scikit-learn 1.9.1, pandas, and PySpark 4.3.0 in local mode (Databricks itself was not available). The Spark ML calls are the same ones the exam names.

**[📖 Exam guide (August 2026)](https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Machine-Learning-Associate-Exam-Guide-August-2026.pdf)** - The official Section 2 objectives

## Summary statistics on a Spark DataFrame

Before you change any data you look at it. On a Spark DataFrame there are two tools. `DataFrame.summary()` returns count, mean, stddev, min, the 25th, 50th and 75th percentiles, and max; you can pass your own list of statistics, for example `df.summary("count", "min", "50%", "max")`. In a Databricks notebook, `dbutils.data.summarize(df)` displays summary statistics and charts for a Spark or pandas DataFrame. The docs warn that it analyzes the complete contents of the DataFrame, so it can be expensive on a very large one, and that with the default `precise=False` some statistics (distinct counts on high-cardinality columns, histograms, percentiles) are approximate.

**[📖 dbutils.data.summarize](https://docs.databricks.com/aws/en/dev-tools/databricks-utils)** - Signature, behavior and accuracy limits of the data summary utility
**[📖 DataFrame.summary](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.summary.html)** - PySpark reference for summary()

Here is `summary()` on a small column with one suspicious value (eight rows, one null, one 200 among values around 10):

```
+-------+-----------------+
|summary|                x|
+-------+-----------------+
|  count|                7|
|   mean|37.92857142857143|
| stddev|71.47868480150136|
|    min|              9.0|
|    25%|             10.0|
|    50%|             11.0|
|    75%|             13.0|
|    max|            200.0|
+-------+-----------------+
```

Read it the way the exam wants you to. `count` is 7 for 8 rows, so one value is missing (counts skip nulls). The mean (37.9) is far above the median (11), and the max is 200 against a 75th percentile of 13: that gap is the signature of a right-skewed column with an outlier. A summary is how you find problems; the next objectives are how you fix them.

- **summary()** - a Spark DataFrame method that returns count, mean, stddev, min, quartiles and max for the columns it is called on, or the statistics you ask for.
- **dbutils.data.summarize** - the Databricks notebook utility that displays summary statistics and charts for a Spark or pandas DataFrame, with approximate results unless `precise=True`.

## Removing outliers: standard deviation and IQR

An outlier rule is a decision about what "far from normal" means, and the two standard rules answer differently.

- **Standard deviation rule:** drop values more than k standard deviations (commonly 3) from the mean. It assumes a roughly bell-shaped column, and it has a weakness: the outliers themselves inflate the mean and the standard deviation, so they can hide.
- **IQR rule:** compute Q1 and Q3, the IQR = Q3 - Q1, and drop values below Q1 - 1.5 x IQR or above Q3 + 1.5 x IQR. It is built from percentiles, which a few extreme values barely move, so it behaves better on skewed data.

I generated 200 values from a normal distribution centered on 50 with two injected extremes (120 and 130):

```
3-sd removed: 2
IQR removed: 5 fences 35.4 63.8
```

Both rules catch the two injected values. The IQR rule also removes three ordinary tail values, because on 200 normal points a 1.5 x IQR fence is tighter than 3 standard deviations. That is the trade-off to state in an answer: IQR is robust to the outliers it is hunting but more aggressive on clean bell curves; the standard deviation rule is gentle on clean data but can be fooled by heavy outliers.

In Spark you compute the quantiles with `df.approxQuantile("x", [0.25, 0.75], 0.0)` and filter the DataFrame. In the eight-row example the fences came out as 5.5 and 17.5, and filtering removed the row with 200 (8 rows became 7). Keep rows with a null in the filter if you plan to impute them, otherwise the comparison silently drops them.

- **Standard deviation rule** - an outlier rule that removes values more than a chosen number of standard deviations from the mean; it assumes roughly normal data and is distorted by the outliers it seeks.
- **IQR rule** - an outlier rule that removes values below Q1 minus 1.5 times the IQR or above Q3 plus 1.5 times the IQR; it is based on percentiles and is robust to skew.

## Visualizing and comparing features

The guide asks you to create visualizations for categorical or continuous features, and to compare two categorical or two continuous features "using the appropriate method". Pair the data type with the plot:

| Question | Feature types | Appropriate method |
|---|---|---|
| What is the distribution of one feature? | Continuous | Histogram or box plot (also shows outliers) |
| What is the distribution of one feature? | Categorical | Bar chart of counts |
| How do two continuous features relate? | Continuous vs continuous | Scatter plot and a correlation coefficient |
| How do two categorical features relate? | Categorical vs categorical | Cross-tabulation (contingency table) or stacked bar chart |

The table is general data-analysis practice, not a Databricks rule; what Databricks adds is `display(df)` with built-in chart types and the data profile view. The principle is the useful part: a correlation coefficient makes no sense for two categorical columns, and a bar chart hides the shape of a continuous one.

## Imputing missing values: mean, median or mode

Models cannot train on nulls, so you either drop rows or fill the gaps. Which fill is correct depends on the column.

- **Mean** suits a continuous column with a roughly symmetric distribution. It is pulled by extremes.
- **Median** suits a skewed continuous column or one with outliers, because it ignores them.
- **Mode** (the most frequent value) is the choice for categorical columns, where a mean has no meaning.

The difference is not academic. On an income-like column with a long right tail, I measured:

```
income mean 60961 median 38030
mean imputes 62204.0
median imputes 38731.0
mode of a categorical: red
```

Filling with the mean would put every missing person above the 75th-percentile earner in a typical case; the median stays where most real values are. This also explains the guide's sample question: scikit-learn's `SimpleImputer` does not auto-select a strategy from the data (you pass `strategy="mean"`, `"median"`, `"most_frequent"` or `"constant"`), so correct results require looking at the distribution first.

In Spark ML the transformer is `Imputer`; in my run, `Imputer(strategy="median", inputCols=["x"], outputCols=["x_i"])` filled the missing value in the example with 10.5, the median of the remaining values. Note that `Imputer` is an Estimator: it must `fit` to learn the median from training data and then `transform`, which is how you avoid computing the fill value from the test set.

- **Mean imputation** - filling missing numeric values with the column mean; suited to symmetric distributions and sensitive to outliers.
- **Median imputation** - filling missing numeric values with the column median; preferred for skewed data or data with outliers.
- **Mode imputation** - filling missing values with the most frequent value; the standard choice for categorical features.

## One-hot encoding

A model cannot use the string "red" directly, and mapping red, green, blue to 0, 1, 2 would tell a linear model that blue is twice green. One-hot encoding avoids that by creating one 0/1 column per category. In scikit-learn:

```
['c_a' 'c_b' 'c_c'] [[0.0, 1.0, 0.0], [0.0, 0.0, 0.0]]
```

The first line is the learned columns; the second encodes a known category `b` and an unseen category `z` (with `handle_unknown="ignore"`, all zeros).

In Spark ML you first convert strings to numeric indices with `StringIndexer`, then expand with `OneHotEncoder`, then combine columns with `VectorAssembler`. The docs list `StringIndexer`'s unseen-label strategies (throw an exception by default, skip the row, or put the label in an extra bucket) and `OneHotEncoder`'s `handleInvalid` options (`error` or `keep`).

**[📖 Extracting, transforming and selecting features](https://spark.apache.org/docs/latest/ml-features.html)** - StringIndexer, OneHotEncoder, Imputer and VectorAssembler reference

**When it is appropriate.** It suits nominal categories with no order and a modest number of levels, used by models that treat inputs as numbers on a scale: linear and logistic regression, neural networks, k-means. It is inappropriate or wasteful for:

- **High-cardinality columns** (thousands of zip codes or user ids): you create thousands of sparse columns. Use hashing, target encoding or embeddings.
- **Ordinal categories** (small, medium, large): the order carries information, so an ordered index preserves it and one-hot encoding throws it away.
- **Tree-based models** often do well on a plain integer index, since a tree can split the index at any point. Many tree libraries also handle categorical columns natively. This is general practice and the exam asks you to "identify and explain" it, so be ready to justify with the model type.

- **One-hot encoding** - turning a categorical feature into one binary column per category, so a numeric model does not read a false order into the values.
- **StringIndexer** - a Spark ML estimator that maps string labels to numeric indices (most frequent label first by default).
- **OneHotEncoder** - a Spark ML estimator that turns category indices into binary vectors, usually applied after StringIndexer.

## When a log scale transformation is appropriate

Use a log transform when a continuous feature or target is right-skewed and spans several orders of magnitude (prices, incomes, counts, durations), or when effects are multiplicative. Taking the log compresses the long tail so the distribution is more symmetric and so a linear model's errors are more even. It is not for features that are already roughly normal, not for categorical columns, and it is undefined for zero or negative values (people use `log1p` for zeros, but negatives still need a different approach).

Measured on a synthetic skewed target built as an exponential of a linear signal plus noise:

```
skew raw 1.57 log -0.01
```

The skewness of 1.57 drops to essentially zero after the log. That is what "more symmetric" means in numbers. The reverse step, which belongs to the next section, is that a model trained on the log scale predicts on the log scale and must be exponentiated before you judge it in original units.

- **Log transformation** - applying a logarithm to a right-skewed, strictly positive variable to compress large values and make its distribution closer to symmetric.
- **log1p** - the natural log of one plus the value, a common way to log-transform data that contains zeros.

## Check yourself against the objectives

Read a `summary()` and say what it implies about skew, nulls and outliers; choose the outlier rule and defend it; pick mean, median or mode from the column's type and shape; name the encoders in the Spark ML chain and say when one-hot is the wrong tool; and name the situation a log transform fits. Questions for this section are in the [Databricks ML Associate bank](../../../practice-questions/databricks-ml-associate.md).
