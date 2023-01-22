# Env

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

## export env
```
conda activate <env> && conda list --explicit
```
The output can be used as the input <env-file> for creating an env.


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
