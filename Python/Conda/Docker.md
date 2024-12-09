# Docker

Steps to build the docker image for a conda app `my-app`.

## install conda
```dockerfile
COPY --chown=user:user docker/.bashenv /home/user/.bashenv
COPY --chown=user:user docker/.condarc /home/user/.condarc
ARG CONDA_VER=24.11.0
ARG MAMBA_VER=2.0.4
RUN conda-pin-package conda=$CONDA_VER && \
    conda config --set ssl_verify /etc/ssl/certs/ca-certificates.crt && \
    conda-install conda mamba==$MAMBA_VER && \
    conda-clean
```

## build conda package `my-app.tar.bz2`
Note that the `--croot` folder must be **outside of the project folder**.
```sh
export NAME=my-repo #pass value to meta.yaml variable NAME
conda build recipe --no-anaconda-upload --python 3.9 --croot ../conda-build --no-test
```

## create a new env and install `my-app`
If we can push the conda package to the conda repo we do not need the local repo.
```sh
conda create --name my-app-0.1.0 --yes
conda install --name my-app-0.1.0 --yes --quiet -v \
--channel /home/user/conda-build --no-update-deps my-app=0.1.0=py39_0 python=3.9
```

## export `conda.env` file listing all packages
```sh
conda activate my-app-0.1.0
conda list --explicit > conda.env
mv /path/to/conda.env path/to/my-app/
conda deactivate
conda remove --name my-app-0.1.0 --all --yes
```

Note that if we cannot send the conda package to the conda repo, 
we have to use the local repo to install the conda package:
```sh
conda install --name my-app-0.1.0 --yes --quiet -v \
 --channel /home/dev/conda-build \
 --no-update-deps my-app-0.1.0=py39_0 python=3.9
```
In this case, after exporting the conda.env file we should change the path of the new conda package according to the dockerfile content.

## copy local conda package folder to under the project folder
Note that the local path of the conda package in `conda.env` must be updated based on the dockerfile content.
```sh
cp -r ../conda-build .build/conda
```

## install conda and all the packages from `conda.env` in dockerfile 
```sh
conda create --yes --quiet --verbose --name my-app-0.1.0 --file conda.env && conda-clean
```

## build docker image
run docker build (pass value to ARG via `--build-arg`)
```sh
docker build . --build-arg NAME=my-app -f ./docker/linux/my-app.docker \
--no-cache --force-rm -t docker.example.com/uat/my-app:0.1.0
```
Here we pass the value for the `NMAE` variable in the dockerfile via the `--build-arg` command flag 
and tag the image as `docker.example.com/uat/my-app:0.1.0`. 

In case the build process fails, we can run into the last successful layer to check the issue:
```sh
docker run -it <last-successful-layer-id> bash -il
```

## push docker image
When the build process is finished we can push the docker image to the docker registry.
```sh
docker push docker.example.com/uat/my-app:0.1.0
```

## Python mamba workaround
```dockerfile
# Workaround for mamba SSL issue https://github.com/mamba-org/mamba/issues/628
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```

## Python conda ssl config
```dockerfile
# SSL configuration for httpx https://www.python-httpx.org/compatibility/#ssl-configuration
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
ENV MINIFORGE_ROOT=/home/user/miniforge/
```
