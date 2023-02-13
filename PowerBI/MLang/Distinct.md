# Distinct

## Distinct col as new table
Better
```
Source = Table.SelectColumnd(Tbl, {"Year"}),
DistinctRows = Table.Distinct(Source)
```

Also works
```
Source = List.Distinct(Tbl[Year]),
Rows = List.Transform(Source, each {_}),
Result = Table.FromRows(Rows, type table [Year = Int64.Type])
```
