# Secret
see also:
Docker Container: SecretProviderClass

https://kubernetes.io/docs/concepts/configuration/secret/#overview-of-secrets

https://stackoverflow.com/questions/69260696/how-to-pass-azure-key-vault-secrets-to-kubernetes-pod-using-file-in-helm-charts

A secret can be used with a pod in three ways:
- As files in a volume mounted on one or more of its containers
- As container environment variable
- By the kubelet when pulling images for the Pod

## mounted volume file
secret.yaml
```
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: "{{ .Chart.Name }}-db"
  namespace: "{{ .Values.namespace }}"
spec:
  provider: azure
  parameters:
    usePodIdentity: "true"
    keyvaultName: "{{ .Values.keyVaultName }}"
    objects:  |
      array:
        - |
          objectName: db--test
          objectType: secret
          objectAlias: test.json
          objectVersion: ""
    tenantId: "xxxkjkj-sjjdf-jjk"
```

deployment.yaml
```
containers:
  volumeMounts:
  - name: secrets-mount
    mountPath: "/home/user/.config/secret"    
    readOnly: true
volumes:
  - name: database
    csi:
      driver: secrets-store.csi.k8s.io
      readOnly: true
      volumeAttributes:
        secretProviderClass: "{{ .Chart.Name }}-db"    
```
