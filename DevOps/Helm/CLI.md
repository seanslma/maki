# CLI

## repo
```
helm repo list
helm repo add kured https://kubereboot.github.io/charts
helm repo remove kured
```

## list chart
```
helm search repo kured
helm search repo kured --versions
```

## install
```
helm install [NAME] [CHART] [flags]
helm install <release-name> <chart-name> #chart reference
helm install jenkins ./jenkins-1.2.3.tgz #packaged chart
helm install jenkins ./jenkins-archive   #unpacked chart folder
helm install jenkins https://example.com/charts/jenkins-1.2.3.tgz   #url
helm install jenkins --repo https://example.com/charts/jenkins-prd  #repo url
```

## uninstall
```
helm uninstall <release-name> [...] [flags]
```

## check deployment status
```
helm status <release-name>
```
