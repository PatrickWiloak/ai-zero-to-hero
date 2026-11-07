# Time-Series Forecasting

**In one line:** Learn the parts of a time series, why you must split by time and never at random, and how to choose between a naive baseline, classic statistics, boosted trees and pretrained forecasting models.
**Last reviewed:** 2026-11-07

---

## The short version

- A **time series** is a measurement repeated over time: daily sales, hourly power use, weekly sign-ups. Order matters, and tomorrow depends on yesterday.
- Most series are some mix of **trend** (slow drift), **seasonality** (repeating cycles) and **noise**.
- Always beat a **naive baseline** first: "tomorrow equals today", or "next week equals the same week last year". Many fancy models fail to.
- Evaluate by **splitting on time**: train on the past, test on the future. A random split lets the model peek at the future and gives scores that collapse in production.
- Pick the simplest method that beats the baseline. Classic statistics (ETS, ARIMA), gradient-boosted trees on lag features and pretrained forecasting models each have a place.

## The parts of a series

| Part | Meaning | Example |
|---|---|---|
| Level | Where the series sits | About 200 orders a day |
| Trend | Long-run rise or fall | Growing 3% a month |
| Seasonality | Fixed-length repeats | Busier on Fridays, every December |
| Cycles | Irregular long swings | Economic booms and busts |
| Noise | Random leftover | A rainy day |
| Events | One-off shocks | A promotion, an outage |

Plot the series before anything else. Most problems (a gap, a unit change, a sudden step) are visible to the eye.

## Baselines you must beat

- **Naive**: the next value equals the last value.
- **Seasonal naive**: the next value equals the value one season ago (same weekday last week).
- **Moving average**: the mean of the last few values.

Hyndman and Athanasopoulos call these benchmark methods and use them to judge everything else. If your model cannot beat seasonal naive, you do not have a forecasting model yet.

## Methods, from simplest

1. **Exponential smoothing (ETS).** A weighted average where recent points count more, with optional trend and seasonal terms. Fast and hard to beat on a single, tidy series.
2. **ARIMA family.** Models a value from its own recent past and recent errors. Needs the series to be made stable first (differencing).
3. **Gradient boosting on lag features.** Turn the series into a table: columns for "value 1 day ago", "value 7 days ago", "rolling 7-day mean", "day of week", "is holiday". Then use any tabular model, such as [boosted trees](decision-trees-and-gradient-boosting.md). This handles many related series (thousands of products) and outside information (price, weather) well. See [Feature engineering and data prep](feature-engineering-and-data-prep.md).
4. **Deep learning and pretrained models.** Recurrent and transformer architectures, and foundation models pretrained on huge collections of series, can forecast a new series with no training on it ("zero-shot"). Treat them as another candidate in the bake-off, judged on your data against the baselines. Check each model's own documentation and licence.

The sequence-model lineage is explained in [Seq2seq](../../papers/architectures/55-seq2seq/summary.md) and [The unreasonable effectiveness of RNNs](../../papers/essays/109-unreasonable-effectiveness-of-rnns/summary.md).

## Splitting and testing correctly

Use **walk-forward** (rolling-origin) validation: train on data up to day N, forecast the next stretch, score it, then move the cut-off forward and repeat. scikit-learn's `TimeSeriesSplit` does this for tables, so each fold's training data comes strictly before its test data.

Three leaks to avoid:

- **Shuffled splits.** Never shuffle rows of a series.
- **Features from the future.** A "7-day centred average" uses days after the one you are predicting. Use only past windows.
- **Scaling on everything.** Fit scalers on the training period only.

Match the metric to the decision. **MAE** (mean absolute error) is easy to explain in the series' own units. **MAPE** (percentage error) breaks when actual values are near zero. **Forecast intervals** (a range, not a point) matter when you must hold stock or staff for the bad case.

## A worked picture

Suppose a shop sells about 100 units on weekdays and 160 on weekends. Seasonal naive forecasts next Saturday as last Saturday, say 158. A boosted model with price and holiday columns might say 171 for a holiday weekend. You compare both over the last twelve walk-forward folds. Whichever has the lower average error wins, and if the gap is small, ship the simpler one.

## Common mistakes

- **Random train/test split.** The most common, and it flatters every model.
- **Forecasting a number you cannot act on.** Decide the horizon (tomorrow? next quarter?) from the decision first.
- **Ignoring structural change.** A pandemic, a price change or a new product line breaks the old pattern. Retrain and monitor error over time.
- **Reporting one number.** Give a range and say how it was measured.
- **Using an LLM to do arithmetic on a table of numbers.** Use a forecasting tool; let the LLM explain the result.

## Next steps

- [Decision trees and gradient boosting](decision-trees-and-gradient-boosting.md)
- [Feature engineering and data prep](feature-engineering-and-data-prep.md)
- [Training, validation and overfitting](training-validation-and-overfitting.md)
- [Tabular ML end to end](../../build/projects/tabular-ml-end-to-end.md)
- For databases, warehouses and time-series storage: [Data Zero to Hero](https://data.noblerworks.com/)

## Sources

- Hyndman and Athanasopoulos, *Forecasting: Principles and Practice*, 3rd ed., free online: https://otexts.com/fpp3/
- scikit-learn, `TimeSeriesSplit` and cross-validation of time series: https://scikit-learn.org/stable/modules/cross_validation.html#time-series-split
- scikit-learn, `HistGradientBoostingRegressor`: https://scikit-learn.org/stable/modules/ensemble.html
