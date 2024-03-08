# Categorical
https://docs.pola.rs/user-guide/concepts/data-types/categoricals/

## CategoricalRemappingWarning
```
Local categoricals have different encodings, expensive re-encoding is done to perform this merge operation.
Consider using a StringCache or an Enum type if the categories are known in advance.
```

solution: using the same `Enum` to encode the column in both series
```py
dtype = pl.Enum(["Polar", "Panda", "Brown"])
cat_series = pl.Series(["Polar", "Panda", "Brown", "Brown", "Polar"], dtype=dtype)
cat2_series = pl.Series(["Panda", "Brown", "Brown", "Polar", "Polar"], dtype=dtype)
print(cat_series.append(cat2_series))
```
