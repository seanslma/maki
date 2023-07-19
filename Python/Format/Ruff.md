# Ruff
https://github.com/astral-sh/ruff

Ruff (flake8, PyLint) is a Python linting tool that checks your Python codebase for errors, styling issues and complexity. 

**caveat**: avoid ruff to automatically fix your code - auto fix without review can be questionable or wrong.

## vscode extension

## config file
```toml
[tool.ruff]
line-length = 88
target-version = "py310"

# Allow unused variables when underscore-prefixed
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

# Enable the pycodestyle (`E`) and Pyflakes (`F`) rules by default
# Unlike Flake8, Ruff doesn't enable pycodestyle warnings (`W`) or
# McCabe complexity (`C901`) by default.
select = ["E", "F"]
ignore = []

# Disable autofix for all enabled rules (when `--fix`) is provided
fixable = []
unfixable = ["ALL"]
```
