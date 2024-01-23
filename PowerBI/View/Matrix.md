# Matrix

## example
create a matrix with `rows` country and city, and `values` year, sale_quantity, price and revenue
- collape the rows to country level, the values should show the sum, weighted average, and sum
- if expanded we can see the city level values with cities as a dented list
- the total should show the correct summary values as well
  
## Turning off stepped layout
Turn off stepped layout on the row headers card, to put each row label in a separate column not the default stepped (indented) layout.

## subtotal
Will use the same measure to calculate value and total so sometimes the total can be incorrect. In this case, we need to use different measures for value and total calculation.
```
Measure = 
    VAR __is_val = HASONEFILTER(Tb2[Col2])
    VAR __tmp_val = CALCULATE(
        SUM(Tb1[Value]), 
        ALL(Tb2),
        ALL(Tb1[Colx]),        
        Tb2[Col2] = "CC",
        Tb1[Colx] <= SELECTEDVALUE(Tb1[Colx])
    )    
RETURN    
    IF(
        __is_val,
        SUMX(
            Tb1,
            SWITCH(
                RELATED(Tb3[Col3]),
                "AA", __val,
                "BB", __val - __tmp_val,
                BLANK()
            )
        ),
        SUMX(
            FILTER(
                Tb1, 
                RELATED(Tb2[Col2]) in {"AA", "CC"}
                    && Tb1[Colx] <= SELECTEDVALUE(Tb1[Colx])
            ),
            Tb1[Value]
        )
    )
```

customize subtotals and totals:
https://community.powerbi.com/t5/Desktop/Different-DAX-calculations-for-different-row-hierarchies-in-a/m-p/2136701#M788896
```
Switch = 
    var _territoty=1
    var _region=2
    var _Total=3
return 
    IF(
        ISINSCOPE('Table'[Region]),
        _region,
        IF(
            ISINSCOPE('Table'[Territory]), 
            _territoty, 
            _Total
        )
    )
```

Seems `ISINSCOPE` does not work. We need to use `HASONEFILTER(Tbl(Col))` to determine which row level the measure is.

## subtotal to sum values (city price) on cities
```
AvgPrice = SUMX(
    SUMMARIZE('Table', 'Table'[city], "Average", divide(sum('Table'[price]),SUM('Table'[quantity]))),
    [Average]
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
