# tip

## astype(int)
will does a conversion toward zero, not rounding, try this
`s1.round().astype(int)`

## np.where(cond, pd.Timestamp(), pd.Timestamp())
will change pd.Timestamp() to inetger, the right way to use where
`np.where(cond, pd.Timestamp(), np.datetime64())`

## list of lists to csv
```py
csv.writer(open('out.csv', 'w', newline='')).writerows(lls)
```

## set index in each group starting from 0
```py
df['idx'] = df.groupby('grp_id').cumcount()
```
