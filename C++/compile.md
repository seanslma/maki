# compile

## DumpBin
```dos
@echo off

set "dir=C:\Users\name\Desktop"
set dumpbin=C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\VC\Tools\MSVC\14.16.27023\bin\Hostx64\x64\dumpbin.exe
"%dumpbin%" /EXPORTS /ALL /OUT:"%dir%\vpnapi_dump.txt" "%dir%\vpnapi.lib"

"%dumpbin%" /DEPENDENTS MathClient.exe

@pause
```

## DLL Search Order
https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order

## disable AVX

\<EnableEnhancedInstructionSet>NotSet</EnableEnhancedInstructionSet>
