# Function

Functions can passed as an argument, returned from a function, modified, and assigned to a variable. 

## Closure
A nested function (function defined in another function) can access the outer scope of the enclosing function. This pattern is known as a Closure. It is a critical concept in decorators.

## functools.partial
`functools.partial` is a powerful function in Python's `functools` module. It allows you to create a new function by partially applying arguments to an existing function, effectively creating a new function with some of the arguments already set.

The `functools.partial` function returns a new function that can be called with the remaining arguments to complete the call to the original function. `functools.partial` is particularly useful when you have a function that requires many arguments, and you want to create a simplified version of it by fixing some of the arguments in advance. It's commonly used in functional programming and can make code more concise and easier to read.

Here's an example to illustrate its usage:
```py
import functools

# Original function
def add(a, b):
    return a + b

# Create a new function with 'a' fixed to 5
add_five = functools.partial(add, 5)

# Now, 'add_five' works like a function that takes only one argument 'b'
result = add_five(3)  # This is equivalent to calling add(5, 3)
print(result)  # Output: 8
```

