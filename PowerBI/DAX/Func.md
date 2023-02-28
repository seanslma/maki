# Function

## HASONEFILTER(columnName)
Returns TRUE when the number of directly filtered values on columnName is one.

## HASONEVALUE(columnName)
Returns TRUE when the context of a specific column has been filtered down to one distinct value only.

## ISFILTERED(columnName)
Returns TRUE when the columnName parameter is filtered in the PivotTable (all simple, non-total rows and columns in a PivotTable are filtered by a given context). 

## SUMMERIZE
Returns a summary table for the requested totals over a set of groups. Similar to SQL `Group By`.

## SUMX
SUMX works on virtual table while SUM does not. 
We can use SUMMERIZE and SUMX together to get sum of all groups 
```
SUMX(SUMMERIZE(table, col_type, val_col_expr), [val_col])
```

## ALLEXCEPT
Removes all context filters in the table except filters that have been applied to the specified columns.
```
AverageTotal = 
  VAR __val = CALCULATE([AverageSales], ALLEXCEPT(Sales, Dates[Year]))
RETURN
  __val
```