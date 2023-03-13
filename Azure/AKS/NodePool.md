# Node Pool

https://learn.microsoft.com/en-us/azure/aks/use-multiple-node-pools

## abort operation on node pool
```
az aks nodepool operation-abort --name <node-pool> \
  --cluster-name <cluster-name> --resource-group <resource-group>
```

## abort operation on managed cluster
```
az aks operation-abort --name <cluster-name> --resource-group <resource-group>
```

## spot node pool
To schedule a pod to run on a Spot node, the pod should define
- a `toleration` that corresponds to the `kubernetes.azure.com/scalesetpriority=spot:NoSchedule` taint and
- a `node affinity` that corresponds to the `kubernetes.azure.com/scalesetpriority=spot` label
```
spec:
  containers:
  - name: spot-example
  tolerations:
  - key: "kubernetes.azure.com/scalesetpriority"
    operator: "Equal"
    value: "spot"
    effect: "NoSchedule"
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: "kubernetes.azure.com/scalesetpriority"
            operator: In
            values:
            - "spot"
```
