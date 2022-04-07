# DAX

https://docs.microsoft.com/en-us/dax/dax-overview

definitions of measures, calculated columns, calculated tables, row-level security etc.

## Pivot columns
```
P = SUMMARIZE(T,
    T[A],
    T[B],
    "C",CALCULATE(SUM(T[V]),T[I]="C"),
    "D",CALCULATE(SUM(T[V]),T[I]="D")
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
