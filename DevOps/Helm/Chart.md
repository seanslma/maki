# Chart

https://helm.sh/docs/topics/charts/

## put a chart into a web repo
```
mv jupyterhub-0.1.0.tgz ./jupyterhub/charts/ #copy chart package to the charts folder
helm repo index ./jupyterhub/charts/ --url https://my.github.io/jupyterhub/charts/ #create index.yaml
```
