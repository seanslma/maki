# Kubernetes

## mount secret as env var
```yaml
containers:
  - name: tfs-agent
    env:
      - name: ENV_VAR_K8S_SECRET
        valueFrom:
          secretKeyRef:
            name: k8s_secret
            key: name
```

## mount azure keyvault secret as env var
https://serverfault.com/questions/1075149/aks-with-azure-key-vault-env-variables-dont-load

secrets.yaml
```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1alpha1
kind: SecretProviderClass
metadata:
  name: azure-kv-secrets
  namespace: dev
spec:
  provider: azure
  parameters:
    usePodIdentity: "true"
    keyvaultName: "my-keyvault"                  
    objects:  |
      array:
        - |
          objectName: my-db-user
          objectType: secret
          #ObjectAlias: user.json
          objectVersion: ""
        - |
          objectName: my-db-pass
          objectType: secret
          #ObjectAlias: pass.json
          objectVersion: ""
    tenantId: "<tenantID>"
```
