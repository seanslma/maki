# Unit Test

## mock
https://docs.python.org/3/library/unittest.mock.html

Mock part of method or object so, for example, you can use the mocked data (instead of getting data from the database) to test part of a function.
```
from unittest.mock import (
    Mock,
    patch,
)

# in namespace dev.db
def get_from_db():
    return pd.DataFrame({'x':[1,2], 'y':[3,4]})
  
def get_db_data():
    df = get_from_db()
    df += 1
    return df
  
def test_get_db_data():  
    db_data = pd.DataFrame({'x':[1,2], 'y':[3,4]})
    with patch.multiple(
        target=dev.db,
        get_from_db=Mock(return_value=db_data),
    ):
        df = get_db_data()
```
