# New column conditional on max value

## max and second max
```
let
    Source = Sql.Database(p_SqlServer, p_SqlDbName),
    Data = Source{[Schema="sch",Item="tbl"]}[Data],
    #"Selected Columns" = Table.SelectColumns(Data,{"Date"}),
    #"Selected Rows" = Table.SelectRows(#"Selected Columns", each [Date] > RangeStart and [Date] <= RangeEnd),
    #"Removed Duplicates" = Table.Distinct(#"Selected Rows"),
    #"Local Date Source" = Table.TransformColumns(#"Removed Duplicates", {"Date", each fn_UtcToLocal(Date.AddDays(_,1)), type datetime}),
    #"Added YearMonth" = Table.AddColumn(#"Local Date Source", "YearMonth", each Date.Year([Date])*100+Date.Month([Date]), Int64.Type),
    #"Calculated Max Date" = List.Max(#"Added YearMonth"[Date]),
    #"Calculated Second Max Date" = List.Max(Table.SelectRows(#"Added YearMonth", each [Date] < #"Calculated Max Date")[Date]),
    #"Added Date String" = Table.AddColumn(#"Added YearMonth", "DateStr", each if [Date] = #"Calculated Max Date" then "1st" else if [Date] = #"Calculated Second Max Date" then "2th" else DateTime.ToText([Date], "yyyy-MM-dd hh:mm:ss"), type text)
in
    #"Added Date String"  
```
