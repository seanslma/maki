# Test

## create a large dataframe
```py
import numpy as np
import pandas as pd
np.random.seed(0)

nrow = 150000
ncol = 45
columns = [f'c{i}' for i in range(ncol)]
df = pd.DataFrame(data=np.random.rand(nrow, ncol),columns=columns)
df.to_parquet('data.parquet')
```
