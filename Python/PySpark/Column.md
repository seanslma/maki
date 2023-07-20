# Column

## distinct
```py
df.select('CustomerID').distinct().count()
```

## convert col types
```py
from pyspark.sql.functions import col, to_timestamp
d = (
    df
    .withColumn('InvoiceNo', col('InvoiceNo').cast('int'))
    .withColumn('Quantity', col('Quantity').cast('double'))
    .withColumn('InvoiceDate', to_timestamp('InvoiceDate', 'dd/MM/yyyy HH:mm'))   
)
d.show(5,0)
```
