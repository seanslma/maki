# Key Vault

## basic
```
az config set defaults.location=westus2
az group create --name <your-resource-group>
az keyvault create \
  --resource-group <your-resource-group> \
  --name <your-key-vault>
  
az keyvault secret set \
  --vault-name <unique-keyvault-namee>  
  --name "<keyvault-secret-name>" \
  --value "mysecretpassword" \
```

## Save secret to file
```
az keyvault secret download \
  --vault-name <keyvault-name> \
  --name <secret-name> \
  --file <filepath>
```    

## Add multi-line secret
```
az keyvault secret set \
  --vault-name "<keyvault-name>" \
  --name "<secret-name>" \
  --file "secretfile.txt"
az keyvault secret set-attributes \
  --vault-name "<keyvault-name>" \
  --name "<secret-name>" \
  --content-type 'application/json'
```

## use secret in aks
https://shailender-choudhary.medium.com/access-secrets-from-azure-key-vault-in-azure-kubernetes-service-e8efffe49427
Secret Provider Class (secret.yml)
```
#using system-assigned identity to access key vault
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: my-secret-csi
  namespace: dev
spec:
  provider: azure
  parameters:
    usePodIdentity: "false"
    useVMManagedIdentity: "true"      #Set to true for using managed identity
    userAssignedIdentityID: ""        #If empty, then defaults to use clientId of the system assigned identity on the VM
    keyvaultName: my-kv-name
    cloudName: "AzurePublicCloud"     #[OPTIONAL for Azure] if not provided, the Azure environment defaults to AzurePublicCloud
    objects:  |
      array:
        - |
          objectName: database--mysql
          objectType: secret          # object types: secret, key, or cert
          objectAlias: "mysql.json"   # [OPTIONAL] name of the secret
          objectVersion: ""           # [OPTIONAL] object versions, default to latest if empty
    tenantId: XXXXXXXXXXXX            # The tenant ID of the key vault
```

job.yml
```
ok
```
