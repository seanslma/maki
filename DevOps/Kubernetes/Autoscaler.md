# Kube Autoscaler

https://www.replex.io/blog/kubernetes-in-production-best-practices-for-cluster-autoscaler-hpa-and-vpa


## cluster-autoscaler status
```
>> kubectl get configmap -n kube-system cluster-autoscaler-status
NAME                        DATA   AGE
cluster-autoscaler-status   1      37h

kubectl get cm cluster-autoscaler-status -n kube-system
kubectl get cm cluster-autoscaler-user-values -n kube-system
```

## cluster austoscaler (CA)
CA increases or decreases the size of a Kubernetes cluster (by adding or removing nodes), based on the presence of pending pods and node utilization metrics.
- Adds nodes to a cluster whenever it detects pending pods that could not be scheduled due to resource shortages
- Removes nodes from a cluster, whenever the utilization of a node falls below a certain threshold defined by the cluster administrator

Best practice:
- Ensure cluster nodes have the same capacity
- Ensure every pod has resource requests defined
  - Utilization is calculated as the sum of **requested resources** divided by the **capacity**.
  - https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-are-the-parameters-to-ca

## horizontal pod autoscaler (HPA)
https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale

Kubernetes uses the horizontal pod autoscaler (HPA) to monitor the resource demand and automatically scale the number of replicas. 


## vertical pod autoscaler (VPA)
https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler

VPA will set the requests automatically based on usage and thus allow proper scheduling onto nodes so that appropriate resource amount is available for each pod. It will also maintain ratios between limits and requests that were specified in initial containers configuration.

## Scale rules
https://docs.giantswarm.io/advanced/cluster-autoscaler/
