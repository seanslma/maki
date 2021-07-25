# newcol

```python
conditions = [
    (df['likes_count'] <= 2),
    (df['likes_count'] > 2) & (df['likes_count'] <= 9),
    (df['likes_count'] > 9) & (df['likes_count'] <= 15),
    (df['likes_count'] > 15)
    ]

# create a list of the values we want to assign for each condition
values = ['tier_4', 'tier_3', 'tier_2', 'tier_1']

# create a new column and use np.select to assign values to it using our lists as arguments
df['tier'] = np.select(conditions, values)
```