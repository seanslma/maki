# CET

## join performance in cet
when join cet tables, by sorting the join columns, the performance can increase 30-60x.
- https://stackoverflow.com/questions/3995958/adding-an-index-to-a-cte
- sort the joinning columns in the CET `ORDER BY Field1, Field2 OFFSET 0 ROWS`
- sqlalchemy: `.orderby(Field1, Field2).offset(0)`

## how to only execute cet conditionally
https://stackoverflow.com/questions/58723615/how-to-prevent-cte-execution-until-reached-or-not-exists
