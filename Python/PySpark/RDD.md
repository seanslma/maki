# RDD (Resilient Distributed Dataset)

## Create RDD

## Cache RDD

## rdd performance
We should try to avoid using RDD as serialization and de-serialization are very expensive operations for Spark applications or any distributed systems - 
most of the time is spent only on serialization of data rather than executing the operations.
