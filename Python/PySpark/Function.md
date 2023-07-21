# Function

## lit
Literal
```py
df.select(concat('country', ', ', 'description'))      #wrong
df.select(concat('country', lit(', '), 'description')) #correct
df.select(concat('country', lit(', '), 'description').alias('cd')) #provide name
```

## col
Return a `col` expression
https://stackoverflow.com/questions/55105363/pyspark-dataframe-column-reference-df-col-vs-dfcol-vs-f-colcol
```py
df.withColumn('typ', when(df['id'].isin([1, 2]), 'animal').otherwise('plant')) #ok
df.withColumn('typ', when(col('id').isin([1, 2]), 'animal').otherwise('plant')) #better
df.withColumn('typ', when(col('id').isin([1, 2]), col('animal')).otherwise(col('plant'))) #select cols, not string
```

`col` can be re-used as it's not df specific and can be used before the df is assigned.
```py
age = col('dob') / 365
if_expr = when(age < 18, 'underage').otherwise('adult')

df1 = df.read.csv(path).withColumn('age_category', if_expr)
df2 = df.read.parquet(path).select('*', age.alias('age'), if_expr.alias('age_category'))
```
