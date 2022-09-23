# Parallel
reuse session\
err: only one usage of each socket address\
Sessions are usually easy to use. Just wrap with requests.Session() as s: around your for loop, and then replace requests.get with s.get

https://iliauk.wordpress.com/2016/03/07/high-performance-python-sessions-async-multi-tasking/

## Ray
Ray is decentralized, meaning each machine runs its own scheduler, so any issues with a scheduled task are handled at the level of the individual machine, not the whole cluster.

## Dask
Dask uses a centralized scheduler that handles all tasks for a cluster.

## joblib
```python
#r = Parallel(n_jobs=1)(delayed(sqrt)(i**2) for i in range(10)) #one return value
#r = Parallel(n_jobs=1)(delayed(modf)(i/2.) for i in range(10)) #several return values
#res, i = zip(*r)
meth = 'threading' #joblib loky (default, not work), threading, and multiprocessing (not work)
Parallel(n_jobs=-3, backend=meth)(
    delayed(my_func)(p1, p2, yr, cols, new_cols) for yr in range(2000, 2022)
)
```

## multi-processing
https://research.wmz.ninja/articles/2018/03/on-sharing-large-arrays-when-using-pythons-multiprocessing.html

```python
import numpy as np
import multiprocessing as mp

# A global dictionary storing the variables passed from the initializer.
var_dict = {}

def init_worker(X, X_shape):
    # Using a dictionary is not strictly necessary. You can also use global variables.
    var_dict['X'] = X
    var_dict['X_shape'] = X_shape

def worker_func(i):
    # Simply computes the sum of the i-th row of the input matrix X
    X_np = np.frombuffer(var_dict['X']).reshape(var_dict['X_shape'])
    time.sleep(1) # Some heavy computations
    return np.asscalar(np.sum(X_np[i,:]))
def main():
    X_shape = (16, 1000000)
    # Randomly generate some data
    data = np.random.randn(*X_shape)

    X = RawArray('d', X_shape[0] * X_shape[1])

    # Wrap X as an numpy array so we can easily manipulates its data.
    X_np = np.frombuffer(X).reshape(X_shape)

    # Copy data to our shared array.
    np.copyto(X_np, data)

    # Start the process pool and do the computation.
    # Here we pass X and X_shape to the initializer of each worker.
    # (Because X_shape is not a shared variable, it will be copied to each child process.)
    with Pool(processes=4, initializer=init_worker, initargs=(X, X_shape)) as pool:
        result = pool.map(worker_func, range(X_shape[0]))
        print('Results (pool):\n', np.array(result))
    # Should print the same results.
    print('Results (numpy):\n', np.sum(X_np, 1))
```
