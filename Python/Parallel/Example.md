# Example

## multiprocessing
```py
# not support asyncio
from multiprocessing.pool import ThreadPool
n_jobs = min(cpu_count(), len(safe_paths))

# option 1, pool.map actually call map_async
with ThreadPool(processes=n_jobs) as pool:
    dfs = pool.map(lambda path: read_parquet_func(fs, path, columns, filters), paths)

# option 2
with ThreadPool(processes=n_jobs) as pool:
  results = [
      pool.apply_async(read_parquet_func, args=(fs, path, columns, filters))
      for path in paths
  ]
  dfs = [sync(result.get()) for result in results]
```

## slower `ThreadPool`
https://superfastpython.com/threadpoolexecutor-slower/

This is because Python threads are constrained by the Global Interpreter Lock, or GIL.
The GIL uses synchronization to ensure that only one thread can execute instructions at a time within a Python process.
If the task is CPU bounded then it's worse than a single for loop.

## concurrent
```py
# support both sync and async
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
    futures = [
        executor.submit(
            read_parquet_func, fs, path, columns, filters
        )
        for path in paths if fs.exists(path)
    ]
    dfs = [future.result() for future in futures]
```

## joblib
```py
from joblib import cpu_count, delayed, Parallel
delayed_func = [
    delayed(read_parquet_func)(fs, path, columns, filters)
    for path in paths if fs.exists(path)
]

n_jobs = min(cpu_count(), len(delayed_func))
with Parallel(n_jobs=n_jobs, prefer='threads') as parallel_pool:
    dfs = parallel_pool(delayed_func)
```
