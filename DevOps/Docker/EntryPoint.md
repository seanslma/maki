# EntryPoint

https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#entrypoint

## example
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

## entrypoint vs cmd
The main difference between `ENTRYPOINT` and `CMD` in a Dockerfile lies in how they are used and overridden when running a container.

### CMD
- The `CMD` instruction in a Dockerfile specifies the default command to run when the container starts. 
- If a Dockerfile has multiple `CMD` instructions, only the last one will take effect.
- The `CMD` instruction can be overridden when running the container by specifying a command at the end of the `docker run` command. If no command is specified, the `CMD` instruction from the Dockerfile is executed.
- If the Dockerfile specifies an `ENTRYPOINT`, the `CMD` values are appended to the `ENTRYPOINT` to form the command that is run.

Example:
```Dockerfile
CMD ["nginx", "-g", "daemon off;"]
```
When running a container from this image, if no command is specified, it will start nginx with the specified configuration. However, you can override the `CMD` by specifying a different command when running the container.

### ENTRYPOINT
- The `ENTRYPOINT` instruction in a Dockerfile specifies the executable that will run when the container starts.
- If a Dockerfile has multiple `ENTRYPOINT` instructions, only the last one will take effect.
- The `ENTRYPOINT` instruction cannot be overridden like `CMD`. Instead, any commands provided when running the container are passed as arguments to the `ENTRYPOINT`.
- If the Dockerfile specifies both `ENTRYPOINT` and `CMD`, the `CMD` values are passed as arguments to the `ENTRYPOINT`.

Example:
```Dockerfile
ENTRYPOINT ["nginx", "-g", "daemon off;"]
```
In this case, `nginx` is the executable that will run when the container starts. Any additional arguments provided when running the container are appended to the `ENTRYPOINT` command.

In summary, `ENTRYPOINT` sets the main command and `CMD` provides default arguments for that command. When both are used together, `CMD` values are passed as arguments to `ENTRYPOINT`.
