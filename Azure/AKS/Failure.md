# AKS Failure
  
## node failure
```
kubectl get nodes
kubectl create -f guestbook-all-in-one.yaml
kubectl get service -w
kubectl get pods -o wide
#new cloud shell: hit the guestbook front end every 5 seconds and get the HTML
while true; do 
  curl -m 1 http://<EXTERNAl-IP>/; 
  sleep 5;
done

kubectl get pods -o wide -w
```

## out-of-resource failure
```
kubectl scale deployment/redis-replica --replicas=10
kubectl get pods
kubectl describe pod redis-replica-<pod-id>
kubectl delete -f guestbook-all-in-one.yaml
```

## storage mount issue
```
#install WordPress
kubectl get all
kubectl get nodes
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install wp bitnami/wordpress
kubectl get pods -w

#get PersistentVolumeClaims 
kubectl get pvc
#show actual PVs created
kubectl get pv
#get more pv details
kubectl describe pv <pv name>
#get IP address
kubectl get service
#get usr and pwd
helm status wp
echo Username: user
echo Password: $(kubectl get secret --namespace default wp-wordpress 
-o jsonpath="{.data.wordpress-password}" | base64 -d)
#watch pods
kubectl get pods -w
#kill two pods having PVC mounted
kubectl delete pod --all
```

## node failure with pvc
```
#get the node hosting app
kubectl get pods -o wide
kubectl get pods -o wide -w
kubectl describe pods/wp-wordpress-<pod-id>
#forcefully remove terminating pod from cluster
kubectl get pods
kubectl delete pod wordpress-wp-<pod-id> --force
#check
kubectl get pods -w
kubectl describe pod wp-wordpress-<pod-id>
#clean up
helm delete wp
kubectl delete pvc --all
kubectl delete pv --all
```
