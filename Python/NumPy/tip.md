# Tip

## rows with same values
```python
# b is the index for rows with the same value in cols j:k
d = df.iloc[:,j:k].values
v = df.iloc[:,[j]].values
b = np.bitwise_and.reduce(d==v,axis=1)
```
