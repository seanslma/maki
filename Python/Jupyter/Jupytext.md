# Jupytext
Automatically convert notebook files to .py files

## Install
```sh
conda install -c conda-forge jupytext
```

## Settings
In repo add `jupytext.toml`:
```toml
# Always pair ipynb files with a light python script
formats = "ipynb,py:light"
```

Settings in Jupyter Lab
- Go to Settings > Settings Editor.
- In the Jupytext section, add the following:
```json
{
  "auto:light": true,
  "auto:percent": false,
  "md": false,
  "md:myst": true
}
```
This tells JupyterLab to automatically pair `.ipynb` notebooks with `.py` (Python script) files with the `light` format.

## Sync
Then manually sync all notebook files in current and subfolders to `.py`:
```sh
jupytext --set-formats ipynb,py:light --sync **/*.ipynb
```
Restart jupyter lab and it should work when the `.py` file is shown with the notebook icon.

We can also manually convert to notebook or back using:
```sh
jupytext --to py notebook.ipynb
jupytext --to ipynb notebook.py
```
