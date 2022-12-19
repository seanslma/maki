# Distributed

## default
```py
import dask
from dask.distributed import Client

client = Client() #[n_workers=1, threads_per_worker=n_cores] similar to threads
client = Client(n_workers=2, threads_per_worker=1) #explicitely set the workers and threads

client.close()
```

## Standalone Python scripts
must put the code in `main`
```py
if __name__ == '__main__':  # This avoids infinite subprocess creation
   from dask.distributed import Client
   client = Client()
```
