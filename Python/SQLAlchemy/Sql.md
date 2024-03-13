# SQL

## sql.literal
Cannot use literal in groupby - use sub query.
```py
sql.literal('name', Unicode).label('surname')
sql.literal(dates.end, Date).label('as_of_date')
```
