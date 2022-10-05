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
