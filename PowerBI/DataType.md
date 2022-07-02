# Data type

## types
```
type text, type date, type time, type number
Text.Type, Date.Type, Int64.Type, Number.Type  
```

## transform columns
The third parameter `type datetime` is for null values. If not set the returned column type is Any (`ABC123`).
```
Table.TransformColumns(Source, {"MyDate", each fn_UtcToLocal(_), type datetime})
```
