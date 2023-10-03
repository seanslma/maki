# PDB (Pod Disruption Budget)
https://kubernetes.io/docs/tasks/run-application/configure-pdb/

A PodDisruptionBudget has three fields:
- A label selector `.spec.selector` to specify the set of pods to which it applies
- `.spec.minAvailable` which is a description of the number of pods from that set that must still be available after the eviction, even in the absence of the evicted pod. absolute number or a percentage.
- `.spec.maxUnavailable` which is a description of the number of pods from that set that can be unavailable after the eviction. absolute number or a percentage.

## get pdb apiversion in kubernetes
```sh
kubectl api-resources | grep pdb
```

## `minAvailable` or `maxUnavailable`
- `minAvailable`:  the number of Pods that must be available during a disruption
- `maxUnavailable`:  the number of Pods that may be disrupted
- only one of `minAvailable` and `maxUnavailable` in a single PodDisruptionBudget can be specified
- an integer represents the number of Pods. If `minAvailable = 10`, then 10 Pods must always be available, even during a disruption.
- a percentage as a string (e.g. "50%") represents a percentage of total Pods. If `minAvailable = 50%"`, then at least 50% of the Pods (rounded) remain available during a disruption.

## `ALLOWED DISRUPTIONS`
- `ALLOWED DISRUPTIONS = 0` when there are not any pods matching `app: my-app` in the namespace
  `ALLOWED DISRUPTIONS = 1` disruption controller has seen the pods, counted the matching pods, and updated the status of the PDB
```sh
kubectl -n <namespace> get pdb <pdb-name>
kubectl -n <namespace> get pdb <pdb-name> -o yaml
```

## Cannot evict pod as it would violate the pod's disruption budget
```
NAMESPACE  NAME              MIN AVAILABLE  MAX UNAVAILABLE  ALLOWED DISRUPTIONS  AGE
jhub       user-placeholder  0              N/A              0                    10d
jhub       user-scheduler    N/A            1                1                    10d
```
PDBs are a feature for HA deployments, and HA deployments imply 2+ replicas. To avoid the error and failure of node reboot, the replicaSet must be larger than 1.
