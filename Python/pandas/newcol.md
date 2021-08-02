# newcol

## split one col to two
```python
df[['cola','colb']] = df['col'].str.rsplit('_', 1, expand=True)
```
## newcol based on conditions on another col
```python
conditions = [
    (df['cnt'] <= 2),
    (df['cnt'] > 2) & (df['cnt'] <= 9),
    (df['cnt'] > 9) & (df['cnt'] <= 15),
    (df['cnt'] > 15)
    ]

#create a list of the values we want to assign for each condition
values = ['band1', 'band2', 'band3', 'band4']

#create a new column and use np.select to assign values to it using our lists as arguments
df['band'] = np.select(conditions, values)

#use pd.cut
#bins = [-np.inf,2,9,15,np.inf] #or
bins = [float('-inf'),2,9,15,float('inf')]
lbls = ['band1', 'band2', 'band3', 'band4]
df['band'] = pd.cut(x=df['cnt'], bins=bins, right=True, labels=lbls).astype(str) #change category to str
```
