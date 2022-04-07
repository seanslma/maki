# Calculated Table

## Pivot columns
```
P = SUMMARIZE(T,
    T[A],
    T[B],
    "C",CALCULATE(SUM(T[V]),T[I]="C"),
    "D",CALCULATE(SUM(T[V]),T[I]="D")
)
```

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

## New table basd on relatioships
```
T = ADDCOLUMNS (
    SUMMARIZE (
        T1,
        T1[A],
        T2[U],
        T3[X],
        T1[B],
        T1[C]
    ),
    "V", CALCULATE ( SUM ( T1[V] ) )
)
```
