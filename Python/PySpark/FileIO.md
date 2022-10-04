# File IO

## csv
with header
```
df = spark.read.load(
    '/data/my.csv',
    format='csv',
    header=True,
)
display(df.limit(5))
```

without header
```
from pyspark.sql.types import *
from pyspark.sql.functions import *

csv_schema = StructType([
    StructField('id', IntegerType()),
    StructField('name', StringType()),
    StructField('price', FloatType()),
])

df = spark.read.load(
    '/data/my.csv',
    format='csv',
    header=False,
    schema=csv_schema,
)
display(df.limit(5))
```
