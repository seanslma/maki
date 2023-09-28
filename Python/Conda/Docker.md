# Docker

## build docker image for a conda app `my-app`
### build conda package `my-app.tar.bz2`
```sh
conda build recipe --no-anaconda-upload --croot ../conda-build --no-test
```
### create a new env and install `my-app`
```sh
conda create --name my-app-0.1.0 python=3.9
conda activate my-app-0.1.0
conda install --yes --quiet -v --channel /home/user/conda-build --no-update-deps my-app=0.1.0=py39_0
```
### export `conda.env` file listing all packages
```sh
conda list --explicit > conda.env
conda deactivate
conda env remove --name my-app-0.1.0
```
- in dockerfile install conda and all the packages in `conda.env`
```sh

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
