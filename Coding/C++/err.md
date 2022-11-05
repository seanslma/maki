# error

### This function or variable may be unsafe. Consider using localtime_s instead
add _CRT_SECURE_NO_WARNINGS to Preprocessor Definitions

### modify a standard header
If you want to modify a standard header, you might try specifying the folder where you put it in **Additional Include Directories**, so the compiler will always find your version first [C/C++ --> All Options].

config properties -> c/c++ -> language -> c++ language standard

### cannot open source file
additional include directory: $(SolutionDir)

### LINK : fatal error LNK1104: cannot open file
the debug run is not stopped, so the target exe file is locked. Or the exe is still open but invisible, use taskkill to close it

### error LNK2019: unresolved external symbol
circular reference is used in two classes, consider changing one class to be independent on the other

### undeclared identifier in method
forgot to add the class to the front of the method so the class's variable is not identified

### string_view
string_view is only available with C++17 or later, should change to language C++17  

'string_view': is not a member of 'std'. force rebuilding some failed projects separately works.

### why class member cannot be constexpr
class member will be initialized. but we need some const values for that class only.
put them in anonymous namespace should be OK. 

### do not return vector.data
create a vector in a function and return its data will end to no where. reason: vector in stack destroyed after return

### app terminated silently
if we use an old dll (such as lp solver) and a new api function does not exist, the app will terminate silently.

In events viewer we can fins something like:
```
Faulting application name: Simulate.exe, version: 0.0.0.0, time stamp: 0x5e3100d2
Faulting module name: KERNELBASE.dll, version: 10.0.17134.1184, time stamp: 0x8569b554
Exception code: 0xc06d007f
Fault offset: 0x000000000003a388
Faulting process id: 0x392c
Faulting application start time: 0x01d5d65760043adb
Faulting application path: C:\Users\dll\Simulate.exe
Faulting module path: C:\WINDOWS\System32\KERNELBASE.dll
```

### app stopped working
0xC000001D STATUS_ILLEGAL_INSTRUCTION\\
built using the wrong release config (Release, but should be Release NoAVX). Old machines do not have a processor supporting AVX

In events viewer we can fins something like:
```
  Problem Event Name:	APPCRASH
  Exception Code:	c000001d
  Exception Offset:	000000000001a915
  OS Version:	6.3.9600.2.0.0.16.7
```

### PBD File not loaded
These messages appear because you don't have the PDB files available in your computer. You can download them by selecting the "Microsoft Symbol Servers" checkbox at Tools > Options > Debugging > Symbol.

dll file was missing

### Pointer to incomplete class type is not allowed

An "incomplete class" is one declared but not defined. Seems forgot to include x.h in y.cpp.
