# Docker Command

## ARG vs ENV
- https://vsupalov.com/docker-arg-env-variable-guide/
- https://docs.docker.com/engine/reference/builder/
- https://stackoverflow.com/questions/63278658/build-and-push-a-docker-image-with-build-arguments-from-devops-to-acr

| Feature               | `ARG`                              | `ENV`                                     |
| --------------------- | ---------------------------------- | ----------------------------------------- |
| Scope                 | **Build-time only**                | **Runtime and build-time**                |
| Default Value         | Can be set with `ARG <name>=<val>` | Can be set with `ENV <name>=<val>`        |
| Overridable           | Overridden with `--build-arg`      | Overridden with `docker run -e`           |
| Persisted in Image    | ❌ Not saved in final image         | ✅ Saved in image and available at runtime |
| Use in RUN            | ✅ Yes                              | ✅ Yes                                     |
| Use in CMD/ENTRYPOINT | ❌ Not available                    | ✅ Available                               |

### arg
Pass argument
```
arguments: '--build-arg ubuntu_version=20.04 --build-arg image_version=1.0.0'
```

```dockerfile
ARG VERS=22.04
FROM ubuntu:$VERS
ARG VERS
RUN echo version is $VERS
```
- Second `VERS` will get default value from the first `global` one
- The ARG statement after a FROM is required to import the value into the build target

## ADD vs COPY
https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#:~:text=ADD%20or%20COPY&text=COPY%20only%20supports%20the%20basic,rootfs.tar.xz%20%2F%20.
- ADD: has some features (like local-only tar extraction and remote URL support)
- COPY: only supports the basic copying of local files into the container, preferred as  it’s more transparent

## RUN
Mainly used to build images and install applications and packages, creating a new layer.

## WORKDIR
- Define the working directory of a Docker container at any given time
- Any RUN, CMD, ADD, COPY, or ENTRYPOINT command will be executed in the specified working directory
- If reused, the path of the new working directory must be given relative to the current working directory
```dockerfile
ARG USER="user-name"
ARG HOME="/home/${USER}"
WORKDIR $HOME
```

## CMD vs ENTRYPOINT
- CMD: Default parameters that ***can*** be overridden from the Docker CLI when a container is running.
- ENTRYPOINT: Default parameters that ***cannot*** be overridden when the Docker Container runs with CLI parameters.
- CMD provides default arguments to the ENTRYPOINT.

| Feature           | `CMD`                                                                        | `ENTRYPOINT`                                                              |
| ----------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Purpose           | Default command + args to run **if no command is given** during `docker run` | Command that **always runs** when container starts                        |
| Can be overridden | Yes — by providing command/args in `docker run`                              | Yes — but you must explicitly override with `--entrypoint`                |
| Syntax forms      | Shell form (string), Exec form (list)                                        | Exec form (list) recommended                                              |
| Typical usage     | Default command with default args                                            | Main executable, often for making the container behave like an executable |

Example #1:
```dockerfile
ENTRYPOINT ["python", "app.py"]
CMD ["--help"]
```
- If you run `docker run my-image`, it runs: `python app.py --help`
- If you run `docker run my-image --version`, it runs: `python app.py --version`

Example #2
```dockerfile
COPY docker/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/bash"]
```
