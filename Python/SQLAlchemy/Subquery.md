# Subquery

## Subquery in column
```
stmt = select([t.c.a, subq.as_scaler()])
stmt = select([t.c.a, subq.correlate(None).as_scaler()])
```

## Subquery in `In clause`
```
stmt = select([t.c.a, t.c.b]).whereclause(t.c.a.in_(subq))
```

## Subquery in `from`
```
query = session.query(t.Id, t.Name)
row_number_column = func.row_number().over(
    partition_by=(t.Name),
    order_by=f.EffectiveDate.desc(),
).label("row_number")
query = query.add_columns(row_number_column)
subquery = query.subquery()
columns = [col for col in subquery.c where col.name != 'row_number']
stmt = select(columns).select_from(subquery).where(subquery.c.row_number == 1)
```
