# Python

## build docker image
https://towardsdatascience.com/a-simple-guide-to-deploying-a-dockerized-python-app-to-azure-29753ee507eb
```
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app

COPY requirements.txt . #include package info
RUN pip --no-cache-dir install -r requirements.txt

docker build -t my-api
```

## Dockerfile using pip
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

## Activate conda env in Dockerfile
https://pythonspeed.com/articles/activate-conda-dockerfile/
