# Figure

## save figure
```
fig = go.Figure()
    fig.update_layout(
        width=18, #pixel, CM_TO_PIXEL = 37.7952755906
        height=9, #pixel
        margin=go.layout.Margin(
            l=10, #default 80
            r=3, #default 80
            b=5, #default 80
            t=10  #default 100
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
    )
fig.write_image(imgfile, scale=1.5)
```

## rotate axis labels
```py
import matplotlib.pyplot as plt
#set font and plot size to be larger
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})
df['rating'].plot(kind='hist', title='Rating')
df.plot(kind='scatter', x='speed', y='distance', title='my plot')
```

## rotate axis labels
```py
for tick in ax.get_xticklabels():
    tick.set_rotation(90)
```

## faceting
Faceting is the act of breaking data variables up across multiple subplots and combining those subplots into a single figure
```py
g = sns.FacetGrid(df, col='class')
g = g.map(sns.kdeplot, 'sepal_length')
```

## pairplot
plot a grid of pairwise relationships in a dataset
```py
sns.pairplot(iris)

from pandas.plotting import scatter_matrix

fig, ax = plt.subplots(figsize=(12,12))
scatter_matrix(iris, alpha=1, ax=ax)
```
## heatmap
```py
sns.heatmap(iris.corr(), annot=True)

# get correlation matrix
corr = iris.corr()
fig, ax = plt.subplots()
# create heatmap
im = ax.imshow(corr.values)

# set labels
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2),
                       ha="center", va="center", color="black")
```


## color bar
```py
def get_cbar_colors(dts):
    z = pd.to_timedelta(dts).total_seconds()
    zmin = min(z)
    zmax = max(z)

    tks = np.arange(0, 1.1, 0.1)
    sec_minmax = zmax - zmin
    secs = tks * sec_minmax
    dts = sec2dt(secs, min(dts))
    lbs = [f'{dt.year}-{dt.month:02}' for dt in dts]

    #cmap = plt.cm.get_cmap('jet',10) #viridis, jet
    colors = {'FUCHSIA':'#FF00FF','PURPLE':'#800080','MAROON':'#800000','GRAY':'#808080','NAVY':'#000080',
              'BLUE':'#0000FF','TEAL':'#008080','GREEN':'#008000','LIME':'#00FF00','AQUA':'#00FFFF'}
    cmap = clrs.ListedColormap(colors.values())
    normalize = plt.Normalize(vmin=0, vmax=1)
    colors = [cmap(value) for value in (z - zmin) / (zmax - zmin)]

    return tks, lbs, colors, cmap, normalize

def plot_cbar(ax, tks, lbs, cmap, normalize):
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=normalize)
    sm._A = [] #fake up the array of the scalar mappable.  not required from verion 3.1
    cbar = plt.colorbar(sm,ax=ax,ticks=tks,label='job create time')
    cbar.ax.set_yticklabels(lbs)
```
