# Maturin

## build options
https://www.maturin.rs/metadata.html#add-maturin-build-options

### dynamic version
To use the Rust crate version from `Cargo.toml` as the Python package version:
```
[project]
name = "my-project"
dynamic = ["version"]
```
