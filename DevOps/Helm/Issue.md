# Issue

## helm `connection reset by peer`
```
looks like "https://jupyterhub.github.io/helm-chart" is not a valid chart repository or cannot be reached:
Get "https://hub.jupyter.org/helm-chart/index.yaml": read tcp xxx.xxx.xxx.xxx:55360->xxx.xxx.xxx.xxx:443: read:
connection reset by peer
```
- an outgoing firewall that needs to be added in place for `hub.jupyter.org` (check blocked by firewall)

## index issue
Need to create the `index.yaml` in the folder.
```sh
helm repo index ./charts/ --url https://my-helm-repo-server/charts/
```

The `index.yaml` file can be created in any folder with the same archived `.tgz` helm chart files.
```
rpc error: code = Unknown desc = Manifest generation error (cached):
`helm dependency build` failed exit status 1:
Error: no cached repository for helm-manager-...c5f4a2 found. (try 'helm repo update'):
open /helm-working-dir/repository/helm-manager-...c5f4a2-index.yaml: no such file or directory
```
