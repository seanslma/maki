# https

HTTPS makes use of Transport Layer Security (TLS) certificates to encrypt traffic between an end user and a server, or between two servers. TLS is the successor to the Secure Sockets Layer (SSL). The terms TLS and SSL are often used interchangeably.

## Azure App Gateway as ingress
An ingress in Kubernetes is an object that is used to route HTTP and HTTPS traffic from outside the cluster to services in a cluster.

Azure application gateway can be used as an ingress for Kubernetes by using the Application Gateway Ingress Controller 
(AGIC). Configuring AGIC can either uses Helm or aks add-on.

### create app gateway
```
#create resource group
az group create -n agic -l westus2
#create public IP with a DNS name
az network public-ip create -n agic-pip \
   -g agic --allocation-method Static --sku Standard \
   --dns-name "<your unique DNS name>"
#create virtual network   
az network vnet create -n agic-vnet -g agic \
  --address-prefix 192.168.0.0/24 --subnet-name agic-subnet \
  --subnet-prefix 192.168.0.0/24
#create app gateway
az network application-gateway create -n agic -l westus2 \
  -g agic --sku Standard_v2 --public-ip-address agic-pip \
  --vnet-name agic-vnet --subnet agic-subnet
```

### setup up AGIC
```
#enable integration between cluster and app gateway
appgwId=$(az network application-gateway \
  show -n agic -g agic -o tsv --query "id") 
az aks enable-addons -n handsonaks \
  -g rg-handsonaks -a ingress-appgw \
  --appgw-id $appgwId
#peer app gateway network with AKS network
nodeResourceGroup=$(az aks show -n handsonaks \
  -g rg-handsonaks -o tsv --query "nodeResourceGroup")
aksVnetName=$(az network vnet list \
  -g $nodeResourceGroup -o tsv --query "[0].name")

aksVnetId=$(az network vnet show -n $aksVnetName \
  -g $nodeResourceGroup -o tsv --query "id")
az network vnet peering create \
  -n AppGWtoAKSVnetPeering -g agic \
  --vnet-name agic-vnet --remote-vnet $aksVnetId \
  --allow-vnet-access
  
appGWVnetId=$(az network vnet show -n agic-vnet \
  -g agic -o tsv --query "id")
az network vnet peering create \
  -n AKStoAppGWVnetPeering -g $nodeResourceGroup \
  --vnet-name $aksVnetName --remote-vnet $appGWVnetId --allow-vnet-
access
```

### add ingress rule
```
#launch app
kubectl create -f guestbook-all-in-one.yaml
#create ingest
kubectl apply -f simple-frontend-ingress.yaml
#verify no external ip
kubectl get service
```

### add TLS to ingress
```
#install cert-manager
kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.2.0/cert-manager.yaml
#install certificate issuer
ubectl create -f certificate-issuer.yaml
#create TLS certificate and secury ingress
kubectl apply -f ingress-with-tls.yaml
kubectl get certificate
kubectl get certificaterequest
kubectl describe certificaterequest

#clean up
kubectl delete -f https://github.com/jetstack/cert-manager/releases/download/v1.1.0/cert-manager.yaml
az aks disable-addons -n handsonaks \
  -g rg-handsonaks -a ingress-appgw 
```
