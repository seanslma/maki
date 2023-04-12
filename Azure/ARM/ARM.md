# ARM

Azure resource management template.

## storage account
```json
{
   "type": "Microsoft.Storage/storageAccounts",
   "name": "[variables('storageAccountName')]",
   "apiVersion": "2023-04-01",
   "location": "[parameters('location')]",
   "sku": {
      "name": "Standard_LRS"
   },
   "kind": "Storage",
   "properties": {}
 },
```
