# Env

## list envs
```sh
conda env list
```

## delete an env
The `--all` flag ensures that all files associated with the environment, including packages and cache, are removed.
```sh
conda remove --name <env-name> --all
```

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
```sh
conda create -n py10 python=3.10
conda create --name <env> --file <env-file> && conda-clean
```

## create env with exported env-file
```sh
conda activate <env> && conda list --explicit > environment.txt
```
The output can be used as the input <env-file> for creating a conda env when build a docker image.
```sh
conda create --name <name> --file ~/environment.txt && conda-clean
```

## create env with env yml file
```sh
conda env create -f environment.yml
```
environment.yml
```yaml
name: env-name
channels:
  - https://conda.mini-forge.com/uat/linux-64/
dependencies:
- python
- pip
- pip:
    - pypi-package-name
```

## install package
```sh
conda activate py10
conda install python=3.10
```

## install from local conda package
assume the conda package is: `/home/user/dev/.build/linux-64/my-dev-package-0.1.1-py39_0.tar.bz2`

why does not work???
```sh
conda activate dev-env \
&& conda install --yes --quiet -v --channel /home/user/dev/.build --no-update-deps my-dev-package=0.1.1=py39_0
```
one command (not correct?)
```sh
conda install -n dev-env --yes --quiet -v \
--channel /home/user/dev/.build --no-update-deps my-dev-package=0.1.1=py39_0 python=3.9
```
