# Feature

## show feature
```sh
az feature show -n AutoUpgradePreview --namespace Microsoft.ContainerService
```

## register feature
```sh
az feature register --namespace Microsoft.ContainerService -n AutoUpgradePreview
az feature registration show --provider-namespace Microsoft.ContainerService -n AutoUpgradePreview
```
