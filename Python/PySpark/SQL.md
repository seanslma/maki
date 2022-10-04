# SQL

## create view and table
```
df.createOrReplaceTempView("viw") #df to temp view
saveAsTable                       #df to table
spark.catalog.createTable         #empty table
spark.catalog.createExternalTable #external table
```

## Spark SQL API
```
df = spark.sql("
    SELECT id, name, price \
    FROM products \
    WHERE category IN ('Mountain Bikes', 'Road Bikes')
")
display(df)
```

## SQL magic
```
%sql

SELECT category, COUNT(id) AS cnt
FROM products
GROUP BY category
ORDER BY category
```
