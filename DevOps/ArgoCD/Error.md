# Error

## rpc error: code = Unknown desc = authentication required
- add the user/pass for the helm chart repo to argocd
- or the user/pass(token) is not correct

## argocd repositories connection status failed
https://levelup.gitconnected.com/connect-argocd-to-your-private-github-repository-493b1483c01e

## could not read Username for 'https://github.com': No such device or address
There are two ways to check out code from Github:
- with user name/password,
- authenticate with an SSH key

In argocd, the credentials template still use `https` not `git@` but the credentials are provided via a pair of ssh keys.

when change the url to `git@` the error became `authentication required`. Maybe the ssh key is not correct??? The private key should not be base64 encoded!!!

If the repositories are connected seccussfully but the applications still show the error, the `AppProject sourceRepos` must also use the `git@` format when the authentication is via `ssh`.

## the server could not find the requested resource
The `apiVersion` for the app such Cronjob might be old and should be updated.

## Argo will not report helm chart rendering error
So the pods are simply not deployed.

## Argo renders templates first, then contacts the apiserver
In a helm chart, if the apiVersion depends on the k8s version. This could be go wrong
```yaml
{{- if .Capabilities.APIVersions.Has "policy/v1" }}
apiVersion: policy/v1
{{- else }}
apiVersion: policy/v1beta1
{{- end }}
kind: PodDisruptionBudget
```

## argocd outofsync `Pending deletion`
one pod is waiting for another pod but the other one was dead.

## Current Sync Status "Unknown"
https://github.com/argoproj/argo-cd/issues/15489

## connection reset by peer
firewall blokced the website?
```
rpc error: code = Unknown desc = Manifest generation error (cached):
`helm dependency build` failed exit status 1:
Error: could not download https://traefik.github.io/charts/traefik/traefik-10.19.5.tgz:
Get "https://traefik.github.io/charts/traefik/traefik-10.19.5.tgz":
read tcp 12.345.678.910:42622->188.199.100.155:443: read: connection reset by peer
```

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
