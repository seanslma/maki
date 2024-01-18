# Measure

Note:
- We can't reference the column as part of a measure without using one of the aggregation functions in DAX

## show one of measure based on slicer
https://towardsdatascience.com/dynamic-filtering-in-power-bi-5a3e2d2c1856

- measure 1: measure1 = SUM('tbl'[amount])
- measure 2: measure2 = CALCULATE('tbl-measure'[measure1],DATESYTD(Dates[Date])), year to day
- create a slicer key-val table `tbl-keyval`: SelectedKey = MIN('tbl-keyval'[key])
- SelectedMeasure = SWITCH([SelectedKey], 1,'tbl-measure'[measure1], 2,'tbl-measure'[measure2])

## use slicer selected value
Measure can use slicer selected value to calculate the measure values.
```
Sales for Selected Category in 2024 = CALCULATE(
    SUM(Sales[Sales Amount]),
    SaleYears[Year] = 2024,
    Sales[Category] = SELECTEDVALUE(Category[Category Name])
)
```

or
```
Sales for Selected Category in 2024 = CALCULATE(
    SUM(Sales[Sales Amount]),
    FILTER(
        Sales,
        SaleYears[Year] = 2024
        && Sales[Category] = SELECTEDVALUE(Category[Category Name])
    )
)
```
 **The purpose of the FILTER function in the examples is to explicitly control which data is included in the calculation based on the slicer selection.** 
 While context filters often work implicitly, using FILTER within measures offers these benefits:
- **Explicit Control:** Ensures the calculation precisely follows the slicer selection, even in complex scenarios with multiple filters or relationships.
- **Handling Multiple Selections:** FILTER, unlike SELECTEDVALUE, can manage scenarios where slicers allow multiple values to be chosen.
- **Conditional Logic:** You can create more intricate logic within measures using FILTER alongside IF or other conditional functions.
- **Custom Calculations:** FILTER enables calculations that might not be possible with context filters alone, such as filtering on a measure or calculated column.

**Here's a breakdown of how the FILTER function works within a measure:**
1. **Retrieves the selected value:** The `SELECTEDVALUE` function extracts the value chosen in the slicer.
2. **Applies the filter:** The `FILTER` function creates a virtual table containing only rows from the specified table where the specified condition is met. In this case, the condition ensures the `Category` or `Country` column matches the selected value.
3. **Calculates using the filtered data:** The calculation (e.g., SUM or AVERAGEX) is performed on this filtered subset of data, ensuring alignment with the slicer selection.
