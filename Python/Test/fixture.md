# fixture

## data path fixture
```py
import pytest
from pathlib import Path

DATA_PATH = Path(__file__).absolute().parent.joinpath('data')

@pytest.fixture
def data_path():
    return DATA_PATH

def test_data_path(data_path: Path):
    ...
```
