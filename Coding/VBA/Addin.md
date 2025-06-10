# Addin

## create
Excel `xlam` file is a regular workbook, marked as add-in. Just save an Excel `xlsm` to `xlam`.

## install
File -> Options –> Add-ins.

The path is usually at: `C:\Users\<user-name>\AppData\Roaming\Microsoft\AddIns`

## scope
Functions in local Excel workbook will be used instead of the one in the addin. To use the addin version, 
add the addin name like `VBAProjectName.FunctionName`, or `ModuleName.FunctionName` or `VBAProjectName.ModuleName.FunctionName`

## convert back to `xlsm`
Open VBA -> AddIn -> ThisWorkbook -> IsAddIn -> False
