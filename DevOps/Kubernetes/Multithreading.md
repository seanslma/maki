# Multithreading

https://stackoverflow.com/questions/53276398/kubernetes-cpu-multithreading

https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/

## cpu count
```sh
grep -c ^processor /proc/cpuinfo #should agree with multiprocessing.cpu_count()
```

## cpu settings
Threads = 2 does not mean the cpu requests should be 2. Should be tested?

The `args` section of the configuration file provides arguments for the container when it starts. The -cpus "2" argument tells the Container to attempt to use 2 CPUs.
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cpu-2
  namespace: cpu-test
spec:
  containers:
  - name: cpu-ctr-2
    image: vish/stress
    resources:
      requests:
        cpu: 500m
      limits:
        cpu: "1"
    args:
    - -cpus
    - "2"
```
