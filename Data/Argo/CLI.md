# CLI

## install cli
```sh
curl -sLO https://github.com/argoproj/argo-workflows/releases/download/v3.4.9/argo-linux-amd64.gz
gunzip argo-linux-amd64.gz
chmod +x argo-linux-amd64
mv ./argo-linux-amd64 /usr/local/bin/argo
```
check if installed correctly `argo version`

## get help
```sh
argo --help
```

## run a workflow
```sh
argo submit -n argo --watch https://raw.githubusercontent.com/argoproj/argo-workflows/master/examples/hello-world.yaml
```

## list workflows
```sh
argo list -n argo
argo get -n argo @latest  #get details about the latest one
argo logs -n argo @latest #view logs
```
