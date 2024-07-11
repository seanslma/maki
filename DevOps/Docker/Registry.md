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
- https://gist.github.com/jaytaylor/86d5efaddda926a25fa68c263830dac1
- https://gist.github.com/abelmferreira/c38036f9642f2adf260ad068ac08f187
- https://stackoverflow.com/questions/25436742/how-to-delete-images-from-a-private-docker-registry

Steps:
- Step 4: Delete the manifest
  ```sh
  curl -sS -X DELETE <domain-or-ip>:5000/v2/<repo>/manifests/<digest>
  ```
- Garbage collect the image. Run this command in your `docker registry container`:
  ```sh
  registry garbage-collect -m /etc/docker/registry/config.yml
  ```
config.yml
```yaml
version: 0.1
log:
    fields:
    service: registry
storage:
    cache:
        blobdescriptor: inmemory
    filesystem:
        rootdirectory: /var/lib/registry
    delete:
        enabled: true
http:
    addr: :5000
    headers:
        X-Content-Type-Options: [nosniff]
health:
    storagedriver:
        enabled: true
        interval: 10s
        threshold: 3
```  
