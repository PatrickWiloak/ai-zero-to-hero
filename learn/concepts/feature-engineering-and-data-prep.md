# Feature Engineering and Data Prep

**In one line:** Turn a messy table into model-ready columns (missing values, categories, scaling, dates), and avoid the leaks that make a model look great in testing and fail in production.
**Last reviewed:** 2026-11-07

---

## The short version

- A **feature** is one input column the model sees. **Feature engineering** is choosing, cleaning and creating those columns. On tabular problems it usually moves the score more than switching algorithms.
- Prep steps: handle missing values, encode categories as numbers, scale numeric columns if the model needs it, and extract signal from dates and text.
- Do every step inside a **pipeline** that is fitted on the training rows only, then applied unchanged to validation, test and live data.
- The deadliest error is **data leakage**: information from the future, or from the test set, reaching the model during training.
- Spend the first hour looking at the data. Counts, plots and a few raw rows find more problems than any library.

## Look before you prep

Before changing anything, check: how many rows and columns, the type of each column, how much is missing and where, how many distinct values each category has, and whether the label is balanced. In pandas, `df.info()`, `df.describe()` and `df["col"].value_counts()` answer most of it. Also ask what each row *is* (one customer? one order?), because mixing grains is a common silent bug. Cleaning pipelines at scale belong to data engineering: see [Data Zero to Hero](https://data.noblerworks.com/).

## Missing values

Options, from simplest:

- **Drop** rows or columns when very little is missing, or a column is mostly empty.
- **Impute**: fill numbers with the median (steadier than the mean when outliers exist) and categories with a constant such as "unknown".
- **Add a "was missing" flag.** Sometimes the absence itself is informative ("no phone number given").
- **Let the model cope.** Gradient-boosted trees such as scikit-learn's `HistGradientBoosting*` accept missing values directly. See [Decision trees and gradient boosting](decision-trees-and-gradient-boosting.md).

Find out *why* values are missing before choosing. Missing because "not applicable" and missing because "the form broke last March" mean different things.

## Categories

Models need numbers. Common encodings:

| Encoding | How | Use when |
|---|---|---|
| One-hot | One 0/1 column per value | Few distinct values (plan type, country group) |
| Ordinal | Map to 0, 1, 2 in a meaningful order | Natural order (small, medium, large) |
| Frequency or target encoding | Replace by how common it is, or by the average outcome | Many values (thousands of zip codes); target encoding must be fitted inside cross-validation or it leaks |
| Embedding | Learn a short vector per value | Neural models with high-cardinality IDs; see [Embeddings and vector search](embeddings-and-vector-search.md) |

Set `handle_unknown="ignore"` on the one-hot encoder so a category first seen in production does not crash the service.

## Numbers: scaling and shape

- **Scale** (standardise to mean 0, spread 1) for models that use distances or weights on raw values: logistic regression, k-nearest neighbours, support vector machines, neural networks. Tree models do not need it.
- **Skewed values** (income, prices, counts) often behave better after a log transform.
- **Outliers**: check whether they are errors (age 999) or real. Cap, fix or keep on purpose.
- **Binning** can help when the effect is stepwise (age bands), though trees find splits on their own.

## Dates and text

A raw timestamp means little to a model. Pull out parts: month, day of week, hour, "is weekend", "is holiday", days since signup, days until renewal. For text, an LLM embedding or classic TF-IDF turns it into numbers; for most modern text tasks an embedding model or an LLM is the better route: [Embeddings and vector search](embeddings-and-vector-search.md). For time-ordered data see [Time-series forecasting](time-series-forecasting.md).

## Creating new features

Domain knowledge beats cleverness. Ratios (spend per visit), counts and recency (orders in the last 30 days), differences (price minus competitor price) and flags ("used the feature in week one") often outperform raw columns. Create a few with a reason each, test whether the held-out score moves, and keep only what helps.

## A runnable example

This runs on a tiny table with a missing plan, a missing tenure and a date. It builds a single reusable preprocessing object:

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.DataFrame({
    "plan": ["basic", "pro", "basic", None, "pro"],
    "tenure_months": [3, 24, np.nan, 12, 40],
    "signup": pd.to_datetime(["2026-01-05", "2024-03-20", "2026-02-11", "2025-06-01", "2023-09-15"]),
})
df["signup_month"] = df["signup"].dt.month
df["signup_is_weekend"] = df["signup"].dt.day_of_week >= 5

prep = ColumnTransformer([
    ("num", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()), ["tenure_months"]),
    ("cat", make_pipeline(SimpleImputer(strategy="constant", fill_value="unknown"),
                          OneHotEncoder(handle_unknown="ignore")), ["plan"]),
])
out = prep.fit_transform(df)
print(prep.get_feature_names_out())
print(np.round(out.toarray() if hasattr(out, "toarray") else out, 2))
```

Output (scikit-learn 1.9.1, pandas 3.1.1, run 2026-11-07):

```
['num__tenure_months' 'cat__plan_basic' 'cat__plan_pro'
 'cat__plan_unknown']
