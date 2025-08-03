# Env file
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually

`environment.yml` vs `meta.yaml`:
- https://stackoverflow.com/questions/78309675/conda-build-duplication-of-requirements-in-environment-yml-and-meta-yml
- `environment.yml` describes what goes into an environment, encompassing all necessary packages for a project
- `meta.yaml` describes how to build a single Conda package, including its specific dependencies and build process
- `environment.yml` can be exported after building a conda package

## create env from env.yml
```
conda env create -f environment.yml
conda env create --name conda-env --file environment.yml --force #force creating new env with the input name if there is one
```

conda env create --name basic-ml-env --file environment.yml --force
environment.yml
```
name: dev
channels:
  - javascript
dependencies:
  - python=3.9
  - bokeh=2.4.2
  - numpy=1.21.*
  - nodejs=16.13.*
  - flask
  - pip
  - pip:
    - Flask-Testing
```
