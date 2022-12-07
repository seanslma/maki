# Scheduler

https://dask.pydata.org/en/latest/scheduler-overview.html#configuring-the-schedulers

## synchronous scheduler
good for debugging
```
dask.config.set(scheduler='single-threaded')
```
