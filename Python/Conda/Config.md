# Config

https://docs.conda.io/projects/conda/en/latest/configuration.html

https://conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html

## conda config
https://docs.conda.io/projects/conda/en/latest/commands/config.html

Modify configuration values in .condarc.
`--env` Write to the active conda environment .condarc file
```
conda config --add channels conda-canary
conda config --env --add pinned_packages conda=$conda_version
conda config --env --set verbosity 3
```
