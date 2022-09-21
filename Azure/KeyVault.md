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
