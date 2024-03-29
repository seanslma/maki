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

 **mount `ConfigMap` as volume into a pod**
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

## mount multiple certificates to the same path
create two secrets. Another option is put multiple certificates in the same secret.
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: certificate-secret-1
data:
  certificate.crt: BASE64_ENCODED_CERTIFICATE_DATA_1
---
apiVersion: v1
kind: Secret
metadata:
  name: certificate-secret-2
data:
  certificate.crt: BASE64_ENCODED_CERTIFICATE_DATA_2
```

Create a Volume that combines these Secrets or ConfigMaps using a projected volume:
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
    - name: certificates-volume
      mountPath: /etc/ssl/certs
  volumes:
  - name: certificates-volume
    projected:
      sources:
      - secret:
          name: certificate-secret-1
          items:
            - key: certificate.crt
              path: certificate1.crt
      - secret:
          name: certificate-secret-2
          items:
            - key: certificate.crt
              path: certificate2.crt
```
In this example, we create a projected volume named certificates-volume that combines two Secrets (certificate-secret-1 and certificate-secret-2) and maps their certificate data to different file paths (certificate1.crt and certificate2.crt) within the /etc/ssl/certs directory. You can access these certificates in your application using the respective file paths.

## mount a secret to an existing path in docker image
If your Docker image already includes files at a specific path, and you want to mount a Kubernetes Secret at the same path within a running container, it depends on whether the mount point in your pod's definition conflicts with the existing files in your Docker image. Here's what you should consider:
- **Mount Conflict**: If the path you want to mount the Secret to already contains files within your Docker image, Kubernetes will typically mount the Secret over the existing files, effectively replacing them during the pod's execution.
-  **File Overwrite**: When you mount a Secret or ConfigMap into a directory that already contains files within the container, the files from the Secret or ConfigMap will overwrite the existing files within that directory for the duration of the pod's lifecycle.

Here's an example:

Suppose your Docker image has a certificate file at `/etc/ssl/certs/my-cert.crt`, and you mount a Secret or ConfigMap to the same path in your pod's definition. In that case, the certificate file from the Secret or ConfigMap will replace the existing `my-cert.crt` file within the container.

If your application expects specific files to be present in that directory and requires those files to have specific content, be cautious when overwriting them with mounted Secrets or ConfigMaps. Make sure the certificates in your Secret or ConfigMap are compatible with what your application expects.

If you want to merge the contents of the mounted Secret or ConfigMap with the existing files, you may need to handle the merge logic within your application or entrypoint script.

It's generally a good practice to ensure that the contents of your Secrets or ConfigMaps are compatible with the expectations of your application and won't lead to unexpected issues when files are overwritten.
