# Threaded

## set threads
**Single machine scheduling**: Dask.dataframe will use the threaded scheduler by default with as many threads as you have logical cores in your machine.

The number of threads and pool implementation can be controlled by keyword arduments such as: `.compute(num_workers=4)`.

Or set the number of workers via env var:
```
dask.config.set('num_workers', 4)
```

## hanging
Numba and Dask aren't currently able to share threadpools, so using multi-threaded Numba and multi-threaded Dask can lead to app hanging.

Using single-threaded Dask, or using single-threaded Numba.
```
from umap import UMAP
UMAP utilizes @numba.njit(parallel=True) #False

from numba import njit
@njit(parallel=True) #False
os.environ["NUMBA_NUM_THREADS"] = "1"
```
