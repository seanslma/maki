# Key Vault

## when updated will take effect
When the secret/key is updated in external secrets store after the initial pod deployment, the updated secret will be periodically updated in the pod mount and the Kubernetes Secret.

Depending on how the application consumes the secret data:
- Mount Kubernetes secret as a volume: Use auto rotation feature + Sync K8s secrets feature in Secrets Store CSI Driver, application will need to watch for changes from the mounted Kubernetes Secret volume. When the Kubernetes Secret is updated by the CSI Driver, the corresponding volume contents are automatically updated.
- Application reads the data from container’s filesystem: Use rotation feature in Secrets Store CSI Driver, application will need to watch for the file change from the volume mounted by the CSI driver.
- Using Kubernetes secret for environment variable: The pod needs to be restarted to get the latest secret as environment variable. Use something like https://github.com/stakater/Reloader to watch for changes on the synced Kubernetes secret and do rolling upgrades on pods.

Additional configuration:
https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/tutorial-akv-secrets-provider#additional-configuration-options

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
