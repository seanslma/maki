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
