# Builing scalable apps

Scale app using **Horizontal Pod Autoscaler (HPA)**. Scale the cluster using **cluster autoscaler**.

## scale app
Scale dimensions include the number of pods a deployment has, and the number of nodes in the cluster.

```
#edit service
kubectl edit service frontend
#watch service
kubectl get service -w
```
