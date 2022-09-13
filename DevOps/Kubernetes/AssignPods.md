# Assign Pods to Nodes

https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/

`nodeSelector` field matching against node `labels`
Pod `nodeSelector`
```
nodeSelector:
    disktype: ssd
```
Node `label`
```
node_config {
    labels {
        "disktype" = "ssd"
    }
}
```

- `Affinity` and `anti-affinity`
- nodeName field
- Pod topology spread constraints
- Node labels
