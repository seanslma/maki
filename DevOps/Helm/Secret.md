<!-- {% raw %} -->
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
- Mount files to a path via Kubernetes Secret
- Mount Azure Key Vault Secrets to another path via `SecretProviderClass`

secret.yaml
```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: "{{ .Chart.Name }}-kv-secret"
  namespace: "{{ .Values.namespace }}"
spec:
  provider: azure
  parameters:
    usePodIdentity: "true"
    keyvaultName: "{{ .Values.keyVaultName }}"
    objects:  |
      array:
        - |
          objectName: secret--a
          objectType: secret
          objectAlias: secret_a.json
          objectVersion: ""
        - |
          objectName: secret--b
          objectType: secret
          objectAlias: secret_b.json
          objectVersion: ""
    tenantId: "{{ .Values.tenantId }}"
```

deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name:  "{{ .Chart.Name }}"
  namespace: "{{ .Values.namespace }}"
spec:
  replicas: {{ .Values.replicaCount }}
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 0
      maxSurge: 1
  selector:
    matchLabels:
      app: "{{ .Chart.Name }}"
  template:
    metadata:
      labels:
        app: "{{ .Chart.Name }}"
        aadpodidbinding: "{{ .Values.azureIdentity.name }}"
    spec:
      enableServiceLinks: False
      containers:
        - name: "{{ .Chart.Name }}"
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: "{{ .Values.image.pullPolicy }}"
          ports:
            - containerPort: 5000
          resources:
            requests:
              cpu: "0.25"
              memory: 2Gi              
            limits:
              cpu: "0.5"
              memory: 4Gi              
          volumeMounts:
            - name: my-file-mount
              mountPath: /opt/app-path/
              readOnly: true
            - name: my-azure-kv-secrets-mount
              mountPath: "/home/<user>/my-secret/"
              readOnly: true
          env:
            - name: MY_DEV_API_URL
              value: https://example.com/api
      volumes:
        - name: my-file-mount
          secret:
            secretName: my-file-secret
        - name: my-azure-kv-secrets-mount
          csi:
            driver: secrets-store.csi.k8s.io
            readOnly: true
            volumeAttributes:
              secretProviderClass: "{{ .Chart.Name }}-kv-secret"
```

<!-- {% endraw %} -->
