# ARM

Azure resource manager template.

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
}
```

## virtual network
```json
{
   "apiVersion": "2023-04-01",
   "type": "Microsoft.Network/virtualNetworks",
   "name": "[variables('virtualNetworkName')]",
   "location": "[parameters('location')]",
   "properties": {
      "addressSpace": {
         "addressPrefixes": [
            "[variables('addressPrefix')]"
         ]
      },
      "subnets": [
         {
            "name": "[variables('subnetName')]",
            "properties": {
               "addressPrefix": "[variables('subnetPrefix')]"
            }
         }
      ]
   }
}
```

## public ip address
```json
{
   "apiVersion": "2023-04-01",
   "type": "Microsoft.Network/publicIPAddresses",
   "name": "[variables('publicIPAddressName')]",
   "location": "[parameters('location')]",
   "properties": {
      "publicIPAllocationMethod": "Dynamic",
      "dnsSettings": {
         "domainNameLabel": "[parameters('dnsLabelPrefix')]"
      }
   }
}
```

## network interface
```json
{
   "apiVersion": "2023-04-01",
   "type": "Microsoft.Network/networkInterfaces",
   "name": "[variables('nicName')]",
   "location": "[parameters('location')]",
   "dependsOn": [
      "[resourceId('Microsoft.Network/publicIPAddresses/', variables('publicIPAddressName'))]",
      "[resourceId('Microsoft.Network/virtualNetworks/', variables('virtualNetworkName'))]"
   ],
   "properties": {
      "ipConfigurations": [
         {
            "name": "ipconfig1",
            "properties": {
               "privateIPAllocationMethod": "Dynamic",
               "publicIPAddress": {
                  "id": "[resourceId('Microsoft.Network/publicIPAddresses',variables('publicIPAddressName'))]"
               },
               "subnet": {
                  "id": "[variables('subnetRef')]"
               }
            }
         }
      ]
   }
}
```

## virtual machine
```json
{
   "apiVersion": "2023-04-01",
   "type": "Microsoft.Compute/virtualMachines",
   "name": "[variables('vmName')]",
   "location": "[resourceGroup().location]",
   "tags": {
      "displayName": "VirtualMachine"
    },
   "dependsOn": [
      "[concat('Microsoft.Storage/storageAccounts/', variables('storageAccountName'))]",
      "[concat('Microsoft.Network/networkInterfaces/', variables('nicName'))]"
   ],
   "properties": {
      "hardwareProfile": { "vmSize": "[variables('vmSize')]" },
      "availabilitySet": {
         "id": "[resourceId('Microsoft.Compute/availabilitySets', parameters('adAvailabilitySetName'))]"
       },
      "osProfile": {
         "computerName": "[variables('vmName')]",
         "adminUsername": "[parameters('adminUsername')]",
         "adminPassword": "[parameters('adminPassword')]"
       },
      "storageProfile": {
         "imageReference": {
            "publisher": "[variables('imagePublisher')]",
            "offer": "[variables('imageOffer')]",
            "sku": "[parameters('windowsOSVersion')]",
            "version": "latest"
         },
         "osDisk": { "createOption": "FromImage" },
         "copy": [
            {
               "name": "dataDisks",
               "count": 2,
               "input": {
                  "lun": "[copyIndex('dataDisks')]",
                  "createOption": "Empty",
                  "diskSizeGB": "512",
                  "name": "[concat(variables('vmName'), '-datadisk', copyIndex('dataDisks'))]"
                }
             }
          ]
        },
         "networkProfile": {
         "networkInterfaces": [
             {
               "id": "[resourceId('Microsoft.Network/networkInterfaces', variables('nicName'))]"
             }
          ]
       }
    }
 }
```
