# Matlab

## Call Matlab func from C# only with Matlab Runtime
- Make .NET Assembly
- Include MCR into package
- Silently install MCR
- Install C# Application
- Run Application

## Issues
In C# when adding 'mlapp.tlb', get the error:
A reference to 'C:\Program Files\MATLAB\R2008a\bin\win32\mlapp.tlb' could not be added. Please make sure that the file is accessible, and that it is a valid assembly or COM component.

## Solution
The reference error is occuring because MATLAB is not registered as a COM server. To work around this issue, register MATLAB as a COM server.
- Open a Command Prompt window,
- using cd, change to the bin\win32/64 subdirectory of the MATLAB installation directory
- and run the following command at the DOS prompt: matlab /regserver
