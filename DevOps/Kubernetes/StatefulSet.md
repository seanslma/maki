# StatefulSet

https://medium.com/avmconsulting-blog/deploying-statefulsets-in-kubernetes-k8s-5924e701d327
StatefulSet Components
- A Headless Service
- A StatefulSet
- A PersistentVolume

## Scaling StatefulSet
https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/
```
kubectl scale sts web --replicas=5                 #scale up
kubectl patch sts web -p '{"spec":{"replicas":3}}' #scale down
```

https://kubernetes.io/docs/tasks/run-application/scale-stateful-set/
- You cannot scale down a StatefulSet when any of the stateful Pods it manages is `unhealthy`. 
- Scaling down only takes place after those stateful Pods become running and ready.

## rollout restart StatefulSet
Stateful set are removed following their ordinal index with the highest ordinal index first.

`kubectl rollout restart` is applicable for deployments, daemonsets and statefulsets.
- `partitions`  if in StatefulSet we have `updateStrategy.rollingUpdate.partition: 1` it will restart all pods with index 1 or higher.
```
kubectl rollout restart statefulset demo -n dev
kubectl rollout status statefulset demo -n dev     
```

## Force delete StatefulSet pod
https://kubernetes.io/docs/tasks/run-application/force-delete-stateful-set-pod/
graceful pod deletion
```
kubectl delete pods <pod>
```

A Pod is not deleted automatically when a node is unreachable. 
The Pods running on an unreachable Node enter the `Terminating` or `Unknown` state after a timeout. 
Pods may also enter these states when the user attempts graceful deletion of a Pod on an unreachable Node. 

The only ways in which a Pod in such a state can be removed from the apiserver are as follows:
- The Node object is deleted (either by you, or by the Node Controller).
- The kubelet on the unresponsive Node starts responding, kills the Pod and removes the entry from the apiserver.
- Force deletion of the Pod by the user.

Force delete StatefulSet pod
```
kubectl delete pods <pod> --grace-period=0 --force
#if the pod is stuck on Unknown state after delete, remove the pod from the cluster using
kubectl patch pod <pod> -p '{"metadata":{"finalizers":null}}'
```
