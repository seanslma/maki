# Sphinx

when to use `sphinx` and when to use `mkdocs`
- sphinx: complicated - for large projects
- mkdocs: simple - good for small projects

## Build Sphinx docs
Install `sphinx-build` first
```sh
mamba install sphinx myst-parser -y
mamba install furo # install theme
```
Then run
```sh
cd docs
sphinx-build -b html . _build
```
HTML lands in `docs/_build`.

or run from root
```sh
sphinx-build -b html docs/api _build/html/api
```
The output HTML will be in `_build/html/api`.


## PyData theme
```sh
mamba install sphinx pydata-sphinx-theme sphinx-rtd-theme sphinx-autodoc-typehints sphinx-design numpydoc -y
```
