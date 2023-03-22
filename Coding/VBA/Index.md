# Index

## one-based
- Retrieving values into an variant array from the worksheet's cells always returns a `1-based 2-D array`
- `Option Base 0` (default) cannot change this behavior
```vb
arr = rng.Value
```

## zero-based
- `Split("x,y,z", ",")` '0-based index
- `Application.Transpose` will return a 1-D `zero-based` array of a single column or single row.
