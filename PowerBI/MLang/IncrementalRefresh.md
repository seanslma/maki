# Incremental refresh

## web api
```
let
    Source = Json. Document (Web.Contents("http://localhost:8000/api/data",
    [
        Query=[apikey="key", tablename="sales", datestart=DateTime.ToText(RangeStart), dateend=DateTime.ToText(RangeEnd)]
    ])),
    
    #"Converted to Table" = Table.FromList(Source, Splitter. SplitByNothing(), null, null, ExtraValues. Error),
    #"Expanded Column1" = Table.ExpandRecordColumn(#"Converted to Table", "Column1", {"code", "quantity", "from_date", "to_date"}, {"code", "quantity", "from_date", "to_date"}), #"Changed Type" = Table.TransformColumnTypes(#"Expanded Column1",{{"code", Int64. Type}, {"quantity", Int64. Type}, {"from_date", type datetime}, {"to_date", type datetime}}), #"Filtered Rows" = Table.SelectRows(#"Changed Type", each [from_date] > RangeStart and [from_date] <= RangeEnd)
in
    #"Filtered Rows"
```
