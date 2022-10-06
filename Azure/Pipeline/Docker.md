# Docker

## Argument
https://stackoverflow.com/questions/63278658/build-and-push-a-docker-image-with-build-arguments-from-devops-to-acr

## Python dockerfile using pip
```
ARG BASE_IMAGE=continuumio/miniconda3
FROM ${BASE_IMAGE}
SHELL ["/bin/bash", "-c"]

WORKDIR /usr/app

COPY *.whl ./
COPY requirements.txt ./
RUN python -m pip install *.whl \
    && python -m pip install --no-cache-dir -r requirements.txt

CMD [ "test-run" ]
```
