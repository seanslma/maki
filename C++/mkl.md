# mkl

## install
Intel oneAPI MKL

https://software.intel.com/content/www/us/en/develop/articles/intel-mkl-link-line-advisor.html
## settings
C/C++, General->Additional Include Directories
  C:\Program Files (x86)\Intel\oneAPI\mkl\2021.1.1\include
 
Linker, General, Additional Library Directories
  C:\Program Files (x86)\Intel\oneAPI\mkl\2021.1.1\lib\intel64
  
Linker, Input, Additional Dependencies
  mkl_intel_lp64.lib;mkl_sequential.lib;mkl_core.lib #MKL Wrapper
  mkl_intel_ilp64.lib;mkl_sequential.lib;mkl_core.lib;mkl_blacs_msmpi_ilp64.lib #Solver

## solution?
Go to Project » Properties » Libraries » Use Intel Math Kernel Library and select Parallel, Sequential, or Cluster as appropriate. 

If the switch don't work,  you may solve the problem by adding mkl header file path, library and library path manually 

1. Select Project » Properties » Linker » General » Additional Library Directories. Add the architecture specific lib folder, for example, \lib\ia32. 

2. Select Project » Properties » Linker » Input » Additional Dependencies. Insert
  mkl_intel_c.lib mkl_sequential.lib mkl_core.lib if 32bit application. 
  mkl_intel_lp64.lib mkl_sequential.lib mkl_core.lib if 64bit application  
