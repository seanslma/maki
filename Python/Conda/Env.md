# Env

## create env and install packages
https://stackoverflow.com/questions/66291897/conda-create-and-conda-install

option 1: create an environment, activate, install packages
```sh
conda create --name env_name python=3.10
conda activate env_name
conda install package_name another_package
```

option 2: create an environment with packages
```sh
conda create -name env_name python=3.10 package_name another_package
conda activate env_name
```

## create env
```
conda create -n py10 python=3.10
conda create --name <env> --file <env-file> && conda-clean
```

## install package
```
conda activate py10
conda install python=3.10
```

## export env-file
```
conda activate <env> && conda list --explicit
```
The output can be used as the input <env-file> for creating a conda env when build a docker image.

## create env with env yml file
```
conda env create -f environment.yml
```
environment.yml
```
name: env-name
channels:
  - https://conda.mini-forge.com/uat/linux-64/
dependencies:
- python
- pip
- pip:
    - pypi-package-name
```
