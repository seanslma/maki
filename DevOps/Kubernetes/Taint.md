# Taints and Tolerations

https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/

`Taints`
- Taints allow a node to repel a set of pods.

`Tolerations`
- Tolerations are applied to pods. 
- Tolerations allow the scheduler to schedule pods with matching taints. 
- Tolerations allow scheduling but don't guarantee scheduling.
