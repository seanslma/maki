# Env

## export env
```
conda activate <env> && conda list --explicit
```
The output can be used as the input <env-file> for creating an env.

## create env
```
conda create --name <env> --file <env-file> && conda-clean
```

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
