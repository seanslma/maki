<!-- {% raw %} -->
# Secrets

https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/

https://howchoo.com/kubernetes/read-kubernetes-secrets

## secret types
https://kubernetes.io/docs/concepts/configuration/secret/
- Opaque Secrets
- ServiceAccount token Secrets
- Basic authentication Secret
- SSH authentication Secrets
- TLS Secrets

## get secret
```sh
kubectl get secrets                   #only summary like name and type etc.
kubectl describe secret <secret-name> #more details such as filenames
kubectl get secret <secret-name> -n <namespace> -o yaml #base64‑encoded contents
kubectl get secret <secret-name> -o jsonpath="{.data.username}" | base64 --decode
kubectl get secret <secret-name> -o jsonpath="{.data.user\.name}" | base64 --decode
kubectl get secret <secret-name> -o jsonpath="{.data['user\.name']}" | base64 --decode
```

## delete secret
```sh
kubectl delete secret <secret-name>
```

## ways of creating secrets
Kubernetes provides three ways of creating secrets:
- from files
- from the command line
- from YAML or JSON definitions

### create secret from files
```sh
#opaque secret: the schema of the contents is unknown
kubectl create secret generic <secret-name> \
  --from-file=./username.txt \
  --from-file=./password.txt

kubectl create secret generic <secret-name> \
  --from-file=username=./username.txt \
  --from-file=password=./password.txt

kubectl create secret <secret-name> \
  --key /etc/certs/{name}.com.key \
  --cert /etc/certs/{name}.com.crt \
  -n <namespace>

kubectl create secret tls <secret-name> \
  --namespace <namespace> \
  --key tls.key \
  --cert tls.crt
```

### create secret using literals
```sh
kubectl create secret generic <secret-name> \
  --namespace=default \
  --from-literal=<key>=<val> \
  --from-literal=password='S!X*hz$z='
```

### create secret from yaml
`kubectl create -f secret.yaml`
```sh
apiVersion: v1
kind: Secret
metadata:
  name: myapiurltoken-yaml
type: Opaque
data:
  url: <base64-encoded values>
  token: <base64-encoded values>
```

## edit secret
```sh
EDITOR="vi"  kubectl edit secrets <secret-name>

#from file
dk=$(base64 < "./a.key" | tr -d '\n')
dv=$(base64 < "./a.crt" | tr -d '\n')

#from string
dk=$(echo -n 'key-string' | base64)
dv=$(echo -n 'crt-string' | base64)

kubectl get secrets <secret-name> -n <namespace> -o json \
    | jq ".data[\"a.key\"] |= \"$dk\"" \
    | jq ".data[\"a.crt\"] |= \"$dv\"" \
    | kubectl apply -f -

kubectl patch secret <secret-name> -n <namespace> \
    -p "{\"data\":{\"a.key\":\"${dk}\",\"a.crt\":\"${dv}\"}}"
```

delete a key in data
```sh
kubectl patch configmap myconfigmap --type=json -p='[{"op": "remove", "path": "/data/mykey"}]'
```

## ways of consuming secrets
Kubernetes provides two ways of consuming secrets: env var and mounted file (preferred).

### Why mounted file is preferred
It is more secure to mount secrets as files.
- Kubernetes treats secrets as environment variables securely
- but the container runtime doesn't treat them securely
```sh
#InstanceID: vmssxxxxxx
kubectl describe pod <pod-name> | grep Node
#DockerID of running pod: docker://<DockerID>
kubectl describe pod <pod-name> | grep 'Container ID'

INSTANCE=<InstanceID>
DOCKERID=<DockerID>
VMSS=$(az vmss list --query '[].name' -o tsv) #node scale set name
RGNAME=$(az vmss list --query '[].resourceGroup' -o tsv) #resource group name

#Kubernetes version <= 1.18 (Docker)
az vmss run-command invoke -g $RGNAME -n $VMSS \
  --command-id RunShellScript --instance-id $INSTANCE \
  --scripts "docker inspect -f '{{ .Config.Env }}' $DOCKERID" -o yaml | grep SECRET

#Kubernetes version >= 1.19 (containerd)
az vmss run-command invoke -g $RGNAME -n $VMSS \
  --command-id RunShellScript --instance-id $INSTANCE \
  --scripts "crictl inspect --output yaml $DOCKERID" -o yaml | grep SECRET
```

### Using secrets as an environment variable
https://blog.nillsf.com/index.php/2020/02/24/dont-use-environment-variables-in-kubernetes-to-consume-secrets/

why is not recommended to mount secretes as env vars: 
- the secret value is accessible within the running pod
- any app can use the secret values by referencing the appropriate env var
- value of the env var will not be updated when the secret itself is updated
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-using-env
spec:
  containers:
  - name: nginx
    image: nginx
  env:
  - name: SECRET_URL
    valueFrom:
      secretKeyRef:
        name: <secret-name>
        key: secreturl.txt
  - name: SECRET_TOKEN
    valueFrom:
      secretKeyRef:
        name: <secret-name>
        key: secrettoken.txt
restartPolicy: Never
```

### Mounting secrets as a file in a pod (preferred)
- the secret value is accessible within the running pod
- can limit which processes can get access to the contents of these files via file system permissions
- secrets mounted as files will be dynamically updated as the secrets are updated
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-using-volume
spec:
  containers:
  - name: nginx
    image: nginx
  volumeMounts:
  - name: <volume-mount-name>
    mountPath: "/etc/secrets"
    readOnly: true
volumes:
- name: <volume-mount-name>
  secret:
    secretName: <secret-name>
```

### Mount a secret as a file and then using bash to set the env vars
Create a `SecretProviderClass`: This will configure how to fetch the secret from Azure Key Vault.
```yaml
apiVersion: secrets-store.csi.k8s.io/v1
kind: SecretProviderClass
metadata:
  name: keyvault-secret-provider
spec:
  provider: azure
  parameters:
    usePodIdentity: "false"  # Set to "true" if using managed identity
    keyvaultName: "<your-key-vault-name>"
    cloudName: "AzurePublicCloud"  # Adjust as necessary
    objects: |
      array:
        - |
          objectName: "<your-secret-name>"
          objectType: secret
    tenantId: "<your-tenant-id>"
```

Create a `Deployment` with Volume Mount: Update your deployment to include the SecretProviderClass as a volume.
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: example-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: example
  template:
    metadata:
      labels:
        app: example
    spec:
      containers:
        - name: example-container
          image: your-image
          volumeMounts:
            - name: secrets-store
              mountPath: /mnt/secrets-store
          command: ["/bin/bash", "-c"]
          args:
            - |
              # Install jq if it's not available
              apt-get update && apt-get install -y jq && \
              # Read the JSON file and set environment variables
              for key in $(jq -r 'keys[]' /mnt/secrets-store/<your-secret-name>.json); do
                  value=$(jq -r ".\"$key\"" /mnt/secrets-store/<your-secret-name>.json)
                  export "$key=$value"
              done
              # Your application command here, e.g., ./start-app
      volumes:
        - name: secrets-store
          csi:
            driver: secrets-store.csi.k8s.io
            volumeAttributes:
              secretProviderClass: "keyvault-secret-provider"
```

<!-- {% endraw %} -->
