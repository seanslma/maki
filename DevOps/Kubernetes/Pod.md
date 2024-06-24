# Pod

## General
```sh
kubectl get pods                #check status
kubectl get pods -o wide        #show more info such node
kubectl describe pod <pod-name> #check events
kubectl get event --field-selector involvedObject.name=<pod-name>
kubectl logs <pod-name>         #check logs
kubectl exec -it <pod-name> -c <container-name> -- bash #connect to pod
```

## pending pods
```sh
kubectl get pods --field-selector=status.phase=Pending
```

## delete failed pods
```sh
kubectl delete pods -A  --field-selector='status.phase=Failed'
```

## forece delete
```sh
kubectl delete pod <pod-name> --grace-period=0 --force
kubectl delete pod <pod-name> --grace-period=0 --force -n <namespace>
```

## pod stuck on terminating
- https://stackoverflow.com/questions/35453792/pods-stuck-in-terminating-status
- https://github.com/kubernetes/kubernetes/issues/51835
```sh
kubectl delete pod <pod-name> --grace-period=0  --force # if does not work, try
kubectl patch pod <pod-name> -n <namespace> -p '{"metadata":{"finalizers":null}}' 
```

## port forward
https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/

Use Port Forwarding to Access Applications in a Cluster.
```sh
kubectl port-forward pod/<pod-name> <local-port>:<pod-port>
```

## pod cpu and memory usage
run into the pod
```sh
cat /sys/fs/cgroup/cpu/cpuacct.usage  #nanosecond
cat /sys/fs/cgroup/memory/memory.usage_in_bytes | awk '{ mem = $1 / 1024 / 1024 / 1024 ; print mem "GB" }'
```

## check pod throttling rate
- `nr_periods`: Total schedule period
- `nr_throttled`: Total throttled period out of nr_periods
- `throttled_time`: Total throttled time in ns
```sh
#run into the pod
cat /sys/fs/cgroup/cpu/cpu.stat
```

## Kubectl run command
https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#notes
When you override the default Entrypoint and Cmd for a Container, these rules apply:
- do not supply `command` or `args`, the defaults defined in the Docker image are used.
- supply a `command` but no `args`, only the supplied command is used. The default EntryPoint and the default Cmd defined in the Docker image are ignored.
- supply only `args`, the default Entrypoint defined in the Docker image is run with the args that you supplied.
- supply a `command` and `args`, the default Entrypoint and the default Cmd defined in the Docker image are ignored. Your command is run with your args.

## create a pod by passing env vars
```sh
kubectl run <pod-name> -n <namespace> \
  --image=<acr-name>.azurecr.io/dev/app:latest --env="PREFIX_UPPER_CASE_PARAM=xyz"
```

## use another entrypoint and let the pod run so can get into the container
https://stackoverflow.com/questions/59248318/kubectl-run-command-vs-arguments
```sh
kubectl run <pod-name> -n <namespace> --image=<image-path> \
  --restart=Never -o yaml --dry-run -- /bin/sh -c "echo hello;sleep 3600"
```

## sleep pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu
  labels:
    app: ubuntu
spec:
  containers:
  - image: ubuntu
    command:
      - "sleep"
      - "604800"
    imagePullPolicy: IfNotPresent
    name: ubuntu
  restartPolicy: Always
```

## temporally create a pod and delete it when it exits
option 1
```sh
kubectl run -it --rm <pod-name> --namespace=<namespace> --image=alpine -- bash
```

option 2: using a yaml file
```sh
kubectl apply -f <debug-pod>.yaml
kubectl exec -it <pod-name> --namespace=<namespace> -- bash
kubectl delete pod <pod-name> --namespace=<namespace>
```

yaml file
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: debug-pod
  namespace: default
spec:
  containers:
  - name: debug-container
    image: alpine
    command: ["/bin/bash", "-c", "tail -f /dev/null"]
    volumeMounts:
    - name: my-volume
      mountPath: /path/in/container
  volumes:
  - name: my-volume
    hostPath:
      path: /path/on/host
```
running the `tail -f /dev/null` command to keep the container running.

## Lifecycle
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#example-states

- Pending
- Running
- Succeeded/Failed

## Status
- `Completed`: when the running process/app/container returns exit code 0.
- `Error`: when return a non-zero exit code the status usually set to Error.

## Pod and container failures
### Container
A **container** in a Pod may fail for a number of reasons, such as
- the process in it exited with a non-zero exit code, or
- the container was killed for exceeding a memory limit, etc.
If this happens, and the .spec.template.spec.restartPolicy = "OnFailure", then the Pod stays on the node, but the container is re-run.

Therefore, your program needs to handle the case when it is restarted locally, or else specify .spec.template.spec.restartPolicy = "Never".

### Pod
An entire **Pod** can also fail, for a number of reasons, such as
- when the pod is kicked off the node (node is upgraded, rebooted, deleted, etc.), or
- if a container of the Pod fails and the .spec.template.spec.restartPolicy = "Never".
When a Pod fails, then the Job controller starts a new Pod.

This means that your application needs to handle the case when it is restarted in a new pod. In particular, it needs to handle temporary files, locks, incomplete output and the like caused by previous runs.

Note that even if you specify .spec.parallelism = 1 and .spec.completions = 1 and .spec.template.spec.restartPolicy = "Never", the same program may sometimes be started twice.

If you do specify .spec.parallelism and .spec.completions both greater than 1, then there may be multiple pods running at once. Therefore, your pods must also be tolerant of concurrency.
