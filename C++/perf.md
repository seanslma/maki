# perf

## string
https://www.oreilly.com/library/view/optimized-c/9781491922057/ch04.html\\

```cpp
//reduce Reallocation by Reserving Storage (1.2x faster)
std::string remove_ctrl_reserve(std::string s) {
    std::string result;
    result.reserve(s.length());
    for (int i=0; i<s.length(); ++i) {
        if (s[i] >= 0x20) result += s[i];
    }
    return result;
}
//eliminate Pointer Dereference Using Iterators (1.2x faster)
std::string remove_ctrl_ref_args_it(std::string const& s) {
    std::string result;
    result.reserve(s.length());
    for (auto it=s.begin(),end=s.end(); it != end; ++it) {
        if (*it >= 0x20) result += *it;
    }
    return result;
}
//use Character Arrays Instead of Strings (10x faster)
void remove_ctrl_cstrings(char* destp, char const* srcp, size_t size) {
    for (size_t i=0; i<size; ++i) {
        if (srcp[i] >= 0x20) *destp++ = srcp[i];
    }
    *destp = 0;
}
```
