# Example

## multiprocessing
```py
from multiprocessing.pool import ThreadPool
n_jobs = min(cpu_count(), len(safe_paths))

# option 1
with ThreadPool(processes=n_jobs) as pool:
    dfs = pool.map(lambda path: read_parquet_func(fs, path, columns, storage_options), safe_paths)

# option 2
with ThreadPool(processes=n_jobs) as pool:
  results = [
      pool.apply_async(read_parquet_func, args=(fs, path, columns, storage_options))
      for path in safe_paths
  ]
  dfs = [sync(result.get()) for result in results]
```

## concurrent
```py
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
    futures = [
        executor.submit(
            read_parquet_func, fs, path, columns, storage_options
        )
        for path in path_list if fs.exists(path)
    ]
    dfs = [future.result() for future in futures]
```

## joblib
from joblib import cpu_count, delayed, Parallel
```py
  delayed_func = [
      delayed(read_parquet_func)(fs, path, columns, storage_options)
      for path in path_list if fs.exists(path)
  ]

  n_jobs = min(cpu_count(), len(delayed_func))
  with Parallel(n_jobs=n_jobs, prefer='threads') as parallel_pool:
      dfs = parallel_pool(delayed_func)
```
