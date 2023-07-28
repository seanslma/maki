# Generator
https://python-course.eu/advanced-python/generators-and-iterators.php

If there is a return statement in the code of a generator, the execution will stop 
with a StopIteration exception error when this code is executed by the Python interpreter.

## do not use `StopIteration`
https://stackoverflow.com/questions/14183803/what-is-the-difference-between-raise-stopiteration-and-a-return-statement-in-gen

From Python 3.3 there is no longer a need to explicitely using `raise StopIteration` in a Generator to end the generator. 

If you raise a StopIteration exception explicitly in your generator there may be some methods that go on to error because they were expecting to receive a regular return (or an implicit return) and were going to raise StopIteration themselves. 

## return type Generator
In Python type hinting, the generator type is represented as Generator[ValueType, SendType, ReturnType]. The second and third parameters represent the type of values that can be sent into the generator and the type of value that the generator can return, respectively.

For the specific example, `Generator[BinaryFile, None, None]`, the type hinting indicates the following:
- `ValueType`: BinaryFile
  `BinaryFile` represents the type of values that the generator yields. In this case, the generator is expected to yield values of the BinaryFile type.
- `SendTyp`: None
  `None` indicates that the generator cannot receive any values through the `send()` method. In other words, it does not expect any values to be sent into the generator during its execution.
- `ReturnType`: None
  `None` indicates that the generator does not have a specific return type. Generators in Python do not have a return statement; instead, they yield values using the `yield` keyword. As a result, their return type is implicitly considered None.

In summary, the `Generator[BinaryFile, None, None]` type hinting represents a generator that yields values of the `BinaryFile` type, does not accept any values through the `send()` method, and does not have a specific return value (i.e., its return type is implicitly `None`).
