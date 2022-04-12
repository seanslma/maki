# SecretProviderClass

https://secrets-store-csi-driver.sigs.k8s.io/getting-started/usage.html

Create a `SecretProviderClass` to use the Secrets Store CSI driver, and add the `SecretProviderClass` into the `Deployment` Yaml.

On pod start and restart, the driver will communicate with the provider using gRPC to retrieve the secret content from the external Secrets Store you have specified in the SecretProviderClass custom resource.
