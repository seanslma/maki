# categorical

https://towardsdatascience.com/staying-sane-while-adopting-pandas-categorical-datatypes-78dbd19dcd8a

## benefit
- reduce memory usage
- runtime performance optimization
- library integrations

## convert
```py
fruit_cat = df['fruit'].astype('category')
my_cat = pd.Categorical(['foo', 'bar', 'baz', 'foo', 'bar'])
my_cat_2 = pd.Categorical.from_codes(codes, categories, ordered=True)
my_cat_2 = my_cats_2.as_ordered() #change to ordered
```

## method
as_ordered, as_unordered, rename_categories, set_categories,
add_categories, remove_categories, remove_unused_categories, reorder_categories
```py
my_cat.cat.codes
my_cat.cat.categories
my_cat.cat.set_categories(['a','b','c','d'])
#remove unobserved categories
cat_s3 = cat_s[cat_s.isin(['a', 'b'])]
cat_s3.cat.remove_unused_categories()
```

## operating on categorical columns
category can be much faster
```py
df['str'].str.upper()
df['cat'].str.upper() #but became string type again
df['cat'].cat.rename_categories(str.upper) #even faster and still cat type
```
`df['cat'].dtype.categories` contains the unique categorical values thus
can work on these values directly if there are no appropriate cat functions.

## merge
`merge` dfs can lead category columns becoming string type 
- merge(str, cat) => str
- merge(cat, cat) => str
- df.astype({'cat': df2['cat'].dtype}).merge(df2, on='cat') => cat

## groupby
When group on a categorical datatype, by default it will group on every value in the datatype even if it isn't present in the data itself.

Using `observed=True` to solve the issue: `df.groupby('cat', observed=True)['val'].mean()`
