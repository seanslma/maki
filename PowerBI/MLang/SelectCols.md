# Select Columns

## select unique cols
```
let
    Source = Sql.Database(p_SqlServer, p_SqlDbName),
    Data = Source{[Schema="sch",Item="tbl"]}[Data],
    #"Selected Columns" = Table.SelectColumns(Data,{"Date"}),
    #"Selected Rows" = Table.SelectRows(#"Selected Columns", each [Date] > RangeStart and [Date] <= RangeEnd),
    #"Removed Duplicates" = Table.Distinct(#"Selected Rows"),
    #"Local Date Source" = Table.TransformColumns(#"Removed Duplicates", {"Date", each fn_UtcToLocal(Date.AddDays(_,1)), type datetime}),
    #"Added YearMonth" = Table.AddColumn(#"Local Date Source", "YearMonth", each Date.Year([Date])*100+Date.Month([Date]), Int64.Type)
in
    #"Added YearMonth"
```
