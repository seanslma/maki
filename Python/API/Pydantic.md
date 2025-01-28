# Pydantic

## 2.0 update list
https://2pointers.medium.com/an-introduction-to-pydantic-v2-alpha-pre-release-a-massive-improvement-over-previous-version-748a1f1118ba

## from_attributes
In Pydantic, the `from_attributes` setting in the `Config` class is a relatively new feature (introduced in Pydantic v2) 
that allows you to create a Pydantic model instance **directly from attributes** (i.e., keyword arguments) instead of the usual **dictionary-based initialization**.

By default, Pydantic models expect input data to be passed as a dictionary (or something that can be converted to one), 
but with `from_attributes = True`, you can initialize the model using individual attributes directly as you would with a regular class.


### Example
```python
from pydantic import BaseModel

class MyPydanticModel(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
```

### Without `from_attributes` (default behavior)
Normally, you would instantiate the model like this:

```python
data = {"id": 1, "name": "Alice"}
model_instance = MyPydanticModel(**data)
```

This works because Pydantic automatically parses the dictionary and assigns the values to the model's fields.

### With `from_attributes = True`
With `from_attributes` enabled, you can instantiate the model directly with attributes:

```python
model_instance = MyPydanticModel(id=1, name="Alice")
```

This works as if `id` and `name` were regular class attributes, but Pydantic will still validate them according to the model's type annotations and run any other model validation logic defined in the model.

### Why would you use `from_attributes`?
This feature can be helpful in scenarios where:
- You have objects or data sources that already provide values as individual attributes, and you want to avoid packing them into a dictionary first.
- You want to simplify the instantiation process when creating models programmatically.

In this case, the `from_attributes` setting makes the instantiation of `MyPydanticModel` feel like working with a normal Python class, where attributes can be passed directly instead of a dictionary.

### Summary
- **`from_attributes = True`** allows Pydantic models to be initialized using keyword arguments (like a regular Python class) rather than needing to pass a dictionary.
- It's useful when you already have data in the form of attributes, and it can simplify your model instantiation code.
