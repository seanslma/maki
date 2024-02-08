# Issue

## stuck on `solving environment`
https://github.com/conda/conda/issues/11919

Reason: added too many packages in base

Solution:
- remove packages un-related to conda in base, or
- use libmamba
  - Update conda and conda-build
    ```
    conda update conda
    conda update conda-build
    ```
  - Install libmamba and set the new solver
    ```
    conda install -n base conda-libmamba-solver
    conda config --set solver libmamba
    ```

## WSL: CondaHTTPError: HTTP 000 CONNECTION FAILED
restart wsl after install conda: `wsl --shutdown`

## conda env became base
https://stackoverflow.com/questions/57028760/why-conda-redefines-base-environment-after-activation-of-another-environment

If the `conda-build` package is installed in the environment name `dev`, then the `dev` environment becomes base after activation.

This means we should only install `conda-build` in base env not other envs.
