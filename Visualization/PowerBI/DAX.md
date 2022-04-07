# DAX

https://docs.microsoft.com/en-us/dax/dax-overview

definitions of measures, calculated columns, calculated tables, row-level security etc.

## Pivot columns
```
TPivot = SUMMARIZE(T,
    T[A],
    T[B],
    "C",CALCULATE(SUM(T[V]),T[I]="C"),
    "D",CALCULATE(SUM(T[V]),T[I]="D")
)
```
