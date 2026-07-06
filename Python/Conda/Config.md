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
- Add `AutoRun` with value `if exists "c:/users/usr/int_cmd.bat" "c:/users/usr/int_cmd.bat"` in `regedit` path `HKEY_CURRENT_USER->Software->Microsoft->Command Processer`
- If `AutoRun` already there, append the command `@CALL "%CONDA_BAT%" activate my-env` to that bat file. 
