# Setup

## 
```py
from pyspark.sql import SparkSession
spark = SparkSession \
.builder \
.appName("Python Spark Logistic Regression example") \
.config("spark.some.config.option", "some-value") \
.getOrCreate()
```
