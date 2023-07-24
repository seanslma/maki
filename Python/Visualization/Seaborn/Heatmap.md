# Heatmap

ridge plot\
https://python.plainenglish.io/ridge-plots-with-pythons-seaborn-4de5725881af

## create df
```py
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.DataFrame(np.random.random((10,7)), columns=['a','b','c','d','e','f','g'])
sns.heatmap(df)
```

## example
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
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# Loop over data dimensions and create text annotations.
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        text = ax.text(
            j, i, np.around(corr.iloc[i, j], decimals=2),
            ha='center', va='center', color='black'
        )
```

## special
```py
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
```py
#df date must be string
fig, ax = plt.subplots(figsize=(10,8))
g = sns.heatmap(df, ax=ax, cmap='coolwarm', vmin=df.min().min(), vmax=df.max().max())
fig.suptitle('My first heatmap')
#custom date labels
getattr(ax, 'set_xticks')(xtks)      #locations of xtls in df.columns
getattr(ax, 'set_xticklabels')(xtls) #a list of date strings
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True)
```
