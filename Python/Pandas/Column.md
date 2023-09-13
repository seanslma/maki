# Column

## set columns in chained method
```py
df = df.set_axis(columns, axis=1)
```

## split one col to two
```py
df[['cola','colb']] = df['col'].str.rsplit('_', 1, expand=True)
```

## newcol from two col levels (year and quarter)
```py
qt_yr = [f'Q{quarter}{str(year)[2:]}' for year, quarter in df.columns]
```
## merge df col levels
```py
data = {
    ('A', 'X'): [1, 2, 3],
    ('A', 'Y'): [4, 5, 6],
    ('B', 'X'): [7, 8, 9],
    ('B', 'Y'): [10, 11, 12]
}
df = pd.DataFrame(data)
df.columns = df.columns.map('_'.join)
df.columns = [f'{i}_{j}' if j != '' else f'{i}' for i,j in df.columns]
```

## newcol based on conditions on another col
```py
#use np.select
cons = [(df['cnt'] <= 2), (df['cnt'] > 2) & (df['cnt'] <= 9), (df['cnt'] > 9) & (df['cnt'] <= 15), (df['cnt'] > 15)]
lbls = ['band1', 'band2', 'band3', 'band4'] #label for each condition
df['band'] = np.select(cons, lbls)

#use pd.cut
#bins = [-np.inf,2,9,15,np.inf] #or
bins = [float('-inf'),2,9,15,float('inf')]
lbls = ['band1', 'band2', 'band3', 'band4]
df['band'] = pd.cut(x=df['cnt'], bins=bins, right=True, labels=lbls).astype(str) #change category to str
```
