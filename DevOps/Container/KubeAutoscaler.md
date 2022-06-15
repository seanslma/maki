# Kube Autoscaler

https://www.replex.io/blog/kubernetes-in-production-best-practices-for-cluster-autoscaler-hpa-and-vpa

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
https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/

## vertical pod autoscaler (VPA)
