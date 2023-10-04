# Config

## `pytest` config
setup.cfg
```
[tool:pytest]
testpaths = tests
addopts =
    -v
    --tb=short
doctest_optionflags =
    NORMALIZE_WHITESPACE
    ELLIPSIS
    FLOAT_CMP
```
Explicitly set the test paths to improve the test collection speed.
