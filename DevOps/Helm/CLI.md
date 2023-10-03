# CLI

## repo
```sh
helm repo list
helm repo add kured https://kubereboot.github.io/charts
helm repo remove kured
helm repo update
```

## list chart
```sh
helm search repo kured
helm search repo kured --versions
```

## install
```sh
helm install [NAME] [CHART] [flags]
helm install <release-name> <chart-name> #chart reference
helm install jenkins ./jenkins-1.2.3.tgz #packaged chart
helm install jenkins ./jenkins-archive   #unpacked chart folder
helm install jenkins https://example.com/charts/jenkins-1.2.3.tgz   #url
helm install jenkins --repo https://example.com/charts/jenkins-prd  #repo url
```

## check deployment status
```sh
helm status <release-name>
```

## list releases installed on cluster
```sh
helm list --namespace <namespace>
helm list --all-namespaces
```

## uninstall
```sh
helm uninstall <release-name> [...] [flags]
helm uninstall --namespace <namespace> ingress-nginx
```
