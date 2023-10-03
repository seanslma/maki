# Kube Autoscaler

https://www.replex.io/blog/kubernetes-in-production-best-practices-for-cluster-autoscaler-hpa-and-vpa


## cluster-autoscaler status
Basic info - not really useful
```sh
>> kubectl get configmap -n kube-system cluster-autoscaler-status
NAME                        DATA   AGE
cluster-autoscaler-status   1      37h

kubectl get cm cluster-autoscaler-status -n kube-system
kubectl get cm cluster-autoscaler-user-values -n kube-system
```
All info
```sh
kubectl describe configmap --namespace kube-system cluster-autoscaler-status
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

Scaling formula:
https://github.com/kubernetes/kubernetes/issues/78761
```
desiredMetricValue = ceil[(currentReplicas * currentMetricValue) / desiredReplicas]
```

Kubernetes uses the horizontal pod autoscaler (HPA) to monitor the resource demand and automatically scale the number of replicas.

```sh
kubectl autoscale deployment <hpa-name> \
  --cpu-percent=50 --min=3 --max=10            #create hpa
kubectl create -f ./hpa.yaml                   #create hpa from yaml
kubectl get hpa                                #check hpa
kubectl get hpa <hpa-name> --watch             #watch hpa
kubectl get deployment <deployment-name>       #deployment
kubectl describe hpa <hpa-name> -n <namespace> #hpa conditions
kubectl delete hpa <hpa-name> -n <namespace>   #delete hpa
kubectl scale deployment <deployment-name> \
  --replicas=<replica-count> -n <namespace>    #scale replicasets
```

HPA yaml file:
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: <hpa-name>
  namespace: <deployment-namespace>
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: <deployment-name>
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 80
    - type: Resource
      resource:
        name: cpu
        target:
          type: AverageValue
          averageValue: 1000m
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Pods
          value: 4
          periodSeconds: 60
        - type: Percent
          value: 10
          periodSeconds: 60
      selectPolicy: Max
```

## vertical pod autoscaler (VPA)
https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler

VPA will set the requests automatically based on usage and thus allow proper scheduling onto nodes so that appropriate resource amount is available for each pod. It will also maintain ratios between limits and requests that were specified in initial containers configuration.

## Scale rules
https://docs.giantswarm.io/advanced/cluster-autoscaler/
