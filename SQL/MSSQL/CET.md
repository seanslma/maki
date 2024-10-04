# CET

## join performance in cet
when join cet tables, by sorting the join columns, the performance can increase 30-60x.
- https://stackoverflow.com/questions/3995958/adding-an-index-to-a-cte
- sort the joinning columns in the CET `ORDER BY Field1, Field2 OFFSET 0 ROWS`
- sqlalchemy: `.ordervy(Field1, Field2).offset(0)`
