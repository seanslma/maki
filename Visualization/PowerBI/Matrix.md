# Matrix

## subtotal
customize subtotals and totals:
https://community.powerbi.com/t5/Desktop/Different-DAX-calculations-for-different-row-hierarchies-in-a/m-p/2136701#M788896
```
Switch = 
var _territoty=1
var _region=2
var _Total=3
return 
IF (
    ISINSCOPE ( 'Table'[Region] ),
    IF ( ISINSCOPE ( 'Table'[Territory] ), _territoty, _region ),
    _Total
)
```

## SUMX vs SWITCH CALCULATE
`SUMX` will calculate the value for all row levels. If use `SWITCH` and CALCULATE based on a specific row level, the subtotal will not show up.
```
Measure = SUMX(
    Tb1,
    SWITCH(
        RELATED(Tb2[Col1]),
        "AA", Tb1[Value],
        "BB", Tb1[Value],
        BLANK()
    )
)

Measure = SWITCH(
    SELECTEDVALUE(Tb2[Col1]),
    "AA", CALCULATE(SUM(Tbl[Value])),
    "BB", CALCULATE(SUM(Tbl[Value])),
    BLANK()
)
```
