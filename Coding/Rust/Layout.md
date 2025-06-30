# Layout

https://medium.com/@kudryavtsev_ia/how-i-design-and-develop-real-world-python-extensions-in-rust-2abfe2377182

- with separate crates bundled into a single workspace
  - separate rust from python
- with namespaces and feature flags, placing Python-related code behind the features

## mixed
https://stackoverflow.com/questions/69057820/how-to-structure-a-mixed-python-rust-package-with-pyo3

`Note`:
- Only explicitely imported rust and python objects will be available in the python module
- We should avoid namespace conflict in rust and python - can't share the same namespace

## workspace
https://doc.rust-lang.org/book/ch14-03-cargo-workspaces.html
