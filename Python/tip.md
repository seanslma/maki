# tip

## remove empty items
```python
l2 = list(filter(None, l1))
```

## diff between two lists
```python
s1 = set(l1).difference(l2)
```  
## list of lists to csv
```python
csv.writer(open('out.csv', 'w', newline='')).writerows(lls)
```  
## set index in each group starting from 0
```python
df['idx'] = df.groupby('grp_id').cumcount()
```  
