# Delayed

## specify number of threads
```
from multiprocessing.pool import ThreadPool
import dask
dask.config.set(pool=ThreadPool(10))
```
