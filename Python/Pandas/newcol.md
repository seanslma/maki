# newcol

## split one col to two
```python
df[['cola','colb']] = df['col'].str.rsplit('_', 1, expand=True)
```
## newcol based on conditions on another col
```python
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
