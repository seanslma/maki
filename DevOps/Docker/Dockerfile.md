# Dockerfile

## example
```dockerfile
ARG BASE_IMAGE=ubuntu:18.04
FROM ${BASE_IMAGE}
SHELL ["/bin/bash", "-c"] #SHELL ["/bin/bash", "--login", "-c"]

ENV PATH="/opt/my-path/:${PATH}"

ARG USER="app"
ARG GROUP="app"
ARG UID="1000"
ARG GID="1000"

RUN groupadd $GROUP --gid $GID \
    && useradd $USER --uid $UID --gid $GID --shell /bin/bash

USER $USER:$GROUP
WORKDIR /home/$USER
CMD ["/bin/bash"]

ARG AUTHORS
ARG RELEASE
ARG TIMESTAMP

LABEL \
    org.opencontainers.image.authors="${AUTHORS}" \
    org.opencontainers.image.authors="${RELEASE}" \
    org.opencontainers.image.created="${TIMESTAMP}"
```

## multiline 
https://github.com/moby/moby/issues/1799
```dockerfile
RUN echo 'All of your\n\
multiline that you ever wanted\n\
into a dockerfile\n'\
>> /etc/example.conf
```
