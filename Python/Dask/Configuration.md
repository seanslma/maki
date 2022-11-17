# Configuration

https://docs.dask.org/en/stable/configuration.html

## Example
```
export DASK_DISTRIBUTED__WORKERS__MEMORY__SPILL=0.85
dask.config.set({"distributed.workers.memory.spill": 0.85})
```

## comm
- `distributed.comm.zstd.threads  0`: 
  Number of threads to use. 0 for single-threaded, -1 to infer from cpu count.

## worker
- `distributed.worker.lifetime.duration  None`
  The time after creation to close the worker, like "1 hour"
- `distributed.worker.lifetime.restart  False`
  Do we try to resurrect the worker after the lifetime deadline?
