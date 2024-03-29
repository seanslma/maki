# Docker Command

## WORKDIR
- Define the working directory of a Docker container at any given time
- Any RUN, CMD, ADD, COPY, or ENTRYPOINT command will be executed in the specified working directory
- If reused, the path of the new working directory must be given relative to the current working directory

## ARG vs ENV
https://vsupalov.com/docker-arg-env-variable-guide/

https://docs.docker.com/engine/reference/builder/

Argument:

https://stackoverflow.com/questions/63278658/build-and-push-a-docker-image-with-build-arguments-from-devops-to-acr

Pass argument
```
arguments: '--build-arg ubuntu_version=20.04 --build-arg image_version=1.0.0'
```

## ADD vs COPY
https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#:~:text=ADD%20or%20COPY&text=COPY%20only%20supports%20the%20basic,rootfs.tar.xz%20%2F%20.
- ADD: has some features (like local-only tar extraction and remote URL support)
- COPY: only supports the basic copying of local files into the container, preferred as  it’s more transparent

## RUN
Mainly used to build images and install applications and packages, creating a new layer.

## CMD vs ENTRYPOINT
- CMD: Default parameters that ***can*** be overridden from the Docker CLI when a container is running.
- ENTRYPOINT: Default parameters that ***cannot*** be overridden when THE Docker Container runs with CLI parameters.
