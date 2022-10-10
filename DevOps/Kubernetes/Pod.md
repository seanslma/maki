# Pod

## General
```
kubectl get pods                #check status
kubectl describe pod <pod-name> #check events
kubectl logs <pod-name>         #check logs
kubectl exec -it <pod-name> -c <container-name> -- bash #connect to pod
```

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
