# DataFrame

## from list
https://stackoverflow.com/questions/65070639/create-empty-dataframe-from-list-is-x4-times-slower-than-from-emptyrdd

creating empty DataFrame from list is 4-100 times slower than from emptyRDD()
```py
spark.createDataFrame([], schema)
spark.createDataFrame(spark.sparkContext.emptyRDD(), schema)
```

Reason:
- `spark.sparkContext.emptyRDD()` creates an RDD with zero partitions
- `spark.createDataFrame([], schema)` creates a DataFrame with at least one partition. The overhead is due to tasks on empty partitions.
