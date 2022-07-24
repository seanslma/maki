# CPU

https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/

Pod scheduling is based on requests. A Pod is scheduled to run on a Node only if the Node has enough CPU resources available to satisfy the Pod CPU request.

## cpu count
Inside a pod, 
```
grep -c ^processor /proc/cpuinfo #should agree with multiprocessing.cpu_count()
```
