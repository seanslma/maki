# Private repo

There are three options to set the key used to connect to the private helm repo
- use a ssh key pair
- use a github user and token (PAT)
- get the user/token from secret store such as Azure KeyVault using manged identity

## ssh key pair
https://levelup.gitconnected.com/connect-argocd-to-your-private-github-repository-493b1483c01e

https://rderik.com/blog/setting-up-access-to-a-private-repository-in-argocd-with-ssm-parameter-store-and-external-secrets-operator/

Setup ArgoCD and Github so argocd can have access to private github repos.

### Generate ssh key-pair
```
ssh-keygen -t rsa -b 4096 -C "key for argocd to access private repo" -f id_rsa_argocd_repo
```

### Add deploy key on GitHub repo
On the repository settings, Deploy keys -> Add deploy key -> add the generated public key

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

## get user/pass from azure key vault
in resource "helm_release"
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