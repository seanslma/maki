# Assign Pods to Nodes

https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/

## `nodeSelector` field matching against node `labels`
Pod `nodeSelector`
```yaml
nodeSelector:
    disktype: ssd
```
Node `label`
```yaml
node_labels {
    "disktype" = "ssd"
}
```

## `Affinity` and `anti-affinity`
- nodeName field
- Pod topology spread constraints
- Node labels
