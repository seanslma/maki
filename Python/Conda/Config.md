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

# not activate conda's base environment on startup
conda config --set auto_activate_base false
```

## REQUESTS_CA_BUNDLE

## Auto activate conda env in windows cmd
- In `regedit` open path `HKEY_CURRENT_USER->Software->Microsoft->Command Processer`
- Add `AutoRun` with value `if exists "c:/users/usr/init_cmd.bat" "c:/users/usr/init_cmd.bat"`
- If `AutoRun` already there, append the command `@CALL "%CONDA_BAT%" activate my-env` to that bat file.

## Define new command for `uv pip`
In the `AutoRun` bat file append the command `@DOSKEY pp=uv pip $*`

## Change folder
In the `AutoRun` bat file append:
```bat
@REM Change directory to dev folder
@CD /D "C:\Users\my-name\dev"`
```
