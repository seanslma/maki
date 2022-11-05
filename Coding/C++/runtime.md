# runtime

## lambda overload
```cpp
#include <type_traits> //std::is_same_v

template<typename T>
constexpr auto translate = [](T idx) 
{
    if constexpr (std::is_same_v<T, int>) {
        constexpr static int table[3]{ 2,1,0 };
        return table[idx];
    }
    else if constexpr (std::is_same_v<T, char>) {
        std::map<char, int> table{ {'a', 0}, {'b', 1}, {'c', 2}};
        return table[idx];
    }
};

//call it like
int r = translate<int>(line[0]);
int c = translate<char>(line[1]);
```

## rvalue
The xvalue defines a behavior in which temporary values can be identified while being able to be moved. To get a xvalue, you need to use the declaration of the rvalue reference: T &&, where T is the type. The statement of the rvalue reference extends the lifecycle of this temporary value, and as long as the variable is alive, the xvalue will continue to survive.

```cpp
int main()
{
    std::string lv1 = "string,"; // lv1 is a lvalue
    // std::string&& r1 = s1; // illegal, rvalue can't ref to lvalue
    std::string&& rv1 = std::move(lv1); // legal, std::move can convert lvalue to rvalue
    std::cout << rv1 << std::endl; // string,

    const std::string& lv2 = lv1 + lv1; // legal, const lvalue reference can extend temp variable's lifecycle
    // lv2 += "Test"; // illegal, const ref can't be modified
    std::cout << lv2 << std::endl; // string,string

    std::string&& rv2 = lv1 + lv2; // legal, rvalue ref extend lifecycle
    rv2 += "string"; // legal, non-const reference can be modified
    std::cout << rv2 << std::endl; // string,string,string,

    reference(rv2); // output: lvalue

    return 0;
}
```

## move
```cpp
std::string str = "Hello world.";
std::vector<std::string> v;

// use push_back(const T&), copy
v.push_back(str); 
std::cout << "str: " << str << std::endl; //"str: Hello world."

// use push_back(const T&&), no copy
v.push_back(std::move(str)); // str is empty now
std::cout << "str: " << str << std::endl; 
```
