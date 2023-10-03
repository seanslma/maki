# Sort By

```sh
kubectl top pod <pod-name> --sort-by=cpu                 #cpu/memory
kubectl get services --sort-by=.metadata.name            #name
kubectl get events --sort-by=.metadata.creationTimestamp #timestamp
kubectl get pv --sort-by=.spec.capacity.storage          #capacity
kubectl get pods --sort-by='.status.containerStatuses[0].restartCount'
```
