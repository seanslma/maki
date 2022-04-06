# Calculated Table

## group tables based on relationships
```
CalculatedTable = ADDCOLUMNS (
    SUMMARIZE (
        Sales,
        'Date'[Year],
        Product[Size]
    ),
    "Total Quantity", CALCULATE ( SUM ( Sales[Quantity] ) )
)
```
