# SLURM

https://www.run.ai/guides/slurm

SLURM is a system for managing and scheduling Linux clusters. It is open source, fault tolerant and scalable, suitable for clusters of various sizes.

## example
```py
from dask_jobqueue import SLURMCluster
from dask.distributed import Client
import dask

import matplotlib.pyplot as plt
import socket
import time
import os

# Submit workers as slurm job
cluster = SLURMCluster(
    cores=os.environ.get("SLURM_CPUS_PER_TASK",2),
    processes=1,
    memory="4GB",
    walltime="00:00:10",
    queue="batch",
    interface="Ethernet0",
)

num_workers = os.environ.get("SLURM_NTASKS",1)
cluster.scale(num_workers)

# Connect to distributed cluster and override default
client = Client(cluster)
client.wait_for_workers()

def inc(x):
    time.sleep(2)
    return x + 1

def dbl(x):
    return x * 2

def add(x, y):
    time.sleep(2)
    return x + y

data = [1, 2, 3, 4, 5, 6]

output = []
for v in data:
    a = dask.delayed(inc)(v)
    b = dask.delayed(dbl)(v)
    c = dask.delayed(add)(a, b)
    output.append(c)

# Second approach as a delayed function
total = dask.delayed(sum)(output)
total.visualize(filename='task_graph.svg')
# parallel execution workers
t0 = time.time()
results = total.compute()
print(f'{time.time() - t0:.3f}: {results}')

#### Very important ############
cluster.close()
```
