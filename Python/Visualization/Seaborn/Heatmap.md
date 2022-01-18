# Heatmap

ridge plot\
https://python.plainenglish.io/ridge-plots-with-pythons-seaborn-4de5725881af

## create df
```
import numpy as np
import pandas as pd
import seaborn as sns
 
df = pd.DataFrame(np.random.random((10,7)), columns=['a','b','c','d','e','f','g'])
sns.heatmap(df)
```

## special
```
#annotate each cell with value
sns.heatmap(df, annot=True, annot_kws={'size': 6})

#grid lines
sns.heatmap(df, linewidths=1, linecolor='blue')

#remove x-axis labels
sns.heatmap(df, xticklabels=False)

#replace x-axis labels
xtls = ['q','r','s','t','u','v','w']
sns.heatmap(df, xticklabels=xtls)

#remove color bar
sns.heatmap(df, cbar=False)

#skip axis labels
sns.heatmap(df, xticklabels=3) #keep first in 3
```

## custom date labels
`AxTransformer` enables conversion from data coordinates to tick locations, and `set_date_ticks` allows custom date ranges to be applied to plots.

https://stackoverflow.com/questions/40925458/date-axis-in-heatmap-seaborn
```
getattr(ax, f'set_{axis}ticks')(tks)
getattr(ax, f'set_{axis}ticklabels')(dt_rng.strftime(date_format))

ax.tick_params(axis=axis, which='both', bottom=True, top=False, labelbottom=True)
```
