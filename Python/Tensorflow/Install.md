# Install

https://www.tensorflow.org/install/pip#windows-native_1

## windows packages are not available from conda-forge

## install via pip in windows
https://www.tensorflow.org/install/pip#windows-native_1
```sh
pip install --upgrade pip
pip install tensorflow

# verify cpu setup
python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
# verify gpu setup
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```
