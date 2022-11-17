# Configuration

https://docs.dask.org/en/stable/configuration.html

## Example
```
export DASK_DISTRIBUTED__WORKERS__MEMORY__SPILL=0.85
dask.config.set({"distributed.workers.memory.spill": 0.85})
```

## comm
`distributed.comm.zstd.threads  0`: 
Number of threads to use. 0 for single-threaded, -1 to infer from cpu count.
