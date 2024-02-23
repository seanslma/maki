# Function

https://vincent-tseng.medium.com/dax-hasonevalue-vs-hasonefilter-724fab64f9aa
https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-hasonefilter-vs-hasonevalue-vs-isfiltered

## HASONEFILTER(columnName)
Returns TRUE when the number of directly filtered values on columnName is one.
- based on a direct filter

## HASONEVALUE(columnName)
Returns TRUE when the context of a specific column has been filtered down to one distinct value only.
- based on a direct/cross-filter

## ISFILTERED(columnName)
Returns TRUE when the columnName parameter is filtered in the PivotTable (all simple, non-total rows and columns in a PivotTable are filtered by a given context). 
- direct filter

## ISCROSSFILTERED(columnName)
Returns TRUE when ColumnName or a column of TableName is being cross-filtered. 
- direct/cross filter

## SUMMERIZE
Returns a summary table for the requested totals over a set of groups. Similar to SQL `Group By`.

## SUMX
SUMX works on virtual table while SUM does not. 
We can use SUMMERIZE and SUMX together to get sum of all groups 
```
SUMX(SUMMERIZE(table, groupby_col_name, val_col_name, val_expr), [val_col_name])
```

Sales example
```
VAR __tbl = SUMMARIZE(Sales, SalesCountries[CountryName], "@val", [Profit_Measure]) 
VAR __tot = SUMX(__tbl, [@val])
```

Demand weighted average price example. In this example, `SUMX` will first calculate the values record by record then sum them together.
```
VAR __dwa_price = DIVIDE( 
    SUMX( 
        Sales,
        Sales[Quantity] * Sales[Price]
    ),
    SUM( Sales[Quantity] )
)
```

## ALLEXCEPT
Removes all context filters in the table except filters that have been applied to the specified columns.
```
AverageTotal = 
  VAR __val = CALCULATE([AverageSales], ALLEXCEPT(Sales, Dates[Year]))
RETURN
  __val
```
