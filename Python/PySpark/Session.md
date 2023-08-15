# Session

## create session
```py
from pyspark.sql import SparkSession
spark = (
    SparkSession
    .builder
    .appName('spark-local')
    .master(local[*])    
    .config("spark.memory.offHeap.enabled","true")
    .config("spark.memory.offHeap.size","10g")
    .getOrCreate()
)
...
spark.stop()
```

## builder.master
Sets the Spark master URL to connect to, such as 
- `local[*]`: run locally with all cores
- `local[4]`: run locally with 4 cores
- `spark://<master-ip>:7077`: run on a Spark standalone cluster
- `yarn`: yse YARN as cluster manager
- cli: `spark-submit --master local[2] my_app.py`
