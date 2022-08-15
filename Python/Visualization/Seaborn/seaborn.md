# seaborn
https://seaborn.pydata.org/tutorial/axis_grids.html

```python
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
```python
sns.barplot(x='tip_pct', y='day', data=df, orient='h')
sns.barplot(x='tip_pct', y='day', data=df, hue='time', orient='h')
```

Use catplot() to combine a barplot() and a FacetGrid - data should not be in index:
```python
g = sns.catplot(
  kind="bar",
  data=tips, 
  x="sex", 
  y="total_bill",
  hue="smoker", 
  col="time",  
  sharey=False, 
  ci=None,   #remove error bars
  height=4, 
  aspect=.7,
)
#ylim, gridline, annotation
ylims = [[1.4,2], [1.2,1.8], [5,8],[3.5,5.5]]
for i, ax in enumerate(g.axes.ravel()):
    ax.set_ylim(ylims[i])
    ax.grid(b=True, which='major', color='black', linewidth=0.075)
    for c in ax.containers:
        labels = [f'{v.get_height():.3f}' for v in c]
        ax.bar_label(c, labels=labels, label_type='edge', rotation=90, fontsize=8) 
```

## hist
```python
sns.distplot(values, bins=100, color='k')
```
  
## scatter
```python
sns.regplot('m1', 'unemp', data=trans_data)
sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})
```

## facetgrid
```python
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

## relplot
```python
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
```python
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
