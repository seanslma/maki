# File IO

## csv
with header
```py
df = spark.read.csv('data.csv', header=True, escape='\"')
df = spark.read.load('data.csv', format='csv', header=True)
display(df.limit(5)) #what is this???
```

without header
```py
from pyspark.sql.types import *
from pyspark.sql.functions import *

csv_schema = StructType([
    StructField('id', IntegerType()),
    StructField('name', StringType()),
    StructField("date", DateType()),
    StructField('price', FloatType()),
])

df = spark.read.load('data.csv', format='csv', header=False, schema=csv_schema)
display(df.limit(5)) #what is this???
```
