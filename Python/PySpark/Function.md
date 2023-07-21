# Function

## lit
Literal
```py
df.select(concat('country', ', ', 'description')).show(5,0)      #wrong
df.select(concat('country', lit(', '), 'description')).show(5,0) #correct
```

## col
https://stackoverflow.com/questions/55105363/pyspark-dataframe-column-reference-df-col-vs-dfcol-vs-f-colcol
