# SecretProviderClass

https://secrets-store-csi-driver.sigs.k8s.io/getting-started/usage.html

Create a `SecretProviderClass` to use the Secrets Store CSI driver, and add the `SecretProviderClass` into the `Deployment` Yaml.

On pod start and restart, the driver will communicate with the provider using gRPC to retrieve the secret content from the external Secrets Store you have specified in the SecretProviderClass custom resource. Then _**the volume is mounted in the pod**_ as tmpfs and the secret contents are written to the volume.

## azure key vault provider
https://docs.microsoft.com/en-us/azure/aks/csi-secrets-store-driver

https://github.com/Azure-Samples/secrets-store-csi-with-aks-akv

After the pod starts:
```
# show secrets held in secrets-store
kubectl exec -n <namespace> <pod-name> -- ls <mountPath>

# print a test secret 'ExampleSecret' held in secrets-store
kubectl exec -n <namespace> <pod-name> -- cat <mountPath>/ExampleSecret
```
or run into the pod:
```
kubectl exec -it -n <namespace> <pod-name> -- /bin/bash
ls -l ~/<mountPath>
```
