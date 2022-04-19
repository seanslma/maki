# m language

## text function
https://docs.microsoft.com/en-us/powerquery-m/text-functions

https://docs.microsoft.com/en-us/powerquery-m/power-query-m-function-reference


## get one col and sort
```
let
    Source = List.Distinct(T[A]),
    SourceTable = Table.FromColumns({Source}, {"A"}),
    ColumnATable = Table.Sort(SourceTable, {"A", Order.Descending})
in
    ColumnATable
```
