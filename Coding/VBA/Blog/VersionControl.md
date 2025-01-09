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

## Use VBA to export files
```vba
Sub ExportVBACode()
    Dim vbComp As Object
    Dim filePath As String
    Dim folderPath As String
    Dim wb As Workbook

    ' Define the folder path where the VBA code will be saved (Change to your preferred folder)
    folderPath = "C:\path\to\your\export\folder\"  ' Adjust path as needed
    
    ' Ensure folder exists
    If Dir(folderPath, vbDirectory) = "" Then
        MkDir folderPath
    End If

    ' Loop through each component in the workbook's VBA project
    For Each vbComp In ThisWorkbook.VBProject.VBComponents
        ' Check if the module is a standard module, class module, or user form
        Select Case vbComp.Type
            Case vbext_ct_StdModule
                ' Export standard module as .bas
                filePath = folderPath & vbComp.Name & ".bas"
            Case vbext_ct_ClassModule
                ' Export class module as .cls
                filePath = folderPath & vbComp.Name & ".cls"
            Case vbext_ct_MSForm
                ' Export user form as .frm
                filePath = folderPath & vbComp.Name & ".frm"
            Case Else
                ' Skip unsupported types
                filePath = ""
                Debug.Print "Skipping: " & vbComp.Name
        End Select
        If filePath <> "" Then
            vbComp.Export filePath
         End If
    Next vbComp
    
    ' Notify user that the export is complete
    MsgBox "VBA code exported successfully to: " & folderPath, vbInformation
End Sub
```
