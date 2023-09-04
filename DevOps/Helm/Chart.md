# Chart

https://helm.sh/docs/topics/charts/

## put a chart into a web repo
```
mv jupyterhub-0.1.0.tgz ./jupyterhub/charts/ #copy chart package to the charts folder
helm repo index ./jupyterhub/charts/ --url https://my.github.io/jupyterhub/charts/ #create index.yaml
```

## create a helm chart and deploy it
```
helm create <chart-name>
helm install <release-name> <chart-name>/ --values <chart-name>/values.yaml 
```

## dependencies
https://helm.sh/docs/chart_best_practices/dependencies/#helm
