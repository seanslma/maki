# string

string is same to other basic types like int, double, so assignment will make a copy of the string [e.g., string s = str_old;].

#include <iostream> when using std::cout

For all the standard library types the member function **empty()** means "are you empty?".

The **clear()** member function is inherited from ios and is used to clear the error state of the stream, e.g. if a file stream has the error state set to eofbit (end-of-file), then calling clear() will set the error state back to goodbit (no error).

if stringstream is at EOF, ss.str("") only sets the content to empty and clears the buffer, we should also use ss.clear() to clear EOF.

You could also use **seekp**(0), but that won't clear the buffer, it will just insert the next value at the beginning. However, it is not possible to use seekp() method on an empty stringstream.

## string_view
std::string_view is just an abstraction of the (char * begin, char * end) pair. std::string_view is a good alternative to std::string const& if you don't need to guarantee a null terminated string. also string_view has a better performance.

```cpp
std::string str{"foobar"};
std::string_view bar{str.c_str(), str.size()};
bar.remove_prefix(3);
assert(bar == "bar");

//string_view to string
string str(str_view); //will make a copy
//bad, why? 
//returns a pointer to the underlying character array, 
//may return a pointer to a buffer that is not null
string str = str_view.data(); 
```
