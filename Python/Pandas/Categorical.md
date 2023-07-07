# categorical

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
