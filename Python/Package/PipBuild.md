# Pip build

## build whl package
```
pip wheel $(Build.SourcesDirectory) --no-deps -w $(Agent.TempDirectory)/pkg --no-cache-dir --verbose
```
