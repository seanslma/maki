# lineplot

## line plot with figure size
will automatically plot x, y, z based on index ts.
```py
df = pd.DataFrame({'ts':ts, 'x': x, 'y': y, 'z': z}).set_index(ts)
plt.figure(figsize=(18,7))
sns.lineplot(data=df)
plt.show()
```
