# SecretProviderClass

## azure usePodIdentity
```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1alpha1
kind: SecretProviderClass
metadata:
  name: key-vault-secret-file
spec:
  provider: azure
  parameters:
    usePodIdentity: "true"
    keyvaultName: "<key-vault-name>"
      objects: |
        array:
          - |
            objectName: <secret-name>
            objectType: secret
      tenantId: "<tenant-id>"
```
