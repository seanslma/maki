# Azure Container Registry
https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration?tabs=azure-cli

## Integrate an existing ACR with existing AKS clusters
```
az aks update -n <cluster-name> -g <resource-group> --attach-acr <acr-name/resource-id>
```

## Remove the integration between an ACR and an AKS cluster
```
az aks update -n <cluster-name> -g <resource-group> --detach-acr <acr-name/resource-id>
```

## Import an image from docker hub into your ACR
```
az acr import  -n <acr-name> --source docker.io/library/nginx:latest --image nginx:v1
```

## Deploy docker image from ACR to AKS
```
kubectl apply -f <path-to-deployment.yaml>
kubectl delete deploy <deployment-name> -n <namespace>
```

Deployment.yaml
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  namespace: dev
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: "<acr-name>.azurecr.io/<namespace>/myapp:latest"
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: 4Gi
            cpu: "1"
          limits:
            memory: 32Gi
            cpu: "3" 
          volumeMounts:
          - name: cfg
            mountPath: "/home/user/.config/cfg1"
            readOnly: true 
          env:
            - name: RESULT_PATH
              value: "test"   
      volumes:
      - name: db
        secret:
          secretName: mysql
      - name: cfg
        csi:
          driver: secrets-store.csi.k8s.io
          readOnly: true
          volumeAttributes:
            secretProviderClass: "myapp-cfg"              
```
