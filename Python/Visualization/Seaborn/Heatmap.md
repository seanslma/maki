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

#remove x labels
sns.heatmap(df, xticklabels=False)

#remove color bar
sns.heatmap(df, cbar=False)

#skip axis labels
sns.heatmap(df, xticklabels=3) #keep first in 3
```
