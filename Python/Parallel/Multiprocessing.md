# Multiprocessing
- threads share memory with the main process
- processes have independent memory spaces. When a process ends, the OS cleans up its memory

## Use `multipricessing.Process`
```py
import os
import time
import multiprocessing

def worker(data_size_mb):
    pid = os.getpid()
    print(f'[PID {pid}] Allocating {data_size_mb}MB')
    # Simulate large memory usage
    big_data = bytearray(data_size_mb * 1024 * 1024)
    time.sleep(2)
    print(f'[PID {pid}] Done.')
    # need to use multiprocessing.Queue or multiprocessing.Pipe to return values

if __name__ == '__main__':
    processes = []
    for _ in range(2):  # Spawn 3 separate processes
        p = multiprocessing.Process(target=worker, args=(100,))  # 100MB each
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print('All worker processes completed.')
```

## Use `multiprocessing.Pool`
```py
import os
import time
import multiprocessing

def worker(data_size_mb):
    pid = os.getpid()
    print(f'[PID {pid}] Allocating {data_size_mb}MB')
    # Simulate large memory usage
    big_data = bytearray(data_size_mb * 1024 * 1024)
    time.sleep(2)
    print(f'[PID {pid}] Done.')
    return f'Process {pid} completed'

if __name__ == '__main__':
    with multiprocessing.Pool(processes=2) as pool:
        # should not use a class method as worker!
        results = pool.map(worker, [100, (100)])  # 2 tasks of 100MB each

        # # different workers
        # result1 = pool.apply_async(worker1, args=args1)
        # result2 = pool.apply_async(worker2, args=args2)
        # results = [result1.get(), result2.get()]

    print('\nAll tasks completed.')
    for r in results:
        print(r)
```
