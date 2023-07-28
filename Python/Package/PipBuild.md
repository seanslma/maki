# Pip build

## build whl package
```sh
pip wheel . --no-deps -w ../pip/pkg --no-cache-dir --verbose
pip wheel $(Build.SourcesDirectory) --no-deps -w $(Agent.TempDirectory)/pkg --no-cache-dir --verbose
```
