# Math

## mod and integer division
```
#"Added Year" = Table.AddColumn(Source, "Year", each Number.IntegerDivide([YearMonth], 100), Int64.Type),
#"Added Month" = Table.AddColumn(#"Added Year", "Month", each Number.Mod([YearMonth], 100), Int64.Type)
```    
