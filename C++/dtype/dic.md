# dict

## std::map

```cpp
//keys are strings and values integers
std::map<std::string, int> pwdUid;

//keys are integers and values are strings
std::map<int, std::string> uidNam;

//insert a user
uidNam[0] = std::string("John Small");
//retrieve a user
std::cout << "User #0 is named: " << uidNam[0] << std::endl;
```

### Checking if a key exists in map
```cpp
std::map::count(key) //return the number of keys which matches the queried key
std::map::find(key) //return an iterator to the found object, or std::map::end() if the object is not found
```

### Iteration
```cpp
std::map<int, std::string> values;
for(auto& x : values) {
    std::cout << x.first << "," << x.second << std::endl;
}
```

### delete one element
```cpp
//remove a user by key
uidNam[2971] = std::string("John");
uidNam.erase(2971); //removes the entry [2971, "John"]
 
//remove a user by iterator
auto iterator = uidNam.find("Ana");
uidNam.erase(iterator); //removes the entry [7362, "Ana"]
```

### avoid copying
this will create a copy of the map value vector
```cpp
myMap = map<int, vector<double>>();
myMap[key].push_back('a');
```


to avoid the copying we should use
```cpp
auto &vec = myMap[key];
vec.push_back('a');
```
