# Pod

## General
```
kubectl get pods                #check status
kubectl get pods -o wide        #show more info such node
kubectl describe pod <pod-name> #check events
kubectl get event --field-selector involvedObject.name=<pod-name>
kubectl logs <pod-name>         #check logs
kubectl exec -it <pod-name> -c <container-name> -- bash #connect to pod

```

## Kubectl run command
https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#notes
When you override the default Entrypoint and Cmd for a Container, these rules apply:
- do not supply `command` or `args`, the defaults defined in the Docker image are used.
- supply a `command` but no `args`, only the supplied command is used. The default EntryPoint and the default Cmd defined in the Docker image are ignored.
- supply only `args`, the default Entrypoint defined in the Docker image is run with the args that you supplied.
- supply a `command` and `args`, the default Entrypoint and the default Cmd defined in the Docker image are ignored. Your command is run with your args.

## create a pod by passing env vars
```
kubectl run <pod-name> -n <namespace> --image=<acr-name>.azurecr.io/retail/app:latest --env="PREFIX_UPPER_CASE_PARAM=xyz"
```

## use another entrypoint and let the pod run so can get into the container
https://stackoverflow.com/questions/59248318/kubectl-run-command-vs-arguments
```
kubectl run <pod-name> -n <namespace> --image=<image-path> --restart=Never -o yaml --dry-run -- /bin/sh -c "echo hello;sleep 3600"
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
