# upgrade app

## changing yaml file
```
code guestbook-all-in-one.yaml              #edit yaml
kubectl apply -f guestbook-all-in-one.yaml  #apply changes
kubectl get service                         #get service public IP
code guestbook-all-in-one.yaml              #change version
kubectl apply -f guestbook-all-in-one.yaml \
  && kubectl get pods -w                    #apply and check
kubectl get events | grep ReplicaSet        #show rolling update strategy
kubectl get replicaset                      #verify
kubectl rollout history deployment frontend #show rollout history
kubectl rollout undo deployment frontend    #rollback deployment
kubectl get replicaset                      #verify
kubectl delete -f guestbook-all-in-one.yaml #clean up
```

## using kubectl edit
This will not work in an automated environment.
```
git reset --hard                            #undo changes
kubectl create -f guestbook-all-in-one.yaml #deploy app
kubectl edit service frontend               #edit service
kubectl get svc -w                          #watch service
```

## using kubectl patch
This can make automated changes, when don't have access to the original YAML file, e.g. in a script or in a **continuous integration/
continuous deployment** system.

### yaml patch file
```
#create ymal file
code frontend-image-patch.yaml
#yaml file
spec:
  template:
    spec:
      containers:
      - name: php-redis
        image: gcr.io/google-samples/gb-frontend:v3
#apply the patch
kubectl patch deployment frontend \
  --patch "$(cat frontend-image-patch.yaml)"
#verify changes
kubectl describe deployment frontend
```

### json inline
```
kubectl patch deployment frontend \
--patch='
{
  "spec": {
    "template": {
      "spec": {
        "containers": [{
          "name": "php-redis",
          "image": "gcr.io/google-samples/gb-frontend:v4"
        }]
      }
    }
  }
}
'
#remove app from cluster
kubectl delete -f guestbook-all-in-one.yaml
```

## using Helm
```
#force an update of the image of the MariaDB container
helm install wp bitnami/wordpress
#check current image version
kubectl describe statefulset wp-mariadb | grep Image
#get MariaDB passwords from secrets in aks
kubectl get secret wp-mariadb -o yaml
#get decoded password
echo "<password>" | base64 -d
#get WordPress password
kubectl get secret wp-wordpress -o yaml
echo "<WordPress password>" | base64 -d

#update image tag with Helm and watch pods change
helm upgrade wp bitnami/wordpress \
  --set mariadb.image.tag=10.5.8-debian-10-r44\
  --set mariadb.auth.password="<decoded password>" \
  --set mariadb.auth.rootPassword="<decoded password>" \
  --set wordpressPassword="<decoded password>" \
  && kubectl get pods -w

#show new image version
kubectl describe pod wp-mariadb-0 | grep Image

#clean up
helm delete wp
kubectl delete pvc --all
kubectl delete pv --all
```
