# Install

## install conda
- install miniforge
- if `'conda' is not recognized as an internal or external command`. add conda path to user path env var.

## update conda
might not work - a fresh install might be needed!
```sh
conda update -n base conda
conda update -n base -c https://conda.anaconda.org/conda-forge conda
conda activate base
conda update mamba
```

Upgrade python to a new version in an existing env:
```sh
conda install python=3.12
mamba install python=3.12
```

Might need to manually remove some packages that are not compatible with python 3.12.
```sh
mamba remove pywin32 gurobi
```

fix inconsistency:
```sh
conda activate base
conda install anaconda
conda update --all
```
