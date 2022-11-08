# Delayed

https://docs.dask.org/en/stable/delayed.html

## specify number of threads
```
from multiprocessing.pool import ThreadPool
import dask
dask.config.set(pool=ThreadPool(10))
```
## best practices
https://docs.dask.org/en/stable/delayed-best-practices.html
