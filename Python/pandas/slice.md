# slice

## slicing
```python
df.ix[[0, 2], 'A'] #obsolete
df.at[ridx, 'A']
df.iat[1,2] #get a single value

#loc to index
df.loc[df.index[[0, 2]], 'A']

#index to loc
df.iloc[[0, 2], df.columns.get_loc('A')]
df.iloc[[0, 2], df.columns.get_indexer(['A', 'B'])]

msk = [True, False, True]
df.loc[msk, df.columns[2:]]

#multiIndex slicing
idx = pd.IndexSlice
df.loc[idx[:, r_level1], idx[:, 'c_level1']]
```

## select rows using list
  df[df['A'].isin([3, 6])]

## chained assignments
The **SettingWithCopyWarning** was created to flag potentially confusing chained assignments. With chained assignment, it is generally difficult to predict whether a view or a copy is returned. When filtering DataFrames, it is possible slice/index a frame to return either a view, or a copy. 

such as:
  df[df['a'] > 2]['b'] = new_val     #new_val not set in df as a copy is made
  df.loc[df['a'] > 2, 'b'] = new_val #good

  df2 = df[df.A > 5]                 #boolean indexing will return a view
  df2.loc[df2.C == 5, 'D'] = 123     #should be --->
  df2 = df[df.A > 5].copy()          #good




