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
