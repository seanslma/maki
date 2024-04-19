# legacy-package-repository-deprecation
https://kubernetes.io/blog/2023/08/31/legacy-package-repository-deprecation/

## check if using the legacy package repo
```sh
cat /etc/apt/sources.list.d/kubernetes.list
```
If the repository definition not use `pkgs.k8s.io` we need to migrate

## migrate to the new community-operated repositories
https://kubernetes.io/blog/2023/08/15/pkgs-k8s-io-introduction/

1. Replace the apt repository definition so that apt points to the new repository
```sh
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
```

2. Download the public signing key for the Kubernetes package repositories
```sh
mkdir /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
```

3. Update the apt package index
```sh
sudo apt-get update
```
