# Session

## create session
```py
from pyspark.sql import SparkSession
spark = (
    SparkSession
    .builder
    .appName('spark-local')
    .master('local[*]')
    .config('spark.memory.offHeap.enabled', 'true')
    .config('spark.memory.offHeap.size', '10g')
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

## default partitions casued slow performance
https://stackoverflow.com/questions/34625410/why-does-my-spark-run-slower-than-pure-python-performance-comparison

By default when run spark in SQL Context or Hive Context it will use 200 partitions by default. This will significantly slow down the performance when running locally.
```py
spark.conf.set('spark.sql.shuffle.partitions', 1)
```
