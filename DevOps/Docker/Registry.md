# Registry

## push docker image to private registry
- omit `--password` so it will not be stored in command history
- the `username` can be the registry address such as `docker push docker.example.com/uat/redis:0.1.0`
```sh
docker login --username <username> [--password]
docker tag <image-id> <username>/my-repo
docker push <username>/my-repo
```
