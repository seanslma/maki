# Image

Every statement like RUN, COPY or ADD in the dockerfile will add a layer into docker image.

## build image
```
docker build https://github.com/docker/rootfs.git#<container-branch>:<docker-dir>
docker build . -f ./docker/filepath/my.docker --platform linux/amd64 -t 1.0.0 -t latest #manually build locally
```

## run image
```
docker run -it <image-id>                        #from default entrypoint
docker run -it --entrypoint /bin/bash <image-id> #from another entrypoint
```

## list images with sort
```
docker images | sort -k1 -h #sort by col1 - repo
```

## remove image with multiple repos/tags
```
docker rmi -f <image-id>
docker rmi [repo-name1]:[tag1] [repo-name2]:[tag2]
```

## check docker image layer sizes
```
docker history <image-id>
docker history --no-trunc <image-id> #keep full created-by command
```
Use `dive` to check layer content: https://github.com/wagoodman/dive

## reduce docker image size
https://jcristharif.com/conda-docker-tips.html

https://uwekorn.com/2021/03/01/deploying-conda-environments-in-docker-how-to-do-it-right.html

- Use an official base image whenever possible
- Use variations of Alpine images when possible
- Every `RUN` instruction in the `Dockerfile` writes a new layer in the image
- Every layer requires extra space on disk
- To keep the number layers to a minimum, commands should be combined into a single RUN instruction
- Free spaces after `update` using `apt clean all`
- Use multistage builds
- Use .dockerignore to exclude files not needed
- Squash layers: https://github.com/goldmann/docker-squash

## Conda docker image size
https://pythonspeed.com/articles/conda-docker-image-size/

Use `conda-pack` to remove conda and use multistage build together to reduce image size.

The base Conda environment is necessary for installation of packages, but once we’re running the code it really doesn’t add much.
