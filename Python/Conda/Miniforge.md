# Miniforge (Mambaforge)

https://github.com/conda-forge/miniforge

## install

```
curl -LO "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh
```

## uninstall
```
# reverse modified shell rc files
conda init --reverse --dry-run
conda init --reverse

# remove the entire Miniforge install directory
CONDA_BASE_ENVIRONMENT=$(conda info --base)
rm -rf ${CONDA_BASE_ENVIRONMENT}

# optionally remove hidden files and folders
rm -rf "${HOME}/.condarc"
```
