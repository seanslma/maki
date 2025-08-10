# Pip build
- https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
- https://github.com/pypa/sampleproject
- old: https://medium.com/@jonathan.hoffman91/a-step-by-step-guide-to-building-python-wheels-4ed8160809a2
- new: https://medium.com/@jonathan_b/building-a-python-wheel-with-pyproject-toml-bbab842e989a

## build whl package
```sh
pip wheel . --no-deps -w . --no-cache-dir --verbose
pip wheel . --no-deps -w ../pip/pkg --no-cache-dir --verbose
pip wheel $(Build.SourcesDirectory) --no-deps -w $(Agent.TempDirectory)/pkg --no-cache-dir --verbose
```

## use build
```sh
pip install build setuptools wheel twine
python -m build --outdir build-output/
python -m build --wheel --no-isolation --outdir build-output/
```
- `--no-isolation`: will not create a separate env, faster but less reproducible
