# EntryPoint

https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#entrypoint

docker-entrypoint file
```sh
#!/bin/bash
set -e
exec "$@"
```

docker entrypoint
```sh
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/bash"]
```
