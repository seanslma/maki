# struct

## assign vector to struct
```cpp
struct myStruct {
   int cnt;
   vector<double> vec;
};

vector<double> val;
val.reserve(10000);

myStruct stu;
stu.cnt = 1000;
stu.vec = std::move(val);
```
