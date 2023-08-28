# caplog

https://docs.pytest.org/en/6.2.x/reference.html#caplog

Access and control log capturing. Returns a `pytest.LogCaptureFixtur`e instance.

The `caplog` is one of pytest's built-in fixtures. 
The `fixture` is an argument that will be automatically passed to the test function by its name. 
Thus all we need to do is to define caplog as the function's argument and then use it in the method.

Here we test the logger using the `caplog`. So the log messgaes are written to caplog and we can check the messages later.
```py
import logging
from pytest import LogCaptureFixture

def test_logger(caplog: LogCaptureFixture) -> None:
    caplog.set_level(logging.INFO, logger=__name__)
    logger = logging.getLogger(__name__)

    logger.info('Test info.')
    logger.critical('Test error!', exc_info=1)

    assert 'Test info.' in caplog.text
    assert 'Test error!' in caplog.text
```
