# Chart repo

https://helm.sh/docs/topics/chart_repository/

## private repo with self-signed cert
https://github.com/helm/helm/issues/8868

not usable

## disable ssl cert
```
helm repo add jh https://jupyterhub.github.io/charts --insecure-skip-tls-verify
```

## use `--ca-file`
```
helm repo add jh https://jupyterhub.github.io/charts --ca-file /path/to/ca-file
```
