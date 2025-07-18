# Table
https://arrow.apache.org/docs/python/generated/pyarrow.Table.html

https://arrow.apache.org/cookbook/py/data.html

## get col unique values
```py
pyarrow.Table.column('nmi_code').unique()
```

## select columns
```py
table.select(['year'])
```

## drop columns
```py
table.drop_columns('animals')
table.drop_columns(['n_legs', 'animals'])
```

## select rows
```py
table.take([1,3])
```

## select rows based on condition
```py
import pyarrow.compute as pc
expr = pc.field('year') <= 2020
table.filter(expr)

table.filter(pc.field('start_date') < pc.field('end_date'))
```

## get rows with zero-copy
```py
table.slice(offset=0, length=3)
```

## sort_by
```py
table.sort_by('animal')
```

## group_by
```py
table.group_by('year').aggregate([('n_legs', 'sum')])
```
