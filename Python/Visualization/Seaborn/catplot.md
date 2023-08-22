# catplot
https://seaborn.pydata.org/generated/seaborn.catplot.html

- `order`, `hue_order`: *lists of strings, optional*
Order to plot the categorical levels in; otherwise the levels are inferred from the data objects.

- `row_order`, `col_order`: *lists of strings, optional*
Order to organize the rows and/or columns of the grid in, otherwise the orders are inferred from the data objects.

## catplot with bar type
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
    ci=None,                   #remove error bars
    order=['male', 'dfemale'], #order for the x value
    height=4,
    aspect=0.7,
)
#ylim, gridline, annotation
# get the (min, max) of the val column for each group (smoker, time)
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
