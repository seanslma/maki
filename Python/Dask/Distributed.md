# Distributed

## default
```py
import dask
from dask.distributed import Client

client = Client() #n_workers=n_cores, threads_per_worker=1
client = Client(n_workers=2, threads_per_worker=1) #explicitely set the workers and threads
```
