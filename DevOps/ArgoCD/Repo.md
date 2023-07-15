# Private repo

https://argo-cd.readthedocs.io/en/stable/user-guide/private-repositories/

There are two options to set the key used to connect to the private helm repo
- HTTPS using username/password, or github user/token (PAT)
- SSH private-public key pair with github deployment key (recommended more secure but one only for one repo)
Get the user/pass/key from secret store such as Azure KeyVault using managed identity

https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/

Each repository must have a `url` field and, depending on whether you connect using HTTPS, SSH, or GitHub App
- `username` and `password` (for `HTTPS`),
- `sshPrivateKey` (for `SSH`), or
- `githubAppPrivateKey` (for `GitHub App`)

## https
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: private-repo
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  type: git
  url: https://github.com/argoproj/my-private-repo
  password: my-password
  username: my-username
```

## ssh
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: private-repo
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  type: git
  url: git@github.com:argoproj/my-private-repo
  sshPrivateKey: |
    -----BEGIN OPENSSH PRIVATE KEY-----
    ...
    -----END OPENSSH PRIVATE KEY-----
```

## Repository Credentials template
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-repo-1
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  type: git
  url: https://github.com/argoproj/private-repo-1
---
apiVersion: v1
kind: Secret
metadata:
  name: my-repo-2
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  type: git
  url: https://github.com/argoproj/private-repo-2
---
apiVersion: v1
kind: Secret
metadata:
  name: private-repo-creds
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repo-creds
stringData:
  type: git
  url: https://github.com/argoproj
  password: my-password
  username: my-username
```

## github user and token
### Store PAT as a Kubernetes secret in the same namespace as your ArgoCD installation
```yaml
kubectl create secret generic github-creds \
  --namespace <argocd-namespace> \
  --from-literal=username=<github-username> \
  --from-literal=password=<github-personal-access-token>
```
### Modify the ArgoCD repository configuration to use the personal access token
We can do this by adding the following to the argocd-cm ConfigMap:
```yaml
data:
  repositories: |
    - url: https://github.com/<github-username>/<repository-name>.git
      type: helm
      name: <repo-name>
      usernameSecret:
        name: github-creds
        key: username
      passwordSecret:
        name: github-creds
        key: password
```

### get user/pass from azure key vault
in values.yaml
```yaml
configs:
  repositories:
    private-helm-repo:
      url: https://my-private-chart-repo.internal
      #   name: private-repo
      #   type: helm
      #   password: my-password
      #   username: my-username
```

in resource `helm_release`
```yaml
  set {
    name  = "configs.repositories.dev.username"
    value = "${jsondecode(data.azurerm_key_vault_secret.dev_creds.value)["username"]}"
  }
  set {
    name  = "configs.repositories.dev.password"
    value = "${jsondecode(data.azurerm_key_vault_secret.dev_creds.value)["password"]}"
  }
```

Here are some best practices to consider when using Azure Key Vault to retrieve secrets for your Helm charts:
- Limit access to the Azure Key Vault. Only grant access to the Azure Key Vault to the entities (users, groups, or services) that need it. Ensure that you have an access policy in place that restricts access to only the secrets that are required.
- Use Managed Identity. Use Managed Identity to authenticate to Azure Key Vault instead of using a client ID and secret, if possible. Managed Identity provides a secure way to access Azure resources without requiring any explicit credentials.
- Store the Azure Key Vault secrets in encrypted form. Ensure that the secrets stored in the Azure Key Vault are encrypted at rest and in transit. This will prevent unauthorized access to the secrets.
- Use Azure Key Vault with TLS. Configure your Azure Key Vault to use TLS, which will encrypt data in transit between the client and the vault.

## ssh key pair
https://levelup.gitconnected.com/connect-argocd-to-your-private-github-repository-493b1483c01e

https://rderik.com/blog/setting-up-access-to-a-private-repository-in-argocd-with-ssm-parameter-store-and-external-secrets-operator/

Setup ArgoCD and Github so argocd can have access to private github repos.

### Generate ssh key-pair
```sh
ssh-keygen -t rsa -b 4096 -C "argocd key for private repo" -f id_rsa_argocd_repo
```

### Add deploy key on GitHub repo
On the repository settings, Deploy keys -> Add deploy key -> add the generated public key

### Setup ssh authentication for ArgoCD
Encoding private key via base64:
```sh
cat id_rsa_argocd_repo | base64
```

Store the private key secret using Kubernetes `Secret`
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: argocd-repo-key
  namespace: argocd
type: Opaque
data:
  privateKey: one line base64 private key
```

Terraform
```yaml
resource "kubernetes_secret" "argocd" {
  metadata {
    name = "argocd-repo-key"
  }

  data = {
    privateKey = base64encode("<privatekey>")
  }

  type = "helm.sh/private"
}
```

Link the secret by `ConfigMap`
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-cm
  namespace: argocd
  labels:
    app.kubernetes.io/name: argocd-cm
    app.kubernetes.io/part-of: argocd
data:
  repositories: |
    - url: git@github.com:<user>/repo.git
      sshPrivateKeySecret:
        name: argocd-repo-key
        key: privateKey
```

how to get the privateKey from Azure Key Vault???
https://github.com/argoproj/argo-cd/issues/7878

Terraform
```yaml
resource "kubernetes_config_map" "argocd" {
  metadata {
    name = "argocd-cm"
  }

  data = {
    "repositories.yaml" = <<-EOT
    apiVersion: v1
    repositories:
    - name: my-private-repo
      url: https://my-private-repo.com/charts
      username: ${kubernetes_secret.private_helm_repo_creds.data["username"]}
      password: ${kubernetes_secret.private_helm_repo_creds.data["password"]}
    EOT
  }
}
```

Change `repoURL` from https to ssh and apply
```
https://github.com/<user>/repo.git
git@github.com:<user>/repo
```
