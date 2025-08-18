# Variance threshold

## sklearn slow
```py
import polars as pl
sklearn.feature_selection import VarianceThreshold
def sklearn_variance_threshold(
    X: pl.DataFrame,
    threshold: float = 0.0,
) -> pl.DataFrame:
    selector = VarianceThreshold(threshold=0.0)
    _ = selector.fit_transform(X)
    df = X[selector.get_support()]
    return df
```
## polars faster 
about 20x faster
```py
import polars as pl
def polars_variance_threshold(
    X: pl.DataFrame,
    threshold: float = 0.0,
) -> pl.DataFrame:
    stats = X.select([
        pl.var(col).alias(col) for col in X.columns
    ])
    variances = stats.row(0)  # get variances as a list
    df = X.select([
        col for col, var in zip(X.columns, variances) 
        if var > threshold
    ])
    return df
```
