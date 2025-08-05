# Issue

## run `conda init` before `conda activate`
https://stackoverflow.com/questions/77901825/unable-to-activate-environment-conda-prompted-to-run-conda-init-before-cond
solution: `source activate base` before `conda activate my_env`? Yes, works.

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

## package with specific version could not be installed
`package libarrow-substrait-16.0.0-h1f0e801_0_cpu requires libabseil >=20240116.2,<20240117.0a0, but none of the providers can be installed`

Solution: try to install the required version till we find the root blocker of the package.
In this case try to install `libabseil=20240116.2` and it will report the causer package and version.
