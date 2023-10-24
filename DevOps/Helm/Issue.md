# Issue

## helm `connection reset by peer`
```
looks like "https://jupyterhub.github.io/helm-chart" is not a valid chart repository or cannot be reached:
Get "https://hub.jupyter.org/helm-chart/index.yaml": read tcp xxx.xxx.xxx.xxx:55360->xxx.xxx.xxx.xxx:443: read:
connection reset by peer
```
- an outgoing firewall that needs to be added in place for `hub.jupyter.org` (check blocked by firewall)
