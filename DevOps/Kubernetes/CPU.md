# CPU

https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/

Pod scheduling is based on requests. A Pod is scheduled to run on a Node only if the Node has enough CPU resources available to satisfy the Pod CPU request.

## cpu count
Inside a pod, 
```
grep -c ^processor /proc/cpuinfo #should agree with multiprocessing.cpu_count()
```

## cpu stalls
https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html

When the cpu is high, most likely the cpu stalls. Temperature trips stalling the processor???

Stalled means the processor was not making forward progress with instructions, and usually happens because it is waiting on memory I/O. 

"I think many people interpret high %CPU to mean that the processing unit is the bottleneck, which is wrong."
