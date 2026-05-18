# SUMMARIZE

## pivot table
```
PvtTable = SUMMARIZE(
    MyTable,
    MyTable[Date],
    MyTable[Type],
    "CodeA", CALCULATE(SUM(MyTable[Value]), MyTable[Code]="CodeA"),
    "CodeB", CALCULATE(SUM(MyTable[Value]), MyTable[Code]="CodeB")
) 
```

## group table
```
GrpTable = ADDCOLUMNS(
    SUMMARIZE (
        MyTable,
        MyTable[Date],
        TypeTable[Type]
    ),
    "Value", CALCULATE(SUM(MyTable[Value]))
)
```

## group by with filters
Calculated cumulated values up to as-of-date for each group
- SUMMARIZE: the groupby
- ADDCOLUMNS: the aggragate

```dax
VAR Threshold = 1
VAR AsOf = MAX('Dates'[Date]) -- Respects slicer or the Month in a trend line

-- Summarize the Retail at the required grain
VAR Groups =
    SUMMARIZE(
        FILTER('Retail', 'Retail'[Date] <= AsOf),
        'Retail'[ClientNumber],
        'Retail'[BillingPeriod]
    )

VAR CalculatedGroups =
    CALCULATETABLE(
        ADDCOLUMNS(
            Groups,
            "@Bal", CALCULATE(SUM('Retail'[Amount])),
            "@FirstDate", CALCULATE(MIN('Retail'[Date])),
            "@LastDate", CALCULATE(MAX('Retail'[Date]))
        ),
        FILTER( ALL('Retail'[Date]), 'Retail'[Date] <= AsOf )
    )

-- Get boundaries from the AgingBuckets table
VAR MinD = SELECTEDVALUE('AgingBuckets'[MinDays], 0)
VAR MaxD = SELECTEDVALUE('AgingBuckets'[MaxDays], 99999)

RETURN
    SUMX(
        FILTER(
            CalculatedGroups,
            VAR CurBal = [@Bal]
            VAR Age = IF(
                ABS(CurBal) < Threshold,
                DATEDIFF([@FirstDate], [@LastDate], DAY),
                DATEDIFF([@FirstDate], AsOf, DAY)
            )
            RETURN
                CurBal >= Threshold && Age >= MinD && Age < MaxD
        ),
        [@Bal]
    )
```
