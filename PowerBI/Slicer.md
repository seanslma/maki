# Slicer

home table
https://forum.enterprisedna.co/t/applying-two-slicers-from-the-same-field-on-table-visual/7454/10

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

## Selected value
```
VAR __val = CALCULATE(
    SUM(Tbl[Value]), 
    ALL(Tbl[Quarter]),
    Tbl[Quarter] <= SELECTEDVALUE(Tbl[Quarter])
)
```

## Sync slicers
https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers?tabs=powerbi-desktop#sync-and-use-slicers-on-other-pages

## Visual interactions
- slicer A -> column A, slicer B -> column B
- value selected in slicer B should not affect slicer A (still show all values)
- Format > Edit interactions > click `no impact` icon near slicer A

## Default max value
PowerBI will remember a constant value so we need to replace the max with a constant, e.g.
```
DateStr = 
    VAR MaxDate = MAX(Dates[Date])
    VAR SecondMaxDate = MAXX(FILTER(Dates,[Date]<MaxDate), Dates[Date])
Return 
    SWITCH(Dates[Date], MaxDate, "Today", SecondMaxDate, "Yesterday", FORMAT(Dates[Date], "yyyy-MM-dd hh:mm:ss"))
```
