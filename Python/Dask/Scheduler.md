# Scheduler

https://dask.pydata.org/en/latest/scheduler-overview.html#configuring-the-schedulers

## schedulers
- `threaded`: a scheduler backed by a thread pool
- `processes`: a scheduler backed by a process pool
- `single-threaded` (sync): a synchronous scheduler, good for debugging
- `distributed`: a distributed scheduler for executing graphs on multiple machines

## synchronous scheduler
good for debugging
```py
# As a context manager
with dask.config.set(scheduler='single-threaded'):
    x.sum().compute()

# Set globally
dask.config.set(scheduler='single-threaded') #processes
x.sum().compute()
```
