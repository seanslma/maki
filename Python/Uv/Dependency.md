# Dependencies

## uv package dependencies
find package dependencies from `actual import`
```sh
uvx deptry .        # missing, unused, and transitive-only deps
uvx pipreqs .       # generate requirements.txt from imports
```
`deptry` is the better choice if you already have a `pyproject.toml` or `requirements.txt`, since it compares them against your imports.
