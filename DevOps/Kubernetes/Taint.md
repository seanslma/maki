# Taints and Tolerations

https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/

`Taints`
- A node property
- Allow a node to repel a set of pods

`Tolerations`
- A pod property, applied to pods 
- Allow scheduling pods on node with matching taints 
- Allow scheduling but don't guarantee scheduling

## Node affinity
Taints and tolerations can be combined with node affinity to create dedicated nodes. 
- Node affinity sets the node to schedule pods using labels by specifying the nodeAffinity in PodSpec
- Taints on the node ensure that all pods without a matching toleration get repelled

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
```
