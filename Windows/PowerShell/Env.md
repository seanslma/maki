# Env

# Print env path line by line
```
echo $env:path.split(';') 
echo ($env:path).split(';') | Sort-Object
```
After activate the conda env, then use vscode to open the code, the env path will be included in the powershell env:path.
