# Format

## vscode black formatter extension
### option 1: works but slow
- install `black` in python env
- In user settings, add
```
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
```

### option 2 (works)
- install black-formatter extension
- In user settings, add
```json
"black-formatter.args": ["-S"]
"python.formatting.provider": "none",
"[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true
}
```

## black
https://black.readthedocs.io/

formatting the code with `black`: `black <filepath>`. e.g., `black .`

### config
https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file

pyproject.toml
```toml
[tool.black]
line-length = 88
target-version = ['py39']
skip-string-normalization = true #disable string double quotes normalization
include = '\.pyi?$'
--force-exclude = '''versioneer.py''' #exclide this file eith from saving or cli
preview = false
```

## Ruff (flake8, PyLint)
https://github.com/astral-sh/ruff

Ruff is a Python linting tool that checks your Python codebase for errors, styling issues and complexity.
