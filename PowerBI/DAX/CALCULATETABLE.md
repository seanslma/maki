# CALCULATETABLE

Can be used to convert a table to another table by adding/removing some filters.

This is useful when calculating total based on row level values.

## Example
```dax
VAR __tot = SUMX(
    CALCULATETABLE (
        SUMMARIZE(
            Sales, 
            ProductCategoryTypes[ProductCategory], 
            Stores[Region]
        ),
        REMOVEFILTERS(Quarters[Quarter]),
        Quarters[Quarter] <= __qtr
    ), 
    [Row_Level_Measure]
) 
```
