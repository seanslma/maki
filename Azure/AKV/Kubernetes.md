# Kubernetes

## mount secret as env var
how to do it???
```yaml
containers:
  - name: tfs-agent
    env:
      - name: ENV_VAR_K8S_SECRET
        valueFrom:
          secretKeyRef:
            name: k8s_secret
            key: name
      - name: ENV_VAR_AZURE_KEYVAULT
        valueFrom:
          secretKeyRef:
            name: azure-secret
            key: AZP_POOL

  - name: AZP_URL
    valueFrom:
      vaultKeyRef:
        vault: <key-vault-name>  # Replace with your Key Vault name
        name: AZP_URL
```
