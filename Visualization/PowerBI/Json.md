# Json

## example1
### file
```json
{ "name":"John",
  "country":[
    {"id":"US","prob":0.09},
    {"id":"AU","prob":0.06}]
}
```

### mlang
```
let
    Source = Json.Document(File.Contents("C:\tmp\name.json")),
    #"Converted to Table" = Table.FromRecords({Source}),
    #"Expanded country" = Table.ExpandListColumn(#"Converted to Table", "country"),
    #"Expanded country1" = Table.ExpandRecordColumn(#"Expanded country", "country", {"id", "prob"}, {"country.id", "country.prob"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Expanded country1",{{"country.id", Text.Type}, {"country.prob", Number.Type}})
in
    #"Changed Type"
```

### table
name | country.id | country.prob |
:----|:-----------|:-------------|
John | US         | 0.09         |
John | AU         | 0.06         |
