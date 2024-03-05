# Map db table

In SQLAlchemy, the `declarative_base` class is used to create a base class for declarative class definitions. Declarative classes are used to define database tables and their associated mapped classes in a more concise and expressive way. The link between the declarative class and the actual database table is established through a class attribute called `__tablename__` and the metadata associated with the `declarative_base` instance.

Here's a step-by-step explanation:

1. **Create a `declarative_base` instance:**
   First, you need to create a `declarative_base` instance. This instance is a factory for declarative base classes and will also hold the metadata about the tables.

    ```python
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()
    ```

2. **Define a Declarative Class:**
   Define a declarative class by inheriting from the `Base` class created in step 1. Within this class, define the table columns as class attributes, and specify the table name using the `__tablename__` attribute.

    ```python
    from sqlalchemy import Column, Integer, String

    class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)
        username = Column(String)
        email = Column(String)
    ```

3. **Table Creation:**
   Once you have defined your declarative class, you can use the `create_all()` method on the `Base` instance to create the associated tables in the database.

    ```python
    from sqlalchemy import create_engine

    # Replace 'sqlite:///example.db' with your actual database URL
    engine = create_engine('sqlite:///example.db')

    # Create tables in the database
    Base.metadata.create_all(engine)
    ```

Now, the `User` class is linked to the 'users' table in the database. SQLAlchemy uses the information provided in the declarative class (such as column types and constraints) to generate the appropriate SQL statements for table creation.

When you perform queries or insert/update records using instances of the `User` class, SQLAlchemy knows how to map the class attributes to the corresponding database columns, establishing a connection between your Python code and the database table.

Here's an example of how you might use the declarative class to add a user to the database:

```python
from sqlalchemy.orm import sessionmaker

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a new user
new_user = User(username='john_doe', email='john@example.com')

# Add the user to the session and commit to the database
session.add(new_user)
session.commit()
```

In this example, the `new_user` instance is associated with the 'users' table, and the changes are committed to the database through the SQLAlchemy session.
