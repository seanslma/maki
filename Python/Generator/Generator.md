# Generator
https://python-course.eu/advanced-python/generators-and-iterators.php

If there is a return statement in the code of a generator, the execution will stop 
with a StopIteration exception error when this code is executed by the Python interpreter.

## do not use `StopIteration`
https://stackoverflow.com/questions/14183803/what-is-the-difference-between-raise-stopiteration-and-a-return-statement-in-gen

From Python 3.3 there is no longer a need to explicitely using `raise StopIteration` in a Generator to end the generator. 

If you raise a StopIteration exception explicitly in your generator there may be some methods that go on to error because they were expecting to receive a regular return (or an implicit return) and were going to raise StopIteration themselves. 
