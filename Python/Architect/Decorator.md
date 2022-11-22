# Decorator

https://peps.python.org/pep-0318/

https://www.datacamp.com/tutorial/decorators-python

Decorators dynamically alter the functionality of a `function`, `method`, or `class` without having to directly use subclasses or change the source code of the function being decorated.
- allow adding new functionality to an existing object without modifying its structure
- decorators are usually called before the definition of a function that is decorated
- application of decorators for a function is from the bottom up
- can do preprocessing and after processing of the function call

## Example
```
def decorator_maker(dp):
    "Decorator maker function"
    def decorator(func):
        "Decorator function"
        def wrapper(fp):
            "Wrapper function"
            print(f'decorator maker parameters: {dp}')
            print(f'function call paremeters: {fp}')
            fp = f'prefix_{fp.upper()}' #pre-processing
            re = func(fp)               #function call
            rt = f'{re}_appendix'       #post-processing
            return rt
        return wrapper
    return decorator

@decorator_maker('dm')
def decorated_func(fp):
    return f'decorated function parameters: {fp}'

print(decorated_func('ok'))
```
