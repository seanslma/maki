# Feature

## Feature example
https://users.rust-lang.org/t/wrap-rust-library-for-python-without-changing-rust-library/69285/4
```rs
#[cfg_attr(feature= "pyo3", pyo3::pyclass)]
pub struct Vector3 {
    pub x: i32,
    pub y: i32,
    pub z: i32
}

// Methods that are only available when building the extension module.
#[cfg_attr(feature= "pyo3", pyo3::pymethods)]
impl Vector3 {
    #[new]
    pub fn new(x: i32, y: i32, z: i32) -> Vector3 {
        Vector3 { x, y, z }
   }

   // ... getters and setters for Vector3's fields here

}

// Methods accessible to both Rust and Python
impl Vector3 {
    pub fn length(&self) -> f64 {
        ((self.x*self.x + self.y*self.y + self.z*self.z) as f64).sqrt()
    }
}
#[#[cfg_attr(feature= "pyo3", pyo3::pymodule)]]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Vector3>()?;
    Ok(())
}
```
