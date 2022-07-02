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

## scale pods

### mannual scale pods
```
kubectl get pods
#show Ip and running status
kubectl get pods -o wide
#scale deployment: add additional pods to the deployment
kubectl scale deployment/frontend --replicas=6
```

### auto scale pods using hpa
```
#hap.ymal
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: frontend-scaler
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: frontend
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
  
#create hpa autoscaler
kubectl create -f hpa.yaml
#check hpa
kubectl get hpa
#watching pods
kubectl get pods -w

#install and run hey (tiny program sending loads to web app) from cloud shell
export GOPATH=~/go
export PATH=$GOPATH/bin:$PATH
go get -u github.com/rakyll/hey
hey -z 20m http://<external-ip> #create up to 20 million connections

#closer look of hpa
kubectl describe hpa
#check hpa
kubectl get hpa -w

#clean up resources
kubectl delete -f hpa.yaml
kubectl delete -f guestbook-all-in-one.yaml
```

## scale cluster
```
#launch guestbook app 
kubectl create -f guestbook-all-in-one.yaml
#mannually scale out redis-replica
kubectl scale deployment redis-replica --replicas 5
#check pods
kubectl get pods

#azure cli configure cluster autoscaler
az aks nodepool update --enable-cluster-autoscaler \
  -g rg01 --cluster-name myaks \
  --name agentpool --min-count 1 --max-count 2
  
#watch nodes
kubectl get nodes -w  
#watch pods
kubectl get pods

#clean up resources
kubectl delete -f guestbook-all-in-one.yaml
#disable cluster autoscaler
az aks nodepool update --disable-cluster-autoscaler \
  -g rg01 --cluster-name myaks --name agentpool
#scale cluster to 2 nodes
az aks nodepool scale --node-count 2 -g rg01 \
  --cluster-name handsonaks --name agentpool
```
