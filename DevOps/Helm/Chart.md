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

local dependencies: Chart.yaml
```yaml
dependencies:
  - name: mychart
    version: 3.1.1
    repository: file://.
```
the value of the `repository` should be the path to the folder in which there is a chart file called `<name>-<version>.tgz` (mychart-3.1.1.tgz). 
In the above example, the `tgz` file should be in the same folder for the `Chart.yaml` file.
