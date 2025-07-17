# Bashrc

## auto activate env
run `mamba shell init` to add code in `.bashrc`.
after that add `mamba activate my-env`

## conda env name not show in terminal
You have custom PS1 definitions that are being applied after your mamba activate p12 command.

This custom PS1 is being applied after mamba activate p12, effectively overwriting the prompt modification that Mamba attempts to do.

Move custom PS1 definitions before `conda/mamba initialize`.
