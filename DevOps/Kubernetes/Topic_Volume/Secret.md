# Secret
https://kubernetes.io/docs/concepts/configuration/secret/

Secrets are similar to `ConfigMaps` but are specifically intended to hold confidential data.

- A secret volume is used to pass sensitive information, such as passwords, to Pods.
- A Secret is always mounted as readOnly.
- A container using a Secret as a subPath volume mount will not receive Secret updates.

## security 
- Anyone with API access can retrieve or modify a Secret, and so can anyone with access to etcd
- Anyone who is authorized to create a Pod in a namespace can use that access to read any Secret in that namespace; this includes indirect access such as the ability to create a Deployment.

## mount example 
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-dotfiles-pod
spec:
  containers:
    - name: dotfile-test-container
      image: registry.k8s.io/busybox
      command:
        - ls
        - "-l"
        - "/etc/secret-volume"
      volumeMounts:
        - name: secret-volume          
          mountPath: "/etc/secret-volume"
          readOnly: true
  volumes:
    - name: secret-volume
      secret:
        secretName: dotfile-secret
```

In this example, the secret is a Kuberneters Secret resource. The following terraform code creats a k8s secret.
```tf
# https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/secret
resource "kubernetes_secret" "main" {
  depends_on = [kubernetes_namespace.ns]
  metadata {
    name        = "k8s-secret"
    labels      = {}
    annotations = {}
    namespace   = var.namespace
  }
  data = {
    "dev.user" = file("//example.com/config/dev.user")
    "dev.pass" = file("//example.com/config/dev.pass")
  }
}
```
