# ReplicaSet

**Note**: ReplicaSet will not be updated automatically for the mounted objects such as key vault secrets - Need to delete the ReplicaSet to force creating a new pod. 

https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/#:~:text=A%20ReplicaSet's%20purpose%20is%20to,specified%20number%20of%20identical%20Pods

A `ReplicaSet`'s purpose is to maintain a stable set of replica Pods running at any given time. 
As such, it is often used to guarantee the availability of a specified number of identical Pods.

A `Deployment` is a higher-level concept that manages ReplicaSets and provides declarative updates to Pods along with a lot of other useful features.

```
kubectl -n <namespace> get rs #get current replicasets
kubectl -n <namespace> describe rs/<replicaset-name> #check the status
```
