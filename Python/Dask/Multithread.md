# Multithread

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
