# MTable

## const table
```
let
    Source = Table.FromRows(
        {
            {1, "A"},
            {2, "B"}
        },
        type table [Id = Int64.Type, Code = text]
    )
in
    Source
```

## replace value
```
#"Replaced Value" = Table.ReplaceValue(
  #"Source",
  each [ColA], each if Text.Contains([ColB],"AA") then "AA" else
    if Text.Contains([ColB],"BB") then "BB" else [ColA],
  Replacer.ReplaceValue,
  {"ColA"}
),
```

## lookup value
```
#"Lookup Column" = Table.AddColumn(
  #"Source",
  "NameId",
  each #"NameTypes"[Id]{List.PositionOf(#"NameTypes"[Name], [Name])}
),
```
