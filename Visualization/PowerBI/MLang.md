# m language

## text function
https://docs.microsoft.com/en-us/powerquery-m/text-functions

https://docs.microsoft.com/en-us/powerquery-m/power-query-m-function-reference

## constant
```
//c_LocalTimeAdjust
let
    Source = #duration(0,10,0,0)
in
    Source
```

## function
```
//fn_UtcToLocal
let
	Source = (InputDateTime as datetime)=>
let
	OutputDateTime = InputDateTime + c_LocalTimeAdjust
in
	OutputDateTime
in
	Source 
```


## filter rows
```
Table.SelectRows(
    MyTable, each [CustomerID] > 2
)
```

## get one col and sort
```
let
    Source = List.Distinct(T[A]),
    SourceTable = Table.FromColumns({Source}, {"A"}),
    ColumnATable = Table.Sort(SourceTable, {"A", Order.Descending})
in
    ColumnATable
```

## get data from sql (incremental refresh)
```
let
    Source = Sql.Database(SQLHostName, "DatabaseName"),
    MyTable = Source{[Schema="SchemaName",Item="TableName"]}[Data],
    #"Select Columns" = Table.SelectColumns(MyTable,{"Date"}),
    #"Filter Rows" = Table.SelectRows(#"Select Columns", each [Date] > RangeStart and [Date] <= RangeEnd),
    #"Remove Duplicates" = Table.Distinct(#"Filter Rows"),
    #"Convert Date To Local" = Table.TransformColumns(#"Remove Duplicates", {"Date", each fn_UtcToLocal(_), type datetime})
in
    #"Convert Date To Local"
```
