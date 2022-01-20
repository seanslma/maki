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
```
#df date must be string
fig, ax = plt.subplots(figsize=(10,8))
g = sns.heatmap(df, ax=ax, cmap='coolwarm', vmin=df.min().min(), vmax=df.max().max())
fig.suptitle('My first heatmap')
#custom date labels
getattr(ax, f'set_xticks')(xtks)      #locations of xtls in df.columns
getattr(ax, f'set_xticklabels')(xtls) #a list of date strings
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True)
```
