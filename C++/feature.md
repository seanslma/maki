# feature

## decltype
```cpp
//get type of variable x
std::is_same<decltype(x), int>::value

//decltype(auto) is mainly used to derive the
//  return type of a forwarding function or package
decltype(auto) look_up_a_string_1() { return lookup1(); }
```

## delete
default and delete allow explicit declarations to take or reject functions that come with the compiler.
```cpp
class Magic {
public:
    Magic() = default; // explicit let compiler use default constructor
    Magic& operator=(const Magic&) = delete; // explicit declare refuse constructor
    Magic(int magic_number);
}
```

## override
When overriding a virtual function, introducing the override keyword will explicitly tell the compiler
to overload, and the compiler will check if the base function has such a virtual function, otherwise it will
not compile.
```cpp
struct Base {
    virtual void foo(int);
};
struct SubClass: Base {
    virtual void foo(int) override; // legal
    virtual void foo(float) override; // illegal, no virtual function in super class
};
```

when use override in derived class it is not necessary to use virtual for a function
```cpp
vector<double> const GetRow() const override; //good
virtual vector<double> const GetRow() const override; //not good
```

## final
final is to prevent the class from being continued to inherit and to terminate the virtual function
to continue to be overloaded.
```cpp
struct Base {
    virtual void foo() final;
};
struct SubClass1 final: Base {
}; // legal

struct SubClass2 : SubClass1 {
}; // illegal, SubClass1 has final

struct SubClass3: Base {
    void foo(); // illegal, foo has final
};
```

## noexcept
If a function modified with noexceptis thrown, the compiler will use std::terminate()to immediately terminate the program.

Specifies whether a function could throw exceptions. Code that uses move_if_nothrow (or whatchamacallit) will see a performance improvement if there's a noexcept move ctor. Strictly, move_if_noexcept won't return a copy, it will return a const lvalue-reference rather than an rvalue-reference. In general that will cause the caller to make a copy instead of a move, but move_if_noexcept isn't doing the copy.
```cpp
template <class T>
void foo() noexcept(noexcept(T())) {}
void bar() noexcept(true) {}
```
