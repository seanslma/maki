# StatefulSet

https://kubernetes.io/docs/tasks/run-application/force-delete-stateful-set-pod/

## delete StatefulSet pod
A Pod is not deleted automatically when a node is unreachable. 
The Pods running on an unreachable Node enter the `Terminating` or `Unknown` state after a timeout. 
Pods may also enter these states when the user attempts graceful deletion of a Pod on an unreachable Node. 

The only ways in which a Pod in such a state can be removed from the apiserver are as follows:
- The Node object is deleted (either by you, or by the Node Controller).
- The kubelet on the unresponsive Node starts responding, kills the Pod and removes the entry from the apiserver.
- Force deletion of the Pod by the user.

## rollout restart StatefulSet
Stateful set are removed following their ordinal index with the highest ordinal index first.

`kubectl rollout restart` is applicable for deployments, daemonsets and statefulsets.
- `partitions`  if in StatefulSet we have `updateStrategy.rollingUpdate.partition: 1` it will restart all pods with index 1 or higher.
```
kubectl rollout restart statefulset demo -n dev
kubectl rollout status statefulset demo -n dev     
```
