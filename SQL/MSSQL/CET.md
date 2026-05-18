# CET

## join performance in cet
when join cet tables, by sorting the join columns, the performance can increase 30-60x.
- https://stackoverflow.com/questions/3995958/adding-an-index-to-a-cte
- sort the joinning columns in the CET `ORDER BY Field1, Field2 OFFSET 0 ROWS`
- sqlalchemy: `.orderby(Field1, Field2).offset(0)`

## how to only execute cet conditionally
https://stackoverflow.com/questions/58723615/how-to-prevent-cte-execution-until-reached-or-not-exists

## when `order by` does not work
SQL Server has three main join strategies:
- Nested Loops (great when one side is small + index seek on the other)
- Hash Join (great for large, unsorted sets; needs memory)
- Merge Join (great when both inputs are already sorted on the join keys)

Sometimes option #1 will not work as the sql server will ignore the sort in CTE.
In this case try option #2 - force the sql server to sort the data so in a later CTE join will use `merge join`.

```sql
option1_cte AS (
    SELECT
        sales.cutomer_code,
        sales.invoice_number,
        sales.amount_due
    FROM
        sales
    ORDER BY sales.cutomer_code, sales.invoice_number OFFSET 0 ROWS -- perf
)

option2_cte AS (
    SELECT
        t.cutomer_code,
        t.invoice_number,
        t.amount_due
    FROM (
        SELECT
            sales.cutomer_code,
            sales.invoice_number,
            sales.amount_due,
            ROW_NUMBER() OVER (ORDER BY sales.cutomer_code, sales.invoice_number) AS mssql_rn
        FROM sales
    ) AS t
    WHERE mssql_rn > 0
)
```