[[-1.32  1.    0.    0.  ]
 [ 0.37  0.    1.    0.  ]
 [-0.11  1.    0.    0.  ]
 [-0.6   0.    0.    1.  ]
 [ 1.66  0.    1.    0.  ]]
```

The missing tenure became the median (12, then scaled), and the missing plan became its own "unknown" column. The date parts (`signup_month`, `signup_is_weekend`) were created but not passed to the transformer here; add them to the numeric or flag lists to use them. The key habit: `fit_transform` on training data, then only `transform` on anything else.

## Data leakage, the silent killer

Leakage means the model sees something at training time that it will not have at prediction time. Typical forms:

- **Target leakage.** A column produced by the outcome, such as "cancellation reason" when predicting cancellation.
- **Preprocessing leakage.** Scaling or imputing on the whole dataset before splitting, so test-set statistics leak into training. A pipeline fitted only on training folds prevents this.
- **Time leakage.** Random splits on time-ordered data.
- **Duplicate leakage.** The same customer in both train and test.

The tell is a score that looks too good. Treat a 0.99 on a hard business problem as a bug report until proven otherwise. See [Training, validation and overfitting](training-validation-and-overfitting.md).

## Common mistakes

- **Fitting preprocessing before the split.** Put it in a `Pipeline`.
- **One-hot encoding a column with 50,000 values.** Use frequency or target encoding, or an embedding.
- **Filling missing values with 0 when 0 means something.**
- **Hand-cleaning in a notebook and not recording it.** If the steps are not code in the pipeline, the live system will not repeat them.
- **Adding hundreds of features hoping one works.** Each one is another chance to leak or overfit.

## Next steps

- [Tabular ML end to end](../../build/projects/tabular-ml-end-to-end.md): a complete pipeline, evaluated and saved
- [Classic ML: supervised vs unsupervised](classic-ml-supervised-vs-unsupervised.md)
- [Decision trees and gradient boosting](decision-trees-and-gradient-boosting.md)
- [Time-series forecasting](time-series-forecasting.md)
- Warehouses, quality checks and feature stores: [Data Zero to Hero](https://data.noblerworks.com/)

## Sources

- scikit-learn user guide, "Preprocessing data": https://scikit-learn.org/stable/modules/preprocessing.html
- scikit-learn user guide, "Imputation of missing values": https://scikit-learn.org/stable/modules/impute.html
- scikit-learn user guide, "ColumnTransformer for heterogeneous data": https://scikit-learn.org/stable/modules/compose.html#column-transformer
- scikit-learn user guide, "Common pitfalls and recommended practices" (data leakage): https://scikit-learn.org/stable/common_pitfalls.html
- pandas documentation, "Working with missing data": https://pandas.pydata.org/docs/user_guide/missing_data.html
- Code in this page run locally on 2026-11-07 (scikit-learn 1.9.1, pandas 3.1.1).
