# seaborn
https://seaborn.pydata.org/tutorial/axis_grids.html

```py
#show NaN values in df
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

#show numbers count in a df col
sns.set_style('whitegrid')
sns.countplot(x='c1', data=df)
sns.countplot(x='c1', hue='c2', data=df, pallete='RdBu_r')

#distribution of df col
sns.distplot(df['c1'].dropna(), kde=False, bins=30)
df['c1'].plot.dist(bins=30)
df['c1'].hist(bins=30, figsize=(10,4))
df['c1'].iplot(kind='hist', bins=30)
```

## bar
```py
sns.barplot(x='tip_pct', y='day', data=df, orient='h')
sns.barplot(x='tip_pct', y='day', data=df, hue='time', orient='h')
```

Use catplot() to combine a barplot() and a FacetGrid - data should not be in index:
```py
g = sns.catplot(
    kind='bar',
    data=tips,
    x='sex',
    y='total_bill',
    row='smoker',
    col='time',
    sharey=False,
    ci=None,                  #remove error bars
    order=['1H', '2H', '4H'], #x order
    height=4,
    aspect=.7,
)
#ylim, gridline, annotation
ylims = (
    d.groupby(['smoker','time'])
    .agg(vmin=('val', 'min'), vmax=('val', 'max'))
    .assign(
        tmin=lambda x: x[['vmin']].groupby(['smoker']).transform('min'),
        tmax=lambda x: x[['vmax']].groupby(['smiker']).transform('max'),
    )
    .drop(columns=['vmin','vmax'])
    .assign(tmin=lambda x: x.tmin * 0.99)
    .to_records(index=False)
)
for i, ax in enumerate(g.axes.ravel()):
    ax.set_ylim(ylims[i])
    ax.grid(visible=True, which='major', color='black', linewidth=0.075)
    for c in ax.containers:
        labels = [f'{v.get_height():.3f}' for v in c]
        ax.bar_label(c, labels=labels, label_type='edge', rotation=90, fontsize=8)
```

## hist
```py
sns.distplot(values, bins=100, color='k')
```

## scatter
```py
sns.regplot('m1', 'unemp', data=trans_data)
sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})
```

## facetgrid
Faceting is the act of breaking data variables up across multiple subplots and combining those subplots into a single figure
```py
g = sns.FacetGrid(df, col='class')
g = g.map(sns.kdeplot, 'sepal_length')
```

```py
sns.factorplot(kind='bar', x='day', y='tip_pct',
               col='smoker', hue='time', data=tips[tips.tip_pct < 1])

#split row and col
g = sns.FacetGrid(tip, row='sex', col='time', hue='smoker', height=4)
g.map(plt.scatter, "total_bill", "tip")
g.add_legend()

#add hue
g = sns.FacetGrid(tip, row='day', row_order = tip.day.value_counts().index, height=1.5, aspect=4)
g.map(sns.distplot, "total_bill", hist=False)

#settings
g.set_titles(row_template = '{row_name}', col_template = '{col_name}') #set new titles
g.set_axis_labels("Total bill (US Dollars)", "Tip")
g.set(xticks=[10, 30, 50], yticks=[2, 6, 10])
g.fig.subplots_adjust(wspace=.02, hspace=.02)
```

## pairplot
plot a grid of pairwise relationships in a dataset
```py
sns.pairplot(iris)

from pandas.plotting import scatter_matrix

fig, ax = plt.subplots(figsize=(12,12))
scatter_matrix(iris, alpha=1, ax=ax)
```

## relplot
```py
g = sns.relplot(kind='line', data=df, x='fye', y='val',
                row='scen', hue='reg', style='fit', height=4, aspect=1.5,
                facet_kws={'sharey': True, 'sharex': False})
g._legend.set_bbox_to_anchor([0.35,0.92])

[plt.setp(ax.texts, text="") for ax in g.axes.flat] #remove the original texts
g.set_titles(row_template = '{row_name}', col_template = '{col_name}') #set new titles

#settings
g.set_axis_labels("Total bill (US Dollars)", "Tip")
g.set(xticks=[10, 30, 50], yticks=[2, 6, 10])
g.fig.subplots_adjust(wspace=.02, hspace=.02)
```

## custom func
```py
from scipy import stats
def quantile_plot(x, **kwargs):
    quantiles, xr = stats.probplot(x, fit=False)
    plt.scatter(xr, quantiles, **kwargs)
g = sns.FacetGrid(tips, col="sex", height=4)
g.map(quantile_plot, "total_bill")

def qqplot(x, y, **kwargs):
    _, xr = stats.probplot(x, fit=False)
    _, yr = stats.probplot(y, fit=False)
    plt.scatter(xr, yr, **kwargs)
g = sns.FacetGrid(tips, col="smoker", height=4)
g.map(qqplot, "total_bill", "tip")
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
    sm._A = [] #fake up the array of the scalar mappable. not required from verion 3.1
    cbar = plt.colorbar(sm,ax=ax,ticks=tks,label='job create time')
    cbar.ax.set_yticklabels(lbs)
```
