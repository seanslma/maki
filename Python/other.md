## other

## python lecture notes
https://codefellows.github.io/sea-python-401d4/lectures/

## tree chart
install code2flow from github:

pip install git https://github.com/user/repo.git@branch

### vs code
There are 4 levels of settings in VS Code, which in ascending order of priority are: Default, User, Workspace, and Workspace Folder. 

  Ctrl+Shift+P -> python: select interpreter

VS Code Conda issue fix:
  - Disable activating terminal automatically, "python.terminal.activateEnvironment": false, and exit VSCode
  - Open command prompt or power shell outside of VSCode.
  - Navigate to your project or workspace directory.
  - Activate conda there.
  - Launch VSCode from the activated conda environment using code . or code project.code-workspace

in launch.json of folder .vscode, add [this will ensure the parent path is added to the path search list]
  "env": {"PYTHONPATH": "${workspaceRoot}"},

### other

```python
#not supported
++i

#check python version, output will be 32 or 64
import struct
struct.calcsize('P') * 8

#check module version
import pandas
pandas.__version__

#create a dictionary
dic = dict(zip(keys, vals))

#ifelse
fruit = 'Apple'
isApple = True if fruit == 'Apple' else False

#change dataframe two cols to dictionary (key has duplicate)
dic = {}
for x in range(len(df)):
   key = df.iloc[x,0]
   val = df.iloc[x,1]
   dic.setdefault(key, [])
   dic[key].append(val)
```

Use cProfile package in Python to find inefficiencies in your code.

In Python, the operation of verifying whether a specific example x belongs to S is efficient when S is declared as a set and is inefficient when S is declared as a list.

Using PyPy, Numba or similar tools to compile your Python code into fast, optimized machine code.
