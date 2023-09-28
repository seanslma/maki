# Docker

## build docker image for a conda app `my-app`
### build conda package `my-app.tar.bz2`
```sh
conda build recipe --no-anaconda-upload --croot ../conda-build --no-test
```
### create a new env and install `my-app`
```sh
conda create --name my-app-0.1.0 --yes
conda install --name my-app-0.1.0 --yes --quiet -v \
--channel /home/user/conda-build --no-update-deps my-app=0.1.0=py39_0 python=3.9
```
### export `conda.env` file listing all packages
```sh
conda activate my-app-0.1.0
conda list --explicit > conda.env
mv /path/to/conda.env path/to/my-app/
conda deactivate
conda remove --name my-app-0.1.0 --all --yes
```
### install conda and all the packages from `conda.env` in dockerfile 
```sh
conda create --yes --quiet --verbose --name my-app-0.1.0 --file conda.env && conda-clean
```
run docker build (pass value to ARG via `--build-arg`)
```sh
docker build . --build-arg NAME=my-app -f ./docker/linux/my-app.docker \
--no-cache --force-rm -t docker.example.com/uat/my-app:0.1.0-linux
```

## Python mamba workaround
```
# Workaround for mamba SSL issue https://github.com/mamba-org/mamba/issues/628
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```

## Python conda ssl config
```
# SSL configuration for httpx https://www.python-httpx.org/compatibility/#ssl-configuration
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
ENV MINIFORGE_ROOT=/home/user/miniforge/
```
