# Decorator

https://peps.python.org/pep-0318/

https://www.datacamp.com/tutorial/decorators-python

Decorators dynamically alter the functionality of a `function`, `method`, or `class` without having to directly use subclasses or change the source code of the function being decorated.
- allow adding new functionality to an existing object without modifying its structure
- decorators are usually called before the definition of a function that is decorated
- application of decorators for a function is from the bottom up
- can do preprocessing and after processing of the function call

## Function decorator
```py
import inspect
import functools
def decorator_maker(dp: str):
    "Decorator maker function"
    def decorator(func):
        "Decorator function"
        sig = inspect.signature(func)
        @functools.wraps(func)        
        def wrapper(*args, **kwargs):
            "Wrapper function"
            print(f'decorator maker args[0]: {dp}')
            bound = sig.bind(*args, **kwargs)
            kw = bound.arguments.get('kw')
            print(f'function call kwargs[kw]: {kw}')                                   
            kw = f'{dp}_{kw.upper()}'   #pre-processing kwargs
            kwargs['kw'] = kw 
            re = func(*args, **kwargs)  #function call
            rt = f'{re}_appendix'       #post-processing results
            kwargs['kw'] = kw 
            return rt
        return wrapper
    return decorator

@decorator_maker('prefix')
def decorated_func(*, kw: str):
    print(f'decorated func preprocessed kwargs[kw]: {kw}')
    return f'decorated func postprocessed result: {kw}'

print(decorated_func(kw='ok'))
```

## class decorator
https://builtin.com/software-engineering-perspectives/python-class-decorator

Class must have 
- `__init__`
- `__call__`
