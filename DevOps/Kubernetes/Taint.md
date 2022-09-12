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

## Pod anti-affinity

## Get tainted nodes
```
kubectl get node -o custom-columns=NAME:.metadata.name,TAINT:.spec.taints[*].effect
kubectl get node -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints #include keys
```
