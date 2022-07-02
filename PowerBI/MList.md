# List

## List.Contains, In cluase in select rows
Buffer will save the list values in memory
```
Filters = Table.SelectRows(Source, each List.Contains(List.Buffer(Tbl[Val]), [QtYr]))
```

## List.Generator
```
let
    Source = List.Generate(
        () => [n = 1, d = c_Today],
        each [n] <= 4 and Date.Year([d]) > Date.Year(c_Today) - 5,
        each [n = [n] + 1, d = Date.AddMonths([d], -3)],
        each Text.End(Number.ToText(Date.Year([d])),2) & "Q" & Number.ToText(Date.QuarterOfYear([d]))
    ),
    #"List To Column" = Table.FromList(Source, null, {"YQ"})  # List must be text
in
    #"List To Column"
```

## List to table (change to rows)
```
let
    Source = List.Distinct(Tbl[Year]),
    Rows = List.Transform(Source, each {_}),
    Result = Table.FromRows(Rows, type table [Year = Int64.Type])
in
    Result
```

## add list as new table column
```
let
    Source = Table,
    MyList = List.Generator(),
    Columns = Table.ToColumns(Source) & {MyList}, 
    Headers = Table.ColumnNames(Source) & {"Col_New"},
    MergedTable = Table.FromColumns(Columns, Headers)
in
    MergedTable
``` 
