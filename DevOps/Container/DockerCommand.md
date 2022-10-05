# Docker Command

## WORKDIR
- Define the working directory of a Docker container at any given time
- Any RUN, CMD, ADD, COPY, or ENTRYPOINT command will be executed in the specified working directory
- If reused, the path of the new working directory must be given relative to the current working directory

## ADD vs COPY
https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#:~:text=ADD%20or%20COPY&text=COPY%20only%20supports%20the%20basic,rootfs.tar.xz%20%2F%20.
- ADD: has some features (like local-only tar extraction and remote URL support)
- COPY: only supports the basic copying of local files into the container, prefferred as  it’s more transparent

## RUN
Mainly used to build images and install applications and packages, creating a new layer. 

## CMD vs ENTRYPOINT
- CMD: Default parameters that ***can*** be overridden from the Docker CLI when a container is running.
- ENTRYPOINT: Default parameters that ***cannot*** be overridden when THE Docker Container runs with CLI parameters.
