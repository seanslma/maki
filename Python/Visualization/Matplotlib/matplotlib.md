# matplotlib

## config
first parameter can be 'figure' , 'axes' , 'xtick' , 'ytick' , 'grid' , 'legend'
```python
plt.rc('figure', figsize=(10, 10))
font_options = {
  'family': 'monospace',
  'weight': 'bold',
  'size': 'small'}
plt.rc('font', **font_options)
```

## subplot
```python
fig, axes = plt.subplots(2, 3, sharex=True, sharey=True)
subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
```

## annotation
```python
dat = [
  (datetime(2007,10, 11), 'Dog'),
  (datetime(2008, 3, 12), 'Bear'),
  (datetime(2008, 9, 15), 'Horse')]
for date, label in dat:
  ax.annotate(label, xy=(date, spx.asof(date) + 75),
    xytext=(date, spx.asof(date) + 225),
    arrowprops=dict(facecolor='black', headwidth=4, width=2, headlength=4),
    horizontalalignment='left', verticalalignment='top')
```

## drawing
```python
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color='g', alpha=0.5)
ax.add_patch(rect)
```

## save fig
```python
plt.savefig('figpath.png', dpi=400, bbox_inches='tight')
```
