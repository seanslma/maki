# Registry

## push docker image to private registry
- omit `--password` so it will not be stored in command history
- the `username` can be the registry address such as `docker push docker.example.com/uat/redis:0.1.0`
```sh
docker login --username <username> [--password]
docker tag <image-id> <username>/my-repo
docker push <username>/my-repo
```

## create a self-hosted registry
- https://microsoft.github.io/PartsUnlimitedMRP/adv/adv-24-Docker-Hub.html
- https://github.com/distribution/distribution

## delete docker images in private registry
https://gist.github.com/jaytaylor/86d5efaddda926a25fa68c263830dac1
