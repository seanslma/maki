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
- `local[1]`: run locally with 1 core
   - much faster than `local[*]` for `spark.createDataFrame` but
   - for data processing we need multiple threads otherwise can be very slow
- `spark://<master-ip>:7077`: run on a Spark standalone cluster
- `yarn`: yse YARN as cluster manager
- cli: `spark-submit --master local[2] my_app.py`

## spark.default.parallelism
https://sparkbyexamples.com/spark/difference-between-spark-sql-shuffle-partitions-and-spark-default-parallelism/

- only applicable to RDD 
- default value is the number of all cores on all nodes in a cluster
- on local, it is set to the number of cores on your system

For RDD, transformations like `reduceByKey()`, `groupByKey()`, `join()` triggers the data shuffling. 
Set the desired partitions for shuffle operations.
```py
spark.conf.set('spark.default.parallelism', 100)
```

## spark.sql.shuffle.partitions
- only works with DataFrame
- default value for this configuration is 200

For DataFrame, transformations like `groupBy()`, `join()` triggers the data shuffling. 
Set the value using:
```py
spark.conf.set('spark.sql.shuffle.partitions', 100)
```

Set the values in cli
```sh
spark-submit --conf spark.sql.shuffle.partitions=100 --conf spark.default.parallelism=100
```

## default partitions casued slow performance
https://stackoverflow.com/questions/34625410/why-does-my-spark-run-slower-than-pure-python-performance-comparison

Spark shuffle is a very expensive operation as it moves the data between executors or even between worker nodes in a cluster. 
Spark automatically triggers the shuffle when we perform aggregation and join operations on RDD and DataFrame.

By default when run spark in SQL Context or Hive Context it will use 200 partitions by default. 
This will significantly slow down the performance when running locally.
```py
spark.conf.set('spark.sql.shuffle.partitions', 1)
```
