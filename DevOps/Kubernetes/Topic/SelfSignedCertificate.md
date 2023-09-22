# Self-signed Certificate
How to deploy a website such as web api using self-signed certificate?

## tls `secret`
We need to put the private/public tls certificate to a Kubernetes Secret.

## how to add certificate to the pod
To update CA certificates within a specific container running in a pod, you should consider 
- incorporating the necessary CA certificates directly into your container image or
- mounting them as a volume into your pod.

Update the Container Image: When building your container image, include the CA certificates you need. You can typically add them to the `/etc/ssl/certs/` directory in your image. This way, your container already has the necessary CA certificates when it starts.

### mount as volume
- Use a ConfigMap or Secret: Store your CA certificates in a Kubernetes ConfigMap or Secret.
- Then, mount this ConfigMap or Secret as a volume inside your pod.
- Your application within the container can use these certificates from the mounted volume.

Here's an example YAML configuration for mounting a `ConfigMap` as a volume into a pod:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: ca-certificates
data:
  my-ca.crt: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----

---
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: my-image:tag
    volumeMounts:
    - name: ca-certs
      mountPath: /etc/ssl/certs
      readOnly: true
  volumes:
  - name: ca-certs
    configMap:
      name: ca-certificates
```
In this example, we create a ConfigMap (ca-certificates) with your CA certificate(s). Then, we mount it into the container at `/etc/ssl/certs`.

Remember that this approach assumes that your application inside the container is configured to use the CA certificates from the specified directory.

If you need to update CA certificates dynamically in a running pod, you'll need to do it within your application itself, as Kubernetes pods are designed to be immutable, and system-level operations like update-ca-certificates aren't directly supported.

why not in `/usr/local/share/ca-certificates/extra/`?
- The choice of where to store CA certificates within your container depends on your application's requirements and how the application expects to find and use CA certificates. /etc/ssl/certs/ is commonly used in many Linux distributions, so it's often a good choice for compatibility.
- If your application is specifically configured to look in /usr/local/share/ca-certificates/extra/ for CA certificates, then you can certainly use that directory instead. Just make sure to configure your application accordingly so that it knows where to find the CA certificates.

**Mount Secret as volume in a pod**

create a secret
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ca-certificates-secret
data:
  my-ca.crt: BASE64_ENCODED_CERTIFICATE_DATA
```

mount secret as volume
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: your-image:tag
    volumeMounts:
    - name: ca-certs
      mountPath: /etc/ssl/certs
      readOnly: true
  volumes:
  - name: ca-certs
    secret:
      secretName: ca-certificates-secret
```
Using a Secret is a good approach for storing sensitive data like certificates because it provides encryption at rest. Just make sure to base64-encode the certificate data before storing it in the Secret, as shown in the example above. You can easily update the Secret when the certificates expire or need updating without modifying the Docker image or the pod definition. The updated certificates will be available to your pods.
