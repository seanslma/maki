# io

## format
```cpp
std::cout << std::fixed << std::setw(8);
std::cout << std::setprecision(2) << val << std::endl;
```

## std::endl vs /n
std::endl flushes the output stream. Flushing the output stream is not frequently required

## output to file
```cpp
string filepath = R"(C:\test.csv)";
ofstream file(filepath);
if (!file.good()) { return; }
file << "index,key,value" << "\n";
file << ind[0] << "," << key[0] << "," << val[0] << "\n";
file.close();
```

## insertion operators
The **default** value for floating-point precision is **six**. For example, the number 3466.9768 prints as 3466.98. To change the way this value prints, use the setprecision manipulator. The manipulator has two flags: fixed and scientific. If fixed is set, the number prints as 3466.976800. If scientific is set, it prints as 3.4669773+003.
```cpp
double values[] = { 1.23, 35.36, 653.7, 4358.24 };
char *names[] = { "Zoot", "Jimmy", "Al", "Stan" };
for (int i = 0; i < 4; i++)
    cout << setiosflags(ios::left) << setw(6) << names[i]
         << resetiosflags(ios::left) << setw(10) << setprecision(1) << values[i]
         << endl;
```

## A faster way to use stringstream

[A faster way to use stringstream](http://cplusplus.bordoon.com/speeding_up_string_conversions.html)

use a static variable of type stringstream and before you perform a string conversion, reset that varible to be empty


```cpp
#include <sstream>            
#include <iomanip>            
				      
using namespace std;                
static stringstream buffer; // moved up here 				                                    
				      
// first use                        
int i = 20;                         
buffer << setw(4) << i << '\0'; 
				      
string v = buffer.str().c_str();                                   
// v now contains "  20"                                            
				      
// second use                       
string tom("tom");                  
buffer.seekp(ios::beg); 
buffer << setw(10) << tom; 
				      
v = buffer.str().c_str();                                            
// v now contains "       tom"      
```

use the .c_str() method on the string returned by buffer.str() is that the seekp function does not reduce the total size of the string kept by the stringstream.

## write sol
```cpp
#include <fstream>
#include <iomanip>

auto pri = getColPrimals();
auto rct = getColReducedCost();
auto obj = getColObjectiveCoeffs();
std::ofstream fc("C:/tmp/lp_col_sol.csv");
if (!fc.good()) return false;
fc << "col,pri,rct,obj,\n";
for (auto i = 0; i < getNumCols(); ++i) {
  fc << 'C' << std::setfill('0') << std::setw(7) << i << ", " << pri[i] << ", " << rct[i] << ", " << obj[i] << "\n";
}
fc.close();

auto act = getRowPrimals();
auto dua = getRowDuals();
auto lhs = getRowLowerBounds();
auto rhs = getRowUpperBounds();
std::ofstream fr("C:/tmp/lp_row_sol.csv");
if (!fr.good()) return false;
fr << "row,dua,act,lhs,rhs,\n";
for (auto i = 0; i < getNumRows(); ++i) {
  fr << 'R' << std::setfill('0') << std::setw(7) << i << "," << dua[i] << "," << act[i] << "," << lhs[i] << "," << rhs[i] << "\n";
}
fr.close();
```
