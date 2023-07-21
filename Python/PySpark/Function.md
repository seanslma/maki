# Function

## lit
Literal
```py
df.select(concat('country', ', ', 'description')).show(5,0)      #wrong
df.select(concat('country', lit(', '), 'description')).show(5,0) #correct
df.select(concat('country', lit(', '), 'description').alias('cd')).show(5,0) #provide name
```

## col
Return a `col` expression
https://stackoverflow.com/questions/55105363/pyspark-dataframe-column-reference-df-col-vs-dfcol-vs-f-colcol
```py
df.withColumn('cd', when(df['InvoiceNo'].isin([536365, 541909]), 'CustomerID').otherwise('Country')).show(5,0) #ok
df.withColumn('cd', when(col('InvoiceNo').isin([536365, 541909]), 'CustomerID').otherwise('Country')).show(5,0) #better
df.withColumn('cd', when(col('InvoiceNo').isin([536365, 541909]), col('CustomerID')).otherwise(col('Country'))).show(5,0) #select cols, not string
```

`col` can be re-used as it's not df specific and can be used before the df is assigned.
```py
age = col('dob') / 365
if_expr = when(age < 18, 'underage').otherwise('adult')

df1 = df.read.csv(path).withColumn('age_category', if_expr)
df2 = df.read.parquet(path).select('*', age.alias('age'), if_expr.alias('age_category'))
```
