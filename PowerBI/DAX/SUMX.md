# SUMX

## Add grouped values
First calculate region/product level sale profit figures then add them together to get the total. We di it that way because we need to do som esepcial treatment of the value in each group (e.g., rounding up).

Here we show how to do it right. Note that we need to calculate the Q1 to current quarter total but the filter selected value is just the current quarter.

```dax
VAR __qtr = SELECTEDVALUE(Quarters[Quarter])
VAR __last_qtr = CALCULATE(
    MAX(Sales[Quarter]),
    ALL(AttributeTypes),
    AttributeTypes[Attribute] = "Profit",
    REMOVEFILTERS(Quarters),
    Quarters[Quarter] <= __qtr
) 
// Ensure product before current quarter being selected as well                   
VAR __tbl = CALCULATETABLE(
    SUMMARIZE(
        Sales, 
        Sales[ProductId]
    ),
    REMOVEFILTERS(Quarters[Quarter]),
    Quarters[Quarter] <= __qtr
)
VAR __sur = SUMX(
    __tbl,
    CALCULATE(
        SUM(Sales[Value]),
        ALL(AttributeTypes), 
        AttributeTypes[Attribute] = "Profit",
        REMOVEFILTERS(Quarters[Quarter]),
        Quarters[Quarter] = __last_qtr                         
    )
)
```
