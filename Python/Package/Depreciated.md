# Depreciated

## future warning
identify future warning
```
# test_file.py
import pytest
pytestmark = pytest.mark.filterwarnings("error::FutureWarning")

def test_my_func():
  assert 1==0  
```
Then run the test on terminal `pytest test_file.py > test.log`, and check the logs.
