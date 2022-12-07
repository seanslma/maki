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

## delayed.compute vs client.compute
https://github.com/dask/distributed/issues/733

`delayed.compute()` is a shortcut of `f=client.compute(d); f.result()` except worker_client (fixed so no exception)
