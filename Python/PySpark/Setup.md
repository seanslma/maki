# Setup

## create session
```py
from pyspark.sql import SparkSession
spark = (
    SparkSession
    .builder
    .appName('spark-dev')
    .config("spark.memory.offHeap.enabled","true")
    .config("spark.memory.offHeap.size","10g")
    .getOrCreate()
)
```

## load data
```py
#df = spark.read.csv('data.csv', header=True, escape='\"')
df = spark.read.parquet('data.parquet')
```

## show top n lines
```py
df.show(5)                #truncate to 20 chars
df.show(5, 0)             #no truncate
df.show(5, vertical=True) #transpose
```

## basic info
```py
def sp_shape(df):
    return df.count, len(df.columns)
# why not include timestamp cols???
df.describe().show() #count, mean, stdev, min, max
df.summary().show()  #count, mean, stdev, min, 25%, 50%, 75%, max
```
