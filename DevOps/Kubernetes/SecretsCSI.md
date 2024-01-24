# Secrets Store CSI Driver

https://secrets-store-csi-driver.sigs.k8s.io/

Allows Kubernetes to mount multiple secrets, keys, and certs stored in enterprise-grade external secrets stores into their pods as a volume.

## csi-secret driver
To deploy this SecretProviderClass in aks do we need to install the csi-secret driver.
- Enable the CSI Secrets Store Driver Add-on:
  - When creating a new AKS cluster, include the `--enable-addons azure-keyvault-secrets-provider` flag in the `az aks create` command.
- Install in Existing Clusters:
  - If the cluster already exists, install it using the following command:
  ```sh
  az aks enable-addons --addons azure-keyvault-secrets-provider --name myAKSCluster --resource-group myResourceGroup
  ```
  - The `secrets-store-csi-driver` pods should be in the `kube-system` namespace: `kubectl get pods -n kube-system`
- Install the csi-secret driver using helm chart
  - `https://azure.github.io/secrets-store-csi-driver-provider-azure/charts`

## SecretProviderClass
Example for azure
```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: my-azure-keyvault
  namespace: <namespace>
spec:
  provider: azure
  parameters:
    usePodIdentity: "true"       # Use pod identity for authentication
    keyvaultName: my-keyvault    # Name of the Azure Key Vault
    cloudName: AzurePublicCloud  # Optional, for Azure Stack or other clouds
    tenantId: <your-tenant-id>   # Tenant ID containing the Key Vault
    objects:                     # List of secrets to be mounted
      - objectName: my-secret        # Name of the secret in Key Vault
        objectType: secret           # Type of secret (secret, key, or cert)
        objectAlias: my-secret.json  # file name alias
        objectVersion: ""            # Optional, specify a particular version
      - objectName: my-certificate
        objectType: cert
      - objectName: my-key
        objectType: key
```
Same using `array`:
```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1alpha1
kind: SecretProviderClass
metadata:
  name: my-azure-keyvault
  namespace: <namespace>
spec:
  provider: azure
  parameters:
    usePodIdentity: "true"
    keyvaultName: my-keyvault
    cloudName: AzurePublicCloud
    tenantId: <your-tenant-id>
    objects: |
      array:
        - |
          objectName: my-secret
          objectType: secret
          objectVersion: ""
        - |
          objectName: my-certificate
          objectType: cert
        - |
          objectName: my-key
          objectType: key
```
