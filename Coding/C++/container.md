# container

## array
Unlike std::vector, the size of the std::array object is fixed. If the container size is fixed, then the std::array container can be used first. In addition, since std::vector is automatically expanded, when a large amount of data is stored, and the container is deleted, the container does not automatically return the corresponding memory of the deleted element. In this case,
you need to manually run shrink_to_fit() to release this part of the memory.

```cpp
std::vector<int> v;
v.push_back(1);
v.push_back(2);
v.clear();
std::cout << "size:" << v.size() << std::endl; // output 0
std::cout << "capacity:" << v.capacity() << std::endl; // output 8
//additional memory can be returned to the system via the shrink_to_fit() call
v.shrink_to_fit();
```

Using std::array instead of traditional array can make the code more “modern” and encapsulate some manipulation functions, such as getting the array size and checking if it is not empty, and also using the standard friendly.

```cpp
std::array<int, 4> arr = {1, 2, 3, 4};

arr.empty(); // check if container is empty
arr.size(); // return the size of the container

// iterator support
for (auto &i : arr)
{
    // ...
}

// use lambda expression for sort
std::sort(arr.begin(), arr.end(), [](int a, int b) { return b < a; });

// array size must be constexpr
constexpr int len = 4;
std::array<int, len> arr = {1, 2, 3, 4};
void foo(int *p, int len) { return; }

std::array<int, 4> arr = {1,2,3,4};

// C-stype parameter passing
// foo(arr, arr.size()); // illegal, cannot convert implicitly
foo(&arr[0], arr.size());
foo(arr.data(), arr.size());

// use std::sort
std::sort(arr.begin(), arr.end()); 
```
