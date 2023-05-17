# PDB (Pod Disruption Budget)
https://kubernetes.io/docs/tasks/run-application/configure-pdb/

## `minAvailable` or `maxUnavailable`
- `minAvailable`:  the number of Pods that must be available during a disruption
- `maxUnavailable`:  the number of Pods that may be disrupted
- only one of `minAvailable` and `maxUnavailable` in a single PodDisruptionBudget can be specified
- an integer represents the number of Pods. If `minAvailable = 10`, then 10 Pods must always be available, even during a disruption.
- a percentage as a string (e.g. "50%") represents a percentage of total Pods. If `minAvailable = 50%"`, then at least 50% of the Pods (rounded) remain available during a disruption.

## `ALLOWED DISRUPTIONS`
- `ALLOWED DISRUPTIONS = 1` when there are no pods matching `app: my-app` in the namespace
- `ALLOWED DISRUPTIONS = 0` when there are not any pods matching `app: my-app` in the namespace
```
kubectl -n <namespace> get pdb <pdb-name>
kubectl -n <namespace> get pdb <pdb-name> -o yaml
```
