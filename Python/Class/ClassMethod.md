# Class Method

 - Class methods are bound to the `class` and not the instance of the class. 
 - They can access and modify `class-level` variables but don't have access to instance-specific attributes.

## example
```py
class MyClass:
    class_variable = 0
    def __init__(self, value):
        self.value = value
    def instance_method(self):
        print('Instance method called with value:', self.value)
    @classmethod
    def class_method(cls):
        print('Class method called with class variable:', cls.class_variable)

# Create instance and call instance method
obj1 = MyClass(10)
obj1.instance_method()

# Call class method
MyClass.class_variable = 5
MyClass.class_method()
```
