# Group

## select and where
```
d = (
    df
    .select('name', 'price')
    .where((df['id']==1) | (df['id']==3))
)
display(d)
```

## count
```
d = (
    df
    .select('id', 'name')
    .groupBy('name')
    .count()
)
display(d)
```

## count distinct
```py
d = df.groupBy('Country').agg(countDistinct('CustomerID').alias('country_count')).orderBy(desc('country_count'))
d.show()
```

## min/max
```py
#d1.agg({'InvoiceDate': 'min', 'InvoiceDate': 'max'}).first()[0] # not work as dict cannot have same keys
from pyspark.sql import functions as f
d = df.agg(
    f.min('InvoiceDate').alias('mn'),
    f.max('InvoiceDate').alias('mx'),
    f.avg('InvoiceDate').alias('ag'),
    f.sum('InvoiceDate').alias('sm'),
).first()
mn, mx, ag, sm = d #d is a Row, we can also get mn by d.mn or d['mn'] or d[:1]
```
