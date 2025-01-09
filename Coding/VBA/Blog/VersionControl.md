# Git version control for Excel files

## Extract VBA Code
OleTools: This Python library can extract VBA code from Excel files into separate text files (e.g., `.bas`, `.cls`).
- Install OleTools: `pip install oletools`
- Extract VBA: `olevba your_workbook.xlsm`

## Version Control the Extracted Code
- Initialize a Git repository: `git init`
- Add the extracted VBA files: `git add *.bas *.cls`
- Commit the initial version: `git commit -m "Initial commit of VBA code"`
- *Push to a remote repository: `git push -u origin main`

## Git Hooks
Create a Git pre-commit hook script to automate the VBA extraction process before each commit.

pre-commit.py:
```python
#!/usr/bin/env python3

import subprocess

def main():
    subprocess.run(["olevba", "your_workbook.xlsm"]) 
    subprocess.run(["git", "add", "*.bas", "*.cls"]) 

if __name__ == "__main__":
    main()
```

## Important Notes
- We still need to include the Excel file itself in our repository for a complete record.
- Tools like `VBA Editor Pro` or `Rubberduck` can enhance your VBA development experience and potentially offer better integration with Git.

