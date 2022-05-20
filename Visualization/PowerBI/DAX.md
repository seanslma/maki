# DAX

https://docs.microsoft.com/en-us/dax/dax-overview

definitions of measures, calculated columns, calculated tables, row-level security etc.

## Measures
Measures are formula calculations depending on the context such as filter, slicer etc.

## Calculated columns
A calculated column's values are calculated using DAX row by row.

## Calculated tables
A calculated table is calculated using DAX based on other tables.

## filter
```
TableNew =
    VAR __IDsWihFlag = FILTER(__Table,[Flag])
RETURN
    FILTER('Table',[id] IN SELECTCOLUMNS(__IDsWithFlag,"id",[id]))
```

## diff between values of two dates
https://www.fourmoo.com/2018/11/06/dax-measure-getting-difference-between-2-values-in-a-table/

https://www.sqlservercentral.com/articles/month-over-month-calculation-using-dax-in-power-bi

Steps:
- create two dates tables including the dates in that table
- the first table has a relationship with the original table while the second is isolated
- calculate the measure values for the first date as usual
- calculate the measure values for the seonds date by ignore the slicer one
- so the page has two single selcetion slicers 
```
NewDateValue = CALCULATE (
    Sum(MyTable[Value])
)
OldDateValue = CALCULATE (
    SUM(MyTable[Value]),
    ALL(Dates[Date]),
    MyTable[Date] = SELECTEDVALUE(Dates2[Date])
)
```

## change values dynamicly based on slicer
https://community.powerbi.com/t5/Desktop/Change-calculated-table-dynamically-on-slicer-selection/m-p/1195458#M535454

## distinct column values to table
```
NewTable = DISTINCT(OldTable[ColName])
```

## measure conditional on another column
```
DateStr = 
    VAR MaxDate = MAX(Dates[Date])
Return 
    If(Dates[Date]=MaxDate, "MaxDate", FORMAT(Dates[Date], "yyyy-MM-dd hh:mm:ss"))
```

## measure by filtering column
```
NewMeasure = CALCULATE (
    SUM(MyTable[Value]),
    MyTable[ValueType] = "Good"
)
```

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
