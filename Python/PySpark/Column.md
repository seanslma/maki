# Column

## distinct
```py
df.select('CustomerID').distinct().count()
```

## min/max
```py
#d1.agg({'InvoiceDate': 'min', 'InvoiceDate': 'max'}).first()[0] # not work as dict cannot have same keys
from pyspark.sql import functions as f
agg = df.agg(f.min('InvoiceDate').alias('mn'), f.max('InvoiceDate').alias('mx'), f.avg('InvoiceDate').alias('ag'), f.sum('InvoiceDate').alias('sm')).first()
mn, mx, ag, sm = agg #agg is a Row, we can also get mn by agg.mn or agg['mn'] or agg[:1]
```
