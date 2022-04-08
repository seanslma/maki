# Key Vault

## basic
```
az config set defaults.location=westus2
az group create --name <your-resource-group>
az keyvault create --resource-group <your-resource-group> \
  --name <your-key-vault>
  
az keyvault secret set \
  --vault-name <unique-keyvault-namee>  
  --name "<keyvault-secret-name>" \
  --value "mysecretpassword" \
```

## add multi-line secret
```
az keyvault secret set --vault-name "<unique-keyvault-name>" --name "<keyvault-secret-name>" --file "secretfile.txt"
```
