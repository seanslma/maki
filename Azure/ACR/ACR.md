# Azure Container Registry
- https://azure.microsoft.com/en-us/services/container-registry/
- https://learn.microsoft.com/en-us/cli/azure/acr?view=azure-cli-latest

## login
```
az acr login -n <container-registry-name>
```

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

When using Azure Container Registry (ACR) with Azure Kubernetes Service (AKS), you need to establish an authentication mechanism. 
You can configure the required permissions between ACR and AKS using the `Azure CLI`, `Azure PowerShell`, or `Azure portal`. 
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

## check arc health
```sh
az acr check-health --name <myregistry> --ignore-errors --yes
```

## Cache for Azure Container Registry
