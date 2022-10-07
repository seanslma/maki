# Env file
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually

## create env from env.yml
```
conda env create -f environment.yml
conda env create --name conda-env --file environment.yml --force
```

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
