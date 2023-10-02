# Registry

## push docker image to private registry
omit `--password` so it will not be stored in command history
```sh
docker login --username <username> [--password]
docker tag <image-id> <username>/my-repo
docker push <username>/my-repo
```
