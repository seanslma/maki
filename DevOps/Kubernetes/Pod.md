# Pod

## Lifecycle
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#example-states

- Pending
- Running
- Succeeded/Failed

## Status
- `Completed`: when the running process/app/container returns exit code 0.
- `Error`: when return a non-zero exit code the status usually set to Error.

## Pod and container failures
A container in a Pod may fail for a number of reasons, such as 
- the process in it exited with a non-zero exit code, or 
- the container was killed for exceeding a memory limit, etc. 
If this happens, and the .spec.template.spec.restartPolicy = "OnFailure", then the Pod stays on the node, but the container is re-run. 

Therefore, your program needs to handle the case when it is restarted locally, or else specify .spec.template.spec.restartPolicy = "Never".
