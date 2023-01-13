# Dockerfile

## example
```
ARG BASE_IMAGE=ubuntu:18.04
FROM ${BASE_IMAGE}
SHELL ["/bin/bash", "-c"] #SHELL ["/bin/bash", "--login", "-c"]

ARG USER="app"
ARG GROUP="app"
ARG UID="1000"
ARG GID="1000"

RUN groupadd $GROUP --gid $GID \
    && useradd $USER --uid $UID --gid $GID --shell /bin/bash

USER $USER:$GROUP
WORKDIR /home/$USER
CMD ["/bin/bash"]
```

## multiline 
https://github.com/moby/moby/issues/1799
```
RUN echo 'All of your\n\
multiline that you ever wanted\n\
into a dockerfile\n'\
>> /etc/example.conf
```
