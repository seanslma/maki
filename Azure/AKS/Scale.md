# Builing scalable apps

Scale app using **Horizontal Pod Autoscaler (HPA)**. Scale the cluster using **cluster autoscaler**.

## scale app
Scale dimensions include the number of pods a deployment has, and the number of nodes in the cluster.

```
kubectl edit service frontend  #edit service
kubectl get service -w         #watch service
```

## scale pods

### mannual scale pods
```
kubectl get pods
kubectl get pods -o wide                       #show Ip and running status
kubectl scale deployment/frontend --replicas=6 #add additional pods to the deployment
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

kubectl create -f hpa.yaml  #create hpa
kubectl get hpa             #check hpa
kubectl get pods -w         #watch pods

#install and run hey (tiny program sending loads to web app) from cloud shell
export GOPATH=~/go
export PATH=$GOPATH/bin:$PATH
go get -u github.com/rakyll/hey
hey -z 20m http://<external-ip> #create up to 20 million connections

kubectl describe hpa  #closer look of hpa
kubectl get hpa -w    #check hpa

#clean up resources
kubectl delete -f hpa.yaml
kubectl delete -f guestbook-all-in-one.yaml
```

## scale cluster
```
kubectl create -f guestbook-all-in-one.yaml          #launch guestbook app
kubectl scale deployment redis-replica --replicas 5  #mannually scale out redis-replica
kubectl get pods                                     #check pods

#azure cli configure cluster autoscaler
az aks nodepool update --enable-cluster-autoscaler \
  -g rg01 --cluster-name myaks \
  --name agentpool --min-count 1 --max-count 2

kubectl get nodes -w  #watch nodes
kubectl get pods      #watch pods

#clean up resources
kubectl delete -f guestbook-all-in-one.yaml
#disable cluster autoscaler
az aks nodepool update --disable-cluster-autoscaler \
  -g rg01 --cluster-name myaks --name agentpool
#scale cluster to 2 nodes
az aks nodepool scale --node-count 2 -g rg01 \
  --cluster-name handsonaks --name agentpool
```
