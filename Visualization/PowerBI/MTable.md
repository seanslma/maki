# MTable

## replacevalue
```
#"Replaced Value" = Table.ReplaceValue(
  #"Source", 
  each [ColA], each if Text.Contains([ColB],"AA") then "AA" else 
    if Text.Contains([ColB],"BB") then "BB" else [ColA], 
  Replacer.ReplaceValue, 
  {"ColA"}
),
```

## lookupvalue
```
#"Lookup Column" = Table.AddColumn(
  #"Source", 
  "NameId", 
  each #"NameTypes"[Id]{List.PositionOf(#"NameTypes"[Name], [Name])}
),
```
