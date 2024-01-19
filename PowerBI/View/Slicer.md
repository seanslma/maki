# Slicer

home table
https://forum.enterprisedna.co/t/applying-two-slicers-from-the-same-field-on-table-visual/7454/10

## order
click 3-dots and sort and change the sort order

## use fact or dim col for slicer
Generally we should use col in dim table for slicer
- dim col can control another dim table so will only show values related to the slicer
- will not affect another slicer - avoid deadlock

## restrict slicer values to filtered values from another slicer
https://www.sqlbi.com/articles/syncing-slicers-in-power-bi/

Filter slicers without using bidirectional filters in Power BI.
- each customer can only have a few colors
- the color slicer should only show the colors for that customer
- use a filter to exclude blank values
- or use `visual interactions`

## remove values not in fact table from slicer
Problem: slicer uses dim table column and some values are not in fact table 2 - do not want to show the non-existent values in the slicer for table 2

Solution: create a measure based on the values in fact table 2 and use it to filter the slicer.

Limit the slicer to show values present in a fact table:
```
SlicerFilter =
    VAR _val_in_fact2 =
        VALUES(fact_tbl2[col])
RETURN
    IF(MAX(dim_tbl[col]) IN _val_in_fact2, 1, 0)
```

## `blank` value issue
Sometimes the slicer will show blank() even all tables do not have blank values.

This happens when a table on the n-side of a 1-to-n relationship contains values not present in the corresponding column of the table on the 1-side (with the slicer on a column from the table on the 1-side). Just like a Left Outer Join on the 1-side table.

## Forced value
`Chiclet Slicer` can force select one of the existing values.

For the default slicer, when source data changed, the last selected missing value will still in the slicer. 

## Slicers stuck on non-existing values
Problem:
- Slicer-year points to years
- Slicer-quarter points to quarters
- In the table there are two records: (A, 2000, 1) and (B, 2001, 3)
- When the values for the sclicers are 2000 and 1, it's not possible to show the second record

Workaround
- Let one of the slicer to be a multi-select and un-select all, so the other slicer will show all values

Solution:
- see `Visual interactions`

## Visual interactions
- slicer A -> column A, slicer B -> column B
- value selected in slicer B should not affect slicer A (still show all values)
- Select slicer B > Format > Edit interactions > click `no impact` icon near slicer A

## Selected value
```
VAR __val = CALCULATE(
    SUM(Tbl[Value]), 
    ALL(Tbl[Quarter]),
    Tbl[Quarter] <= SELECTEDVALUE(Tbl[Quarter])
)
```

## Default max value
PowerBI will remember a constant value so we need to replace the max with a constant, e.g.
```
DateStr = 
    VAR MaxDate = MAX(Dates[Date])
    VAR SecondMaxDate = MAXX(FILTER(Dates,[Date]<MaxDate), Dates[Date])
Return 
    SWITCH(Dates[Date], MaxDate, "Today", SecondMaxDate, "Yesterday", FORMAT(Dates[Date], "yyyy-MM-dd hh:mm:ss"))
```

## Slicer not showing all values in a table
https://community.fabric.microsoft.com/t5/Desktop/Slicer-not-showing-all-values-that-are-shown-in-visual/m-p/2580206#M910972

Scenario: both the slicer and view table column refer to the same table column

Solution: one of the relationships in the dataset had the cross-filter direction set to both which resulted in the date filter affecting the product group dimension.

Need to filter out empty records based on another column.
