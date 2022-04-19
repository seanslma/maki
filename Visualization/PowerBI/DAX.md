# DAX

https://docs.microsoft.com/en-us/dax/dax-overview

definitions of measures, calculated columns, calculated tables, row-level security etc.

## filter
```
TableNew =
    VAR __IDsWihFlag = FILTER(__Table,[Flag])
RETURN
    FILTER('Table',[id] IN SELECTCOLUMNS(__IDsWithFlag,"id",[id]))
```
