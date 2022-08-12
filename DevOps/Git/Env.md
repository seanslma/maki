# Git Env

## git command in conda env not show anything
Run the command in terminal and it will show the error, e.g., msys-2.0.exe not found. This means the exe in the conda env is missing.

Under PowerShell, check the linked exe to git command:
```
Get-Command git #will show the source path of git.exe
```
