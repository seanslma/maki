# VSCode

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
