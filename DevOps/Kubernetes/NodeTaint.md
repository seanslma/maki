# Taints and Tolerations

https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/

https://blog.kubecost.com/blog/kubernetes-taints/

## Taints
- A node property
- Allow a node to repel a set of pods

## Tolerations
- A pod property, applied to pods 
- Allow scheduling pods on node with matching taints, but don't guarantee scheduling
- `Equal` operator requires the taint value and will not match if the value is different
- `Exists` operator will match any value as it only considers if the taint is defined regardless of the value

## Node affinity
Taints and tolerations can be combined with node affinity to create dedicated nodes. 
- Node affinity sets the node to schedule pods using labels by specifying the nodeAffinity in PodSpec
- Taints on the node ensure that all pods without a matching toleration get repelled

## Node Selector
Node selectors are a simpler way to constrain pod scheduling to nodes with specific labels. 
- They use the nodeSelector field in a pod's spec to specify node label requirements.
- A pod will only be scheduled on nodes that satisfy all of the specified node selector requirements.

## Pod anti-affinity
- Can prevent schedulers from locating new pods on nodes where the label selector on the new pod matches the label on an existing pod
- Relies on label key-value pairs on other pods to determine its scheduling behavior

## Add taint to node
```
kubectl taint node <node-name> <taint-key>=<taint-value>:<taint-effect>
```

## Get tainted nodes
```
kubectl get node -o custom-columns=NAME:.metadata.name,TAINT:.spec.taints[*].effect
kubectl get node -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints #include keys
kubectl get node -o=jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.taints[*].key}{"="}{.spec.taints[*].value}{":"}{.spec.taints[*].effect}{"\n"}{end}'  
```

Node taints example:
```
node_taints = [
 "key=value:effect"
]
```

Pod tolerations example:
```
tolerations:
- key: key
  operator: Equal
  value: value
  effect: NoSchedule
- key: key2
  operator: Exists
  effect: NoSchedule 
 ```
