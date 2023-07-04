# Azure Container Registry
https://learn.microsoft.com/en-us/cli/azure/acr?view=azure-cli-latest

## Cache for Azure Container Registry
https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Flearn.microsoft.com%2Fazure%2Fcontainer-registry%2Ftutorial-registry-cache%23cache-for-acr-preview&data=05%7C01%7Cshuiliang.ma%40stanwell.com%7C0303cd71fff8446615ec08db7c586db8%7C556f4662c7de43129a81dd4e68521c32%7C0%7C0%7C638240491464210202%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=B9DGdrKiB%2FLLfOxwBaiXxx6iSY0rm6jK9JWVrpnFYcg%3D&reserved=0

## List repos in ACR
```
az acr repository list --name <acr-name> --output table #list repos
az acr repository show-tags --name <acr-name> \
    --repository sample/hello-world --output table      #list repo tags
```

## Run an image from ACR
https://learn.microsoft.com/en-us/learn/modules/publish-container-image-to-azure-container-registry/6-build-run-image-azure-container-registry
```
az acr run \
--registry <acr-name> \
--cmd '<acr-name>.azurecr.io/sample/hello-world:v1' /dev/null
```
`cmd` docs:

https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-reference-yaml#cmd

Create a container instantance:

https://learn.microsoft.com/en-us/training/modules/create-run-container-images-azure-container-instances/3-run-azure-container-instances-cloud-shell
```
az container create --resource-group az204-aci-rg \
    --name mycontainer \
    --image mcr.microsoft.com/azuredocs/aci-helloworld \
    --ports 80 \
    --dns-name-label $DNS_NAME_LABEL --location <myLocation> \
```

## Integrate an existing ACR with existing AKS clusters
https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration?tabs=azure-cli
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
