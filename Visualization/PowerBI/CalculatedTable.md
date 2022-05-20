# Calculated Table

duplicate column use DAX RELATED???

Calculated tables are tables in the Data Model whose data source is a DAX expression that returns a table. 

## Power query or DAX
https://www.reddit.com/r/PowerBI/comments/axkydz/power_query_or_calculated_table/

The rule of thumb is to push your Calculated Column/Table (basically anything that is not Measure) as close to your database/query/data source/data warehouse as possible, before loading them into your data model. 

In short, it's because the PowerBI's Vertipaq engine compresses the data (before loading into the model) better than Calculated Column/Table, reducing memory usage and improving performance.

## Power query vs DAX calculated columns
https://www.sqlbi.com/articles/comparing-dax-calculated-columns-with-power-query-computed-columns/

### issue: calculated table slow down incremental refresh
Power Query works bottom up, not top down, if:
- Query 1 to SQL Server
- Query 2 to transform Query 1 to a good FACT table
- Query 3 based on Query 2 to filter your FACT table.
Both query 3 and query 2 will go all the way back to Query 1 independently. Power query doesn't process Query 2 and then use hold the results of that for Query 3. It will redo Query 2, and consequently Query 1.

It's better to directly get the data from SQL server (not use calculated table). 

Also, some calculated table not updated after incremental refresh.

### issue: calculated columns bsed on calculated table will not update after refresh

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
